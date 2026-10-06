// dsc_driver.h -- software side of the fused DSC CFU
#pragma once
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
  int H, W, N, M, P;                 // input HxWxN, expanded channels M, output channels P
  int stride, out_h, out_w;
  int row_off, col_off;              // = -pad_top, -pad_left  (TFLite SAME padding)
  int ex_in_off, ex_out_zp, ex_min, ex_max;   // in_off = -input_zero_point
  int dw_in_off, dw_out_zp, dw_min, dw_max;   // dw_in_off = -ex_out_zp
  int pr_in_off, pr_out_zp, pr_min, pr_max;   // pr_in_off = -dw_out_zp
  const int8_t  *ex_w;  const int32_t *ex_b, *ex_m, *ex_s;   // [M][N]   TFLite filter layout
  const int8_t  *dw_w;  const int32_t *dw_b, *dw_m, *dw_s;   // [3][3][M]
  const int8_t  *pr_w;  const int32_t *pr_b, *pr_m, *pr_s;   // [P][M]
} dsc_layer_t;

// weights/params/config: load once per layer.   ifmap: load per inference.
void     dsc_load_layer(const dsc_layer_t *L);
void     dsc_load_ifmap(const dsc_layer_t *L, const int8_t *in_nhwc);
void     dsc_start(void);
void     dsc_wait(void);
void     dsc_run(void);                                  // start + wait
void     dsc_read_output(const dsc_layer_t *L, int8_t *out_nhwc);
uint32_t dsc_hw_cycles(void);                            // busy cycles of last job
uint32_t dsc_ping(void);                                 // expect 0xD5C00001

// pure-C layer-by-layer reference (the "baseline" / what TFLM does op-by-op)
// f1_buf: H*W*M bytes, f2_buf: out_h*out_w*M bytes (these are the intermediate maps the CFU removes)
void     dsc_ref_run(const dsc_layer_t *L, const int8_t *in, int8_t *f1_buf, int8_t *f2_buf, int8_t *out);

#ifdef __cplusplus
}
#endif
