# Webcam application under Renode

`make renode-webcam` works like `make renode`, but the **PC webcam** feeds the simulated board.

```
cd proj/fused_cfu_mobilenetv2_webcam        # inside the cfu-common conda environment
make renode-webcam
```

1. `make` builds the firmware and the Renode scripts (as `make renode` does), then starts `pc/renode_webcam.py`.
2. That program starts Renode **headless** with the board's UART on a local TCP socket (port 4321) and becomes the
   board's console: the CFU-Playground menu and all firmware output appear in the terminal; your key presses go to
   the simulated board.
3. Press **3** (project menu). The firmware prints `@@READY`, the program opens the webcam and:
   * takes a picture right away and then every **120 s** (`--interval`), **5** pictures (`--count`) = 10 minutes,
   * sends each picture (224x224 RGB, checksummed) to the simulated board,
   * prints the **predicted class**, the top-5, the **cycle counts** (whole model, CFU busy, fused-path CPU) and the
     wall-clock times, and saves `captures/<stamp>.{jpg,dat,h,json}` and `captures/results.csv`.
4. After the last result the program sends `BYE!`; the firmware leaves the image server and the **CFU-Playground menu
   comes back** (press 3 again for another round, **Ctrl-C** to quit and stop Renode).

Options (`make renode-webcam WEBCAM_ARGS="..."`):

| option | meaning |
|---|---|
| `--count N`, `--interval S` | pictures per round (5) and seconds between them (120) |
| `--camera 1` | another camera index (or a video file) |
| `--no-preview` | no preview window (e.g. over SSH) |
| `--show-profile` | also print the firmware's per-operator cycle table |
| `--auto3` | press 3 automatically when the menu appears |
| `--tcp-port 4400` | another local port if 4321 is taken |
| `--transport uart` | send the picture over the simulated UART instead of the RAM mailbox |
| `--chunk 8 --chunk-delay 0.004` | (UART transport only) send more slowly |
| `--image a.jpg --image b.jpg` | use image files instead of the camera (testing) |
| `--once` | quit after the first round |
| `q` (while waiting) | stop the loop early and return to the menu |

## How it works

The firmware runs inside Renode and cannot see the PC's webcam, so the PC program sits between them:
webcam -> `renode_webcam.py` -> TCP socket -> Renode's simulated UART -> firmware (`src/image_server.h`).
The simulated board's console therefore appears in the terminal running `make renode-webcam`, not in Renode's own
UART window (a program cannot type into that window). Protocol additions for this flow: `BYE!` makes the firmware
leave the image server (`@@BYE`), so the menu returns.

## Notes and troubleshooting

* **Timing.** Pictures are taken every `--interval` seconds of *wall-clock* time. Simulating one inference in Renode
  (with the CFU running through Verilator) can take minutes; if a picture is still being processed when the next one
  is due, the next one starts right after it (a message says so). The cycle counts printed are the simulated board's
  (75 MHz) cycles, independent of how long the simulation took.
* **Where the board's output comes from.** Renode logs every line the simulated board prints
  (`uart: [host: ..|virt: ..] <text>`), and the program reads the board's output from that log (`--board-output log`,
  the default when it starts Renode); the UART socket is only used for typing keys. This was added after a real run
  showed that the socket stopped delivering the board's replies although the board was answering. The log is also kept
  in `build/renode/renode_webcam.log`. `--board-output socket` selects the socket again. At the end of a round `BYE`
  goes through the mailbox as well, so the loop does not depend on the socket at all.
* **How the picture reaches the simulated board.** Pushing 150 KB through Renode's simulated UART did not work reliably
  (the board's UART receive path is interrupt driven with a 128-byte ring buffer; single key presses and the board's text
  output are fine, bulk input is not). So the firmware has a **mailbox in RAM** (`@@MAILBOX addr=0x...` is printed before
  `@@READY`): the PC program copies the picture into it through Renode's monitor (`pause`, `sysbus LoadBinary @file
  addr`, `sysbus WriteDoubleWord ...`, `start`), the firmware sees it, checks length and checksum, and answers over the
  UART as before. No UART transfer is involved, so it takes a fraction of a second. On a real board the picture still
  goes over the UART (that path is unchanged). `--transport uart` forces the UART transfer in Renode too (paced chunks;
  a failed transfer is retried with smaller, slower chunks); `--transport mailbox` insists on the mailbox.
* **Renode log:** `build/renode/renode_webcam.log` (Renode's own messages, including errors of the monitor commands
  the program types; look here if a picture is never accepted).
* **Qt / Wayland warnings** printed by OpenCV when the preview window opens are harmless; `--no-preview` silences them.
* **"renode did not open the UART socket"**: the log tail is printed; it is retried once with Renode's default terminal
  options. Make sure no other Renode (e.g. `make renode`) is still running.
* **Camera:** `ERROR: cannot open camera 0` -> close other programs using it, try `--camera 1`.
* **Menu text not shown right after start:** the banner was printed before the program connected; the program sends
  one unknown key to make the menu print again (you will see ` *unknown*`).

## Tests

`scripts/test_renode_flow.sh` tests the PC program without Renode or a camera, against stand-ins in
`sim/fake_renode/` (a fake `renode` that opens the UART socket and a fake board that speaks the real protocol).
It checks the whole round (start, menu, `3`, pictures at the interval, class and cycles printed, return to the menu,
shutdown), the retry after a corrupted transfer, the fallback if Renode rejects a terminal option, connecting to a
running Renode, and stopping early. The firmware's `Serve()` loop including `BYE!` was tested separately with a
small harness built from the real `src/image_server.h`.

**Confirmed on a real Renode** (by the user's log): Renode starts from `make renode-webcam`, the menu, key `3`, the model
load, `@@READY`, the camera, the first capture, and the mailbox transfer: the monitor commands were accepted and the
firmware answered `@@ACK`, classified the picture (class 785, 311,867,000 cycles, 16 of 16 blocks fused) and printed the
result. `sim/renode_console_sample.txt` is a trimmed copy of that real console output, used as a test fixture.
**Not tested here:** a complete round against a real Renode with the log-based output channel (the parser and the
classification were tested on the real console text above, and the whole program against stand-ins). The firmware side
(mailbox, checksum, ACK/NAK, BYE) was tested with a harness built from the real `src/image_server.h`.
