#include "fused_depthwise.h"

#include <stddef.h>

#include "mnv2_cfu.h"

namespace {

bool Valid(const Mnv2FusedParams& p, const int8_t* input, int8_t* output) {
  return input != nullptr && output != nullptr &&
         p.expansion_weights != nullptr && p.expansion_bias != nullptr &&
         p.depthwise_weights != nullptr && p.depthwise_bias != nullptr &&
         p.projection_weights != nullptr && p.projection_bias != nullptr &&
         p.input_channels > 0 &&
         p.input_channels <= MNV2_FUSED_MAX_INPUT_CHANNELS &&
         p.expanded_channels > 0 &&
         p.expanded_channels <= MNV2_FUSED_MAX_EXPANDED_CHANNELS &&
         p.output_channels > 0 &&
         p.output_channels <= MNV2_FUSED_MAX_OUTPUT_CHANNELS &&
         p.expansion_shift >= 0 && p.expansion_shift <= 31 &&
         p.depthwise_shift >= 0 && p.depthwise_shift <= 31 &&
         p.projection_shift >= 0 && p.projection_shift <= 31;
}

int8_t ShiftAndClamp(int32_t value, int shift) {
  const int32_t shifted = value >> shift;
  if (shifted > 127) return 127;
  if (shifted < -128) return -128;
  return static_cast<int8_t>(shifted);
}

}  // namespace

bool Mnv2FusedReference(const Mnv2FusedParams& p,
                        const int8_t* input_patch,
                        int8_t* output) {
  if (!Valid(p, input_patch, output)) return false;

  int8_t expanded[MNV2_FUSED_KERNEL_TAPS]
                 [MNV2_FUSED_MAX_EXPANDED_CHANNELS] = {};
  int8_t depthwise[MNV2_FUSED_MAX_EXPANDED_CHANNELS] = {};

  for (int tap = 0; tap < MNV2_FUSED_KERNEL_TAPS; ++tap) {
    for (int e = 0; e < p.expanded_channels; ++e) {
      int32_t acc = p.expansion_bias[e];
      for (int i = 0; i < p.input_channels; ++i) {
        acc += static_cast<int32_t>(input_patch[tap * p.input_channels + i]) *
               p.expansion_weights[e * p.input_channels + i];
      }
      expanded[tap][e] = ShiftAndClamp(acc, p.expansion_shift);
    }
  }

  for (int e = 0; e < p.expanded_channels; ++e) {
    int32_t acc = p.depthwise_bias[e];
    for (int tap = 0; tap < MNV2_FUSED_KERNEL_TAPS; ++tap) {
      acc += static_cast<int32_t>(expanded[tap][e]) *
             p.depthwise_weights[tap * p.expanded_channels + e];
    }
    depthwise[e] = ShiftAndClamp(acc, p.depthwise_shift);
  }

  for (int o = 0; o < p.output_channels; ++o) {
    int32_t acc = p.projection_bias[o];
    for (int e = 0; e < p.expanded_channels; ++e) {
      acc += static_cast<int32_t>(depthwise[e]) *
             p.projection_weights[o * p.expanded_channels + e];
    }
    output[o] = ShiftAndClamp(acc, p.projection_shift);
  }
  return true;
}

bool Mnv2FusedRunImage(const Mnv2FusedParams& p,
                       const int8_t* input,
                       int input_height,
                       int input_width,
                       int stride,
                       int padding,
                       int input_zero_point,
                       int8_t* output,
                       int output_capacity,
                       int* output_height,
                       int* output_width) {
  if (!input || !output || !output_height || !output_width ||
      input_height <= 0 || input_width <= 0 ||
      (stride != 1 && stride != 2) || (padding != 0 && padding != 1) ||
      input_zero_point < -128 || input_zero_point > 127 ||
      !Valid(p, input, output)) {
    return false;
  }
  const int oh = (input_height + 2 * padding - 3) / stride + 1;
  const int ow = (input_width + 2 * padding - 3) / stride + 1;
  if (oh <= 0 || ow <= 0 || output_capacity < oh * ow * p.output_channels) {
    return false;
  }
  *output_height = oh;
  *output_width = ow;
  int8_t patch[MNV2_FUSED_KERNEL_TAPS * MNV2_FUSED_MAX_INPUT_CHANNELS];
  for (int oy = 0; oy < oh; ++oy) {
    for (int ox = 0; ox < ow; ++ox) {
      for (int ky = 0; ky < 3; ++ky) {
        const int iy = oy * stride + ky - padding;
        for (int kx = 0; kx < 3; ++kx) {
          const int ix = ox * stride + kx - padding;
          const int tap = ky * 3 + kx;
          for (int c = 0; c < p.input_channels; ++c) {
            patch[tap * p.input_channels + c] =
                (iy >= 0 && iy < input_height && ix >= 0 && ix < input_width)
                    ? input[(iy * input_width + ix) * p.input_channels + c]
                    : static_cast<int8_t>(input_zero_point);
          }
        }
      }
      if (!Mnv2FusedCfu(p, patch,
                        output + (oy * ow + ox) * p.output_channels)) {
        return false;
      }
    }
  }
  return true;
}

bool Mnv2FusedCfu(const Mnv2FusedParams& p,
                  const int8_t* input_patch,
                  int8_t* output) {
  if (!Valid(p, input_patch, output)) return false;

  MNV2_FUSED_OP(MNV2_FUSED_RESET, 0);
  MNV2_FUSED_OP(MNV2_FUSED_CONFIG,
                MNV2_FUSED_PACK_CONFIG(p.input_channels,
                                       p.expanded_channels,
                                       p.output_channels));
  MNV2_FUSED_OP(MNV2_FUSED_SET_SHIFTS,
                MNV2_FUSED_PACK_SHIFTS(p.expansion_shift,
                                       p.depthwise_shift,
                                       p.projection_shift));

  for (int n = 0; n < MNV2_FUSED_KERNEL_TAPS * p.input_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_INPUT, input_patch[n]);
  for (int n = 0; n < p.expanded_channels * p.input_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_EXP_WEIGHT, p.expansion_weights[n]);
  for (int n = 0; n < p.expanded_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_EXP_BIAS, p.expansion_bias[n]);
  for (int n = 0; n < MNV2_FUSED_KERNEL_TAPS * p.expanded_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_DW_WEIGHT, p.depthwise_weights[n]);
  for (int n = 0; n < p.expanded_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_DW_BIAS, p.depthwise_bias[n]);
  for (int n = 0; n < p.output_channels * p.expanded_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_PROJ_WEIGHT, p.projection_weights[n]);
  for (int n = 0; n < p.output_channels; ++n)
    MNV2_FUSED_OP(MNV2_FUSED_PUSH_PROJ_BIAS, p.projection_bias[n]);

  MNV2_FUSED_OP(MNV2_FUSED_RUN, 0);
  const uint32_t status = MNV2_FUSED_OP(MNV2_FUSED_STATUS, 0);
  if ((status & (1u << 3)) != 0 || (status & (1u << 2)) == 0) return false;

  for (int o = 0; o < p.output_channels; ++o) {
    output[o] = static_cast<int8_t>(MNV2_FUSED_OP(MNV2_FUSED_POP_OUTPUT, 0));
  }
  return true;
}
