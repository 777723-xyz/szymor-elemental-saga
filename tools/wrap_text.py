#!/usr/bin/env python3
"""Insert \\n line breaks into translated dialogue that would overflow.

RPG Maker MV 1.6.1 never auto-wraps message text, so English lines longer
than the message window budget (780px, 612px when a face is shown) get clipped.
This tool re-wraps such lines at word boundaries using the real game font.

Usage:
    python3 tools/wrap_text.py docs/text/translated.tsv
        [--data www/data] [--font www/fonts/mplus-1m-regular.ttf]
        [--size 28] [--dry-run]

Lines are rewritten with literal \\n control codes (same convention as the
source data). Rows not exceeding the budget are left untouched. Control codes
(\\c[n], \\i[n], \\N[n], ...) are preserved as atomic tokens.
"""
import argparse
import csv
import re

from check_text_fit import Measurer, FaceLookup, MAP_ID_RE, FACE_BUDGET, NO_FACE_BUDGET

CTRL_RE = re.compile(r"\\([A-Za-z.])(?:\[[^\]]*\])?")


def tokenize(text):
    """Split text into tokens: ('w', word incl. trailing space) or ('c', code)."""
    tokens = []
    run = []

    def flush():
        if run:
            tokens.append(("w", "".join(run)))
            run.clear()

    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            m = CTRL_RE.match(text, i)
            if m:
                flush()
                tokens.append(("c", m.group(0)))
                i = m.end()
                continue
        if ch in (" ", "\u3000"):
            run.append(ch)  # keep the space attached to the word
            flush()
            i += 1
            continue
        run.append(ch)
        i += 1
    flush()
    return tokens


def wrap(measurer, text, budget):
    """Return the text with \\n inserted so each rendered line fits budget."""
    tokens = tokenize(text)
    lines = [[]]
    widths = []  # rendered width per current line

    def line_width(toks):
        w = 0.0
        for kind, val in toks:
            if kind == "w":
                w += measurer.measure_simple(val)
            else:
                w += measurer.control_width(val)
        return w

    for kind, val in tokens:
        if kind == "w":
            # try to fit whole word on current line
            candidate = lines[-1] + [("w", val)]
            if line_width(candidate) <= budget and lines[-1]:
                lines[-1].append(("w", val))
            else:
                if lines[-1] and any(k == "w" for k, _ in lines[-1]):
                    lines.append([("w", val)])
                else:
                    # a single word wider than budget (rare): keep on line
                    lines[-1].append(("w", val))
        else:
            lines[-1].append(("c", val))
    return "\\n".join("".join(v for _, v in ln) for ln in lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tsv", help="translated TSV")
    ap.add_argument("--data", default="www/data")
    ap.add_argument("--font", default="www/fonts/mplus-1m-regular.ttf")
    ap.add_argument("--size", type=int, default=28)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(args.tsv, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    header = rows[0].keys()

    measurer = Measurer(args.font, args.size, args.data, {})
    faces = FaceLookup(args.data)

    modified = 0
    for r in rows:
        if r.get("type") != "dialogue":
            continue
        text = (r.get("translation") or "").strip()
        if not text:
            continue
        face = faces.face_active(r["id"])
        budget = FACE_BUDGET if face else NO_FACE_BUDGET
        widths, _ = measurer.measure(text)
        if max(widths, default=0) <= budget:
            continue
        new = wrap(measurer, text, budget)
        if new != text:
            r["translation"] = new
            modified += 1

    if not args.dry_run:
        with open(args.tsv, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=header, delimiter="\t")
            w.writeheader()
            w.writerows(rows)

    print(f"Rewrapped {modified} dialogue rows")


if __name__ == "__main__":
    main()
