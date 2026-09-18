/*
 * Copyright 2021 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 */

#include "cpp_math.h"

#include "cfu.h"
#include "tensorflow/lite/kernels/internal/common.h"

int32_t cpp_math_mul_by_quantized_mul_software(int32_t x,
                                               int32_t quantized_multiplier,
                                               int shift) {
  return tflite::MultiplyByQuantizedMultiplier(x, quantized_multiplier, shift);
}

int32_t cpp_math_mul_by_quantized_mul_gateware1(int32_t x,
                                                int32_t quantized_multiplier,
                                                int shift) {
  using gemmlowp::RoundingDivideByPOT;
  int left_shift = shift > 0 ? shift : 0;
  int right_shift = shift > 0 ? 0 : -shift;
  int64_t left_shifted = x * (1 << left_shift);
  int32_t srdhm = cfu_op7_hw(0, left_shifted, quantized_multiplier);
  return RoundingDivideByPOT(srdhm, right_shift);
}

int32_t cpp_math_mul_by_quantized_mul_gateware2(int32_t x,
                                                int32_t quantized_multiplier,
                                                int shift) {
  int left_shift = shift > 0 ? shift : 0;
  int right_shift = shift > 0 ? 0 : -shift;
  int32_t left_shifted = x << left_shift;
  int32_t srdhm = cfu_op7_hw(0, left_shifted, quantized_multiplier);
  return cfu_op6_hw(0, srdhm, right_shift);
}

int32_t cpp_math_srdhm_software(int32_t a, int32_t b) {
  return gemmlowp::SaturatingRoundingDoublingHighMul(a, b);
}

int32_t cpp_math_rdbpot_software(int32_t value, int shift) {
  return gemmlowp::RoundingDivideByPOT(value, shift);
}
