#!/usr/bin/env python3
"""Extract all translatable strings from an RPG Maker MV game into TSV tables.

Targets the unencrypted data layout of this project (RPG Maker MV 1.6.1):

    www/data/Map*.json          -> dialogue, choices, names, scripts (events)
    www/data/CommonEvents.json  -> dialogue in common events
    www/data/<DB>.json          -> Actors/Skills/Items/Weapons/Armors/Enemies/
                                   States/Troops/Classes: name/description/note
    www/data/System.json        -> title, terms, elements, skill/weapon/armor types
    www/js/plugins.js           -> plugin parameter values containing Japanese

Usage:
    python3 tools/extract_text.py [--data www/data] [--out docs/text]
                                  [--plugins www/js/plugins.js] [--all]

Output (UTF-8, tab-separated, columns: id, file, context, type, japanese, translation):
    dialogue.tsv  database.tsv  system.tsv  plugins.tsv  all.tsv
    all.json      machine-readable master table keyed by id (for the injector)

Notes on RPG Maker MV specifics handled here:
- 401 = Show Text, 405 = scrolling text line, 102 = Show Choices (params[0]).
- 402 "when" branches are matched by INDEX (params[0]), not by text, so the
  duplicated text in 402 (params[1]) is NOT extracted -- it is display-only
  and the injector may sync it from the translated 102 entry.
- 320 = Change Name (params[1] is the new name).
- 355/655 = script lines: extracted as type "script" for MANUAL review only,
  never machine-translate code.
- Control codes (\\c[n], \\i[n], \\v[n], \\N[n], \\n, \\, \\>, \\<) are left
  as-is; translators must keep them untouched.
"""
import argparse
import json
import os
import re
import sys

JP_RE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")

DB_FIELDS = ("name", "description", "note")
DB_FILES = ("Actors", "Classes", "Skills", "Items", "Weapons",
            "Armors", "Enemies", "States", "Troops")


def esc(s):
    return s.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")


def has_jp(s):
    return bool(JP_RE.search(s or ""))


def emit(rows, all_rows, json_rows, rid, fname, ctx, rtype, text):
    """Append a row unless --all is off and the text has no Japanese."""
    if not text:
        return
    if not args.all and not has_jp(text):
        return
    rows[rtype].append((rid, fname, ctx, rtype, esc(text)))
    all_rows.append((rid, fname, ctx, rtype, esc(text)))
    json_rows[rid] = {"file": fname, "context": ctx, "type": rtype,
                      "japanese": text, "translation": None}


def walk_commands(commands, fname, prefix, rows, all_rows, json_rows):
    """Walk an event command list; prefix is the stable row-id prefix."""
    for idx, cmd in enumerate(commands):
        code = cmd["code"]
        rid = f"{prefix}_{idx}"
        if code == 401:  # Show Text
            emit(rows, all_rows, json_rows, rid, fname, str(cmd.get("indent", "")),
                 "dialogue", cmd["parameters"][0])
        elif code == 405:  # scrolling text line
            emit(rows, all_rows, json_rows, rid, fname, "scrolling text",
                 "dialogue", cmd["parameters"][0])
        elif code == 102:  # Show Choices
            for ci, choice in enumerate(cmd["parameters"][0]):
                emit(rows, all_rows, json_rows, f"{rid}_c{ci}", fname,
                     "choice", "choice", choice)
        elif code == 320:  # Change Name
            emit(rows, all_rows, json_rows, rid, fname, "change name",
                 "name", cmd["parameters"][1])
        elif code in (355, 655):  # Script: manual review only
            emit(rows, all_rows, json_rows, rid, fname, "script (review)",
                 "script", cmd["parameters"][0])


def extract_maps(data_dir, rows, all_rows, json_rows):
    map_files = []
    for f in os.listdir(data_dir):
        m = re.fullmatch(r"Map(\d+)\.json", f)
        if m:
            map_files.append((int(m.group(1)), os.path.join(data_dir, f)))
    for mapid, path in sorted(map_files):
        data = json.load(open(path, encoding="utf-8-sig"))
        for ei, ev in enumerate(data["events"] or []):
            if not ev:
                continue
            for pi, page in enumerate(ev["pages"] or []):
                prefix = f"MAP{mapid}_e{ei}_p{pi}"
                walk_commands(page["list"], f"Map{mapid:03d}.json", prefix,
                              rows, all_rows, json_rows)


def extract_common_events(data_dir, rows, all_rows, json_rows):
    path = os.path.join(data_dir, "CommonEvents.json")
    data = json.load(open(path, encoding="utf-8-sig"))
    for ce in data:
        if not ce or not ce.get("list"):
            continue
        walk_commands(ce["list"], "CommonEvents.json", f"CE{ce['id']}",
                      rows, all_rows, json_rows)


def extract_database(data_dir, rows, all_rows, json_rows):
    for db in DB_FILES:
        path = os.path.join(data_dir, f"{db}.json")
        data = json.load(open(path, encoding="utf-8-sig"))
        for entry in data:
            if not entry:
                continue
            eid = entry.get("id")
            for field in DB_FIELDS:
                val = entry.get(field) or ""
                if field == "note" and not has_jp(val):
                    continue  # notes are mostly plugin data; keep only JP notes
                rid = f"DB_{db}_{eid}_{field}"
                ctx = f"{db}.json #{eid}"
                if field == "name":
                    ctx += f" ({entry.get('name', '')})"
                rtype = field if field != "note" else "note"
                emit(rows, all_rows, json_rows, rid, f"{db}.json", ctx,
                     rtype, val)


def extract_system(data_dir, rows, all_rows, json_rows):
    path = os.path.join(data_dir, "System.json")
    d = json.load(open(path, encoding="utf-8-sig"))
    emit(rows, all_rows, json_rows, "SYS_gameTitle", "System.json",
         "game title", "system", d.get("gameTitle") or "")
    emit(rows, all_rows, json_rows, "SYS_currencyUnit", "System.json",
         "currency unit", "system", d.get("currencyUnit") or "")
    for key in ("elements", "skillTypes", "weaponTypes", "armorTypes",
                "equipTypes"):
        for i, val in enumerate(d.get(key) or []):
            if val:
                emit(rows, all_rows, json_rows, f"SYS_{key}_{i}",
                     "System.json", key, "system", val)
    terms = d.get("terms") or {}
    for cat, vals in terms.items():
        if isinstance(vals, dict):
            for k, v in vals.items():
                if isinstance(v, str):
                    emit(rows, all_rows, json_rows, f"SYS_terms_{cat}_{k}",
                         "System.json", f"terms.{cat}", "system", v)
        elif isinstance(vals, list):
            for i, v in enumerate(vals):
                if isinstance(v, str):
                    emit(rows, all_rows, json_rows,
                         f"SYS_terms_{cat}_{i}", "System.json",
                         f"terms.{cat}", "system", v)


def extract_plugins(plugins_path, rows, all_rows, json_rows):
    text = open(plugins_path, encoding="utf-8-sig").read()
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1:
        print("  !! could not parse plugins.js", file=sys.stderr)
        return
    try:
        plugins = json.loads(text[start:end + 1])
    except json.JSONDecodeError as e:
        print(f"  !! plugins.js JSON parse failed: {e}", file=sys.stderr)
        return
    for plug in plugins:
        pname = plug.get("name", "?")
        for key, val in (plug.get("parameters") or {}).items():
            if not isinstance(val, str) or not has_jp(val):
                continue
            rid = f"PLUGIN_{pname}_{key}"
            emit(rows, all_rows, json_rows, rid, "js/plugins.js",
                 f"plugin {pname}", "plugins", val)


def write_tsv(path, header, rows):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(header + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")


def main():
    global args
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default="www/data",
                    help="game data dir (default: www/data)")
    ap.add_argument("--out", default="docs/text",
                    help="output dir (default: docs/text)")
    ap.add_argument("--plugins", default="www/js/plugins.js",
                    help="path to js/plugins.js (default: www/js/plugins.js)")
    ap.add_argument("--all", action="store_true",
                    help="also dump strings without Japanese characters")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    header = "id\tfile\tcontext\ttype\tjapanese\ttranslation"
    rows = {k: [] for k in ("dialogue", "choice", "name", "description",
                            "script", "system", "plugins", "note")}
    all_rows = []
    json_rows = {}

    extract_maps(args.data, rows, all_rows, json_rows)
    extract_common_events(args.data, rows, all_rows, json_rows)
    extract_database(args.data, rows, all_rows, json_rows)
    extract_system(args.data, rows, all_rows, json_rows)
    extract_plugins(args.plugins, rows, all_rows, json_rows)

    for kind, r in rows.items():
        write_tsv(os.path.join(args.out, f"{kind}.tsv"), header, r)
    write_tsv(os.path.join(args.out, "all.tsv"), header,
              sorted(all_rows, key=lambda x: (x[1], x[0])))
    with open(os.path.join(args.out, "all.json"), "w", encoding="utf-8") as fh:
        json.dump(json_rows, fh, ensure_ascii=False, indent=1)

    n = sum(len(r) for r in rows.values())
    print(f"Output: {os.path.abspath(args.out)}")
    for kind, r in sorted(rows.items()):
        print(f"  {kind:10s} {len(r):6d} strings")
    print(f"  {'TOTAL':10s} {n:6d} strings, "
          f"{sum(len(j['japanese']) for j in json_rows.values()):6d} JP chars")


if __name__ == "__main__":
    main()
