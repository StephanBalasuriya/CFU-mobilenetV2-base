# Experimental Results Ledger

Every value in this file states its source. A value supplied verbally or
from notes outside the repository is not "verified" until a log or report
backing it is committed under `paper_context/project/` (or elsewhere in the
repository) and referenced here.

Status of this ledger: created 2026-10-07 at merge commit `74cdc33`.

## VERIFIED CURRENT RESULTS

### V1. Gateware unit tests — 25/25 pass

- **Value:** 25 tests, 25 pass (`Ran 25 tests ... OK`).
- **How verified:** re-run on 2026-10-07 on merge commit `74cdc33`:
  `cd proj/mnv2_cfu_package && ../../scripts/pyrun -m unittest discover -s gateware -t . -p 'test_*.py'`
- **Covers:** `gateware/test_*.py`, including `test_depthwise_macc.py`
  (3×3 MAC vectors, `SHIFT_RIGHT`, sliding row with signed offsets, LOAD
  after SHIFT/latency) and `test_mnv2_cfu.py::test_depthwise_3x3_shift_right`
  (opcodes 40–44 through the real CFU instruction interface).
- **Environment:** Amaranth pysim (Python), not FPGA.

### V2. 3×3 depthwise CFU instruction counts (whole model, one inference)

Re-derived analytically on 2026-10-07 from the counting formula in
`src/tensorflow/lite/micro/kernels/depthwise_conv.cc` (`Dw3x3VerifyReport`)
and the MobileNetV2-0.35-224 depthwise layer shapes. The model contains
explicit `PAD` ops before the stride-2 depthwise layers
(`block_{1,3,6,13}_pad`), so stride-2 layers have no border windows. All
values match the figures previously reported by the team exactly:

| Instruction | Before (3 LOADs/window) | After (sliding window) |
|---|---:|---:|
| LOAD (op 40) | 2,529,552 | 726,864 |
| SHIFT_RIGHT (op 44) | 0 | 600,896 |
| RUN (op 41) | 843,184 | 843,184 |
| GET_RESULT (op 42) | 843,184 | 843,184 |
| CONFIGURE (op 43) | 17 | 17 |

- **LOAD reduction:** 1 − 726,864 / 2,529,552 = 0.712651 → **71.27 %**
  when rounded (71.26 % if truncated). Use one convention consistently.
- **Caveat:** this is an analytical cross-check of the source, not an
  on-board counter log. A `make DW3X3_VERIFY=1` run log should be added
  under `project/` to make it measured evidence. Instruction counts are not
  a speedup.

### V3. Existing 1×1 CFU vs CPU-only (repository-documented)

Source: `proj/mnv2_cfu_package/README_MNV2_EXISTING_CFU.md` and
`proj/mnv2_baseline/README_MNV2_CPU_BASELINE.md`.

| Configuration | Whole-model cycles |
|---|---:|
| CPU-only baseline (`mnv2_baseline`, `NO_CFU=1 SW_ONLY=1`) | 1,216,227,740 |
| Existing 1×1 CFU (`mnv2_cfu_package`, before 3×3 work) | 448,959,843 |

- Speedup 2.709×, cycle reduction 63.09 % (computed from these numbers).
- Measured in **Renode/Verilator simulation** (README states "not physical
  FPGA timing or power measurements"). Same model, same cat image.
- No raw log is committed; only the README text.

### Values supplied by the team that could NOT be confirmed in the repository

These are not entered as verified. Each needs its source log/report.

| Item | Supplied value | Status |
|---|---|---|
| CPU-only cycles | 1,216,038,298 | Not found in repository. Differs from README value 1,216,227,740 (−0.016 %). |
| Existing 1×1 CFU cycles | 448,945,811 | Not found in repository. Differs from README value 448,959,843 (−0.003 %). |
| Speedup | 2.708× | Consistent with the supplied pair (2.7087×); README pair gives 2.7090×. |
| Cycle reduction | 63.08 % | Consistent with the supplied pair (63.081 %); README pair gives 63.086 %. |
| Host functional equivalence | 400/400 | No host-equivalence test or log exists in the repository. |
| Timing | WNS = +0.243 ns, TNS = 0.000 ns, 0 failing endpoints | No Vivado timing report in the repository. |
| Top-level resources | LUT 6192, FF 4504, RAMB36 15, RAMB18 33, DSP 8 | No Vivado utilization report in the repository. |
| CFU hierarchy resources | LUT 1514, FF 1081, RAMB36 4, RAMB18 8, DSP 4 | No Vivado utilization report in the repository. |

Before using either cycle pair, decide which run is current (environment,
image, commit) and record the log. Do not mix the two pairs in one table.

## RESULTS STILL REQUIRED

- [REQUIRED] Final controlled end-to-end cycle count: 1×1 + 3×3 depthwise
  CFU (no sliding window), same model/image/arena/profiler as baseline.
- [REQUIRED] Final controlled end-to-end cycle count: 1×1 + 3×3 + sliding
  window (current `b82da40` code).
- [REQUIRED] Matching CPU-only and 1×1-only cycle counts from the same
  environment and commit family, with raw logs.
- [REQUIRED] Per-operator cycle breakdown (TFLM profiler) for each
  configuration, especially `DEPTHWISE_CONV_2D` and `CONV_2D`.
- [REQUIRED] Measurement platform statement: Renode/Verilator simulation
  vs. physical board (Arty?) — current repository evidence is simulation only.
- [REQUIRED] Functional equivalence evidence: per-layer FNV-1a checksums
  (`DW3X3_VERIFY=1`) and final `Output FNV1a` / Top-1 for CPU vs CFU runs.
- [REQUIRED] Host functional-equivalence test (400/400) source and log.
- [REQUIRED] On-target `DW3X3_VERIFY=1` instruction-count log (to promote V2
  from analytical to measured).
- [REQUIRED] Final optimized Vivado resource report (top level and CFU
  hierarchy) for the merged 1×1 + 3×3 + sliding-window CFU.
- [REQUIRED] Final Vivado timing report (WNS/TNS/failing endpoints) and the
  target clock.
- [REQUIRED] Final Fmax.
- [REQUIRED] Resource/timing of the 1×1-only CFU for an area-overhead
  comparison (optional ablation).

## HISTORICAL / SUPERSEDED RESULTS

| Source | Value | Reason historical / superseded |
|---|---|---|
| `proj/mnv2_cfu_package/README_MNV2_EXISTING_CFU.md` | 1×1 CFU 448,959,843 cycles | Measured on the 1×1-only package before the 3×3 depthwise path existed; valid as the "existing CFU" reference point but not a measurement of the current merged design. Kept in V3 as a reference, not a current-design result. |
| `proj/mnv2_cfu_package/README_MNV2_EXISTING_CFU.md` ("Important Scope" section) | Architecture diagram shows "Depthwise CONV → CPU" | Superseded by the 3×3 depthwise CFU path; the same README's earlier section already lists "eligible 3x3 depthwise → Dedicated depthwise CFU". |
| Commit `42c42a5` (first 3×3 CFU) | Design: raw words stored on LOAD; nine combinational multipliers + `tree_sum` registered in one cycle on RUN | Superseded by `35e4493` ("timing violation fixed"): products registered during LOAD, then a 3-stage pipelined accumulation. Any timing/resource numbers taken before `35e4493` are historical. |
