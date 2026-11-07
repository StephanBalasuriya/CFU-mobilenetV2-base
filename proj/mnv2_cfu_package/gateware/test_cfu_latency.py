# Directed latency test: cycles from instruction issue (cmd_valid) to
# response (rsp_valid), counting the issue cycle as 1, through the real
# CFU interface. These values back Table I of the paper.
from amaranth_cfu import CfuTestBase, pack_vals

from .mnv2_cfu import make_cfu


class CfuLatencyTest(CfuTestBase):
    def create_dut(self):
        return make_cfu()

    def test_depthwise_instruction_latency(self):
        measured = {}

        def issue(funct7, in0=0, in1=0):
            d = self.dut
            yield d.cmd_function_id.eq((funct7 << 3) | 0)
            yield d.cmd_in0.eq(in0 & 0xffffffff)
            yield d.cmd_in1.eq(in1 & 0xffffffff)
            yield d.cmd_valid.eq(1)
            yield d.rsp_ready.eq(1)
            cycles = 1
            yield
            while not (yield d.cmd_ready):
                yield
            yield d.cmd_valid.eq(0)
            while not (yield d.rsp_valid):
                yield
                cycles += 1
            yield d.rsp_ready.eq(0)
            yield
            return cycles

        def process():
            yield from issue(43, 128, 0)  # warm-up
            measured['CONFIGURE'] = yield from issue(43, 128, 0)
            measured['LOAD'] = yield from issue(
                40, pack_vals(1, 2, 3, 4), pack_vals(1, 1, 1, 1))
            yield from issue(
                40, pack_vals(1, 2, 3, 4), pack_vals(1, 1, 1, 1))
            yield from issue(
                40, pack_vals(1, 0, 0, 0), pack_vals(1, 0, 0, 0))
            measured['RUN_after_LOAD'] = yield from issue(41)
            measured['GET_RESULT'] = yield from issue(42)
            measured['SHIFT_RIGHT'] = yield from issue(
                44, pack_vals(1, 2, 3, 0))
            measured['RUN_after_SHIFT'] = yield from issue(41)

        self.run_sim(process, False)
        self.assertEqual(measured, {
            'CONFIGURE': 1, 'LOAD': 1, 'RUN_after_LOAD': 4,
            'GET_RESULT': 1, 'SHIFT_RIGHT': 1, 'RUN_after_SHIFT': 5,
        })
