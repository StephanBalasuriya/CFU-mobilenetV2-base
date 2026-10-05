# MobileNetV2 a0.35 INT8 — CFU Baseline

This is the **CFU-accelerated companion** to the working CPU-only
`mnv2_baseline` project.

It keeps the same:
- `mobilenetv2_a035_224_int8.tflite`
- 224x224 RGB input
- embedded image
- FLOAT32 1000-class output
- whole-model `mcycle` measurement

and enables the existing MobileNetV2 CFU architecture from the upstream
CFU-Playground `mnv2_first` project.

## What is accelerated?

The package preserves the existing eligible **1x1 CONV_2D** accelerator and
adds a dedicated **3x3 INT8 DEPTHWISE_CONV_2D** datapath.
The upstream kernel checks the convolution parameters and dispatches eligible
MobileNetV2 1x1 convolutions to `Mnv2ConvPerChannel1x1()` when `ACCEL_CONV`
is defined.

The depthwise path is selected only for INT8 input and weights, a 3x3 filter,
depth multiplier 1, unit dilation, and stride 1 or 2. Interior windows are
packed into three input/weight word pairs and processed with one 9-MAC CFU
operation. Padding and unsupported quantization cases use the original
reference implementation.

## Install inside your existing CFU-Playground checkout

The package should live here:

    CFU-Playground/
      proj/
        mnv2_baseline/
        mnv2_cfu/

The upstream project must also exist:

    proj/mnv2_first/

After extracting this directory:

    cd ~/Documents/github/CFU-Playground/proj/mnv2_cfu
    ./vendor_cfu.sh

The script copies the exact current `mnv2_first` CFU gateware and TFLM
integration into this project. This avoids silently using a stale hand-copied
hardware implementation.

## Regenerate the image

If you change the input image:

    cd ~/Documents/github/CFU-Playground

    python3 proj/mnv2_cfu/tools/image_to_header.py         proj/mnv2_cfu/inputs/cat.jpg         proj/mnv2_cfu/src/cat_image.h

## CPU build

This project is the CFU version, so DO NOT use `NO_CFU=1`.

    cd ~/Documents/github/CFU-Playground

    source env/conda/bin/activate cfu-common
    export CFU_ROOT=$PWD

    make -C proj/mnv2_cfu clean
    make -C proj/mnv2_cfu -j$(nproc)

## Renode

    make -C proj/mnv2_cfu renode

The build should generate `cfu.v`, build the CFU-enabled SoC software,
and launch Renode.

## Expected experiment

Run exactly the same image/model on:

    mnv2_baseline  -> CPU-only
    mnv2_cfu       -> existing 1x1 CFU + 3x3 depthwise CFU

Record:

    baseline_cycles
    cfu_cycles

and calculate:

    speedup = baseline_cycles / cfu_cycles

The profiler output still gives the per-operator cycle counts, so you can
identify which CONV_2D and DEPTHWISE_CONV_2D operations benefit from the
accelerator. The application input, model, quantization, and output
interpretation are unchanged.

## CFU generation and measurements

From the repository root, with the normal CFU-Playground environment active:

``` bash
make -C proj/mnv2_cfu_package generate_cfu
make -C proj/mnv2_cfu_package clean
make -C proj/mnv2_cfu_package renode
make -C proj/mnv2_cfu_package run-renode
```

Record total cycles and the operator profiler's
`DEPTHWISE_CONV_2D`/`CONV_2D` ticks from `build/software.log`. The expected
functional check remains the known class-64 result (approximately 0.406250).

## Important

The upstream CFU-Playground documentation describes the framework as a way
to choose a TFLite operator, design custom instructions, build the CFU, modify
the TFLM kernel, and measure the resulting performance. This project follows
that architecture while keeping your MobileNetV2 application separate.

Reference:
https://github.com/google/CFU-Playground
