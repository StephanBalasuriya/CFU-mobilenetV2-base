#!/usr/bin/env python3
"""
fix_logits_range.py -- repair a saturated classification head of an int8 TFLite model WITHOUT retraining.

Problem it fixes: the logits (the output of the last 1x1 conv / FC, just before the SOFTMAX) are stored as int8 with a
range that was measured during calibration.  If that range was too narrow, every confident prediction is CLIPPED at
the largest int8 value (q = 127); several classes then look identical and the int8 softmax turns them into an exact tie
(the firmware prints the lowest class index among the tied ones).  tools/check_int8_model.py shows whether a model has
this problem.

What it does: it sets a wider quantisation range [lo, hi] on the logits tensor and on the reshape-like tensors that
must share its parameters.  Weights and biases stay valid (they only depend on the layer's INPUT scale); the runtime
derives the layer's output multiplier from the tensor scales when the model is loaded, so the layer simply stops
clipping.  The price is a coarser step ((hi-lo)/255), so do not make the range much wider than needed.

    python3 fix_logits_range.py in.tflite out.tflite                 # default range [-8, 16]
    python3 fix_logits_range.py in.tflite out.tflite --lo -6 --hi 12

Superseded by tools/percentile_calibrate.py, which fixes the whole network (this tool only repairs the last layer).
Needs:  pip install tflite flatbuffers numpy
"""
import argparse, sys
import numpy as np
import tflite

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--lo", type=float, default=-8.0, help="smallest logit to represent (default -8)")
    ap.add_argument("--hi", type=float, default=16.0, help="largest logit to represent (default 16)")
    a = ap.parse_args()

    buf = bytearray(open(a.src, "rb").read())
    m = tflite.Model.GetRootAsModel(buf, 0)
    g = m.Subgraphs(0)
    codes = [max(m.OperatorCodes(i).BuiltinCode(), m.OperatorCodes(i).DeprecatedBuiltinCode()) for i in range(m.OperatorCodesLength())]
    B = tflite.BuiltinOperator
    def opcode(op): return codes[op.OpcodeIndex()]
    producers = {}
    for i in range(g.OperatorsLength()):
        op = g.Operators(i)
        for j in range(op.OutputsLength()):
            producers[op.Outputs(j)] = op

    # the SOFTMAX feeding the model output
    out = g.Outputs(0)
    sm = producers.get(out)
    if sm is None or opcode(sm) != B.SOFTMAX:
        sys.exit("the model output is not produced by a SOFTMAX; nothing to fix")
    # walk back through reshape-like ops (they share quantisation) to the layer that really computes the logits
    chain = [sm.Inputs(0)]
    while True:
        p = producers[chain[-1]]
        if opcode(p) in (B.RESHAPE, B.SQUEEZE, B.EXPAND_DIMS):
            chain.append(p.Inputs(0))
        else:
            break
    last = producers[chain[-1]]
    if opcode(last) not in (B.CONV_2D, B.FULLY_CONNECTED):
        sys.exit("expected the logits to come from a CONV_2D / FULLY_CONNECTED, found %s" % opcode(last))

    def params(t):
        q = g.Tensors(t).Quantization()
        return q.Scale(0), q.ZeroPoint(0)
    s0, z0 = params(chain[0])
    scale = (a.hi - a.lo) / 255.0
    zp = int(round(-128 - a.lo / scale))
    zp = max(-128, min(127, zp))
    print("logits tensors: %s" % chain)
    print("old: scale %.5f zero point %d  -> represents %.2f .. %.2f" % (s0, z0, (-128 - z0) * s0, (127 - z0) * s0))
    for t in chain:
        q = g.Tensors(t).Quantization()
        if q.ScaleLength() != 1:
            sys.exit("per-channel quantised logits are not supported")
        sc_w = np.frombuffer(buf, dtype=np.float32, count=1, offset=q._tab.Vector(q._tab.Offset(8)))   # QuantizationParameters.scale
        zp_w = np.frombuffer(buf, dtype=np.int64, count=1, offset=q._tab.Vector(q._tab.Offset(10)))    # .zero_point
        sc_w[0] = scale
        zp_w[0] = zp
    open(a.dst, "wb").write(buf)
    m2 = tflite.Model.GetRootAsModel(bytes(buf), 0); g2 = m2.Subgraphs(0)
    q = g2.Tensors(chain[0]).Quantization()
    print("new: scale %.5f zero point %d  -> represents %.2f .. %.2f" % (q.Scale(0), q.ZeroPoint(0),
          (-128 - q.ZeroPoint(0)) * q.Scale(0), (127 - q.ZeroPoint(0)) * q.Scale(0)))
    print("wrote %s" % a.dst)

if __name__ == "__main__":
    main()
