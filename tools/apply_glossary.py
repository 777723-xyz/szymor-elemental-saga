#!/usr/bin/env python3
"""Pre-fill translations in a TSV from the approved glossary.

Reads a translation TSV (default docs/text/all.tsv) and the finalized glossary
(default docs/text/glossary_final.tsv), filling the empty `translation` column
with:

1. exact matches (japanese == glossary entry), and
2. speaker prefixes (japanese == "NAME：rest" -> "NAME: rest", keeping any
   text after the colon).

Writes the result to docs/text/translated.tsv (or --out).

Usage:
    python3 tools/apply_glossary.py [--tsv docs/text/all.tsv]
        [--glossary docs/text/glossary_final.tsv] [--out docs/text/translated.tsv]
"""
import argparse
import csv


def load_tsv(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tsv", default="docs/text/all.tsv")
    ap.add_argument("--glossary", default="docs/text/glossary_final.tsv")
    ap.add_argument("--out", default="docs/text/translated.tsv")
    args = ap.parse_args()

    gloss = {r["japanese"]: r["proposed"] for r in load_tsv(args.glossary)
             if r.get("proposed")}
    rows = load_tsv(args.tsv)

    exact = prefix = 0
    for r in rows:
        if (r.get("translation") or "").strip():
            continue
        jp = r["japanese"]
        if jp in gloss:
            r["translation"] = gloss[jp]
            exact += 1
            continue
        if jp.endswith("："):
            name = jp[:-1]
            if name in gloss:
                r["translation"] = gloss[name] + ":"
                prefix += 1
                continue
        # name followed by more text on the same line
        for name in gloss:
            if jp.startswith(name + "："):
                r["translation"] = gloss[name] + ":" + jp[len(name) + 1:]
                prefix += 1
                break

    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys(), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    filled = sum(1 for r in rows if (r.get("translation") or "").strip())
    print(f"Wrote {args.out}: {filled}/{len(rows)} rows translated "
          f"({exact} exact, {prefix} prefix)")


if __name__ == "__main__":
    main()
