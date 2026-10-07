import random

from amaranth_cfu import TestBase

from .macc import Depthwise3x3Mac


class Depthwise3x3MacTest(TestBase):
    def create_dut(self):
        return Depthwise3x3Mac()

    def test_vectors(self):
        vectors = [
            ([1] * 9, [2] * 9, 0, 0),
            ([-1, 2, -3, 4, -5, 6, -7, 8, -9],
             [9, -8, 7, -6, 5, -4, 3, -2, 1], 0, 0),
            ([0] * 9, [127] * 9, 0, 0),
            ([-128] * 9, [-128] * 9, 0, 0),
            ([127] * 9, [-128] * 9, 3, -2),
        ]

        def pack(values):
            return sum((value & 0xff) << (8 * index)
                       for index, value in enumerate(values))

        def process():
            for inputs, weights, input_offset, weight_offset in vectors:
                yield self.dut.configure.eq(1)
                yield self.dut.input_offset.eq(input_offset)
                yield self.dut.weight_offset.eq(weight_offset)
                yield
                yield self.dut.configure.eq(0)
                for start in (0, 4, 8):
                    yield self.dut.load.eq(1)
                    yield self.dut.load_input.eq(pack(inputs[start:start + 4]))
                    yield self.dut.load_weight.eq(pack(weights[start:start + 4]))
                    yield
                yield self.dut.load.eq(0)
                yield self.dut.run.eq(1)
                yield
                yield self.dut.run.eq(0)

                # Wait for the pipelined accumulation to finish
                while not (yield self.dut.done):
                    yield

                expected = sum(
                    (x + input_offset) * (w + weight_offset)
                    for x, w in zip(inputs, weights))
                self.assertEqual((yield self.dut.result), expected)

        self.run_sim(process, False)


def pack(values):
    return sum((value & 0xff) << (8 * index)
               for index, value in enumerate(values))


def window_at(image, x):
    """3x3 window (row-major) of a 3-row image starting at column x."""
    return [image[row][x + col] for row in range(3) for col in range(3)]


class Depthwise3x3ShiftRightTest(TestBase):
    def create_dut(self):
        return Depthwise3x3Mac()

    # -- helpers ----------------------------------------------------------

    def configure(self, input_offset, weight_offset):
        yield self.dut.configure.eq(1)
        yield self.dut.input_offset.eq(input_offset)
        yield self.dut.weight_offset.eq(weight_offset)
        yield
        yield self.dut.configure.eq(0)

    def load(self, inputs, weights):
        for start in (0, 4, 8):
            yield self.dut.load.eq(1)
            yield self.dut.load_input.eq(pack(inputs[start:start + 4]))
            yield self.dut.load_weight.eq(pack(weights[start:start + 4]))
            yield
        yield self.dut.load.eq(0)

    def shift_right(self, column):
        yield self.dut.shift.eq(1)
        yield self.dut.shift_column.eq(pack(column))
        yield
        yield self.dut.shift.eq(0)

    def run_and_wait(self):
        """Returns (result, cycles from RUN issue until done)."""
        yield self.dut.run.eq(1)
        yield
        yield self.dut.run.eq(0)
        cycles = 1
        while not (yield self.dut.done):
            yield
            cycles += 1
        return ((yield self.dut.result), cycles)

    def read_window(self, signals):
        yield  # let the last sync update become visible
        values = []
        for s in signals:
            values.append((yield s))
        return values

    # -- tests ------------------------------------------------------------

    def test_shift_right_updates_window_only(self):
        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        weights = [9, -8, 7, -6, 5, -4, 3, -2, 1]

        def process():
            yield from self.configure(0, 0)
            yield from self.load(inputs, weights)
            self.assertEqual(
                (yield from self.read_window(self.dut.input_window)), inputs)
            self.assertEqual(
                (yield from self.read_window(self.dut.weight_window)), weights)

            yield from self.shift_right([10, 11, 12])
            self.assertEqual(
                (yield from self.read_window(self.dut.input_window)),
                [2, 3, 10, 5, 6, 11, 8, 9, 12])
            self.assertEqual(
                (yield from self.read_window(self.dut.weight_window)), weights)

            result, _ = yield from self.run_and_wait()
            expected = sum(x * w for x, w in zip(
                [2, 3, 10, 5, 6, 11, 8, 9, 12], weights))
            self.assertEqual(result, expected)

        self.run_sim(process, False)

    def test_sliding_row_signed_with_offsets(self):
        """LOAD first window, then SHIFT_RIGHT across a row of signed data."""
        rng = random.Random(1234)
        cases = [
            (0, 0),
            (128, 0),     # typical MNV2 input offset (zero point -128)
            (-5, 0),
            (3, -2),
            (255, -255),  # extremes of the signed(9) offsets
        ]
        width = 10
        rows = [
            # deterministic edge values
            [[-128] * width, [127] * width, [-128, 127] * (width // 2)],
        ] + [
            [[rng.randint(-128, 127) for _ in range(width)]
             for _ in range(3)]
            for _ in range(3)
        ]

        def process():
            for input_offset, weight_offset in cases:
                for image in rows:
                    weights = [rng.randint(-128, 127) for _ in range(9)]
                    yield from self.configure(input_offset, weight_offset)

                    def expected_at(x):
                        return sum(
                            (i + input_offset) * (w + weight_offset)
                            for i, w in zip(window_at(image, x), weights))

                    yield from self.load(window_at(image, 0), weights)
                    result, _ = yield from self.run_and_wait()
                    self.assertEqual(result, expected_at(0))

                    for x in range(1, width - 2):
                        yield from self.shift_right(
                            [image[row][x + 2] for row in range(3)])
                        result, _ = yield from self.run_and_wait()
                        self.assertEqual(result, expected_at(x), (
                            input_offset, weight_offset, x))
                        # GET_RESULT is a register read: still stable.
                        yield
                        self.assertEqual(
                            (yield self.dut.result), expected_at(x))

        self.run_sim(process, False)

    def test_load_after_shift_and_latency(self):
        """LOAD path keeps its latency; SHIFT adds one refresh cycle."""
        a = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        b = [-9, 8, -7, 6, -5, 4, -3, 2, -1]
        weights = [2, 3, -4, 5, -6, 7, -8, 9, 10]

        def process():
            yield from self.configure(1, 0)
            yield from self.load(a, weights)
            result, load_cycles = yield from self.run_and_wait()
            self.assertEqual(result, sum((x + 1) * w
                                         for x, w in zip(a, weights)))

            yield from self.shift_right([0, 0, 0])
            _, shift_cycles = yield from self.run_and_wait()
            self.assertEqual(shift_cycles, load_cycles + 1)

            # A full LOAD after a SHIFT replaces the window and clears
            # the stale flag, so RUN is back to the original latency.
            yield from self.load(b, weights)
            result, cycles = yield from self.run_and_wait()
            self.assertEqual(result, sum((x + 1) * w
                                         for x, w in zip(b, weights)))
            self.assertEqual(cycles, load_cycles)

            # Repeated RUN without a new SHIFT does not refresh again.
            result2, cycles = yield from self.run_and_wait()
            self.assertEqual(result2, result)
            self.assertEqual(cycles, load_cycles)

        self.run_sim(process, False)
