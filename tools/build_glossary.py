#!/usr/bin/env python3
"""Build a translation glossary from the RPG Maker MV game data.

Combines every proper-noun-ish string from the database (actors, enemies,
skills, items, weapons, armors, states, classes, map names) with speaker-name
prefixes found in dialogue (e.g. "市民ジェームズ：") and writes a deduplicated
table to docs/text/glossary.tsv for the translator/reviewer.

Usage:
    python3 tools/build_glossary.py [--data www/data] [--out docs/text/glossary.tsv]
"""
import argparse
import json
import os
import re
from collections import Counter

DB_SOURCES = ("Actors", "Enemies", "Skills", "Items", "Weapons", "Armors",
              "States", "Classes")
CATEGORY = {"Actors": "actor", "Enemies": "enemy", "Skills": "skill",
            "Items": "item", "Weapons": "weapon", "Armors": "armor",
            "States": "state", "Classes": "class"}
SPEAKER_RE = re.compile(r"^([^：\n]{1,20})：")


def load_json(path):
    return json.load(open(path, encoding="utf-8-sig"))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default="www/data")
    ap.add_argument("--out", default="docs/text/glossary.tsv")
    args = ap.parse_args()

    entries = {}  # japanese -> {"category": first-seen, "dialogue": count}
    order = []

    def add(jp, category):
        if jp in entries:
            return
        entries[jp] = {"category": category, "dialogue": 0}
        order.append(jp)

    for db in DB_SOURCES:
        data = load_json(os.path.join(args.data, f"{db}.json"))
        for e in data:
            if e and e.get("name"):
                add(e["name"], CATEGORY[db])

    for m in load_json(os.path.join(args.data, "MapInfos.json")):
        if m and m.get("name"):
            add(m["name"], "map")

    speakers = Counter()
    for fname in sorted(os.listdir(args.data)):
        if not fname.startswith("Map") or fname == "MapInfos.json":
            continue
        data = load_json(os.path.join(args.data, fname))
        for ev in data["events"] or []:
            if not ev:
                continue
            for page in ev["pages"] or []:
                for cmd in page["list"]:
                    if cmd["code"] == 401:
                        m = SPEAKER_RE.match(cmd["parameters"][0])
                        if m:
                            speakers[m.group(1)] += 1
    for ce in load_json(os.path.join(args.data, "CommonEvents.json")):
        if not ce:
            continue
        for cmd in ce.get("list") or []:
            if cmd["code"] == 401:
                m = SPEAKER_RE.match(cmd["parameters"][0])
                if m:
                    speakers[m.group(1)] += 1

    for jp, c in speakers.items():
        if jp not in entries:
            add(jp, "speaker")
        entries[jp]["dialogue"] = c

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("category\tjapanese\tdialogue\tproposed\tnotes\n")
        for jp in order:
            e = entries[jp]
            fh.write(f"{e['category']}\t{jp}\t{e['dialogue']}\t\t\n")

    total = len(order)
    speakers_only = sum(1 for jp in order if entries[jp]["category"] == "speaker")
    print(f"Wrote {args.out}: {total} entries "
          f"({speakers_only} from dialogue prefixes)")


if __name__ == "__main__":
    main()
