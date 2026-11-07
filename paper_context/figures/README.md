# Figures

Final paper diagrams and graphs. Planned figures are listed in
`../README_PAPER_CONTEXT.md`.

| Subdirectory | Contents |
|---|---|
| `architecture/` | System-level architecture figures (TFLM → VexRiscv → CFU → FPGA) |
| `diagrams/` | Technical diagrams: 3×3 depthwise datapath, sliding-window reuse, MobileNetV2 operator mapping / CFU coverage |
| `graphs/` | Measured performance, resource and instruction-count graphs |

Rules:

- Diagrams must match the source code (`../ARCHITECTURE_NOTES.md`).
- Graphs are plotted only from files in `../evidence/`. Keep the plotting
  script and its input data next to each graph.
- Keep editable sources (e.g. `.drawio`, `.svg`, script) together with the
  exported PDF/PNG.
