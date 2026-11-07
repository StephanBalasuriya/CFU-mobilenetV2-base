#!/usr/bin/env bash
set -euo pipefail

# This script vendors the exact MobileNetV2 CFU implementation from the
# google/CFU-Playground checkout that already contains this project.
#
# Run from:
#   CFU-Playground/proj/mnv2_cfu
#
# Expected:
#   ../mnv2_first exists in the same CFU-Playground checkout.

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UPSTREAM="${HERE}/../mnv2_first"

if [[ ! -d "${UPSTREAM}" ]]; then
  echo "ERROR: ${UPSTREAM} does not exist."
  echo "This package is designed to be installed beside the upstream"
  echo "proj/mnv2_first project from google/CFU-Playground."
  exit 1
fi

echo "Vending MobileNetV2 CFU from:"
echo "  ${UPSTREAM}"

# Gateware is kept as an exact copy of the upstream mnv2_first CFU.
rm -rf "${HERE}/cfu/gateware"
mkdir -p "${HERE}/cfu"
cp -a "${UPSTREAM}/gateware" "${HERE}/cfu/"

# Copy the generator used by CFU-Playground to create cfu.v.
cp "${UPSTREAM}/cfu_gen.py" "${HERE}/cfu_gen.py"

# Software-side CFU interface and emulation.
cp "${UPSTREAM}/src/mnv2_cfu.h" "${HERE}/src/mnv2_cfu.h"
cp "${UPSTREAM}/src/software_cfu.cc" "${HERE}/src/software_cfu.cc"

# The upstream accelerator replaces the integer reference convolution with
# a MobileNetV2-specific 1x1 implementation when ACCEL_CONV is enabled.
TARGET="${HERE}/src/tensorflow/lite/kernels/internal/reference/integer_ops"
mkdir -p "${TARGET}"
cp "${UPSTREAM}/src/tensorflow/lite/kernels/internal/reference/integer_ops/conv.cc" \
   "${TARGET}/conv.cc"
cp "${UPSTREAM}/src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_conv.cc" \
   "${TARGET}/mnv2_conv.cc"
cp "${UPSTREAM}/src/tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_conv.h" \
   "${TARGET}/mnv2_conv.h"

echo
echo "CFU sources copied successfully."
echo
echo "Files:"
find "${HERE}/cfu" -maxdepth 2 -type f | sort
echo
echo "Next:"
echo "  cd ${HERE}/../.."
echo "  make -C proj/mnv2_cfu clean"
echo "  make -C proj/mnv2_cfu -j\$(nproc)"
echo "  make -C proj/mnv2_cfu renode"
