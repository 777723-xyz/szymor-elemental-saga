#!/usr/bin/env python3
"""Insert \\n line breaks into translated dialogue and descriptions.

RPG Maker MV 1.6.1 never auto-wraps message text, so English lines longer
than the message window budget (780px, 612px when a face is shown) get clipped.
This tool re-wraps such lines at word boundaries using the real game font.

Usage:
    python3 tools/wrap_text.py docs/text/translated.tsv
        [--data www/data] [--font www/fonts/mplus-1m-regular.ttf]
        [--size 28] [--dry-run]

Coverage:
- dialogue rows (401 show-text / 405 scrolling text): budget 780px, or 612px
  when a face image is shown; message boxes are capped at 4 lines (scrolling
  text is not capped).
- description rows (Items/Skills/Weapons/Armors): budget 780px, capped at 3
  lines (the help window is 3 lines tall).

Existing \\n breaks are re-optimized: a balanced (minimum-raggedness) wrap
avoids single-word orphan lines. Runs of spaces / ideographic spaces are kept
intact. Rows that still cannot fit (even at the line cap) are reported so they
can be condensed by hand.
"""
import argparse
import csv
import re
from functools import lru_cache

from check_text_fit import (Measurer, FaceLookup, FACE_BUDGET,
                            NO_FACE_BUDGET)

CTRL_RE = re.compile(r"\\([A-Za-z.])(?:\[[^\]]*\])?")
SPACE_RE = re.compile(r"[ \u3000]+")


def tokenize(text):
    """Split text into tokens: ('w', word), ('s', space-run), ('c', code)."""
    tokens = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "\\" and i + 1 < n:
            m = CTRL_RE.match(text, i)
            if m:
                tokens.append(("c", m.group(0)))
                i = m.end()
                continue
        if ch in (" ", "\u3000"):
            m = SPACE_RE.match(text, i)
            tokens.append(("s", m.group(0)))
            i = m.end()
            continue
        j = i
        while j < n:
            c2 = text[j]
            if c2 in (" ", "\u3000"):
                break
            if c2 == "\\" and j + 1 < n and CTRL_RE.match(text, j):
                break
            j += 1
        tokens.append(("w", text[i:j]))
        i = j
    return tokens


def token_width(measurer, token):
    kind, val = token
    if kind == "c":
        return measurer.control_width(val)
    return measurer.font.getlength(val)


def balanced_wrap(measurer, text, budget, max_lines):
    """Wrap text into <= max_lines lines, minimizing squared slack.

    Returns (new_text, line_count), or (None, None) if it cannot fit. Existing
    \\n line-break markers (and \\f page breaks) are dropped and re-optimized;
    other control codes are preserved. Space runs are preserved verbatim.
    """
    tokens = []
    for t in tokenize(text):
        if t[0] == "c" and t[1] in ("\\n", "\\f"):
            # the break marker is re-optimized away; if it stood between two
            # words ("festivals and\\nrituals"), keep a space so the words do
            # not get glued together
            if (t[1] == "\\n" and tokens
                    and tokens[-1][1][-1] not in " \u3000"):
                tokens.append(("s", " "))
            continue
        tokens.append(t)
    if not tokens:
        return text, 1
    widths = [token_width(measurer, t) for t in tokens]
    n = len(tokens)
    INF = float("inf")

    @lru_cache(maxsize=None)
    def solve(i, lines):
        if i == n:
            return (0, ())
        if lines <= 0:
            return (INF, None)
        best = None
        wsum = 0
        for j in range(i, n):
            wsum += widths[j]
            if wsum > budget:
                break
            sub, sub_breaks = solve(j + 1, lines - 1)
            if sub is INF:
                continue
            slack = budget - wsum
            cost = slack * slack + sub
            if best is None or cost < best[0]:
                best = (cost, (j,) + sub_breaks)
        return best if best else (INF, None)

    best, breaks = solve(0, max_lines)
    if best is INF:
        return None, None

    out_lines = []
    start = 0
    for end in breaks:
        line = "".join(t[1] for t in tokens[start:end + 1])
        line = line.rstrip(" \u3000")
        # a break before a space-run would leave it dangling at the next
        # line's start; the first line keeps its original leading indent
        if out_lines:
            line = line.lstrip(" \u3000")
        if line:
            out_lines.append(line)
        start = end + 1
    return "\\n".join(out_lines), len(out_lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tsv", help="translated TSV")
    ap.add_argument("--data", default="www/data")
    ap.add_argument("--font", default="www/fonts/mplus-1m-regular.ttf")
    ap.add_argument("--size", type=int, default=28)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(args.tsv, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    header = rows[0].keys()

    measurer = Measurer(args.font, args.size, args.data, {})
    faces = FaceLookup(args.data)

    modified = 0
    failed = []
    for r in rows:
        rtype = r.get("type")
        if rtype not in ("dialogue", "description"):
            continue
        # normalize real newlines (older rows store them literally) to the
        # standard \\n break marker used by the pipeline
        text = (r.get("translation") or "").strip().replace("\n", "\\n")
        if not text:
            continue
        if rtype == "description":
            budget, max_lines = NO_FACE_BUDGET, 3
            needs = ("\\n" in text) or (
                max(measurer.measure(text)[0], default=0) > budget)
        else:
            face = faces.face_active(r["id"])
            budget = FACE_BUDGET if face else NO_FACE_BUDGET
            max_lines = 100 if r.get("context") == "scrolling text" else 4
            needs = ("\\n" in text) or (
                max(measurer.measure(text)[0], default=0) > budget)
        if not needs:
            continue
        new, nlines = balanced_wrap(measurer, text, budget, max_lines)
        if new is None:
            failed.append((r["id"], rtype, text[:80]))
            continue
        if new != text:
            r["translation"] = new
            modified += 1

    if not args.dry_run:
        with open(args.tsv, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=header, delimiter="\t",
                               lineterminator="\r\n")
            w.writeheader()
            w.writerows(rows)

    print(f"Rewrapped {modified} rows")
    if failed:
        print(f"Could not fit {len(failed)} rows:")
        for rid, rtype, tx in failed:
            print(f"  !! {rid} [{rtype}] {tx!r}")


if __name__ == "__main__":
    main()
