/*
 * Copyright 2026 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 */
#ifndef TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_INTEGER_OPS_MNV2_DEPTHWISE_CONV_H_
#define TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_INTEGER_OPS_MNV2_DEPTHWISE_CONV_H_

#include <algorithm>
#include <cstdint>

#include "mnv2_cfu.h"
#include "tensorflow/lite/kernels/internal/common.h"

#ifdef DW3X3_PROFILE
#include "perf.h"
#include <stdio.h>
#endif

namespace tflite {
namespace reference_integer_ops {

#ifdef DW3X3_PROFILE
struct Mnv2Dw3x3ProfileCounters {
  uint64_t operand_fetch_load_shift = 0;
  uint64_t run_get_result = 0;
  uint64_t output_store_postprocess = 0;
  uint64_t software_border = 0;
  uint64_t total_start = 0;
};

static Mnv2Dw3x3ProfileCounters mnv2_dw3x3_profile;

inline uint64_t Mnv2Dw3x3ProfileStart() {
  return perf_get_mcycle64();
}

inline void Mnv2Dw3x3ProfileAdd(uint64_t* bucket, uint64_t start) {
  *bucket += Mnv2Dw3x3ProfileStart() - start;
}

inline void Mnv2Dw3x3ProfileReset() {
  mnv2_dw3x3_profile = Mnv2Dw3x3ProfileCounters{};
  mnv2_dw3x3_profile.total_start = Mnv2Dw3x3ProfileStart();
}

inline void Mnv2Dw3x3ProfileReport() {
  const uint64_t total =
      Mnv2Dw3x3ProfileStart() - mnv2_dw3x3_profile.total_start;
  printf(
      "DW3X3 profile: operand_fetch_load_shift=%llu "
      "run_get_result=%llu output_store_postprocess=%llu "
      "software_border=%llu total=%llu\n",
      static_cast<unsigned long long>(
          mnv2_dw3x3_profile.operand_fetch_load_shift),
      static_cast<unsigned long long>(mnv2_dw3x3_profile.run_get_result),
      static_cast<unsigned long long>(
          mnv2_dw3x3_profile.output_store_postprocess),
      static_cast<unsigned long long>(mnv2_dw3x3_profile.software_border),
      static_cast<unsigned long long>(total));
}
#endif

inline void Mnv2DepthwiseConvPerChannel3x3(
    const DepthwiseParams& params, const int32_t* output_multiplier,
    const int32_t* output_shift, const RuntimeShape& input_shape,
    const int8_t* input_data, const RuntimeShape& filter_shape,
    const int8_t* filter_data, const RuntimeShape& bias_shape,
    const int32_t* bias_data, const RuntimeShape& output_shape,
    int8_t* output_data) {
  const int batches = MatchingDim(input_shape, 0, output_shape, 0);
  const int input_height = input_shape.Dims(1);
  const int input_width = input_shape.Dims(2);
  const int input_depth = input_shape.Dims(3);
  const int output_height = output_shape.Dims(1);
  const int output_width = output_shape.Dims(2);
  const int input_offset = params.input_offset;
  const int output_offset = params.output_offset;

#ifdef DW3X3_PROFILE
  Mnv2Dw3x3ProfileReset();
#endif
  CFU_DW3X3_CONFIGURE(input_offset, params.weights_offset);

  for (int batch = 0; batch < batches; ++batch) {
    for (int out_y = 0; out_y < output_height; ++out_y) {
      const int in_y_origin =
          out_y * params.stride_height - params.padding_values.height;
      for (int out_x = 0; out_x < output_width; ++out_x) {
        const int in_x_origin =
            out_x * params.stride_width - params.padding_values.width;
        const bool full_window =
            in_x_origin >= 0 && in_y_origin >= 0 &&
            in_x_origin + 2 < input_width && in_y_origin + 2 < input_height;

        for (int channel = 0; channel < input_depth; ++channel) {
          int32_t acc = 0;
          if (full_window) {
#ifdef DW3X3_PROFILE
            const uint64_t fetch_start = Mnv2Dw3x3ProfileStart();
#endif
            for (int word = 0; word < 3; ++word) {
              uint32_t input_word = 0;
              uint32_t filter_word = 0;
              for (int byte = 0; byte < 4; ++byte) {
                const int index = word * 4 + byte;
                if (index >= 9) {
                  break;
                }
                const int filter_y = index / 3;
                const int filter_x = index % 3;
                input_word |= static_cast<uint32_t>(static_cast<uint8_t>(
                    input_data[Offset(input_shape, batch,
                                      in_y_origin + filter_y,
                                      in_x_origin + filter_x, channel)]))
                              << (byte * 8);
                filter_word |= static_cast<uint32_t>(static_cast<uint8_t>(
                    filter_data[Offset(filter_shape, 0, filter_y, filter_x,
                                       channel)]))
                               << (byte * 8);
              }
              CFU_DW3X3_LOAD(input_word, filter_word);
            }
#ifdef DW3X3_PROFILE
            Mnv2Dw3x3ProfileAdd(
                &mnv2_dw3x3_profile.operand_fetch_load_shift, fetch_start);
            const uint64_t run_start = Mnv2Dw3x3ProfileStart();
#endif
            CFU_DW3X3_RUN();
            acc = static_cast<int32_t>(CFU_DW3X3_GET_RESULT());
#ifdef DW3X3_PROFILE
            Mnv2Dw3x3ProfileAdd(&mnv2_dw3x3_profile.run_get_result, run_start);
#endif
          } else {
#ifdef DW3X3_PROFILE
            const uint64_t border_start = Mnv2Dw3x3ProfileStart();
#endif
            for (int filter_y = 0; filter_y < 3; ++filter_y) {
              for (int filter_x = 0; filter_x < 3; ++filter_x) {
                const int in_x = in_x_origin + filter_x;
                const int in_y = in_y_origin + filter_y;
                if (in_x >= 0 && in_x < input_width && in_y >= 0 &&
                    in_y < input_height) {
                  const int32_t input_val =
                      input_data[Offset(input_shape, batch, in_y, in_x,
                                        channel)];
                  const int32_t filter_val =
                      filter_data[Offset(filter_shape, 0, filter_y, filter_x,
                                         channel)];
                  acc += filter_val * (input_val + input_offset);
                }
              }
            }
#ifdef DW3X3_PROFILE
            Mnv2Dw3x3ProfileAdd(&mnv2_dw3x3_profile.software_border,
                                border_start);
#endif
          }

#ifdef DW3X3_PROFILE
          const uint64_t store_start = Mnv2Dw3x3ProfileStart();
#endif
          if (bias_data) {
            acc += bias_data[channel];
          }
          acc = MultiplyByQuantizedMultiplier(
              acc, output_multiplier[channel], output_shift[channel]);
          acc += output_offset;
          acc = std::max(acc, params.quantized_activation_min);
          acc = std::min(acc, params.quantized_activation_max);
          output_data[Offset(output_shape, batch, out_y, out_x, channel)] =
              static_cast<int8_t>(acc);
#ifdef DW3X3_PROFILE
          Mnv2Dw3x3ProfileAdd(
              &mnv2_dw3x3_profile.output_store_postprocess, store_start);
#endif
        }
      }
    }
  }
}

}  // namespace reference_integer_ops
}  // namespace tflite

#endif  // TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_INTEGER_OPS_MNV2_DEPTHWISE_CONV_H_
