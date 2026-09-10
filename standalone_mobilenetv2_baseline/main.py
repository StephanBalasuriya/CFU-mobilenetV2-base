#!/usr/bin/env python3
"""
MobileNetV2 Baseline CPU Inference Script (Standalone - Outside CFU-Playground)

Runs MobileNetV2 quantized TFLite inference directly on the host CPU using standard
TensorFlow Lite Interpreter. Completely independent of LiteX, VexRiscv, and CFU Playground.
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
    import tensorflow as tf
    Interpreter = tf.lite.Interpreter
except ImportError:
    try:
        from tflite_runtime.interpreter import Interpreter
    except ImportError:
        print("Error: tensorflow or tflite_runtime is required. Install via: pip install tflite-runtime")
        sys.exit(1)


# Golden test inputs and their expected output[1] - output[0] score difference
GOLDEN_TESTS = [
    ("input_00001_7281.dat", -148),
    ("input_00001_7425.dat", 68),
    ("input_00002_2532.dat", -112),
    ("input_00002_25869.dat", 134),
    ("input_00004_970.dat", 128),
]


def run_standalone_baseline():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "model_mobilenetv2_160_035.tflite")
    inputs_dir = os.path.join(script_dir, "inputs")

    if not os.path.exists(model_path):
        print(f"Error: Model file not found at '{model_path}'")
        sys.exit(1)

    print("==========================================================")
    print(" MobileNetV2 Baseline CPU Runner (Standalone Codebase)")
    print("==========================================================")
    print(f"Loading TFLite Model: {model_path}")

    # Load TFLite Model onto Host CPU without delegates for exact reference integer ops
    try:
        interpreter = Interpreter(model_path=model_path, experimental_delegates=[])
    except TypeError:
        interpreter = Interpreter(model_path=model_path)

    interpreter.allocate_tensors()

    # Get input and output tensor details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    input_dtype = input_details[0]['dtype']
    output_dtype = output_details[0]['dtype']

    print(f"Input Tensor Shape : {input_shape} ({input_dtype})")
    print(f"Output Tensor Shape: {output_details[0]['shape']} ({output_dtype})")
    print("----------------------------------------------------------")

    # Run Golden Tests
    passed = 0
    total = len(GOLDEN_TESTS)

    for filename, expected_score in GOLDEN_TESTS:
        filepath = os.path.join(inputs_dir, filename)
        if not os.path.exists(filepath):
            print(f"[SKIP] Input file missing: {filename}")
            continue

        with open(filepath, "rb") as f:
            raw_data = f.read()

        # Input data is 160x160x3 uint8 array
        raw_uint8 = np.frombuffer(raw_data, dtype=np.uint8)

        # Convert unsigned uint8 [0..255] to signed int8 [-128..127] exactly like tflite_set_input_unsigned
        input_int8 = (raw_uint8.astype(np.int16) - 128).astype(np.int8).reshape(input_shape)

        interpreter.set_tensor(input_details[0]['index'], input_int8)

        # Benchmark Inference Time on CPU
        start_time = time.perf_counter()
        interpreter.invoke()
        end_time = time.perf_counter()

        latency_ms = (end_time - start_time) * 1000.0

        # Get output
        output_data = interpreter.get_tensor(output_details[0]['index'])[0]
        actual_score = int(output_data[1]) - int(output_data[0])

        status = "PASS" if actual_score == expected_score else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"Test {filename:20s} -> Output Score: {actual_score:4d} (Expected: {expected_score:4d}) | [{status}] | CPU Latency: {latency_ms:.3f} ms")

    print("----------------------------------------------------------")
    print(f"Golden Tests Completed: {passed}/{total} Passed")
    print("==========================================================")


if __name__ == "__main__":
    run_standalone_baseline()
