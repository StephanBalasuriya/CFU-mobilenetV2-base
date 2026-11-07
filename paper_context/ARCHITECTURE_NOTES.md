# Architecture Notes

Derived from the synchronized source at merge commit `74cdc33` (branch
`mindi`). All paths are relative to `proj/mnv2_cfu_package/` unless noted.
Anything not confirmed by source is marked [UNCONFIRMED].

## 1. Overall system

```
TFLite Micro (INT8 MobileNetV2-0.35-224, src/mnv2_app.cc)
  → VexRiscv RISC-V CPU (CFU-Playground SoC, soc/)
  → CFU interface (custom R-type instruction, cfu_op0(funct7, in0, in1))
  → One CFU (gateware/mnv2_cfu.py :: Mnv2RegisterInstruction)
       ├─ existing 1×1 pointwise datapath (funct7 10–34, 112)
       └─ new 3×3 depthwise datapath     (funct7 40–44)
  → FPGA (Verilog generated to cfu.v by cfu_gen.py / Amaranth)
```

- Both datapaths live in the **same** CFU module and share the
  `RegisterFileInstruction` dispatch (`gateware/registerfile.py`); each
  funct7 value is a registered `Xetter`.
- Build switches (`Makefile`): `ACCEL_CONV` enables the 1×1 path;
  `DW3X3_VERIFY=1` adds instruction counters/checksums (not for timing).
- The repository's recorded cycle numbers come from Renode/Verilator
  simulation. Physical FPGA runs are [UNCONFIRMED] in repository evidence.

## 2. Existing 1×1 CFU

Origin: CFU-Playground `mnv2_first` accelerator, reused unchanged in
architecture (`README_MNV2_EXISTING_CFU.md`).

- **Software entry:** `src/tensorflow/lite/kernels/internal/reference/integer_ops/conv.cc`
  → `Mnv2ConvPerChannel1x1` in `.../mnv2_conv.cc`, guarded by `#ifdef ACCEL_CONV`.
- **Eligibility (conv.cc):** no padding, dilation 1, activation range
  [−128, 127], batch 1, stride 1, input H/W = output H/W, 1×1 filter, bias
  present, `input_depth < MAX_CONV_INPUT_VALUES`, input depth and output
  depth multiples of 8.
- **Configuration registers (funct7):** 10 input depth (words), 11 output
  depth, 12 input offset, 13 output offset, 14/15 activation min/max,
  20 output batch size (also restarts stores).
- **Parameter stores:** 21 output multiplier, 22 output shift, 23 bias
  (per-output-channel `DualPortMemory` + `CircularIncrementer`, depth 512);
  24 filter values (4 × 512-word memories, `FilterValueFetcher`);
  25 input values (`InputStore`, `MAX_PER_PIXEL_INPUT_WORDS` = 1024).
- **Datapath:** `Madd4Pipeline` (4 INT8 MACs per cycle, input offset added
  in hardware) → `Accumulator` → `PostProcessor` (bias, per-channel
  multiplier/shift requantization, output offset, activation clamp in
  hardware) → `ByteToWordShifter` → output FIFO (`SyncFIFOBuffered`, depth 512).
- **Control:** `Sequencer` (`gateware/sequencing.py`); 33 `MACC_RUN` starts
  computing all output channels for one input pixel; 34 `GET_OUTPUT` pops
  packed output words; 112 marks input read finished.
- **Software loop (mnv2_conv.cc):** load per-channel params and filter words
  for an output-channel batch, then per pixel: store input words, `MACC_RUN`,
  read outputs.

## 3. 3×3 depthwise CFU

Hardware: `gateware/macc.py :: Depthwise3x3Mac`; instruction wiring:
`gateware/mnv2_cfu.py :: _make_depthwise_3x3`; software:
`src/mnv2_cfu.h`, `src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_depthwise_conv.h`.

### Interface / opcodes (`cfu_op0(funct7, in0, in1)`)

| funct7 | Name | in0 | in1 | Returns | Completion |
|---|---|---|---|---|---|
| 40 | `DW3X3_LOAD` | 4 packed INT8 inputs | 4 packed INT8 weights | – | same cycle |
| 41 | `DW3X3_RUN` | – | – | – | waits for `dw.done` |
| 42 | `DW3X3_GET_RESULT` | – | – | INT32 accumulator | same cycle |
| 43 | `DW3X3_CONFIGURE` | input offset | weight offset | – | same cycle |
| 44 | `DW3X3_SHIFT_RIGHT` | new column: bytes [7:0]/[15:8]/[23:16] = rows 0/1/2 | – | – | same cycle |

### Input/weight handling

- A window is loaded with three LOADs (row-major, index = y·3 + x):
  LOAD 0 → elements 0–3, LOAD 1 → 4–7, LOAD 2 → element 8 (byte 0 only).
  An internal `load_index` (0→1→2→0) tracks which LOAD is next;
  CONFIGURE resets it to 0.
- Offsets are 9-bit signed registers set by CONFIGURE. Inputs and weights
  are sign-extended and offset-added to 10-bit signed values.
- LOAD stores offset-applied values in `input_window[9]` / `weight_window[9]`.

### MAC datapath and pipeline

- **During LOAD:** 4 parallel 10×10-bit signed multiplies; products
  registered into `product_regs[9]` (20-bit).
- **RUN pipeline (after `35e4493`):**
  - Stage 1: P0+P1, P2+P3, P4+P5, P6+P7, P8 pass-through (21-bit).
  - Stage 2: S0+S1, S2+S3, S4 pass-through (22-bit).
  - Stage 3: final sum → 32-bit `result`; `done` asserted (state 3).
- **After SHIFT_RIGHT:** products are flagged stale; the next RUN spends one
  extra cycle recomputing all nine products from the window registers
  (9 multiplies, state 4) before the same 3-stage accumulation.
- The CPU stalls on RUN until `done` (RunXetter: `done = dw.done`).

### Result handling

- GET_RESULT returns the raw INT32 sum Σ (x + input_offset)(w + weight_offset).
- **Bias, requantization (`MultiplyByQuantizedMultiplier`), output offset,
  activation clamp and the store are done in software**
  (`Mnv2Dw3x3StoreOutput`). Unlike the 1×1 path, there is no hardware
  post-processing in the depthwise path.

### Configuration / eligibility (`src/tensorflow/lite/micro/kernels/depthwise_conv.cc`)

INT8 input and filter, 3×3 filter, stride 1 or 2 in each dimension,
dilation 1, depth multiplier 1, and `weights_offset == 0`. Other cases
fall back to the TFLM reference kernels. CONFIGURE is issued once per
layer (17 per inference = 17 eligible depthwise layers).

## 4. Sliding-window reuse

Implemented in commit `b82da40`.

- **Applicable conditions:** `stride_width == 1`, and the output row's 3×3
  window is fully inside the input vertically; applies to the output
  columns `[slide_x_begin, slide_x_end)` whose window is fully inside
  horizontally.
- **Loop order change:** for sliding rows, iteration is channel → x
  (instead of x → channel) so one channel's weights stay in the CFU while
  the window moves right.
- **Overlap:** consecutive stride-1 windows share 6 of 9 inputs (two columns).
- **Retained state:** `weight_window` (unchanged), and input columns 1–2,
  which shift into columns 0–1.
- **Newly loaded data:** one 3-byte column (rows 0..2) packed into one word,
  raw INT8; the CFU adds `input_offset` on entry.
- **SHIFT operation:** register-only update; marks products stale; next RUN
  takes +1 cycle to recompute products.
- **Software/CFU interaction:** first window of each (row, channel) run →
  3× LOAD; subsequent windows → 1× SHIFT_RIGHT; then RUN + GET_RESULT +
  software post-processing for every window.
- **Not covered:** stride-2 layers (always 3 LOADs per window), and
  border windows that overlap padding (computed fully in software).

## 5. TFLM integration

| Operator | Integration point | Mechanism |
|---|---|---|
| `CONV_2D` (1×1) | `src/tensorflow/lite/kernels/internal/reference/integer_ops/conv.cc` → `mnv2_conv.cc` | Project override of the TFLM reference kernel, `#ifdef ACCEL_CONV` |
| `DEPTHWISE_CONV_2D` (3×3) | `src/tensorflow/lite/micro/kernels/depthwise_conv.cc` (`Eval`) → `mnv2_depthwise_conv.h` | Project override of the TFLM micro kernel |
| Application | `src/mnv2_app.cc` | Loads model and image, runs inference, prints Top-1 and `Output FNV1a` |

`src/software_cfu.cc` provides a software CFU model for the 1×1 instructions
(CFU-Playground convention). It does **not** model the depthwise opcodes
40–44 (no cases for them), so `SW_ONLY` builds cannot exercise the 3×3 path.

## 6. Accelerated operations

| Category | Executed by |
|---|---|
| Eligible 1×1 `CONV_2D` (expand/project layers) | 1×1 pointwise CFU, incl. hardware requantization |
| Eligible 3×3 `DEPTHWISE_CONV_2D`, fully-inside windows | 3×3 depthwise CFU MAC; post-processing in software |
| — of which stride-1, fully-inside rows | + sliding-window reuse (SHIFT_RIGHT) |
| Depthwise border windows touching padding | Software (scalar loop in `mnv2_depthwise_conv.h`) |
| First 3×3 `CONV_2D` (stride 2), any non-eligible conv | Software (TFLM reference) |
| `PAD`, `ADD`, `AVERAGE_POOL_2D`/mean, `FULLY_CONNECTED`/final conv, `SOFTMAX`, `RESHAPE`, quantize | Software (TFLM reference) [exact op list UNCONFIRMED — read from profiler log] |

## 7. Important source files

| Path | Role |
|---|---|
| `gateware/mnv2_cfu.py` | Top-level CFU; opcode map; instantiates both datapaths |
| `gateware/macc.py` | `Depthwise3x3Mac`, `Madd4Pipeline`, `Accumulator`, `ByteToWordShifter` |
| `gateware/sequencing.py` | 1×1 sequencer |
| `gateware/store.py` | Filter/input/param stores |
| `gateware/post_process.py` | 1×1 hardware requantization |
| `gateware/registerfile.py` | Funct7 dispatch, `Xetter` base |
| `gateware/config.py` | Memory depths (512-word EBRAM units) |
| `gateware/test_depthwise_macc.py`, `gateware/test_mnv2_cfu.py` | 3×3 / sliding-window gateware tests |
| `src/mnv2_cfu.h` | CFU instruction macros (both datapaths) |
| `src/.../integer_ops/conv.cc`, `mnv2_conv.cc` | 1×1 TFLM integration |
| `src/tensorflow/lite/micro/kernels/depthwise_conv.cc` | 3×3 dispatch + `DW3X3_VERIFY` instrumentation |
| `src/.../integer_ops/mnv2_depthwise_conv.h` | 3×3 + sliding-window kernel |
| `src/mnv2_app.cc` | Application / inference driver |
| `cfu_gen.py` | Generates `cfu.v` (generated file is git-ignored) |
| `Makefile` | Project build flags |
