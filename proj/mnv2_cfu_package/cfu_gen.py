# Copyright 2021 The CFU-Playground Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# Generate the Verilog CFU from the vendored MobileNetV2 Amaranth design.

import os.path
from amaranth.back import verilog

from gateware.mnv2_cfu import make_cfu

VERILOG_FILENAME = "cfu.v"


def read_file():
    if os.path.exists(VERILOG_FILENAME):
        with open(VERILOG_FILENAME, "r") as f:
            return f.read()
    return None


def main():
    cfu = make_cfu()
    new_verilog = verilog.convert(cfu, name="Cfu", ports=cfu.ports)
    old_verilog = read_file()
    if new_verilog != old_verilog:
        with open(VERILOG_FILENAME, "w") as f:
            f.write(new_verilog)


if __name__ == "__main__":
    main()
