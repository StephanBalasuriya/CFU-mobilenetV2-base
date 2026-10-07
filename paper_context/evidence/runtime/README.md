# Runtime Evidence

Actual MobileNetV2 (INT8, a0.35, 224×224) execution logs and measured
cycle/instruction counts. Every configuration must use the same model,
input image, tensor arena, profiler and platform.

| Subdirectory | Configuration | Build |
|---|---|---|
| `cpu_only/` | CPU-only baseline | `proj/mnv2_baseline`, `NO_CFU=1 SW_ONLY=1 make renode` |
| `cfu_1x1/` | Existing 1×1 CFU only | 1×1-only build of `proj/mnv2_cfu_package` (pre-3×3 commit, e.g. `3514b03`) |
| `cfu_1x1_3x3/` | 1×1 + 3×3 depthwise CFU, no sliding window | e.g. commit `35e4493` |
| `sliding_window/` | 1×1 + 3×3 + sliding window | current `mindi` (`b82da40` merged) |

Each log should include the whole-model cycle count, per-operator profiler
output, Top-1 result and `Output FNV1a`. Instruction-count runs
(`make DW3X3_VERIFY=1`) are stored separately from timing runs, because
the counters change the cycle count.

## Existing evidence in the repository (2026-10-07)

No raw runtime logs are committed. Repository-documented values (text only,
Renode/Verilator simulation):

| Value | Source |
|---|---|
| CPU-only 1,216,227,740 cycles | `proj/mnv2_baseline/README_MNV2_CPU_BASELINE.md` |
| 1×1 CFU 448,959,843 cycles | `proj/mnv2_cfu_package/README_MNV2_EXISTING_CFU.md` |

Sliding-window instruction counts (LOAD 2,529,552 → 726,864; SHIFT 600,896;
RUN/GET 843,184; CONFIGURE 17) are reproducible analytically from
`proj/mnv2_cfu_package/src/tensorflow/lite/micro/kernels/depthwise_conv.cc`
(`Dw3x3VerifyReport`) but have no measured log yet. See
`../../EXPERIMENTAL_RESULTS.md`.

`proj/mnv2_baseline/baseline_build.log` is **not** runtime evidence: it is a
build log from another machine ending in a link failure.
