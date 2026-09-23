# MobileNetV3 Minimalistic Image Classification in CFU-Playground (Renode Simulation)

This guide documents how **CFU-Playground-MNv3-min** (the `proj/mnv2_first` project) was
extended with a full **image classification pipeline** for MobileNetV3-Small Minimalistic,
mirroring the architecture already established for MobileNetV2.

---

## 1. Overview & Architecture

### 1.1 The Firmware Model

The embedded model is `model_mobilenetv3_small_min.tflite` — exported by
`common/src/models/mnv3/generate_mnv3_model.py`:

| Property | Value |
|---|---|
| Architecture | MobileNetV3-Small (`minimalistic=True`) |
| Input Resolution | **160 × 160 × 3** (INT8, zero-point = 128) |
| Width Multiplier `alpha` | 0.35 |
| Output Classes | 2 (binary: `class_0_negative` / `class_1_positive`) |
| Quantization | Full INT8 (`inference_input_type = tf.int8`) |
| SE Modules | ❌ Removed |
| h-swish Activation | ❌ Replaced with ReLU6 |

> [!NOTE]
> The current model is a **2-class binary** model trained without real ImageNet weights (`weights=None`).
> To use it as a 1000-class ImageNet classifier, see **Section 6: Training / Replacing the Model**.

### 1.2 Key Differences from MobileNetV2

| Aspect | MobileNetV2 | MobileNetV3-Min |
|---|---|---|
| Input size | 224 × 224 | **160 × 160** |
| Input dtype | UINT8 (`uint8_t`) | **INT8 (`int8_t`)** |
| Zero-point shift | none needed | **subtract 128** from each pixel |
| Output dtype | UINT8 softmax | **INT8 logits** |
| Output classes | 1001 (ImageNet) | 2 (binary, default) |
| Tensor arena | 4 MB | 800 KB |
| CFU acceleration | 1x1 Conv (SIMD4) | 1x1 Conv (SIMD4) — **same CFU** |

---

## 2. Image Ingestion Pipeline (`images/` Directory)

Renode simulates bare-metal RISC-V firmware (`software.bin` on VexRiscv).
There is no filesystem in the simulated SoC, so images must be pre-processed and
compiled as C byte arrays before building the firmware.

### 2.1 Directory Structure

```
CFU-Playground-MNv3-min/
├── images/                                  # Drop your test images here
│   ├── cat.jpg
│   ├── dog.jpg
│   └── test_sample.jpg
├── scripts/
│   └── process_all_images_mnv3.py           # ← MNv3 preprocessing script
└── common/src/models/mnv3/
    ├── image_inputs_mnv3.h                  # Auto-generated INT8 C database
    ├── labels_mnv3.h                        # Class label helpers
    ├── model_mobilenetv3_small_min.h        # TFLite flatbuffer C array
    ├── mnv3.cc                              # Firmware inference & menu handler
    └── mnv3.h
```

### 2.2 Adding Any Image

1. Copy your image file (`.jpg`, `.jpeg`, `.png`, `.bmp`) into `images/`:
   ```bash
   cp /path/to/my_image.jpg \
       ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/images/
   ```
2. Run the MNv3 preprocessing script to regenerate `image_inputs_mnv3.h`:
   ```bash
   /home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python \
       CFU-Playground-MNv3-min/scripts/process_all_images_mnv3.py
   ```

### 2.3 What `process_all_images_mnv3.py` Does

- Scans `images/` for all valid image files.
- Resizes each image to **160 × 160** with RGB channels using LANCZOS.
- Applies INT8 zero-point shift: `int8_val = uint8_val - 128` to match the quantized model.
- Writes `common/src/models/mnv3/image_inputs_mnv3.h`, which contains:
  - `mnv3_img_<filename>[]`: INT8 pixel array per image (76,800 bytes each).
  - `struct ImageSampleMnv3 ALL_IMAGES_MNV3[]`: table of filename + pointer + size.
  - `NUM_IMAGES_MNV3`: total image count used by the firmware loop.

---

## 3. Firmware & Memory Configuration

### 3.1 Tensor Arena Size in `common/src/tflite.cc`

```cpp
#ifdef INCLUDE_MODEL_MNV3
    800 * 1024,   // 800 KB for MNv3-Small-Min 160x160
#endif
```

MNv3 at 160 × 160 with `alpha=0.35` has a peak activation footprint of ~600 KB,
so the 800 KB arena provides ample headroom. The Renode LiteX SoC provides **256 MB RAM**.

### 3.2 Label Helpers in `common/src/models/mnv3/labels_mnv3.h`

```c
#define MNV3_NUM_CLASSES 2

static const char* const MNV3_LABELS[MNV3_NUM_CLASSES] = {
    "class_0_negative",
    "class_1_positive",
};

static inline const char* mnv3_get_label(int class_id) { ... }
```

When you retrain with more classes, update `MNV3_NUM_CLASSES` and `MNV3_LABELS[]` here.

### 3.3 Inference Engine in `common/src/models/mnv3/mnv3.cc`

When inference runs:
1. `tflite_set_input_unsigned(sample->data)` loads the 160 × 160 × 3 INT8 byte array.
2. `tflite_classify()` invokes the model on VexRiscv with optional CFU acceleration.
3. `find_top_k_mnv3()` uses insertion sort to find the **Top-K output logits** (no heap).
4. Results are printed ranked with confidence % computed from the INT8 logit value.
5. If `CSR_VIDEO_FRAMEBUFFER_BASE` is set, the image is rendered in the Renode GUI window.

---

## 4. Step-by-Step: Build and Run in Renode

### Step 1: Activate the Conda Toolchain Environment

```bash
source ~/cfu-playground-fork/CFU-Playground/env/conda/bin/activate cfu-common
```

### Step 2: Ingest Images from `images/`

```bash
cd ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min
python scripts/process_all_images_mnv3.py
```

Output confirms:
```
Found 3 image(s): ['cat.jpg', 'dog.jpg', 'test_sample.jpg']
  Processed 'cat.jpg': 76800 bytes → mnv3_img_cat
  ...
Successfully generated: common/src/models/mnv3/image_inputs_mnv3.h
```

### Step 3: Navigate to the Target Project

```bash
cd ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/proj/mnv2_first
```

### Step 4: Clean and Build Firmware

```bash
make clean
make software -j$(nproc)
make renode-scripts
```

### Step 5: Launch Renode Simulation

- **Interactive GUI mode** (opens Renode window + UART analyzer):
  ```bash
  make renode
  ```
- **Headless mode** (UART output in current terminal):
  ```bash
  make renode-headless
  ```

> [!IMPORTANT]
> If you add new images after building, re-run Step 2, then **`make clean && make renode`**
> to embed the updated `image_inputs_mnv3.h` into the firmware.

---

## 5. Renode UART Menu Interaction & Expected Output

### Navigating the Menu

```text
CFU Playground
==============
 1: TfLM Models menu
 2: Functional CFU Tests
 3: Project menu
 ...
main> 1
```

Select `1` to enter TfLM Models, then select **MobileNetV3 Minimalistic models**:

```text
TfLM Models
===========
 1: Person Detection int8 model
 2: Mobile Net v2 models
 3: MobileNetV3 Minimalistic models
models> 3
```

You are now in the MNv3 menu:

```text
MobileNetV3 Minimalistic Models
================================
 i: Classify ALL images in images/ folder
 1: Classify first image
 g: Run golden test input (input_00001)
 z: Run zeros input test
mnv3>
```

### Prompt for CFU Acceleration

```text
==================================================
Disable CFU acceleration? (y/n) [n]: n
--> CFU ENABLED: Running model inside CFU.
==================================================
```

### Sample Output for `cat.jpg`

```text
Loading image: cat.jpg (76800 bytes)...
Running MobileNetV3 Minimalistic (CFU accelerated) on: cat.jpg

=================================================================
           CLASSIFICATION RESULTS: cat.jpg
=================================================================
 Rank #1: class_1_positive               [Class    1] ->  72% (logit:   55)
 Rank #2: class_0_negative               [Class    0] ->  28% (logit:  -56)
=================================================================
>>> IDENTIFIED: class_1_positive (72% confidence) <<<
```

> [!NOTE]
> Confidence values reflect the current **binary model** (2 classes). After replacing the
> model with a 1000-class ImageNet MNv3, predictions will show breed/object names.

### Sample Output for Golden Test Input

```text
mnv3> g
==================================================
Disable CFU acceleration? (y/n) [n]: n
--> CFU ENABLED: Running model inside CFU.
==================================================
Running MobileNetV3 Minimalistic (CFU accelerated) on: golden_input_00001

=================================================================
           CLASSIFICATION RESULTS: golden_input_00001
=================================================================
 Rank #1: class_0_negative               [Class    0] ->  51% (logit:    6)
 Rank #2: class_1_positive               [Class    1] ->  49% (logit:   -7)
=================================================================
>>> IDENTIFIED: class_0_negative (51% confidence) <<<
```

---

## 6. Training / Replacing the Model (Optional)

To use a full **1000-class ImageNet** MNv3 model in firmware:

### Step A: Export an ImageNet INT8 MNv3 Model

Use the standalone exporter at `standalone_mobilenetv3_min/export_model.py`:

```bash
cd standalone_mobilenetv3_min
python export_model.py --variant small --quantize \
    --output ../CFU-Playground-MNv3-min/common/src/models/mnv3/model_mobilenetv3_small_min.tflite
```

> [!WARNING]
> The exported model will use **224 × 224 input** and **1000 output classes**.
> You must update `generate_mnv3_model.py` `INPUT_SHAPE` and `NUM_CLASSES`, rerun
> `process_all_images_mnv3.py` with `TARGET_SIZE = (224, 224)`, and expand `labels_mnv3.h`
> with all 1000 ImageNet labels. Tensor arena may need to grow beyond 800 KB.

### Step B: Convert `.tflite` to C Header

```bash
python CFU-Playground-MNv3-min/scripts/xxd.py \
    common/src/models/mnv3/model_mobilenetv3_small_min.tflite \
    common/src/models/mnv3/model_mobilenetv3_small_min.h
```

### Step C: Update Labels

Edit `common/src/models/mnv3/labels_mnv3.h`:
```c
#define MNV3_NUM_CLASSES 1000
static const char* const MNV3_LABELS[MNV3_NUM_CLASSES] = {
    "tench", "goldfish", "great white shark", /* ... all 1000 ImageNet labels ... */
};
```

You can copy-adapt from `common/src/models/mnv2/labels.h` (which already has 1001 labels).

### Step D: Update Image Preprocessing

In `scripts/process_all_images_mnv3.py`, change:
```python
TARGET_SIZE = (224, 224)  # match new model input
```

Then re-run `python scripts/process_all_images_mnv3.py` and `make clean && make renode`.

---

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `AllocateTensors() failed` | Tensor arena too small | Increase `800 * 1024` in [`tflite.cc:97`](file:///home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/common/src/tflite.cc#L97) |
| `No images available` in menu | `image_inputs_mnv3.h` not generated | Run `python scripts/process_all_images_mnv3.py` |
| Images added but not shown | Old `.h` cached in build | `make clean && make renode` |
| `Unsupported Op: HARD_SWISH` | Model exported without `minimalistic=True` | Re-export with `minimalistic=True` |
| 1x1 Conv not accelerated | Channel depth not divisible by 8 | Use `alpha=0.35` or `alpha=1.0` |
| Confidence always ~50% | Binary model, random weights (`weights=None`) | Replace with pretrained ImageNet model |

---

## 8. New Files Added by This Implementation

| File | Description |
|---|---|
| [`scripts/process_all_images_mnv3.py`](file:///home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/scripts/process_all_images_mnv3.py) | Image preprocessor — resizes to 160×160, INT8 zero-point shift |
| [`common/src/models/mnv3/image_inputs_mnv3.h`](file:///home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/common/src/models/mnv3/image_inputs_mnv3.h) | Auto-generated INT8 image database (3 images, 76800 bytes each) |
| [`common/src/models/mnv3/labels_mnv3.h`](file:///home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/common/src/models/mnv3/labels_mnv3.h) | Class label helper — mirrors `mnv2/labels.h` pattern |
| [`common/src/models/mnv3/mnv3.cc`](file:///home/victus_linux/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/common/src/models/mnv3/mnv3.cc) | Updated firmware — adds image DB menu (`i`, `1`), Top-K, labels |
