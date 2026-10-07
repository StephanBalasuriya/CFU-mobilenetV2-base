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

// Loads the full 3x3 input/weight window at (in_y_origin, in_x_origin) for
// one channel into the CFU as three packed words (row-major, 4+4+1 bytes).
inline void Mnv2Dw3x3LoadWindow(const RuntimeShape& input_shape,
                                const int8_t* input_data,
                                const RuntimeShape& filter_shape,
                                const int8_t* filter_data, int batch,
                                int in_y_origin, int in_x_origin,
                                int channel) {
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
                         filter_data[Offset(filter_shape, 0, filter_y,
                                            filter_x, channel)]))
                     << (byte * 8);
    }
    CFU_DW3X3_LOAD(input_word, filter_word);
  }
}

// Bias, requantization, output offset, activation clamp and store.
inline void Mnv2Dw3x3StoreOutput(const DepthwiseParams& params,
                                 const int32_t* output_multiplier,
                                 const int32_t* output_shift,
                                 const int32_t* bias_data,
                                 const RuntimeShape& output_shape,
                                 int8_t* output_data, int batch, int out_y,
                                 int out_x, int channel, int32_t acc) {
  if (bias_data) {
    acc += bias_data[channel];
  }
  acc = MultiplyByQuantizedMultiplier(acc, output_multiplier[channel],
                                      output_shift[channel]);
  acc += params.output_offset;
  acc = std::max(acc, params.quantized_activation_min);
  acc = std::min(acc, params.quantized_activation_max);
  output_data[Offset(output_shape, batch, out_y, out_x, channel)] =
      static_cast<int8_t>(acc);
}

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

  CFU_DW3X3_CONFIGURE(input_offset, params.weights_offset);

  // Stride-1 sliding window: [slide_x_begin, slide_x_end) is the range of
  // out_x whose 3x3 window lies fully inside the input horizontally (same
  // test as full_window below). In fully-inside rows these outputs are
  // computed channel -> x so the CFU can keep one channel's weights and
  // shift the input window right by one column per output.
  const bool slide_enabled = params.stride_width == 1;
  int slide_x_begin = 0;
  int slide_x_end = 0;
  if (slide_enabled) {
    slide_x_begin = std::max<int>(0, params.padding_values.width);
    slide_x_end = std::min<int>(output_width,
                                input_width - 2 + params.padding_values.width);
  }

  for (int batch = 0; batch < batches; ++batch) {
    for (int out_y = 0; out_y < output_height; ++out_y) {
      const int in_y_origin =
          out_y * params.stride_height - params.padding_values.height;
      const bool slide_row = slide_enabled && in_y_origin >= 0 &&
                             in_y_origin + 2 < input_height &&
                             slide_x_begin < slide_x_end;

      if (slide_row) {
        for (int channel = 0; channel < input_depth; ++channel) {
          for (int out_x = slide_x_begin; out_x < slide_x_end; ++out_x) {
            const int in_x_origin = out_x - params.padding_values.width;
            if (out_x == slide_x_begin) {
              // First window of the row for this channel: inputs + weights.
              Mnv2Dw3x3LoadWindow(input_shape, input_data, filter_shape,
                                  filter_data, batch, in_y_origin,
                                  in_x_origin, channel);
            } else {
              // Same channel, next x: only the new right column. Raw int8
              // bytes, row 0..2 in bytes 0..2; the CFU adds input_offset.
              const int new_x = in_x_origin + 2;
              uint32_t column = 0;
              for (int row = 0; row < 3; ++row) {
                column |= static_cast<uint32_t>(static_cast<uint8_t>(
                              input_data[Offset(input_shape, batch,
                                                in_y_origin + row, new_x,
                                                channel)]))
                          << (row * 8);
              }
              CFU_DW3X3_SHIFT_RIGHT(column);
            }
            CFU_DW3X3_RUN();
            const int32_t acc = static_cast<int32_t>(CFU_DW3X3_GET_RESULT());
            Mnv2Dw3x3StoreOutput(params, output_multiplier, output_shift,
                                 bias_data, output_shape, output_data, batch,
                                 out_y, out_x, channel, acc);
          }
        }
      }

      for (int out_x = 0; out_x < output_width; ++out_x) {
        if (slide_row && out_x >= slide_x_begin && out_x < slide_x_end) {
          continue;  // Already computed by the sliding window above.
        }
        const int in_x_origin =
            out_x * params.stride_width - params.padding_values.width;
        const bool full_window =
            in_x_origin >= 0 && in_y_origin >= 0 &&
            in_x_origin + 2 < input_width && in_y_origin + 2 < input_height;

        for (int channel = 0; channel < input_depth; ++channel) {
          int32_t acc = 0;
          if (full_window) {
            Mnv2Dw3x3LoadWindow(input_shape, input_data, filter_shape,
                                filter_data, batch, in_y_origin, in_x_origin,
                                channel);
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

          Mnv2Dw3x3StoreOutput(params, output_multiplier, output_shift,
                               bias_data, output_shape, output_data, batch,
                               out_y, out_x, channel, acc);
        }
      }
    }
  }
}

}  // namespace reference_integer_ops
}  // namespace tflite

#endif  // TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_INTEGER_OPS_MNV2_DEPTHWISE_CONV_H_
