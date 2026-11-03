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
Copied 150528 RAW UINT8 bytes at 0x4031cc20
Input image loaded successfully.

Running MobileNetV2 inference...
----------------------------------------
...DW3X3 profile: operand_fetch_load_shift=16892555 run_get_result=4069255 output_store_postprocess=27931703 software_border=1971878 total=70782654
....DW3X3 profile: operand_fetch_load_shift=44728254 run_get_result=3010681 output_store_postprocess=30813608 software_border=0 total=96378340
...DW3X3 profile: operand_fetch_load_shift=19460050 run_get_result=2939796 output_store_postprocess=25259997 software_border=3253188 total=65968650
.....DW3X3 profile: operand_fetch_load_shift=8697421 run_get_result=752689 output_store_postprocess=6050033 software_border=0 total=20313854
...DW3X3 profile: operand_fetch_load_shift=7846052 run_get_result=1361996 output_store_postprocess=10630909 software_border=3113264 total=30321571
....DW3X3 profile: operand_fetch_load_shift=7854185 run_get_result=1361923 output_store_postprocess=10574429 software_border=2911548 total=30068243
.....DW3X3 profile: operand_fetch_load_shift=4400892 run_get_result=376430 output_store_postprocess=2425195 software_border=0 total=9435313
...DW3X3 profile: operand_fetch_load_shift=3040790 run_get_result=434329 output_store_postprocess=4212889 software_border=2279367 total=12786802
....DW3X3 profile: operand_fetch_load_shift=3605019 run_get_result=434377 output_store_postprocess=4155380 software_border=2504246 total=13584633
....DW3X3 profile: operand_fetch_load_shift=3037623 run_get_result=434363 output_store_postprocess=5299328 software_border=2144320 total=13893743
....DW3X3 profile: operand_fetch_load_shift=3066424 run_get_result=434364 output_store_postprocess=4001471 software_border=2243306 total=12562369
...DW3X3 profile: operand_fetch_load_shift=4011883 run_get_result=578996 output_store_postprocess=6693142 software_border=2899382 total=17981431
....DW3X3 profile: operand_fetch_load_shift=3988422 run_get_result=579058 output_store_postprocess=7043778 software_border=2786477 total=18322136
.....DW3X3 profile: operand_fetch_load_shift=2166780 run_get_result=188209 output_store_postprocess=1498243 software_border=0 total=4999898
...DW3X3 profile: operand_fetch_load_shift=2061750 run_get_result=174965 output_store_postprocess=2801467 software_border=2352979 total=9099526
....DW3X3 profile: operand_fetch_load_shift=2158586 run_get_result=174965 output_store_postprocess=2720644 software_border=2501795 total=9211993
....DW3X3 profile: operand_fetch_load_shift=2512524 run_get_result=174965 output_store_postprocess=2677520 software_border=3014544 total=10102809
......
"Event","Tag","Ticks"
0,QUANTIZE,777
1,CONV_2D,156246
2,DEPTHWISE_CONV_2D,69185
3,CONV_2D,1448
4,CONV_2D,2537
5,PAD,16446
6,DEPTHWISE_CONV_2D,94175
7,CONV_2D,879
8,CONV_2D,637
9,DEPTHWISE_CONV_2D,64485
10,CONV_2D,885
11,ADD,2802
12,CONV_2D,638
13,PAD,4116
14,DEPTHWISE_CONV_2D,19890
15,CONV_2D,322
16,CONV_2D,407
17,DEPTHWISE_CONV_2D,29674
18,CONV_2D,590
19,ADD,1424
20,CONV_2D,389
21,DEPTHWISE_CONV_2D,29425
22,CONV_2D,591
23,ADD,1412
24,CONV_2D,392
25,PAD,2066
26,DEPTHWISE_CONV_2D,9266
27,CONV_2D,200
28,CONV_2D,221
29,DEPTHWISE_CONV_2D,12547
30,CONV_2D,289
31,ADD,539
32,CONV_2D,216
33,DEPTHWISE_CONV_2D,13324
34,CONV_2D,286
35,ADD,542
36,CONV_2D,217
37,DEPTHWISE_CONV_2D,13626
38,CONV_2D,287
39,ADD,537
40,CONV_2D,215
41,DEPTHWISE_CONV_2D,12326
42,CONV_2D,348
43,CONV_2D,368
44,DEPTHWISE_CONV_2D,17620
45,CONV_2D,456
46,ADD,714
47,CONV_2D,361
48,DEPTHWISE_CONV_2D,17950
49,CONV_2D,456
50,ADD,720
51,CONV_2D,363
52,PAD,1039
53,DEPTHWISE_CONV_2D,4933
54,CONV_2D,237
55,CONV_2D,354
56,DEPTHWISE_CONV_2D,8943
57,CONV_2D,460
58,ADD,318
59,CONV_2D,340
60,DEPTHWISE_CONV_2D,9052
61,CONV_2D,460
62,ADD,318
63,CONV_2D,343
64,DEPTHWISE_CONV_2D,9924
65,CONV_2D,855
66,CONV_2D,2545
67,MEAN,12143
68,FULLY_CONNECTED,17276
69,SOFTMAX,2204
70,DEQUANTIZE,240
Perf counters not enabled.
   694M (    694302831 )  cycles total
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