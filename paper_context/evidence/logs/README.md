# Experimental Logs

Raw or summarized experimental logs that do not belong to a single
`runtime/`, `vivado/` or `verification/` category, such as UART/Renode
console captures and profiler dumps.

Name files so their status is obvious, and use these prefixes or
subdirectories where appropriate:

- `current_` — produced from the current `mindi` code; may support claims.
- `historical_` — valid for an older design point (e.g. 1×1-only, or 3×3
  before `35e4493` timing fix); may be cited only as such.
- `superseded_` — replaced by a newer measurement; keep for traceability,
  never cite.

Each log starts with (or is accompanied by) its commit hash, command,
platform and date.

## Existing logs in the repository (2026-10-07)

| Path | Status | Notes |
|---|---|---|
| `proj/mnv2_baseline/baseline_build.log` | Not evidence | Build log from another machine; ends in `collect2: error: ld returned 1 exit status`. No cycle data. |
