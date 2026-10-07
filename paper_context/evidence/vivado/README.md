# Vivado Evidence

Synthesis, implementation, utilization, timing and FPGA reports for the
merged 1×1 + 3×3 + sliding-window CFU SoC (target board: Digilent Arty, per
`soc/build/digilent_arty.*`).

| Subdirectory | Expected files |
|---|---|
| `synthesis/` | Post-synthesis utilization (`report_utilization`, incl. `-hierarchical` for the CFU instance) |
| `implementation/` | Post-route utilization (top level and CFU hierarchy), DRC |
| `timing/` | `report_timing_summary` (WNS, TNS, failing endpoints), target clock, Fmax derivation |

## Current evidence (commit `1397800`)

Reports are stored per configuration (not per stage):

| Directory | Configuration | Reports |
|---|---|---|
| `cfu_1x1/` | B. 1×1 CFU | utilization hierarchical (synth, place), timing (synth, post-route), clock utilization, power (routed) |
| `cfu_1x1_3x3/` | C. 1×1 + 3×3 DW CFU | same set, no power |
| `sliding_window/` | D. + sliding window | same set, no power |

Vivado v.2024.1, `xc7a100tcsg324-1` (Nexys4 DDR), system clock 75 MHz.
Utilization = post-place; timing = post-route. Parsed values:
`../tables/fpga_resources.md`. The `synthesis/`, `implementation/` and
`timing/` folders are unused.

Earlier quoted figures (WNS +0.243 ns; LUT 6192 / FF 4504; CFU 1514 /
1081) are not in any report and are historical (see
`../RESULTS_AUDIT.md`). Vivado project outputs (`*.runs/`, `*.cache/`,
…) must not be copied here, only `.rpt` files.
