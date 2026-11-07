 CXX micro_test_globals.cc     micro_test_globals.o
  CXX flatbuffer_conversions_bridge.cc  flatbuffer_conversions_bridge.o
  CXX micro_error_reporter.cc   micro_error_reporter.o
  CXX op_resolver_bridge.cc     op_resolver_bridge.o
  CXX schema_utils.cc   schema_utils.o
  CXX tflite.cc tflite.o
  CXX tflite_unit_tests.cc      tflite_unit_tests.o
  AS  crt0-vexriscv.S   crt0-vexriscv.o
  LD       software.elf
  OBJDUMP  software.elf.dis
  OBJDUMP  software.elf.sym
  OBJCOPY  software.bin
  IHEX     software.ihex
make[1]: Leaving directory '/home/kasunyah/CFU-mobilenetV2-base/proj/mnv2_cfu_package/build'
Running interactively on FPGA Board
# Load hook allows common_soc.py to provide board-specific changes to load.
make -C /home/kasunyah/CFU-mobilenetV2-base/soc -f /home/kasunyah/CFU-mobilenetV2-base/soc/common_soc.mk load_hook
make[1]: Entering directory '/home/kasunyah/CFU-mobilenetV2-base/soc'
MAKEFLAGS=-j8 /home/kasunyah/CFU-mobilenetV2-base/scripts/pyrun ./common_soc.py --output-dir build/digilent_nexys4ddr.mnv2_cfu_package --csr-json build/digilent_nexys4ddr.mnv2_cfu_package/csr.json --cpu-cfu  /home/kasunyah/CFU-mobilenetV2-base/proj/mnv2_cfu_package/cfu.v --uart-baudrate 115200 --target digilent_nexys4ddr  --software-load --software-path /home/kasunyah/CFU-mobilenetV2-base/proj/mnv2_cfu_package/build/software.bin
make[1]: Leaving directory '/home/kasunyah/CFU-mobilenetV2-base/soc'
/home/kasunyah/CFU-mobilenetV2-base/soc/bin/litex_term --speed 115200  --kernel /home/kasunyah/CFU-mobilenetV2-base/proj/mnv2_cfu_package/build/software.bin /dev/ttyUSB1

        __   _ __      _  __
       / /  (_) /____ | |/_/
      / /__/ / __/ -_)>  <
     /____/_/\__/\__/_/|_|
   Build your hardware, easily!

 (c) Copyright 2012-2022 Enjoy-Digital
 (c) Copyright 2007-2015 M-Labs

 BIOS built on Nov  7 2026 09:56:08
 BIOS CRC passed (b5b95dd3)

 LiteX git sha1: b9a1fec30

--=============== SoC ==================--
CPU:            VexRiscv_FullCfu @ 75MHz
BUS:            WISHBONE 32-bit @ 4GiB
CSR:            32-bit data
ROM:            128KiB
SRAM:           8KiB
L2:             8KiB
SDRAM:          131072KiB 16-bit @ 300MT/s (CL-3 CWL-2)

--========== Initialization ============--
Initializing SDRAM @0x40000000...
Switching SDRAM to software control.
Read leveling:
  m0, b00: |00000000000000000000000000000000| delays: -
  m0, b01: |00000000000000000000000000000000| delays: -
  m0, b02: |11111111111110000000000000000000| delays: 06+-06
  m0, b03: |00000000000000111111111111111111| delays: 22+-09
  m0, b04: |00000000000000000000000000000000| delays: -
  m0, b05: |00000000000000000000000000000000| delays: -
  m0, b06: |00000000000000000000000000000000| delays: -
  m0, b07: |00000000000000000000000000000000| delays: -
  best: m0, b03 delays: 23+-09
  m1, b00: |00000000000000000000000000000000| delays: -
  m1, b01: |00000000000000000000000000000000| delays: -
  m1, b02: |11111111111100000000000000000000| delays: 06+-06
  m1, b03: |00000000000001111111111111111111| delays: 22+-09
  m1, b04: |00000000000000000000000000000000| delays: -
  m1, b05: |00000000000000000000000000000000| delays: -
  m1, b06: |00000000000000000000000000000000| delays: -
  m1, b07: |00000000000000000000000000000000| delays: -
  best: m1, b03 delays: 22+-09
Switching SDRAM to hardware control.
Memtest at 0x40000000 (2.0MiB)...
  Write: 0x40000000-0x40200000 2.0MiB     
   Read: 0x40000000-0x40200000 2.0MiB     
Memtest OK
Memspeed at 0x40000000 (Sequential, 2.0MiB)...
  Write speed: 25.3MiB/s
   Read speed: 34.0MiB/s

--============== Boot ==================--
Booting from serial...
Press Q or ESC to abort boot completely.
sL5DdSMmkekro
[LITEX-TERM] Received firmware download request from the device.
[LITEX-TERM] Uploading /home/kasunyah/CFU-mobilenetV2-base/proj/mnv2_cfu_package/build/software.bin to 0x40000000 (3023960 bytes)...
[LITEX-TERM] Upload calibration... (inter-frame: 10.00us, length: 64)
[LITEX-TERM] Upload complete (9.9KB/s).
[LITEX-TERM] Booting the device.
[LITEX-TERM] Done.
Executing booted program at 0x40000000

--============= Liftoff! ===============--
Hello, World!

CFU Playground
==============
 1: TfLM Models menu
 2: Functional CFU Tests
 3: Project menu
 4: Performance Counter Tests
 5: TFLite Unit Tests
 6: Benchmarks
 7: Util Tests
 8: Embench IoT
main> 1

Running TfLM Models menu

TfLM Models
===========
 1: Person Detection int8 model
 2: Mobile Net v2 models
 x: eXit to previous menu
models> 2

Running Mobile Net v2 models

========================================
 MobileNetV2 a0.35 INT8
 CFU-ACCELERATED VERSION
========================================
Model             : mobilenetv2_a035_224_int8.tflite
Input             : embedded image
Resolution        : 224 x 224 x 3
External input    : UINT8
Internal compute  : INT8
External output   : FLOAT32
Classes           : 1000
Mode              : EXISTING MNV2 CFU
Accelerated op    : eligible 1x1 CONV_2D
========================================

Loading MobileNetV2 model...
Error_reporter OK!
Input: 150528 bytes, 4 dims: 1 224 224 3

Model loaded successfully.

========================================
 Embedded Image Verification
========================================
Header length : 150528 bytes
Expected      : 150528 bytes
Size          : OK
RGB min       : 0
RGB max       : 254
RGB mean      : 132.546715
RGB FNV1a     : 0xbe3b0c0b

First 30 RGB bytes:
173 178 76 173 178 76 173 178 76 174 179 77 174 179 77 174 179 77 174 179 77 174 179 77 174 179 77 174 179 77 

First 10 RGB pixels:
Pixel  0: R=173 G=178 B=76
Pixel  1: R=173 G=178 B=76
Pixel  2: R=173 G=178 B=76
Pixel  3: R=174 G=179 B=77
Pixel  4: R=174 G=179 B=77
Pixel  5: R=174 G=179 B=77
Pixel  6: R=174 G=179 B=77
Pixel  7: R=174 G=179 B=77
Pixel  8: R=174 G=179 B=77
Pixel  9: R=174 G=179 B=77

Input format verified:
  UINT8
  RGB
  224 x 224 x 3
  Raw bytes unchanged
========================================

Loading input image into TFLite...
Input tensor type: 3
Input tensor bytes: 150528
Copied 150528 RAW UINT8 bytes at 0x4031b9a0
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
.......................................................................
"Event","Tag","Ticks"
0,QUANTIZE,796
1,CONV_2D,156475
2,DEPTHWISE_CONV_2D,60469
3,CONV_2D,1411
4,CONV_2D,2536
5,PAD,16440
6,DEPTHWISE_CONV_2D,61537
7,CONV_2D,842
8,CONV_2D,637
9,DEPTHWISE_CONV_2D,91233
10,CONV_2D,847
11,ADD,2812
12,CONV_2D,639
13,PAD,4114
14,DEPTHWISE_CONV_2D,13233
15,CONV_2D,308
16,CONV_2D,389
17,DEPTHWISE_CONV_2D,27871
18,CONV_2D,568
19,ADD,1418
20,CONV_2D,389
21,DEPTHWISE_CONV_2D,27205
22,CONV_2D,567
23,ADD,1414
24,CONV_2D,391
25,PAD,2064
26,DEPTHWISE_CONV_2D,6718
27,CONV_2D,191
28,CONV_2D,213
29,DEPTHWISE_CONV_2D,11443
30,CONV_2D,281
31,ADD,529
32,CONV_2D,214
33,DEPTHWISE_CONV_2D,14490
34,CONV_2D,279
35,ADD,515
36,CONV_2D,217
37,DEPTHWISE_CONV_2D,11092
38,CONV_2D,278
39,ADD,527
40,CONV_2D,215
41,DEPTHWISE_CONV_2D,10082
42,CONV_2D,341
43,CONV_2D,360
44,DEPTHWISE_CONV_2D,18072
45,CONV_2D,445
46,ADD,701
47,CONV_2D,361
48,DEPTHWISE_CONV_2D,19504
49,CONV_2D,445
50,ADD,700
51,CONV_2D,363
52,PAD,1035
53,DEPTHWISE_CONV_2D,4526
54,CONV_2D,227
55,CONV_2D,342
56,DEPTHWISE_CONV_2D,7365
57,CONV_2D,438
58,ADD,318
59,CONV_2D,342
60,DEPTHWISE_CONV_2D,6727
61,CONV_2D,438
62,ADD,303
63,CONV_2D,342
64,DEPTHWISE_CONV_2D,6255
65,CONV_2D,819
66,CONV_2D,2544
67,MEAN,12019
68,FULLY_CONNECTED,16507
69,SOFTMAX,2118
70,DEQUANTIZE,247
Perf counters not enabled.
   654M (    653639586 )  cycles total
3x3 depthwise CFU used

========================================
 MobileNetV2 Classification Result
========================================

Output tensor : FLOAT32
Output size   : 1000 classes

First 20 FLOAT32 outputs:
  output[0] = 0 x 10^-6
  output[1] = 0 x 10^-6
  output[2] = 0 x 10^-6
  output[3] = 0 x 10^-6
  output[4] = 0 x 10^-6
  output[5] = 0 x 10^-6
  output[6] = 0 x 10^-6
  output[7] = 0 x 10^-6
  output[8] = 0 x 10^-6
  output[9] = 0 x 10^-6
  output[10] = 0 x 10^-6
  output[11] = 0 x 10^-6
  output[12] = 0 x 10^-6
  output[13] = 0 x 10^-6
  output[14] = 0 x 10^-6
  output[15] = 0 x 10^-6
  output[16] = 0 x 10^-6
  output[17] = 0 x 10^-6
  output[18] = 0 x 10^-6
  output[19] = 0 x 10^-6

Output statistics:
  Min  = 0 x 10^-6
  Max  = 406250 x 10^-6
  Mean = 781 x 10^-6

Output FNV1a      : 0x2d8f8f61
Top-1 class index : 64
Top-1 score       : 406250 x 10^-6

Prediction class index: 64
Prediction class label: green_mamba
========================================

Inference completed.
---

TfLM Models
===========
 1: Person Detection int8 model
 2: Mobile Net v2 models
 x: eXit to previous menu
models> 