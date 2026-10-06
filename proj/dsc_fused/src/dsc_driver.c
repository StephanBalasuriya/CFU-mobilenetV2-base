// dsc_driver.c -- loads config/weights/ifmap into the fused DSC CFU and runs it.
#include "dsc_driver.h"

// ---- CFU access -----------------------------------------------------------
// On target (CFU-Playground) cfu.h provides cfu_op0(funct7, rs1, rs2).
// For host-side protocol logging, compile with -DDSC_CFU_STUB and provide
// uint32_t dsc_cfu_stub(int f7, uint32_t a, uint32_t b).
#ifdef DSC_CFU_STUB
  extern uint32_t dsc_cfu_stub(int f7, uint32_t a, uint32_t b);
  #define DSC_CFU(f7, a, b) dsc_cfu_stub((f7), (uint32_t)(a), (uint32_t)(b))
#else
  #include "cfu.h"
  #define DSC_CFU(f7, a, b) ((uint32_t)cfu_op0((f7), (uint32_t)(a), (uint32_t)(b)))
#endif

enum { F_PING = 0, F_CFG = 1, F_MEMW = 2, F_START = 3, F_STATUS = 4, F_OUTRD = 5, F_WAIT = 6, F_CYCLES = 7 };
enum { MEM_EXW = 0, MEM_EXB = 1, MEM_EXM = 2, MEM_EXS = 3, MEM_DWW = 4 /*..12*/,
       MEM_DWB = 13, MEM_DWM = 14, MEM_DWS = 15, MEM_PRW = 16, MEM_PRB = 17, MEM_PRM = 18,
       MEM_PRS = 19, MEM_IFM = 20 };
enum { C_H, C_W, C_N, C_M, C_P, C_STRIDE, C_OUT_H, C_OUT_W, C_ROWOFF, C_COLOFF,
       C_EX_INOFF, C_EX_ZP, C_EX_MIN, C_EX_MAX, C_DW_INOFF, C_DW_ZP, C_DW_MIN, C_DW_MAX,
       C_PR_INOFF, C_PR_ZP, C_PR_MIN, C_PR_MAX, C_WQN, C_NC };

static inline void cfg(int idx, int32_t v)                 { DSC_CFU(F_CFG, idx, v); }
static inline void memw(int id, uint32_t addr, uint32_t d) { DSC_CFU(F_MEMW, ((uint32_t)id << 27) | addr, d); }
static inline uint32_t pack4(const int8_t *p) {
  return (uint32_t)(uint8_t)p[0] | ((uint32_t)(uint8_t)p[1] << 8) |
         ((uint32_t)(uint8_t)p[2] << 16) | ((uint32_t)(uint8_t)p[3] << 24);
}

uint32_t dsc_ping(void) { return DSC_CFU(F_PING, 0, 0); }

void dsc_load_layer(const dsc_layer_t *L) {
  const int NC = L->N / 8, WQ = (L->W + 2) / 3;
  cfg(C_H, L->H); cfg(C_W, L->W); cfg(C_N, L->N); cfg(C_M, L->M); cfg(C_P, L->P);
  cfg(C_STRIDE, L->stride); cfg(C_OUT_H, L->out_h); cfg(C_OUT_W, L->out_w);
  cfg(C_ROWOFF, L->row_off); cfg(C_COLOFF, L->col_off);
  cfg(C_EX_INOFF, L->ex_in_off); cfg(C_EX_ZP, L->ex_out_zp); cfg(C_EX_MIN, L->ex_min); cfg(C_EX_MAX, L->ex_max);
  cfg(C_DW_INOFF, L->dw_in_off); cfg(C_DW_ZP, L->dw_out_zp); cfg(C_DW_MIN, L->dw_min); cfg(C_DW_MAX, L->dw_max);
  cfg(C_PR_INOFF, L->pr_in_off); cfg(C_PR_ZP, L->pr_out_zp); cfg(C_PR_MIN, L->pr_min); cfg(C_PR_MAX, L->pr_max);
  cfg(C_WQN, WQ * NC); cfg(C_NC, NC);

  for (int w = 0; w < L->M * L->N / 4; w++) memw(MEM_EXW, w, pack4(L->ex_w + 4 * w));
  for (int m = 0; m < L->M; m++) {
    memw(MEM_EXB, m, (uint32_t)L->ex_b[m]); memw(MEM_EXM, m, (uint32_t)L->ex_m[m]); memw(MEM_EXS, m, (uint32_t)L->ex_s[m]);
    memw(MEM_DWB, m, (uint32_t)L->dw_b[m]); memw(MEM_DWM, m, (uint32_t)L->dw_m[m]); memw(MEM_DWS, m, (uint32_t)L->dw_s[m]);
  }
  for (int j = 0; j < 9; j++)                               // bank j = filter tap j
    for (int w = 0; w < L->M / 4; w++) memw(MEM_DWW + j, w, pack4(L->dw_w + j * L->M + 4 * w));
  for (int p = 0; p < L->P; p++) {
    for (int w = 0; w < L->M / 4; w++) memw(MEM_PRW, ((uint32_t)p << 8) | w, pack4(L->pr_w + p * L->M + 4 * w));
    memw(MEM_PRB, p, (uint32_t)L->pr_b[p]); memw(MEM_PRM, p, (uint32_t)L->pr_m[p]); memw(MEM_PRS, p, (uint32_t)L->pr_s[p]);
  }
}

void dsc_load_ifmap(const dsc_layer_t *L, const int8_t *in) {
  const int WQ = (L->W + 2) / 3, wpp = L->N / 4;            // 32-bit words per pixel
  for (int r = 0; r < L->H; r++)
    for (int c = 0; c < L->W; c++) {
      const int bank = (r % 3) * 3 + (c % 3);
      const int slot = (r / 3) * WQ + (c / 3);
      const int8_t *px = in + (r * L->W + c) * L->N;
      for (int j = 0; j < wpp; j++)
        memw(MEM_IFM, ((uint32_t)bank << 23) | (uint32_t)(slot * wpp + j), pack4(px + 4 * j));
    }
}

void dsc_start(void)  { DSC_CFU(F_START, 0, 0); }
void dsc_wait(void)   { DSC_CFU(F_WAIT, 0, 0); }
void dsc_run(void)    { dsc_start(); dsc_wait(); }
uint32_t dsc_hw_cycles(void) { return DSC_CFU(F_CYCLES, 0, 0); }

void dsc_read_output(const dsc_layer_t *L, int8_t *out) {
  const int words = L->out_h * L->out_w * L->P / 4;
  for (int w = 0; w < words; w++) {
    uint32_t v = DSC_CFU(F_OUTRD, w, 0);
    out[4 * w + 0] = (int8_t)(v);       out[4 * w + 1] = (int8_t)(v >> 8);
    out[4 * w + 2] = (int8_t)(v >> 16); out[4 * w + 3] = (int8_t)(v >> 24);
  }
}
