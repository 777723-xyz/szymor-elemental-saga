#!/usr/bin/env python3
"""Apply translations from a TSV back into RPG Maker MV game data.

Usage:
    python3 tools/inject_text.py docs/text/translated.tsv
        [--data www/data] [--plugins www/js/plugins.js] [--apply-scripts]

Input TSV: same columns as docs/text/all.tsv
(id, file, context, type, japanese, translation). Rows with an empty
translation or translation == japanese are skipped.

Behaviour:
- Backs up every modified file to docs/text/backups/<timestamp>/ first.
- Syncs the display text of choice branches (command 402, params[1]) from the
  translated 102 choices (branch matching in MV 1.6.1 is by INDEX, but the
  editor displays this text, so it is kept consistent).
- Rows of type "script" (eval'd script lines) are never applied unless
  --apply-scripts is given -- machine-altering code is dangerous.
- Rows of type "note" are applied but reported separately for review.
"""
import argparse
import json
import os
import re
import shutil
import time

DB_FILES = ("Actors", "Classes", "Skills", "Items", "Weapons",
            "Armors", "Enemies", "States", "Troops")
SYSTEM_ARRAYS = ("elements", "skillTypes", "weaponTypes", "armorTypes",
                 "equipTypes")
TERM_ARRAY_CATS = ("basic", "commands", "params")

MAP_ID_RE = re.compile(r"^MAP(\d+)_e(\d+)_p(\d+)_(\d+)(?:_c(\d+))?$")
CE_ID_RE = re.compile(r"^CE(\d+)_(\d+)$")
DB_ID_RE = re.compile(r"^DB_(\w+)_(\d+)_(name|description|note)$")


def load_tsv(path):
    """Return (header, rows) with rows as dicts keyed by header."""
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh]
    header = lines[0].split("\t")
    rows = []
    for ln in lines[1:]:
        if not ln.strip():
            continue
        rows.append(dict(zip(header, ln.split("\t"))))
    return header, rows


def load_json(path):
    return json.load(open(path, encoding="utf-8-sig"))


def save_json(path, data):
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False,
              indent=2)


def find_plugins(plugins_path):
    """Parse the $plugins array from plugins.js; returns (prefix, plugins, suffix)."""
    text = open(plugins_path, encoding="utf-8-sig").read()
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1:
        raise SystemExit(f"cannot parse {plugins_path}")
    return text[:start], json.loads(text[start:end + 1]), text[end + 1:]


def patch_text(cmd, rtype, t):
    """Patch one event command in place; returns True on success, False if the
    command does not match the expected type (caller records a warning)."""
    if rtype == "dialogue":
        if cmd["code"] not in (401, 405):
            return False
        cmd["parameters"][0] = t
    elif rtype == "name":
        if cmd["code"] != 320:
            return False
        cmd["parameters"][1] = t
    else:
        return False
    return True


def apply_to_maps(data_dir, pending, state):
    by_file = {}
    for r in pending:
        m = MAP_ID_RE.match(r["id"])
        if not m:
            continue
        by_file.setdefault(f"Map{int(m.group(1)):03d}.json", []).append(r)

    for fname, rows in sorted(by_file.items()):
        path = os.path.join(data_dir, fname)
        data = load_json(path)
        changed = False
        for row in rows:
            rid = row["id"]
            m = MAP_ID_RE.match(rid)
            mapid, ei, pi, idx = (int(m.group(1)), int(m.group(2)),
                                  int(m.group(3)), int(m.group(4)))
            ci = m.group(5)
            if mapid != int(fname[3:6]):
                state["warnings"].append(f"{rid}: map id/file mismatch")
                continue
            cmd = data["events"][ei]["pages"][pi]["list"][idx]
            t = row["translation"]
            rtype = row["type"]
            if rtype == "choice":
                if cmd["code"] != 102 or ci is None:
                    state["warnings"].append(
                        f"{rid}: expected 102 choice, got code {cmd['code']}")
                    continue
                cmd["parameters"][0][int(ci)] = t
                # Sync the display text of every matching 402 branch
                # (params[1]) in this choice block. Branch commands and their
                # nested content share indent >= the 102; the block ends at the
                # first same-indent non-branch command (e.g. another 102).
                lst = data["events"][ei]["pages"][pi]["list"]
                block_indent = cmd["indent"]
                for j in range(idx + 1, len(lst)):
                    c = lst[j]
                    if c["indent"] < block_indent:
                        break
                    if c["indent"] > block_indent:
                        continue  # nested branch content
                    if c["code"] == 402 and c["parameters"][0] == int(ci):
                        c["parameters"][1] = t
                    elif c["code"] not in (402, 403):
                        break  # left the choice block
            elif not patch_text(cmd, rtype, t):
                state["warnings"].append(
                    f"{rid}: type/code mismatch (code {cmd['code']}, type {rtype})")
                continue
            changed = True
            state["applied"].append((rid, fname))
        if changed:
            save_json(path, data)
            state["modified"].add(fname)


def apply_to_common_events(data_dir, pending, state):
    rows = [r for r in pending if r["type"] in ("dialogue", "name")]
    if not rows:
        return
    path = os.path.join(data_dir, "CommonEvents.json")
    data = load_json(path)
    by_id = {ce["id"]: ce for ce in data if ce}
    changed = False
    for row in rows:
        m = CE_ID_RE.match(row["id"])
        if not m:
            continue
        ceid, idx = int(m.group(1)), int(m.group(2))
        ce = by_id.get(ceid)
        if not ce or idx >= len(ce["list"]):
            state["warnings"].append(f"{row['id']}: not found")
            continue
        if not patch_text(ce["list"][idx], row["type"], row["translation"]):
            state["warnings"].append(f"{row['id']}: type/code mismatch")
            continue
        changed = True
        state["applied"].append((row["id"], "CommonEvents.json"))
    if changed:
        save_json(path, data)
        state["modified"].add("CommonEvents.json")


def apply_to_database(data_dir, pending, state):
    db_rows = [r for r in pending if r["id"].startswith("DB_")]
    if not db_rows:
        return
    cache = {}
    changed = set()
    for row in db_rows:
        m = DB_ID_RE.match(row["id"])
        if not m:
            state["warnings"].append(f"{row['id']}: malformed DB id")
            continue
        fname, eid, field = m.group(1), int(m.group(2)), m.group(3)
        if fname not in DB_FILES:
            state["warnings"].append(f"{row['id']}: unknown database {fname}")
            continue
        path = os.path.join(data_dir, f"{fname}.json")
        if path not in cache:
            cache[path] = load_json(path)
        entry = next((e for e in cache[path] if e and e.get("id") == eid), None)
        if entry is None:
            state["warnings"].append(f"{row['id']}: entry {eid} not in {fname}.json")
            continue
        if row["type"] == "note":
            state["skipped"].append((row["id"], f"{fname}.json", "note applied"))
        entry[field] = row["translation"]
        changed.add(path)
        state["applied"].append((row["id"], f"{fname}.json"))
    for path in changed:
        save_json(path, cache[path])
        state["modified"].add(os.path.basename(path))


def apply_to_system(data_dir, pending, state):
    rows = [r for r in pending if r["id"].startswith("SYS_")]
    if not rows:
        return
    path = os.path.join(data_dir, "System.json")
    d = load_json(path)
    changed = False
    for row in rows:
        rid, t = row["id"], row["translation"]
        if rid == "SYS_gameTitle":
            d["gameTitle"] = t
        elif rid == "SYS_currencyUnit":
            d["currencyUnit"] = t
        elif rid.startswith("SYS_terms_messages_"):
            d["terms"]["messages"][rid[len("SYS_terms_messages_"):]] = t
        else:
            m = re.match(r"^SYS_terms_(\w+)_(\w+)$", rid)
            if m and m.group(1) in TERM_ARRAY_CATS:
                d["terms"][m.group(1)][int(m.group(2))] = t
            else:
                m = re.match(r"^SYS_(\w+)_(\d+)$", rid)
                if m and m.group(1) in SYSTEM_ARRAYS:
                    d[m.group(1)][int(m.group(2))] = t
                else:
                    state["warnings"].append(f"{rid}: cannot map to System.json")
                    continue
        changed = True
        state["applied"].append((rid, "System.json"))
    if changed:
        save_json(path, d)
        state["modified"].add("System.json")


def apply_to_plugins(plugins_path, pending, state):
    rows = [r for r in pending if r["id"].startswith("PLUGIN_")]
    if not rows:
        return
    prefix, plugins, suffix = find_plugins(plugins_path)
    param_map = {}
    for plug in plugins:
        for key in (plug.get("parameters") or {}):
            param_map[f"PLUGIN_{plug['name']}_{key}"] = (plug, key)
    changed = False
    for row in rows:
        hit = param_map.get(row["id"])
        if not hit:
            state["warnings"].append(f"{row['id']}: plugin param not found")
            continue
        hit[0]["parameters"][hit[1]] = row["translation"]
        changed = True
        state["applied"].append((row["id"], "js/plugins.js"))
    if changed:
        open(plugins_path, "w", encoding="utf-8").write(
            prefix + json.dumps(plugins, ensure_ascii=False, indent=1) + suffix)
        state["modified"].add("js/plugins.js")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tsv", help="translated TSV (copy of docs/text/all.tsv)")
    ap.add_argument("--data", default="www/data", help="game data dir")
    ap.add_argument("--plugins", default="www/js/plugins.js")
    ap.add_argument("--apply-scripts", action="store_true",
                    help="also apply type=script rows (dangerous)")
    ap.add_argument("--no-backup", action="store_true",
                    help="do not copy modified files to docs/text/backups")
    args = ap.parse_args()

    header, rows = load_tsv(args.tsv)
    if "translation" not in header:
        raise SystemExit("TSV has no 'translation' column")

    pending = []
    for r in rows:
        t = (r.get("translation") or "").strip()
        if not t or t == r.get("japanese"):
            continue
        if r.get("type") == "script" and not args.apply_scripts:
            continue
        r["translation"] = t
        pending.append(r)
    if not pending:
        raise SystemExit("no rows with translations to apply")

    state = {"applied": [], "skipped": [], "warnings": [], "modified": set()}
    apply_to_maps(args.data, pending, state)
    apply_to_common_events(args.data, pending, state)
    apply_to_database(args.data, pending, state)
    apply_to_system(args.data, pending, state)
    apply_to_plugins(args.plugins, pending, state)

    if state["modified"] and not args.no_backup:
        stamp = time.strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join("docs", "text", "backups", stamp)
        os.makedirs(backup_dir, exist_ok=True)
        for fname in state["modified"]:
            src = fname if os.path.exists(fname) else os.path.join(args.data, fname)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(backup_dir, os.path.basename(fname)))

    print(f"Applied {len(state['applied'])} strings across "
          f"{len(state['modified'])} files")
    per_file = {}
    for _, fname in state["applied"]:
        per_file[fname] = per_file.get(fname, 0) + 1
    for fname, n in sorted(per_file.items()):
        print(f"  {fname:24s} {n} strings")
    if state["skipped"]:
        print(f"Noted ({len(state['skipped'])}): "
              + ", ".join(s[1] for s in state["skipped"][:5]))
    if state["warnings"]:
        print(f"Warnings ({len(state['warnings'])}):")
        for w in state["warnings"][:30]:
            print(f"  !! {w}")


if __name__ == "__main__":
    main()
