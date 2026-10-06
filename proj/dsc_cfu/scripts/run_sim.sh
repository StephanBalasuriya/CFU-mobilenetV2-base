#!/bin/sh
# Regression: for each config -> generate vectors -> build+run real C driver with logging stub
#             -> replay instruction stream in RTL (Icarus) -> compare with Python golden.
# Usage: scripts/run_sim.sh            (run from the project root)
set -e
mkdir -p build
iverilog -g2005 -o build/sim.vvp tb/tb_cfu.v rtl/cfu.v
fail=0
run() {
  echo "=== $* ==="
  python3 scripts/gen_vectors.py --outdir build "$@"
  gcc -O1 -Wall -DDSC_CFU_STUB -Isw -Ibuild -o build/host_log sw/host_log_main.c sw/dsc_driver.c sw/dsc_ref.c
  ./build/host_log build/cmds.txt
  out=$(vvp build/sim.vvp 2>&1 | grep -E "MISMATCH|RESULT|busy cycles")
  echo "$out"
  echo "$out" | grep -q "RESULT: PASS" || fail=1
}
run --H 8  --W 8  --N 8  --M 16 --P 8  --stride 1 --seed 1
run --H 8  --W 8  --N 8  --M 16 --P 8  --stride 2 --seed 2
run --H 9  --W 7  --N 16 --M 24 --P 16 --stride 1 --seed 3
run --H 11 --W 10 --N 16 --M 32 --P 8  --stride 2 --seed 4
run --H 6  --W 6  --N 24 --M 48 --P 24 --stride 1 --seed 5
run --H 7  --W 7  --N 8  --M 48 --P 56 --stride 1 --seed 6
run --H 10 --W 10 --N 8  --M 16 --P 8  --stride 1 --seed 7 --pos 0.5
run --H 5  --W 5  --N 56 --M 336 --P 56 --stride 1 --seed 8
run --H 3  --W 3  --N 8  --M 8  --P 4  --stride 1 --seed 9
run --H 13 --W 13 --N 8  --M 48 --P 8  --stride 2 --seed 10
[ $fail -eq 0 ] && echo "ALL REGRESSIONS PASSED" || { echo "SOME REGRESSIONS FAILED"; exit 1; }
