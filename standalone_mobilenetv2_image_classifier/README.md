# MobileNetV2 Standalone Image Classifier & Layer Profiler

This is a **standalone image classification and profiling codebase** for running MobileNetV2 CPU inference on image files (JPEG, PNG), profiling layer execution times, and running benchmark tests directly on any host CPU (x86_64, ARM, Linux, macOS, Windows).

> 💡 **100% Independent of CFU-Playground**: This codebase does **NOT** use LiteX, VexRiscv, `cfu.v`, FPGA synthesis tools, or any CFU-Playground Makefiles.

---

## 📂 Codebase Structure

```
standalone_mobilenetv2_image_classifier/
├── classify_image.py                 # Image Classifier & Layer-by-Layer Profiler
├── main.py                           # Benchmark runner for golden binary inputs
├── my_cat.jpg                        # Sample input image
├── mobilenet_v2_timing.csv           # Output CSV containing detailed layer profiling metrics
├── model_mobilenetv2_160_035.tflite  # Quantized MobileNetV2 TFLite Model (used by main.py)
├── inputs/                           # Golden test input data files (.dat)
│   ├── input_00001_7281.dat
│   ├── input_00001_7425.dat
│   ├── input_00002_2532.dat
│   ├── input_00002_25869.dat
│   └── input_00004_970.dat
└── README.md                         # Documentation & Usage Guide
```

---

## 🚀 How to Run

> ⚠️ **Note on Python Environment**: Use the repository's pre-configured `cfu-common` Conda environment (`/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python`) as it has `tensorflow`, `numpy`, and `Pillow` pre-installed.

### Scenario A: Running from repository root (`CFU-mobilenetV2-base/`)

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base

/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python standalone_mobilenetv2_image_classifier/classify_image.py
```

### Scenario B: Running inside directory (`standalone_mobilenetv2_image_classifier/`)

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/standalone_mobilenetv2_image_classifier

/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py
```

---

#### What `classify_image.py` Performs:
1. **Model Loading & Image Preprocessing**: Loads MobileNetV2, resizes image to 224x224, and preprocesses inputs.
2. **Model Warm-Up**: Performs warm-up runs to stabilize execution before timing.
3. **Inference Benchmarking**: Measures full-model inference latency over multiple runs (`NUM_RUNS = 10`), computing **Average**, **Minimum**, and **Maximum** timings in milliseconds.
4. **Top 5 Predictions**: Outputs top ImageNet class predictions and confidence scores.
5. **Layer-by-Layer Profiling**: Iterates through all `Conv2D` and `DepthwiseConv2D` layers to profile individual execution times.
6. **Bottleneck Breakdown**: Categorizes layer latency into key MobileNetV2 operations:
   - **Expansion 1x1**
   - **Depthwise 3x3**
   - **Projection 1x1**
   - **Other Conv2D**
7. **CSV Export**: Automatically exports per-layer profiling data to `mobilenet_v2_timing.csv`.

---

### Run Standalone Golden TFLite Benchmark Tests (`main.py`)

From repository root:
```bash
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python standalone_mobilenetv2_image_classifier/main.py
```

---

## 🔍 Key Technical Details

1. **CPU Execution Engine**: Standard TensorFlow / Keras MobileNetV2 framework execution running directly on host CPU cores.
2. **Measurement Stability**: Uses warm-up iterations and multi-run statistical metrics (`average`, `min`, `max`) to eliminate initial initialization noise.
3. **Layer-Level Profiling**: Constructs dynamic sub-models to isolate and measure individual bottleneck convolution operations.
4. **No Hardware Dependencies**: Does not require RISC-V cross-compilers, Renode, Verilator, or LiteX.
