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
Copied 150528 RAW UINT8 bytes at 0x4031bcf0
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
...DW3X3 profile: operand_fetch_load_shift=35736672 run_get_result=3872050 output_store_postprocess=25384154 software_border=1587144 total=89855504
....DW3X3 profile: operand_fetch_load_shift=44713366 run_get_result=3010610 output_store_postprocess=31140652 software_border=0 total=96975625
...DW3X3 profile: operand_fetch_load_shift=31543157 run_get_result=2799410 output_store_postprocess=26607436 software_border=2435747 total=83894724
.....DW3X3 profile: operand_fetch_load_shift=8708585 run_get_result=752690 output_store_postprocess=5743325 software_border=0 total=19890929
...DW3X3 profile: operand_fetch_load_shift=15468477 run_get_result=1297970 output_store_postprocess=11153056 software_border=2614298 total=39216794
....DW3X3 profile: operand_fetch_load_shift=15078114 run_get_result=1297970 output_store_postprocess=10155533 software_border=2345466 total=37541062
.....DW3X3 profile: operand_fetch_load_shift=4327964 run_get_result=376370 output_store_postprocess=2627764 software_border=0 total=9652484
...DW3X3 profile: operand_fetch_load_shift=4708645 run_get_result=414770 output_store_postprocess=4529067 software_border=1735468 total=14522220
....DW3X3 profile: operand_fetch_load_shift=5945962 run_get_result=414770 output_store_postprocess=4995025 software_border=2036771 total=17149463
....DW3X3 profile: operand_fetch_load_shift=6009110 run_get_result=414770 output_store_postprocess=4486386 software_border=1881192 total=16698555
....DW3X3 profile: operand_fetch_load_shift=4638192 run_get_result=414770 output_store_postprocess=3956371 software_border=1747063 total=13894187
...DW3X3 profile: operand_fetch_load_shift=9359970 run_get_result=553010 output_store_postprocess=7435142 software_border=2728474 total=25736744
....DW3X3 profile: operand_fetch_load_shift=6036252 run_get_result=553010 output_store_postprocess=6872696 software_border=2142969 total=20082142
.....DW3X3 profile: operand_fetch_load_shift=1972024 run_get_result=188213 output_store_postprocess=1682858 software_border=0 total=5050128
...DW3X3 profile: operand_fetch_load_shift=2136188 run_get_result=168050 output_store_postprocess=2727183 software_border=2147279 total=9306530
....DW3X3 profile: operand_fetch_load_shift=2022091 run_get_result=168050 output_store_postprocess=2719584 software_border=2104438 total=8755911
....DW3X3 profile: operand_fetch_load_shift=2460692 run_get_result=168050 output_store_postprocess=2805525 software_border=2285818 total=9662153
......
"Event","Tag","Ticks"
0,QUANTIZE,775
1,CONV_2D,158835
2,DEPTHWISE_CONV_2D,87794
3,CONV_2D,1441
4,CONV_2D,2534
5,PAD,16094
6,DEPTHWISE_CONV_2D,94745
7,CONV_2D,874
8,CONV_2D,636
9,DEPTHWISE_CONV_2D,81976
10,CONV_2D,879
11,ADD,2803
12,CONV_2D,638
13,PAD,4032
14,DEPTHWISE_CONV_2D,19465
15,CONV_2D,320
16,CONV_2D,406
17,DEPTHWISE_CONV_2D,38343
18,CONV_2D,586
19,ADD,1424
20,CONV_2D,390
21,DEPTHWISE_CONV_2D,36707
22,CONV_2D,586
23,ADD,1412
24,CONV_2D,392
25,PAD,2019
26,DEPTHWISE_CONV_2D,9467
27,CONV_2D,196
28,CONV_2D,221
29,DEPTHWISE_CONV_2D,14227
30,CONV_2D,284
31,ADD,538
32,CONV_2D,216
33,DEPTHWISE_CONV_2D,16792
34,CONV_2D,282
35,ADD,528
36,CONV_2D,217
37,DEPTHWISE_CONV_2D,16350
38,CONV_2D,282
39,ADD,536
40,CONV_2D,216
41,DEPTHWISE_CONV_2D,13613
42,CONV_2D,344
43,CONV_2D,365
44,DEPTHWISE_CONV_2D,25177
45,CONV_2D,454
46,ADD,721
47,CONV_2D,361
48,DEPTHWISE_CONV_2D,19655
49,CONV_2D,454
50,ADD,719
51,CONV_2D,363
52,PAD,1014
53,DEPTHWISE_CONV_2D,4971
54,CONV_2D,235
55,CONV_2D,348
56,DEPTHWISE_CONV_2D,9131
57,CONV_2D,452
58,ADD,326
59,CONV_2D,341
60,DEPTHWISE_CONV_2D,8593
61,CONV_2D,452
62,ADD,333
63,CONV_2D,343
64,DEPTHWISE_CONV_2D,9479
65,CONV_2D,843
66,CONV_2D,2544
67,MEAN,12071
68,FULLY_CONNECTED,20304
69,SOFTMAX,2208
70,DEQUANTIZE,276
Perf counters not enabled.
   771M (    771235854 )  cycles total
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