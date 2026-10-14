#!/usr/bin/env python3
"""
requantize_from_int8.py -- re-calibrate an existing int8 Keras-MobileNetV3-small TFLite model WITHOUT the original float
weights.

Idea: the weights inside an int8 model are good (per-channel int8 weights lose little); what is often wrong is the
calibration of the ACTIVATION ranges (see tools/check_int8_model.py).  So this tool
  1. reads the int8 weights and biases and turns them back into float  (w = q * scale_per_channel,  b = q * in_scale * w_scale),
  2. loads them into a fresh Keras MobileNetV3Small (batch-norm is already folded into the conv weights, so each BN layer is set
     to an identity that only adds the folded bias),
  3. converts that float model to full-integer int8 again, now with a REPRESENTATIVE calibration set.
The result has the same structure as before (same fused CFU blocks) and the same input/output quantisation.

    python3 requantize_from_int8.py --int8 old.tflite --images ~/photos_or_array.npy --out new.tflite [--alpha 0.75]

--images: a folder of jpg/png photos (200-500 diverse ones) or a .npy file with uint8 images of shape [N,224,224,3].
Preprocessing as the firmware: image squashed to 224x224 (bilinear), raw 0..255 (the model rescales itself).
Needs: pip install tensorflow tflite flatbuffers pillow numpy
"""
import argparse, glob, os, random, sys
import numpy as np
import tflite
import tensorflow as tf
from PIL import Image


def load_weights(path):
    raw = open(path, "rb").read()
    m = tflite.Model.GetRootAsModel(raw, 0)
    g = m.Subgraphs(0)
    names = {v: k for k, v in vars(tflite.BuiltinOperator).items() if not k.startswith("_")}
    codes = [max(m.OperatorCodes(i).BuiltinCode(), m.OperatorCodes(i).DeprecatedBuiltinCode()) for i in range(m.OperatorCodesLength())]

    def tensor_data(t, dtype):
        T = g.Tensors(t)
        arr = m.Buffers(T.Buffer()).DataAsNumpy()
        return np.frombuffer(arr.tobytes(), dtype=dtype).reshape([int(x) for x in T.ShapeAsNumpy()])

    out = []
    for i in range(g.OperatorsLength()):
        op = g.Operators(i)
        kind = names[codes[op.OpcodeIndex()]]
        if kind not in ("CONV_2D", "DEPTHWISE_CONV_2D"):
            continue
        wq = tensor_data(op.Inputs(1), np.int8).astype(np.float32)
        qw = g.Tensors(op.Inputs(1)).Quantization()
        wscale = qw.ScaleAsNumpy().astype(np.float32)
        qdim = qw.QuantizedDimension()
        shape = [1] * wq.ndim
        shape[qdim] = -1
        w = wq * wscale.reshape(shape)                                   # per-channel dequantisation (zero point 0)
        bq = tensor_data(op.Inputs(2), np.int32).astype(np.float64)
        in_scale = g.Tensors(op.Inputs(0)).Quantization().Scale(0)
        b = (bq * in_scale * wscale.astype(np.float64)).astype(np.float32)
        if kind == "CONV_2D":
            w = np.transpose(w, (1, 2, 3, 0))                            # [O,kh,kw,I] -> [kh,kw,I,O]
        else:
            w = np.transpose(w, (1, 2, 3, 0))                            # [1,kh,kw,C] -> [kh,kw,C,1]
        out.append((i, kind, w, b))
    return out


def build_float_model(int8_path, alpha, minimalistic):
    model = tf.keras.applications.MobileNetV3Small(input_shape=(224, 224, 3), alpha=alpha, minimalistic=minimalistic,
                                                   weights=None, include_preprocessing=True)
    layers = [l for l in model.layers if isinstance(l, (tf.keras.layers.Conv2D, tf.keras.layers.DepthwiseConv2D))]
    wl = load_weights(int8_path)
    if len(wl) != len(layers):
        sys.exit("the int8 model has %d conv layers but MobileNetV3Small(alpha=%s) has %d: wrong --alpha / --minimalistic?"
                 % (len(wl), alpha, len(layers)))
    for (i, kind, w, b), l in zip(wl, layers):
        if list(l.kernel.shape) != list(w.shape):
            sys.exit("shape mismatch at op %d (%s): int8 %s vs Keras %s %s" % (i, kind, w.shape, l.name, l.kernel.shape))
        if l.name.endswith("squeeze_excite_conv_1"):
            b = b - 3.0            # the converter folded the '+ 3' of hard_sigmoid = relu6(x + 3) / 6 into this bias
        if l.use_bias:
            l.set_weights([w, b])
        else:
            l.set_weights([w])
            bn = model.get_layer(l.name + "_bn")                         # identity BN that adds the folded bias
            bn.set_weights([np.ones_like(b), b, np.zeros_like(b), np.full_like(b, 1.0 - bn.epsilon)])
    return model


def load_images(src, n):
    if src.endswith(".npy"):
        a = np.load(src)
        return a[:n]
    files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
        files += glob.glob(os.path.join(src, "**", ext), recursive=True)
    files = sorted(set(files))
    random.Random(0).shuffle(files)
    return np.stack([np.asarray(Image.open(f).convert("RGB").resize((224, 224), Image.BILINEAR)) for f in files[:n]])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--int8", required=True); ap.add_argument("--images", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--alpha", type=float, default=0.75); ap.add_argument("--minimalistic", action="store_true")
    ap.add_argument("--n", type=int, default=500, help="max calibration images")
    ap.add_argument("--save-float", help="also save the rebuilt float Keras model here (.keras)")
    a = ap.parse_args()
    imgs = load_images(a.images, a.n)
    if len(imgs) < 100:
        print("WARNING: only %d calibration images; use 200-500 diverse photos." % len(imgs))
    model = build_float_model(a.int8, a.alpha, a.minimalistic)
    if a.save_float:
        model.save(a.save_float)

    def representative():
        for im in imgs:
            yield [im.astype(np.float32)[None]]

    conv = tf.lite.TFLiteConverter.from_keras_model(model)
    conv.optimizations = [tf.lite.Optimize.DEFAULT]
    conv.representative_dataset = representative
    conv.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    conv.inference_input_type = tf.int8
    conv.inference_output_type = tf.int8
    data = conv.convert()
    open(a.out, "wb").write(data)
    print("wrote %s (%d bytes) calibrated on %d images" % (a.out, len(data), len(imgs)))


if __name__ == "__main__":
    main()
