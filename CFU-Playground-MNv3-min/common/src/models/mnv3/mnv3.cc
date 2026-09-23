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
 * mnv3.cc  —  MobileNetV3-Small Minimalistic firmware menu handler
 *
 * Provides three classification modes inside Renode/hardware:
 *   'g' → Run golden test vector (input_00001.dat)
 *   'i' → Classify all images embedded from images/ directory
 *   'z' → Run with zeros input
 *
 * Images are pre-processed into image_inputs_mnv3.h by running:
 *   python scripts/process_all_images_mnv3.py
 * from the CFU-Playground-MNv3-min project root.
 */

#include "models/mnv3/mnv3.h"

#include <stdio.h>
#include <string.h>

#include "cfu.h"
#include "menu.h"
#include "models/mnv3/image_inputs_mnv3.h"
#include "models/mnv3/input_00001.h"
#include "models/mnv3/labels_mnv3.h"
#include "models/mnv3/model_mobilenetv3_small_min.h"
#include "playground_util/console.h"
#include "tflite.h"

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
extern "C" {
#include "fb_util.h"
};
#endif

// -------------------------------------------------------------------------
// CFU Enable/Disable prompt (shared by all inference paths)
// -------------------------------------------------------------------------
static void ask_cfu_setting(void) {
  printf("\n==================================================\n");
  printf("Disable CFU acceleration? (y/n) [n]: ");
  char c;
  do {
    c = readchar();
  } while (c == '\n' || c == '\r');
  putchar(c);
  putchar('\n');
  if (c == 'y' || c == 'Y') {
    set_cfu_enabled(0);
    printf("--> CFU DISABLED: Running model directly on CPU.\n");
  } else {
    set_cfu_enabled(1);
    printf("--> CFU ENABLED: Running model inside CFU.\n");
  }
  printf("==================================================\n\n");
}

// -------------------------------------------------------------------------
// Model initialisation
// -------------------------------------------------------------------------
static void mnv3_init(void) {
  tflite_load_model(model_mobilenetv3_small_min, model_mobilenetv3_small_min_len);
}

// -------------------------------------------------------------------------
// Top-K scoring (no heap allocation)
// -------------------------------------------------------------------------
struct TopPredictionMnv3 {
  int   class_index;
  int8_t score;        /* INT8 output logit */
};

static void find_top_k_mnv3(const int8_t* scores, int num_classes, int k,
                             struct TopPredictionMnv3* top_k) {
  for (int i = 0; i < k; i++) {
    top_k[i].class_index = -1;
    top_k[i].score = -128;
  }
  for (int i = 0; i < num_classes; i++) {
    int8_t val = scores[i];
    for (int j = 0; j < k; j++) {
      if (val > top_k[j].score) {
        for (int m = k - 1; m > j; m--) top_k[m] = top_k[m - 1];
        top_k[j].class_index = i;
        top_k[j].score = val;
        break;
      }
    }
  }
}

// -------------------------------------------------------------------------
// Core classification engine
// -------------------------------------------------------------------------
static void mnv3_run_and_print(const char* label) {
  printf("Running MobileNetV3 Minimalistic (%s) on: %s\n",
         is_cfu_enabled() ? "CFU accelerated" : "Pure CPU", label);
  tflite_classify();

  int8_t* output = tflite_get_output();

  // Top-K over all output classes
  int k = (MNV3_NUM_CLASSES < 5) ? MNV3_NUM_CLASSES : 5;
  struct TopPredictionMnv3 topk[5];
  find_top_k_mnv3(output, MNV3_NUM_CLASSES, k, topk);

  printf("\n=================================================================\n");
  printf("           CLASSIFICATION RESULTS: %s\n", label);
  printf("=================================================================\n");
  for (int i = 0; i < k; i++) {
    int idx = topk[i].class_index;
    if (idx >= 0 && idx < MNV3_NUM_CLASSES) {
      // Map [-128..127] → 0..100%
      int pct = ((int)(topk[i].score) + 128) * 100 / 255;
      printf(" Rank #%d: %-32s [Class %4d] -> %3d%% (logit: %4d)\n",
             i + 1, mnv3_get_label(idx), idx, pct, (int)topk[i].score);
    }
  }
  printf("=================================================================\n");

  if (topk[0].class_index >= 0) {
    int pct = ((int)(topk[0].score) + 128) * 100 / 255;
    printf(">>> IDENTIFIED: %s (%d%% confidence) <<<\n\n",
           mnv3_get_label(topk[0].class_index), pct);
  }
}

// -------------------------------------------------------------------------
// Classify one image from the embedded database
// -------------------------------------------------------------------------
static void classify_image_mnv3(const struct ImageSampleMnv3* sample) {
  printf("\nLoading image: %s (%u bytes)...\n",
         sample->filename, (unsigned)sample->size);

  // INT8 input: data is already zero-point-shifted by process_all_images_mnv3.py
  tflite_set_input_unsigned((const uint8_t*)sample->data);

  mnv3_run_and_print(sample->filename);

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  char msg[256];
  int idx  = 0; /* use first class index from top1 */
  int8_t* out = tflite_get_output();
  snprintf(msg, sizeof(msg), "%s", sample->filename);
  fb_clear();
  fb_draw_string(0, 10, 0x00FFAA00, "MobileNetV3 Min - Image Classify");
  fb_draw_buffer(0, 40, 160, 160, (const uint8_t*)sample->data, 3);
  fb_draw_string(0, 210, 0x00FFAA00, msg);
  flush_cpu_dcache();
  flush_l2_cache();
#endif
}

// -------------------------------------------------------------------------
// Menu actions
// -------------------------------------------------------------------------
static void do_classify_all_images(void) {
  ask_cfu_setting();
  printf("Found %d image(s) in MNv3 image database.\n", NUM_IMAGES_MNV3);
  for (int i = 0; i < NUM_IMAGES_MNV3; i++) {
    classify_image_mnv3(&ALL_IMAGES_MNV3[i]);
  }
}

static void do_classify_first_image(void) {
  ask_cfu_setting();
  if (NUM_IMAGES_MNV3 > 0) {
    classify_image_mnv3(&ALL_IMAGES_MNV3[0]);
  } else {
    printf("No images available. Run scripts/process_all_images_mnv3.py first.\n");
  }
}

static void do_classify_golden(void) {
  ask_cfu_setting();
  tflite_set_input_unsigned(input_00001);
  mnv3_run_and_print("golden_input_00001");
}

static void do_classify_zeros(void) {
  ask_cfu_setting();
  tflite_set_input_zeros();
  mnv3_run_and_print("zeros_input");
}

// -------------------------------------------------------------------------
// Menu descriptor
// -------------------------------------------------------------------------
static struct Menu MENU = {
    "MobileNetV3 Minimalistic Models",
    "mnv3",
    {
        MENU_ITEM('i', "Classify ALL images in images/ folder", do_classify_all_images),
        MENU_ITEM('1', "Classify first image",                  do_classify_first_image),
        MENU_ITEM('g', "Run golden test input (input_00001)",   do_classify_golden),
        MENU_ITEM('z', "Run zeros input test",                  do_classify_zeros),
        MENU_END,
    },
};

void mnv3_menu(void) {
  mnv3_init();

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  fb_init();
  flush_cpu_dcache();
  flush_l2_cache();
#endif

  menu_run(&MENU);
}
