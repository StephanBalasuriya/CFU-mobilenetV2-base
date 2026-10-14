#!/bin/sh
# Downloads 1000 real ImageNet photos (one per class, ~110 MB) to use as calibration data for tools/percentile_calibrate.py.
# Source: https://github.com/EliSchwartz/imagenet-sample-images   (use your own varied photos if you prefer: 200+ of them)
set -e
mkdir -p calibration_photos && cd calibration_photos
curl -L -o imnet.zip https://codeload.github.com/EliSchwartz/imagenet-sample-images/zip/refs/heads/master
unzip -q imnet.zip && rm imnet.zip
echo "photos in: $(pwd)/imagenet-sample-images-master   ->  python3 tools/percentile_calibrate.py --int8 ... --images that_folder --out ..."
