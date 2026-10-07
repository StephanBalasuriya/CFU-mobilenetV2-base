# Configuration Map

Mapping of every evidence file to the paper's hardware configurations.
Evidence added by commit `1397800` ("vivado logs and output added",
2026-10-07); analysed at that commit on branch `mindi`.

| Configuration | Runtime evidence | Vivado evidence | Model | Status |
|---|---|---|---|---|
| A. CPU-only | **none** (`runtime/cpu_only/` empty) | **none** | – | **MISSING** |
| B. Existing 1×1 CFU | `runtime/cfu_1x1/output.md` (828,991,457 cycles) | `vivado/cfu_1x1/b_digilent_nexys4ddr_*` (6 reports incl. power) | `mobilenetv2_a035_224_int8.tflite` | Runtime + Vivado present |
| C. 1×1 + 3×3 depthwise CFU | `runtime/cfu_1x1_3x3/output.md` (615,396,021 cycles) | `vivado/cfu_1x1_3x3/digilent_nexys4ddr_*` (5 reports, no power) | same | Runtime + Vivado present |
| D. 1×1 + 3×3 + sliding window | `runtime/sliding_window/output.md` (573,258,998 cycles) | `vivado/sliding_window/sw_digilent_nexys4ddr_*` (5 reports, no power) | same | Runtime + Vivado present |

All Vivado reports: Vivado v.2024.1, device `xc7a100tcsg324-1`, design
`digilent_nexys4ddr` (Digilent Nexys4 DDR), system clock
`soc_crg_clkout0` = 13.333 ns (75 MHz).

## How each mapping was confirmed (not by filename alone)

### Runtime logs

All three logs show the same model, 224×224×3 UINT8 input, input
FNV-1a `0xbe3b0c0b`, and the same 71-event operator mix. The banner
`Mode: EXISTING MNV2 CFU / Accelerated op: eligible 1x1 CONV_2D` is printed
by **all three** logs, so it does not identify the configuration. The
following source markers do:

| Marker in log | Introduced in commit | B (1×1) | C (1×1+3×3) | D (sliding) |
|---|---|:---:|:---:|:---:|
| `3x3 depthwise CFU used` (`src/mnv2_app.cc`) | `42c42a5` | absent | present | present |
| `Output FNV1a : 0x…` (`src/mnv2_app.cc`) | `b82da40` | absent | absent | present |
| DEPTHWISE_CONV_2D ticks (17 events) | – | 569,466 | 360,818 | 309,533 |

- **B** predates the 3×3 CFU (no marker), and its depthwise layers are
  the slowest, consistent with software depthwise.
- **C** was built from `42c42a5` or `35e4493` (has the 3×3 marker, lacks
  the `b82da40` FNV line). The log cannot tell these two apart:
  `42c42a5` has a single-cycle RUN, `35e4493` a 3-stage pipelined RUN.
  **[REQUIRED] confirm which commit produced this log.**
- **D** was built from `b82da40` or later (sliding-window commit).

### Vivado reports

Confirmed from the hierarchical utilization contents:

| Report set | `depthwise_3x3` instance | `depthwise_3x3` LUT / FF | Interpretation |
|---|---|---|---|
| `cfu_1x1/` | absent | – | 1×1-only CFU (B) |
| `cfu_1x1_3x3/` | present | 198 / 394 | 3×3 MAC without window registers. 394 FF fits `35e4493` (9×20-bit product regs + 3-stage adder pipeline) (C) |
| `sliding_window/` | present | 1,136 / 576 | +182 FF = 18 × 10-bit `input_window`/`weight_window` registers, + LUTs for the 9-product refresh path of `b82da40` (D) |

The post-route critical path of C ends at
`Cfu/fn0/depthwise_3x3/dw_product_6_reg[19]`, a register that exists only
from `35e4493` on. So C's Vivado build is from `35e4493`, not `42c42a5`.

Report dates (Vivado header): C = Tue Oct 6 18:53–18:54, D = Wed Oct 7
09:34–09:35, B = Wed Oct 7 10:00–10:02 (B was rebuilt last, from a
1×1-only source tree).

## Open questions

- **[REQUIRED]** Platform of the runtime logs: the logs do not say whether
  they come from the Nexys4 DDR board or from simulation (Renode/Verilator).
  Board runs are assumed nowhere in the tables until confirmed.
- **[REQUIRED]** Exact commits for each runtime log and Vivado build.
- **[REQUIRED]** Confirmation that each runtime log was produced from the
  same bitstream/gateware as the matching Vivado report.
