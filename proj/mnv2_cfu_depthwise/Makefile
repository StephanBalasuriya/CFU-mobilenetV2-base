#!/usr/bin/env make

# Minimal CFU-Playground integration for the CPU-fed fused operator.
# The model-wide TFLite integration is intentionally not enabled: this project
# exposes and tests one explicit fused pixel command stream.
export DEFINES := NDEBUG
export SKIP_TFLM := 1
RUN_MENU_ITEMS := 1
TEST_MENU_ITEMS := 1

include ../proj.mk

.PHONY: test test-python test-cxx generate image clean

IMAGE ?= inputs/input.jpg

image:
	cd $(CURDIR) && $(PYRUN) tools/image_to_header.py $(IMAGE) src/input_image.h

test: test-python test-cxx

test-python:
	cd $(CURDIR) && $(PYRUN) -m unittest discover -s gateware -p 'test_*.py'
	cd $(CURDIR) && $(PYRUN) -m unittest discover -s tests -p 'test_*.py'

test-cxx:
	mkdir -p build/tests
	g++ -std=c++11 -Wall -Wextra -Werror -DCFU_SOFTWARE_DEFINED \
		-I$(CFU_ROOT)/common/src -Isrc \
		src/fused_depthwise.cc src/software_cfu.cc tests/test_cxx_reference.cc \
		-o build/tests/test_cxx_reference
	build/tests/test_cxx_reference
	g++ -std=c++11 -Wall -Wextra -Werror -DCFU_SOFTWARE_DEFINED \
		-I$(CFU_ROOT)/common/src -Isrc \
		src/fused_depthwise.cc src/software_cfu.cc tests/test_software_cfu.cc \
		-o build/tests/test_software_cfu
	build/tests/test_software_cfu

generate:
	cd $(CURDIR) && $(PYRUN) cfu_gen.py
