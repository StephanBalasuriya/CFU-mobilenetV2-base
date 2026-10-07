# Baseline Functional Verification

## Purpose

This document records the functional verification performed for the baseline 3x3 depthwise-convolution CFU implementation.

The objective was to verify that the CFU produces functionally correct results and matches the software/reference implementation for the supported depthwise-convolution operations.

## Verification Scope

The verification covered:

- 3x3 depthwise-convolution CFU functionality.
- Correct input and weight loading.
- Correct multiply-accumulate execution.
- Correct result retrieval.
- Configuration parameters such as input/weight offsets.
- Bias and quantization behavior.
- Functional equivalence against the reference depthwise implementation and TFLM reference behavior.

## Verification Method

Two levels of verification were performed:

1. Gateware-level unit tests.
2. Host-side functional-equivalence tests.

The tests included different depthwise-convolution configurations and parameter combinations rather than relying on a single fixed test case.

## Gateware Verification

- **Tests passed:** 25 / 25
- **Tests failed:** 0 / 25

The gateware tests verified the basic hardware datapath and control behavior of the 3x3 depthwise CFU.

## Host Functional-Equivalence Verification

A broader host-side verification compared the implementation against the existing/reference depthwise implementation.

- **Cases tested:** 400 / 400
- **Cases passed:** 400
- **Cases failed:** 0
- **Functional mismatches:** 0

The tested cases included:

- Random input shapes.
- `SAME` and `VALID` padding.
- Stride 1 and stride 2.
- Random input and weight offsets.
- Bias handling.
- Quantization multipliers.
- Different valid depthwise-convolution configurations.

The outputs were byte-identical for all tested cases.

## TFLM Reference Equivalence

The implementation was also checked against TensorFlow Lite Micro (TFLM) reference behavior. The tested depthwise-convolution results matched the expected reference output.

## MobileNetV2 Functional Check

The 3x3 depthwise CFU was exercised as part of the INT8 MobileNetV2 inference flow.

**Model:** `mobilenetv2_a035_224_int8.tflite`

Configuration:

- Input resolution: 224 x 224 x 3
- External input: UINT8
- Internal computation: INT8
- Output: FLOAT32
- Number of classes: 1000

The inference completed successfully with:

- **Top-1 class index:** 64
- **Top-1 score:** 0.406250

## Conclusion

The baseline 3x3 depthwise CFU passed both gateware-level and host-level functional verification.

The results establish that the CFU datapath is functionally correct for the tested configurations and can execute successfully within the end-to-end INT8 MobileNetV2 inference pipeline.

This verification serves as the functional baseline before evaluating the sliding-window/data-reuse optimization.

## Verification Summary

| Verification Item | Result |
|---|---:|
| Gateware unit tests | 25 / 25 passed |
| Host functional-equivalence tests | 400 / 400 passed |
| Functional mismatches | 0 |
| MobileNetV2 inference | Passed |
| MobileNetV2 Top-1 class | 64 |
| MobileNetV2 Top-1 score | 0.406250 |
