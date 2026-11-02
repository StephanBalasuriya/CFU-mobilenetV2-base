# CFU-Playground – Nexys A7 Board Testing

Execution guide for building, programming, loading, and testing the
`mnv2_first` CFU-Playground project on a **Nexys A7-100T** using Vivado.

## 1. Prerequisites

- WSL2 / Ubuntu
- CFU-Playground
- Conda environment: `cfu-common`
- Vivado 2024.1
- Nexys A7-100T
- USB cable

Working configuration:

```text
Target:       digilent_nexys4ddr
Toolchain:    Vivadoa
Vivado:       2024.1
UART:         115200
UART device:  /dev/ttyUSB1
Project:      proj/mnv2_first
```

---

## 2. Connect the Board to WSL

### Windows PowerShell — Administrator

Check the board:

```powershell
usbipd list
```

Find the Digilent device, for example:

```text
2-1    0403:6010    USB Serial Converter A, USB Serial Converter B
```

If it says `Not shared`:

```powershell
usbipd bind --busid 2-1
```

Attach it to WSL:

```powershell
usbipd attach --wsl --busid 2-1
```

Use your actual BUSID if it is different.

### WSL

Check USB:

```bash
lsusb
```

Expected:

```text
0403:6010
```

Check the UART:

```bash
ls /dev/ttyUSB*
```

Normally:

```text
/dev/ttyUSB1
```

---

## 3. Setup the CFU Environment

```bash
cd ~/CFU-Playground
source env/conda/bin/activate cfu-common
```

Load Vivado:

```bash
source ~/Xilinx/Vivado/2024.1/settings64.sh
```

Set LiteX paths:

```bash
export PYTHONPATH=$HOME/CFU-Playground/third_party/python/litex:$HOME/CFU-Playground/third_party/python/liteeth:$HOME/CFU-Playground/third_party/python/litedram:$HOME/CFU-Playground/third_party/python/litex-boards:$PYTHONPATH
```

Check:

```bash
python -c "import litex; print('LiteX OK')"
vivado -version
```

---

## 4. Go to the Project

```bash
cd ~/CFU-Playground/proj/mnv2_first
```

---

## 5. Check JTAG

Before building:

```bash
openocd \
-f ~/CFU-Playground/third_party/python/litex_boards/litex_boards/prog/openocd_xc7_ft2232.cfg \
-c "init" \
-c "scan_chain" \
-c "exit"
```

Expected:

```text
JTAG tap: xc7.tap tap/device found: 0x13631093
```

---

## 6. Clean and Program the FPGA

For a fresh build:

```bash
make clean
```

Build and program:

```bash
make prog TARGET=digilent_nexys4ddr USE_VIVADO=1 UART_SPEED=115200
```

Check the generated bitstream if needed:

```bash
ls -lh ~/CFU-Playground/soc/build/digilent_nexys4ddr.mnv2_first/gateware/*.bit
```

---

## 7. Load the Software

Use:

```bash
make load TARGET=digilent_nexys4ddr TTY=/dev/ttyUSB1 UART_SPEED=115200
```

If your UART is different, replace `/dev/ttyUSB1`.

When `litex_term` starts:

**Press RESET on the Nexys A7 once.**

Wait for:

```text
Booting from serial...
```

then:

```text
Liftoff!
```

and finally:

```text
CFU Playground
...
main>
```

---

## 8. Run Golden Tests

At:

```text
main>
```

select:

```text
1
```

Then:

```text
1
```

Select:

```text
g
```

This runs the **Person Detection int8 model Golden Tests**.

---

## 9. Run Automated Tests

Once `make load` successfully reaches:

```text
main>
```

stop the interactive session with:

```text
Ctrl+C
```

Then run:

```bash
make run TARGET=digilent_nexys4ddr TTY=/dev/ttyUSB1 UART_SPEED=115200
```

---

## 10. Troubleshooting

### `Looking for top-level-menu...` keeps appearing

First run:

```bash
make load TARGET=digilent_nexys4ddr TTY=/dev/ttyUSB1 UART_SPEED=115200
```

Make sure the board reaches:

```text
main>
```

before using `make run`.

### Gibberish / incorrect UART output

Check that both build and terminal use:

```text
115200
```

Rebuild if necessary:

```bash
make clean
make prog TARGET=digilent_nexys4ddr USE_VIVADO=1 UART_SPEED=115200
```

### `litex_term` does not stop

```bash
pkill -9 -f litex_term
```

### Terminal stops displaying typed characters

```bash
stty sane
```

---

## 11. Complete Workflow

```bash
# Windows PowerShell first:
# usbipd list
# usbipd attach --wsl --busid <BUSID>

# WSL
cd ~/CFU-Playground
source env/conda/bin/activate cfu-common
source ~/Xilinx/Vivado/2024.1/settings64.sh

export PYTHONPATH=$HOME/CFU-Playground/third_party/python/litex:$HOME/CFU-Playground/third_party/python/liteeth:$HOME/CFU-Playground/third_party/python/litedram:$HOME/CFU-Playground/third_party/python/litex-boards:$PYTHONPATH

cd ~/CFU-Playground/proj/mnv2_first

make clean
make prog TARGET=digilent_nexys4ddr USE_VIVADO=1 UART_SPEED=115200
make load TARGET=digilent_nexys4ddr TTY=/dev/ttyUSB1 UART_SPEED=115200
```

Then:

```text
RESET once
    ↓
Wait for main>
    ↓
Golden test: 1 → 1 → g
```

Or:

```bash
make run TARGET=digilent_nexys4ddr TTY=/dev/ttyUSB1 UART_SPEED=115200
```

> **Important:** Always specify `TARGET=digilent_nexys4ddr` to avoid accidentally using a different default target.
