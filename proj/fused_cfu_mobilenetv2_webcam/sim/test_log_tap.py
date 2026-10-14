#!/usr/bin/env python3
"""Replays a REAL Renode console capture (sim/renode_console_sample.txt: colour-code remnants, every UART line printed
twice, monitor prompts mixed into lines) through the log parser and through BoardLink.classify, and checks that the
board's lines and the result (class, cycles, fused stats) come out right."""
import os, sys, threading, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "pc"))
import renode_webcam as rw
from webcam_classifier import BoardLink

got = []
rw.LogTap(got.append).feed(open(os.path.join(HERE, "renode_console_sample.txt"), "rb").read())
ok = True
def check(name, cond):
    global ok
    print("   %s  %s" % ("PASS" if cond else "FAIL", name)); ok = ok and cond
for want in ("Hello, World!", " 3: Project menu", " 8: Embench IoT", "main> 3", "@@MAILBOX addr=0x402c28a0 size=150544",
             "@@READY mode=fused_dsc_cfu bytes=150528", "@@ACK len=150528 fnv=0xf32f562c",
             "   312M (    311867000 )  cycles total", "@@RESULT frame=1 top1=785 score_e6=136718", "@@END"):
    check("line extracted: %s" % want.strip()[:50], want in got)
check("each line once (duplicates dropped)", got.count("@@ACK len=150528 fnv=0xf32f562c") == 1)
check("Renode's own messages are not board lines", not any(("Machine" in g) or ("Pausing" in g) or ("sysbus" in g) for g in got))

class Dummy:
    def read_chunk(self): time.sleep(0.1); return b""
    def write(self, b): pass
link = BoardLink(Dummy()); link.ignore_transport_lines = True
def feeder():
    time.sleep(0.3)
    on = False
    for ln in got:
        on = on or ln.startswith("@@ACK")
        if on: link.feed(ln); time.sleep(0.005)
threading.Thread(target=feeder, daemon=True).start()
r = link.classify(bytes(150528), ack_timeout=10, result_timeout=20, send_fn=lambda p: None)
check("classify: class 785", r["top1"] == 785)
check("classify: 311,867,000 cycles", r["cycles"] == 311867000)
check("classify: 16 fused blocks, hw 1,837,367 cycles", r["fused"] and r["fused"]["blocks"] == 16 and r["fused"]["hw_cycles"] == 1837367)
print("RESULT: ALL PASS" if ok else "RESULT: FAIL"); sys.exit(0 if ok else 1)
