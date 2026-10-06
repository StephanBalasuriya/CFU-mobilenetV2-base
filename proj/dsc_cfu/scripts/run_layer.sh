#!/bin/sh
# usage: scripts/run_layer.sh H W N M P [stride] [tag]   -> builds in build_<tag>/ (safe to run in parallel)
H=$1; W=$2; N=$3; M=$4; P=$5; S=${6:-1}; TAG=${7:-L${H}x${W}x${N}}
D=build_$TAG; mkdir -p $D
python3 scripts/gen_vectors.py --outdir $D --H $H --W $W --N $N --M $M --P $P --stride $S --seed 11 | head -1
gcc -O1 -DDSC_CFU_STUB -Isw -I$D -o $D/host_log sw/host_log_main.c sw/dsc_driver.c sw/dsc_ref.c
./$D/host_log $D/cmds.txt > /dev/null
sed -e "s#build/#$D/#g" tb/tb_cfu.v > $D/tb.v
iverilog -g2005 -o $D/sim.vvp $D/tb.v rtl/cfu.v
vvp $D/sim.vvp 2>&1 | grep -E "RESULT|busy cycles|commands|MISMATCH"
