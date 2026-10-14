#!/usr/bin/env python3
"""
percentile_calibrate.py -- repair the int8 accuracy of a Keras-MobileNetV3-small TFLite model (full variant: 5x5, hard-swish,
squeeze-and-excite) by choosing every activation range from a PERCENTILE of real float activations.

Why: int8 PTQ of this network is very lossy with the converter's min/max ranges.  Its activations have outliers (|x| up to
~100 with a typical spread of ~6) and the depthwise layers amplify the resulting rounding noise.  Clipping each tensor at a high
percentile gives much finer steps for the bulk of the values.  Measured on 666 held-out ImageNet photos: float 67.9% top-1,
converter min/max int8 15.3%, this tool (99.97%) 50.9%.

Pipeline (needs tensorflow, tflite, ai-edge-litert, pillow, numpy):
  1. read the int8 weights of --int8 and rebuild the float network (tools/requantize_from_int8.py),
  2. convert it to a float TFLite model (reference activations) and to an int8 TFLite model (same structure),
  3. run the float model over the calibration images and collect every operator output,
  4. rewrite the int8 model's per-tensor scales/zero points from the chosen percentile and re-derive each conv bias
     (int32 bias = float bias / (input scale x weight scale)).  Weights are unchanged.

    python3 percentile_calibrate.py --int8 old.tflite --images photos_or_array.npy --out new.tflite [--pct 99.97]

--images: folder of 200+ diverse photos, or .npy uint8 [N,224,224,3] (squashed 224x224, raw 0..255).
Keep --pct between about 99.95 and 99.99: 99.9 and below, and 99.9999, collapse the accuracy.
"""
import argparse, os, sys, tempfile
import numpy as np
import tflite
import tensorflow as tf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requantize_from_int8 as rq
from ai_edge_litert.interpreter import Interpreter, OpResolverType


def convert(model, imgs, quant):
    conv = tf.lite.TFLiteConverter.from_keras_model(model)
    if quant:
        conv.optimizations = [tf.lite.Optimize.DEFAULT]
        conv.representative_dataset = lambda: ([im.astype(np.float32)[None]] for im in imgs)
        conv.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        conv.inference_input_type = tf.int8
        conv.inference_output_type = tf.int8
    return conv.convert()


def collect_stats(float_bytes, imgs, per_tensor=20000):
    path = tempfile.mktemp(suffix=".tflite"); open(path, "wb").write(float_bytes)
    it = Interpreter(model_path=path, experimental_op_resolver_type=OpResolverType.BUILTIN_REF,
                     experimental_preserve_all_tensors=True)
    it.allocate_tensors()
    m = tflite.Model.GetRootAsModel(float_bytes, 0); g = m.Subgraphs(0)
    outs = [g.Operators(i).Outputs(0) for i in range(g.OperatorsLength())]
    samples = [[] for _ in outs]; rng = np.random.default_rng(0)
    for im in imgs:
        it.set_tensor(it.get_input_details()[0]["index"], im.astype(np.float32)[None]); it.invoke()
        for j, t in enumerate(outs):
            a = it.get_tensor(t)
            if a.dtype == np.float32 and a.size > 1:
                f = a.reshape(-1)
                samples[j].append(f[rng.integers(0, f.size, per_tensor)] if f.size > per_tensor else f.copy())
    os.remove(path)
    return [np.concatenate(s) if s else None for s in samples]


def apply_percentiles(int8_bytes, stats, pct):
    buf = bytearray(int8_bytes)
    m = tflite.Model.GetRootAsModel(buf, 0); g = m.Subgraphs(0)
    names = {v: k for k, v in vars(tflite.BuiltinOperator).items() if not k.startswith("_")}
    codes = [max(m.OperatorCodes(i).BuiltinCode(), m.OperatorCodes(i).DeprecatedBuiltinCode()) for i in range(m.OperatorCodesLength())]
    kind = lambda op: names[codes[op.OpcodeIndex()]]
    n = g.OperatorsLength()
    new = {}
    for j in range(n):
        op = g.Operators(j); k = kind(op); t = op.Outputs(0)
        if k in ("CONV_2D", "DEPTHWISE_CONV_2D", "HARD_SWISH", "ADD", "MUL", "MEAN") and stats[j] is not None and g.Tensors(t).Type() == 9:
            s = stats[j]; lo = np.percentile(s, 100 - pct); hi = np.percentile(s, pct)
            relu = False
            if k in ("CONV_2D", "DEPTHWISE_CONV_2D"):
                o = tflite.Conv2DOptions() if k == "CONV_2D" else tflite.DepthwiseConv2DOptions()
                o.Init(op.BuiltinOptions().Bytes, op.BuiltinOptions().Pos)
                act = o.FusedActivationFunction()
                relu = act in (1, 3)                                  # RELU / RELU6
                if act == 3: hi = min(hi, 6.0)
            if relu: lo = 0.0
            lo = min(lo, 0.0); hi = max(hi, 1e-6)
            sc = (hi - lo) / 255.0
            zp = max(-128, min(127, int(round(-128 - lo / sc))))
            new[t] = (sc, zp)
    for j in range(n):                                                # reshape-like ops share their input's parameters
        op = g.Operators(j)
        if kind(op) in ("RESHAPE", "SQUEEZE", "EXPAND_DIMS") and op.Inputs(0) in new:
            new[op.Outputs(0)] = new[op.Inputs(0)]
    old = {}
    for t in range(g.TensorsLength()):
        q = g.Tensors(t).Quantization()
        if g.Tensors(t).Type() == 9 and q is not None and q.ScaleLength() == 1:
            old[t] = (q.Scale(0), q.ZeroPoint(0))
    for j in range(n):                                                # biases first: they need the OLD input scale
        op = g.Operators(j)
        if kind(op) in ("CONV_2D", "DEPTHWISE_CONV_2D"):
            tin, tw, tb = op.Inputs(0), op.Inputs(1), op.Inputs(2)
            s_old = old[tin][0]; s_new = new.get(tin, old[tin])[0]
            ws = g.Tensors(tw).Quantization().ScaleAsNumpy().astype(np.float64)
            B = g.Tensors(tb); bq = m.Buffers(B.Buffer()).DataAsNumpy().view(np.int32)
            bf = bq.astype(np.float64) * s_old * ws
            bq[:] = np.clip(np.round(bf / (s_new * ws)), -2**31 + 1, 2**31 - 1).astype(np.int32)
            B.Quantization().ScaleAsNumpy()[:] = (s_new * ws).astype(np.float32)
    for t, (sc, zp) in new.items():
        q = g.Tensors(t).Quantization()
        np.frombuffer(buf, dtype=np.float32, count=1, offset=q._tab.Vector(q._tab.Offset(8)))[0] = sc
        np.frombuffer(buf, dtype=np.int64, count=1, offset=q._tab.Vector(q._tab.Offset(10)))[0] = zp
    return bytes(buf), len(new)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--int8", required=True); ap.add_argument("--images", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--pct", type=float, default=99.97)
    ap.add_argument("--alpha", type=float, default=0.75); ap.add_argument("--minimalistic", action="store_true")
    ap.add_argument("--n", type=int, default=250, help="calibration images (default 250)")
    a = ap.parse_args()
    if not 99.9 < a.pct < 99.999:
        sys.exit("--pct should be between 99.9 and 99.999 (about 99.95-99.99 works best)")
    imgs = rq.load_images(a.images, a.n)
    print("calibration images:", len(imgs))
    model = rq.build_float_model(a.int8, a.alpha, a.minimalistic)
    print("converting float and int8 models ...", flush=True)
    fl = convert(model, imgs, False); q8 = convert(model, imgs, True)
    print("collecting float activation statistics ...", flush=True)
    stats = collect_stats(fl, imgs)
    out, k = apply_percentiles(q8, stats, a.pct)
    open(a.out, "wb").write(out)
    print("wrote %s  (percentile %.3f applied to %d tensors)" % (a.out, a.pct, k))


if __name__ == "__main__":
    main()
