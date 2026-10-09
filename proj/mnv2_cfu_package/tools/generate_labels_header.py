#!/usr/bin/env python3

import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate_labels_header.py LABELS OUTPUT")

    labels_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    labels = []

    for line_number, line in enumerate(
        labels_path.read_text(encoding="utf-8").splitlines(), 1
    ):
        index_text, separator, label = line.partition(": ")
        if not separator or int(index_text) != len(labels) or not label:
            raise ValueError(f"invalid label at line {line_number}")
        labels.append(label)

    if len(labels) != 1000:
        raise ValueError(f"expected 1000 labels, found {len(labels)}")

    output_path.write_text(
        "#ifndef IMAGENET_LABELS_H\n"
        "#define IMAGENET_LABELS_H\n\n"
        "static const char* const kImageNetLabels[] = {\n"
        + "".join(f'    "{label}",\n' for label in labels)
        + "};\n\n"
        "static const int kImageNetLabelCount =\n"
        "    sizeof(kImageNetLabels) / sizeof(kImageNetLabels[0]);\n\n"
        "#endif\n",
        encoding="ascii",
    )


if __name__ == "__main__":
    main()