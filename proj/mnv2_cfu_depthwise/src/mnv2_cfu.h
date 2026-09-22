#ifndef PROJ_MNV2_CFU_DEPTHWISE_MNV2_CFU_H_
#define PROJ_MNV2_CFU_DEPTHWISE_MNV2_CFU_H_

#include <stdint.h>

#include "cfu.h"

#ifdef __cplusplus
extern "C" {
#endif

enum Mnv2FusedCommand {
  MNV2_FUSED_RESET = 0,
  MNV2_FUSED_CONFIG = 1,
  MNV2_FUSED_SET_SHIFTS = 2,
  MNV2_FUSED_PUSH_INPUT = 3,
  MNV2_FUSED_PUSH_EXP_WEIGHT = 4,
  MNV2_FUSED_PUSH_EXP_BIAS = 5,
  MNV2_FUSED_PUSH_DW_WEIGHT = 6,
  MNV2_FUSED_PUSH_DW_BIAS = 7,
  MNV2_FUSED_PUSH_PROJ_WEIGHT = 8,
  MNV2_FUSED_PUSH_PROJ_BIAS = 9,
  MNV2_FUSED_RUN = 10,
  MNV2_FUSED_POP_OUTPUT = 11,
  MNV2_FUSED_STATUS = 12,
};

enum {
  MNV2_FUSED_MAX_INPUT_CHANNELS = 8,
  MNV2_FUSED_MAX_EXPANDED_CHANNELS = 8,
  MNV2_FUSED_MAX_OUTPUT_CHANNELS = 8,
  MNV2_FUSED_KERNEL_TAPS = 9,
};

#define MNV2_FUSED_OP(command, value) cfu_op0((command), (uint32_t)(value), 0)
#define MNV2_FUSED_PACK_CONFIG(cin, cexp, cout) \
  ((uint32_t)(cin) | ((uint32_t)(cexp) << 8) | ((uint32_t)(cout) << 16))
#define MNV2_FUSED_PACK_SHIFTS(exp, dw, proj) \
  ((uint32_t)(exp) | ((uint32_t)(dw) << 8) | ((uint32_t)(proj) << 16))

#ifdef __cplusplus
}
#endif

#endif  // PROJ_MNV2_CFU_DEPTHWISE_MNV2_CFU_H_
