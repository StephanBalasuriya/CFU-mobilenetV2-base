# Document Layout Check — MCSoC 2026 Paper Draft

Date: 2026-10-07. Nothing committed.

## Files

| Item | Path |
|---|---|
| Source template (read-only) | `paper_context/conference/conference-template-letter.docx`. MD5 `6b4f836483b5a5e01781f8e3c444a861`, unchanged before/after |
| Output document | `paper_context/drafts/MCSoC2026_MaxMarvels_Paper_Draft.docx` |
| Generator (source of truth for text) | `paper_context/drafts/scripts/build_docx.py` (`CONTENT` list) |

The generator opens a copy of the template and keeps verbatim: the title
paragraph format, the author grid (4-column sections), the section breaks,
page setup, styles, numbering, footer and settings. It replaces only the
template's guidance paragraphs. Rebuild with
`python3 paper_context/drafts/scripts/build_docx.py`. (The earlier Markdown
section drafts were removed in the workspace cleanup; the script holds the
current text.)

## Format checks

| Check | Result |
|---|---|
| A. Template unmodified | PASS (MD5 identical) |
| B. Opens correctly | PASS: LibreOffice renders it; skill validator (XSD, against original) "All validations PASSED". The template is **Strict OOXML**, so pandoc cannot read it; Word and LibreOffice can |
| C. Genuine IEEE two-column | PASS: template's own section with `w:cols w:num="2" w:space="18pt"`; title/author area single-column + 4-column author grid; US Letter 612×792 pt; margins top 54 pt, bottom 72 pt, left/right 44.65 pt (template values) |
| D. Headings | PASS: template styles `Heading1` (auto "I.", small caps), `Heading2` (auto "A.", italic), `Heading5` (References). Separate-line, not run-in (see note) |
| E. Citations | PASS: [1]–[10], numbered in order of first citation; all cited in text; bibliography uses template `references` style (auto "[n]") |
| F. Overflow/clipping | PASS: no clipped text in the rendered PDF |
| G. Placeholders vs layout | PASS: 3 single-column bordered boxes (2.0 / 1.4 / 1.8 in) + `figurecaption` captions (auto "Fig. n."); no column breakage |
| H. Page count | **3 pages** (rendered with LibreOffice; Liberation Serif = metric-compatible Times New Roman) |
| I. Title/author/abstract/keyword placeholders | Title set; author grid = template's 6 placeholder blocks; abstract = marked placeholder; keywords = proposed list marked [PROPOSED] |
| J. Unsupported claims | None found. Every number is traced in `README_DRAFT_NOTES.md`. One generalization fixed during build ("standalone accelerators use hundreds of DSP slices" → "a standalone accelerator uses 392 DSP slices [7]") |

**Heading note.** The template has no lettered run-in subsection style:
`Heading4` is run-in but numbered "1)". The draft therefore uses the
template's standard `Heading2` (A., B., …). Converting the nine subsection
heads to run-in text would save ≈ 9 lines; decide at the page-fitting
stage.

## Content placement (rendered)

| Section | Words (body) | Location |
|---|---:|---|
| Title + author grid + abstract/keywords | – | p.1 top ≈ 45% |
| I. Introduction | 512 | p.1 left col (from ≈ 50%) → p.1 right col → p.2 left col top (last two contribution bullets) |
| Fig. 1 placeholder (2.0 in) + caption | 23 | p.2 left col |
| II. Background and Related Work | 610 (incl. Fig. 2 caption) | p.2 left col (lower half) → p.2 right col (full) |
| Fig. 2 placeholder (1.4 in) + caption | – | p.2 left col bottom |
| III–VII placeholders + Fig. 3 (1.8 in) | ≈ 130 | p.2 right col bottom → p.3 left col → p.3 right col top |
| References [1]–[10] | 240 | p.3 right col, ≈ 45% of the column |

Page breaks: p.1→p.2 inside contribution bullet 2 ("Sliding-window reuse");
p.2→p.3 inside the Section III placeholder.

**Budget implication.** Real content occupies ≈ 2.4 pages, including the
3 figure boxes and references. Under a 4-page limit, Sections III–VII plus
the abstract (~150 words) have about **1.6 pages**. Results also need
tables/graphs (e.g., Fig. `end_to_end_performance`, resource table). Expect
to trim Sections I–II by ~15–20% and/or use run-in subsection heads at the
fitting stage.

## Unresolved evidence items

| Tag | Item | Status |
|---|---|---|
| [E1] | Runtime logs: single run each; board vs simulation and commit not stated | Open |
| [E2] | **CPU-only baseline**: `paper_context/evidence/runtime/cpu_only/` does not exist on `mindi` (or any branch history). 1,216,038,298 appears only in our own notes as unverified. CPU-only is kept as a configuration with **no number**. | Open |
| [E2-note] | The quoted CPU-only 1,216,038,298 was paired with a 1×1 run of **448,945,811** cycles. The current controlled 1×1 log is **828,991,457** cycles (same model and input FNV `0xbe3b0c0b`). These come from different setups. Even with its log found, 1,216,038,298 is only a valid baseline if its setup matches the current 1×1/3×3/SW runs. The ~877,223,683-cycle FPGA run mentioned in the brief is not in the repository and is not used anywhere. | Open |
| [E3] | LOAD/SHIFT counts analytical (no `DW3X3_VERIFY=1` log) | Open |
| – | 400/400 host equivalence: summary document only, no test source/log (not cited in I–II) | Open |
| – | CPU variant ("VexRiscv_FullCfu") not confirmed by reports; text says "VexRiscv" | Open |

Evidence tags are **visible in the document text** so they cannot be
missed. Remove each tag only after the item is resolved.

## Unresolved citation items

- [2] MobileNetV2 and [3] TFLM: metadata from secondary reference lists,
  PDFs not in `literature/` (marked "[VERIFY …]" in the bibliography).
- [8] Véstias et al.: venue/year unknown (marked). Drop if not found; [7]
  covers DSP packing.
- [4] CFU Playground: cited as arXiv v3; check for a published version
  (marked "[CHECK …]").
- [6], [10]: arXiv preprints; check for published versions.

## Formatting issues / template leftovers to handle later

- Copyright footer on p.1 still shows the template placeholder
  `XXX-X-XXXX-XXXX-X/XX/$XX.00 ©20XX IEEE`. Replace with the code supplied
  by MCSoC at camera-ready.
- Author grid: template's 6 placeholder authors. Reduce to the real author
  count (the template's instructions: change the author section's columns).
- The template's funding text box ("Identify applicable funding agency…")
  was removed together with the guidance body. Re-add if there is funding
  to acknowledge.
- No Acknowledgment section yet (template's `Heading5`).
- Page limit not stated in the CFP. Confirm "4 pages" on EDAS before
  fitting.
- Rendering used Liberation Serif in place of Times New Roman. Confirm
  final page count in Microsoft Word.
