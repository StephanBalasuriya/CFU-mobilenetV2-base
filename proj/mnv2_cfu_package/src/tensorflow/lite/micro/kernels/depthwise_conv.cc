/* Copyright 2026 The CFU-Playground Authors. */

#include "tensorflow/lite/micro/kernels/depthwise_conv.h"

#include "tensorflow/lite/c/builtin_op_data.h"
#include "tensorflow/lite/c/common.h"
#include "tensorflow/lite/kernels/internal/reference/depthwiseconv_float.h"
#include "tensorflow/lite/kernels/internal/reference/integer_ops/depthwise_conv.h"
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
