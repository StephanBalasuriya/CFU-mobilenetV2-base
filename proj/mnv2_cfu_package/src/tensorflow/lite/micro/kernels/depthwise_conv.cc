/* Copyright 2026 The CFU-Playground Authors. */

#include "tensorflow/lite/micro/kernels/depthwise_conv.h"

#include "tensorflow/lite/c/builtin_op_data.h"
#include "tensorflow/lite/c/common.h"
#include "tensorflow/lite/kernels/internal/reference/depthwiseconv_float.h"
#include "tensorflow/lite/kernels/internal/reference/integer_ops/depthwise_conv.h"

// Build with -DDW3X3_VERIFY to count 3x3 depthwise CFU instructions per layer
// and print an FNV-1a checksum of each layer's output. The counting wrappers
// are installed before the kernel header is included. Not for timing runs.
#ifdef DW3X3_VERIFY
#include <cstdio>

#include "mnv2_cfu.h"

namespace {
struct Dw3x3Counters {
  uint32_t configure, load, shift, run, get_result;
};
Dw3x3Counters dw3x3_counters;
}  // namespace

#undef CFU_DW3X3_LOAD
#undef CFU_DW3X3_RUN
#undef CFU_DW3X3_GET_RESULT
#undef CFU_DW3X3_CONFIGURE
#undef CFU_DW3X3_SHIFT_RIGHT
#define CFU_DW3X3_LOAD(in0, in1) \
  (++dw3x3_counters.load, cfu_dw3x3_load(in0, in1))
#define CFU_DW3X3_RUN() (++dw3x3_counters.run, cfu_dw3x3_run())
#define CFU_DW3X3_GET_RESULT() \
  (++dw3x3_counters.get_result, cfu_dw3x3_get_result())
#define CFU_DW3X3_CONFIGURE(input_offset, weight_offset) \
  (++dw3x3_counters.configure, cfu_dw3x3_configure(input_offset, weight_offset))
#define CFU_DW3X3_SHIFT_RIGHT(column) \
  (++dw3x3_counters.shift, cfu_dw3x3_shift_right(column))
#endif  // DW3X3_VERIFY

#include "tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_depthwise_conv.h"
#include "tensorflow/lite/kernels/kernel_util.h"
#include "tensorflow/lite/micro/kernels/kernel_util.h"
#include "tensorflow/lite/micro/micro_log.h"

namespace tflite {
namespace {

void* Init(TfLiteContext* context, const char* buffer, size_t length) {
  TFLITE_DCHECK(context->AllocatePersistentBuffer != nullptr);
  return context->AllocatePersistentBuffer(context, sizeof(OpDataConv));
}

#ifdef DW3X3_VERIFY
// Prints CFU instruction counts for one 3x3 depthwise layer, the counts
// expected for a 3-LOAD-per-window (old) and sliding-window (new) kernel,
// and an FNV-1a checksum of the layer output.
void Dw3x3VerifyReport(const DepthwiseParams& p, const RuntimeShape& in,
                       const RuntimeShape& out, const int8_t* out_data) {
  static int layer = 0;
  const int in_h = in.Dims(1), in_w = in.Dims(2), depth = in.Dims(3);
  const int out_h = out.Dims(1), out_w = out.Dims(2);
  auto full = [](int o, int s, int pad, int size) {
    const int origin = o * s - pad;
    return origin >= 0 && origin + 2 < size;
  };
  uint32_t full_rows = 0, full_cols = 0;
  for (int y = 0; y < out_h; ++y)
    full_rows += full(y, p.stride_height, p.padding_values.height, in_h);
  for (int x = 0; x < out_w; ++x)
    full_cols += full(x, p.stride_width, p.padding_values.width, in_w);
  const uint32_t windows = out.Dims(0) * full_rows * full_cols * depth;
  const uint32_t row_runs = out.Dims(0) * full_rows * depth;
  const bool slide = p.stride_width == 1 && full_cols > 0;
  const uint32_t exp_load = slide ? 3 * row_runs : 3 * windows;
  const uint32_t exp_shift = slide ? windows - row_runs : 0;

  uint32_t hash = 2166136261u;
  for (int i = 0; i < out.FlatSize(); ++i) {
    hash ^= static_cast<uint8_t>(out_data[i]);
    hash *= 16777619u;
  }
  const Dw3x3Counters& c = dw3x3_counters;
  printf("DW3X3 layer %d in=%dx%dx%d out=%dx%d stride=%d windows=%lu "
         "cfg=%lu load=%lu shift=%lu run=%lu get=%lu "
         "old_load=%lu exp_load=%lu exp_shift=%lu fnv=0x%08lx\n",
         layer++, in_h, in_w, depth, out_h, out_w, p.stride_width,
         (unsigned long)windows, (unsigned long)c.configure,
         (unsigned long)c.load, (unsigned long)c.shift, (unsigned long)c.run,
         (unsigned long)c.get_result, (unsigned long)(3 * windows),
         (unsigned long)exp_load, (unsigned long)exp_shift,
         (unsigned long)hash);
  dw3x3_counters = Dw3x3Counters{};
}
#endif  // DW3X3_VERIFY

TfLiteStatus Eval(TfLiteContext* context, TfLiteNode* node) {
  auto& params =
      *(reinterpret_cast<TfLiteDepthwiseConvParams*>(node->builtin_data));
  const OpDataConv& data = *(static_cast<const OpDataConv*>(node->user_data));
  TfLiteEvalTensor* output =
      tflite::micro::GetEvalOutput(context, node, kDepthwiseConvOutputTensor);
  const TfLiteEvalTensor* input =
      tflite::micro::GetEvalInput(context, node, kDepthwiseConvInputTensor);
  const TfLiteEvalTensor* filter =
      tflite::micro::GetEvalInput(context, node, kDepthwiseConvWeightsTensor);
  const TfLiteEvalTensor* bias =
      NumInputs(node) == 3
          ? tflite::micro::GetEvalInput(context, node,
                                        kDepthwiseConvBiasTensor)
          : nullptr;

  if (input->type == kTfLiteInt8 && filter->type == kTfLiteInt8) {
    const RuntimeShape filter_shape = tflite::micro::GetTensorShape(filter);
    const DepthwiseParams quantized_params =
        DepthwiseConvParamsQuantized(params, data);
    if (filter_shape.Dims(1) == 3 && filter_shape.Dims(2) == 3 &&
        params.stride_width >= 1 && params.stride_width <= 2 &&
        params.stride_height >= 1 && params.stride_height <= 2 &&
        params.dilation_width_factor == 1 &&
        params.dilation_height_factor == 1 && params.depth_multiplier == 1 &&
        quantized_params.weights_offset == 0) {
      reference_integer_ops::Mnv2DepthwiseConvPerChannel3x3(
          quantized_params, data.per_channel_output_multiplier,
          data.per_channel_output_shift,
          tflite::micro::GetTensorShape(input),
          tflite::micro::GetTensorData<int8_t>(input), filter_shape,
          tflite::micro::GetTensorData<int8_t>(filter),
          tflite::micro::GetTensorShape(bias),
          tflite::micro::GetOptionalTensorData<int32_t>(bias),
          tflite::micro::GetTensorShape(output),
          tflite::micro::GetTensorData<int8_t>(output));
#ifdef DW3X3_VERIFY
      Dw3x3VerifyReport(quantized_params, tflite::micro::GetTensorShape(input),
                        tflite::micro::GetTensorShape(output),
                        tflite::micro::GetTensorData<int8_t>(output));
#endif
      return kTfLiteOk;
    }
  }

  switch (input->type) {
    case kTfLiteFloat32:
      tflite::reference_ops::DepthwiseConv(
          DepthwiseConvParamsFloat(params, data),
          tflite::micro::GetTensorShape(input),
          tflite::micro::GetTensorData<float>(input),
          tflite::micro::GetTensorShape(filter),
          tflite::micro::GetTensorData<float>(filter),
          tflite::micro::GetTensorShape(bias),
          tflite::micro::GetOptionalTensorData<float>(bias),
          tflite::micro::GetTensorShape(output),
          tflite::micro::GetTensorData<float>(output));
      break;
    case kTfLiteInt8:
      if (filter->type == kTfLiteInt4) {
        int8_t* unpacked_filter_data = static_cast<int8_t*>(
            context->GetScratchBuffer(context, data.filter_buffer_index));
        reference_integer_ops::DepthwiseConvPerChannelWithPackedInt4Weights(
            DepthwiseConvParamsQuantized(params, data),
            data.per_channel_output_multiplier, data.per_channel_output_shift,
            tflite::micro::GetTensorShape(input),
            tflite::micro::GetTensorData<int8_t>(input),
            tflite::micro::GetTensorShape(filter),
            tflite::micro::GetTensorData<int8_t>(filter),
            unpacked_filter_data, tflite::micro::GetTensorShape(bias),
            tflite::micro::GetOptionalTensorData<int32_t>(bias),
            tflite::micro::GetTensorShape(output),
            tflite::micro::GetTensorData<int8_t>(output));
        break;
      } else if (filter->type == kTfLiteInt8) {
        reference_integer_ops::DepthwiseConvPerChannel(
            DepthwiseConvParamsQuantized(params, data),
            data.per_channel_output_multiplier, data.per_channel_output_shift,
            tflite::micro::GetTensorShape(input),
            tflite::micro::GetTensorData<int8_t>(input),
            tflite::micro::GetTensorShape(filter),
            tflite::micro::GetTensorData<int8_t>(filter),
            tflite::micro::GetTensorShape(bias),
            tflite::micro::GetOptionalTensorData<int32_t>(bias),
            tflite::micro::GetTensorShape(output),
            tflite::micro::GetTensorData<int8_t>(output));
        break;
      }
      MicroPrintf("Filter type %s (%d) not supported.",
                  TfLiteTypeGetName(filter->type), filter->type);
      return kTfLiteError;
    default:
      MicroPrintf("Input type %s (%d) not supported.",
                  TfLiteTypeGetName(input->type), input->type);
      return kTfLiteError;
  }
  return kTfLiteOk;
}

}  // namespace

TfLiteRegistration Register_DEPTHWISE_CONV_2D() {
  return tflite::micro::RegisterOp(Init, DepthwiseConvPrepare, Eval);
}

}  // namespace tflite
