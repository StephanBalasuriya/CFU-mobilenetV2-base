#!/bin/env python
# Copyright 2026 CFU-Playground Authors
#
# MobileNetV2 Baseline Project Makefile
# Runs MobileNetV2 strictly on the CPU (No CFU custom instructions or hardware acceleration)

# C Preprocessor Definitions
export DEFINES :=

# Optimization flags: Disable debug macros for maximum CPU performance
DEFINES += NDEBUG

# Include MobileNetV2 TFLite Micro model in the build
DEFINES += INCLUDE_MODEL_MNV2

# Default menu sequence for interactive / automated execution
# Item 3 = Models Menu (MobileNetV2), Item 1 = Test 1
RUN_MENU_ITEMS := 3 1

include ../proj.mk
