# Model quality: why the printed class was wrong, and how it was fixed

## Short answer
The fused CFU was never the problem: it reproduces the CPU (TFLM) result bit for bit. The problem was the **int8 model**.
The weights inside the supplied int8 file are good (the float network rebuilt from them reaches 67.9% top-1 on held-out
ImageNet photos and answers *green mamba* for the embedded snake image). Standard int8 conversion of this architecture
destroys most of that accuracy; `model/` now holds a re-calibrated model that keeps about three quarters of it.

## Measured (666 held-out ImageNet photos, 1 per class, never used for calibration; TFLite reference kernels = like TFLM)
| model | top-1 | top-5 | images whose #1 is a tie |
|---|---|---|---|
| float network rebuilt from the int8 weights (reference) | 67.9% | 90.1% | |
| original int8 model | 16.5% | 39.3% | 37.8% |
| original + wider logits range (`fix_logits_range.py`) | 20.1% | 40.1% | 3.6% |
| re-converted with the converter's min/max calibration, 334 real photos | 15.3% | 33.6% | 9.0% |
| **percentile-calibrated (`percentile_calibrate.py`, 99.97%) = `model/`** | **51.5%** | **74.9%** | 2.0% |

Under TFLM itself (the code the board runs, 300 of those photos): 57.3% top-1, 76.7% top-5 (about +-5 points at this sample size).
The embedded snake image under TFLM: green_mamba 0.672, green_snake 0.160, African_chameleon 0.027, vine_snake 0.020, ringneck_snake 0.008.
The fused CFU output equals plain TFLM exactly (10/10 blocks, 10,024,685 CFU cycles, unchanged).

Percentile sweep (same photos): 99.9999 -> 17.0%, 99.999 -> 45.8%, 99.99 -> 49.4%, 99.98 -> 50.6%, 99.97 -> 50.9%, 99.95 -> 51.5%,
99.9 -> 16.1% (too much clipping destroys information). Use 99.95-99.99.

## Why standard int8 conversion fails here
* The int8 kernels are accurate (about 1.2% error per operator). What hurts is **error amplification**: the first depthwise layer
  turns a 1.2% input rounding error into 13.6% (79-98% in some channels, where the signal is small and the noise gain is large),
  and the squeeze-and-excite gates carry it forward; by the middle of the network the signal is gone.
* The activations have outliers (|x| up to ~100 with a typical spread of ~6). The converter takes each tensor's min/max as its int8
  range, so the step is far too coarse for the bulk of the values. Clipping at a high percentile gives much finer steps.
* The original model additionally had a too-narrow logits range (clipped at +5.9), which made confident classes tie.

## What `percentile_calibrate.py` does (needs tensorflow, tflite, ai-edge-litert, pillow)
Rebuilds the float network from the int8 weights (undoing the batch-norm folding; the `+3` of the squeeze-and-excite hard-sigmoid
is folded into a bias by the converter and is removed again), converts it to an int8 model with the same structure, runs the
float model over 250 calibration photos, and rewrites every activation range from the chosen percentile, re-deriving each conv
bias for its new input scale. Weights are unchanged; the fused-block plan and the CFU are unaffected (same 10 blocks).
```
tools/get_calibration_images.sh                              # 1000 ImageNet photos (or use your own, 200+ varied)
python3 tools/percentile_calibrate.py --int8 model_original/mobilenetv3_small_full_int8_original.tflite \
        --images calibration_photos/imagenet-sample-images-master --out model/mobilenetv3_small_full_int8.tflite
python3 tools/check_int8_model.py model/mobilenetv3_small_full_int8.tflite --labels tools/imagenet_labels.txt photo.jpg
python3 tools/gen_fused_plan.py model/mobilenetv3_small_full_int8.tflite src/fused_plan.h
```

## Honest limits
* About 51-57% top-1 is clearly better than 16%, but still well below the float network's 68%. Closing the rest needs
  quantisation-aware fine-tuning (training), which was not possible here.
* The percentile was compared on the same held-out photos that are reported, so the best figure may be slightly optimistic.
* Calibration used ImageNet sample photos. For very different images (e.g. a webcam in a dim room) results can differ; calibrate with
  photos like the ones you will classify if possible.
* Different int8 implementations of the same model still differ by a few steps (the vendored TFLM computes the quantised MEAN with
  float math, current TFLite with integer math), so borderline images can flip between close classes. The fused CFU always equals TFLM.
* Not tested here: the new firmware output and this model on a board or in Renode (tested on the PC with the real RTL and TFLM).
