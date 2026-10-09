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

## Current evidence (commit `1397800`)

| Directory | Log | Cycles |
|---|---|---:|
| `cpu_only/` | **missing** | [REQUIRED] |
| `cfu_1x1/` | `output.md` | 828,991,457 |
| `cfu_1x1_3x3/` | `output.md` | 615,396,021 |
| `sliding_window/` | `output.md` | 573,258,998 |

Configuration identification and open metadata questions:
`../CONFIGURATION_MAP.md`. Parsed tables: `../tables/`. The old
Renode/Verilator README values (1,216,227,740 / 448,959,843) are historical
and must not be mixed with these logs. `proj/mnv2_baseline/baseline_build.log`
is not runtime evidence (failed link).
