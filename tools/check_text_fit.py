#!/usr/bin/env python3
"""Flag translated dialogue lines that will overflow the message window.

RPG Maker MV 1.6.1 does NOT auto-wrap message text: lines are broken only by
\\n control codes, and characters wider than the message area are clipped.
This tool estimates the rendered width of every line with the actual game
font (mplus-1m-regular.ttf) and flags lines that exceed the window.

Model (verified against the game's own rpg_windows.js / YEP_CoreEngine):
- window width 816, standard padding 18  -> 780px usable text width
- if a face image is active (command 101 with a face name before the text),
  text starts at x=168 -> 612px usable
- font size 28, line height 36 (no wrapping, so no line-count problem)
- control codes: \\c[n] zero width, \\i[n] icon 32px, \\N[n]/\\P[n] actor name,
  \\V[n]/\\v[n] variable value (ESTIMATE, flagged), \\G currency unit,
  \\n newline, \\f page break; \\., \\|, \\!, \\^, \\$, \\>, \\< are zero width.

Usage:
    python3 tools/check_text_fit.py docs/text/all.tsv
        [--data www/data] [--font www/fonts/mplus-1m-regular.ttf]
        [--size 28] [--budget 780] [--source prefer] [--top 40]

Rows of type "dialogue" are checked (401 show-text and 405 scrolling text).
The "translation" column is measured when filled; otherwise "japanese".
"""
import argparse
import json
import os
import re

from PIL import ImageFont

MAP_ID_RE = re.compile(r"^MAP(\d+)_e(\d+)_p(\d+)_(\d+)(?:_c(\d+))?$")
CTRL_RE = re.compile(r"\\([A-Za-z.])(?:\[([^\]]*)\])?")
FACE_BUDGET = 612.0  # 780 - 168 (face column)
NO_FACE_BUDGET = 780.0  # 816 - 2*18 padding


def load_tsv(path):
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh]
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def load_json(path):
    return json.load(open(path, encoding="utf-8-sig"))


class Measurer:
    def __init__(self, font_path, size, data_dir, tmap):
        self.font = ImageFont.truetype(font_path, size)
        self.actor_names = {}
        for a in load_json(os.path.join(data_dir, "Actors.json")):
            if a:
                self.actor_names[a["id"]] = a["name"]
        system = load_json(os.path.join(data_dir, "System.json"))
        self.currency = system.get("currencyUnit") or "G"
        # translated actor names override the originals for \\N[n] resolution
        for rid, trans in tmap.items():
            m = re.match(r"^DB_Actors_(\d+)_name$", rid)
            if m:
                self.actor_names[int(m.group(1))] = trans
        self.var_estimate = self.font.getlength("99999")

    def measure(self, text):
        """Return (widths_per_line, used_variable_estimate)."""
        lines = [[]]
        i, run = 0, []
        var_estimate = False

        def flush():
            if run:
                lines[-1].append(self.font.getlength("".join(run)))
                run.clear()

        while i < len(text):
            if text[i] == "\\" and i + 1 < len(text):
                flush()
                m = CTRL_RE.match(text, i)
                if m:
                    code, arg = m.group(1), m.group(2)
                    i = m.end()
                    if code in ("n", "f"):
                        lines.append([])
                    elif code == "i":
                        lines[-1].append(32)
                    elif code in ("v", "V"):
                        lines[-1].append(self.var_estimate)
                        var_estimate = True
                    elif code in ("N", "P"):
                        name = ""
                        if arg and arg.isdigit():
                            name = self.actor_names.get(int(arg), "")
                        lines[-1].append(self.font.getlength(name))
                    elif code == "G":
                        lines[-1].append(self.font.getlength(self.currency))
                    # c / . / | / ! / ^ / $ / > / < / { / } -> zero width
                    continue
            run.append(text[i])
            i += 1
        flush()
        return [sum(ln) for ln in lines], var_estimate


class FaceLookup:
    """Find whether a face image is displayed before a map dialogue command."""

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.cache = {}

    def face_active(self, row_id):
        m = MAP_ID_RE.match(row_id)
        if not m:
            return False  # common events / scrolling text: no face
        mapid, ei, pi, idx = (int(m.group(1)), int(m.group(2)),
                              int(m.group(3)), int(m.group(4)))
        fname = f"Map{mapid:03d}.json"
        if fname not in self.cache:
            self.cache[fname] = load_json(os.path.join(self.data_dir, fname))
        lst = self.cache[fname]["events"][ei]["pages"][pi]["list"]
        if lst[idx]["code"] == 405:
            return False  # scrolling text never shows a face
        for j in range(idx - 1, -1, -1):
            if lst[j]["code"] == 101:
                return lst[j]["parameters"][0] != ""
            if lst[j]["code"] not in (101, 401, 405):
                break
        return False


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tsv", help="TSV to check (docs/text/all.tsv or a translated copy)")
    ap.add_argument("--data", default="www/data")
    ap.add_argument("--font", default="www/fonts/mplus-1m-regular.ttf")
    ap.add_argument("--size", type=int, default=28)
    ap.add_argument("--budget", type=float, default=NO_FACE_BUDGET,
                    help=f"usable message width (default {NO_FACE_BUDGET:.0f}; "
                         f"{FACE_BUDGET:.0f} with face)")
    ap.add_argument("--source", choices=("prefer", "japanese", "translation"),
                    default="prefer",
                    help="column to measure (prefer: translation if filled)")
    ap.add_argument("--top", type=int, default=40, help="max flagged rows to print")
    args = ap.parse_args()

    rows = load_tsv(args.tsv)
    tmap = {r["id"]: r.get("translation") or ""
            for r in rows if (r.get("translation") or "").strip()}
    measurer = Measurer(args.font, args.size, args.data, tmap)
    faces = FaceLookup(args.data)

    flagged, estimates, checked = [], 0, 0
    for row in rows:
        if row.get("type") != "dialogue":
            continue
        rid = row["id"]
        text = row.get("translation") or ""
        if args.source == "japanese":
            text = row["japanese"]
        elif args.source == "prefer" and not text.strip():
            text = row["japanese"]
        if not text:
            continue
        face = faces.face_active(rid)
        budget = FACE_BUDGET if face else args.budget
        widths, est = measurer.measure(text)
        checked += 1
        estimates += 1 if est else 0
        overflow = max((w - budget for w in widths), default=0)
        if overflow > 0:
            flagged.append((overflow, rid, row["file"], row["japanese"][:60],
                            text[:60], widths, budget, face))

    flagged.sort(reverse=True)
    print(f"Checked {checked} dialogue rows "
          f"({estimates} with variable-value estimates)")
    print(f"Flagged {len(flagged)} rows exceeding the message width:")
    for ov, rid, fname, jp, tx, widths, budget, face in flagged[:args.top]:
        why = " (face shown)" if face else ""
        print(f"\n  [{fname}::{rid}]{why} overflow +{ov:.0f}px "
              f"budget {budget:.0f}px")
        print(f"    lines: {[round(w) for w in widths]}")
        print(f"    JP : {jp}")
        print(f"    EN : {tx}")


if __name__ == "__main__":
    main()
