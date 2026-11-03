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
 CPU-ONLY BASELINE
========================================
Model             : mobilenetv2_a035_224_int8.tflite
Input             : embedded image
Resolution        : 224 x 224 x 3
External input    : UINT8
Internal compute  : INT8
External output   : FLOAT32
Classes           : 1000
Mode              : CPU ONLY
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
Copied 150528 RAW UINT8 bytes at 0x403044f0
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
.......................................................................
"Event","Tag","Ticks"
0,QUANTIZE,776
1,CONV_2D,216140
2,DEPTHWISE_CONV_2D,105690
3,CONV_2D,52806
4,CONV_2D,233864
5,PAD,16095
6,DEPTHWISE_CONV_2D,94000
7,CONV_2D,37958
8,CONV_2D,61879
9,DEPTHWISE_CONV_2D,90432
10,CONV_2D,28310
11,ADD,2801
12,CONV_2D,55707
13,PAD,4032
14,DEPTHWISE_CONV_2D,21647
15,CONV_2D,15839
16,CONV_2D,40776
17,DEPTHWISE_CONV_2D,42279
18,CONV_2D,27876
19,ADD,1417
20,CONV_2D,44482
21,DEPTHWISE_CONV_2D,44070
22,CONV_2D,31925
23,ADD,1400
24,CONV_2D,40695
25,PAD,2019
26,DEPTHWISE_CONV_2D,12476
27,CONV_2D,9720
28,CONV_2D,21552
29,DEPTHWISE_CONV_2D,17175
30,CONV_2D,15365
31,ADD,525
32,CONV_2D,19145
33,DEPTHWISE_CONV_2D,16504
34,CONV_2D,16012
35,ADD,515
36,CONV_2D,21145
37,DEPTHWISE_CONV_2D,15064
38,CONV_2D,15620
39,ADD,523
40,CONV_2D,20240
41,DEPTHWISE_CONV_2D,20021
42,CONV_2D,19138
43,CONV_2D,34862
44,DEPTHWISE_CONV_2D,21733
45,CONV_2D,27530
46,ADD,711
47,CONV_2D,33750
48,DEPTHWISE_CONV_2D,23126
49,CONV_2D,26478
50,ADD,695
51,CONV_2D,34978
52,PAD,1004
53,DEPTHWISE_CONV_2D,6450
54,CONV_2D,11564
55,CONV_2D,23947
56,DEPTHWISE_CONV_2D,9269
57,CONV_2D,20969
58,ADD,321
59,CONV_2D,25488
60,DEPTHWISE_CONV_2D,10527
61,CONV_2D,20923
62,ADD,324
63,CONV_2D,25941
64,DEPTHWISE_CONV_2D,8931
65,CONV_2D,41817
66,CONV_2D,170019
67,MEAN,12257
68,FULLY_CONNECTED,16520
69,SOFTMAX,2313
70,DEQUANTIZE,235
Perf counters not enabled.
  2221M (   2220572091 )  cycles total

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

Top-1 class index : 64
Top-1 score       : 406250 x 10^-6

Prediction class index: 64
========================================

Inference completed.
---

TfLM Models
===========
 1: Person Detection int8 model
 2: Mobile Net v2 models
 x: eXit to previous menu
models> 