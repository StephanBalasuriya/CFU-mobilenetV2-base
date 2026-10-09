# Source Index

Source-of-truth index for the paper, at merge commit `74cdc33` (branch
`mindi`). Paths are relative to the repository root.

"Authoritative" means the file can be cited as evidence for the
implementation or for a result without further confirmation.

## RTL

The CFU RTL is written in Amaranth (Python HDL); Verilog is generated.

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/gateware/mnv2_cfu.py` | Top CFU, opcode map, both datapaths | Core | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/macc.py` | `Depthwise3x3Mac` (3×3 + SHIFT), `Madd4Pipeline` (1×1) | Core | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/sequencing.py` | 1×1 sequencer | 1×1 path | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/store.py` | Input/filter/param stores | 1×1 path | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/post_process.py` | 1×1 hardware requantization | 1×1 path | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/registerfile.py` | funct7 dispatch / `Xetter` | Both | YES (implementation) |
| `proj/mnv2_cfu_package/gateware/config.py` | Memory depths | Both | YES (implementation) |
| `proj/mnv2_cfu_package/cfu.v` | Generated Verilog | Build output | NO — git-ignored and dated 2026-10-03, i.e. older than the merged sliding-window code; regenerate before any synthesis |
| `proj/mnv2_cfu_package/cfu/gateware/*` | Vendored copy of `mnv2_first` gateware | Original 1×1 CFU reference | NO — does not contain the 3×3 CFU |
| `proj/mnv2_first/gateware/*` | Upstream CFU-Playground `mnv2_first` CFU | Provenance of the 1×1 CFU | YES (for "existing CFU" provenance only) |
| `soc/` | LiteX SoC + VexRiscv variants | Platform | YES (platform) |

## C/C++

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/src/mnv2_cfu.h` | CFU instruction macros (10–34, 40–44, 112) | Interface | YES (implementation) |
| `proj/mnv2_cfu_package/src/mnv2_app.cc` | Inference app; Top-1, `Output FNV1a` | Evaluation harness | YES (implementation) |
| `proj/mnv2_cfu_package/src/software_cfu.cc` | Software model of 1×1 CFU ops | Not used for 3×3 | YES (implementation) |
| `proj/mnv2_cfu_package/src/cat_image.h`, `cat_image.dat` | Input image | Evaluation input | YES |

## Python

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/cfu_gen.py` | Generates `cfu.v` | Build | YES (implementation) |
| `proj/mnv2_cfu_package/tools/image_to_header.py` | Image → C header | Input prep | YES (implementation) |
| `proj/mnv2_cfu_package/tools/generate_labels_header.py` | Labels header | App | YES (implementation) |
| `scripts/pyrun` | Runs Python in the project environment | Test runner | YES |

## TFLM integration

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/src/tensorflow/lite/kernels/internal/reference/integer_ops/conv.cc` | 1×1 eligibility + dispatch (`ACCEL_CONV`) | 1×1 path | YES (implementation) |
| `proj/mnv2_cfu_package/src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_conv.cc/.h` | 1×1 CFU driver | 1×1 path | YES (implementation) |
| `proj/mnv2_cfu_package/src/tensorflow/lite/micro/kernels/depthwise_conv.cc` | 3×3 eligibility, dispatch, `DW3X3_VERIFY` counters | 3×3 path | YES (implementation) |
| `proj/mnv2_cfu_package/src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_depthwise_conv.h` | 3×3 + sliding-window kernel | 3×3 path | YES (implementation) |
| `proj/mnv2_cfu_package/model/mobilenetv2_a035_224_int8.tflite` | Evaluated model | Workload | YES |

## Build/configuration

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/Makefile` | `ACCEL_CONV`, `DW3X3_VERIFY`, model selection | Build flags | YES |
| `proj/mnv2_baseline/Makefile` | CPU-only baseline project | Baseline | YES |
| `proj/proj.mk` | Common build rules (`pytest`, `renode`, …) | Build | YES |
| `environment`, `env/` | Toolchain environment | Build | NO (environment, git-ignored `env/`) |

## Tests

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/gateware/test_depthwise_macc.py` | 3×3 MAC, SHIFT_RIGHT, sliding row, latency | 3×3 verification | YES — part of 25/25 run on 2026-10-07 |
| `proj/mnv2_cfu_package/gateware/test_mnv2_cfu.py` | Full CFU via instruction interface incl. opcodes 40–44 | Integration | YES — part of 25/25 |
| `proj/mnv2_cfu_package/gateware/test_{macc,sequencing,store,output,post_process,registerfile}.py` | 1×1 sub-block tests | 1×1 verification | YES — part of 25/25 |
| Host functional-equivalence test (400/400) | — | Claimed result | NOT FOUND in repository |

Run: `cd proj/mnv2_cfu_package && ../../scripts/pyrun -m unittest discover -s gateware -t . -p 'test_*.py'`

## Experimental logs

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| — | No committed Renode/board run logs | Cycle results | — Logs must be added under `paper_context/project/` |
| `proj/mnv2_cfu_package/build/`, `soc/build/` | Local build outputs | Build artifacts | NO (git-ignored) |

## Vivado reports

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| — | No utilization or timing reports in the repository | Resources/timing/Fmax | — Must be added under `paper_context/project/` |

## Existing documentation

| Path | Purpose | Relevance | Authoritative |
|---|---|---|---|
| `proj/mnv2_cfu_package/README_MNV2_EXISTING_CFU.md` | 1×1 CFU description; 448,959,843 cycles | 1×1 reference result | PARTIAL — result is Renode/Verilator sim, no raw log; its "Important Scope" diagram is outdated (shows depthwise → CPU) |
| `proj/mnv2_baseline/README_MNV2_CPU_BASELINE.md` | CPU baseline; 1,216,227,740 cycles | Baseline reference | PARTIAL — sim, no raw log |
| `proj/mnv2_cfu_package/README.md` | Build/run instructions | Methodology | PARTIAL — some commands reference `proj/mnv2_cfu` (old name) |
| `proj/mnv2_first/src/README.md` | Upstream mnv2_first notes | Provenance | NO |
| `../../paper/main.tex` (outside repo, `/home/students/fyp_22_MaxMarvels/paper/`) | Pre-existing LaTeX stub ("CFU Playground Research") | None yet | NO |
