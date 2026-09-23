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
 * Class label helpers for the MobileNetV3-Small Minimalistic model compiled
 * into CFU-Playground firmware.
 *
 * The current embedded model (model_mobilenetv3_small_min.tflite) was exported
 * with NUM_CLASSES = 2 (binary classification). If you retrain/replace the
 * model with a 1000-class ImageNet variant, increase MNV3_NUM_CLASSES to 1000
 * and expand MNV3_LABELS accordingly (see README_MNV3min_IMAGE_CLASSIFICATION.md).
 */

#ifndef _MNV3_LABELS_H_
#define _MNV3_LABELS_H_

#include <stdbool.h>

/* -----------------------------------------------------------------------
 * Adjust this to match the number of output classes in your .tflite model
 * ----------------------------------------------------------------------- */
#define MNV3_NUM_CLASSES 2

/* Labels for the default 2-class binary model.
 * Class 0 = negative / no-object
 * Class 1 = positive / object-present
 *
 * Replace with your own label strings when using a multi-class model.
 */
static const char* const MNV3_LABELS[MNV3_NUM_CLASSES] = {
    "class_0_negative",  /* output[0] */
    "class_1_positive",  /* output[1] */
};

/* Retrieve the human-readable label for a given class index */
static inline const char* mnv3_get_label(int class_id) {
    if (class_id >= 0 && class_id < MNV3_NUM_CLASSES) {
        return MNV3_LABELS[class_id];
    }
    return "unknown";
}

/* Check if a class index is valid */
static inline bool mnv3_is_valid_class(int class_id) {
    return (class_id >= 0 && class_id < MNV3_NUM_CLASSES);
}

#endif  // _MNV3_LABELS_H_
