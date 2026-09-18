# MobileNetV2 Existing CFU Package

## Purpose

This project runs MobileNetV2 INT8 using the existing MobileNetV2 CFU
implementation from CFU-Playground.

The existing accelerator targets eligible **1x1 `CONV_2D`** operations.
It is not the custom 5x5 depthwise-convolution accelerator planned for
the later research stage.

## File Structure

``` text
proj/
└── mnv2_cfu_package/
    ├── Makefile
    ├── README.md
    ├── vendor_cfu.sh
    ├── cfu_gen.py
    ├── cfu.v
    ├── gateware/
    │   ├── mnv2_cfu.py
    │   └── test_mnv2_cfu.py
    ├── model/
    │   └── mobilenetv2_a035_224_int8.tflite
    ├── inputs/
    │   └── cat.jpg
    ├── src/
    │   ├── mnv2_app.cc
    │   ├── mnv2_cfu.h
    │   ├── software_cfu.cc
    │   ├── cpp_math.cc
    │   ├── cpp_math.h
    │   ├── cat_image.h
    │   ├── cat_image.dat
    │   └── tensorflow/
    │       └── lite/
    │           └── kernels/
    │               └── internal/
    │                   └── reference/
    │                       └── integer_ops/
    │                           ├── conv.cc
    │                           ├── mnv2_conv.cc
    │                           └── mnv2_conv.h
    └── tools/
        └── image_to_header.py
```

Generated files appear under `build/`.

## What Each File Does

### `Makefile`

Enables the MobileNetV2 model and accelerated convolution path:

``` make
DEFINES += ACCEL_CONV
export MNv2_BASELINE := 1
DEFINES += INCLUDE_MODEL_MNV2
```

It uses the common CFU-Playground build system through `../proj.mk`.

### `vendor_cfu.sh`

Copies the existing MobileNetV2 CFU implementation from the upstream
`proj/mnv2_first` implementation into this package.

Run:

``` bash
./vendor_cfu.sh
```

### `cfu_gen.py`

Generates the Verilog CFU wrapper used by the build.

### `cfu.v`

Generated Verilog representation of the CFU. It is compiled by Verilator
for the Renode simulation.

### `gateware/mnv2_cfu.py`

Amaranth gateware implementing the existing MobileNetV2 CFU, including
MAC/accumulation, storage, sequencing, and post-processing logic.

### `gateware/test_mnv2_cfu.py`

Tests the CFU gateware independently.

### `src/mnv2_cfu.h`

Defines the software CFU instruction interface, including configuration,
data storage, MACC execution, and output retrieval operations.

### `src/software_cfu.cc`

Provides software-side CFU support/helpers.

### `src/cpp_math.h`

Declarations for MobileNetV2 quantization and math helper functions.

### `src/cpp_math.cc`

Implementations of those math helpers, including CFU-backed arithmetic
where used by the existing implementation.

### `src/tensorflow/lite/kernels/internal/reference/integer_ops/conv.cc`

Modified integer convolution reference code. It checks whether a
convolution satisfies the existing accelerator's requirements. Eligible
1x1 convolutions are dispatched to `Mnv2ConvPerChannel1x1()`; other
operations remain on the CPU.

### `src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_conv.h`

Declares `Mnv2ConvPerChannel1x1()`.

### `src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_conv.cc`

Implements the accelerated 1x1 convolution and invokes the CFU
instructions.

### `src/mnv2_app.cc`

Main application. It initializes TFLite Micro, loads the model/image,
verifies the input, runs inference, profiles operators, and prints the
classification result.

### `src/cat_image.h`

Embedded image header/data.

### `src/cat_image.dat`

Image data used by the application.

### `tools/image_to_header.py`

Converts the input image into an embeddable C/C++ representation.

## Prerequisites

``` bash
cd ~/Documents/github/CFU-mobilenetV2-base
conda activate cfu-common
cd ~/Documents/github/CFU-mobilenetV2-base/proj/mnv2_cfu_package
```

## Refresh the Existing CFU

``` bash
./vendor_cfu.sh
```

Check the important files:

``` bash
find gateware -type f | sort
find src/tensorflow/lite/kernels/internal/reference/integer_ops -type f | sort
```

## Clean Build and Run

Always clean when changing versions:

``` bash
rm -rf build
make renode
```

The build generates the software firmware and Verilator model for the
CFU.

## Build Flow

``` text
Makefile
   |
   v
CFU-Playground build system
   |
   +--> TFLite Micro software
   |
   +--> Accelerated conv.cc
   |
   +--> mnv2_conv.cc
   |
   +--> CFU Verilog
   |
   +--> Verilator
   |
   v
Renode
   |
   v
MobileNetV2 inference
   |
   v
Eligible 1x1 CONV_2D
   |
   v
Mnv2ConvPerChannel1x1()
   |
   v
Existing MobileNetV2 CFU
```

Non-eligible operations continue through the CPU implementation.

## How to Check That the CFU Was Built

``` bash
find build -type f | grep -E 'Vcfu|cfu\.v|libV'
```

A successful Verilator build should contain CFU-related generated files
such as `Vcfu.cpp` and the generated simulation library.

## Runtime Evidence

The strongest runtime evidence is the operator profiler.

The current CFU run measured:

``` text
448,959,843 cycles
```

The CPU-only baseline measured:

``` text
1,216,227,740 cycles
```

For the same model/input this corresponds to approximately:

``` text
2.71x fewer total cycles
63.1% reduction in total cycles
```

These are Renode/Verilator simulation measurements, not physical FPGA
timing or power measurements.

## Why Only Some CONV_2D Operations Become Fast

The existing CFU accelerates eligible **1x1 `CONV_2D`** operations.

Therefore:

``` text
1x1 CONV_2D        -> Existing CFU
DEPTHWISE_CONV_2D -> CPU/reference implementation
Other operations   -> CPU/reference implementation
```

This behavior is expected and is important because the later research
stage will investigate a custom 5x5 depthwise-convolution accelerator.

## Fair A/B Experiment

### CPU baseline

``` bash
cd ~/Documents/github/CFU-mobilenetV2-base/proj/mnv2_baseline
rm -rf build
NO_CFU=1 SW_ONLY=1 make renode
```

Record the total cycles.

### Existing CFU

``` bash
cd ~/Documents/github/CFU-mobilenetV2-base/proj/mnv2_cfu_package
rm -rf build
make renode
```

Record:

-   whole-model cycles;
-   per-operator cycles;
-   input checksum;
-   final classification result.

The same input and model should produce the same functional result while
the accelerated implementation changes the cycle count.

## Current Comparison

  Measurement                          CPU Baseline                 Existing CFU
  -------------------- ---------------------------- ----------------------------
  Model                  MobileNetV2 a0.35 224 INT8   MobileNetV2 a0.35 224 INT8
  Input                              Same cat image               Same cat image
  Accelerator                                  None             Existing 1x1 CFU
  Whole-model cycles                  1,216,227,740                  448,959,843

## Important Scope

This package is the **existing-CFU reference**, not the final custom
accelerator.

Current architecture:

``` text
MobileNetV2
     |
     +-- 1x1 CONV_2D ------> Existing MobileNetV2 CFU
     |
     +-- Depthwise CONV ----> CPU
     |
     +-- Other operators ---> CPU
```

The next research stage can extend this flow with the proposed 5x5
depthwise-convolution CFU.
