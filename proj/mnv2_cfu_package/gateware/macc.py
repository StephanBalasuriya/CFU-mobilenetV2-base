#!/bin/env python
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from amaranth import Array, Cat, Mux, Signal, signed

from amaranth_cfu import all_words, SimpleElaboratable, tree_sum

from .delay import Delayer
from .post_process import PostProcessor
from .registerfile import Xetter


class Depthwise3x3Mac(SimpleElaboratable):
    """Explicit 3x3 signed INT8 depthwise MAC datapath.

    Three packed words are loaded for inputs and weights.  The first two
    words contain four bytes and the last word contains the final byte.
    """

    def __init__(self):
        super().__init__()
        self.load = Signal()
        self.load_input = Signal(32)
        self.load_weight = Signal(32)
        self.configure = Signal()
        self.input_offset = Signal(signed(9))
        self.weight_offset = Signal(signed(9))
        self.run = Signal()
        self.result = Signal(signed(32))

    def elab(self, m):
        input_words = Array(Signal(32, name=f"dw_input_{n}") for n in range(3))
        weight_words = Array(Signal(32, name=f"dw_weight_{n}") for n in range(3))
        load_index = Signal(range(3))
        input_offset = Signal(signed(9))
        weight_offset = Signal(signed(9))
        result = Signal(signed(32))

        m.d.comb += self.result.eq(result)
        with m.If(self.configure):
            m.d.sync += [
                input_offset.eq(self.input_offset),
                weight_offset.eq(self.weight_offset),
                load_index.eq(0),
            ]
        with m.Elif(self.load):
            with m.Switch(load_index):
                for index in range(3):
                    with m.Case(index):
                        m.d.sync += [
                            input_words[index].eq(self.load_input),
                            weight_words[index].eq(self.load_weight),
                        ]
            m.d.sync += load_index.eq(Mux(load_index == 2, 0, load_index + 1))

        products = []
        for word_index, (input_word, weight_word) in enumerate(
                zip(input_words, weight_words)):
            for byte_index, (input_byte, weight_byte) in enumerate(zip(
                    all_words(input_word, 8), all_words(weight_word, 8))):
                if word_index == 2 and byte_index > 0:
                    continue
                input_value = Signal(signed(10))
                weight_value = Signal(signed(10))
                product = Signal(signed(20))
                m.d.comb += [
                    input_value.eq(input_byte.as_signed() + input_offset),
                    weight_value.eq(weight_byte.as_signed() + weight_offset),
                    product.eq(input_value * weight_value),
                ]
                products.append(product)

        mac_result = tree_sum(products)
        with m.If(self.run):
            m.d.sync += result.eq(mac_result)


class Madd4Pipeline(SimpleElaboratable):
    """A 4-wide Multiply Add pipeline.

    Pipeline takes 2 additional cycles.

    f_data and i_data each contain 4 signed 8 bit values. The
    calculation performed is:

    result = sum((i_data[n] + offset) * f_data[n] for n in range(4))

    Public Interface
    ----------------
    offset: Signal(signed(8)) input
        Offset to be added to all inputs.
    f_data: Signal(32) input
        4 bytes of filter data to use next
    i_data: Signal(32) input
        4 bytes of input data data to use next
    result: Signal(signed(32)) output
        Result of the multiply and add
    """
    PIPELINE_CYCLES = 2

    def __init__(self):
        super().__init__()
        self.offset = Signal(signed(9))
        self.f_data = Signal(32)
        self.i_data = Signal(32)
        self.result = Signal(signed(32))

    def elab(self, m):
        # Product is 17 bits: 8 bits * 9 bits = 17 bits
        products = [Signal(signed(17), name=f"product_{n}") for n in range(4)]
        for i_val, f_val, product in zip(
                all_words(self.i_data, 8), all_words(self.f_data, 8), products):
            f_tmp = Signal(signed(9))
            m.d.sync += f_tmp.eq(f_val.as_signed())
            i_tmp = Signal(signed(9))
            m.d.sync += i_tmp.eq(i_val.as_signed() + self.offset)
            m.d.comb += product.eq(i_tmp * f_tmp)

        m.d.sync += self.result.eq(tree_sum(products))


class Accumulator(SimpleElaboratable):
    """An accumulator for a Madd4Pipline

    Public Interface
    ----------------
    add_en: Signal() input
        When to add the input
    in_value: Signal(signed(32)) input
        The input data to add
    clear: Signal() input
        Zero accumulator.
    result: Signal(signed(32)) output
        Result of the multiply and add
    """

    def __init__(self):
        super().__init__()
        self.add_en = Signal()
        self.in_value = Signal(signed(32))
        self.clear = Signal()
        self.result = Signal(signed(32))

    def elab(self, m):
        accumulator = Signal(signed(32))
        m.d.comb += self.result.eq(accumulator)
        with m.If(self.add_en):
            m.d.sync += accumulator.eq(accumulator + self.in_value)
            m.d.comb += self.result.eq(accumulator + self.in_value)
        # clear always resets accumulator next cycle, even if add_en is high
        with m.If(self.clear):
            m.d.sync += accumulator.eq(0)


class ByteToWordShifter(SimpleElaboratable):
    """Shifts bytes into a word.

    Bytes are shifted from high to low, so that result is little-endian,
    with the "first" byte occupying the LSBs

    Public Interface
    ----------------
    shift_en: Signal() input
        When to shift the input
    in_value: Signal(8) input
        The input data to shift
    result: Signal(32) output
        Result of the shift
    """

    def __init__(self):
        super().__init__()
        self.shift_en = Signal()
        self.in_value = Signal(8)
        self.clear = Signal()
        self.result = Signal(32)

    def elab(self, m):
        register = Signal(32)
        m.d.comb += self.result.eq(register)

        with m.If(self.shift_en):
            calc = Signal(32)
            m.d.comb += [
                calc.eq(Cat(register[8:], self.in_value)),
                self.result.eq(calc),
            ]
            m.d.sync += register.eq(calc)
