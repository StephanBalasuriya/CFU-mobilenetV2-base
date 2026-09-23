/*
 * Copyright 2021 The CFU-Playground Authors
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

#include "models/mnv2/mnv2.h"

#include <stdio.h>
#include <string.h>

#include "cfu.h"
#include "menu.h"
#include "models/mnv2/labels.h"
#include "models/mnv2/model_mobilenetv2_1000_classes.h"
#include "models/mnv2/image_inputs.h"
#include "playground_util/console.h"
#include "tflite.h"

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
extern "C" {
#include "fb_util.h"
};
#endif

// Prompt user on Renode display to disable CFU or run with CFU
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

// Initialize the 1000-class MobileNetV2 model once
static void mnv2_init(void) {
  tflite_load_model(model_mobilenetv2_1000_classes, model_mobilenetv2_1000_classes_len);
}

struct TopPrediction {
  int class_index;
  uint8_t score;
};

// Find Top-K predicted classes using insertion sort (no dynamic allocation)
static void find_top_k(const uint8_t* scores, int num_classes, int k, struct TopPrediction* top_k) {
  for (int i = 0; i < k; i++) {
    top_k[i].class_index = -1;
    top_k[i].score = 0;
  }
  for (int i = 0; i < num_classes; i++) {
    uint8_t val = scores[i];
    for (int j = 0; j < k; j++) {
      if (val > top_k[j].score) {
        for (int m = k - 1; m > j; m--) {
          top_k[m] = top_k[m - 1];
        }
        top_k[j].class_index = i;
        top_k[j].score = val;
        break;
      }
    }
  }
}

// Run inference on a specific ImageSample and print top recognized objects
static void classify_image_sample(const struct ImageSample* sample) {
  printf("\nLoading image: %s (%u bytes)...\n", sample->filename, (unsigned)sample->size);
  tflite_set_input_mobilenet_pixels(sample->data);

  printf("Running MobileNetV2 inference (%s)...\n",
         is_cfu_enabled() ? "CFU accelerated" : "Pure CPU");
  tflite_classify();

  // Read output probabilities across 1001 ImageNet classes
  uint8_t* output = (uint8_t*)tflite_get_output();

  struct TopPrediction top5[5];
  find_top_k(output, MNV2_NUM_CLASSES, 5, top5);

  printf("\n=================================================================\n");
  printf("           CLASSIFICATION RESULTS: %s\n", sample->filename);
  printf("=================================================================\n");
  for (int i = 0; i < 5; i++) {
    int idx = top5[i].class_index;
    if (idx >= 0 && idx < MNV2_NUM_CLASSES) {
      int confidence = ((int)top5[i].score * 100) / 255;
      printf(" Rank #%d: %-32s [Class %4d] -> %3d%% (raw: %3d/255)\n",
             i + 1, mnv2_get_label(idx), idx, confidence, top5[i].score);
    }
  }
  printf("=================================================================\n");

  const char* best_label = (top5[0].class_index >= 0) ? mnv2_get_label(top5[0].class_index) : "Unknown";
  int best_conf = ((int)top5[0].score * 100) / 255;
  printf(">>> IDENTIFIED OBJECT: %s (%d%% confidence) <<<\n\n", best_label, best_conf);

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  char msg_buff[256];
  snprintf(msg_buff, sizeof(msg_buff), "%s: %s (%d%%)", sample->filename, best_label, best_conf);
  fb_clear();
  fb_draw_string(0, 10, 0x007FFF00, sample->filename);
  fb_draw_buffer(0, 50, 224, 224, sample->data, 3);
  fb_draw_string(0, 280, 0x007FFF00, msg_buff);
  flush_cpu_dcache();
  flush_l2_cache();
#endif
}

// Classify all images found in images/ one after another
static void do_classify_all_images(void) {
  ask_cfu_setting();
  printf("Found %d image(s) in image database.\n", NUM_IMAGES);
  for (size_t i = 0; i < NUM_IMAGES; i++) {
    classify_image_sample(&ALL_IMAGES[i]);
  }
}

// Classify the first image
static void do_classify_first_image(void) {
  ask_cfu_setting();
  if (NUM_IMAGES > 0) {
    classify_image_sample(&ALL_IMAGES[0]);
  } else {
    printf("No images available in image database.\n");
  }
}

// Run classification on zeros input
static void do_classify_zeros(void) {
  ask_cfu_setting();
  tflite_set_input_zeros();
  printf("Running MobileNetV2 with zeros input...\n");
  tflite_classify();
  uint8_t* output = (uint8_t*)tflite_get_output();
  struct TopPrediction top1;
  find_top_k(output, MNV2_NUM_CLASSES, 1, &top1);
  printf("Top class for zeros: %s (id: %d, score: %d)\n",
         mnv2_get_label(top1.class_index), top1.class_index, top1.score);
}

static struct Menu MENU = {
    "Tests for MobileNetV2 1000-class Model",
    "mnv2",
    {
        MENU_ITEM('a', "Classify ALL images in images/ folder", do_classify_all_images),
        MENU_ITEM('1', "Classify first image", do_classify_first_image),
        MENU_ITEM('z', "Run with zeros input", do_classify_zeros),
        MENU_END,
    },
};

// For integration into menu system
void mnv2_menu() {
  mnv2_init();

#ifdef CSR_VIDEO_FRAMEBUFFER_BASE
  fb_init();
  flush_cpu_dcache();
  flush_l2_cache();
#endif

  menu_run(&MENU);
}
