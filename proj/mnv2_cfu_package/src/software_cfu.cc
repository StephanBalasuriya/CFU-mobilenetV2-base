/*
 * Copyright 2021 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 */

#include "software_cfu.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "cpp_math.h"
#include "mnv2_cfu.h"

namespace {
int32_t reg_output_depth;
int32_t reg_input_offset;
int32_t reg_output_offset;
int32_t reg_activation_min;
int32_t reg_activation_max;

#define MAX_OUTPUT_DEPTH 512
struct ParamStore {
  int32_t params[MAX_OUTPUT_DEPTH];
  int count;
  int read_index;
};

int32_t reg_output_batch_size;
struct ParamStore output_multiplier;
struct ParamStore output_shift;
struct ParamStore output_bias;

void param_store_restart(struct ParamStore* ps) {
  ps->count = 0;
  ps->read_index = 0;
}

int32_t param_store_set(struct ParamStore* ps, int32_t value) {
  ps->params[ps->count++] = value;
  return 0;
}

int32_t param_store_read(struct ParamStore* ps) {
  int32_t result = ps->params[ps->read_index];
  ps->read_index += 1;
  if (ps->read_index == ps->count) {
    ps->read_index = 0;
  }
  return result;
}

int32_t post_process(int32_t acc) {
  acc += param_store_read(&output_bias);
  acc = cpp_math_mul_by_quantized_mul_software(
      acc, param_store_read(&output_multiplier),
      param_store_read(&output_shift));
  acc += reg_output_offset;
  if (acc < reg_activation_min) {
    acc = reg_activation_min;
  } else if (acc > reg_activation_max) {
    acc = reg_activation_max;
  }
  return acc;
}

struct FilterStore {
  int32_t values[NUM_FILTER_DATA_EBRAMS][NUM_FILTER_DATA_WORDS];
  int write_index;
  int write_bank;
  int read_index;
  int read_bank;
};

struct FilterStore filter_store;

void filter_store_restart(struct FilterStore* fs) {
  fs->write_index = 0;
  fs->write_bank = 0;
  fs->read_index = 0;
  fs->read_bank = 0;
}

uint32_t filter_store_set(struct FilterStore* fs, uint32_t val) {
  fs->values[fs->write_bank][fs->write_index] = val;
  fs->write_bank = (fs->write_bank + 1) % NUM_FILTER_DATA_EBRAMS;
  if (fs->write_bank == 0) {
    fs->write_index = (fs->write_index + 1) % NUM_FILTER_DATA_WORDS;
  }
  return 0;
}

uint32_t filter_store_read(struct FilterStore* fs) {
  uint32_t result = fs->values[fs->read_bank][fs->read_index];
  fs->read_bank = (fs->read_bank + 1) % NUM_FILTER_DATA_EBRAMS;
  if (fs->read_bank == 0) {
    fs->read_index = (fs->read_index + 1) % fs->write_index;
  }
  return result;
}

struct InputStore {
  bool write_allowed[2];
  bool read_allowed[2];
  int curr_read_buffer;
  int curr_write_buffer;
  int32_t values[NUM_INPUT_DATA_EBRAMS][NUM_INPUT_DATA_WORDS];
  uint32_t input_depth;
  uint32_t write_addr;
  uint32_t read_addr;
};

struct InputStore input_store;

void input_store_restart(struct InputStore* is) {
  memset(is, 0, sizeof(struct FilterStore));
  is->write_allowed[0] = true;
  is->write_allowed[1] = true;
}

int32_t input_store_set(struct InputStore* is, uint32_t val) {
  if (!is->write_allowed[is->curr_write_buffer]) {
    printf("could not write\n");
    return 0;
  }

  is->read_allowed[is->curr_write_buffer] = false;

  int bank = is->write_addr & 0x3;
  int w_addr = (is->write_addr >> 2) +
               (is->curr_write_buffer ? EBRAM_DEPTH_WORDS / 2 : 0);
  is->values[bank][w_addr] = val;

  is->write_addr++;
  if (is->write_addr == is->input_depth) {
    is->write_addr = 0;
    is->read_allowed[is->curr_write_buffer] = true;
    is->curr_write_buffer = 1 - is->curr_write_buffer;
    return 1;
  }
  return 0;
}

uint32_t input_store_read(struct InputStore* is) {
  if (!is->read_allowed[is->curr_read_buffer]) {
    printf("could not read\n");
    return 0;
  }

  is->write_allowed[is->curr_read_buffer] = false;

  int bank = is->read_addr & 0x3;
  int r_addr =
      (is->read_addr >> 2) +
      (is->curr_read_buffer ? EBRAM_DEPTH_WORDS / 2 : 0);
  uint32_t result = is->values[bank][r_addr];

  is->read_addr++;
  if (is->read_addr == is->input_depth) {
    is->read_addr = 0;
  }

  return result;
}

uint32_t input_store_mark_read_finished(struct InputStore* is) {
  is->read_addr = 0;
  is->write_allowed[is->curr_read_buffer] = true;
  is->curr_read_buffer = 1 - is->curr_read_buffer;
  return 0;
}

struct OutputQueue {
  uint32_t data[EBRAM_DEPTH_WORDS];
  int r;
  int w;
};

struct OutputQueue output_queue;

uint32_t oq_get(struct OutputQueue* oq) {
  uint32_t result = oq->data[oq->r];
  oq->r = (oq->r + 1) % EBRAM_DEPTH_WORDS;
  return result;
}

void oq_put(struct OutputQueue* oq, uint32_t word) {
  oq->data[oq->w] = word;
  oq->w = (oq->w + 1) % EBRAM_DEPTH_WORDS;
  static int dbg_ctr = 0;
  if (dbg_ctr++ == 0) {
    printf("oqput: 0x%08lx\n", word);
  }
}

inline int32_t macc(const int8_t input_val, int8_t filter_val) {
  return ((int32_t)filter_val) *
         ((int32_t)input_val + reg_input_offset);
}

int32_t macc4(uint32_t input_vals, uint32_t filter_vals) {
  int32_t result = 0;
  result += macc(input_vals & 0xff, filter_vals & 0xff);
  filter_vals >>= 8;
  input_vals >>= 8;
  result += macc(input_vals & 0xff, filter_vals & 0xff);
  filter_vals >>= 8;
  input_vals >>= 8;
  result += macc(input_vals & 0xff, filter_vals & 0xff);
  filter_vals >>= 8;
  input_vals >>= 8;
  result += macc(input_vals & 0xff, filter_vals & 0xff);
  return result;
}

int32_t macc4_run4(struct InputStore* is, struct FilterStore* fs) {
  uint32_t result = 0;
  for (int i = 0; i < 4; i++) {
    int32_t accumulator = 0;
    for (uint32_t j = 0; j < is->input_depth; j++) {
      accumulator += macc4(
          input_store_read(&input_store),
          filter_store_read(&filter_store));
    }
    result = (result >> 8) |
             ((0xff & post_process(accumulator)) << 24);
  }
  return result;
}

uint32_t calc_to_oq(
    struct OutputQueue* oq,
    struct InputStore* is,
    struct FilterStore* fs) {

  for (int i = 0; i < reg_output_batch_size; i += 4) {
    oq_put(
        oq,
        macc4_run4(
            is,
            fs));
  }

  input_store_mark_read_finished(is);

  return 0;
}

uint32_t set_reg(
    int funct7,
    uint32_t in0,
    uint32_t in1) {

  switch (funct7) {

    case 10:
      input_store_restart(&input_store);
      input_store.input_depth = in0;
      return 0;

    case 11:
      reg_output_depth = in0;
      return 0;

    case 12:
      reg_input_offset = in0;
      return 0;

    case 13:
      reg_output_offset = in0;
      return 0;

    case 14:
      reg_activation_min = in0;
      return 0;

    case 15:
      reg_activation_max = in0;
      break;

    case 20:
      reg_output_batch_size = in0;
      param_store_restart(&output_multiplier);
      param_store_restart(&output_shift);
      param_store_restart(&output_bias);
      filter_store_restart(&filter_store);
      break;

    case 21:
      return param_store_set(
          &output_multiplier,
          in0);

    case 22:
      return param_store_set(
          &output_shift,
          in0);

    case 23:
      return param_store_set(
          &output_bias,
          in0);

    case 24:
      return filter_store_set(
          &filter_store,
          in0);

    case 25:
      input_store_set(
          &input_store,
          in0);
      return 0;

    case 33:
      return calc_to_oq(
          &output_queue,
          &input_store,
          &filter_store);

    case 34:
      return oq_get(
          &output_queue);

    default:
      return 0;
  }

  return 0;
}

}  // anonymous namespace

uint32_t software_cfu(
    int funct3,
    int funct7,
    uint32_t in0,
    uint32_t in1) {

  switch (funct3) {

    case 0:
      return set_reg(
          funct7,
          in0,
          in1);

    default:
      return 0;
  }
}
