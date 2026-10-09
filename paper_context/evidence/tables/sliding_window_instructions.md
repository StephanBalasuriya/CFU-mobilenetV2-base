# Sliding-Window 3×3 CFU Instruction Counts

Per inference, all 17 eligible 3×3 depthwise layers. **Instruction-count reduction, not a speedup.** The end-to-end effect is in `end_to_end_performance.md`.

| Instruction | Before (3 LOADs/window) | After (sliding window) | Reduction |
|---|---:|---:|---:|
| CONFIGURE | 17 | 17 | 0 % |
| LOAD | 2,529,552 | 726,864 | 71.27 % |
| SHIFT_RIGHT | 0 | 600,896 | new (0 → 600,896) |
| RUN | 843,184 | 843,184 | 0 % |
| GET_RESULT | 843,184 | 843,184 | 0 % |
| **Total 3×3 CFU instructions** | 4,215,937 | 3,014,145 | 28.51 % |

LOAD reduction = 1 − 726,864 / 2,529,552 = 71.265 % → **71.27 %** rounded (71.26 % if truncated). Use one convention consistently.

## Status: analytical (source-derived), not measured

No `make DW3X3_VERIFY=1` counter log exists in the evidence. The counts are computed by `dw_instruction_counts()` in `paper_context/figures/scripts/build_results.py`, which mirrors `Dw3x3VerifyReport()` in `proj/mnv2_cfu_package/src/tensorflow/lite/micro/kernels/depthwise_conv.cc` and the loop structure of `mnv2_depthwise_conv.h`, applied to the MobileNetV2 a0.35 224 depthwise layer shapes. The result matches the counts reported independently by the team exactly (all 10 values).

Formula: reduction = (before − after) / before × 100
