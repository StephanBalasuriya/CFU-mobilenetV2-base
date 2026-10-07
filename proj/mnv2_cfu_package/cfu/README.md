# Upstream CFU provenance

This project uses the MobileNetV2 CFU architecture from:

https://github.com/google/CFU-Playground/tree/main/proj/mnv2_first

The accelerator consists of:
- Amaranth gateware in `cfu/gateware/`
- `cfu_gen.py` to generate `cfu.v`
- `src/mnv2_cfu.h` for the CPU-side instruction interface
- `src/software_cfu.cc` for software CFU emulation
- TFLM integer convolution overrides under
  `src/tensorflow/lite/kernels/internal/reference/integer_ops/`

Run `../vendor_cfu.sh` from this project if the `cfu/` sources have not
already been populated.

The accelerator is the upstream MobileNetV2 1x1 convolution CFU. It does
NOT accelerate MobileNetV2 depthwise 3x3/5x5 convolutions. That distinction
is intentional: this version establishes a clean CPU-vs-existing-CFU
baseline before a custom 5x5 depthwise CFU is designed.
