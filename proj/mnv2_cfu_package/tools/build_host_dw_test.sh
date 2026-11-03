#!/bin/bash
# Builds and runs the host equivalence test for the 3x3 depthwise kernel.
# Independent of the FPGA: uses tools/mock/cfu.h instead of the hardware cfu.h.
set -euo pipefail
PKG="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="$(cd "$PKG/../.." && pwd)"
TFLM="$ROOT/third_party/tflite-micro"
OUT="${OUT:-${TMPDIR:-/tmp}/host_dw_test}"
g++ -std=c++17 -O2 -Wall \
  -DTF_LITE_STATIC_MEMORY -DTF_LITE_DISABLE_X86_NEON \
  -I"$PKG/tools/mock" -I"$PKG/src" -I"$TFLM" \
  -I"$TFLM/third_party/gemmlowp" -I"$TFLM/third_party/flatbuffers/include" \
  -I"$TFLM/third_party/ruy" -I"$TFLM/third_party/kissfft" \
  "$PKG/tools/host_dw_test.cc" -o "$OUT"
"$OUT"
