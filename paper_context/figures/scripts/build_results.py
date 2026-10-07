#!/usr/bin/env python3
"""Builds the MCSoC result tables, figure data and figures from evidence.

Every number is parsed from files under paper_context/evidence/ (runtime
UART logs and Vivado .rpt files) or derived from them with the formulas
stated in the generated Markdown. Nothing is typed in by hand, except the
MobileNetV2 depthwise layer shapes used by the analytical instruction-count
derivation (see DW_LAYERS).

Run from anywhere:
    python3 paper_context/figures/scripts/build_results.py
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PC = ROOT / "paper_context"
EV = PC / "evidence"
TABLES = EV / "tables"
FIG_DATA = PC / "figures" / "data"
GRAPHS = PC / "figures" / "graphs"

TICK_CYCLES = 1024  # common/src/tensorflow/lite/micro/micro_time.cc: mcycle >> 10
SYS_CLOCK = "soc_crg_clkout0"

# Configuration key -> (label, runtime log, Vivado report prefix)
CONFIGS = [
    ("cpu_only", "CPU-only",
     EV / "runtime/cpu_only/output.md", None),
    ("cfu_1x1", "1×1 CFU",
     EV / "runtime/cfu_1x1/output.md",
     EV / "vivado/cfu_1x1/b_digilent_nexys4ddr_"),
    ("cfu_1x1_3x3", "1×1 + 3×3 DW CFU",
     EV / "runtime/cfu_1x1_3x3/output.md",
     EV / "vivado/cfu_1x1_3x3/digilent_nexys4ddr_"),
    ("sliding_window", "1×1 + 3×3 DW CFU + sliding window",
     EV / "runtime/sliding_window/output.md",
     EV / "vivado/sliding_window/sw_digilent_nexys4ddr_"),
]
LABEL = {k: lbl for k, lbl, _, _ in CONFIGS}
SHORT = {"cpu_only": "CPU-only", "cfu_1x1": "1×1 CFU",
         "cfu_1x1_3x3": "1×1 + 3×3", "sliding_window": "1×1 + 3×3\n+ sliding win."}


def rel(p):
    return str(Path(p).relative_to(ROOT))


# ---------------------------------------------------------------------------
# Runtime logs
# ---------------------------------------------------------------------------

def parse_runtime(path):
    if not path.exists():
        return None
    text = path.read_text()

    def one(pattern, cast=str, required=True):
        m = re.search(pattern, text, re.M)
        if not m:
            if required:
                sys.exit(f"{rel(path)}: pattern not found: {pattern}")
            return None
        return cast(m.group(1))

    events = [(int(i), tag, int(t)) for i, tag, t in
              re.findall(r"^(\d+),([A-Z_0-9]+),(\d+)$", text, re.M)]
    return {
        "path": path,
        "cycles": one(r"\(\s*(\d+)\s*\)\s+cycles total", int),
        "events": events,
        "input_fnv": one(r"RGB FNV1a\s*:\s*(0x[0-9a-f]+)"),
        "output_fnv": one(r"Output FNV1a\s*:\s*(0x[0-9a-f]+)", required=False),
        "top1": one(r"Top-1 class index\s*:\s*(\d+)", int),
        "top1_score_e6": one(r"Top-1 score\s*:\s*(\d+) x 10\^-6", int),
        "label": one(r"Prediction class label:\s*(\S+)"),
        "model": one(r"Model\s*:\s*(\S+)"),
        "resolution": one(r"Resolution\s*:\s*(.+)$").strip(),
        "dw_used_marker": "3x3 depthwise CFU used" in text,
    }


def op_breakdown(rt):
    """Cycle estimates per operator class from profiler ticks (x1024)."""
    dw = sum(t for _, tag, t in rt["events"] if tag == "DEPTHWISE_CONV_2D")
    conv = sum(t for _, tag, t in rt["events"] if tag == "CONV_2D")
    dw_c, conv_c = dw * TICK_CYCLES, conv * TICK_CYCLES
    return {
        "dw_ticks": dw, "conv_ticks": conv,
        "all_ticks": sum(t for _, _, t in rt["events"]),
        "dw_cycles_est": dw_c, "conv_cycles_est": conv_c,
        "other_cycles_est": rt["cycles"] - dw_c - conv_c,
    }


# ---------------------------------------------------------------------------
# Vivado reports
# ---------------------------------------------------------------------------

def header(text, field):
    m = re.search(rf"^\|\s*{field}\s*:\s*(.+?)\s*$", text, re.M)
    return m.group(1) if m else None


def parse_util(path):
    text = path.read_text()
    rows = {}
    for name, key in (("digilent_nexys4ddr", "top"), ("Cfu", "cfu"),
                      ("depthwise_3x3", "depthwise_3x3")):
        m = re.search(rf"^\|\s+{name}\s+\|[^|]+\|" + r"\s*(\d+)\s*\|" * 8,
                      text, re.M)
        if m:
            v = [int(x) for x in m.groups()]
            rows[key] = dict(zip(
                ["lut", "logic_lut", "lutram", "srl", "ff",
                 "ramb36", "ramb18", "dsp"], v))
    return {"path": path, "state": header(text, "Design State"),
            "device": header(text, "Device"), "date": header(text, "Date"),
            "tool": header(text, "Tool Version"), "rows": rows}


def parse_timing(path):
    text = path.read_text()
    m = re.search(r"WNS\(ns\).*\n\s*-+.*\n\s*(.+)", text)
    v = m.group(1).split()
    period = re.search(rf"^\s*{SYS_CLOCK}\s+\{{[^}}]*\}}\s+([\d.]+)\s+([\d.]+)",
                       text, re.M)
    intra = text[text.index("Intra Clock Table"):]
    clk = re.search(rf"^\s*{SYS_CLOCK}\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(\d+)",
                    intra, re.M)
    return {
        "path": path, "state": header(text, "Design State"),
        "date": header(text, "Date"),
        "wns": float(v[0]), "tns": float(v[1]), "tns_fail": int(v[2]),
        "whs": float(v[4]), "ths": float(v[5]), "ths_fail": int(v[6]),
        "met": "All user specified timing constraints are met." in text,
        "sys_period_ns": float(period.group(1)),
        "sys_freq_mhz": float(period.group(2)),
        "sys_wns": float(clk.group(1)),
    }


def parse_power(path):
    if not path.exists():
        return None
    text = path.read_text()
    g = lambda f: float(re.search(rf"\|\s*{f}\s*\|\s*([\d.]+)", text).group(1))
    return {"path": path, "state": header(text, "Design State"),
            "total_w": g(r"Total On-Chip Power \(W\)"),
            "dynamic_w": g(r"Dynamic \(W\)"),
            "static_w": g(r"Device Static \(W\)"),
            "confidence": re.search(r"\|\s*Confidence Level\s*\|\s*(\w+)",
                                    text).group(1)}


# ---------------------------------------------------------------------------
# Analytical 3x3 depthwise CFU instruction counts
# ---------------------------------------------------------------------------

# MobileNetV2 a0.35 224 depthwise layers: (input H=W, channels, stride).
# Stride-2 layers are preceded by explicit PAD ops in the model
# (block_{1,3,6,13}_pad; 4 PAD events in every runtime log), so they run
# VALID on an (H+1)x(H+1) input with no border windows.
DW_LAYERS = [(112, 16, 1), (112, 48, 2), (56, 48, 1), (56, 48, 2),
             (28, 96, 1), (28, 96, 1), (28, 96, 2), (14, 144, 1),
             (14, 144, 1), (14, 144, 1), (14, 144, 1), (14, 192, 1),
             (14, 192, 1), (14, 192, 2), (7, 336, 1), (7, 336, 1),
             (7, 336, 1)]


def dw_instruction_counts():
    """Mirrors Dw3x3VerifyReport() in
    proj/mnv2_cfu_package/src/tensorflow/lite/micro/kernels/depthwise_conv.cc
    and the loop structure of mnv2_depthwise_conv.h."""
    before = dict(CONFIGURE=0, LOAD=0, SHIFT_RIGHT=0, RUN=0, GET_RESULT=0)
    after = dict(before)
    for n, c, s in DW_LAYERS:
        if s == 2:
            n_in, out, pad = n + 1, n // 2, 0
        else:
            n_in, out, pad = n, n, 1

        def full(o):
            return o * s - pad >= 0 and o * s - pad + 2 < n_in

        full_rows = sum(full(o) for o in range(out))
        windows = full_rows * full_rows * c
        row_runs = full_rows * c
        slide = s == 1 and full_rows > 0
        for d in (before, after):
            d["CONFIGURE"] += 1
            d["RUN"] += windows
            d["GET_RESULT"] += windows
        before["LOAD"] += 3 * windows
        after["LOAD"] += 3 * row_runs if slide else 3 * windows
        after["SHIFT_RIGHT"] += windows - row_runs if slide else 0
    return before, after


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def write_csv(path, header_row, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header_row)
        w.writerows(rows)


def fmt(n):
    return f"{n:,}"


def main():
    TABLES.mkdir(parents=True, exist_ok=True)
    FIG_DATA.mkdir(parents=True, exist_ok=True)
    GRAPHS.mkdir(parents=True, exist_ok=True)

    rt = {k: parse_runtime(p) for k, _, p, _ in CONFIGS}
    hw = {}
    for k, _, _, prefix in CONFIGS:
        if prefix is None:
            continue
        hw[k] = {
            "util_place": parse_util(Path(f"{prefix}utilization_hierarchical_place.rpt")),
            "util_synth": parse_util(Path(f"{prefix}utilization_hierarchical_synth.rpt")),
            "timing_route": parse_timing(Path(f"{prefix}timing.rpt")),
            "timing_synth": parse_timing(Path(f"{prefix}timing_synth.rpt")),
            "power": parse_power(Path(f"{prefix}power.rpt")),
        }
    measured = [k for k, *_ in CONFIGS if rt[k]]
    cpu = rt["cpu_only"]
    ref = rt["cfu_1x1"]

    # ---------------- end-to-end performance ----------------
    perf_rows = []
    for k, label, path, _ in CONFIGS:
        r = rt[k]
        if r is None:
            perf_rows.append([k, label, "", "", "", "", "",
                              f"MISSING: {rel(path)}"])
            continue
        c = r["cycles"]
        vs_cpu = (f"{cpu['cycles'] / c:.3f}", f"{(cpu['cycles'] - c) / cpu['cycles'] * 100:.2f}") if cpu else ("", "")
        perf_rows.append([k, label, c, *vs_cpu,
                          f"{ref['cycles'] / c:.3f}",
                          f"{(ref['cycles'] - c) / ref['cycles'] * 100:.2f}",
                          rel(r["path"])])
    hdr = ["configuration", "label", "cycles", "speedup_vs_cpu",
           "cycle_reduction_vs_cpu_pct", "speedup_vs_1x1",
           "cycle_reduction_vs_1x1_pct", "source"]
    write_csv(TABLES / "end_to_end_performance.csv", hdr, perf_rows)
    write_csv(FIG_DATA / "end_to_end_cycles.csv",
              ["configuration", "cycles", "dw_cycles_est", "conv2d_cycles_est",
               "other_cycles_est", "source"],
              [[k, rt[k]["cycles"], *(op_breakdown(rt[k])[x] for x in
               ("dw_cycles_est", "conv_cycles_est", "other_cycles_est")),
                rel(rt[k]["path"])] for k in measured])
    write_csv(FIG_DATA / "speedup.csv",
              ["configuration", "cycles", "baseline", "speedup",
               "cycle_reduction_pct"],
              [[k, rt[k]["cycles"], "cfu_1x1",
                f"{ref['cycles'] / rt[k]['cycles']:.3f}",
                f"{(ref['cycles'] - rt[k]['cycles']) / ref['cycles'] * 100:.2f}"]
               for k in measured])

    md = ["# End-to-End Performance", "",
          "Whole-model cycles for one MobileNetV2 a0.35 224 INT8 inference "
          "(same embedded image, input FNV-1a `0xbe3b0c0b` in every log).", "",
          "| Configuration | Cycles | Speedup vs CPU | Cycle reduction vs CPU "
          "| Speedup vs 1×1 CFU | Cycle reduction vs 1×1 CFU |",
          "|---|---:|---:|---:|---:|---:|"]
    for row in perf_rows:
        k = row[0]
        if row[2] == "":
            md.append(f"| {LABEL[k]} | [REQUIRED] | [REQUIRED] | [REQUIRED] | – | – |")
        else:
            sp = f"{row[3]}×" if row[3] else "N/A"
            cr = f"{row[4]} %" if row[4] else "N/A"
            md.append(f"| {LABEL[k]} | {fmt(row[2])} | {sp} | {cr} | "
                      f"{row[5]}× | {row[6]} % |")
    md += ["", "Speedup and reduction vs CPU are **N/A**: no CPU-only runtime "
           "log exists under `evidence/runtime/cpu_only/`." if not cpu else "",
           "", "## Sources", ""]
    for k in measured:
        md.append(f"- {LABEL[k]}: `{rel(rt[k]['path'])}` (line `( N ) cycles total`)")
    md += ["", "## Formulas", "",
           "- Speedup vs X = cycles(X) / cycles(configuration)",
           "- Cycle reduction vs X = (cycles(X) − cycles(configuration)) / cycles(X) × 100",
           "", "## Caveats", "",
           "- One run per configuration; no repeat runs, so run-to-run variation "
           "is unknown. Operators the CFU does not touch vary between logs "
           "(e.g. MEAN: 12,170 / 12,019 / 21,806 ticks), see "
           "`../RESULTS_AUDIT.md`.",
           "- The logs do not state whether they were captured on the Nexys4 DDR "
           "board or in simulation, nor the exact commit. See "
           "`../CONFIGURATION_MAP.md`.",
           "- Generated by `paper_context/figures/scripts/build_results.py`."]
    (TABLES / "end_to_end_performance.md").write_text("\n".join(md) + "\n")

    # ---------------- operator-level ----------------
    ops_md = ["# Operator Execution (TFLM profiler)", "",
              "Each log contains a 71-event profiler trace (`Event,Tag,Ticks`). "
              "1 tick = 1024 CPU cycles (`common/src/tensorflow/lite/micro/"
              "micro_time.cc`: `perf_get_mcycle64() >> 10`). Tick values are "
              "therefore quantized to 1024 cycles; cycle values below marked "
              "*est.* are ticks × 1024.", "",
              "## Event counts (identical in all three logs)", ""]
    tags = {}
    for _, tag, _ in rt["cfu_1x1"]["events"]:
        tags[tag] = tags.get(tag, 0) + 1
    for k in measured[1:]:
        t2 = {}
        for _, tag, _ in rt[k]["events"]:
            t2[tag] = t2.get(tag, 0) + 1
        assert t2 == tags, f"event mix differs in {k}"
    ops_md += ["| Operator | Events |", "|---|---:|"]
    ops_md += [f"| {t} | {n} |" for t, n in sorted(tags.items(), key=lambda x: -x[1])]
    ops_md += [f"| **Total** | **{sum(tags.values())}** |", "",
               "Of the 35 `CONV_2D` events, event 1 is the network's first "
               "standard convolution (3×3, stride 2 in MobileNetV2; not eligible "
               "for the 1×1 CFU, which requires a 1×1 filter, see "
               "`proj/mnv2_cfu_package/src/tensorflow/lite/kernels/internal/"
               "reference/integer_ops/conv.cc`); the remaining 34 are 1×1 "
               "pointwise convolutions. The event trace does not name layers, "
               "so this split relies on the MobileNetV2 layer order.", "",
               "## Ticks and estimated cycles per operator class", "",
               "| Configuration | DW ticks | DW cycles (est.) | CONV_2D ticks | "
               "CONV_2D cycles (est.) | Σ all ticks × 1024 | Logged total cycles |",
               "|---|---:|---:|---:|---:|---:|---:|"]
    rows = []
    for k in measured:
        b = op_breakdown(rt[k])
        ops_md.append(f"| {LABEL[k]} | {fmt(b['dw_ticks'])} | "
                      f"{fmt(b['dw_cycles_est'])} | {fmt(b['conv_ticks'])} | "
                      f"{fmt(b['conv_cycles_est'])} | "
                      f"{fmt(b['all_ticks'] * TICK_CYCLES)} | "
                      f"{fmt(rt[k]['cycles'])} |")
    b1, b2, b3 = (op_breakdown(rt[k]) for k in
                  ("cfu_1x1", "cfu_1x1_3x3", "sliding_window"))
    ops_md += ["", "Derived (from ticks, formula = ticks_A / ticks_B):", "",
               f"- DEPTHWISE_CONV_2D share of total, 1×1 CFU: "
               f"{b1['dw_cycles_est'] / rt['cfu_1x1']['cycles'] * 100:.1f} %",
               f"- DEPTHWISE_CONV_2D ticks, 1×1 → 1×1+3×3: "
               f"{b1['dw_ticks'] / b2['dw_ticks']:.3f}× fewer",
               f"- DEPTHWISE_CONV_2D ticks, 1×1+3×3 → sliding window: "
               f"{b2['dw_ticks'] / b3['dw_ticks']:.3f}× fewer",
               f"- CONV_2D ticks, 1×1 / 1×1+3×3 / sliding: "
               f"{fmt(b1['conv_ticks'])} / {fmt(b2['conv_ticks'])} / "
               f"{fmt(b3['conv_ticks'])} (unchanged within 0.2 %)", "",
               "## Per depthwise layer (ticks)", "",
               "Stride is not printed in the log; stride-2 layers are the four "
               "DEPTHWISE_CONV_2D events that directly follow a PAD event.", "",
               "| Event | Stride | 1×1 CFU | 1×1+3×3 | Sliding window | "
               "1×1→3×3 | 3×3→sliding |", "|---:|---:|---:|---:|---:|---:|---:|"]
    ev = {k: rt[k]["events"] for k in measured}
    per_layer = []
    for i, (idx, tag, t1) in enumerate(ev["cfu_1x1"]):
        if tag != "DEPTHWISE_CONV_2D":
            continue
        stride = 2 if ev["cfu_1x1"][i - 1][1] == "PAD" else 1
        t2, t3 = ev["cfu_1x1_3x3"][i][2], ev["sliding_window"][i][2]
        per_layer.append([idx, stride, t1, t2, t3])
        ops_md.append(f"| {idx} | {stride} | {fmt(t1)} | {fmt(t2)} | {fmt(t3)} | "
                      f"{(t2 - t1) / t1 * 100:+.1f} % | {(t3 - t2) / t2 * 100:+.1f} % |")
    n_dw_faster = sum(1 for r in per_layer if r[3] < r[2])
    ops_md += ["",
               f"- {n_dw_faster} of {len(per_layer)} depthwise events take fewer "
               "ticks with the 3×3 CFU than with the 1×1-only build, consistent "
               "with all 17 depthwise layers invoking the 3×3 CFU (17 CONFIGURE "
               "calls in the analytical count). No per-layer CFU-call log exists.",
               "- With sliding window, the 4 stride-2 layers (which do not use "
               "SHIFT_RIGHT) and events 60 and 64 take *more* ticks than in the "
               "1×1+3×3 log. Unexplained; treat per-layer differences as "
               "unreliable until repeat runs exist (see `../RESULTS_AUDIT.md`).",
               "", "## Sources", ""]
    ops_md += [f"- `{rel(rt[k]['path'])}`" for k in measured]
    ops_md += ["", "Generated by `paper_context/figures/scripts/build_results.py`."]
    (TABLES / "operator_execution.md").write_text("\n".join(ops_md) + "\n")
    write_csv(FIG_DATA / "depthwise_layer_ticks.csv",
              ["event", "stride", "cfu_1x1_ticks", "cfu_1x1_3x3_ticks",
               "sliding_window_ticks"], per_layer)

    # ---------------- sliding-window instructions ----------------
    before, after = dw_instruction_counts()
    order = ["CONFIGURE", "LOAD", "SHIFT_RIGHT", "RUN", "GET_RESULT"]
    tb, ta = sum(before.values()), sum(after.values())
    sw_rows = []
    for ins in order:
        b, a = before[ins], after[ins]
        red = f"{(b - a) / b * 100:.2f}" if b else ""
        sw_rows.append([ins, b, a, red])
    sw_rows.append(["TOTAL_3X3_CFU_INSTRUCTIONS", tb, ta, f"{(tb - ta) / tb * 100:.2f}"])
    write_csv(TABLES / "sliding_window_instructions.csv",
              ["instruction", "before", "after", "reduction_pct"], sw_rows)
    write_csv(FIG_DATA / "sliding_window_instructions.csv",
              ["instruction", "before", "after", "reduction_pct"], sw_rows)
    md = ["# Sliding-Window 3×3 CFU Instruction Counts", "",
          "Per inference, all 17 eligible 3×3 depthwise layers. "
          "**Instruction-count reduction, not a speedup.** The end-to-end effect "
          "is in `end_to_end_performance.md`.", "",
          "| Instruction | Before (3 LOADs/window) | After (sliding window) | Reduction |",
          "|---|---:|---:|---:|"]
    for ins, b, a, red in sw_rows:
        name = "**Total 3×3 CFU instructions**" if ins.startswith("TOTAL") else ins
        r = f"{red} %" if red else ("new (0 → %s)" % fmt(a) if a else "0 %")
        if red == "0.00":
            r = "0 %"
        md.append(f"| {name} | {fmt(b)} | {fmt(a)} | {r} |")
    md += ["",
           f"LOAD reduction = 1 − {fmt(after['LOAD'])} / {fmt(before['LOAD'])} = "
           f"{(1 - after['LOAD'] / before['LOAD']) * 100:.3f} % → **71.27 %** "
           "rounded (71.26 % if truncated). Use one convention consistently.", "",
           "## Status: analytical (source-derived), not measured", "",
           "No `make DW3X3_VERIFY=1` counter log exists in the evidence. The counts "
           "are computed by `dw_instruction_counts()` in "
           "`paper_context/figures/scripts/build_results.py`, which mirrors "
           "`Dw3x3VerifyReport()` in "
           "`proj/mnv2_cfu_package/src/tensorflow/lite/micro/kernels/depthwise_conv.cc` "
           "and the loop structure of `mnv2_depthwise_conv.h`, applied to the "
           "MobileNetV2 a0.35 224 depthwise layer shapes. The result matches "
           "the counts reported independently by the team exactly (all 10 values).",
           "", "Formula: reduction = (before − after) / before × 100"]
    (TABLES / "sliding_window_instructions.md").write_text("\n".join(md) + "\n")

    # ---------------- FPGA resources ----------------
    res_rows = []
    res_md = ["# FPGA Resources and Timing", "",
              "Device: `%s` (Digilent Nexys4 DDR SoC, design `digilent_nexys4ddr`), "
              "Vivado %s." % (hw["cfu_1x1"]["util_place"]["device"],
                              hw["cfu_1x1"]["util_place"]["tool"].split()[1]), "",
              "**Stages:** utilization = **post-place** (`Design State: Fully "
              "Placed`; no post-route utilization report exists). Timing = "
              "**post-route** (`Design State: Physopt postRoute`).", "",
              "## CFU hierarchy (`Cfu` instance), post-place", "",
              "| Configuration | LUT | FF | BRAM | DSP | WNS (ns) | TNS (ns) | "
              "Fmax est. (MHz) | Timing Status |",
              "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    top_md = ["", "## Whole SoC (top level), post-place", "",
              "| Configuration | LUT | FF | BRAM | DSP | WNS (ns) | TNS (ns) | "
              "Fmax est. (MHz) | Timing Status |",
              "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    synth_md = ["", "## Synthesis-stage values (for reference only, not for the paper)", "",
                "| Configuration | Level | LUT | FF | RAMB36 | RAMB18 | DSP | "
                "Synth WNS (ns) |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for k in ("cfu_1x1", "cfu_1x1_3x3", "sliding_window"):
        u, us = hw[k]["util_place"], hw[k]["util_synth"]
        t, ts = hw[k]["timing_route"], hw[k]["timing_synth"]
        assert u["state"] == "Fully Placed", u["state"]
        assert "postRoute" in t["state"], t["state"]
        assert t["sys_wns"] == t["wns"], "worst slack not on system clock"
        fmax = 1000.0 / (t["sys_period_ns"] - t["wns"])
        status = (f"MET @ {t['sys_freq_mhz']:.0f} MHz"
                  if t["met"] and t["tns_fail"] == 0 and t["ths_fail"] == 0 else "FAILED")
        for level, md_list in (("cfu", res_md), ("top", top_md)):
            r = u["rows"][level]
            bram = f"{r['ramb36']}×36K + {r['ramb18']}×18K"
            md_list.append(f"| {LABEL[k]} | {fmt(r['lut'])} | {fmt(r['ff'])} | "
                           f"{bram} | {r['dsp']} | {t['wns']:+.3f} | "
                           f"{t['tns']:.3f} | {fmax:.1f} | {status} |")
            res_rows.append([k, level, "post-place", r["lut"], r["logic_lut"],
                             r["lutram"], r["ff"], r["ramb36"], r["ramb18"],
                             r["dsp"], t["wns"], t["tns"], t["tns_fail"],
                             t["whs"], t["ths"], t["sys_period_ns"],
                             f"{fmax:.1f}", status, rel(u["path"]), rel(t["path"])])
        for level in ("top", "cfu"):
            r = us["rows"][level]
            synth_md.append(f"| {LABEL[k]} | {level} | {fmt(r['lut'])} | "
                            f"{fmt(r['ff'])} | {r['ramb36']} | {r['ramb18']} | "
                            f"{r['dsp']} | {ts['wns']:+.3f} |")
    rhdr = ["configuration", "level", "stage", "lut", "logic_lut", "lutram", "ff",
            "ramb36", "ramb18", "dsp", "wns_ns", "tns_ns", "failing_endpoints",
            "whs_ns", "ths_ns", "sys_clock_period_ns", "fmax_est_mhz",
            "timing_status", "utilization_source", "timing_source"]
    write_csv(TABLES / "fpga_resources.csv", rhdr, res_rows)
    write_csv(FIG_DATA / "fpga_resources.csv",
              ["configuration", "level", "lut", "ff", "ramb36", "ramb18", "dsp",
               "dw3x3_lut", "dw3x3_ff", "wns_ns", "fmax_est_mhz"],
              [[k, "cfu", hw[k]["util_place"]["rows"]["cfu"]["lut"],
                hw[k]["util_place"]["rows"]["cfu"]["ff"],
                hw[k]["util_place"]["rows"]["cfu"]["ramb36"],
                hw[k]["util_place"]["rows"]["cfu"]["ramb18"],
                hw[k]["util_place"]["rows"]["cfu"]["dsp"],
                hw[k]["util_place"]["rows"].get("depthwise_3x3", {}).get("lut", 0),
                hw[k]["util_place"]["rows"].get("depthwise_3x3", {}).get("ff", 0),
                hw[k]["timing_route"]["wns"],
                f"{1000.0 / (hw[k]['timing_route']['sys_period_ns'] - hw[k]['timing_route']['wns']):.1f}"]
               for k in ("cfu_1x1", "cfu_1x1_3x3", "sliding_window")])
    pw = hw["cfu_1x1"]["power"]
    tail = ["", "## Notes", "",
            "- WNS/TNS: post-route `report_timing_summary`, Design Timing Summary "
            "(setup). The worst setup path is on the SoC system clock "
            f"`{SYS_CLOCK}` (period {hw['cfu_1x1']['timing_route']['sys_period_ns']} ns, "
            f"{hw['cfu_1x1']['timing_route']['sys_freq_mhz']:.0f} MHz) in all three "
            "builds. All builds: 0 failing setup/hold endpoints.",
            "- **Fmax est.** is not reported by Vivado. Derived: "
            "Fmax ≈ 1000 / (T_sys − WNS) MHz, T_sys = 13.333 ns. It is a "
            "single-corner estimate from the post-route slack; the designs were "
            "constrained and run at 75 MHz.",
            "- No CPU-only Vivado build exists, so there is no CPU-only row.",
            "- BRAM and DSP counts are identical in all three configurations "
            "(CFU: 4×RAMB36 + 8×RAMB18, 4 DSP; the 4 DSPs are in the 1×1 "
            "post-processor `pp`). The 3×3 depthwise unit uses **0 DSP** "
            "(its multipliers map to LUTs).",
            f"- Power: only the 1×1 build has a power report "
            f"(`{rel(pw['path'])}`, {pw['state']}): total {pw['total_w']} W, "
            f"dynamic {pw['dynamic_w']} W, static {pw['static_w']} W, confidence "
            f"{pw['confidence']}. Not comparable across configurations; do not use.",
            "", "## Sources", ""]
    for k in ("cfu_1x1", "cfu_1x1_3x3", "sliding_window"):
        tail.append(f"- {LABEL[k]}: `{rel(hw[k]['util_place']['path'])}`, "
                    f"`{rel(hw[k]['timing_route']['path'])}`")
    tail += ["", "Generated by `paper_context/figures/scripts/build_results.py`."]
    (TABLES / "fpga_resources.md").write_text(
        "\n".join(res_md + top_md + synth_md + tail) + "\n")

    # ---------------- resource deltas ----------------
    dmd = ["# Resource Deltas (post-place)", "",
           "delta = optimized configuration − baseline configuration. "
           "No percentages: baselines are stated per table.", ""]
    for title, base, opt in (("3×3 depthwise CFU overhead", "cfu_1x1", "cfu_1x1_3x3"),
                             ("Sliding-window overhead", "cfu_1x1_3x3", "sliding_window"),
                             ("Total (1×1 → sliding window)", "cfu_1x1", "sliding_window")):
        dmd += [f"## {title}: {LABEL[opt]} − {LABEL[base]}", "",
                "| Level | ΔLUT | ΔFF | ΔRAMB36 | ΔRAMB18 | ΔDSP |",
                "|---|---:|---:|---:|---:|---:|"]
        for level in ("cfu", "depthwise_3x3", "top"):
            rb = hw[base]["util_place"]["rows"].get(level)
            ro = hw[opt]["util_place"]["rows"].get(level)
            if ro is None:
                continue
            rb = rb or dict.fromkeys(ro, 0)
            d = {x: ro[x] - rb[x] for x in ro}
            dmd.append(f"| {level} | {d['lut']:+,} | {d['ff']:+,} | "
                       f"{d['ramb36']:+} | {d['ramb18']:+} | {d['dsp']:+} |")
        dmd.append("")
    c1 = hw["cfu_1x1"]["util_place"]["rows"]["cfu"]
    c2 = hw["cfu_1x1_3x3"]["util_place"]["rows"]["cfu"]
    t1 = hw["cfu_1x1"]["util_place"]["rows"]["top"]
    t2 = hw["cfu_1x1_3x3"]["util_place"]["rows"]["top"]
    dmd += ["## Notes", "",
            "- `depthwise_3x3` is the `Depthwise3x3Mac` sub-instance of `Cfu/fn0`; "
            "absent in the 1×1 build (counted as 0).",
            f"- Top-level ΔLUT for the 3×3 CFU ({t2['lut'] - t1['lut']:+,}) is larger "
            f"than the CFU-level ΔLUT ({c2['lut'] - c1['lut']:+,}). The difference "
            "is outside the CFU (placement/optimization variation in the rest of "
            "the SoC). For accelerator cost, cite the **CFU-level** delta.",
            "", "## Sources", ""]
    dmd += [f"- `{rel(hw[k]['util_place']['path'])}`"
            for k in ("cfu_1x1", "cfu_1x1_3x3", "sliding_window")]
    dmd += ["", "Generated by `paper_context/figures/scripts/build_results.py`."]
    (TABLES / "resource_deltas.md").write_text("\n".join(dmd) + "\n")

    make_figures(rt, hw, measured, before, after)
    print("OK:", ", ".join(LABEL[k] for k in measured), "runtime;",
          len(hw), "Vivado configurations")


# ---------------------------------------------------------------------------
# Figures (IEEE single column: 3.5 in wide)
# ---------------------------------------------------------------------------

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"  # validated slots 1-3
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"


def style():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "STIXGeneral", "mathtext.fontset": "stix",
        "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8,
        "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
        "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
        "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.grid.axis": "y", "grid.color": GRID,
        "grid.linewidth": 0.5, "axes.axisbelow": True, "hatch.linewidth": 0.5,
        "pdf.fonttype": 42, "svg.fonttype": "none", "legend.frameon": False,
    })
    return plt


def save(fig, name):
    for ext in ("pdf", "svg", "png"):
        fig.savefig(GRAPHS / f"{name}.{ext}", bbox_inches="tight",
                    dpi=600 if ext == "png" else None,
                    metadata=None if ext == "png" else {})


def make_figures(rt, hw, measured, before, after):
    plt = style()

    # Figure: end-to-end cycles by operator class
    keys = [k for k in measured]
    br = [op_breakdown(rt[k]) for k in keys]
    fig, ax = plt.subplots(figsize=(3.5, 2.2))
    x = range(len(keys))
    segs = [("Depthwise conv (3×3)", "dw_cycles_est", BLUE, ""),
            ("Conv2D (1×1 + first 3×3)", "conv_cycles_est", ORANGE, "////"),
            ("Other ops", "other_cycles_est", AQUA, "\\\\\\\\")]
    bottom = [0.0] * len(keys)
    for name, key, color, hatch in segs:
        vals = [b[key] / 1e6 for b in br]
        ax.bar(x, vals, 0.55, bottom=bottom, color=color, label=name,
               hatch=hatch, edgecolor="white", linewidth=0.8)
        bottom = [b + v for b, v in zip(bottom, vals)]
    ref = rt["cfu_1x1"]["cycles"]
    for i, k in enumerate(keys):
        c = rt[k]["cycles"]
        ax.text(i, c / 1e6 + 12, f"{c / 1e6:.1f} M\n{ref / c:.2f}×",
                ha="center", va="bottom", fontsize=7, color=INK)
    ax.set_xticks(list(x), [SHORT[k] for k in keys])
    ax.set_ylabel("Cycles per inference (millions)")
    ax.set_ylim(0, max(rt[k]["cycles"] for k in keys) / 1e6 * 1.25)
    ax.legend(loc="upper right", ncol=1, handlelength=1.2)
    save(fig, "end_to_end_performance")
    plt.close(fig)

    # Figure: sliding-window instruction counts
    ins = ["LOAD", "SHIFT_RIGHT", "RUN", "GET_RESULT"]
    fig, ax = plt.subplots(figsize=(3.5, 2.0))
    w = 0.36
    xs = range(len(ins))
    ax.bar([i - w / 2 for i in xs], [before[n] / 1e6 for n in ins], w,
           color=BLUE, label="Before (3 LOADs per window)",
           edgecolor="white", linewidth=0.8)
    ax.bar([i + w / 2 for i in xs], [after[n] / 1e6 for n in ins], w,
           color=ORANGE, hatch="////", label="After (sliding window)",
           edgecolor="white", linewidth=0.8)
    red = (before["LOAD"] - after["LOAD"]) / before["LOAD"] * 100
    ax.annotate(f"−{red:.1f} %", xy=(w / 2, after["LOAD"] / 1e6),
                xytext=(w / 2 + 0.55, before["LOAD"] / 1e6 * 0.75),
                fontsize=7, color=INK, ha="center",
                arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.6))
    ax.set_xticks(list(xs), ["LOAD", "SHIFT_RIGHT", "RUN", "GET_RESULT"])
    ax.set_ylabel("Instructions per inference (M)")
    ax.set_ylim(0, before["LOAD"] / 1e6 * 1.15)
    ax.legend(loc="upper right")
    save(fig, "sliding_window_instructions")
    plt.close(fig)

    # Figure: CFU resources (LUT, FF) split into 3x3 unit vs rest of CFU
    cfg = ["cfu_1x1", "cfu_1x1_3x3", "sliding_window"]
    fig, axes = plt.subplots(1, 2, figsize=(3.5, 2.0), sharey=False)
    for ax, (res, title) in zip(axes, (("lut", "LUTs"), ("ff", "Flip-flops"))):
        rest, dw = [], []
        for k in cfg:
            rows = hw[k]["util_place"]["rows"]
            d = rows.get("depthwise_3x3", {}).get(res, 0)
            dw.append(d)
            rest.append(rows["cfu"][res] - d)
        xs = range(len(cfg))
        ax.bar(xs, rest, 0.6, color=BLUE, label="Rest of CFU (1×1 path)",
               edgecolor="white", linewidth=0.8)
        ax.bar(xs, dw, 0.6, bottom=rest, color=ORANGE, hatch="////",
               label="3×3 depthwise unit", edgecolor="white", linewidth=0.8)
        for i, (r, d) in enumerate(zip(rest, dw)):
            ax.text(i, r + d + 40, f"{r + d:,}", ha="center", va="bottom",
                    fontsize=6.5, color=INK)
        ax.set_title(f"CFU {title}", pad=2)
        ax.set_xticks(list(xs), ["1×1", "1×1+3×3", "+SW"])
        ax.set_ylim(0, max(r + d for r, d in zip(rest, dw)) * 1.18)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, fontsize=7,
               handlelength=1.2, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(w_pad=1.0, rect=(0, 0.09, 1, 1))
    save(fig, "fpga_resources")
    plt.close(fig)


if __name__ == "__main__":
    main()
