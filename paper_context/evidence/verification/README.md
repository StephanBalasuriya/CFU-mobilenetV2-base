# Verification Evidence

Gateware and functional-equivalence test evidence.

| Subdirectory | Contents |
|---|---|
| `gateware/` | Amaranth unit-test runs of the CFU (`proj/mnv2_cfu_package/gateware/test_*.py`) |
| `functional/` | End-to-end functional equivalence: CPU vs CFU output checksums, Top-1, per-layer `DW3X3_VERIFY` FNV-1a checksums, host equivalence tests |

## Existing evidence

| File | Result | Notes |
|---|---|---|
| `gateware/gateware_unittest_b984b75.log` | 25/25 OK | Real run captured 2026-10-07 on `mindi` commit b984b75 (code identical to merge `74cdc33`). Simulation (pysim), not FPGA. |

Test sources: `proj/mnv2_cfu_package/gateware/test_depthwise_macc.py`,
`test_mnv2_cfu.py` (incl. `test_depthwise_3x3_shift_right`), and the 1×1
sub-block tests.

Functional equivalence: `functional/baseline_functional_verification.md`
is a written summary reporting 400/400 host equivalence tests (0
mismatches) for the baseline 3×3 CFU and Top-1 class 64 / 0.406250. No
test source or raw log is in the repository. See
`../tables/correctness_results.md`. The repository provides the instrumentation to produce it:
`Output FNV1a` in `src/mnv2_app.cc` and per-layer checksums under
`make DW3X3_VERIFY=1`.
