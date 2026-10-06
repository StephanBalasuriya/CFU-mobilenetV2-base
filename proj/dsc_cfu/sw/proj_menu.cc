// proj_menu.cc -- CFU-Playground menu for the fused DSC CFU.
// Replace proj/<your_proj>/proj_menu.cc with this file and copy dsc_driver.{c,h}, dsc_ref.c and
// the generated test_vectors.h into the same project directory (next to proj_menu.cc).
#include "proj_menu.h"
#include <stdio.h>
#include <stdlib.h>
#include "menu.h"
#include "perf.h"
#include "dsc_driver.h"
#include "test_vectors.h"      // from scripts/gen_vectors.py

static void do_ping(void) {
  printf("CFU PING -> 0x%08lx (expect 0xd5c00001)\n", (unsigned long)dsc_ping());
}

static void do_selftest(void) {
  const dsc_layer_t *L = &dsc_tv_layer;
  const int out_n = L->out_h * L->out_w * L->P;
  static int8_t f1[40 * 40 * 48], f2[40 * 40 * 48], out_sw[40 * 40 * 8 * 6], out_hw[40 * 40 * 8 * 6];
  if (L->H * L->W * L->M > (int)sizeof f1 || out_n > (int)sizeof out_hw) { puts("test vector too large for static buffers"); return; }

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

  int bad_hw = 0, bad_sw = 0;
  for (int i = 0; i < out_n; i++) { bad_hw += out_hw[i] != dsc_tv_expected[i]; bad_sw += out_sw[i] != dsc_tv_expected[i]; }
  printf("CFU vs golden : %s (%d/%d mismatches)\n", bad_hw ? "FAIL" : "PASS", bad_hw, out_n);
  printf("SW  vs golden : %s (%d/%d mismatches)\n", bad_sw ? "FAIL" : "PASS", bad_sw, out_n);
  printf("cycles  load_weights=%u  load_ifmap=%u  compute(CPU-side)=%u  hw_busy=%lu  read_out=%u\n",
         t1 - t0, t2 - t1, t3 - t2, (unsigned long)dsc_hw_cycles(), t4 - t3);
  printf("cycles  software layer-by-layer reference = %u\n", t5 - t4);
  printf("fused total (ifmap+compute+readback)      = %u\n", (t2 - t1) + (t3 - t2) + (t4 - t3));
}

static struct Menu MENU = {
    "Fused DSC CFU", "dsc",
    {
        MENU_ITEM('p', "ping CFU", do_ping),
        MENU_ITEM('t', "self-test + cycle comparison", do_selftest),
        MENU_END,
    },
};

extern "C" void do_proj_menu() { menu_run(&MENU); }
