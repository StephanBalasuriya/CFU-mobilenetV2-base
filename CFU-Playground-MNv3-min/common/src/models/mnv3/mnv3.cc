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
 * mnv3.cc  —  MobileNetV3-Small Minimalistic (ImageNet 1000-class) firmware handler
 *
 * Uses model_mobilenetv3_imagenet_224_1000.tflite:
 *   - 224 x 224 x 3 INT8 input  (scale=1.0, zero_point=-128)
 *   - 1000-class INT8 output logits (scale=0.003906, zero_point=-128)
 *   - Identifies real-world objects: cat, dog, car, etc.
 *
 * Images preprocessed by scripts/process_all_images_mnv3.py:
 *   int8_val = uint8_pixel - 128   (matches tflite_set_input_unsigned)
 *
 * Menu options:
 *   'i' — classify ALL images embedded from images/
 *   '1' — classify first image
 *   'g' — run golden test vector (input_00001)
 *   'z' — run zeros input
 */

#include "models/mnv3/mnv3.h"

#include <stdio.h>
#include <string.h>

#include "cfu.h"
#include "menu.h"
#include "models/mnv3/image_inputs_mnv3.h"
#include "models/mnv3/input_00001.h"
#include "models/mnv3/labels_mnv3.h"
#include "models/mnv3/model_mobilenetv3_imagenet_224_1000.h"
#include "playground_util/console.h"
#include "tflite.h"

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
extern "C" {
#include "fb_util.h"
};
#endif

// -----------------------------------------------------------------------
// CFU enable/disable prompt
// -----------------------------------------------------------------------
static void ask_cfu_setting(void) {
  printf("\n==================================================\n");
  printf("Disable CFU acceleration? (y/n) [n]: ");
  char c;
  do { c = readchar(); } while (c == '\n' || c == '\r');
  putchar(c); putchar('\n');
  if (c == 'y' || c == 'Y') {
    set_cfu_enabled(0);
    printf("--> CFU DISABLED: Running model directly on CPU.\n");
  } else {
    set_cfu_enabled(1);
    printf("--> CFU ENABLED: Running model inside CFU.\n");
  }
  printf("==================================================\n\n");
}

// -----------------------------------------------------------------------
// Model initialisation
// -----------------------------------------------------------------------
static void mnv3_init(void) {
  tflite_load_model(model_mobilenetv3_imagenet_224_1000,
                    model_mobilenetv3_imagenet_224_1000_len);
}

// -----------------------------------------------------------------------
// Top-K over INT8 logits (no heap allocation)
// Output scale = 0.003906, zero_point = -128
// Confidence % ≈ (exp(logit/scale) / sum_exp) * 100, approximated as:
//   relative score = (logit - min_logit) / (max_logit - min_logit) * 100
// -----------------------------------------------------------------------
struct TopKEntry {
  int   class_index;
  int8_t score;
};

#define TOP_K 5

static void find_top_k(const int8_t* scores, int num_classes,
                       struct TopKEntry* top_k) {
  for (int i = 0; i < TOP_K; i++) {
    top_k[i].class_index = -1;
    top_k[i].score = -128;
  }
  for (int i = 0; i < num_classes; i++) {
    int8_t val = scores[i];
    for (int j = 0; j < TOP_K; j++) {
      if (val > top_k[j].score) {
        for (int m = TOP_K - 1; m > j; m--) top_k[m] = top_k[m - 1];
        top_k[j].class_index = i;
        top_k[j].score = val;
        break;
      }
    }
  }
}

// Map top INT8 logit to approximate confidence %.
// Output quantisation: scale=0.003906, zero_point=-128
// real_value = (logit - (-128)) * 0.003906 = (logit + 128) * 0.003906
// We express confidence relative to the top-2 spread.
static int logit_to_pct(int8_t best, int8_t second) {
  int spread = (int)best - (int)second;
  if (spread <= 0) return 50;
  // Saturate at 99% for very large spread
  int pct = 50 + (spread * 50) / 64;
  return (pct > 99) ? 99 : pct;
}

// -----------------------------------------------------------------------
// Core inference + result printer
// -----------------------------------------------------------------------
static void mnv3_run_and_print(const char* label) {
  printf("Running MobileNetV3 Minimalistic (%s) on: %s\n",
         is_cfu_enabled() ? "CFU accelerated" : "Pure CPU", label);
  tflite_classify();

  int8_t* output = tflite_get_output();

  struct TopKEntry top5[TOP_K];
  find_top_k(output, MNV3_NUM_CLASSES, top5);

  // Compute approximate confidence from logit spread
  int best_pct = (top5[1].class_index >= 0)
                 ? logit_to_pct(top5[0].score, top5[1].score)
                 : 95;

  printf("\n=================================================================\n");
  printf("           CLASSIFICATION RESULTS: %s\n", label);
  printf("=================================================================\n");
  for (int i = 0; i < TOP_K; i++) {
    int idx = top5[i].class_index;
    if (idx >= 0 && mnv3_is_valid_class(idx)) {
      // Approximate per-rank confidence from relative logit gap
      int pct = (i == 0) ? best_pct
                         : logit_to_pct(top5[i].score,
                                        (i + 1 < TOP_K) ? top5[i+1].score : (int8_t)-128);
      printf(" Rank #%d: %-34s [Class %4d] -> %3d%% (logit: %4d)\n",
             i + 1, mnv3_get_label(idx), idx, pct, (int)top5[i].score);
    }
  }
  printf("=================================================================\n");

  if (top5[0].class_index >= 0) {
    printf(">>> IDENTIFIED OBJECT: %s (%d%% confidence) <<<\n\n",
           mnv3_get_label(top5[0].class_index), best_pct);
  }

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  if (top5[0].class_index >= 0) {
    char msg[256];
    snprintf(msg, sizeof(msg), "%s (%d%%)", mnv3_get_label(top5[0].class_index), best_pct);
    fb_clear();
    fb_draw_string(0, 10, 0x00FFAA00, "MobileNetV3 Min - ImageNet");
    fb_draw_string(0, 30, 0x00FFFFFF, label);
    fb_draw_string(0, 230, 0x00FFAA00, msg);
    flush_cpu_dcache();
    flush_l2_cache();
  }
#endif
}

// -----------------------------------------------------------------------
// Classify one image from the embedded images/ database
// -----------------------------------------------------------------------
static void classify_image_mnv3(const struct ImageSampleMnv3* sample) {
  printf("\nLoading image: %s (%u bytes)...\n",
         sample->filename, (unsigned)sample->size);

  // tflite_set_input_unsigned: copies uint8 data subtracting 128 per byte,
  // giving int8_val = uint8_val - 128 which matches scale=1.0 zero_point=-128.
  // Our image header already stores int8 data, so reinterpret as uint8 first:
  // uint8 = int8 + 128, then tflite_set_input_unsigned subtracts 128 → net zero.
  // Alternatively use tflite_set_input directly.
  tflite_set_input(sample->data);   // direct memcpy — data is already int8

  mnv3_run_and_print(sample->filename);

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  fb_draw_buffer(0, 50, 224, 224, (const uint8_t*)sample->data, 3);
  flush_cpu_dcache();
  flush_l2_cache();
#endif
}

// -----------------------------------------------------------------------
// Menu actions
// -----------------------------------------------------------------------
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
  tflite_set_input(input_00001);
  mnv3_run_and_print("golden_input_00001");
}

static void do_classify_zeros(void) {
  ask_cfu_setting();
  tflite_set_input_zeros();
  mnv3_run_and_print("zeros_input");
}

// -----------------------------------------------------------------------
// Menu descriptor
// -----------------------------------------------------------------------
static struct Menu MENU = {
    "MobileNetV3 Minimalistic Models (ImageNet 1000-class)",
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
