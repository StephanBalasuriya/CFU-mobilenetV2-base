#!/bin/env python
SHELL := /bin/bash

# Common build rules for all projects. Included by project makefiles.

# There are three execution environments supported by this makefile
#
# * Arty A7
# * Renode
# * Verilator simulation
#
# Arty builds require 3 parts:
# - SoC Gateware
# - SoC Software - BIOS, libraries and #includes
# - The main C program
#
# Renode builds are quite similar to Arty, and use the same Soc
# Software and C program builds.
#
# Simulator builds are a little different:
# - Verilator C++ instead of Gateware
# - Soc Software is different due to the simulator having a different
#   set of peripherals
# - The main C program requires rebuilding since it uses different
#   Soc Software.
#
# To run on Arty (from within proj/xxx subdirectory):
# $ make prog
# $ make load
#
# To run on Renode:
# $ make renode

export UART_SPEED ?= 1843200

# Need a slower baudrate when communicating with Serv
ifdef SERV
export UART_SPEED = 115200
endif

export PROJ       := $(lastword $(subst /, ,${CURDIR}))
export CFU_ROOT   := $(realpath $(CURDIR)/../..)
export PLATFORM   ?= common_soc
export TARGET     ?= digilent_arty
export TTY        ?= $(or $(wildcard /dev/ttyUSB?), $(wildcard /dev/ttyACM?))

RUN_MENU_ITEMS    ?= 1 1 1
TEST_MENU_ITEMS   ?= 5

PLATFORMS=common_soc sim hps
ifneq 'common_soc' '$(findstring $(PLATFORM),$(PLATFORMS))'
$(error PLATFORM must be one of following: $(PLATFORMS))
endif

ifneq 'common_soc' '$(PLATFORM)'
TARGET := $(PLATFORM)
endif

SOC_DIR          := $(CFU_ROOT)/soc
SOC_BUILD_NAME   := $(TARGET).$(PROJ)
SOC_BUILD_DIR    := $(SOC_DIR)/build/$(SOC_BUILD_NAME)
SOC_SOFTWARE_DIR := $(SOC_BUILD_DIR)/software
export SOC_SOFTWARE_DIR
SOC_GATEWARE_DIR := $(SOC_BUILD_DIR)/gateware

# Make software build dependent on platform
export DEFINES    += PLATFORM_$(PLATFORM)
export DEFINES    += PLATFORM=$(PLATFORM)

# We can specify NOT compiling the TFLite-micro library
ifdef SKIP_TFLM
export DEFINES    += SKIP_TFLM
endif

SHELL           := /bin/bash
CRC             :=
#CRC             := --no-crc

# Tools we use
COPY := /bin/cp -a
RM := /bin/rm -rf
MKDIR := /bin/mkdir

# TODO: search upward until we find the root
# ... or get CFU_ROOT from an env variable

LXTERM       := $(SOC_DIR)/bin/litex_term
BITSTREAM    := $(SOC_GATEWARE_DIR)/$(PLATFORM).bit

PROJ_DIR        := $(realpath .)

CFU_GEN         := $(PROJ_DIR)/cfu_gen.py

# Only define CFU_VERILOG when CFU is enabled.
# CPU-only builds must not try to build or pass a CFU Verilog file.
ifndef NO_CFU
CFU_VERILOG     := $(if $(wildcard $(PROJ_DIR)/cfu.sv),$(PROJ_DIR)/cfu.sv,$(PROJ_DIR)/cfu.v)
endif

BUILD_DIR       := $(PROJ_DIR)/build
PYRUN           := $(CFU_ROOT)/scripts/pyrun

# Optional additional arguments for cfu_gen
CFU_GEN_EXTRA_ARGS ?=

# Additional dependencies for assembling the build directory
BUILD_DIR_EXTRA_DEP ?=

# Matching pattern used by pytest to find unit tests
PYTEST_PATTERN ?= 'test_*.py'

COMMON_DIR         := $(CFU_ROOT)/common
RVI_DIR            := $(COMMON_DIR)/renode-verilator-integration
COMMON_FILES       := $(shell find $(COMMON_DIR) -type f)
MLCOMMONS_SRC_DIR  := $(CFU_ROOT)/third_party/mlcommons
SAXON_SRC_DIR      := $(CFU_ROOT)/third_party/SaxonSoc
DONUT_SRC_DIR      := $(CFU_ROOT)/third_party/litex-donut
RENODE_DIR         := $(CFU_ROOT)/third_party/renode
VIL_DIR            := $(RENODE_DIR)/verilator-integration-library
LITEX_RENODE_DIR   := $(CFU_ROOT)/third_party/python/litex-renode
SRC_DIR            := $(abspath $(PROJ_DIR)/src)

TFLM_SRC_DIR       := $(CFU_ROOT)/third_party/tflite-micro
TFLM_MAKE_DIR      := $(TFLM_SRC_DIR)/tensorflow/lite/micro/tools/make
TFLM_TP_DIR        := $(TFLM_SRC_DIR)/third_party

# Copy every file found in these directories, except those excluded
TFLM_COPY_SRC_DIRS := \
	tensorflow/lite \
	tensorflow/lite/c \
	tensorflow/lite/core/api \
	tensorflow/lite/core/c \
	tensorflow/lite/kernels \
	tensorflow/lite/kernels/internal \
	tensorflow/lite/kernels/internal/optimized \
	tensorflow/lite/kernels/internal/reference \
	tensorflow/lite/kernels/internal/reference/integer_ops \
	tensorflow/lite/micro \
	tensorflow/lite/micro/kernels \
	tensorflow/lite/micro/memory_planner \
	tensorflow/lite/micro/arena_allocator \
	tensorflow/lite/micro/tflite_bridge \
	tensorflow/lite/schema

TFLM_FIND_PARAMS := \
	-maxdepth 1 -type f \
	-not -name '*_test*' \
	-regex '.*\.\(h\|c\|cc\)'

# Just copy data files from these dirs
TFLM_COPY_DATA_DIRS := \
	tensorflow/lite/micro/examples/magic_wand \
	tensorflow/lite/micro/examples/micro_speech/micro_features \
	tensorflow/lite/micro/examples/person_detection \
	tensorflow/lite/micro/models \
	tensorflow/lite/micro/kernels/testdata

SOFTWARE_BIN     := $(BUILD_DIR)/software.bin
SOFTWARE_ELF     := $(BUILD_DIR)/software.elf
SOFTWARE_LOG     := $(BUILD_DIR)/software.log
UNITTEST_LOG     := $(BUILD_DIR)/unittest.log

# Directory where we build the project-specific gateware
SOC_DIR      := $(CFU_ROOT)/soc
HPS_MK       := $(MAKE) -C $(SOC_DIR) -f $(SOC_DIR)/hps.mk
SIM_MK       := $(MAKE) -C $(SOC_DIR) -f $(SOC_DIR)/sim.mk SOFTWARE_BIN=$(SOFTWARE_BIN)
COMMON_SOC_MK := $(MAKE) -C $(SOC_DIR) -f $(SOC_DIR)/common_soc.mk

ifeq '$(PLATFORM)' 'hps'
	SOC_MK   := $(HPS_MK)
else ifeq '$(PLATFORM)' 'common_soc'
	SOC_MK   := $(COMMON_SOC_MK)
else ifeq '$(PLATFORM)' 'sim'
	SOC_MK   := $(SIM_MK)
else
	$(error PLATFORM must be 'common_soc' or 'hps' or 'sim')
endif

TARGET_REPL := $(BUILD_DIR)/renode/$(TARGET)_generated.repl

ifneq '$(VERILATOR_TRACE_DEPTH)' ''
	ENABLE_TRACE_ARG := --trace
endif

ifeq '$(ENABLE_TRACE_ARG)' '--trace'
	VERILATOR_TRACE_PATH := $(BUILD_DIR)/simx.vcd
else ifeq '$(ENABLE_TRACE_ARG)' '--trace-fst'
	VERILATOR_TRACE_PATH := $(BUILD_DIR)/simx.fst
endif

BUILD_JOBS ?= $(shell nproc)

.PHONY: renode
renode: renode-scripts
	@echo Running interactively under renode
	pushd $(BUILD_DIR)/renode/ && $(RENODE_DIR)/renode -e "s @$(TARGET).resc" && popd

.PHONY: renode-headless
renode-headless: renode-scripts
	pushd $(BUILD_DIR)/renode/ && $(RENODE_DIR)/renode --console --disable-xwt --hide-log -e "s @$(TARGET).resc ; uart_connect sysbus.uart" && popd

.PHONY: renode-test
renode-test: renode-scripts
	$(RENODE_DIR)/renode-test $(BUILD_DIR)/renode/$(TARGET).robot

.PHONY: renode-scripts
renode-scripts: $(SOFTWARE_ELF)
	@mkdir -p $(BUILD_DIR)/renode
ifneq '$(SW_ONLY)' '1'
ifndef NO_CFU
	pushd $(BUILD_DIR)/renode && cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_TRACE=$(ENABLE_TRACE_ARG) -DTRACE_DEPTH_VAL=$(VERILATOR_TRACE_DEPTH) \
		-DINCLUDE_DIR="$(PROJ_DIR)" -DVTOP="$(CFU_VERILOG)" -DVIL_DIR="$(VIL_DIR)" $${VERILATOR_PATH:+"-DUSER_VERILATOR_DIR=$$VERILATOR_PATH"} \
		-DTRACE_FILEPATH="$(VERILATOR_TRACE_PATH)" "$(RVI_DIR)" && make libVtop && popd
	$(CFU_ROOT)/scripts/generate_renode_scripts.py $(SOC_BUILD_DIR)/csr.json $(TARGET) $(BUILD_DIR)/renode/ --repl $(TARGET_REPL)
else
	$(CFU_ROOT)/scripts/generate_renode_scripts.py $(SOC_BUILD_DIR)/csr.json $(TARGET) $(BUILD_DIR)/renode/ --repl $(TARGET_REPL) --sw-only
endif
else
	$(CFU_ROOT)/scripts/generate_renode_scripts.py $(SOC_BUILD_DIR)/csr.json $(TARGET) $(BUILD_DIR)/renode/ --repl $(TARGET_REPL) --sw-only
endif
	@echo Generating Renode scripts finished

.PHONY: clean
clean:
	$(SOC_MK) clean
	$(SIM_MK) clean
	@echo Removing $(BUILD_DIR)
	$(RM) $(BUILD_DIR)

.PHONY: software
software: $(SOFTWARE_BIN)

$(SOFTWARE_BIN) $(SOFTWARE_ELF): litex-software build-dir
	$(MAKE) -C $(BUILD_DIR) all -j $(BUILD_JOBS)

# Always run cfu_gen when it exists
# cfu_gen should not update cfu.v unless it has changed
ifneq (,$(wildcard $(CFU_GEN)))
ifndef NO_CFU
$(CFU_VERILOG): generate_cfu
endif

.PHONY: generate_cfu
generate_cfu:
	$(PYRUN) $(CFU_GEN) $(CFU_GEN_EXTRA_ARGS)

endif

# Note that the common Makefile is used in preference to the TfLM Makefile
# TODO: consider using rsync instead of cp
#$(COPY) $(TFLM_SRC_DIR)/third_party  $(BUILD_DIR)/src/third_party
#	$(COPY) $(TFLM_SRC_DIR)/third_party  $(BUILD_DIR)/src/third_party

$(BUILD_DIR)/src:
	@echo "Making BUILD_DIR"
	@mkdir -p $(BUILD_DIR)/src

.PHONY: tflite-micro-src
tflite-micro-src: $(BUILD_DIR)/src
ifndef SKIP_TFLM
	@echo "Copying tflite-micro files"
	for d in $(TFLM_COPY_SRC_DIRS); do \
		mkdir -p $(BUILD_DIR)/src/$$d; \
		$(COPY) `find $(TFLM_SRC_DIR)/$$d $(TFLM_FIND_PARAMS)` $(BUILD_DIR)/src/$$d; \
	done

	$(COPY) $(TFLM_SRC_DIR)/tensorflow/lite/micro/kernels/conv_test* \
		$(BUILD_DIR)/src/tensorflow/lite/micro/kernels

	$(COPY) $(TFLM_SRC_DIR)/tensorflow/lite/micro/kernels/depthwise_conv_test* \
		$(BUILD_DIR)/src/tensorflow/lite/micro/kernels

	@for d in $(TFLM_COPY_DATA_DIRS); do \
		mkdir -p $(BUILD_DIR)/src/$$d; \
		$(COPY) `find $(TFLM_SRC_DIR)/$$d -maxdepth 1 -type f -regex '.*_data\.\(h\|cc\)'` \
			$(BUILD_DIR)/src/$$d; \
	done

	mkdir -p $(BUILD_DIR)/src/tensorflow/lite/micro/examples/person_detection

	$(COPY) $(TFLM_SRC_DIR)/tensorflow/lite/micro/examples/person_detection/model_settings* \
		$(BUILD_DIR)/src/tensorflow/lite/micro/examples/person_detection

	@echo "TfLM: copying selected third_party files"

	mkdir -p $(BUILD_DIR)/src/third_party/gemmlowp

	$(COPY) $(TFLM_TP_DIR)/gemmlowp/fixedpoint \
		$(BUILD_DIR)/src/third_party/gemmlowp

	$(COPY) $(TFLM_TP_DIR)/gemmlowp/internal \
		$(BUILD_DIR)/src/third_party/internal

	mkdir -p $(BUILD_DIR)/src/third_party/flatbuffers/include

	$(COPY) $(TFLM_TP_DIR)/flatbuffers/include/* \
		$(BUILD_DIR)/src/third_party/flatbuffers/include

	mkdir -p $(BUILD_DIR)/src/third_party/ruy/ruy/profiler

	$(COPY) $(TFLM_TP_DIR)/ruy/ruy/profiler/instrumentation.h \
		$(BUILD_DIR)/src/third_party/ruy/ruy/profiler
endif

.PHONY: build-dir
build-dir: $(BUILD_DIR)/src tflite-micro-src $(BUILD_DIR_EXTRA_DEP)
	@echo "build-dir: copying source to build dir"

	$(COPY) $(COMMON_DIR)/*              $(BUILD_DIR)
	$(COPY) $(MLCOMMONS_SRC_DIR)/*       $(BUILD_DIR)/src
	$(COPY) $(SAXON_SRC_DIR)/riscv.h     $(BUILD_DIR)/src
	$(COPY) $(DONUT_SRC_DIR)/donut.*     $(BUILD_DIR)/src
	$(COPY) $(SRC_DIR)/*                 $(BUILD_DIR)/src

ifdef MNv2_BASELINE
	@echo "mnv2_baseline: copying TFLite model"
	@mkdir -p $(BUILD_DIR)/src/models/mnv2
	$(COPY) $(PROJ_DIR)/model/*.tflite $(BUILD_DIR)/src/models/mnv2
endif

ifdef MNv2_BASELINE
	@echo "mnv2_baseline: removing upstream MobileNetV2 application"
	$(RM) $(BUILD_DIR)/src/proj_menu.cc
	$(RM) $(BUILD_DIR)/src/models/mnv2/mnv2.cc
	$(RM) $(BUILD_DIR)/src/models/mnv2/input_*.h
	$(RM) $(BUILD_DIR)/src/models/mnv2/model_mobilenetv2_160_035.h
endif

	$(RM) $(BUILD_DIR)/_*

# Overlay platform / target specific changes.
ifneq ($(wildcard $(COMMON_DIR)/_$(PLATFORM)/$(TARGET)/*),)
	$(COPY) $(COMMON_DIR)/_$(PLATFORM)/$(TARGET)/* $(BUILD_DIR)
endif

.PHONY: litex-software
ifdef NO_CFU
litex-software:
	$(SOC_MK) litex-software
else
litex-software: $(CFU_VERILOG)
	$(SOC_MK) litex-software
endif

TTY_TARGETS := load unit run
.PHONY: $(TTY_TARGETS) prog bitstream run-renode unit-renode

ifneq 'sim' '$(PLATFORM)'
# $(PLATFORM) == 'common_soc' or 'hps'

ifdef NO_CFU

prog:
	@echo "Error: prog is not available for NO_CFU=1 CPU-only build"

bitstream:
	@echo "Error: bitstream is not available for NO_CFU=1 CPU-only build"

synth:
	@echo "Error: synth is not available for NO_CFU=1 CPU-only build"

else

prog: $(CFU_VERILOG)
	$(SOC_MK) prog

bitstream: $(CFU_VERILOG)
	$(SOC_MK) bitstream

synth: $(CFU_VERILOG)
	$(SOC_MK) synth

endif

run-renode: $(SOFTWARE_ELF) renode-scripts
	@echo Running automated test in Renode
	$(BUILD_DIR)/interact.expect r $(RUN_MENU_ITEMS) |& tee $(SOFTWARE_LOG)

unit-renode: $(SOFTWARE_ELF) renode-scripts
	@echo Running unit test in Renode simulation
	$(BUILD_DIR)/interact.expect r $(TEST_MENU_ITEMS) |& tee $(UNITTEST_LOG)

ifeq '1' '$(words $(TTY))'

run: $(SOFTWARE_BIN)
	@echo Running automated pdti8 test on board
	$(BUILD_DIR)/interact.expect $(SOFTWARE_BIN) $(TTY) $(UART_SPEED) |& tee $(SOFTWARE_LOG)

unit: $(SOFTWARE_BIN)
	$(BUILD_DIR)/interact.expect $(SOFTWARE_BIN) $(TTY) $(UART_SPEED) |& tee $(UNITTEST_LOG)

ifeq 'hps' '$(PLATFORM)'

load: $(SOFTWARE_BIN)
	@echo Running interactively on HPS Board
	$(CFU_ROOT)/scripts/hps_prog $(SOFTWARE_BIN) program
	$(LXTERM) --speed 115200 $(TTY)

connect:
	@echo Connecting to HPS Board
	$(LXTERM) --speed 115200 $(TTY)

else

load: $(SOFTWARE_BIN)
	@echo Running interactively on FPGA Board
	# Load hook allows common_soc.py to provide board-specific changes to load.
	$(SOC_MK) load_hook
	@while [ ! -e $(TTY) ]; do echo "Waiting for UART"; sleep 1; done
	$(LXTERM) --speed $(UART_SPEED) $(CRC) --kernel $(SOFTWARE_BIN) $(TTY)

connect:
	@echo Connecting to board
	$(LXTERM) --speed $(UART_SPEED) $(CRC) --kernel $(SOFTWARE_BIN) $(TTY)

endif

else

$(TTY_TARGETS):
	@echo Error: could not determine unique TTY
	@echo TTY possibilities: $(TTY)
	@echo Optionally, manually specify TTY= on the command line

endif

else
# $(PLATFORM) == sim

load: $(CFU_VERILOG) $(SOFTWARE_BIN)
	$(SIM_MK) run

run: $(SOFTWARE_BIN)
	@echo Running automated test in Verilator simulation
	$(BUILD_DIR)/interact.expect s $(RUN_MENU_ITEMS) |& tee $(SOFTWARE_LOG)

unit: $(SOFTWARE_BIN)
	@echo Running unit test in Verilator simulation
	$(BUILD_DIR)/interact.expect s $(TEST_MENU_ITEMS) |& tee $(SOFTWARE_LOG)

prog bitstream:
	@echo Target not supported when PLATFORM=sim

endif

.PHONY: pytest
pytest:
	$(PYRUN) -m unittest discover -p ${PYTEST_PATTERN}