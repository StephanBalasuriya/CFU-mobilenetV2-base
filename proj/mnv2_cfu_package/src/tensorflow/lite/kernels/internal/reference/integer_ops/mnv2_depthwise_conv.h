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

namespace tflite {
namespace reference_integer_ops {

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
            CFU_DW3X3_RUN();
            acc = static_cast<int32_t>(CFU_DW3X3_GET_RESULT());
          } else {
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
          }

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
        }
      }
    }
  }
}

}  // namespace reference_integer_ops
}  // namespace tflite

#endif  // TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_INTEGER_OPS_MNV2_DEPTHWISE_CONV_H_
