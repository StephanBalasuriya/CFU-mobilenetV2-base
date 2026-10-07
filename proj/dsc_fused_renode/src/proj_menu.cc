// proj_menu.cc -- menu for the fused DSC CFU.  Copy to proj/<your_proj>/src/proj_menu.cc
// (together with dsc_driver.c/.h, dsc_ref.c and the generated test_vectors.h).
//
//  p  ping the CFU
//  t  self-test + cycle report (hardware counter, formula, CPU counter, speedup)
//  d  diagnose: locate mismatches, check read-back stability, try gap/poll variants
//
// SYSTEM CLOCK: set DSC_MHZ to your SoC clock (Nexys A7 build printed 75 MHz).
#include "proj_menu.h"
#include <stdio.h>
#include <stdlib.h>
#include "menu.h"
#include "perf.h"
#include "dsc_driver.h"
#include "test_vectors.h"

#ifndef DSC_MHZ
#define DSC_MHZ 75
#endif

// static buffers sized for up to 40x40 maps with M=48 (3rd MobileNetV2 layer)
#define BUF_F  (40 * 40 * 48)
#define BUF_O  (40 * 40 * 8 * 6)
static int8_t f1[BUF_F], f2[BUF_F], out_sw[BUF_O], out_hw[BUF_O], out_tmp[BUF_O];

static int count_bad(const int8_t *got, const int8_t *exp, int n, int show, const dsc_layer_t *L) {
  int bad = 0;
  for (int i = 0; i < n; i++)
    if (got[i] != exp[i]) {
      if (bad < show) {
        int pix = i / L->P;
        printf("    idx %d  (y=%d x=%d ch=%d)  got %d  expected %d\n", i, pix / L->out_w, pix % L->out_w,
               i % L->P, got[i], exp[i]);
      }
      bad++;
    }
  return bad;
}

static int fits(const dsc_layer_t *L) {
  if (L->H * L->W * L->M > BUF_F || L->out_h * L->out_w * L->M > BUF_F || L->out_h * L->out_w * L->P > BUF_O) {
    puts("test vector too large for the static buffers in proj_menu.cc");
    return 0;
  }
  return 1;
}

static void do_ping(void) { printf("CFU PING -> 0x%08lx (expect 0xd5c00001)\n", (unsigned long)dsc_ping()); }

static void do_selftest(void) {
  const dsc_layer_t *L = &dsc_tv_layer;
  if (!fits(L)) return;
  const int out_n = L->out_h * L->out_w * L->P;

  unsigned t0 = perf_get_mcycle();
  dsc_load_layer(L);
  unsigned t1 = perf_get_mcycle();
  dsc_load_ifmap(L, dsc_tv_in);
  unsigned t2 = perf_get_mcycle();
  dsc_run();
  unsigned t3 = perf_get_mcycle();
  dsc_read_output(L, out_hw);
  unsigned t4 = perf_get_mcycle();
  dsc_ref_run(L, dsc_tv_in, f1, f2, out_sw);
  unsigned t5 = perf_get_mcycle();

  int bad_hw = count_bad(out_hw, dsc_tv_expected, out_n, 8, L);
  int bad_sw = count_bad(out_sw, dsc_tv_expected, out_n, 0, L);
  unsigned hw = (unsigned)dsc_hw_cycles(), pred = (unsigned)dsc_predict_cycles(L);
  unsigned fused = (t2 - t1) + hw + (t4 - t3), sw = t5 - t4;
  
  printf("\n=== correctness ===\n");
  printf("CFU vs golden : %s (%d/%d mismatches)\n", bad_hw ? "FAIL" : "PASS", bad_hw, out_n);
  printf("SW  vs golden : %s (%d/%d mismatches)\n", bad_sw ? "FAIL" : "PASS", bad_sw, out_n);
  printf("\n=== CFU compute cycles (hardware counter = authoritative) ===\n");
  printf("hw_busy   = %u cycles   (%u us @ %d MHz)\n", hw, hw / DSC_MHZ, DSC_MHZ);
  printf("predicted = %u cycles   -> %s\n", pred, hw == pred ? "MATCH" : "DIFFERENT (check formula/config)");
  printf("            formula: 31 + P + pixels*(2 + M*N/8) + (pixels-1)*max(0, P+4 - M*N/8)\n");
  printf("\n=== CPU-measured phases (mcycle) ===\n");
  printf("load_weights (once/layer) = %u\n", t1 - t0);
  printf("load_ifmap                = %u\n", t2 - t1);
  printf("compute (CPU waiting)     = %u   <- only meaningful on real hardware; Renode does not count CFU time\n", t3 - t2);
  printf("read_out                  = %u\n", t4 - t3);
  printf("fused per-inference total = %u cycles (%u us)\n", fused, fused / DSC_MHZ);
  printf("software reference        = %u cycles (%u us)\n", sw, sw / DSC_MHZ);
  if (fused) printf("speedup (end-to-end)      = %u.%ux   | compute-only (sw / hw_busy) = %u.%ux\n",
                    (unsigned)(sw / fused), (unsigned)((sw * 10ull / fused) % 10),
                    hw ? (unsigned)(sw / hw) : 0u, hw ? (unsigned)((sw * 10ull / hw) % 10) : 0u);
}

static void do_diag(void) {
  const dsc_layer_t *L = &dsc_tv_layer;
  if (!fits(L)) return;
  const int n = L->out_h * L->out_w * L->P;
  int b;

  printf("1) blocking WAIT (expected to FAIL on Renode: its CFU op timeout)\n");
  dsc_set_gap(0);
  dsc_load_layer(L); dsc_load_ifmap(L, dsc_tv_in); dsc_start(); dsc_wait(); dsc_read_output(L, out_hw);
  b = count_bad(out_hw, dsc_tv_expected, n, 12, L);
  printf("   mismatches = %d / %d   hw_busy = %lu\n", b, n, (unsigned long)dsc_hw_cycles());

  printf("2) read-back stability (read output again)\n");
  dsc_read_output(L, out_tmp);
  b = count_bad(out_tmp, out_hw, n, 8, L);
  printf("   differences between two reads = %d\n", b);

  printf("3) re-run without reloading (same inputs)\n");
  dsc_run(); dsc_read_output(L, out_tmp);
  b = count_bad(out_tmp, dsc_tv_expected, n, 8, L);
  printf("   mismatches vs golden = %d\n", b);

  printf("4) gap variant: 2 extra PINGs after every write\n");
  dsc_set_gap(2);
  dsc_load_layer(L); dsc_load_ifmap(L, dsc_tv_in); dsc_run(); dsc_read_output(L, out_tmp);
  dsc_set_gap(0);
  b = count_bad(out_tmp, dsc_tv_expected, n, 8, L);
  printf("   mismatches vs golden = %d\n", b);

  printf("5) poll variant: START, then poll STATUS instead of blocking WAIT\n");
  dsc_load_layer(L); dsc_load_ifmap(L, dsc_tv_in); dsc_start(); dsc_wait_poll(); dsc_read_output(L, out_tmp);
  b = count_bad(out_tmp, dsc_tv_expected, n, 8, L);
  printf("   mismatches vs golden = %d\n", b);
  printf("done. Send me this whole output if any line is non-zero.\n");
}

static struct Menu MENU = {
    "Fused DSC CFU", "dsc",
    {
        MENU_ITEM('p', "ping CFU", do_ping),
        MENU_ITEM('t', "self-test + cycle report", do_selftest),
        MENU_ITEM('d', "diagnose mismatches", do_diag),
        MENU_END,
    },
};

extern "C" void do_proj_menu() { menu_run(&MENU); }