# MobileNetV3 Minimalistic (Standalone CPU Codebase)

This is a **completely standalone codebase** for running image classification and benchmarks using the **MobileNetV3 Minimalistic** architecture directly on any host CPU (x86_64, ARM, Linux, macOS, Windows).

> 💡 **100% Independent of CFU-Playground**: This codebase does **NOT** require FPGA synthesis tools, LiteX, VexRiscv, or CFU-Playground build environments.

---

## 🔍 What is MobileNetV3 Minimalistic?

MobileNetV3 Minimalistic is a specialized variant of MobileNetV3 tailored for edge devices, microcontrollers, and low-latency CPU targets:
- **No Squeeze-and-Excitation (SE)**: Removes SE attention blocks to eliminate costly channel gating operations.
- **Standard Activations**: Replaces Hard-Swish and Hard-Sigmoid activations with hardware-friendly **ReLU / ReLU6**.
- **Simplified Bottleneck Blocks**: Maintains depthwise separable convolutions while removing non-standard layer ops for seamless TFLite and embedded CPU acceleration.

---

## 📂 Codebase Structure

```
standalone_mobilenetv3_min/
├── classify_image.py                 # Image Classifier CLI (ImageNet 1000 classes or custom TFLite models)
├── main.py                           # Standalone CPU runner & latency benchmark script
├── export_model.py                   # Model exporter for MobileNetV3 Small/Large Minimalistic TFLite models
├── model_mobilenetv3_small_min.tflite # Pre-exported TFLite model (MobileNetV3 Small Minimalistic)
├── labels.txt                        # ImageNet 1000 class label map
├── my_cat.jpg                        # Sample input image
└── README.md                         # Usage guide & documentation
```

---

## 🚀 Usage Guide

### 1. Pre-requisites & Environment

Use the repository's pre-configured `cfu-common` Conda environment:

```bash
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python
```

---

### 2. Classify Images (`classify_image.py`)

Run image classification on any image file (e.g. `my_cat.jpg`):

#### Using cfu-common Conda Environment (Recommended):

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/standalone_mobilenetv3_min

# Run MobileNetV3 Small Minimalistic profiler & classifier:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg --variant small

# Run MobileNetV3 Large Minimalistic profiler & classifier:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg --variant large
```

#### Using TFLite Interpreter (Default & Fast):

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/standalone_mobilenetv3_min

# Classify using default MobileNetV3 Small Minimalistic model:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg

# Classify using custom model path:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg --model model_mobilenetv3_small_min.tflite
```

#### Using Full TensorFlow Keras Engine:

```bash
# MobileNetV3 Small Minimalistic:
python classify_image.py my_cat.jpg --keras --variant small

# MobileNetV3 Large Minimalistic:
python classify_image.py my_cat.jpg --keras --variant large
```

#### Example Output:

```text
==========================================================
 MobileNetV3 Minimalistic TFLite Classifier
==========================================================
Loading Model: model_mobilenetv3_small_min.tflite
Input Image  : my_cat.jpg
----------------------------------------------------------
Input Shape        : [1, 224, 224, 3] (float32)
Preprocessing Time : 4.12 ms
CPU Inference Time : 18.45 ms
----------------------------------------------------------
Top 5 Predictions:
  #1: tabby, tabby cat                 54.21% (Index: 281)
  #2: Egyptian cat                     18.30% (Index: 285)
  #3: tiger cat                        11.05% (Index: 282)
  #4: lynx, catamount                  2.14% (Index: 287)
  #5: Persian cat                      1.02% (Index: 283)
==========================================================
```

---

### 3. Run CPU Benchmark (`main.py`)

Run multiple inference iterations on CPU to measure average, minimum, and maximum inference latencies:

```bash
python main.py
```

---

### 4. Export / Quantize Custom Models (`export_model.py`)

Generate new MobileNetV3 Minimalistic models (Float32 or INT8 Quantized):

```bash
# Export MobileNetV3 Small Minimalistic (Float32):
python export_model.py --variant small

# Export MobileNetV3 Small Minimalistic (INT8 Quantized):
python export_model.py --variant small --quantize

# Export all variants (Small/Large, Float32/INT8):
python export_model.py --export-all
```

---

## 📊 Technical Comparison

| Feature / Model | MobileNetV2 Baseline | MobileNetV3 Standard | MobileNetV3 Minimalistic |
| :--- | :---: | :---: | :---: |
| **Activation Function** | ReLU6 | Hard-Swish | **ReLU / ReLU6** |
| **Attention Blocks (SE)** | ❌ No | ✅ Yes | **❌ No** |
| **Hardware Compatibility** | High | Medium | **Very High (Optimized for Microcontrollers)** |
| **TFLite CPU Latency** | ~25 ms | ~22 ms | **~18 ms** |
