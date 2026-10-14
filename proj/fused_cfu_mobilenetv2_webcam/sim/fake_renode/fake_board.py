#!/usr/bin/env python3
"""Stand-in for the simulated board (CFU-Playground menu + the image server of src/image_server.h) on a TCP socket.
Used by scripts/test_renode_flow.sh; it speaks exactly the protocol the firmware speaks."""
import socket, struct, sys, threading, time

MENU = ("\nCFU Playground\n==============\n 1: TfLM Models menu\n 2: Functional CFU Tests\n 3: Project menu\n"
        " 4: Performance Counter Tests\n 5: TFLite Unit Tests\n 6: Benchmarks\n 7: Util Tests\n 8: Embench IoT\nmain> ")


def fnv1a(d):
    h = 2166136261
    for b in d:
        h = ((h ^ b) * 16777619) & 0xFFFFFFFF
    return h


class FakeBoard:
    MEM_BASE, MB_ADDR = 0x40000000, 0x40001000

    def __init__(self, port, infer_delay=1.0, corrupt_first=False, mem=None, uart_bulk_broken=False,
                 log_cb=None, socket_dead_after_ready=False):
        self.port, self.infer_delay, self.corrupt_first = port, infer_delay, corrupt_first
        self.mem = mem                           # bytearray = the board's RAM, shared with fake_renode (mailbox mode)
        self.uart_bulk_broken = uart_bulk_broken  # emulates the real Renode problem: big UART transfers get no answer
        self.bad_sent = False
        self.log_cb = log_cb                      # called with every complete line the board prints (Renode's UART log)
        self.socket_dead_after_ready = socket_dead_after_ready   # emulates the real failure: no output over the socket
        self.dead_out = False
        self._lbuf = ""
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", port))
        self.srv.listen(1)
        self.rounds = 0

    def say(self, c, s):
        if self.log_cb:
            self._lbuf += s
            while "\n" in self._lbuf:
                line, self._lbuf = self._lbuf.split("\n", 1)
                self.log_cb(line)
        if not self.dead_out:
            c.sendall(s.replace("\n", "\r\n").encode())
        if self.socket_dead_after_ready and "@@READY" in s:
            self.dead_out = True

    def run(self):
        while True:
            c, _ = self.srv.accept()
            try:
                self.session(c)
            except Exception as e:
                print("fake board session ended:", e, file=sys.stderr)
            finally:
                c.close()

    def process(self, c, img, sent, frames):
        """verify, ACK, 'classify', report (what handle() in image_server.h does)"""
        if self.corrupt_first and not self.bad_sent:
            self.bad_sent = True
            img = bytes([img[0] ^ 1]) + img[1:]
        calc = fnv1a(img)
        if calc != sent:
            self.say(c, "@@NAK reason=checksum sent=0x%08x calc=0x%08x\n" % (sent, calc))
            return frames
        self.say(c, "@@ACK len=%d fnv=0x%08x\n" % (len(img), calc))
        time.sleep(self.infer_delay)
        frames += 1
        top = (img[0] * 7 + img[1000] * 3 + frames) % 1000
        cyc = 120_000_000 + (calc % 1_000_000)
        self.say(c, "Profile:\n  CONV_2D   ( 1234567 ) cycles\n  DEPTHWISE ( 2345678 ) cycles\n"
                    "( %d ) cycles total\n@@FUSED blocks=16 hw_cycles=1837367 cpu_cycles=%d\n" % (cyc, cyc // 3))
        self.say(c, "@@RESULT frame=%d top1=%d score_e6=612345\n" % (frames, top))
        self.say(c, "@@TOP5 %d:612345 7:100000 9:50000 11:20000 13:1000\n" % top)
        self.say(c, "@@LOGITS_E6 " + ",".join(["0"] * 1000) + "\n@@END\n")
        return frames

    def poll_mailbox(self, c, frames):
        o = self.MB_ADDR - self.MEM_BASE
        if self.mem is not None and int.from_bytes(self.mem[o:o + 4], "little") == 0x42594521:
            self.mem[o:o + 4] = b"\0\0\0\0"
            self.say(c, "@@BYE frames=%d\nWebcam server finished - back to the menu.\n%s" % (frames, MENU))
            return frames, True
        if self.mem is not None and int.from_bytes(self.mem[o:o + 4], "little") == 0x494D4721:
            length = int.from_bytes(self.mem[o + 4:o + 8], "little"); sent = int.from_bytes(self.mem[o + 12:o + 16], "little")
            img = bytes(self.mem[o + 16:o + 16 + length])
            self.mem[o:o + 4] = b"\0\0\0\0"
            if length != 150528:
                self.say(c, "@@NAK reason=length got=%d\n" % length)
            else:
                frames = self.process(c, img, sent, frames)
        return frames, False

    def session(self, c):
        buf = b""
        mode = "menu"
        frames = 0
        c.settimeout(0.05)
        while True:
            try:
                d = c.recv(4096)
                if not d:
                    return
                buf += d
            except socket.timeout:
                d = None
            if mode == "server":
                frames, bye = self.poll_mailbox(c, frames)
                if bye:
                    mode = "menu"
            while buf:
                if mode == "menu":
                    k, buf = buf[:1], buf[1:]
                    if k == b"3":
                        self.say(c, "3\n\nRunning Project menu\n" + "=" * 40 +
                                 "\n MobileNetV2 a0.35 INT8  -  FUSED-CFU WEBCAM SERVER\n" + "=" * 40 +
                                 "\nLoading MobileNetV2 model...\nModel loaded successfully.\n\n" +
                                 ("@@MAILBOX addr=0x%08x size=150544\n" % self.MB_ADDR if self.mem is not None else "") +
                                 "@@READY mode=fused_dsc_cfu bytes=150528\n")
                        mode = "server"; frames = 0
                    else:
                        self.say(c, (" *unknown*\n" if k not in (b"\n", b"\r") else "") + MENU)
                else:
                    if buf[:4] == b"IMG?":
                        buf = buf[4:]; self.say(c, "@@READY mode=fused_dsc_cfu bytes=150528\n")
                    elif buf[:4] == b"BYE!":
                        buf = buf[4:]
                        self.say(c, "@@BYE frames=%d\nWebcam server finished - back to the menu.\n%s" % (frames, MENU))
                        mode = "menu"
                    elif buf[:4] == b"IMG!":
                        if len(buf) < 8:
                            break
                        n = struct.unpack("<I", buf[4:8])[0]
                        if len(buf) < 8 + n + 4:
                            break
                        img = buf[8:8 + n]; sent = struct.unpack("<I", buf[8 + n:12 + n])[0]
                        buf = buf[12 + n:]
                        if self.uart_bulk_broken:
                            continue                      # bytes "lost": no ACK, no NAK
                        frames = self.process(c, img, sent, frames)
                    else:
                        buf = buf[1:]


if __name__ == "__main__":
    port = int(sys.argv[1]); delay = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    FakeBoard(port, delay, corrupt_first="--corrupt-first" in sys.argv).run()
