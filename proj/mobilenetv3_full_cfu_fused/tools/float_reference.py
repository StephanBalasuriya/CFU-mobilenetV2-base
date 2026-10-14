#!/usr/bin/env python3
"""
float_reference.py -- what the FLOAT (not quantised) Keras MobileNetV3-small predicts for an image.
This is the class an int8 version of the same network should come close to; compare with the board / check_int8_model.py.

    python3 float_reference.py photo.jpg [--alpha 0.75] [--labels imagenet_labels.txt]

Same preprocessing as the firmware: image squashed to 224x224 (bilinear), raw 0..255 (the model rescales itself).
Needs: pip install tensorflow pillow numpy   (internet the first time, for the pretrained ImageNet weights)
"""
import argparse
import numpy as np
from PIL import Image
import tensorflow as tf

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("image"); ap.add_argument("--alpha", type=float, default=0.75)
ap.add_argument("--minimalistic", action="store_true"); ap.add_argument("--labels")
ap.add_argument("--weights", default="imagenet")
a = ap.parse_args()
labels = [l.strip().split(": ", 1)[-1] for l in open(a.labels)] if a.labels else []
model = tf.keras.applications.MobileNetV3Small(input_shape=(224, 224, 3), alpha=a.alpha, minimalistic=a.minimalistic,
                                               weights=None if a.weights == "none" else "imagenet",
                                               include_preprocessing=True)
x = np.asarray(Image.open(a.image).convert("RGB").resize((224, 224), Image.BILINEAR), dtype=np.float32)[None]
p = model.predict(x, verbose=0)[0]
for k, i in enumerate(np.argsort(-p)[:5]):
    print("#%d  %4d  %-28s %.3f" % (k + 1, i, labels[i] if i < len(labels) else "", p[i]))
