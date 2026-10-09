# Correctness Results

| Verification | Result | Evidence |
|---|---|---|
| Gateware tests | **25 / 25 pass** | `../verification/gateware/gateware_unittest_b984b75.log`: raw unittest output, run 2026-10-07 on sliding-window code (`b984b75`, gateware identical to `b82da40`). Amaranth simulation, not FPGA. Also stated in `../verification/functional/baseline_functional_verification.txt`. |
| Functional equivalence (host) | **400 / 400 pass, 0 mismatches (reported)** | `../verification/functional/baseline_functional_verification.txt`, a written summary by the team. **No test source code or raw log** in the repository, so it is not reproducible from the evidence. The summary describes the *baseline* 3×3 CFU, not the sliding-window version. |
| MobileNetV2 Top-1 | **Class 64 (`green_mamba`), score 0.406250 in all three CFU configurations** | `../runtime/cfu_1x1/output.md`, `../runtime/cfu_1x1_3x3/output.md`, `../runtime/sliding_window/output.md` (`Top-1 class index : 64`, `Top-1 score : 406250 x 10^-6`) |
| Input checksum | **`0xbe3b0c0b` in all three logs** | Same three logs, `RGB FNV1a` line. Confirms identical input. |
| Output agreement / checksum | **Partial.** Top-1 index, Top-1 score, output min/max/mean and the first 20 outputs are identical across B, C and D. A full output checksum exists only for D: `Output FNV1a 0x2d8f8f61`. | Same three logs. B and C predate the `Output FNV1a` print (`b82da40`), so a byte-exact output comparison across configurations is **not possible** from current evidence. |
| CPU-only reference output | **MISSING** | No CPU-only runtime log, so agreement with the CPU reference cannot be shown. |

## Not verified / required

- [REQUIRED] Host functional-equivalence test source and raw log (400/400).
- [REQUIRED] `Output FNV1a` for CPU-only, 1×1 and 1×1+3×3 runs (rebuild with
  the current `mnv2_app.cc`), to show byte-identical outputs.
- [REQUIRED] Per-layer output checksums (`make DW3X3_VERIFY=1`) for C vs D.
