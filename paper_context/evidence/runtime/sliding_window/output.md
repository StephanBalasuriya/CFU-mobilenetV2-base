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
Copied 150528 RAW UINT8 bytes at 0x4031c560
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
.......................................................................
"Event","Tag","Ticks"
0,QUANTIZE,780
1,CONV_2D,156491
2,DEPTHWISE_CONV_2D,43197
3,CONV_2D,1411
4,CONV_2D,2537
5,PAD,16448
6,DEPTHWISE_CONV_2D,74106
7,CONV_2D,842
8,CONV_2D,637
9,DEPTHWISE_CONV_2D,40445
10,CONV_2D,847
11,ADD,2801
12,CONV_2D,638
13,PAD,4122
14,DEPTHWISE_CONV_2D,13607
15,CONV_2D,308
16,CONV_2D,390
17,DEPTHWISE_CONV_2D,20019
18,CONV_2D,568
19,ADD,1419
20,CONV_2D,390
21,DEPTHWISE_CONV_2D,23042
22,CONV_2D,569
23,ADD,1402
24,CONV_2D,391
25,PAD,2063
26,DEPTHWISE_CONV_2D,8428
27,CONV_2D,190
28,CONV_2D,215
29,DEPTHWISE_CONV_2D,9244
30,CONV_2D,280
31,ADD,526
32,CONV_2D,215
33,DEPTHWISE_CONV_2D,8732
34,CONV_2D,279
35,ADD,515
36,CONV_2D,217
37,DEPTHWISE_CONV_2D,8626
38,CONV_2D,279
39,ADD,524
40,CONV_2D,215
41,DEPTHWISE_CONV_2D,9930
42,CONV_2D,342
43,CONV_2D,361
44,DEPTHWISE_CONV_2D,11734
45,CONV_2D,446
46,ADD,713
47,CONV_2D,361
48,DEPTHWISE_CONV_2D,13594
49,CONV_2D,446
50,ADD,697
51,CONV_2D,363
52,PAD,1033
53,DEPTHWISE_CONV_2D,4435
54,CONV_2D,228
55,CONV_2D,342
56,DEPTHWISE_CONV_2D,6841
57,CONV_2D,439
58,ADD,322
59,CONV_2D,341
60,DEPTHWISE_CONV_2D,7331
61,CONV_2D,439
62,ADD,325
63,CONV_2D,342
64,DEPTHWISE_CONV_2D,6222
65,CONV_2D,819
66,CONV_2D,2546
67,MEAN,21806
68,FULLY_CONNECTED,16506
69,SOFTMAX,2125
70,DEQUANTIZE,241
Perf counters not enabled.
   573M (    573258998 )  cycles total
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

