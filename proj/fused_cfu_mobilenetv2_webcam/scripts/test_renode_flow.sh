#!/bin/sh
# Tests pc/renode_webcam.py WITHOUT Renode or a camera, against stand-ins (sim/fake_renode): a fake `renode` that opens
# the UART socket the way the real one does, and a fake board that speaks the real protocol (menu, @@READY, images,
# checksum NAK, BYE!).  Checks: Renode start + UART connection, the menu, '3' starting the loop, N pictures with the
# interval, class + cycles printed, return to the menu, clean shutdown, retry after a corrupted transfer, fallback when
# Renode rejects the terminal option, 'q' stopping early.
cd "$(dirname "$0")/.." || exit 1
T=$(mktemp -d); mkdir -p $T/work $T/img
python3 - "$T" <<'PY'
import sys
from PIL import Image
import numpy as np
t = sys.argv[1]; rng = np.random.default_rng(1)
for i in range(3):
    a = (rng.random((120, 160, 3)) * 255).astype("uint8"); a[:, :, i] = 255
    Image.fromarray(a).save("%s/img/t%d.jpg" % (t, i))
open("%s/work/digilent_arty.resc" % t, "w").write("# dummy\n")
PY
IMG="--image $T/img/t0.jpg --image $T/img/t1.jpg --image $T/img/t2.jpg"
FR=sim/fake_renode/fake_renode.py
RUN="python3 pc/renode_webcam.py --renode $FR --workdir $T/work --resc digilent_arty.resc $IMG --first-delay 1 --once --quiet-wait --chunk 64 --chunk-delay 0.0005 --out-dir $T/cap"
fail=0
chk() { if echo "$2" | grep -q "$3"; then echo "   PASS  $1"; else echo "   FAIL  $1  (missing: $3)"; fail=1; fi; }

echo "== 0. Renode log parser on a REAL console capture (sim/renode_console_sample.txt)"
python3 sim/test_log_tap.py | grep -E "PASS|FAIL" | sed 's/^/ /'
python3 sim/test_log_tap.py > /dev/null 2>&1 || fail=1

echo "== 1. normal round: 3 pictures, 4 s apart, '3' pressed automatically"
O=$(FAKE_INFER_DELAY=0.5 timeout 120 $RUN --tcp-port 4381 --count 3 --interval 4 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "UART connected"               "$O" "Connected to the simulated board"
chk "menu shown"                   "$O" "3: Project menu"
chk "loop started after @@READY"   "$O" "WEBCAM LOOP: 3 picture"
chk "picture 3 of 3"               "$O" "PICTURE 3 of 3"
chk "predicted class printed"      "$O" "PREDICTED CLASS"
chk "cycles printed"               "$O" "whole-model cycles"
chk "fused CFU stats printed"      "$O" "fused CFU"
chk "summary printed"              "$O" "SUMMARY (3 of 3"
chk "back at the menu"             "$O" "back at the CFU-Playground menu"
chk "Renode stopped"               "$O" "Stopping Renode"
n=$(echo "$O" | grep -c "PICTURE [0-9] of 3")
[ "$n" -eq 3 ] && echo "   PASS  exactly 3 pictures" || { echo "   FAIL  picture count $n"; fail=1; }

echo "== 2. corrupted first transfer -> NAK -> automatic retry"
O=$(FAKE_INFER_DELAY=0.2 FAKE_CORRUPT_FIRST=1 timeout 120 $RUN --tcp-port 4382 --count 1 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "retry announced"              "$O" "transfer failed"
chk "result after the retry"       "$O" "PREDICTED CLASS"

echo "== 3. Renode rejects the 'false' terminal option -> retried with default options"
O=$(FAKE_RENODE_REJECT_FALSE=1 FAKE_INFER_DELAY=0.2 timeout 120 $RUN --tcp-port 4383 --count 1 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "fallback used"                "$O" "Retrying with the default terminal options"
chk "result after the fallback"    "$O" "PREDICTED CLASS"

echo "== 4. connect to a running Renode, user types 3, 'q' stops early"
(cd sim/fake_renode && python3 fake_board.py 4384 0.3 >/dev/null 2>&1 & echo $! > $T/fb.pid); sleep 1
O=$( (printf '3'; sleep 6; printf 'q'; sleep 3) | timeout 60 python3 pc/renode_webcam.py --connect 127.0.0.1:4384 $IMG --count 5 --interval 20 --first-delay 1 --once --quiet-wait --chunk 64 --chunk-delay 0.0005 --out-dir $T/cap4 2>&1 | tr '\r' '\n')
kill $(cat $T/fb.pid) 2>/dev/null
chk "first picture classified"     "$O" "PREDICTED CLASS"
chk "stopped early by q"           "$O" "Stopped early by 'q'"
chk "back at the menu"             "$O" "back at the CFU-Playground menu"

echo "== 5. Renode flow uses the RAM mailbox (picture placed through the monitor, no UART transfer)"
O=$(FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4385 --count 2 --interval 3 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "mailbox transfer announced"   "$O" "placing the picture in the simulated board's RAM"
chk "board accepted the picture"   "$O" "picture accepted by the simulated board"
chk "both pictures classified"     "$O" "SUMMARY (2 of 2"
n=$(echo "$O" | grep -c "sending to the simulated board")
[ "$n" -eq 0 ] && echo "   PASS  no UART bulk transfer used" || { echo "   FAIL  UART transfer was used ($n lines)"; fail=1; }

echo "== 6. bulk UART input broken (the real Renode symptom): mailbox still works, plain UART reports it"
O=$(FAKE_UART_BULK_BROKEN=1 FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4386 --count 1 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "mailbox works anyway"         "$O" "PREDICTED CLASS"
O=$(FAKE_UART_BULK_BROKEN=1 FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4387 --count 1 --auto3 --transport uart --ack-timeout 2 < /dev/null 2>&1 | tr '\r' '\n')
chk "UART path: no answer reported" "$O" "transfer failed (no answer)"

echo "== 7. firmware without mailbox (older firmware): automatic fallback to the UART transfer"
O=$(FAKE_MAILBOX=0 FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4388 --count 1 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "UART fallback works"          "$O" "PREDICTED CLASS"

echo "== 8. the UART socket delivers NO output after @@READY (the real failure): board output is read from Renode's log"
O=$(FAKE_SOCKET_DEAD_AFTER_READY=1 FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4389 --count 2 --interval 3 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "board output taken from the log" "$O" "WEBCAM LOOP: 2 picture"
chk "picture accepted"             "$O" "picture accepted by the simulated board"
chk "both pictures classified"     "$O" "SUMMARY (2 of 2"
chk "BYE through the mailbox: menu again" "$O" "back at the CFU-Playground menu"
n=$(echo "$O" | grep -c "Project menu")
[ "$n" -ge 2 ] && echo "   PASS  menu printed again after the round ($n times)" || { echo "   FAIL  menu not shown again"; fail=1; }

echo "== 9. Renode console without ESC bytes (as when pasted), duplicates, stray prompt text"
O=$(FAKE_LOG_NO_ESC=1 FAKE_INFER_DELAY=0.3 timeout 120 $RUN --tcp-port 4390 --count 1 --auto3 < /dev/null 2>&1 | tr '\r' '\n')
chk "works without ESC bytes"      "$O" "PREDICTED CLASS"

rm -rf $T
[ $fail -eq 0 ] && echo "RESULT: ALL PASS" || { echo "RESULT: FAIL"; exit 1; }
