# Drafts

ONE paper, no per-section drafts.

| File | Role |
|---|---|
| `MCSoC2026_MaxMarvels_Paper_Draft.docx` | **Authoritative paper** (copy of the official IEEE template, two-column) |
| `MCSoC2026_MaxMarvels_Paper_Draft.pdf` | Current rendering, for visual/page-layout inspection |
| `scripts/build_docx.py` | Generator: holds the paper text (`CONTENT`) and inserts it into a copy of `../conference/conference-template-letter.docx` (the template itself is never modified) |
| `README_DRAFT_NOTES.md` | Evidence tags [E1]–[E3], citation/claim audit, open literature gaps |
| `DOCUMENT_LAYOUT_CHECK.md` | Layout verification of the generated DOCX |

Rebuild and render:

```
python3 paper_context/drafts/scripts/build_docx.py
soffice --headless --convert-to pdf --outdir paper_context/drafts \
    paper_context/drafts/MCSoC2026_MaxMarvels_Paper_Draft.docx
```

Rules: prose must use only facts from `../EXPERIMENTAL_RESULTS.md`
(verified section), `../ARCHITECTURE_NOTES.md` and references in
`../LITERATURE_INDEX.md`. Do not keep page-preview PNGs here; the PDF is
the inspection copy. Research figures belong in `../figures/`.

Note: once the team starts editing the DOCX directly in Word, the generator
must no longer be re-run (it would overwrite manual edits). Decide this
switch explicitly.
