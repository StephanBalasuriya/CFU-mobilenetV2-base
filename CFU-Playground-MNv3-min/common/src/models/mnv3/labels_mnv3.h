/*
 * Copyright 2026 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/*
 * labels_mnv3.h
 *
 * 1001-class ImageNet label helpers for the MobileNetV3-Small Minimalistic
 * ImageNet model (model_mobilenetv3_imagenet_224_1000.h) compiled into
 * CFU-Playground firmware.
 *
 * Reuses the label table from models/mnv2/labels.h (which already contains
 * all 1001 ImageNet labels) under MNV3_ aliases to avoid duplicating ~18 KB.
 *
 * Class layout (matches MNv2 1001-class convention):
 *   [0]      = "background"
 *   [1..1000] = ImageNet 1000 classes (tench, goldfish, ... tabby, Egyptian cat, ...)
 */

#ifndef _MNV3_LABELS_H_
#define _MNV3_LABELS_H_

#include <stdbool.h>

/* Pull in the full ImageNet label table from the MNv2 header */
#include "models/mnv2/labels.h"

/* -------------------------------------------------------------------
 * MNV3_ aliases — number of classes and label accessor
 * ------------------------------------------------------------------- */
#define MNV3_NUM_CLASSES MNV2_NUM_CLASSES   /* 1001 */

static inline const char* mnv3_get_label(int class_id) {
    return mnv2_get_label(class_id);
}

static inline bool mnv3_is_valid_class(int class_id) {
    return mnv2_is_valid_class(class_id);
}

#endif  // _MNV3_LABELS_H_
