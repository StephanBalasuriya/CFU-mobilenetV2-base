# MobileNetV2 Image Classification in CFU-Playground (Renode Simulation)

This guide documents how **CFU-Playground-MNv3-min** was converted from a 2-class binary model into a general-purpose **ImageNet 1000-class Image Classifier** capable of recognizing **any image** placed in the `images/` directory and running inference directly inside the **Renode** RISC-V simulation environment.

---

## 1. Overview & Architecture

### 1.1 The Limitation of the Original Baseline Model
The default MobileNetV2 implementation in CFU-Playground used `model_mobilenetv2_160_035.h`:
- **Input Resolution**: $160 \times 160 \times 3$ (INT8)
- **Output Classes**: **Only 2 logits** (`output[1] - output[0]`) designed solely for binary wake-word or person detection.
- **Limitation**: It could not identify real-world categories (such as cats, dogs, cars, instruments, or any everyday objects).

### 1.2 The General Multi-Class Model
To classify arbitrary images, the project uses `model_mobilenetv2_1000_classes.tflite` (compiled into `common/src/models/mnv2/model_mobilenetv2_1000_classes.h`):
- **Architecture**: MobileNetV2 trained on ImageNet-1k.
- **Input Resolution**: $224 \times 224 \times 3$ (UINT8, 150,528 bytes per image, zero-point = 128, scale = 0.0078125).
- **Output Classes**: **1001 classes** (1 background + 1000 ImageNet categories, UINT8 softmax probabilities).
- **Recognition Capability**: Any image matching ImageNet categories (120+ dog breeds, domestic and wild cats, vehicles, household items, food, sports equipment, electronics, wildlife, etc.).

---

## 2. Image Ingestion Pipeline (`images/` Directory)

Renode simulates bare-metal RISC-V firmware (`software.bin` running on LiteX VexRiscv). Because there is no underlying Linux OS or filesystem inside the simulated SoC to open `.jpg` files at runtime, images placed in `images/` must be preprocessed and converted into C byte arrays.

### 2.1 Directory Structure
```
CFU-Playground-MNv3-min/
├── images/                             # Place your test images here (.jpg, .png)
│   ├── cat.jpg
│   ├── dog.jpg
│   └── test_sample.jpg
├── scripts/
│   └── process_all_images.py           # Preprocessing script
└── common/src/models/mnv2/
    ├── image_inputs.h                  # Auto-generated C database header
    ├── labels.h                        # 1001 ImageNet class labels & helpers
    ├── model_mobilenetv2_1000_classes.h # 1000-class model flatbuffer C array
    └── mnv2.cc                         # Firmware inference & menu handler
```

### 2.2 Adding Any Image
To classify any new image:
1. Save the image file (`.jpg`, `.jpeg`, `.png`, or `.bmp`) directly into `images/` (e.g. `images/airplane.jpg`, `images/banana.jpg`, `images/sports_car.jpg`).
2. Run the image preprocessing script:
   ```bash
   /home/victus_linux/cfu-playground-fork/CFU-Playground/env/conda/envs/cfu-common/bin/python CFU-Playground-MNv3-min/scripts/process_all_images.py
   ```

### 2.3 What `process_all_images.py` Does
- Scans `images/` for all valid image files.
- Resizes each image to $224 \times 224$ with RGB channels.
- Extracts raw `uint8` pixel arrays (150,528 bytes each).
- Automatically writes `common/src/models/mnv2/image_inputs.h`, populating:
  - `img_data_<filename>[]`: Array of pixel bytes for each image.
  - `struct ImageSample ALL_IMAGES[]`: Table containing filename, pointer, and size.
  - `NUM_IMAGES`: Total number of images registered.

---

## 3. Firmware & Memory Configuration

### 3.1 Tensor Arena Size in `common/src/tflite.cc`
Full $224 \times 224$ MobileNetV2 requires more activation memory than the original 800 KB arena:
```cpp
#ifdef INCLUDE_MODEL_MNV2
    4 * 1024 * 1024,   // 4 MB Tensor Arena
#endif
```
In Renode, the Digilent Arty SoC platform provides **256 MB of main RAM** (`0x40000000` to `0x50000000`), so the 4 MB tensor arena fits with ample headroom.

### 3.2 Label Helpers in `common/src/models/mnv2/labels.h`
`labels.h` contains the complete list of 1001 ImageNet labels (`MNV2_LABELS`) and general helper functions:
```c
static inline const char* mnv2_get_label(int class_id) {
  if (class_id >= 0 && class_id < MNV2_NUM_CLASSES) {
    return MNV2_LABELS[class_id];
  }
  return "unknown";
}

static inline bool mnv2_is_valid_class(int class_id) {
  return (class_id >= 0 && class_id < MNV2_NUM_CLASSES);
}
```

### 3.3 Inference & Top-5 Scoring Engine in `common/src/models/mnv2/mnv2.cc`
When inference is run:
1. `tflite_set_input(sample->data)` loads the $224 \times 224 \times 3$ pixel bytes into the TFLM input tensor.
2. `tflite_classify()` invokes the model on VexRiscv (with optional CFU acceleration).
3. `find_top_k()` uses an in-place insertion sort to identify the **Top-5 predicted classes** and their confidence scores.
4. The system prints a ranked breakdown of predictions and announces the recognized object.
5. If the video framebuffer is enabled (`CSR_VIDEO_FRAMEBUFFER_BASE`), the image is rendered onto the Renode GUI window.

---

## 4. Step-by-Step Guide: Build and Run in Renode

### Step 1: Activate the Conda Toolchain Environment
```bash
source ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/env/conda/bin/activate cfu-common
```

### Step 2: Ingest Images from `images/`
```bash
cd ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min
python scripts/process_all_images.py
```
*(Uses the pre-configured Python environment with PIL and NumPy).*

### Step 3: Navigate to the Target Project
```bash
cd ~/cfu-playground-fork/CFU-mobilenetV2-base/CFU-Playground-MNv3-min/proj/mnv2_first
```

### Step 4: Build the Firmware and Renode Scripts
```bash
make software -j
make renode-scripts
```

### Step 5: Launch Renode Simulation
- **Interactive GUI Mode** (opens Renode GUI and UART analyzer):
  ```bash
  make renode
  ```
- **Headless Mode** (runs directly inside the current terminal):
  ```bash
  make renode-headless
  ```

---

## 5. Renode UART Menu Interaction & Expected Output

### Navigating the Menu
Once Renode boots, you will see the CFU Playground top-level menu in the UART terminal:
```text
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
```

Select `1` to enter the TfLM Models menu, then select `Mobile Net v2 models`:
```text
TfLM Models
===========
 1: Person Detection int8 model
 ...
 4: Mobile Net v2 models
models> 4
```

You are now in the MobileNetV2 1000-class image classification menu:
```text
Tests for MobileNetV2 1000-class Model
======================================
 a: Classify ALL images in images/ folder
 1: Classify first image
 z: Run with zeros input
mnv2> a
```

### Prompt for CFU Acceleration
The system prompts whether to run with CFU acceleration or pure CPU:
```text
==================================================
Disable CFU acceleration? (y/n) [n]: n
--> CFU ENABLED: Running model inside CFU.
==================================================
```

### Sample Output for `cat.jpg`
```text
Loading image: cat.jpg (150528 bytes)...
Running MobileNetV2 inference (CFU accelerated)...

=================================================================
           CLASSIFICATION RESULTS: cat.jpg
=================================================================
 Rank #1: tabby                            [Class  282] ->  68% (raw: 173/255)
 Rank #2: Egyptian cat                     [Class  286] ->  13% (raw:  32/255)
 Rank #3: tiger cat                        [Class  283] ->  10% (raw:  26/255)
 Rank #4: lynx                             [Class  288] ->   1% (raw:   3/255)
 Rank #5: electric ray                     [Class  436] ->   1% (raw:   3/255)
=================================================================
>>> IDENTIFIED OBJECT: tabby (68% confidence) <<<
```

### Sample Output for `dog.jpg`
```text
Loading image: dog.jpg (150528 bytes)...
Running MobileNetV2 inference (CFU accelerated)...

=================================================================
           CLASSIFICATION RESULTS: dog.jpg
=================================================================
 Rank #1: miniature schnauzer              [Class  208] ->  93% (raw: 237/255)
 Rank #2: giant schnauzer                  [Class  209] ->   2% (raw:   4/255)
 Rank #3: Lhasa                            [Class  216] ->   1% (raw:   2/255)
 Rank #4: tennis ball                      [Class  853] ->   0% (raw:   1/255)
 Rank #5: Italian greyhound                [Class  185] ->   0% (raw:   1/255)
=================================================================
>>> IDENTIFIED OBJECT: miniature schnauzer (93% confidence) <<<
```

---

## 6. Training Custom Non-ImageNet Classes (Optional)

If you need to recognize custom categories not present in ImageNet's 1,000 classes (e.g., custom factory components or domain-specific objects):

1. **Transfer Learning in Python / TensorFlow**:
   ```python
   base_model = tf.keras.applications.MobileNetV2(
       input_shape=(224, 224, 3), include_top=False, weights='imagenet'
   )
   base_model.trainable = False
   x = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
   outputs = tf.keras.layers.Dense(NUM_CUSTOM_CLASSES, activation='softmax')(x)
   model = tf.keras.Model(base_model.input, outputs)
   ```
2. **Quantize to UINT8 / INT8**:
   ```python
   converter = tf.lite.TFLiteConverter.from_keras_model(model)
   converter.optimizations = [tf.lite.Optimize.DEFAULT]
   converter.representative_dataset = representative_dataset_gen
   tflite_quant_model = converter.convert()
   with open("custom_model.tflite", "wb") as f:
       f.write(tflite_quant_model)
   ```
3. **Convert to C Array**:
   ```bash
   python scripts/xxd.py custom_model.tflite custom_model.h
   ```
4. **Update Labels**: Update `labels.h` with your custom label names and rebuild the firmware.
