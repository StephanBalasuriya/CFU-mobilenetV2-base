# Literature Index

Tracking list for references. Do not fill in bibliographic details from
memory — only from the paper itself (in `literature/`) or an authoritative
source (publisher page, DOI record). PDFs go in `literature/`.

| # | Work | Status | File | Citation | Relevance |
|---|---|---|---|---|---|
| 1 | CFU Playground / Prakash et al. | USED [4] | `literature/CFU Playground.pdf` | arXiv:2201.01863v3, 2023 (check for published version) | Closest system; 55× op / 3× model; DW access-pattern remark |
| 2 | CFU Playground / DATE 2023 | NOT USED ([4] covers the CFU interface) | `literature/CFU Playground_Want A ML Processor.pdf` | DATE 2023 | CFU interface (2 operands, 1 result) |
| 3 | Yildirim & Ozturk 2025 | USED [8] | `literature/RISCV_BasedTinyML_Accelerator_…pdf` | arXiv:2511.21232, 2025 | Fused DSC CFU, 16,484 LUT / 173 DSP, NLR depthwise |
| 4 | Véstias et al. | USED [9] (metadata incomplete) | `literature/DSP Block.pdf` | **Venue/year not in PDF** | Mixed DSP/LUT MACs |
| 5 | Li et al. 2022 | USED [6] | `literature/A_digital_signal_processor-efficient_accelerator_f.pdf` | Electron. Lett. 58(7):271–273, 2022, doi:10.1049/ell2.12435 | DWC reuse limits, DSP packing, 392 DSPs |
| 6 | Sabih et al. 2024 | USED [7] | `literature/Hardware Software CoDesign of RISCV Extensions…pdf` | FPT 2024 | Sparse CFU extensions |
| 7 | MobileNetV2 | USED [2] (secondary) | **PDF missing** | Sandler et al., CVPR 2018 (from refs of [6], [7]) | Workload |
| 8 | MobileNetV3 | ADDED, not used | `literature/searching for mobilenetv3.pdf` | arXiv:1905.02244 | – |
| 9 | MLPerf Tiny | USED [1] | `literature/MLPerf Tiny Benchmarking.pdf` | arXiv:2106.07597, 2021 | TinyML constraints |
| 10 | TFLM (David et al.) | USED [3] (secondary) | **PDF missing** | Proc. MLSys vol. 3, 2021 (from refs of [5]) | Runtime |
| 11 | Vahdatpour & Zhang 2026 | USED [5] | `literature/EnergyEfficient…pdf` | arXiv:2603.23668, 2026 | Data movement limits |
| 12 | Banbury et al. (Benchmarking TinyML) | ADDED, not used | `literature/benchmarking tinyml systems.pdf` | arXiv:2003.04821 | – |
| 13 | Gray et al. (Composable CFUs) | ADDED, not used | `literature/Composable Custom Extensions…pdf` | poster abstract | – |

Reference numbers [n] are those of the current paper draft
(`drafts/`, latest version), numbered in order of first citation.

Status values: NOT ADDED → ADDED (PDF in `literature/`) → VERIFIED
(citation checked against an authoritative source) → USED (cited in the paper).

## Citation / claim audit

| Claim in the paper | Ref | Verified in |
|---|---|---|
| Embedded inference under tight memory, latency and energy budgets | [1] | `MLPerf Tiny Benchmarking.pdf` (KB-scale models; latency and energy metrics) |
| Inverted residual block: 1×1 expansion, 3×3 depthwise, 1×1 projection | [2] | **Secondary**: described in [8] §II; [2] PDF not in `literature/` |
| TFLM runs one kernel per operator | [3] | **Secondary**: [3] PDF not in `literature/`; consistent with the repository kernels |
| CFU Playground: tightly coupled R-type CFU (two operands, one result, internal state); LiteX/VexRiscv; MobileNetV2 1×1 CFU with 4-way INT8 MACs and HW requantization; 3× whole-model speedup; depthwise left in software | [4] | `CFU Playground.pdf` §III, §V-B.1, footnote 3; repo `proj/mnv2_first` has no depthwise kernel override |
| KWS case study: depthwise uses one lane of the 4-way MAC CFU; separate depthwise CFU did not fit | [4] | `CFU Playground.pdf`, KWS-on-Fomu case study |
| Data movement increasingly limits ML hardware performance/energy | [5] | `EnergyEfficient…pdf` abstract |
| Depthwise: no cross-channel input reuse ("only weights can be reused"); two 8-bit multiplications per DSP | [6] | `A_digital_signal_processor-efficient_…pdf` |
| RISC-V extensions for sparse, pruned DNNs | [7] | `Hardware Software CoDesign…pdf` (FPT 2024) |
| Fused expansion→depthwise→projection CFU on CFU Playground/VexRiscv; layer-level speedups (59.3× on 3rd layer); SoC grows from 4,438 to 20,922 LUTs and 5 to 178 DSPs | [8] | `RISCV_BasedTinyML_…pdf`, Tables I–IV, §IV |
| Mixed DSP/LUT parallel 8-bit MAC units | [9] | `DSP Block.pdf` |

### Claims deliberately not made

- No "first"/"novel" claim, and no "no standalone 3×3 depthwise CFU exists"
  claim: other CFU Playground projects (`kws_micro_accel`, `proj_accel_1`)
  use CFU instructions inside depthwise loops, and [8] has a fused
  depthwise stage.
- No speedup versus CPU-only (no CPU-only log on the current platform).
- No efficiency comparison with [8] (different clock, 100 MHz vs 75 MHz;
  per-layer vs whole-model metrics).
- The 4-way MAC and the 1×1 CFU are CFU Playground's, not ours.

## Open literature/metadata items

1. Add the MobileNetV2 [2] and TFLM [3] PDFs to `literature/`.
2. Véstias et al. [9]: venue and year are not in the PDF (PDF created 2017).
   Find the published version or drop [9].
3. CFU Playground [4] is cited as arXiv v3 (2023); check for a
   peer-reviewed version. [5] and [8] are arXiv preprints.
