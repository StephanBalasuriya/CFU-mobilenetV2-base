#!/bin/env python

# MobileNetV2 a0.35 INT8 + CFU project.
#
# This project uses the existing CFU-Playground mnv2_first
# accelerator architecture, but runs it with our 224x224
# ImageNet MobileNetV2 model and application.

export DEFINES :=
DEFINES += NDEBUG

# Enable the MobileNetV2 CFU path.
DEFINES += ACCEL_CONV

# Keep the model and application isolated from upstream mnv2_first.
export MNv2_BASELINE := 1

# The model is an external project model copied from model/.
DEFINES += INCLUDE_MODEL_PDTI8

ifneq 'hps' '$(PLATFORM)'
DEFINES += INCLUDE_MODEL_MNV2
endif

RUN_MENU_ITEMS := 3 1

LABELS_SOURCE = $(CFU_ROOT)/proj/mnv2_baseline/mobilenetv2_a035_224_int8_labels.txt
LABELS_HEADER = $(BUILD_DIR)/src/imagenet_labels.h

BUILD_DIR_EXTRA_DEP += $(LABELS_HEADER)

include ../proj.mk


$(LABELS_HEADER): $(LABELS_SOURCE) $(PROJ_DIR)/tools/generate_labels_header.py
	@mkdir -p $(dir $@)
	python3 $(PROJ_DIR)/tools/generate_labels_header.py \
		$(LABELS_SOURCE) \
		$@
