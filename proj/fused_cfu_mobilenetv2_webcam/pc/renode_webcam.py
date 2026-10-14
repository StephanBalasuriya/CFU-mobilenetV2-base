#!/usr/bin/env python3
"""
renode_webcam.py -- run the fused-CFU MobileNetV2 webcam application under Renode, with the PC webcam as the camera.

    make renode-webcam            (instead of `make renode`)

What it does
  1. starts Renode (headless) with the simulated board's UART exposed on a local TCP socket,
  2. becomes your console: the CFU-Playground menu and everything the firmware prints appear in THIS terminal and
     your key presses go to the simulated board,
  3. when you press  3  (project menu) and the firmware reports "@@READY", it opens the webcam and, every INTERVAL
     seconds (default 120), captures a picture, sends it to the simulated board, and prints the predicted class,
     top-5, and the cycle counts,
  4. after COUNT pictures (default 5 = 10 minutes) it tells the firmware to leave the webcam server, the CFU-Playground
     menu comes back, and the console keeps running (press 3 to run another round, Ctrl-C to quit Renode).

Without `make`:
    python3 renode_webcam.py --renode ../../../third_party/renode/renode --workdir ../build/renode --resc digilent_arty.resc
Renode already running with  emulation CreateServerSocketTerminal 4321 "t" false ; connector Connect sysbus.uart t :
    python3 renode_webcam.py --connect 127.0.0.1:4321
Testing without a camera:  --image some.jpg  (repeatable)
"""
import argparse, csv, datetime, json, os, pty, re, select, signal, socket, subprocess, sys, termios, threading, time, tty

import webcam_classifier as wc
from webcam_classifier import BoardLink, CameraSource, ImageSource, fnv1a, load_labels, save_capture, to_model_input

HERE = os.path.dirname(os.path.abspath(__file__))
_DEBUG = {"f": None}


def dbg(msg):
    """--debug: timestamped trace of everything the program sees (file <out-dir>/renode_webcam_debug.log)."""
    f = _DEBUG["f"]
    if f:
        f.write("%s  %s\n" % (datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3], msg))
        f.flush()


# ----------------------------------------------------------------------------- the board's output, read from Renode's log
_ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\[[0-9;]*m")           # colour codes, with or without the ESC byte
_UART = re.compile(r"uart: \[host:[^\]]*\] ?(.*)$")


def uart_text_of(console_line):
    """'12:56:34.8553 [INFO] uart: [host: 12.27s (+3.35s)|virt: 24.52s (+6.76s)] @@ACK len=...'  ->  '@@ACK len=...'
    (None for every other Renode message)."""
    m = _UART.search(_ANSI.sub("", console_line))
    return m.group(1).rstrip("\r") if m else None


class LogTap:
    """Turns the byte stream of Renode's console into the lines the simulated board printed.  Renode logs every UART
    line as  '<time> [INFO] uart: [host: ..|virt: ..] <text>' ; the same line can appear twice (stdout and stderr go
    to the same terminal), so a line identical to the previous one within 100 ms is dropped."""
    def __init__(self, on_line):
        self.on_line = on_line
        self.buf = b""
        self.last = (None, 0.0)

    def feed(self, data):
        self.buf += data
        while True:
            i = min([k for k in (self.buf.find(b"\n"), self.buf.find(b"\r")) if k >= 0] or [-1])
            if i < 0:
                break
            raw, self.buf = self.buf[:i], self.buf[i + 1:]
            text = uart_text_of(raw.decode("utf-8", "replace"))
            if text is None:
                continue
            now = time.time()
            if text == self.last[0] and now - self.last[1] < 0.1:
                self.last = (text, now)
                continue
            self.last = (text, now)
            self.on_line(text)


# ----------------------------------------------------------------------------- Renode process (own pseudo-terminal)
class RenodeProcess:
    def __init__(self, exe, workdir, resc, tcp_port, log_path):
        self.exe, self.workdir, self.resc, self.port, self.log_path = exe, workdir, resc, tcp_port, log_path
        self.p = None
        self.master = None
        self.tail = b""
        self.logf = None
        self.tap = None                                   # LogTap: the board's output, parsed from Renode's log

    def start(self, emit_config):
        wrapper = os.path.join(self.workdir, "webcam_uart.resc")
        with open(wrapper, "w") as f:
            f.write("include @%s\n" % self.resc)
            f.write('emulation CreateServerSocketTerminal %d "webcam_term"%s\n' % (self.port, "" if emit_config else " false"))
            f.write("connector Connect sysbus.uart webcam_term\n")
            f.write("start\n")
        self.master, slave = pty.openpty()                  # Renode's --console mode wants a terminal
        self.logf = open(self.log_path, "ab")
        self.p = subprocess.Popen([self.exe, "--console", "--disable-xwt", "webcam_uart.resc"], cwd=self.workdir,
                                  stdin=slave, stdout=slave, stderr=slave, close_fds=True, start_new_session=True)
        os.close(slave)
        threading.Thread(target=self._pump, daemon=True).start()

    def _pump(self):
        while True:
            try:
                d = os.read(self.master, 4096)
            except OSError:
                return
            if not d:
                return
            self.tail = (self.tail + d)[-3000:]
            try:
                self.logf.write(d); self.logf.flush()
            except Exception:
                pass
            if self.tap is not None:
                try:
                    self.tap.feed(d)
                except Exception as e:
                    dbg("log tap error: %r" % e)

    def alive(self):
        return self.p is not None and self.p.poll() is None

    def cmd(self, text):
        """Type one command into Renode's monitor (the pseudo-terminal is its console)."""
        dbg("monitor> %s" % text)
        os.write(self.master, (text + "\r").encode())

    def stop(self):
        if not self.alive():
            self._close_master()
            return
        try:
            os.write(self.master, b"quit\r")
            self.p.wait(timeout=4)
        except Exception:
            try:
                os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)
                self.p.wait(timeout=3)
            except Exception:
                try:
                    os.killpg(os.getpgid(self.p.pid), signal.SIGKILL)
                except Exception:
                    pass
        self._close_master()

    def _close_master(self):
        try:
            if self.master is not None:
                os.close(self.master)
                self.master = None
        except OSError:
            pass


# ----------------------------------------------------------------------------- socket transport that also acts as the console
class SocketTransport:
    """TCP socket to Renode's UART terminal.  Every received byte is also handed to on_chunk (for the console display).
    Telnet negotiation bytes (if Renode sends any) are stripped."""
    def __init__(self, host, port, on_chunk=None):
        self._addr = (host, port)
        self.sock = socket.create_connection((host, port), timeout=5)
        self.sock.settimeout(0.2)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.on_chunk = on_chunk
        self._st = 0

    def write(self, b):
        self.sock.sendall(b)

    def _strip(self, data):
        out = bytearray()
        for c in data:
            if self._st == 0:
                if c == 0xFF:
                    self._st = 1
                else:
                    out.append(c)
            elif self._st == 1:
                self._st = 2 if 251 <= c <= 254 else 0
            else:
                self._st = 0
        return bytes(out)

    def read_chunk(self):
        try:
            d = self.sock.recv(4096)
        except socket.timeout:
            return b""
        if d == b"":
            raise ConnectionError("connection closed")
        d = self._strip(d)
        if d and self.on_chunk:
            self.on_chunk(d)
        return d

    def reconnect(self):
        for _ in range(5):
            try:
                self.sock.close()
                self.sock = socket.create_connection(self._addr, timeout=5)
                self.sock.settimeout(0.2)
                self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                dbg("reconnected to %s" % (self._addr,))
                return True
            except OSError:
                time.sleep(0.5)
        return False

    def close(self):
        try:
            self.sock.close()
        except Exception:
            pass


# ----------------------------------------------------------------------------- keyboard (cbreak) -- works without a tty too
class Keyboard:
    def __init__(self):
        self.fd = sys.stdin.fileno()
        self.tty = sys.stdin.isatty()
        self.eof = False
        self.old = None

    def __enter__(self):
        if self.tty:
            self.old = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
        return self

    def __exit__(self, *a):
        if self.old is not None:
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)

    def read(self):
        if self.eof:
            return b""
        if select.select([self.fd], [], [], 0)[0]:
            d = os.read(self.fd, 64)
            if not d:
                self.eof = True
            return d
        return b""


# ----------------------------------------------------------------------------- console state shared with the reader thread
class Console:
    def __init__(self, auto3):
        self.show = True
        self.auto3 = auto3
        self.sent3 = False
        self.nbytes = 0
        self.tail = ""
        self.link = None
        self.mailbox = None                      # RAM address of the firmware's picture mailbox (from "@@MAILBOX")
        self.nlines = 0
        self.menu_seen = False
        self.log_mode = False                    # board output comes from Renode's log instead of the socket
        self.renode = None

    def on_uart_line(self, text):
        """one line the simulated board printed (taken from Renode's log)"""
        self.nlines += 1
        dbg("uart line: %r" % text[:160])
        if self.link is not None:
            self.link.feed(text)
        if self.show:
            sys.stdout.write(text + "\n")
            sys.stdout.flush()
        if "Embench IoT" in text:                                    # last line of the CFU-Playground menu
            self.menu_seen = True
            if self.auto3 and not self.sent3 and self.link is not None:
                self.sent3 = True
                self.link.send(b"3")

    def on_chunk(self, d):
        if self.log_mode:                        # the socket is only used for typing; its output is not shown twice
            dbg("rx(socket, ignored) %d bytes" % len(d))
            return
        self.nbytes += len(d)
        dbg("rx %d bytes: %r" % (len(d), d[:160]))
        text = d.decode("utf-8", "replace")
        if self.show:
            sys.stdout.write(text.replace("\r\n", "\n"))
            sys.stdout.flush()
        self.tail = (self.tail + text)[-40:]
        if self.auto3 and not self.sent3 and "main> " in self.tail and self.link is not None:
            self.sent3 = True
            self.link.send(b"3")


def hms():
    return datetime.datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------------------------------------- the capture loop
def webcam_loop(link, con, kb, a, labels, results_csv, renode=None):
    con.show = False
    print("\n\n" + "=" * 72)
    print(" WEBCAM LOOP: %d picture(s), one every %d s (first one now)   [q = stop early]" % (a.count, a.interval))
    print("=" * 72)
    src = None
    try:
        if a.image or a.image_dir:
            paths = list(a.image or [])
            if a.image_dir:
                paths += sorted(os.path.join(a.image_dir, f) for f in os.listdir(a.image_dir)
                                if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")))
            src = ImageSource(paths)
            print("(using %d image file(s) instead of the camera)" % len(paths))
        else:
            print("Opening camera %s ..." % a.camera)
            src = CameraSource(a.camera)
            print("Camera is open.")
    except Exception as e:
        print("ERROR: %s" % e)
        print("Leaving the webcam server (BYE).")
        _leave(link, con)
        return []

    preview = not a.no_preview and isinstance(src, CameraSource)
    os.makedirs(a.out_dir, exist_ok=True)
    new_csv = not os.path.exists(results_csv)
    done = []
    next_t = time.monotonic() + a.first_delay
    stop = False
    try:
        for n in range(1, a.count + 1):
            while time.monotonic() < next_t and not stop:           # wait, keep the camera fresh, watch for 'q'
                src.pump()
                left = int(next_t - time.monotonic())
                if preview:
                    try:
                        fr = src.preview_bgr()
                        if fr is not None:
                            import cv2
                            fr = fr.copy()
                            cv2.putText(fr, "picture %d/%d in %ds" % (n, a.count, max(0, left)), (10, 24),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            cv2.imshow("fused-CFU MobileNetV2 under Renode", fr)
                            cv2.waitKey(30)
                    except Exception:
                        preview = False
                        print("(preview window not available - continuing without it)")
                else:
                    time.sleep(0.1)
                if b"q" in kb.read():
                    stop = True
                if not a.quiet_wait and left % 30 == 0 and left > 0 and getattr(webcam_loop, "_lastp", None) != (n, left):
                    webcam_loop._lastp = (n, left)
                    print("   [%s] next picture (%d/%d) in %d s" % (hms(), n, a.count, left))
            if stop:
                print("\nStopped early by 'q'.")
                break

            t_start = time.monotonic()
            stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            base = os.path.join(a.out_dir, stamp)
            rgb = src.latest_rgb()
            data = to_model_input(rgb, a.center_crop)
            save_capture(base, rgb, data)
            print("\n" + "-" * 72)
            print(" [%s] PICTURE %d of %d   saved %s.{jpg,dat,h}" % (hms(), n, a.count, base))
            print("-" * 72)
            row = dict(timestamp=stamp, picture=n, image=base + ".dat")

            def prog(dn, tot, _last=[-1]):
                if dn * 10 // tot != _last[0]:
                    _last[0] = dn * 10 // tot
                    print("   sending to the simulated board %3d%%" % (dn * 100 // tot), end="\r", flush=True)
            try:
                use_mb = renode is not None and con.mailbox is not None and a.transport in ("auto", "mailbox")
                if a.transport == "mailbox" and not use_mb:
                    raise RuntimeError("--transport mailbox needs Renode started by this program and the firmware "
                                       "that prints @@MAILBOX (rebuild the firmware: make renode-webcam)")
                if use_mb:
                    print("   placing the picture in the simulated board's RAM (Renode monitor, no UART transfer) ...")

                    def send_fn(payload, _base=base):
                        mailbox_send(renode, con.mailbox, os.path.abspath(_base + ".dat"), payload, n)
                else:
                    send_fn = None
                r = link.classify(data, progress=prog, chunk=a.chunk, delay=a.chunk_delay, send_fn=send_fn, ack_timeout=a.ack_timeout,
                                  on_ack=lambda: print("   picture accepted by the simulated board; it is classifying it now "
                                                       "(Renode can take minutes) ..."),
                                  heartbeat=lambda t: print("   ... still running, %d s elapsed (wall clock)" % t))
                print(" " * 60)
                name = labels.get(r["top1"], "class %d" % r["top1"])
                if a.show_profile:
                    for ln in r["profile"]:
                        print("   board>", ln)
                print("   transfer %.1f s (wall clock), inference %.1f s (wall clock)" % (r["send_s"], r["infer_s"]))
                print("   >>> PREDICTED CLASS: %d  %s   (score %.6f)" % (r["top1"], name, r["score_e6"] / 1e6))
                for i, (idx, sc) in enumerate(r["top5"]):
                    print("       #%d  %4d  %-28s %.6f" % (i + 1, idx, labels.get(idx, "?"), sc / 1e6))
                if r["cycles"]:
                    print("   whole-model cycles : {:,}   (= {:.1f} ms at 75 MHz)".format(r["cycles"], r["cycles"] / 75e3))
                if r["fused"]:
                    f = r["fused"]
                    print("   fused CFU          : %d/16 blocks, CFU busy {:,} cycles, fused-path CPU {:,} cycles".format(
                        f.get("hw_cycles", 0), f.get("cpu_cycles", 0)) % f.get("blocks", 0))
                row.update(top1=r["top1"], label=name, score=r["score_e6"] / 1e6, cycles=r["cycles"],
                           fused_blocks=(r["fused"] or {}).get("blocks"), fused_hw_cycles=(r["fused"] or {}).get("hw_cycles"),
                           fused_cpu_cycles=(r["fused"] or {}).get("cpu_cycles"), send_s=round(r["send_s"], 1))
                with open(base + ".json", "w") as jf:
                    json.dump({k: v for k, v in r.items() if k != "profile"}, jf)
                done.append(row)
            except (TimeoutError, RuntimeError, ConnectionError) as e:
                print("   ERROR:", e)
                row.update(label="ERROR: %s" % e)
                if "closed" in str(e):
                    stop = True
            with open(results_csv, "a", newline="") as cf:
                cols = ["timestamp", "picture", "image", "top1", "label", "score", "cycles", "fused_blocks",
                        "fused_hw_cycles", "fused_cpu_cycles", "send_s"]
                w = csv.DictWriter(cf, fieldnames=cols)
                if new_csv:
                    w.writeheader(); new_csv = False
                w.writerow({c: row.get(c, "") for c in cols})
            if stop:
                break
            if n < a.count:
                late = time.monotonic() - (next_t + a.interval)
                if late > 0:
                    print("   (this picture took longer than the interval: the next one starts right away)")
                next_t = max(next_t + a.interval, time.monotonic() + 0.5)
    finally:
        try:
            src.close()
        except Exception:
            pass
        try:
            import cv2
            cv2.destroyAllWindows()
        except Exception:
            pass

    print("\n" + "=" * 72)
    print(" SUMMARY (%d of %d pictures classified)" % (len(done), a.count))
    for r in done:
        print("   #%d  %s  %-28s score %.3f   cycles {:,}".format(r.get("cycles") or 0) %
              (r["picture"], r["timestamp"], r.get("label", "?"), r.get("score") or 0))
    print("=" * 72)
    _leave(link, con)
    return done


def mailbox_send(renode, addr, path, payload, seq):
    """Put one picture into the board's mailbox through Renode's monitor:
    pause, copy the 150528 bytes to addr+16, write fnv/length/seq, write the magic LAST, resume."""
    fnv = fnv1a(payload)
    renode.cmd("pause")
    renode.cmd("sysbus LoadBinary @%s 0x%08x" % (path, addr + 16))
    renode.cmd("sysbus WriteDoubleWord 0x%08x 0x%08x" % (addr + 12, fnv))
    renode.cmd("sysbus WriteDoubleWord 0x%08x 0x%08x" % (addr + 8, seq))
    renode.cmd("sysbus WriteDoubleWord 0x%08x 0x%08x" % (addr + 4, len(payload)))
    renode.cmd("sysbus WriteDoubleWord 0x%08x 0x494D4721" % addr)
    renode.cmd("start")


def mailbox_bye(renode, addr):
    renode.cmd("pause")
    renode.cmd("sysbus WriteDoubleWord 0x%08x 0x42594521" % addr)
    renode.cmd("start")


def _leave(link, con):
    """Tell the firmware to leave the image server; the CFU-Playground menu comes back."""
    con.show = True                       # everything the firmware prints from now on (incl. the menu) is displayed
    if con.renode is not None and con.mailbox is not None:
        mailbox_bye(con.renode, con.mailbox)              # no UART involved
    else:
        link.send(b"BYE!")
    t0 = time.time()
    while time.time() - t0 < 30:
        ln = link._get(0.5)
        if ln is None:
            return
        if ln.startswith("@@BYE"):
            break
    time.sleep(0.5)
    print("\n[back at the CFU-Playground menu: press 3 for another round, Ctrl-C to quit]\n")


# ----------------------------------------------------------------------------- main
def parse_connect(s):
    h, _, p = s.rpartition(":")
    return (h or "127.0.0.1"), int(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--renode", default=None, help="path of the renode executable (default: <repo>/third_party/renode/renode)")
    ap.add_argument("--workdir", default=os.path.join(HERE, "..", "build", "renode"), help="build/renode directory")
    ap.add_argument("--resc", default="digilent_arty.resc", help="generated Renode script inside --workdir")
    ap.add_argument("--tcp-port", type=int, default=4321, help="local TCP port of Renode's UART terminal (default 4321)")
    ap.add_argument("--connect", default=None, metavar="HOST:PORT", help="do not start Renode, connect to a running one")
    ap.add_argument("--camera", default="0")
    ap.add_argument("--count", type=int, default=5, help="pictures per round (default 5)")
    ap.add_argument("--interval", type=float, default=120.0, help="seconds between pictures (default 120)")
    ap.add_argument("--first-delay", type=float, default=2.0, help="seconds between '@@READY' and the first picture")
    ap.add_argument("--out-dir", default="captures")
    ap.add_argument("--center-crop", action="store_true")
    ap.add_argument("--image", action="append", help="image file(s) instead of the camera (testing)")
    ap.add_argument("--image-dir")
    ap.add_argument("--no-preview", action="store_true")
    ap.add_argument("--labels", default=os.path.join(HERE, "labels.txt"))
    ap.add_argument("--transport", choices=("auto", "mailbox", "uart"), default="auto",
                    help="how the picture reaches the simulated board: 'mailbox' = copied into its RAM through Renode's "
                         "monitor (default when this program started Renode), 'uart' = sent over the UART")
    ap.add_argument("--ack-timeout", type=float, default=60.0, help="seconds to wait for the board to accept a picture")
    ap.add_argument("--board-output", choices=("auto", "log", "socket"), default="auto",
                    help="where the board's output is read from: 'log' = Renode's console log (default when this program "
                         "started Renode: it contains every UART line), 'socket' = the UART socket")
    ap.add_argument("--chunk", type=int, default=16, help="bytes per write to the simulated UART (default 16)")
    ap.add_argument("--chunk-delay", type=float, default=0.002, help="pause after each write, seconds (default 0.002)")
    ap.add_argument("--show-profile", action="store_true", help="also print the firmware's per-operator cycle table")
    ap.add_argument("--quiet-wait", action="store_true", help="no countdown lines while waiting")
    ap.add_argument("--auto3", action="store_true", help="press '3' automatically when the main menu appears")
    ap.add_argument("--once", action="store_true", help="quit after the first round instead of staying in the console")
    ap.add_argument("--debug", action="store_true", help="write a trace of all received data to <out-dir>/renode_webcam_debug.log")
    a = ap.parse_args()

    labels = load_labels(a.labels)
    if a.debug:
        os.makedirs(a.out_dir, exist_ok=True)
        _DEBUG["f"] = open(os.path.join(a.out_dir, "renode_webcam_debug.log"), "a")
        dbg("---- started: %s" % " ".join(sys.argv))
    renode = None
    log_path = os.path.join(os.path.abspath(a.workdir), "renode_webcam.log")

    if a.connect:
        host, port = parse_connect(a.connect)
    else:
        exe = a.renode or os.path.join(HERE, "..", "..", "..", "third_party", "renode", "renode")
        exe = os.path.abspath(exe)
        if not os.path.exists(exe):
            sys.exit("renode executable not found: %s  (pass --renode)" % exe)
        workdir = os.path.abspath(a.workdir)
        if not os.path.exists(os.path.join(workdir, a.resc)):
            sys.exit("%s not found - run `make renode-scripts` first" % os.path.join(workdir, a.resc))
        host, port = "127.0.0.1", a.tcp_port
        renode = RenodeProcess(exe, workdir, a.resc, port, log_path)

    con = Console(a.auto3)
    con.renode = renode
    if renode and a.board_output in ("auto", "log"):
        con.log_mode = True                       # board output comes from Renode's log (see LogTap) from the very start
        renode.tap = LogTap(con.on_uart_line)
    transport = None
    try:
        if renode:
            for emit in (False, True):
                print("Starting Renode (log: %s) ..." % log_path)
                renode.start(emit)
                t0 = time.time()
                while time.time() - t0 < 60 and transport is None:
                    if not renode.alive():
                        break
                    try:
                        transport = SocketTransport(host, port, con.on_chunk)
                    except OSError:
                        time.sleep(0.5)
                if transport is not None:
                    break
                print("Renode did not open the UART socket. Last Renode output:\n%s" %
                      renode.tail.decode("utf-8", "replace")[-1200:])
                renode.stop()
                if emit:
                    sys.exit("giving up - see %s" % log_path)
                print("Retrying with the default terminal options ...")
        else:
            transport = SocketTransport(host, port, con.on_chunk)

        link = BoardLink(transport, verbose=False)
        con.link = link
        if a.auto3 and con.menu_seen and not con.sent3:        # the menu was printed before we connected
            con.sent3 = True
            link.send(b"3")
        if con.log_mode:
            link.ignore_transport_lines = True
            dbg("board output is read from Renode's log; the socket is used for typing only")
        print("Connected to the simulated board.  This terminal is now its console.")
        print("Press 3 for the project menu: the webcam loop starts by itself (%d pictures, every %d s)." %
              (a.count, a.interval))
        print("Ctrl-C quits.\n")

        t_conn = time.time()
        nudged = False
        results_csv = os.path.join(a.out_dir, "results.csv")
        with Keyboard() as kb:
            while True:
                if renode and not renode.alive():
                    print("\nRenode has exited. Last output:\n%s" % renode.tail.decode("utf-8", "replace")[-800:])
                    break
                if not nudged and con.nbytes == 0 and con.nlines == 0 and time.time() - t_conn > 2.5:
                    nudged = True                                   # the banner went by before we connected:
                    link.send(b" ")                                 # an unknown key makes the menu print again
                data = kb.read()
                if data:
                    try:
                        link.send(data)
                    except OSError as e:
                        print("\n[cannot send keys to the simulated board: %s]" % e)
                ln = link._get(0.05)
                if ln is None:
                    print("\nconnection to the simulated board closed.")
                    dbg("connection closed")
                    break
                if ln:
                    dbg("line: %r" % ln[:160])
                if "@@MAILBOX" in ln:
                    m = re.search(r"addr=0x([0-9a-fA-F]+)", ln)
                    if m:
                        con.mailbox = int(m.group(1), 16)
                        dbg("mailbox at 0x%08x" % con.mailbox)
                if "@@READY" in ln:
                    dbg("READY detected -> starting the webcam loop")
                    try:
                        webcam_loop(link, con, kb, a, labels, results_csv, renode)
                    except KeyboardInterrupt:
                        raise
                    except Exception:
                        import traceback
                        print("\nERROR in the webcam loop:\n" + traceback.format_exc())
                        dbg("exception in webcam loop: " + traceback.format_exc())
                        _leave(link, con)
                    con.sent3 = False
                    if a.once:
                        time.sleep(1.0)
                        break
                if kb.eof and not a.auto3 and not data:
                    pass
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        if transport:
            transport.close()
        if renode:
            print("Stopping Renode ...")
            renode.stop()


if __name__ == "__main__":
    main()
