/*
 * Host-side software model of the 3x3 depthwise CFU (custom function 0,
 * funct7 40..44). Selected instead of the hardware cfu.h with
 * "-I tools/mock" so that src/mnv2_cfu.h and
 * mnv2_depthwise_conv.h compile unchanged on a host.
 *
 * Semantics are taken from gateware/macc.py (Depthwise3x3Mac) and the
 * xetters in gateware/mnv2_cfu.py (_make_depthwise_3x3):
 *
 *   43 CONFIGURE   input_offset = signed9(in0), weight_offset = signed9(in1),
 *                  load_index = 0.
 *   40 LOAD        in0/in1 hold four signed bytes (byte 0 = LSB). Each is
 *                  extended by the matching offset to a signed 10-bit value.
 *                  load_index 0 -> window[0..3], 1 -> window[4..7],
 *                  2 -> window[8] (byte 0 only; products become fresh).
 *                  Products are signed 20-bit. load_index wraps 0,1,2,0.
 *   44 SHIFT_RIGHT each input row moves left by one; new right column is
 *                  signed byte of in0 (row 0 = bits 7:0, row 1 = 15:8,
 *                  row 2 = 23:16) + input_offset. Weights unchanged.
 *                  Products become stale.
 *   41 RUN         if stale: products = input_window * weight_window.
 *                  Then 3-stage reduction (21, 22, 32-bit signed sums).
 *   42 GET_RESULT  returns the 32-bit signed result of the last RUN.
 *
 * Besides the arithmetic, the mock counts instructions and flags protocol
 * violations (RUN with a partial window, SHIFT_RIGHT before a full window).
 * Any other funct7 aborts, because the host test never uses them.
 */
#ifndef HOST_MOCK_CFU_H
#define HOST_MOCK_CFU_H

#include <cstdint>
#include <cstdio>
#include <cstdlib>

namespace mock_cfu {

// Sign-extend the low `bits` bits of v.
inline int64_t wrap(int64_t v, int bits) {
  const uint64_t mask = (bits == 64) ? ~0ULL : ((1ULL << bits) - 1);
  uint64_t u = static_cast<uint64_t>(v) & mask;
  const uint64_t sign = 1ULL << (bits - 1);
  return static_cast<int64_t>((u ^ sign) - sign);
}

inline int64_t byte_s(uint32_t word, int n) {
  return static_cast<int8_t>((word >> (8 * n)) & 0xff);
}

struct State {
  int64_t input_offset = 0, weight_offset = 0;
  int load_index = 0;
  int64_t in_win[9] = {}, w_win[9] = {}, prod[9] = {};
  bool stale = false;
  int64_t result = 0;
  bool window_valid = false;  // a complete LOAD x3 happened since reset
  bool ran = false;

  // Statistics and protocol checks.
  uint64_t n_cfg = 0, n_load = 0, n_shift = 0, n_run = 0, n_get = 0;
  uint64_t protocol_errors = 0;
};

inline State& st() {
  static State s;
  return s;
}

inline void reset_stats() {
  State& s = st();
  s = State{};
}

inline uint32_t op(uint32_t funct7, uint32_t in0, uint32_t in1) {
  State& s = st();
  switch (funct7) {
    case 43: {  // CONFIGURE
      ++s.n_cfg;
      s.input_offset = wrap(static_cast<int32_t>(in0), 9);
      s.weight_offset = wrap(static_cast<int32_t>(in1), 9);
      s.load_index = 0;
      s.window_valid = false;
      s.stale = false;
      return 0;
    }
    case 40: {  // LOAD
      ++s.n_load;
      const int nbytes = (s.load_index == 2) ? 1 : 4;
      const int base = s.load_index * 4;
      for (int b = 0; b < nbytes; ++b) {
        const int64_t iv = wrap(byte_s(in0, b) + s.input_offset, 10);
        const int64_t wv = wrap(byte_s(in1, b) + s.weight_offset, 10);
        s.in_win[base + b] = iv;
        s.w_win[base + b] = wv;
        s.prod[base + b] = wrap(iv * wv, 20);
      }
      if (s.load_index == 2) {
        s.stale = false;
        s.window_valid = true;
        s.load_index = 0;
      } else {
        ++s.load_index;
      }
      return 0;
    }
    case 44: {  // SHIFT_RIGHT
      ++s.n_shift;
      if (!s.window_valid) ++s.protocol_errors;
      for (int row = 0; row < 3; ++row) {
        const int b = row * 3;
        s.in_win[b + 0] = s.in_win[b + 1];
        s.in_win[b + 1] = s.in_win[b + 2];
        s.in_win[b + 2] = wrap(byte_s(in0, row) + s.input_offset, 10);
      }
      s.stale = true;
      return 0;
    }
    case 41: {  // RUN
      ++s.n_run;
      if (!s.window_valid || s.load_index != 0) ++s.protocol_errors;
      if (s.stale) {
        for (int n = 0; n < 9; ++n)
          s.prod[n] = wrap(s.in_win[n] * s.w_win[n], 20);
        s.stale = false;
      }
      int64_t s1[5], s2[3];
      s1[0] = wrap(s.prod[0] + s.prod[1], 21);
      s1[1] = wrap(s.prod[2] + s.prod[3], 21);
      s1[2] = wrap(s.prod[4] + s.prod[5], 21);
      s1[3] = wrap(s.prod[6] + s.prod[7], 21);
      s1[4] = wrap(s.prod[8], 21);
      s2[0] = wrap(s1[0] + s1[1], 22);
      s2[1] = wrap(s1[2] + s1[3], 22);
      s2[2] = wrap(s1[4], 22);
      s.result = wrap(s2[0] + s2[1] + s2[2], 32);
      s.ran = true;
      return 0;
    }
    case 42: {  // GET_RESULT
      ++s.n_get;
      if (!s.ran) ++s.protocol_errors;
      return static_cast<uint32_t>(s.result);
    }
    default:
      std::fprintf(stderr, "mock cfu: unexpected funct7=%u\n", funct7);
      std::abort();
  }
}

}  // namespace mock_cfu

// The kernel header only uses custom function 0.
static inline uint32_t cfu_op0(uint32_t funct7, uint32_t in0, uint32_t in1) {
  return mock_cfu::op(funct7, in0, in1);
}

#endif  // HOST_MOCK_CFU_H
