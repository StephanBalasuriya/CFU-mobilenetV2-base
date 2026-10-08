# MCSoC 2026 Paper Context

## Purpose

This directory is the persistent context for writing the MCSoC 2026
four-page short paper. It collects the verified project facts, results
ledger, architecture notes, source index, literature tracking and
conference material that every drafting session must start from.

Paper prose lives only in the Word drafts under `drafts/`.

## Current Git state

| Item | Value |
|---|---|
| Repository | `CFU-mobilenetV2-base` (`origin` = github.com/StephanBalasuriya/CFU-mobilenetV2-base) |
| Working branch | `mindi` |
| Synchronization merge commit | `74cdc33` — Merge remote-tracking branch 'origin/kasunya_3x3_cfu' into mindi |
| `origin/kasunya_3x3_cfu` merged | YES, at `b82da40` ("Implemented sliding buffer on top of 3x3 cfu"), which includes `35e4493` ("timing violation fixed") |
| Earlier merge of the same branch | `e346df0` (merged `42c42a5`, "implemented cfu for 3x3 depthwise") |
| Synchronization date | 2026-10-07 |
| Conflicts | None |

## Current project direction

Based only on the synchronized repository (`proj/mnv2_cfu_package`):

- **Model:** INT8 MobileNetV2, width multiplier 0.35, 224×224 input
  (`model/mobilenetv2_a035_224_int8.tflite`).
- **Platform:** TensorFlow Lite Micro on a VexRiscv RISC-V core with a
  CFU-Playground Custom Function Unit (CFU).
- **Existing 1×1 pointwise CFU:** inherited from CFU-Playground
  `mnv2_first`; accelerates eligible 1×1 `CONV_2D` layers.
- **3×3 depthwise CFU:** new opcodes 40–44 in the same CFU; accelerates
  eligible 3×3 `DEPTHWISE_CONV_2D` windows.
- **Sliding-window data reuse:** stride-1 horizontal reuse via a
  `SHIFT_RIGHT` instruction that inserts one new input column.
- **End-to-end evaluation:** whole-model cycle counts via the TFLM
  profiler for the 1×1, 1×1+3×3 and sliding-window configurations, plus
  Vivado reports for a Nexys4 DDR (xc7a100t) SoC at 75 MHz (see
  `EXPERIMENTAL_RESULTS.md`). The runtime logs do not state whether they
  ran on the board or in simulation, and the CPU-only log is still missing.

## Central paper story

The paper investigates extending an existing tightly coupled RISC-V CFU
MobileNetV2 execution path with:

1. lightweight 3×3 depthwise acceleration,
2. sliding-window data reuse,
3. end-to-end evaluation.

## Important rules

- No unsupported novelty claims.
- Do not claim the first 3×3 depthwise CFU.
- Do not claim novel DSP packing.
- Do not claim all MobileNetV2 operators are hardware accelerated. (Border
  windows, `PAD`, non-1×1 `CONV_2D`, `ADD`, pooling, etc. remain on the CPU.)
- Do not call LOAD-instruction reduction a speedup. It is an instruction
  count reduction; speedup needs measured cycles.
- Do not invent results. Use `[REQUIRED]` for anything not yet measured.
- Do not mix historical and current experiments.
- Do not describe simulation cycle counts as FPGA measurements.
- Source code and verified measurements take priority over assumptions.

## Planned paper structure

I. Introduction
II. Background and Related Work
III. Proposed System and CFU Architecture
IV. Experimental Methodology
V. Results and Discussion
VI. Conclusion
References

## Planned figures

These are planned figures only; none have been made yet.

- **Figure 1:** Overall RISC-V/TFLM/CFU architecture.
- **Figure 2:** MobileNetV2 computation mapping and CFU coverage.
- **Figure 3:** 3×3 depthwise CFU datapath and sliding-window reuse.
- **Figure 4:** End-to-end performance/ablation results.

## Files in this workspace

| File | Role |
|---|---|
| `EXPERIMENTAL_RESULTS.md` | Results ledger: verified / required / historical |
| `ARCHITECTURE_NOTES.md` | Source-derived architecture description |
| `SOURCE_INDEX.md` | Which repository files are authoritative |
| `LITERATURE_INDEX.md` | Reference tracking list |
| `PAPER_CLAIMS.md` | Claims we may / may not make |
| `conference/` | CFP and IEEE template |
| `literature/` | Reference PDFs |
| `evidence/` | Runtime logs, Vivado reports, verification logs and parsed tables |
| `figures/` | Result graphs (generated from `evidence/`) and diagram specs |
| `drafts/` | The paper (Word) and its PDF rendering |
