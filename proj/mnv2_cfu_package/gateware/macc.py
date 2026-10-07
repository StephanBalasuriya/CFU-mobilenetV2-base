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

    Three packed words are loaded for inputs and weights.
    The first two words contain four bytes and the last word
    contains the final byte.

    Products are registered during LOAD.

    RUN starts a 3-stage pipelined accumulation:
        Stage 1: pairwise sums
        Stage 2: partial sums
        Stage 3: final sum

    The DONE signal is asserted only when the final result is ready.

    Sliding window (stride-1 horizontal reuse):
        LOAD also records the offset-applied input and weight values
        in input_window / weight_window (row-major, index = y*3 + x).

        SHIFT_RIGHT shifts every input row left by one and inserts
        shift_column bytes [7:0], [15:8], [23:16] as the new right
        column of rows 0, 1, 2. Weights are unchanged. SHIFT_RIGHT
        only updates registers and marks the products stale.

        If products are stale, RUN spends one extra cycle recomputing
        all nine products from the window registers before entering
        the unchanged 3-stage accumulation.
    """

    def __init__(self):
        super().__init__()

        self.load = Signal()
        self.load_input = Signal(32)
        self.load_weight = Signal(32)

        self.configure = Signal()
        self.input_offset = Signal(signed(9))
        self.weight_offset = Signal(signed(9))

        self.shift = Signal()
        self.shift_column = Signal(32)

        self.run = Signal()
        self.result = Signal(signed(32))

        # Offset-applied window values, row-major (index = y*3 + x).
        self.input_window = [
            Signal(signed(10), name=f"dw_input_window_{n}")
            for n in range(9)
        ]
        self.weight_window = [
            Signal(signed(10), name=f"dw_weight_window_{n}")
            for n in range(9)
        ]

        # Asserted when a RUN operation has completed.
        self.done = Signal()

    def elab(self, m):
        load_index = Signal(range(3))

        input_offset = Signal(signed(9))
        weight_offset = Signal(signed(9))

        # ------------------------------------------------------------
        # Registered products
        # ------------------------------------------------------------

        product_regs = [
            Signal(signed(20), name=f"dw_product_{n}")
            for n in range(9)
        ]

        # ------------------------------------------------------------
        # Pipelined accumulation registers
        # ------------------------------------------------------------

        # Stage 1:
        #   P0 + P1
        #   P2 + P3
        #   P4 + P5
        #   P6 + P7
        #   P8 passes through
        stage1 = [
            Signal(signed(21), name=f"dw_sum1_{n}")
            for n in range(5)
        ]

        # Stage 2:
        #   S0 + S1
        #   S2 + S3
        #   S4 passes through
        stage2 = [
            Signal(signed(22), name=f"dw_sum2_{n}")
            for n in range(3)
        ]

        # Final accumulated result.
        result = Signal(signed(32))

        # Pipeline state:
        #
        # 0 = idle
        # 1 = stage 1 completed
        # 2 = stage 2 completed
        # 3 = final result completed / done
        # 4 = products refreshed from window (only after SHIFT_RIGHT)
        pipeline_state = Signal(range(5))

        # Set by SHIFT_RIGHT: product_regs no longer match the window.
        products_stale = Signal()

        input_window = self.input_window
        weight_window = self.weight_window

        m.d.comb += [
            self.result.eq(result),
            self.done.eq(pipeline_state == 3),
        ]

        # ------------------------------------------------------------
        # CONFIGURE
        # ------------------------------------------------------------

        with m.If(self.configure):
            m.d.sync += [
                input_offset.eq(self.input_offset),
                weight_offset.eq(self.weight_offset),
                load_index.eq(0),
            ]

        # ------------------------------------------------------------
        # LOAD
        #
        # LOAD 0 -> products 0..3
        # LOAD 1 -> products 4..7
        # LOAD 2 -> product 8
        # ------------------------------------------------------------

        with m.Elif(self.load):

            input_bytes = list(all_words(self.load_input, 8))
            weight_bytes = list(all_words(self.load_weight, 8))

            load_products = []
            load_inputs = []
            load_weights = []

            for byte_index in range(4):

                input_value = Signal(
                    signed(10),
                    name=f"dw_load_input_{byte_index}"
                )

                weight_value = Signal(
                    signed(10),
                    name=f"dw_load_weight_{byte_index}"
                )

                product = Signal(
                    signed(20),
                    name=f"dw_load_product_{byte_index}"
                )

                m.d.comb += [
                    input_value.eq(
                        input_bytes[byte_index].as_signed()
                        + input_offset
                    ),

                    weight_value.eq(
                        weight_bytes[byte_index].as_signed()
                        + weight_offset
                    ),

                    product.eq(
                        input_value * weight_value
                    ),
                ]

                load_products.append(product)
                load_inputs.append(input_value)
                load_weights.append(weight_value)

            with m.Switch(load_index):

                with m.Case(0):
                    m.d.sync += [
                        product_regs[0].eq(load_products[0]),
                        product_regs[1].eq(load_products[1]),
                        product_regs[2].eq(load_products[2]),
                        product_regs[3].eq(load_products[3]),
                    ]
                    m.d.sync += [
                        input_window[n].eq(load_inputs[n])
                        for n in range(4)
                    ]
                    m.d.sync += [
                        weight_window[n].eq(load_weights[n])
                        for n in range(4)
                    ]

                with m.Case(1):
                    m.d.sync += [
                        product_regs[4].eq(load_products[0]),
                        product_regs[5].eq(load_products[1]),
                        product_regs[6].eq(load_products[2]),
                        product_regs[7].eq(load_products[3]),
                    ]
                    m.d.sync += [
                        input_window[4 + n].eq(load_inputs[n])
                        for n in range(4)
                    ]
                    m.d.sync += [
                        weight_window[4 + n].eq(load_weights[n])
                        for n in range(4)
                    ]

                with m.Case(2):
                    m.d.sync += [
                        product_regs[8].eq(load_products[0]),
                        input_window[8].eq(load_inputs[0]),
                        weight_window[8].eq(load_weights[0]),
                        # All nine products now match the window.
                        products_stale.eq(0),
                    ]

            m.d.sync += load_index.eq(
                Mux(
                    load_index == 2,
                    0,
                    load_index + 1
                )
            )

        # ------------------------------------------------------------
        # SHIFT_RIGHT
        #
        # Registers only: each row moves left by one and the new
        # column (plus input offset) enters on the right. Weights
        # are unchanged. Products are recomputed at the next RUN.
        # ------------------------------------------------------------

        with m.Elif(self.shift):

            column_bytes = list(all_words(self.shift_column, 8))

            for row in range(3):
                base = row * 3
                m.d.sync += [
                    input_window[base + 0].eq(input_window[base + 1]),
                    input_window[base + 1].eq(input_window[base + 2]),
                    input_window[base + 2].eq(
                        column_bytes[row].as_signed() + input_offset
                    ),
                ]

            m.d.sync += products_stale.eq(1)

        # ------------------------------------------------------------
        # PIPELINED ACCUMULATION
        # ------------------------------------------------------------

        with m.Else():

            # --------------------------------------------------------
            # Refresh products after SHIFT_RIGHT (one extra cycle)
            # --------------------------------------------------------

            with m.If(
                (pipeline_state == 0) &
                self.run &
                products_stale
            ):
                m.d.sync += [
                    product_regs[n].eq(input_window[n] * weight_window[n])
                    for n in range(9)
                ]
                m.d.sync += [
                    products_stale.eq(0),
                    pipeline_state.eq(4),
                ]

            # --------------------------------------------------------
            # Start pipeline
            # --------------------------------------------------------

            with m.Elif(
                ((pipeline_state == 0) & self.run) |
                (pipeline_state == 4)
            ):
                m.d.sync += [
                    # Stage 1
                    stage1[0].eq(product_regs[0] + product_regs[1]),
                    stage1[1].eq(product_regs[2] + product_regs[3]),
                    stage1[2].eq(product_regs[4] + product_regs[5]),
                    stage1[3].eq(product_regs[6] + product_regs[7]),
                    stage1[4].eq(product_regs[8]),

                    pipeline_state.eq(1),
                ]

            # --------------------------------------------------------
            # Stage 2
            # --------------------------------------------------------

            with m.Elif(pipeline_state == 1):
                m.d.sync += [
                    stage2[0].eq(stage1[0] + stage1[1]),
                    stage2[1].eq(stage1[2] + stage1[3]),
                    stage2[2].eq(stage1[4]),

                    pipeline_state.eq(2),
                ]

            # --------------------------------------------------------
            # Stage 3 / final result
            # --------------------------------------------------------

            with m.Elif(pipeline_state == 2):
                m.d.sync += [
                    result.eq(
                        stage2[0] +
                        stage2[1] +
                        stage2[2]
                    ),

                    pipeline_state.eq(3),
                ]

            # --------------------------------------------------------
            # DONE state
            # --------------------------------------------------------

            with m.Elif(pipeline_state == 3):
                m.d.sync += pipeline_state.eq(0)


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
