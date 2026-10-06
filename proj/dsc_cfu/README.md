# Fused DSC CFU (Expansion -> Depthwise -> Projection) for CFU-Playground

University study implementation of the architecture in Yildirim & Ozturk,
"RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions in Edge AI".

## Layout
rtl/cfu.v              whole accelerator, single file (module Cfu)
sw/dsc_driver.[ch]     loads config/weights/ifmap, runs, reads output
sw/dsc_ref.c           layer-by-layer INT8 reference (software baseline + golden on target)
sw/proj_menu.cc        CFU-Playground menu (ping, self-test, cycle comparison)
sw/host_log_main.c     PC-side logger: runs the real driver, logs every custom instruction
tb/tb_cfu.v            replays the log into the RTL, checks outputs
scripts/gen_vectors.py bit-exact TFLM golden model + test-vector/header generator
scripts/run_sim.sh     10-config regression;  scripts/run_layer.sh  single (paper) layer

## Step 1 - simulate (PC)
    sh scripts/run_sim.sh            # must end with ALL REGRESSIONS PASSED
    sh scripts/run_layer.sh 40 40 8 48 8 1 l3     # paper 3rd layer (slow: minutes)
Needs iverilog, gcc, python3+numpy.

## Step 2 - build on FPGA
    cp -r $CFU_ROOT/proj/proj_template_v $CFU_ROOT/proj/dsc_fused
    cp rtl/cfu.v sw/proj_menu.cc sw/dsc_driver.* sw/dsc_ref.c dsc_fused/
    python3 scripts/gen_vectors.py --H 40 --W 40 --N 8 --M 48 --P 8 --outdir dsc_fused
    cd $CFU_ROOT/proj/dsc_fused && make clean && make prog TARGET=digilent_nexys_a7_100 && make load
(Target name and file locations depend on your CFU-Playground version; keep the template's
cfu.h. If its macro is not cfu_op0(funct7,rs1,rs2) edit the DSC_CFU macro in dsc_driver.c.)
Menu: 'p' must print 0xd5c00001, then 't' must print PASS for CFU and SW.
Delete the generated build/ directory before rebuilding after any RTL change.

## Step 3 - measure
Vivado reports (LUT/FF/BRAM/DSP/WNS) for the synthesized design; menu 't' prints cycles.
If DSPs or timing are too tight, lower NPE in module Cfu (max output channels P) or
add pipeline registers; hw cycle counter = CYCLES instruction.

## Limits
IFMAP bank depth 1024 x 64b (IF_AW), expansion weights M*N <= 32768, output buffer 16 KB,
P <= NPE(56), N,M multiples of 8, P multiple of 4, H,W <= 255. Larger maps: tile in
software (row_off/col_off exist for this; untested). Residual add stays in software.
The fused op is not auto-used by TFLM: needs a custom op / graph rewrite.
