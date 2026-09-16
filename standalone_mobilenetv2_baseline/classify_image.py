#!/usr/bin/env python3
"""
Image Classifier for MobileNetV2 Standalone CPU Baseline

Classifies image files (e.g. cat.jpg, dog.png) using MobileNetV2.
Predicts image categories (1000 ImageNet classes) or custom TFLite models.
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
    from PIL import Image
except ImportError:
    print("Error: Pillow (PIL) is required. Install via: pip install pillow")
    sys.exit(1)

try:
    import tensorflow as tf
except ImportError:
    print("Error: tensorflow is required. Install via: pip install tensorflow")
    sys.exit(1)


def classify_image_keras(image_path):
    """
    Classifies an image using full MobileNetV2 model (1000 ImageNet classes).
    Returns top 5 predictions with percentage confidence.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: '{image_path}'")

    print("==========================================================")
    print(" MobileNetV2 Image Classifier (ImageNet 1000 Classes)")
    print("==========================================================")
    print(f"Input Image  : {image_path}")

    # Load MobileNetV2 model
    print("Loading MobileNetV2 Model...")
    model = tf.keras.applications.MobileNetV2(weights="imagenet")

    # Load & Preprocess image
    img = Image.open(image_path).convert('RGB')
    img_resized = img.resize((224, 224), Image.Resampling.LANCZOS)
    img_array = np.array(img_resized, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    input_tensor = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # Warm-up
    _ = model(input_tensor, training=False)

    # Inference & timing
    start_time = time.perf_counter()
    predictions = model(input_tensor, training=False)
    if isinstance(predictions, (tf.Tensor, tf.Variable)):
        predictions = predictions.numpy()
    latency_ms = (time.perf_counter() - start_time) * 1000.0

    # Decode top 5 ImageNet predictions
    results = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]

    print("----------------------------------------------------------")
    print(f"CPU Inference Latency: {latency_ms:.2f} ms")
    print("----------------------------------------------------------")
    print("Top Predictions (Image Kind):")
    for rank, (class_id, label, score) in enumerate(results, 1):
        print(f"  #{rank}: {label:30s} {score * 100:6.2f}%")
    print("==========================================================")


def classify_image_tflite(image_path, model_path, labels_path=None):
    """
    Classifies an image using a custom TFLite model (.tflite).
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: '{image_path}'")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: '{model_path}'")

    print("==========================================================")
    print(" Standalone MobileNetV2 TFLite Image Classifier")
    print("==========================================================")
    print(f"Loading Model: {model_path}")
    print(f"Input Image  : {image_path}")

    Interpreter = tf.lite.Interpreter
    try:
        interpreter = Interpreter(model_path=model_path, experimental_delegates=[])
    except TypeError:
        interpreter = Interpreter(model_path=model_path)

    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    batch, height, width, channels = input_shape
    input_dtype = input_details[0]['dtype']

    print(f"Model Input Dimensions: {width}x{height}x{channels} ({input_dtype})")

    img = Image.open(image_path).convert('RGB')
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    img_array = np.array(img, dtype=np.uint8)

    if input_dtype == np.int8:
        input_data = (img_array.astype(np.int16) - 128).astype(np.int8)
    elif input_dtype == np.uint8:
        input_data = img_array
    else:
        input_data = (img_array.astype(np.float32) / 127.5) - 1.0

    input_data = np.expand_dims(input_data, axis=0)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    start_time = time.perf_counter()
    interpreter.invoke()
    latency_ms = (time.perf_counter() - start_time) * 1000.0

    output_tensor = interpreter.get_tensor(output_details[0]['index'])[0]
    num_classes = output_tensor.shape[0] if len(output_tensor.shape) > 0 else 1

    print("----------------------------------------------------------")
    print(f"CPU Inference Latency: {latency_ms:.2f} ms")
    print("----------------------------------------------------------")

    if num_classes == 2:
        score_diff = int(output_tensor[1]) - int(output_tensor[0])
        prediction = "Class 1 (Target)" if score_diff > 0 else "Class 0 (Non-Target)"
        print(f"Prediction       : {prediction}")
        print(f"Logits (Class 0) : {output_tensor[0]}")
        print(f"Logits (Class 1) : {output_tensor[1]}")
        print(f"Score Difference : {score_diff}")
    else:
        labels = None
        if labels_path and os.path.exists(labels_path):
            with open(labels_path, 'r') as f:
                labels = [line.strip() for line in f.readlines()]

        top_indices = np.argsort(output_tensor)[::-1][:5]
        print("Top Predictions:")
        for rank, idx in enumerate(top_indices, 1):
            label_name = labels[idx] if labels and idx < len(labels) else f"Class {idx}"
            score = output_tensor[idx]
            print(f"  #{rank}: {label_name:25s} (Raw Score: {score})")

    print("==========================================================")


def main():
    parser = argparse.ArgumentParser(description="Classify images and determine image kind using MobileNetV2")
    parser.add_argument("image", help="Path to input image file (JPEG/PNG)")
    parser.add_argument("--model", help="Path to custom .tflite model file", default=None)
    parser.add_argument("--labels", help="Path to text file containing class labels", default=None)
    args = parser.parse_args()

    if args.model:
        classify_image_tflite(args.image, args.model, args.labels)
    else:
        classify_image_keras(args.image)


if __name__ == "__main__":
    main()
