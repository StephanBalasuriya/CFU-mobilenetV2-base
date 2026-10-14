#!/usr/bin/env python3
"""Stand-in for the `renode` executable: reads the generated wrapper script, opens the UART socket terminal it asks
for (like `emulation CreateServerSocketTerminal`), runs the fake board behind it, and understands the monitor commands
the PC program types (pause, start, sysbus LoadBinary @file addr, sysbus WriteDoubleWord addr value, quit)."""
import os, re, sys, threading, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fake_board import FakeBoard

resc = [a for a in sys.argv[1:] if a.endswith(".resc")][0]
text = open(resc).read()
m = re.search(r'CreateServerSocketTerminal\s+(\d+)\s+"[^"]*"(\s+false)?', text)
print("(fake renode) script %s" % resc)
if m.group(2) and os.environ.get("FAKE_RENODE_REJECT_FALSE"):
    print("Bad parameters for command emulation CreateServerSocketTerminal"); sys.stdout.flush(); sys.exit(1)
import datetime
from fake_board import MENU
_t0 = time.time()
_lock = threading.Lock()
ESC = "" if os.environ.get("FAKE_LOG_NO_ESC") else "\x1b"


def log_uart(line):
    """print a UART line the way Renode's log does (colour codes, host/virt time stamps), twice like the real console"""
    now = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-2]
    el = time.time() - _t0
    text = line.rstrip("\r")
    with _lock:
        for _ in range(2):
            sys.stdout.write("%s[39;49m%s[92m%s [INFO] uart: [host: %.2fs (+1ms)|virt: %.2fs (+0s)] %s\n" %
                             (ESC, ESC, now, el, el * 2, text))
        sys.stdout.flush()


mem = bytearray(0x40000) if os.environ.get("FAKE_MAILBOX", "1") != "0" else None
b = FakeBoard(int(m.group(1)), float(os.environ.get("FAKE_INFER_DELAY", "1.0")),
              corrupt_first=bool(os.environ.get("FAKE_CORRUPT_FIRST")), mem=mem,
              uart_bulk_broken=bool(os.environ.get("FAKE_UART_BULK_BROKEN")),
              log_cb=log_uart, socket_dead_after_ready=bool(os.environ.get("FAKE_SOCKET_DEAD_AFTER_READY")))
threading.Thread(target=b.run, daemon=True).start()
for ln in ("Hello, World!\n" + MENU.replace("main> ", "")).split("\n"):      # the boot banner (printed before anyone connects)
    log_uart(ln)
print("(fake renode) UART terminal on port %s" % m.group(1)); sys.stdout.flush()
running = True
for line in sys.stdin:
    cmd = line.strip()
    if not cmd:
        continue
    if cmd == "quit":
        break
    if cmd in ("pause", "start"):
        running = (cmd == "start"); continue
    mm = re.match(r"sysbus LoadBinary @(\S+) (0x[0-9a-fA-F]+|\d+)$", cmd)
    if mm and mem is not None:
        data = open(mm.group(1), "rb").read(); off = int(mm.group(2), 0) - FakeBoard.MEM_BASE
        mem[off:off + len(data)] = data; continue
    mm = re.match(r"sysbus WriteDoubleWord (0x[0-9a-fA-F]+|\d+) (0x[0-9a-fA-F]+|\d+)$", cmd)
    if mm and mem is not None:
        off = int(mm.group(1), 0) - FakeBoard.MEM_BASE; mem[off:off + 4] = int(mm.group(2), 0).to_bytes(4, "little"); continue
    print("Could not find command or device: %s" % cmd); sys.stdout.flush()
