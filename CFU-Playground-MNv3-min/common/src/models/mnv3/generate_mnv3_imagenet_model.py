#!/usr/bin/env python3
"""
generate_mnv3_imagenet_model.py
================================
Exports MobileNetV3-Small Minimalistic with pre-trained ImageNet weights
to a full INT8 quantized TFLite flatbuffer compatible with CFU-Playground firmware.

Model properties:
  - Architecture : MobileNetV3Small (minimalistic=True)
  - Weights      : imagenet (1000 classes)
  - Input        : 224x224x3 INT8 (zero_point & scale from quantization)
  - Output       : INT8 logits, 1000 classes
  - Activation   : ReLU6 (no h-swish, no SE blocks)

Output files:
  model_mobilenetv3_imagenet_224_1000.tflite  — INT8 TFLite flatbuffer
"""

import os
import sys
import time
import numpy as np

try:
    import tensorflow as tf
except ImportError:
    print("Error: tensorflow is required.")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_TFLITE = os.path.join(SCRIPT_DIR, "model_mobilenetv3_imagenet_224_1000.tflite")

INPUT_SHAPE  = (224, 224, 3)
NUM_CLASSES  = 1000
NUM_CAL_IMGS = 200   # calibration images for representative dataset


def representative_dataset_gen():
    """
    Synthetic representative dataset for post-training INT8 quantisation.
    MobileNetV3 Keras preprocessing maps [0,255] -> [-1, 1].
    We simulate realistic normalised images.
    """
    rng = np.random.default_rng(42)
    for _ in range(NUM_CAL_IMGS):
        # Simulate images in [0, 255] uint8, then apply MNv3 preprocessing:
        # preprocess_input(x) = x / 127.5 - 1.0
        raw = rng.integers(0, 256, size=(1, *INPUT_SHAPE), dtype=np.uint8).astype(np.float32)
        preprocessed = tf.keras.applications.mobilenet_v3.preprocess_input(raw)
        yield [preprocessed]


def main():
    print("=" * 65)
    print("  Generating MobileNetV3-Small Minimalistic (ImageNet, INT8)")
    print("=" * 65)
    print(f"  Input shape : {INPUT_SHAPE}")
    print(f"  Classes     : {NUM_CLASSES}")
    print(f"  Output path : {OUTPUT_TFLITE}")
    print()

    # 1. Build Keras model with ImageNet weights
    print("[1/4] Loading MobileNetV3Small (minimalistic=True, weights='imagenet')...")
    t0 = time.time()
    model = tf.keras.applications.MobileNetV3Small(
        input_shape=INPUT_SHAPE,
        alpha=1.0,            # full-width: best accuracy for ImageNet
        minimalistic=True,    # no SE blocks, ReLU6 activations
        include_top=True,
        weights="imagenet",   # pre-trained weights
        classes=NUM_CLASSES,
        classifier_activation="softmax",
    )
    print(f"    Loaded in {time.time()-t0:.1f}s — {model.count_params():,} parameters")

    # 2. Convert to TFLite with full INT8 quantisation
    print("\n[2/4] Converting to INT8 TFLite (full quantisation)...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.representative_dataset = representative_dataset_gen
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type  = tf.int8
    converter.inference_output_type = tf.int8

    tflite_model = converter.convert()
    print(f"    Conversion done — {len(tflite_model):,} bytes ({len(tflite_model)/1024/1024:.2f} MB)")

    # 3. Save .tflite
    print("\n[3/4] Saving TFLite flatbuffer...")
    with open(OUTPUT_TFLITE, "wb") as f:
        f.write(tflite_model)
    print(f"    Saved: {OUTPUT_TFLITE}")

    # 4. Verify quantisation parameters
    print("\n[4/4] Verifying quantisation parameters...")
    interp = tf.lite.Interpreter(model_content=tflite_model)
    interp.allocate_tensors()
    inp = interp.get_input_details()[0]
    out = interp.get_output_details()[0]
    print(f"    Input  dtype={inp['dtype'].__name__}  shape={inp['shape']}  "
          f"scale={inp['quantization'][0]:.6f}  zero_point={inp['quantization'][1]}")
    print(f"    Output dtype={out['dtype'].__name__}  shape={out['shape']}  "
          f"scale={out['quantization'][0]:.6f}  zero_point={out['quantization'][1]}")

    # 5. Generate Golden Test Vector (.dat) for 224x224x3
    print("\n[5/5] Generating golden test vector (input_00001.dat)...")
    dat_path = os.path.join(SCRIPT_DIR, "input_00001.dat")
    sample_input = np.random.randint(-128, 127, size=inp['shape'], dtype=np.int8)
    sample_input.tofile(dat_path)
    print(f"    Saved golden test vector: {dat_path} ({os.path.getsize(dat_path):,} bytes)")

    print("\n" + "=" * 65)
    print("  DONE — run scripts/convert_mnv3_model.sh to generate .h")
    print("=" * 65)


if __name__ == "__main__":
    main()
