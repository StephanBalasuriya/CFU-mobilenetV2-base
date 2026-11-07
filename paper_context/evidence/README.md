# Evidence

Authoritative evidence supporting paper claims. A number may appear in the
paper only if the file backing it is stored here (or its original
repository path is referenced here) and it is entered in
`../EXPERIMENTAL_RESULTS.md`.

| Directory | Contents |
|---|---|
| `vivado/` | Synthesis, implementation, utilization, timing and FPGA reports |
| `runtime/` | MobileNetV2 execution logs and measured cycle/instruction counts |
| `verification/` | Gateware and functional-equivalence test evidence |
| `logs/` | Raw or summarized experimental logs (current / historical / superseded) |

Rules:

- Never create, edit or "clean up" a report or log by hand. Store the tool
  output as produced.
- Every evidence file records: commit hash, build command, platform
  (Renode/Verilator simulation or physical board), and date.
- Empty directories mean the evidence does not exist yet.
