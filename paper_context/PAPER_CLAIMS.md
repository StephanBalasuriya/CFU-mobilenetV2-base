# Paper Claims Control

## Claims we can make

- We extend an existing RISC-V CFU-based MobileNetV2 acceleration path.
- We implement a dedicated 3×3 depthwise-convolution CFU.
- The 3×3 CFU complements the existing 1×1 pointwise CFU.
- We implement sliding-window reuse for eligible stride-1 3×3 depthwise operations.
- The sliding-window mechanism reduces redundant LOAD instructions.
- We evaluate end-to-end INT8 MobileNetV2 execution.
- We evaluate FPGA timing and resource utilization.
- We perform functional verification.

## Claims requiring measured evidence

- End-to-end speedup from the 3×3 CFU.
- End-to-end speedup from sliding-window reuse.
- Final FPGA resource overhead.
- Final Fmax.
- Layer-level performance improvement.

## Claims we must NOT make

- First 3×3 depthwise CFU.
- First MobileNetV2 CFU accelerator.
- Novel DSP packing.
- First sliding-window reuse technique.
- All MobileNetV2 operators are hardware accelerated.
- 71.26% end-to-end speedup from sliding-window reuse.

## Safe positioning

The work investigates a lightweight extension of an existing tightly coupled RISC-V CFU MobileNetV2 execution path with 3×3 depthwise acceleration and sliding-window data reuse, evaluated through end-to-end performance, data-movement, FPGA resource/timing, and functional verification.
