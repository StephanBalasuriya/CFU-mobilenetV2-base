
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
Copied 150528 RAW UINT8 bytes at 0x4031c930
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
...DW3X3 layer 0 in=112x112x16 out=112x112 stride=1 windows=193600 cfg=1 load=5280 shift=191840 run=193600 get=193600 old_load=580800 exp_load=5280 exp_shift=191840 fnv=0x008bd69b
....DW3X3 layer 1 in=113x113x48 out=56x56 stride=2 windows=150528 cfg=1 load=451584 shift=0 run=150528 get=150528 old_load=451584 exp_load=451584 exp_shift=0 fnv=0xe080f1b0
...DW3X3 layer 2 in=56x56x48 out=56x56 stride=1 windows=139968 cfg=1 load=7776 shift=137376 run=139968 get=139968 old_load=419904 exp_load=7776 exp_shift=137376 fnv=0xf0c14aba
.....DW3X3 layer 3 in=57x57x48 out=28x28 stride=2 windows=37632 cfg=1 load=112896 shift=0 run=37632 get=37632 old_load=112896 exp_load=112896 exp_shift=0 fnv=0xa20b5937
...DW3X3 layer 4 in=28x28x96 out=28x28 stride=1 windows=64896 cfg=1 load=7488 shift=62400 run=64896 get=64896 old_load=194688 exp_load=7488 exp_shift=62400 fnv=0xbd76c1d7
....DW3X3 layer 5 in=28x28x96 out=28x28 stride=1 windows=64896 cfg=1 load=7488 shift=62400 run=64896 get=64896 old_load=194688 exp_load=7488 exp_shift=62400 fnv=0xa01a13b5
.....DW3X3 layer 6 in=29x29x96 out=14x14 stride=2 windows=18816 cfg=1 load=56448 shift=0 run=18816 get=18816 old_load=56448 exp_load=56448 exp_shift=0 fnv=0x9c186f04
...DW3X3 layer 7 in=14x14x144 out=14x14 stride=1 windows=20736 cfg=1 load=5184 shift=19008 run=20736 get=20736 old_load=62208 exp_load=5184 exp_shift=19008 fnv=0x8d9dc085
....DW3X3 layer 8 in=14x14x144 out=14x14 stride=1 windows=20736 cfg=1 load=5184 shift=19008 run=20736 get=20736 old_load=62208 exp_load=5184 exp_shift=19008 fnv=0xcf02c24b
....DW3X3 layer 9 in=14x14x144 out=14x14 stride=1 windows=20736 cfg=1 load=5184 shift=19008 run=20736 get=20736 old_load=62208 exp_load=5184 exp_shift=19008 fnv=0xf1a7bc5a
....DW3X3 layer 10 in=14x14x144 out=14x14 stride=1 windows=20736 cfg=1 load=5184 shift=19008 run=20736 get=20736 old_load=62208 exp_load=5184 exp_shift=19008 fnv=0xa4bc1556
...DW3X3 layer 11 in=14x14x192 out=14x14 stride=1 windows=27648 cfg=1 load=6912 shift=25344 run=27648 get=27648 old_load=82944 exp_load=6912 exp_shift=25344 fnv=0x66c8e113
....DW3X3 layer 12 in=14x14x192 out=14x14 stride=1 windows=27648 cfg=1 load=6912 shift=25344 run=27648 get=27648 old_load=82944 exp_load=6912 exp_shift=25344 fnv=0x78b8cfae
.....DW3X3 layer 13 in=15x15x192 out=7x7 stride=2 windows=9408 cfg=1 load=28224 shift=0 run=9408 get=9408 old_load=28224 exp_load=28224 exp_shift=0 fnv=0xd4d06b09
...DW3X3 layer 14 in=7x7x336 out=7x7 stride=1 windows=8400 cfg=1 load=5040 shift=6720 run=8400 get=8400 old_load=25200 exp_load=5040 exp_shift=6720 fnv=0xb1349046
....DW3X3 layer 15 in=7x7x336 out=7x7 stride=1 windows=8400 cfg=1 load=5040 shift=6720 run=8400 get=8400 old_load=25200 exp_load=5040 exp_shift=6720 fnv=0x3a0a16c0
....DW3X3 layer 16 in=7x7x336 out=7x7 stride=1 windows=8400 cfg=1 load=5040 shift=6720 run=8400 get=8400 old_load=25200 exp_load=5040 exp_shift=6720 fnv=0x8d0a215c
......
"Event","Tag","Ticks"
0,QUANTIZE,781
1,CONV_2D,156641
2,DEPTHWISE_CONV_2D,56837
3,CONV_2D,1431
4,CONV_2D,2536
5,PAD,16447
6,DEPTHWISE_CONV_2D,77221
7,CONV_2D,869
8,CONV_2D,636
9,DEPTHWISE_CONV_2D,54535
10,CONV_2D,870
11,ADD,2805
12,CONV_2D,638
13,PAD,4113
14,DEPTHWISE_CONV_2D,16162
15,CONV_2D,317
16,CONV_2D,400
17,DEPTHWISE_CONV_2D,25035
18,CONV_2D,582
19,ADD,1433
20,CONV_2D,390
21,DEPTHWISE_CONV_2D,29379
22,CONV_2D,582
23,ADD,1415
24,CONV_2D,391
25,PAD,2069
26,DEPTHWISE_CONV_2D,8440
27,CONV_2D,196
28,CONV_2D,217
29,DEPTHWISE_CONV_2D,11627
30,CONV_2D,281
31,ADD,571
32,CONV_2D,216
33,DEPTHWISE_CONV_2D,11471
34,CONV_2D,282
35,ADD,562
36,CONV_2D,218
37,DEPTHWISE_CONV_2D,11562
38,CONV_2D,282
39,ADD,568
40,CONV_2D,215
41,DEPTHWISE_CONV_2D,11603
42,CONV_2D,343
43,CONV_2D,363
44,DEPTHWISE_CONV_2D,15195
45,CONV_2D,451
46,ADD,724
47,CONV_2D,361
48,DEPTHWISE_CONV_2D,14156
49,CONV_2D,451
50,ADD,731
51,CONV_2D,363
52,PAD,1032
53,DEPTHWISE_CONV_2D,4671
54,CONV_2D,233
55,CONV_2D,348
56,DEPTHWISE_CONV_2D,7502
57,CONV_2D,451
58,ADD,331
59,CONV_2D,343
60,DEPTHWISE_CONV_2D,8363
61,CONV_2D,449
62,ADD,322
63,CONV_2D,346
64,DEPTHWISE_CONV_2D,8469
65,CONV_2D,837
66,CONV_2D,2542
67,MEAN,12100
68,FULLY_CONNECTED,17266
69,SOFTMAX,2324
70,DEQUANTIZE,244
Perf counters not enabled.
   629M (    629137927 )  cycles total
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