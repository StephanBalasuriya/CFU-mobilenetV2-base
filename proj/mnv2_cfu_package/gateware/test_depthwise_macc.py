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
