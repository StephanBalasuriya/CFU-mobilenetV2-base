#!/usr/bin/env python3
"""
MobileNetV3 Minimalistic Model Generator & TFLite Exporter

Exports MobileNetV3 Small and Large Minimalistic models (with or without ImageNet weights)
to TensorFlow Lite (.tflite) format. Supports float32 and INT8 quantization modes.

MobileNetV3 Minimalistic features:
- Removes Squeeze-and-Excitation (SE) blocks.
- Replaces Hard-Swish / Hard-Sigmoid activations with standard ReLU / ReLU6.
- Optimized for lightweight embedded CPUs and microcontrollers.
"""

import os
import sys
import argparse
import time

try:
    import numpy as np
except ImportError:
    print("Error: numpy is required. Install via: pip install numpy")
    sys.exit(1)

try:
    import tensorflow as tf
except ImportError:
    print("Error: tensorflow is required. Install via: pip install tensorflow")
    sys.exit(1)


def representative_dataset_gen():
    """Generates synthetic representative dataset for post-training INT8 quantization."""
    for _ in range(100):
        # MobileNetV3 expects normalized input images [-1.0, 1.0] or [0.0, 255.0] depending on preprocessing
        # For MobilenetV3 in Keras, preprocessing expects values in [0, 255] or scaling by 1/255
        data = np.random.uniform(0.0, 255.0, (1, 224, 224, 3)).astype(np.float32)
        yield [data]


def export_mobilenetv3_minimalistic(variant="small", weights="imagenet", quantize=False, output_path=None):
    """
    Exports MobileNetV3 Minimalistic model to TFLite format.
    
    Args:
        variant (str): 'small' or 'large'
        weights (str): 'imagenet' or None
        quantize (bool): If True, applies INT8 dynamic range / post-training quantization
        output_path (str): File path for saving the .tflite model
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if output_path is None:
        q_suffix = "_int8" if quantize else ""
        output_path = os.path.join(script_dir, f"model_mobilenetv3_{variant}_min{q_suffix}.tflite")

    print("==========================================================")
    print(f" Exporting MobileNetV3 {variant.capitalize()} Minimalistic Model")
    print("==========================================================")
    print(f"Variant     : MobileNetV3-{variant.capitalize()} (Minimalistic)")
    print(f"Weights     : {weights}")
    print(f"Quantized   : {quantize}")
    print(f"Target Path : {output_path}")

    start_time = time.time()

    # 1. Build Keras Model
    print("\nBuilding Keras Model...")
    if variant.lower() == "large":
        model = tf.keras.applications.MobileNetV3Large(
            input_shape=(224, 224, 3),
            weights=weights,
            minimalistic=True,
            classes=1000
        )
    else:
        model = tf.keras.applications.MobileNetV3Small(
            input_shape=(224, 224, 3),
            weights=weights,
            minimalistic=True,
            classes=1000
        )

    print(f"Model Name  : {model.name}")
    print(f"Total Layers: {len(model.layers)}")
    print(f"Total Params: {model.count_params():,}")

    # 2. Convert to TFLite
    print("\nConverting to TensorFlow Lite...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    if quantize:
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        # Optional INT8 representative dataset
        converter.representative_dataset = representative_dataset_gen
        print("Applied INT8 post-training quantization optimization.")

    tflite_model = converter.convert()

    # 3. Save to disk
    with open(output_path, "wb") as f:
        f.write(tflite_model)

    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    elapsed_sec = time.time() - start_time

    print("----------------------------------------------------------")
    print(f"SUCCESS: Exported TFLite Model to: {output_path}")
    print(f"File Size   : {file_size_mb:.2f} MB ({len(tflite_model):,} bytes)")
    print(f"Export Time : {elapsed_sec:.2f} seconds")
    print("==========================================================")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="MobileNetV3 Minimalistic Model Generator & TFLite Exporter")
    parser.add_argument("--variant", choices=["small", "large"], default="small", help="MobileNetV3 variant (small/large)")
    parser.add_argument("--no-weights", action="store_true", help="Do not load pre-trained ImageNet weights")
    parser.add_argument("--quantize", action="store_true", help="Export INT8 quantized TFLite model")
    parser.add_argument("--output", type=str, default=None, help="Custom output .tflite file path")
    parser.add_argument("--export-all", action="store_true", help="Export both small and large minimalistic models (float & int8)")

    args = parser.parse_args()

    weights = None if args.no_weights else "imagenet"

    if args.export_all:
        print("Exporting all standard MobileNetV3 Minimalistic variants...")
        export_mobilenetv3_minimalistic("small", weights=weights, quantize=False)
        export_mobilenetv3_minimalistic("small", weights=weights, quantize=True)
        export_mobilenetv3_minimalistic("large", weights=weights, quantize=False)
        export_mobilenetv3_minimalistic("large", weights=weights, quantize=True)
    else:
        export_mobilenetv3_minimalistic(
            variant=args.variant,
            weights=weights,
            quantize=args.quantize,
            output_path=args.output
        )


if __name__ == "__main__":
    main()
