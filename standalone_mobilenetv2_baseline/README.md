# MobileNetV2 Baseline (Standalone CPU Codebase)

This is a **completely standalone codebase** for running MobileNetV2 baseline inference directly on any host CPU (x86_64, ARM, Linux, macOS, Windows).

> 💡 **100% Independent of CFU-Playground**: This codebase does **NOT** use LiteX, VexRiscv, `cfu.v`, FPGA synthesis tools, or any CFU-Playground Makefiles.

---

## 📂 Codebase Structure

```
standalone_mobilenetv2_baseline/
├── model_mobilenetv2_160_035.tflite  # Quantized MobileNetV2 TFLite Model
├── main.py                           # Standalone Python CPU runner & benchmark
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

### Method 1: Using Repository Environment (Pre-installed & Recommended)

The repository's conda environment already has `numpy` and `tensorflow` installed. Simply run:

```bash
/home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python standalone_mobilenetv2_baseline/main.py
```

Or using the environment script:
```bash
source environment
python3 standalone_mobilenetv2_baseline/main.py
```

---

### Method 2: Virtual Environment (`venv`)

To run in a clean Python virtual environment without modifying system packages:

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install numpy tensorflow

# 3. Run inference script
python3 standalone_mobilenetv2_baseline/main.py
```

---

### Method 3: System Pip (`--break-system-packages`)

If installing directly to user Python on modern Linux (PEP 668):

```bash
pip install --break-system-packages numpy tensorflow
python3 standalone_mobilenetv2_baseline/main.py
```

---

## 📊 Execution Output

```text
==========================================================
 MobileNetV2 Baseline CPU Runner (Standalone Codebase)
==========================================================
Loading TFLite Model: /home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/standalone_mobilenetv2_baseline/model_mobilenetv2_160_035.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
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
1. **Model**: Quantized MobileNetV2 160x160x3 (`model_mobilenetv2_160_035.tflite`).
2. **CPU Execution Engine**: Standard TensorFlow Lite Interpreter running directly on host CPU cores.
3. **No Hardware Dependencies**: Does not require RISC-V cross-compilers, Renode, Verilator, or LiteX.
