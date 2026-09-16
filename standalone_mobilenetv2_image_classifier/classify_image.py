#!/usr/bin/env python3
"""
MobileNetV2 Standalone Profiler & Image Classifier

Measures model loading time, preprocessing time, complete model inference latency,
and per-layer timing for Conv2D / DepthwiseConv2D bottleneck operations (Expansion 1x1,
Depthwise 3x3, Projection 1x1). Exports detailed timing metrics to CSV.
"""

import os
import sys
import time
import csv

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
except ImportError:
    print("Error: tensorflow is required. Install via: pip install tensorflow")
    sys.exit(1)


# ============================================================
# CONFIGURATION & MEASUREMENT PARAMETERS
# ============================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_IMAGE = os.path.join(SCRIPT_DIR, "my_cat.jpg") if os.path.exists(os.path.join(SCRIPT_DIR, "my_cat.jpg")) else os.path.join(SCRIPT_DIR, "test_sample.jpg")

IMAGE_PATH = os.environ.get("IMAGE_PATH", DEFAULT_IMAGE if os.path.exists(DEFAULT_IMAGE) else "images/cat.jpg")
CSV_PATH = os.path.join(SCRIPT_DIR, "mobilenet_v2_timing.csv")

# Key Measurement Parameters
NUM_RUNS = 10         # Number of measurements for each operation (increase to 20-30 for higher stability)
WARMUP_RUNS = 5       # Number of warm-up executions before timing full model
LAYER_WARMUP_RUNS = 3 # Number of warm-up executions before timing individual layers


# ============================================================
# HELPER FUNCTION
# ============================================================

def measure_model(model_to_measure, input_tensor, runs=NUM_RUNS, warmup=LAYER_WARMUP_RUNS):
    """
    Measure the execution time of a Keras model over multiple runs.

    A few warm-up runs are performed first because TensorFlow
    may perform initialization on the first execution.
    """
    # Warm-up
    for _ in range(warmup):
        output = model_to_measure(input_tensor, training=False)
        if isinstance(output, (tf.Tensor, tf.Variable)):
            output.numpy()

    times = []
    for _ in range(runs):
        start = time.perf_counter()
        output = model_to_measure(input_tensor, training=False)
        # Force TensorFlow execution completion
        if isinstance(output, (tf.Tensor, tf.Variable)):
            output.numpy()
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000.0
        times.append(elapsed_ms)

    return {
        "average": np.mean(times),
        "minimum": np.min(times),
        "maximum": np.max(times)
    }


def main():
    global IMAGE_PATH

    # Allow command line argument for image path if provided
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        IMAGE_PATH = sys.argv[1]

    # ============================================================
    # 1. LOAD MODEL
    # ============================================================
    print("=" * 90)
    print("LOADING MOBILENETV2")
    print("=" * 90)

    model_start = time.perf_counter()
    model = tf.keras.applications.MobileNetV2(
        weights="imagenet"
    )
    model_end = time.perf_counter()
    model_loading_time = model_end - model_start

    print(f"Model loading time: {model_loading_time * 1000:.2f} ms")


    # ============================================================
    # 2. LOAD IMAGE
    # ============================================================
    print("\n" + "=" * 90)
    print("LOADING IMAGE")
    print("=" * 90)
    print(f"Image: {IMAGE_PATH}")

    if not os.path.exists(IMAGE_PATH):
        print(f"Warning: Image '{IMAGE_PATH}' not found. Searching in script directory...")
        fallback = os.path.join(SCRIPT_DIR, os.path.basename(IMAGE_PATH))
        if os.path.exists(fallback):
            IMAGE_PATH = fallback
        elif os.path.exists(DEFAULT_IMAGE):
            IMAGE_PATH = DEFAULT_IMAGE
        else:
            print(f"Error: Cannot locate valid image file at '{IMAGE_PATH}'.")
            sys.exit(1)
        print(f"Using image: {IMAGE_PATH}")

    image = Image.open(IMAGE_PATH).convert("RGB")
    print(f"Original image size: {image.size}")


    # ============================================================
    # 3. PREPROCESS IMAGE
    # ============================================================
    preprocess_start = time.perf_counter()

    image_resized = image.resize((224, 224))
    image_array = np.array(image_resized, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
    x = tf.convert_to_tensor(image_array, dtype=tf.float32)

    preprocess_end = time.perf_counter()
    preprocess_time = preprocess_end - preprocess_start

    print(f"Preprocessing time: {preprocess_time * 1000:.2f} ms")


    # ============================================================
    # 4. WARM UP COMPLETE MODEL
    # ============================================================
    print("\n" + "=" * 90)
    print("WARMING UP COMPLETE MODEL")
    print("=" * 90)

    for _ in range(WARMUP_RUNS):
        output = model(x, training=False)
        output.numpy()

    print(f"Warm-up completed ({WARMUP_RUNS} iterations).")


    # ============================================================
    # 5. NORMAL MOBILENETV2 INFERENCE
    # ============================================================
    print("\n" + "=" * 90)
    print("NORMAL MOBILENETV2 INFERENCE")
    print("=" * 90)

    normal_times = []
    for _ in range(NUM_RUNS):
        start = time.perf_counter()
        predictions = model(x, training=False)
        predictions.numpy()
        end = time.perf_counter()
        normal_times.append((end - start) * 1000.0)

    normal_average = np.mean(normal_times)
    normal_min = np.min(normal_times)
    normal_max = np.max(normal_times)

    print(f"Average inference time : {normal_average:.2f} ms")
    print(f"Minimum inference time : {normal_min:.2f} ms")
    print(f"Maximum inference time : {normal_max:.2f} ms")


    # ============================================================
    # 6. PREDICTION
    # ============================================================
    predictions = model(x, training=False)
    predictions_numpy = predictions.numpy()

    results = tf.keras.applications.mobilenet_v2.decode_predictions(
        predictions_numpy, top=5
    )[0]

    print("\n" + "=" * 90)
    print("TOP 5 PREDICTIONS")
    print("=" * 90 + "\n")

    for _, label, probability in results:
        print(f"{label:30s}{probability * 100:8.2f}%")


    # ============================================================
    # 7. LIST ALL CONVOLUTION LAYERS
    # ============================================================
    print("\n" + "=" * 90)
    print("FINDING CONVOLUTION LAYERS")
    print("=" * 90)

    conv_layers = [l for l in model.layers if isinstance(l, tf.keras.layers.Conv2D)]
    print(f"\nFound {len(conv_layers)} Conv2D layers.")


    # ============================================================
    # 8. LIST DEPTHWISE LAYERS
    # ============================================================
    depthwise_layers = [l for l in model.layers if isinstance(l, tf.keras.layers.DepthwiseConv2D)]
    print(f"Found {len(depthwise_layers)} DepthwiseConv2D layers.")


    # ============================================================
    # 9. DISPLAY CONVOLUTION STRUCTURE
    # ============================================================
    print("\n" + "=" * 90)
    print("MOBILENETV2 CONVOLUTION STRUCTURE")
    print("=" * 90 + "\n")

    print(f"{'Layer':45s}{'Type':25s}{'Kernel':15s}{'Filters':10s}")
    print("-" * 95)

    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Conv2D):
            kernel = layer.kernel_size
            filters = layer.filters
            print(f"{layer.name:45s}{'Conv2D':25s}{str(kernel):15s}{str(filters):10s}")
        elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
            kernel = layer.kernel_size
            print(f"{layer.name:45s}{'DepthwiseConv2D':25s}{str(kernel):15s}{'depthwise':10s}")


    # ============================================================
    # 10. PROFILE CONVOLUTION LAYERS
    # ============================================================
    print("\n" + "=" * 90)
    print("PROFILING CONVOLUTION LAYERS")
    print("=" * 90 + "\n")

    timing_results = []

    for layer in model.layers:
        is_conv = isinstance(layer, tf.keras.layers.Conv2D)
        is_depthwise = isinstance(layer, tf.keras.layers.DepthwiseConv2D)

        if not (is_conv or is_depthwise):
            continue

        try:
            layer_input = layer.input
            layer_output = layer.output
        except Exception as e:
            print(f"Skipping {layer.name}: cannot access graph tensors.")
            continue

        try:
            layer_model = tf.keras.Model(inputs=layer_input, outputs=layer_output)
        except Exception as e:
            print(f"Skipping {layer.name}: cannot create profiling model.")
            continue

        try:
            prefix_model = tf.keras.Model(inputs=model.input, outputs=layer_input)
            layer_input_value = prefix_model(x, training=False)
        except Exception as e:
            print(f"Skipping {layer.name}: cannot generate layer input.")
            continue

        result = measure_model(layer_model, layer_input_value, runs=NUM_RUNS, warmup=LAYER_WARMUP_RUNS)

        if is_depthwise:
            operation = "Depthwise 3x3"
        else:
            name = layer.name.lower()
            if "expand" in name:
                operation = "Expansion 1x1"
            elif "project" in name:
                operation = "Projection 1x1"
            else:
                operation = "Other Conv2D"

        timing_results.append({
            "layer": layer.name,
            "type": layer.__class__.__name__,
            "operation": operation,
            "average_ms": result["average"],
            "minimum_ms": result["minimum"],
            "maximum_ms": result["maximum"]
        })


    # ============================================================
    # 11. PRINT TIMING RESULTS
    # ============================================================
    print("\n" + "=" * 110)
    print("CONVOLUTION TIMING RESULTS")
    print("=" * 110 + "\n")

    print(f"{'Layer':40s}{'Operation':22s}{'Average (ms)':15s}{'Min (ms)':15s}{'Max (ms)':15s}")
    print("-" * 110)

    for result in timing_results:
        print(
            f"{result['layer']:40s}"
            f"{result['operation']:22s}"
            f"{result['average_ms']:15.4f}"
            f"{result['minimum_ms']:15.4f}"
            f"{result['maximum_ms']:15.4f}"
        )


    # ============================================================
    # 12. CALCULATE OPERATION TOTALS
    # ============================================================
    expansion_total = 0.0
    depthwise_total = 0.0
    projection_total = 0.0
    other_conv_total = 0.0

    for result in timing_results:
        operation = result["operation"]
        time_ms = result["average_ms"]

        if operation == "Expansion 1x1":
            expansion_total += time_ms
        elif operation == "Depthwise 3x3":
            depthwise_total += time_ms
        elif operation == "Projection 1x1":
            projection_total += time_ms
        elif operation == "Other Conv2D":
            other_conv_total += time_ms

    bottleneck_total = expansion_total + depthwise_total + projection_total


    # ============================================================
    # 13. OPERATION SUMMARY
    # ============================================================
    print("\n" + "=" * 90)
    print("MOBILENETV2 OPERATION SUMMARY")
    print("=" * 90 + "\n")

    print(f"Expansion 1x1 total     : {expansion_total:.4f} ms")
    print(f"Depthwise 3x3 total     : {depthwise_total:.4f} ms")
    print(f"Projection 1x1 total    : {projection_total:.4f} ms")
    print(f"Other Conv2D total      : {other_conv_total:.4f} ms")
    print("------------------------------------------")
    print(f"Total bottleneck conv   : {bottleneck_total:.4f} ms")


    # ============================================================
    # 14. TIME CONTRIBUTION
    # ============================================================
    print("\n" + "=" * 90)
    print("TIME CONTRIBUTION")
    print("=" * 90 + "\n")

    if normal_average > 0:
        expansion_percentage = (expansion_total / normal_average) * 100
        depthwise_percentage = (depthwise_total / normal_average) * 100
        projection_percentage = (projection_total / normal_average) * 100
        bottleneck_percentage = (bottleneck_total / normal_average) * 100

        print(f"Expansion 1x1      : {expansion_percentage:.2f}%")
        print(f"Depthwise 3x3      : {depthwise_percentage:.2f}%")
        print(f"Projection 1x1     : {projection_percentage:.2f}%")
        print(f"All bottlenecks    : {bottleneck_percentage:.2f}%")


    # ============================================================
    # 15. SAVE CSV
    # ============================================================
    print("\n" + "=" * 90)
    print("SAVING RESULTS")
    print("=" * 90)

    with open(CSV_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Layer", "Type", "Operation", "Average_ms", "Minimum_ms", "Maximum_ms"])
        for result in timing_results:
            writer.writerow([
                result["layer"],
                result["type"],
                result["operation"],
                result["average_ms"],
                result["minimum_ms"],
                result["maximum_ms"]
            ])

    print(f"Saved timing results to: {CSV_PATH}")


    # ============================================================
    # 16. FINAL SUMMARY
    # ============================================================
    print("\n" + "=" * 90)
    print("FINAL SUMMARY")
    print("=" * 90 + "\n")

    print(f"{'Model loading':35s}: {model_loading_time * 1000:.2f} ms")
    print(f"{'Image preprocessing':35s}: {preprocess_time * 1000:.2f} ms")
    print(f"{'MobileNetV2 inference (average)':35s}: {normal_average:.2f} ms")
    print(f"{'MobileNetV2 inference (minimum)':35s}: {normal_min:.2f} ms")
    print(f"{'MobileNetV2 inference (maximum)':35s}: {normal_max:.2f} ms")
    print()
    print(f"{'Expansion 1x1':35s}: {expansion_total:.4f} ms")
    print(f"{'Depthwise 3x3':35s}: {depthwise_total:.4f} ms")
    print(f"{'Projection 1x1':35s}: {projection_total:.4f} ms")
    print(f"{'Bottleneck operations':35s}: {bottleneck_total:.4f} ms")

    print("\n" + "=" * 90)
    print("DONE")
    print("=" * 90)


if __name__ == "__main__":
    main()
