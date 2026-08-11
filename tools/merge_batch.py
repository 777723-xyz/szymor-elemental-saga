#!/usr/bin/env python3
"""Merge one or more batch translation files into the master translated TSV.

Batch files: TSV with columns `id  japanese  translation` (translation may be
empty to keep a row untouched). Rows in the batch override the master by id
when their translation is non-empty.

Usage:
    python3 tools/merge_batch.py BATCH.tsv [BATCH2.tsv ...]
        [--master docs/text/translated.tsv]
"""
import argparse
import csv
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batches", nargs="+", help="batch TSV files")
    ap.add_argument("--master", default="docs/text/translated.tsv")
    args = ap.parse_args()

    with open(args.master, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    by_id = {r["id"]: r for r in rows}

    applied = 0
    for bpath in args.batches:
        with open(bpath, encoding="utf-8") as fh:
            batch = list(csv.DictReader(fh, delimiter="\t"))
        for b in batch:
            t = (b.get("translation") or "").strip()
            if not t or b["id"] not in by_id:
                continue
            by_id[b["id"]]["translation"] = t
            applied += 1
        print(f"{bpath}: {len(batch)} rows read")

    with open(args.master, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys(), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    filled = sum(1 for r in rows if (r.get("translation") or "").strip())
    print(f"Merged {applied} translations; {filled}/{len(rows)} rows translated")


if __name__ == "__main__":
    main()
