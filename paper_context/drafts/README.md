# Drafts

The paper is a Word document built on `../conference/conference-template-letter.docx`
(Strict OOXML: Word and LibreOffice open it, pandoc cannot). Edit the
newest `MCSoC2026_MaxMarvels_Paper_Draft_v*.docx` directly and keep a PDF
rendering next to it for page-layout checks:

```
soffice --headless --convert-to pdf --outdir paper_context/drafts \
    paper_context/drafts/MCSoC2026_MaxMarvels_Paper_Draft_vN.docx
```

| Version | Content |
|---|---|
| v5 | Revised Introduction and Background/Related Work (explicit research gap, Sec. II-D) on top of the long v2 Sections III–V |
| v4 | Kasunya's condensed draft (`kasunya_3x3_cfu` @ `a1600a2`), source of v6 Sections III–V |
| v6 | **Current.** v5 Introduction and Background + Kasunya's condensed Sections III–V (`kasunya_3x3_cfu` @ `a1600a2`), with abstract, limitations, conclusion and reconciled references. 4 pages |

Open items in v6: figures 1–3 (boxes reserve the space) and the cycle-count
platform in Table II (board or simulation).

Rules: prose uses only facts from `../EXPERIMENTAL_RESULTS.md` (verified
section), `../ARCHITECTURE_NOTES.md` and references tracked in
`../LITERATURE_INDEX.md`. Research figures belong in `../figures/`.
