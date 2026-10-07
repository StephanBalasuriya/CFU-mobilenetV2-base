# Draft Notes (2026-10-07)

The paper text lives in ONE place: `scripts/build_docx.py` (`CONTENT`),
which generates `MCSoC2026_MaxMarvels_Paper_Draft.docx`. Edit the script,
not the DOCX, until the move to manual editing in Word is decided (see
`README.md`). The earlier Markdown section drafts were removed; their final
wording is in the script.

Sections I–II length: Introduction ≈ 480 words, Background ≈ 545 words, ≈ 1.1 IEEE
two-column pages including headings. Use run-in subsection headings
(`\paragraph{}`-style) in LaTeX to save ~8 lines.

The CFP (`conference/R2-MCSOC2026_CFP.pdf`) states **no page limit**. The
4-page limit comes from the team brief and must be confirmed on EDAS
(https://edas.info/N34632). Suggested track: *Hardware Acceleration of AI
on Embedded Edge SoCs*. Submission deadline: **Oct 10, 2026 (hard)**.

## Evidence tags used in the text

| Tag | Sentence(s) | Status | Resolution |
|---|---|---|---|
| [E1] | "about 70% of inference cycles"; "25.8% … 30.8%"; "all designs meet timing" | Verified from single-run logs (`evidence/tables/`), platform/commit unstated | State platform (board vs sim); ideally repeat runs |
| [E2] | "CPU-only" configuration | **Missing.** 1,216,038,298 cycles is an UNVERIFIED historical note (paired with a 448,945,811-cycle 1×1 run from a different setup; current 1×1 = 828,991,457). The ~877,223,683 FPGA figure has no evidence. Neither is used | Keep CPU-only as a configuration; add a CPU-only log from the same setup as the current runs |
| [E3] | "removes 71.3% of 3×3 CFU LOAD instructions" | **Analytically derived from the instruction-generation/execution structure** (kernel loop + `Dw3x3VerifyReport` formula); matches team counts; NOT a measured runtime log | Add `DW3X3_VERIFY=1` log, or present as "by construction" in Sec. III. Never call it a speedup |

All other numbers are from the cited papers (see audit) or from post-place
/ post-route Vivado reports (+167 LUT, +394 FF, 0 DSP, 0 BRAM; 75 MHz met).

## Why this framing is acceptance-oriented

- **Embedded-SoC problem first.** The argument is about operator coverage
  under a resource budget in a CPU+CFU SoC, which fits the CFP's
  "Hardware Acceleration of AI on Embedded Edge SoCs" track.
- **The gap comes from the cited papers themselves.** CFU Playground
  reports 55× on the operator but 3× on the model, and that a depthwise CFU
  did not fit. Yildirim & Ozturk use a no-local-reuse depthwise dataflow at
  16k LUTs / 173 DSPs. The gap needs no "first" claim.
- **Honest positioning.** Specialized designs are credited with larger
  per-layer gains, and our design point is cost-constrained coverage, not
  peak speedup. Reviewers who know [6] will see we have read it.
- **Operator vs end-to-end** is made explicit (55× vs 3×; LOAD reduction
  explicitly not a speedup), which guards against the most likely reviewer
  objection.
- **Contributions match what was built and measured.** None depends on
  DSP packing or novelty of the 4-way MAC.

## Citation / claim audit

| Claim | Ref | Verified in |
|---|---|---|
| Embedded memory budgets (KB–MB), latency/energy as TinyML metrics | [1] | MLPerf Tiny: models 96–325 KB; "memory (GBs)" too large; measures accuracy, latency, energy |
| Inverted residual block: 1×1 expansion, 3×3 depthwise, 1×1 projection | [2] | **Secondary**: described in [6] §II; [2] PDF not in `literature/` |
| TFLM integer kernels, one kernel per operator | [3] | **Secondary**: [3] PDF not in `literature/`; consistent with repo kernels |
| MNV2 baseline ≈900 M cycles; 1×1 63%, DW 22.5%, 3×3 11%; 55× operator; 3× overall; 4-way MAC; HW requantization | [4] | `CFU Playground.pdf` §V-B.1 and footnote 3 |
| Depthwise has a "different memory access pattern"; separate DW CFU did not fit | [4] | `CFU Playground.pdf`, KWS-on-Fomu case study |
| CFU = in-pipeline, R-type, two operands / one result, multi-instruction sequences, CFU state | [5] | `CFU Playground_Want A ML Processor.pdf` |
| Fused Ex→Dw→Pr CFU, 59.3× on 3rd block, accelerator 16,484 LUT / 173 DSP, base SoC 4,438 LUT, NLR depthwise dataflow | [6] | `RISCV_BasedTinyML_…pdf`, Tables II–IV, §IV |
| DWC: no cross-channel reuse, "only weights can be reused"; 9×9 tile → 7×7 outputs; 392 DSPs; two 8×8 MACs per DSP | [7] | `A_digital_signal_processor-efficient_…pdf` |
| Mixed DSP/LUT parallel 8-bit MAC units | [8] | `DSP Block.pdf` |
| CFU Playground-based sparse extensions, pruned models | [9] | `Hardware Software CoDesign…pdf` (FPT 2024) |
| Data movement increasingly limits performance/energy | [10] | `EnergyEfficient…pdf` abstract |
| Our ~6× LUT / >40× DSP comparison | [6] + ours | 16,484/2,693 = 6.1×; 173/4 = 43× (our CFU, post-place) |

### Claims deliberately NOT made

- No "first" / "novel" anywhere. The gap is stated as "not characterized
  by these works".
- No speedup vs CPU (no CPU-only log).
- No comparison of our cycles with [4]'s or [6]'s absolute cycles: their
  platforms differ (Arty A7-35T and 100 MHz respectively), and [6]
  reports per-block speedups only.
- No claim that DSP packing or the 4-way MAC is ours. The 4-way MAC is
  CFU Playground's.
- No sliding-window/line-buffer novelty claim. Tiling reuse in dedicated
  accelerators is acknowledged ([7]).
- No claim that all operators are accelerated (§I-B, §II-B, §II-E).

## Literature / metadata gaps (resolve before freezing)

1. **Add MobileNetV2 PDF** (Sandler et al., CVPR 2018) to `literature/`.
   Currently cited from secondary reference lists.
2. **Add TFLM PDF** (David et al., MLSys 2021).
3. **Véstias et al. [8]**: venue and year are not in the PDF. Find the
   published version (IEEE Xplore / DBLP) or drop [8]. [7] alone supports
   the DSP-packing remark.
4. **CFU Playground [4]**: cited as arXiv v3 (2023). Check whether a
   peer-reviewed version exists and cite that.
5. [6] and [10] are arXiv preprints (2025, 2026). Acceptable, but check for
   published versions.
6. The brief names **"VexRiscv_FullCfu"**. The Vivado reports do not name
   the CPU variant (`soc/patch_cpu_variant.py` defines `full+cfu`). The
   text says only "VexRiscv". Confirm the variant before Sec. III.

## Note on the window illustration in the brief

The brief's example (`[a b c]/[e f g]/[h i j] → [b c d]/[e f g]/[h i j]`)
keeps rows 2–3 unchanged, which does not match the row-wise shift in
`Depthwise3x3Mac`. The text avoids a matrix and says "share six of nine
inputs". For figures use `figures/diagrams/sliding_window_diagram_spec.md`
(`A B C/D E F/G H I → B C J/E F K/H I L`).
