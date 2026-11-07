# Vivado Evidence

Synthesis, implementation, utilization, timing and FPGA reports for the
merged 1×1 + 3×3 + sliding-window CFU SoC (target board: Digilent Arty, per
`soc/build/digilent_arty.*`).

| Subdirectory | Expected files |
|---|---|
| `synthesis/` | Post-synthesis utilization (`report_utilization`, incl. `-hierarchical` for the CFU instance) |
| `implementation/` | Post-route utilization (top level and CFU hierarchy), DRC |
| `timing/` | `report_timing_summary` (WNS, TNS, failing endpoints), target clock, Fmax derivation |

## Existing evidence in the repository (2026-10-07)

None. No `.rpt`, `.dcp`, `.bit` or Vivado log exists in the repository.
`soc/build/digilent_arty.mnv2_cfu_package/gateware/` is empty (no gateware
build has been run in this checkout).

The figures previously quoted for the team (WNS +0.243 ns; top level LUT
6192 / FF 4504 / RAMB36 15 / RAMB18 33 / DSP 8; CFU LUT 1514 / FF 1081 /
RAMB36 4 / RAMB18 8 / DSP 4) have no report here and remain unverified.

Note: the local `proj/mnv2_cfu_package/cfu.v` (git-ignored, dated
2026-10-03) predates the sliding-window merge. Regenerate it before
synthesis so reports match the current code. Vivado project outputs
(`*.runs/`, `*.cache/`, `*.gen/`, `*.hw/`, `*.ip_user_files/`) must not be
copied here; copy only the `.rpt` files.
