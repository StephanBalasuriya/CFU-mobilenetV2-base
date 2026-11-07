/*
 * Host functional-equivalence test: optimized 3x3 depthwise kernel
 * (src/.../mnv2_depthwise_conv.h, using the software CFU model in
 * tools/mock/cfu.h) versus the TFLM reference kernel
 * reference_integer_ops::DepthwiseConvPerChannel.
 *
 * Build and run: tools/build_host_dw_test.sh
 * Output: per-mismatch detail and a final "cases=N mismatches=M" line.
 */
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <random>
#include <string>
#include <vector>

#include "mnv2_cfu.h"  // pulls in tools/mock/cfu.h (-I order)
#include "tensorflow/lite/kernels/internal/reference/integer_ops/depthwise_conv.h"
#include "tensorflow/lite/kernels/internal/reference/integer_ops/mnv2_depthwise_conv.h"
#include "tensorflow/lite/kernels/internal/types.h"

using tflite::DepthwiseParams;
using tflite::RuntimeShape;

namespace {

struct Case {
  int h, w, depth, stride;
  bool same;
  int input_offset, output_offset, act_min, act_max;
  const char* kind;
};

struct Totals {
  uint64_t cases = 0, mismatching_cases = 0, mismatching_elems = 0;
  uint64_t elems = 0, cfu_windows = 0, load = 0, shift = 0;
  uint64_t protocol_errors = 0;
  uint64_t cases_with_shift = 0, cases_load_only = 0, cases_with_border = 0;
};

int OutDim(int in, int stride, bool same) {
  return same ? (in + stride - 1) / stride : (in - 3) / stride + 1;
}

int PadBefore(int in, int out, int stride, bool same) {
  if (!same) return 0;
  const int total = std::max((out - 1) * stride + 3 - in, 0);
  return total / 2;
}

bool RunCase(int idx, const Case& c, std::mt19937& rng, Totals& t) {
  std::uniform_int_distribution<int> i8(-128, 127);
  const int out_h = OutDim(c.h, c.stride, c.same);
  const int out_w = OutDim(c.w, c.stride, c.same);

  const int32_t in_dims[] = {1, c.h, c.w, c.depth};
  const int32_t f_dims[] = {1, 3, 3, c.depth};
  const int32_t b_dims[] = {c.depth};
  const int32_t out_dims[] = {1, out_h, out_w, c.depth};
  RuntimeShape in_shape(4, in_dims);
  RuntimeShape f_shape(4, f_dims);
  RuntimeShape b_shape(1, b_dims);
  RuntimeShape out_shape(4, out_dims);

  std::vector<int8_t> input(in_shape.FlatSize()), filter(f_shape.FlatSize());
  std::vector<int32_t> bias(c.depth), mult(c.depth), shift(c.depth);
  std::vector<int8_t> ref(out_shape.FlatSize()), opt(out_shape.FlatSize());

  const bool extreme = std::string(c.kind) == "extreme";
  for (auto& v : input) v = extreme ? (rng() & 1 ? -128 : 127) : i8(rng);
  for (auto& v : filter) v = extreme ? (rng() & 1 ? -128 : 127) : i8(rng);
  std::uniform_int_distribution<int32_t> bias_d(-(1 << 20), 1 << 20);
  std::uniform_int_distribution<int32_t> mult_d(1 << 30, INT32_MAX);
  std::uniform_int_distribution<int> shift_d(-9, 1);
  for (int ch = 0; ch < c.depth; ++ch) {
    bias[ch] = bias_d(rng);
    mult[ch] = mult_d(rng);
    shift[ch] = shift_d(rng);
  }

  DepthwiseParams p;
  p.padding_type = c.same ? tflite::PaddingType::kSame
                          : tflite::PaddingType::kValid;
  p.padding_values.width = PadBefore(c.w, out_w, c.stride, c.same);
  p.padding_values.height = PadBefore(c.h, out_h, c.stride, c.same);
  p.stride_width = p.stride_height = c.stride;
  p.dilation_width_factor = p.dilation_height_factor = 1;
  p.depth_multiplier = 1;
  p.input_offset = c.input_offset;
  p.weights_offset = 0;  // the CFU path requires zero weight offset
  p.output_offset = c.output_offset;
  p.quantized_activation_min = c.act_min;
  p.quantized_activation_max = c.act_max;

  tflite::reference_integer_ops::DepthwiseConvPerChannel(
      p, mult.data(), shift.data(), in_shape, input.data(), f_shape,
      filter.data(), b_shape, bias.data(), out_shape, ref.data());

  mock_cfu::reset_stats();
  tflite::reference_integer_ops::Mnv2DepthwiseConvPerChannel3x3(
      p, mult.data(), shift.data(), in_shape, input.data(), f_shape,
      filter.data(), b_shape, bias.data(), out_shape, opt.data());
  const mock_cfu::State& s = mock_cfu::st();

  uint64_t bad = 0;
  for (size_t i = 0; i < ref.size(); ++i) {
    if (ref[i] != opt[i]) {
      if (bad < 5) {
        const int ch = i % c.depth;
        const int x = (i / c.depth) % out_w;
        const int y = i / (c.depth * out_w);
        std::printf(
            "MISMATCH case=%d kind=%s in=%dx%dx%d stride=%d pad=%s "
            "index=%zu (y=%d x=%d c=%d) expected=%d actual=%d\n",
            idx, c.kind, c.h, c.w, c.depth, c.stride, c.same ? "SAME" : "VALID",
            i, y, x, ch, ref[i], opt[i]);
      }
      ++bad;
    }
  }

  ++t.cases;
  t.elems += ref.size();
  t.cfu_windows += s.n_run;
  t.load += s.n_load;
  t.shift += s.n_shift;
  t.protocol_errors += s.protocol_errors;
  if (s.n_shift > 0) ++t.cases_with_shift;
  if (s.n_run > 0 && s.n_shift == 0) ++t.cases_load_only;
  if (s.n_run < ref.size()) ++t.cases_with_border;
  if (bad) {
    ++t.mismatching_cases;
    t.mismatching_elems += bad;
  }
  return bad == 0;
}

}  // namespace

int main() {
  std::mt19937 rng(20261103u);  // fixed seed
  const int dims[] = {5, 7, 14, 28, 56};
  const int depths[] = {1, 8, 16, 32};
  Totals t;
  int idx = 0;

  for (int h : dims)
    for (int w : dims)
      for (int d : depths)
        for (int stride : {1, 2})
          for (bool same : {true, false}) {
            std::uniform_int_distribution<int> off(-127, 128);
            std::uniform_int_distribution<int> oo(-128, 127);
            Case c{h, w, d, stride, same, off(rng), oo(rng), -128, 127,
                   "random"};
            if (idx % 2) {  // narrower activation clamp on half the cases
              c.act_min = std::max(-128, c.output_offset - 20);
              c.act_max = std::min(127, c.output_offset + 40);
            }
            RunCase(idx++, c, rng, t);
          }

  // Extreme operands: +-128/127 data, extreme input offsets and clamps.
  for (int off : {-127, 128}) {
    for (int stride : {1, 2}) {
      Case c{14, 14, 8, stride, true, off, 127, -128, 127, "extreme"};
      RunCase(idx++, c, rng, t);
      Case c2{7, 7, 16, stride, false, off, -128, -128, 127, "extreme"};
      RunCase(idx++, c2, rng, t);
    }
  }

  std::printf(
      "coverage: output_elems=%llu cfu_windows(RUN)=%llu "
      "software_border_elems=%llu LOAD=%llu SHIFT_RIGHT=%llu\n",
      (unsigned long long)t.elems, (unsigned long long)t.cfu_windows,
      (unsigned long long)(t.elems - t.cfu_windows),
      (unsigned long long)t.load, (unsigned long long)t.shift);
  std::printf(
      "coverage: cases_with_sliding=%llu cases_load_only=%llu "
      "cases_with_software_border=%llu protocol_errors=%llu\n",
      (unsigned long long)t.cases_with_shift,
      (unsigned long long)t.cases_load_only,
      (unsigned long long)t.cases_with_border,
      (unsigned long long)t.protocol_errors);
  std::printf("cases=%llu mismatches=%llu\n", (unsigned long long)t.cases,
              (unsigned long long)t.mismatching_elems);
  return (t.mismatching_elems == 0 && t.protocol_errors == 0) ? 0 : 1;
}
