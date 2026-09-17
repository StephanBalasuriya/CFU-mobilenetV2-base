#!/usr/bin/env python

export DEFINES :=
DEFINES += NDEBUG

# CPU-only baseline.
export NO_CFU := 1

# Tell proj.mk to remove the upstream MobileNetV2 application
# from the copied common source tree.
export MNv2_BASELINE := 1

DEFINES += INCLUDE_MODEL_PDTI8

ifneq 'hps' '$(PLATFORM)'
DEFINES += INCLUDE_MODEL_MNV2
endif

RUN_MENU_ITEMS := 3 1

include ../proj.mk