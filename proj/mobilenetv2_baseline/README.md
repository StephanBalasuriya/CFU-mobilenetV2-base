# MobileNetV2 Baseline (Pure CPU Execution)

This project contains the **baseline MobileNetV2 execution code** running directly on the RISC-V CPU without using any CFU (Custom Function Unit) hardware acceleration or custom assembly/C++ kernels.

---

## 📌 Technical Summary

| Parameter | Configuration |
| :--- | :--- |
| **Model** | MobileNetV2 160x160 (`INCLUDE_MODEL_MNV2`) |
| **Execution Engine** | TensorFlow Lite Micro (Reference C++ integer ops) |
| **Target Architecture** | RISC-V (VexRiscv CPU) |
| **CFU Acceleration** | **Disabled** (No `ACCEL_CONV` or custom instructions) |

---

## 📂 Project Structure

```
proj/mobilenetv2_baseline/
├── Makefile       # Project configuration & build defines
├── README.md      # Documentation & execution instructions
├── cfu.v          # Pass-through Verilog stub for build system compatibility
└── src/
    ├── README.md  # Source notes
    └── proj_menu.cc # Project-specific serial menu interface
```

---

## 🚀 How to Build and Run

### 1. Build and Run interactively in Renode Simulator
```bash
cd proj/mobilenetv2_baseline
make renode
```

### 2. Run Automated Classification Tests in Renode (Headless)
```bash
cd proj/mobilenetv2_baseline
make run-renode
```

### 3. Run in Verilator Simulation
```bash
cd proj/mobilenetv2_baseline
make load PLATFORM=sim
```

### 4. Build Software Binary Only (`SW_ONLY=1`)
```bash
cd proj/mobilenetv2_baseline
make software SW_ONLY=1
```

---

## 🎮 Interactive Menu Operations

When the application boots into the terminal interface:

1. Type `3` to open the **mnv2** (MobileNetV2) model menu.
2. Select any test option:
   - `0` - Run test image 0
   - `1` - Run test image 1
   - `g` - Run all golden tests (verifies model accuracy on reference images)
   - `z` - Run inference on zero-filled input tensor
