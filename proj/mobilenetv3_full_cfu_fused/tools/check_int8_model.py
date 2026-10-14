#!/usr/bin/env python3
"""
check_int8_model.py -- classify images with an int8 TFLite classifier (reference interpreter, same preprocessing as the
firmware) and report whether the classification head is SATURATED.

    python3 check_int8_model.py model.tflite --labels labels.txt  img1.jpg img2.jpg ...
    python3 check_int8_model.py model.tflite --labels labels.txt  --dir some_folder

Preprocessing = what the firmware / webcam program sends: the image squashed to 224x224 (bilinear), raw 0..255 bytes,
converted to int8 by -128 (the model contains its own rescaling).  --crop uses resize-256 + centre-crop-224 instead.

For every image it prints the top-5 and the logits just before the softmax.  If several classes sit at the largest
int8 value (q = 127) the model is clipping its confident predictions (calibration range too small): they become an
exact tie after the softmax.  Fix: tools/fix_logits_range.py (quick) or tools/quantize_mobilenetv3_keras.py (proper).

Needs: pip install ai-edge-litert tflite flatbuffers numpy pillow   (tflite_runtime / tensorflow also work)
"""
import argparse, glob, os, sys
import numpy as np
from PIL import Image
import tflite

def load_interpreter(path):
    for mod in ("ai_edge_litert.interpreter", "tflite_runtime.interpreter", "tensorflow.lite"):
        try:
            m = __import__(mod, fromlist=["Interpreter"])
            return m.Interpreter(model_path=path, experimental_preserve_all_tensors=True)
        except ImportError:
            continue
    sys.exit("no TFLite interpreter found: pip install ai-edge-litert")

def prep(path, crop):
    im = Image.open(path).convert("RGB")
    if crop:
        w, h = im.size; s = 256.0 / min(w, h)
        im = im.resize((round(w * s), round(h * s)), Image.BILINEAR)
        w, h = im.size; l = (w - 224) // 2; t = (h - 224) // 2
        im = im.crop((l, t, l + 224, t + 224))
    else:
        im = im.resize((224, 224), Image.BILINEAR)
    return np.asarray(im)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model"); ap.add_argument("images", nargs="*")
    ap.add_argument("--dir"); ap.add_argument("--labels"); ap.add_argument("--crop", action="store_true")
    a = ap.parse_intermixed_args()
    paths = list(a.images) + (sorted(glob.glob(os.path.join(a.dir, "*"))) if a.dir else [])
    if not paths:
        sys.exit("give some images (or --dir)")
    labels = [l.strip().split(": ", 1)[-1] for l in open(a.labels)] if a.labels else []
    name = lambda i: labels[i] if i < len(labels) else str(i)

    buf = open(a.model, "rb").read()
    m = tflite.Model.GetRootAsModel(buf, 0); g = m.Subgraphs(0)
    sm_in = g.Operators(g.OperatorsLength() - 1).Inputs(0)          # tensor feeding the last op (the SOFTMAX)
    it = load_interpreter(a.model); it.allocate_tensors()
    det = {t["index"]: t for t in it.get_tensor_details()}
    sc, zp = det[sm_in]["quantization"]
    print("logits tensor before the softmax: scale %.4f zero point %d -> represents %.2f .. %.2f"
          % (sc, zp, (-128 - zp) * sc, (127 - zp) * sc))
    inp = it.get_input_details()[0]["index"]; outp = it.get_output_details()[0]["index"]
    bad = 0
    for p in paths:
        try:
            x = prep(p, a.crop)
        except Exception as e:
            print("skip %s (%s)" % (p, e)); continue
        it.set_tensor(inp, (x.astype(np.int16) - 128).astype(np.int8)[None]); it.invoke()
        o = it.get_tensor(outp)[0].astype(np.int32)
        lg = it.get_tensor(sm_in).reshape(-1).astype(np.int32)
        top = np.argsort(-o, kind="stable")[:5]
        at_max = int((lg == lg.max()).sum()) if lg.max() == 127 else 0
        ties = int((o == o.max()).sum())
        print("\n%s" % os.path.basename(p))
        print("   top-5: " + ", ".join("%d %s %.3f" % (i, name(i), (o[i] + 128) / 256.0) for i in top))
        print("   logits %+.2f .. %+.2f   classes at the top of the int8 range: %d   classes tied for #1: %d"
              % ((lg.min() - zp) * sc, (lg.max() - zp) * sc, at_max, ties))
        if at_max > 1 or ties > 1:
            bad += 1
    print("\n%s" % ("SATURATED / TIED on %d of %d images: the head clips confident predictions -> fix_logits_range.py or re-quantise"
                    % (bad, len(paths)) if bad else "no saturation or ties on these images"))

if __name__ == "__main__":
    main()
