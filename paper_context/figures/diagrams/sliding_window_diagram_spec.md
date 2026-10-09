# Diagram Specification: 3×3 Depthwise CFU and Sliding-Window Reuse

Specification only. The actual figure is still to be drawn. Every element
below is taken from `proj/mnv2_cfu_package/gateware/macc.py`
(`Depthwise3x3Mac`) and `.../integer_ops/mnv2_depthwise_conv.h`.

Target: one IEEE column (3.5 in), two panels (a) and (b), left to right
or top to bottom.

## Panel (a): input reuse between consecutive windows

One channel of the input feature map, stride 1. Two consecutive output
positions x and x+1 on the same output row.

Use this lettering. It matches the hardware:

```
Window 1 (output x)        Window 2 (output x+1)
 A  B  C                    B  C  J
 D  E  F        ──SHIFT──▶  E  F  K
 G  H  I                    H  I  L
```

**Correction to the originally requested lettering.** The request listed
Window 2 as `B C D / E F G / H I J`. That treats the window as a flat
9-element sequence shifted by one. It does not match the hardware or the
image geometry: D and G are Window 1's *left* column, which is discarded,
and only one of the three new values (J) would be new. In
`Depthwise3x3Mac`, SHIFT_RIGHT shifts **each row** left by one
(`input_window[3r+0] ← [3r+1]`, `[3r+1] ← [3r+2]`) and writes the new
column into positions 2, 5, 8. The figure must show the row-wise shift
above.

Visual encoding (must survive grayscale print, so use fill + pattern):

- **Six reused values**: Window 1 columns 1–2 → Window 2 columns 0–1
  (B, C, E, F, H, I). Plain fill, label "retained (6)".
- **Three new values** (J, K, L in Window 2's right column, i.e. the image
  column to the right of Window 1): hatched fill, label "new column
  (3 bytes, 1 instruction)".
- **Dropped values** (A, D, G, Window 1's left column): outline only,
  faded.
- Arrow from Window 1 to Window 2 labelled `SHIFT_RIGHT (op 44)`.

Caption facts:

- First window of each (row, channel) run: 3 × `LOAD` (op 40), packing
  4 + 4 + 1 input bytes with 4 + 4 + 1 weight bytes.
- Each following window: 1 × `SHIFT_RIGHT` carrying one packed column
  (bytes [7:0], [15:8], [23:16] = rows 0, 1, 2).
- Weights are **retained** across the whole row run (the loop order is
  channel → x, so the same channel's weights stay in the CFU).
- Applies only to stride-1 layers and to windows fully inside the input.
  Border windows run in software; stride-2 layers always use 3 LOADs.

## Panel (b): CFU datapath

Blocks left to right:

1. **CONFIGURE (op 43)** → `input_offset`, `weight_offset` registers
   (9-bit signed). Also resets `load_index`.
2. **LOAD (op 40)**: 4 bytes in0 (inputs) + 4 bytes in1 (weights)
   → +offset → 4 parallel 10×10-bit signed multipliers → `product_regs[0..8]`
   (20-bit); also writes `input_window[9]` / `weight_window[9]`
   (offset-applied, 10-bit). `load_index` 0→1→2 selects elements 0–3,
   4–7, 8.
3. **SHIFT_RIGHT (op 44)**: each `input_window` row shifts left by one;
   the new column (+ input_offset) enters on the right. Weights untouched.
   Sets `products_stale`. Draw as a register-only path (no multiplier).
4. **Product refresh** (only when `products_stale`, +1 cycle at RUN):
   9 multipliers `input_window[n] × weight_window[n]` → `product_regs`.
5. **RUN (op 41)**: 3-stage adder pipeline.
   - Stage 1: P0+P1, P2+P3, P4+P5, P6+P7, P8 (21-bit)
   - Stage 2: S0+S1, S2+S3, S4 (22-bit)
   - Stage 3: final sum → 32-bit `result`, `done`
   The CPU stalls on RUN until `done`.
6. **GET_RESULT (op 42)** → INT32 accumulator to the CPU.
7. Box outside the CFU, on the CPU side: "bias + requantize + offset +
   clamp + store (software)".

Do **not** draw DSP blocks inside the 3×3 unit: the post-place report
shows `depthwise_3x3` uses 0 DSP (all multipliers in LUTs).

## Annotation numbers (from verified evidence only)

- LOAD 2,529,552 → 726,864 per inference (−71.27 %), SHIFT_RIGHT 600,896
  (source: `evidence/tables/sliding_window_instructions.md`, analytical).
- Do not put cycle or speedup numbers in this diagram.
