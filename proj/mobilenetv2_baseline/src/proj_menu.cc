/*
 * MobileNetV2 Baseline Project Menu
 */

#include "proj_menu.h"

#include <stdio.h>

#include "menu.h"

namespace {

void do_baseline_info(void) {
  puts("\r\n--- MobileNetV2 Pure CPU Baseline ---");
  puts("Executing TensorFlow Lite Micro reference integer ops directly on VexRiscv CPU.");
  puts("No CFU hardware acceleration (ACCEL_CONV disabled).\r\n");
}

struct Menu MENU = {
    "MobileNetV2 Baseline Project Menu",
    "mnv2_baseline",
    {
        MENU_ITEM('i', "Show Baseline CPU Info", do_baseline_info),
        MENU_END,
    },
};
}  // anonymous namespace

extern "C" void do_proj_menu() { menu_run(&MENU); }
