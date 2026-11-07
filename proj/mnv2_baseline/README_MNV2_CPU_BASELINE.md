# MobileNetV2 CPU-Only Baseline

## Purpose

This project runs the MobileNetV2 INT8 model on the VexRiscv CPU without
using the MobileNetV2 CFU accelerator. It is the reference
implementation for comparison with the existing-CFU version.

## File Structure

``` text
proj/
└── mnv2_baseline/
    ├── Makefile
    ├── README.md
    ├── model/
    │   └── mobilenetv2_a035_224_int8.tflite
    ├── inputs/
    │   └── cat.jpg
    └── src/
        ├── mnv2_app.cc
        ├── cat_image.h
        └── cat_image.dat
```

Generated files appear under `build/` and should not be edited manually.

## What Each File Does

### `Makefile`

Controls the CFU-Playground build. The baseline uses the MobileNetV2
model and is built with `NO_CFU=1` so no custom CFU accelerator is used.

### `model/mobilenetv2_a035_224_int8.tflite`

The MobileNetV2 a0.35, 224x224 INT8 TFLite model. The same model must be
used for the CFU experiment.

### `inputs/cat.jpg`

The input image used for inference. Use the same image in both
experiments.

### `src/cat_image.h`

C/C++ embedded image data/header used by the application.

### `src/cat_image.dat`

Image data used for the embedded input.

### `src/mnv2_app.cc`

Main application. It initializes TFLite Micro, loads the model and
embedded image, verifies the input, runs inference, profiles operators,
and prints the classification result.

## Prerequisites

``` bash
cd ~/Documents/github/CFU-mobilenetV2-base
conda activate cfu-common
```

Go to the project:

``` bash
cd ~/Documents/github/CFU-mobilenetV2-base/proj/mnv2_baseline
```

## Clean Build and Run

``` bash
rm -rf build
NO_CFU=1 SW_ONLY=1 make renode
```

The CPU-only build can also be created with:

``` bash
NO_CFU=1 SW_ONLY=1 make
```

## Useful Commands

``` bash
# Enter project
cd ~/Documents/github/CFU-mobilenetV2-base/proj/mnv2_baseline

# Clean
rm -rf build

# Build CPU-only firmware
NO_CFU=1 SW_ONLY=1 make

# Build and run Renode
NO_CFU=1 SW_ONLY=1 make renode

# Find generated firmware
find build -type f \( -name "*.elf" -o -name "*.bin" \)

# Find copied model
find build/src/models/mnv2 -type f
```

## Runtime Measurement

The important result is the whole-model cycle count printed by the
profiler.

Current baseline measurement:

``` text
1,216,227,740 cycles
```

The profiler also reports individual TFLite Micro operator cycle counts.

## Baseline Execution Flow

``` text
MobileNetV2 INT8
      |
      v
TFLite Micro reference operators
      |
      v
VexRiscv CPU
      |
      v
Total cycle count
```

No MobileNetV2 CFU instructions are used.

## Fair Comparison Requirements

Run baseline and CFU using exactly the same:

-   model;
-   input image;
-   input preprocessing;
-   tensor arena;
-   profiler;
-   Renode/Verilator environment.

Record the whole-model cycles, per-operator cycles, input checksum, and
final output.

## Current Reference Result

  Measurement                          CPU Baseline
  -------------------- ----------------------------
  Model                  MobileNetV2 a0.35 224 INT8
  Input                               224 x 224 RGB
  Accelerator                                  None
  Execution                            VexRiscv CPU
  Whole-model cycles                  1,216,227,740
