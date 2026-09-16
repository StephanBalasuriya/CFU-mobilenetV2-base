#!/usr/bin/env python3
"""
MobileNetV3 Minimalistic CPU Benchmark Runner (Standalone Codebase)

Loads the exported MobileNetV3 Minimalistic TFLite model, initializes the standard
TensorFlow Lite Interpreter on CPU, runs multiple inference iterations, and prints
detailed latency metrics and classification outputs. Completely standalone.
"""

import os
import sys
import time

try:
    import numpy as np
except ImportError:
    print("Error: numpy is required. Install via: pip install numpy")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow (PIL) is required. Install via: pip install pillow")
    sys.exit(1)

try:
    import tensorflow as tf
    Interpreter = tf.lite.Interpreter
except ImportError:
    try:
        from tflite_runtime.interpreter import Interpreter
    except ImportError:
        print("Error: tensorflow or tflite_runtime is required. Install via: pip install tflite-runtime")
        sys.exit(1)


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "model_mobilenetv3_small_min.tflite")
IMAGE_PATH = os.path.join(SCRIPT_DIR, "my_cat.jpg")
LABELS_PATH = os.path.join(SCRIPT_DIR, "labels.txt")

WARMUP_RUNS = 5
BENCHMARK_RUNS = 20


def load_labels():
    if not os.path.exists(LABELS_PATH):
        return None
    with open(LABELS_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def run_standalone_benchmark():
    print("==========================================================")
    print(" MobileNetV3 Minimalistic CPU Benchmark & Classifier")
    print("==========================================================")

    # Auto-generate TFLite model if not yet present
    if not os.path.exists(MODEL_PATH):
        print(f"Model file '{MODEL_PATH}' not found. Generating default model...")
        from export_model import export_mobilenetv3_minimalistic
        export_mobilenetv3_minimalistic(variant="small", quantize=False, output_path=MODEL_PATH)

    print(f"TFLite Model File  : {MODEL_PATH}")
    print(f"Model Size         : {os.path.getsize(MODEL_PATH) / (1024 * 1024):.2f} MB")
    print(f"Test Input Image   : {IMAGE_PATH}")

    # Initialize TFLite Interpreter
    try:
        interpreter = Interpreter(model_path=MODEL_PATH, experimental_delegates=[])
    except TypeError:
        interpreter = Interpreter(model_path=MODEL_PATH)

    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    input_dtype = input_details[0]['dtype']
    output_shape = output_details[0]['shape']
    output_dtype = output_details[0]['dtype']

    print("----------------------------------------------------------")
    print(f"Input Tensor Shape  : {input_shape} ({input_dtype.__name__})")
    print(f"Output Tensor Shape : {output_shape} ({output_dtype.__name__})")
    print("----------------------------------------------------------")

    # Load and preprocess input image
    if os.path.exists(IMAGE_PATH):
        img = Image.open(IMAGE_PATH).convert("RGB")
        img_resized = img.resize((input_shape[2], input_shape[1]), Image.Resampling.LANCZOS)
        img_array = np.array(img_resized, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)

        # Scale input
        if hasattr(tf, "keras") and hasattr(tf.keras.applications, "mobilenet_v3"):
            input_tensor = tf.keras.applications.mobilenet_v3.preprocess_input(img_array)
        else:
            input_tensor = img_array
    else:
        print("Warning: Sample image missing. Using random input tensor.")
        input_tensor = np.random.uniform(0.0, 255.0, input_shape).astype(np.float32)

    if input_dtype == np.uint8:
        input_tensor = np.clip(input_tensor, 0, 255).astype(np.uint8)
    elif input_dtype == np.int8:
        input_tensor = np.clip(input_tensor - 128, -128, 127).astype(np.int8)
    else:
        input_tensor = input_tensor.astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_tensor)

    # 1. Warm-up
    for _ in range(WARMUP_RUNS):
        interpreter.invoke()

    # 2. Benchmark Iterations
    latencies = []
    for _ in range(BENCHMARK_RUNS):
        start = time.perf_counter()
        interpreter.invoke()
        end = time.perf_counter()
        latencies.append((end - start) * 1000.0)

    avg_latency = np.mean(latencies)
    min_latency = np.min(latencies)
    max_latency = np.max(latencies)

    # Extract Top Prediction
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    if output_data.dtype != np.float32:
        scale, zero_point = output_details[0]['quantization']
        if scale > 0:
            output_data = (output_data.astype(np.float32) - zero_point) * scale

    exp_preds = np.exp(output_data - np.max(output_data))
    probs = exp_preds / np.sum(exp_preds)

    labels = load_labels()
    top_idx = int(np.argmax(probs))
    top_confidence = probs[top_idx] * 100.0
    top_label = labels[top_idx] if labels and top_idx < len(labels) else f"Class #{top_idx}"

    print(f"Benchmark Results ({BENCHMARK_RUNS} runs):")
    print(f"  Average CPU Latency : {avg_latency:.2f} ms")
    print(f"  Minimum CPU Latency : {min_latency:.2f} ms")
    print(f"  Maximum CPU Latency : {max_latency:.2f} ms")
    print("----------------------------------------------------------")
    print(f"Top Prediction        : {top_label} ({top_confidence:.2f}%)")
    print("==========================================================")


if __name__ == "__main__":
    run_standalone_benchmark()
