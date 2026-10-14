#!/usr/bin/env python3
"""
quantize_mobilenetv3_keras.py -- build a full-integer int8 MobileNetV3-small TFLite model with the converter's standard
min/max calibration.

NOTE: for the FULL MobileNetV3-small (hard-swish, squeeze-and-excite) this standard conversion is not enough: measured on held-out
ImageNet photos it gives only ~15% top-1 even with 334 real calibration photos (float: 68%).  Use tools/percentile_calibrate.py,
which reaches ~51%.  This script is kept for models that quantise well (e.g. the minimalistic variant: --minimalistic).

    python3 quantize_mobilenetv3_keras.py --images ~/calibration_photos --out mobilenetv3_small_full_int8.tflite

Why calibration matters: TFLite chooses the int8 range of every tensor from the values it sees while running the
representative images.  If those images are few or unlike real photos, ranges are too narrow, confident predictions are
clipped and the classifier outputs a flat, tied distribution (what tools/check_int8_model.py reports as SATURATED).

Use 200-500 DIVERSE real photos (an ImageNet validation subset is ideal; any varied photos work: animals, objects,
indoor/outdoor, different lighting).  Do NOT use random noise or a handful of similar pictures.

Preprocessing = the firmware's: image squashed to 224x224 (bilinear), raw 0..255 values; the model contains its own
rescaling (include_preprocessing=True), and the input is int8 with scale 1, zero point -128.

Needs: pip install tensorflow pillow numpy   (and internet the first time, for the pretrained ImageNet weights)
Afterwards: python3 check_int8_model.py <out.tflite> --labels imagenet_labels.txt some_photos...   and copy the model to model/.
"""
import argparse, glob, os, random, sys
import numpy as np
from PIL import Image
import tensorflow as tf

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--images", required=True, help="folder with calibration photos (jpg/png)")
    ap.add_argument("--out", default="mobilenetv3_small_full_int8.tflite")
    ap.add_argument("--alpha", type=float, default=0.75, help="width multiplier (0.75 = the model used so far, or 1.0)")
    ap.add_argument("--minimalistic", action="store_true", help="the minimalistic variant (3x3 only, no hard-swish / SE)")
    ap.add_argument("--n", type=int, default=300, help="number of calibration images to use (default 300)")
    ap.add_argument("--weights", default="imagenet", help="'imagenet' (default) or 'none' (random weights, for testing the flow)")
    a = ap.parse_args()

    files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
        files += glob.glob(os.path.join(a.images, "**", ext), recursive=True)
    files = sorted(set(files))
    random.Random(0).shuffle(files)
    files = files[:a.n]
    if len(files) < 50:
        print("WARNING: only %d calibration images found; use at least 100-200 diverse photos." % len(files))
    if not files:
        sys.exit("no images found in %s" % a.images)

    model = tf.keras.applications.MobileNetV3Small(
        input_shape=(224, 224, 3), alpha=a.alpha, minimalistic=a.minimalistic,
        weights=None if a.weights == "none" else "imagenet", include_preprocessing=True)

    def representative_data():
        for f in files:
            try:
                im = Image.open(f).convert("RGB").resize((224, 224), Image.BILINEAR)
            except Exception:
                continue
            yield [np.asarray(im, dtype=np.float32)[None]]            # raw 0..255, the model rescales itself

    conv = tf.lite.TFLiteConverter.from_keras_model(model)
    conv.optimizations = [tf.lite.Optimize.DEFAULT]
    conv.representative_dataset = representative_data
    conv.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    conv.inference_input_type = tf.int8
    conv.inference_output_type = tf.int8
    data = conv.convert()
    open(a.out, "wb").write(data)
    print("wrote %s (%d bytes) from %d calibration images" % (a.out, len(data), len(files)))
    it = tf.lite.Interpreter(model_path=a.out)
    it.allocate_tensors()
    i, o = it.get_input_details()[0], it.get_output_details()[0]
    print("input  %s %s quantization (scale, zero point) = %s" % (i["dtype"].__name__, [int(x) for x in i["shape"]], i["quantization"]))
    print("output %s %s quantization (scale, zero point) = %s" % (o["dtype"].__name__, [int(x) for x in o["shape"]], o["quantization"]))
    print("expected: input (1.0, -128) and output (0.00390625, -128). Now run tools/check_int8_model.py on the result.")

if __name__ == "__main__":
    main()
