/*
 * Copyright 2021 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 */
#ifndef _CPP_MATH_H
#define _CPP_MATH_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

int32_t cpp_math_mul_by_quantized_mul_software(int32_t x, int32_t quantized_multiplier,
                                               int shift);
int32_t cpp_math_mul_by_quantized_mul_gateware1(int32_t x, int32_t quantized_multiplier,
                                                int shift);
int32_t cpp_math_mul_by_quantized_mul_gateware2(int32_t x, int32_t quantized_multiplier,
                                                int shift);
int32_t cpp_math_srdhm_software(int32_t a, int32_t b);
int32_t cpp_math_rdbpot_software(int32_t value, int shift);

#ifdef __cplusplus
}
#endif
#endif  // _CPP_MATH_H
