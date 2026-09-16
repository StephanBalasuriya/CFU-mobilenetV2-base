# MobileNetV2 Baseline (Standalone CPU Codebase)

This is a **completely standalone codebase** for running MobileNetV2 baseline inference directly on any host CPU (x86_64, ARM, Linux, macOS, Windows).

> 💡 **100% Independent of CFU-Playground**: This codebase does **NOT** use LiteX, VexRiscv, `cfu.v`, FPGA synthesis tools, or any CFU-Playground Makefiles.

---

## 📂 Codebase Structure

```
standalone_mobilenetv2_baseline/
├── classify_image.py                 # Image Classifier (1000 ImageNet classes or custom .tflite)
├── main.py                           # Standalone Python CPU runner & golden dataset benchmark
├── model_mobilenetv2_160_035.tflite  # Quantized MobileNetV2 TFLite Model
├── my_cat.jpg                        # Sample input image
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

---

### 1. Classify Images (`classify_image.py`)

#### Scenario A: Running from inside `standalone_mobilenetv2_baseline/` directory

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/standalone_mobilenetv2_baseline

# General Image Kind Classification (ImageNet 1000 Classes):
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg

# Custom TFLite Model Classification:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python classify_image.py my_cat.jpg --model model_mobilenetv2_160_035.tflite
```

#### Scenario B: Running from repository root (`CFU-mobilenetV2-base/`)

```bash
cd /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base

# General Image Kind Classification:
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python standalone_mobilenetv2_baseline/classify_image.py standalone_mobilenetv2_baseline/my_cat.jpg
```

#### Example Output:

```text
==========================================================
 MobileNetV2 Image Classifier (ImageNet 1000 Classes)
==========================================================
Input Image  : my_cat.jpg
Loading MobileNetV2 Model...
----------------------------------------------------------
CPU Inference Latency: 95.41 ms
----------------------------------------------------------
Top Predictions (Image Kind):
  #1: tabby                           52.58%
  #2: Egyptian_cat                    14.53%
  #3: tiger_cat                        6.72%
  #4: lynx                             1.32%
  #5: cup                              1.08%
==========================================================
```

---

### 2. Run Golden TFLite Dataset Benchmark (`main.py`)

To run reference CPU inference against golden binary `.dat` input tensors:

#### Running from inside `standalone_mobilenetv2_baseline/`:

```bash
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python main.py
```

#### Running from repository root (`CFU-mobilenetV2-base/`):

```bash
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python standalone_mobilenetv2_baseline/main.py
```

#### Example Output:

```text
==========================================================
 MobileNetV2 Baseline CPU Runner (Standalone Codebase)
==========================================================
Loading TFLite Model: model_mobilenetv2_160_035.tflite
Input Tensor Shape : [  1 160 160   3] (<class 'numpy.int8'>)
Output Tensor Shape: [1 2] (<class 'numpy.int8'>)
----------------------------------------------------------
Test input_00001_7281.dat -> Output Score: -146 (Expected: -148) | [FAIL] | CPU Latency: 2.133 ms
Test input_00001_7425.dat -> Output Score:   66 (Expected:   68) | [FAIL] | CPU Latency: 0.810 ms
Test input_00002_2532.dat -> Output Score: -112 (Expected: -112) | [PASS] | CPU Latency: 1.056 ms
Test input_00002_25869.dat -> Output Score:  138 (Expected:  134) | [FAIL] | CPU Latency: 1.156 ms
Test input_00004_970.dat  -> Output Score:  128 (Expected:  128) | [PASS] | CPU Latency: 1.009 ms
----------------------------------------------------------
Golden Tests Completed: 2/5 Passed
==========================================================
```

---

## 🔍 Key Technical Details

1. **Model Support**: Supports full MobileNetV2 (1000 ImageNet categories) and custom quantized TFLite models (`model_mobilenetv2_160_035.tflite`).
2. **CPU Execution Engine**: Standard TensorFlow / TFLite Interpreter running directly on host CPU cores.
3. **No Hardware Dependencies**: Does not require RISC-V cross-compilers, Renode, Verilator, or LiteX.
