// host_log_main.c -- compiles the REAL driver on the PC, with the CFU replaced by a
// stub that logs every custom instruction to build/cmds.txt.  The log is replayed
// into the RTL by tb/tb_cfu.v, so the exact instruction stream the RISC-V will
// issue is what gets simulated.  Also checks the C reference against the Python golden.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "test_vectors.h"

static FILE *g_log;
uint32_t dsc_cfu_stub(int f7, uint32_t a, uint32_t b) {
  fprintf(g_log, "%x %08x %08x\n", f7, a, b);
  return 0;
}

int main(int argc, char **argv) {
  const dsc_layer_t *L = &dsc_tv_layer;
  const char *path = argc > 1 ? argv[1] : "build/cmds.txt";
  const int out_n = L->out_h * L->out_w * L->P;
  int8_t *f1 = malloc(L->H * L->W * L->M), *f2 = malloc(L->out_h * L->out_w * L->M), *out = malloc(out_n);
  dsc_ref_run(L, dsc_tv_in, f1, f2, out);
  int bad = 0;
  for (int i = 0; i < out_n; i++) bad += (out[i] != dsc_tv_expected[i]);
  printf("[host] C reference vs Python golden: %s (%d/%d mismatches)\n", bad ? "FAIL" : "PASS", bad, out_n);

  g_log = fopen(path, "w");
  dsc_load_layer(L);
  dsc_load_ifmap(L, dsc_tv_in);
  dsc_run();
  dsc_hw_cycles();
  dsc_read_output(L, out);          // responses are produced by the RTL, not here
  fclose(g_log);
  printf("[host] wrote instruction log %s\n", path);
  return bad != 0;
}
