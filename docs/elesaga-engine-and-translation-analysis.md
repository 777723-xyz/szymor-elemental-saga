# Elesaga (エレサガ Elemental Saga) — Engine & Translation Analysis

**Objective:** Identify the game engine/runtime of the downloaded Japanese game and assess the feasibility and steps for translating it.

**Scope:** Local sample in `/home/szymek/repos/elemental-saga` (extracted game, dated 2020-06-25). No modification of game data performed.

**Date:** 2026-08-11

## Environment & Tools
- OS: Linux 7.1
- Tools used: `file`, `strings`, `python3`, `grep`. (Ghidra/jadx not needed — game data is plaintext.)
- Sandbox: none required; static analysis only.

## Game Identification
| Item | Value |
|---|---|
| Title | エレサガ Elemental Saga 紋章物語 (Elesaga / Monshou Monogatari), ver 2.51 |
| Author | 西園寺ハムカツ (WGT Saionji Hamkatsu) |
| Origin | FreeM! (freem.ne.jp), brand 9933 |
| ReadMe note | Original made in RPGツクール5 (RPG Maker 95) ~18 years ago; remade in MV. ~4h story, story-focused RPG. |

## Engine & Runtime (verified locally)
- **Engine: RPG Maker MV (RPGツクールMV), core version 1.6.1**
  - Evidence: `www/js/rpg_core.js` → `RPGMAKER_VERSION = "1.6.1"`; standard `www/data/*.json` format (Maps, Actors, Skills, Items, Troops…); `www/js/libs/pixi.js` = Pixi.js **v4.5.4** (matches MV 1.6.x); `fonts/mplus-1m-regular.ttf`.
- **Runtime: NW.js 0.18.7 (win32, ia32)** — FreeM! "Multi Deployment System" packaging.
  - Evidence: `01_GameStart.exe` = PE32 i386 GUI (renamed `nw.exe` wrapper); `nw.dll`/`nw_elf.dll`/`node.dll`; build path `e:\build\nw18_win32\...`; ReadMe marker `Multi Deployment System:20161126--1.01--v0.18.7-win-ia32`.
- **Rendering:** HTML5 (WebGL/Canvas via Pixi), window 816×624. Game is browser-runnable from `www/index.html`.

## Encryption / Data Protection
- **None.** `System.json` has no `hasEncryptedImages`/`hasEncryptedAudio` flags; all `data/*.json` files are plaintext UTF-8 (with BOM); images (PNG) and audio (OGG) are in open folders, not archived.

## Text Volume (counted from data)
| Source | Amount |
|---|---|
| Show Text commands (code 401, maps + common events) | 13,183 |
| Scrolling text lines (code 405) | 452 |
| Total dialogue characters (JP) | ~166,000 |
| Database `name`/`description` fields (Actors/Skills/Items/Weapons/Armors/Enemies…) | ~11,000 additional chars |
| UI terms/messages | `System.json` → `terms` (basic/commands/params/messages), e.g. 攻撃/アイテム/セーブ/タイトル画面へ… |
| Plugin UI strings | A handful, in `www/js/plugins.js` params (e.g. RetryBattle: 再びバトル！/ゲームデータをロード/バトルに敗れた…; MakeScreenCapture watermark ⒸWGTハムカツ 2019 紋章物語 エレサガ) |
| In-game README | `www/ridomi.txt` (root `02_ReadMe.txt` also Japanese) |

Game size: 98 maps (95 with events), 40 actors, 180 skills, 60 items / 60 weapons / 60 armors, 100 enemies, 150 troops, 4 common events.

## Translation Difficulty: LOW–MODERATE (technically easy)
Why low risk:
- No encryption or custom packing — text is plain, standards-compliant RPG Maker MV JSON.
- Text is cleanly separated from code; every string lives in data files, not binaries.
- Known community tooling and workflows exist for RPG Maker MV (text extract/inject scripts, MT engines like DeepL/ChatGPT, tools such as Translator++).
- The NW.js/Windows wrapper is irrelevant — data editing alone changes the language.

Main challenges are linguistic + layout, not technical:
- ~177k JP characters of dialogue; needs translation + human QA (a few days to weeks depending on quality bar).
- English is typically longer: message window is 816 px at font size 28, so lines must be re-wrapped to avoid overflow (MV wraps at ~half the window width; plan to cap ~34–42 chars/line and re-flow paragraphs).
- Must preserve RPG Maker MV control codes exactly: `\c[n]`, `\i[n]`, `\v[n]`, `\V[n]`, `\N[n]`, `\n`, `\`, `\G`, `\>`, `\<`, `%1` placeholders, and name-prefix syntax (「名：」before text opens a name window).
- Keep JSON valid and keep UTF-8 BOM encoding for safe reads.

## Required Steps
1. **Extract:** script over `www/data/Map*.json` + `CommonEvents.json` (codes 401/405), database `name`/`description` fields, `System.json` `terms`/`messages`, and UI strings in `js/plugins.js` parameters. Export to a translation table (TSV/XLIFF).
2. **Translate:** machine translate (DeepL/ChatGPT) then human proofread; keep codes/placeholders intact; decide on name romanization (ロイ=Roi, ホノオ=Hono, ナガレ=Nagare…).
3. **Inject:** write back into the same JSON structure/encoding. Validate JSON and re-verify that no control code was mangled.
4. **Fit text:** re-wrap long English lines, adjust message-window widths/line breaks if needed; consider switching `fonts/gamefont.css` if target language glyphs are missing (mplus-1m includes Latin; Chinese/others may need a font swap — YEP_CoreEngine already exposes `Chinese Font`/`Korean Font` params).
5. **Test:** run via `01_GameStart.exe` (Windows/Wine) or open `www/index.html` in a browser; check dialogue, menus, battle messages, save/load, and plugin screens (retry battle, gamepad/keyboard config).
6. **Redistribution caveat:** `02_ReadMe.txt` states the data is licensed ("DO NOT use this game's data", FreeM! terms apply). A private patch is low-risk; **public distribution requires author permission** (PliCy/Twitter: WGT 西園寺ハムカツ).

## Conclusion
Engine: **RPG Maker MV 1.6.1** running under **NW.js 0.18.7** (FreeM! Multi Deployment System package). Translation is **very feasible** — all text is plaintext JSON with zero encryption; effort is dominated by translation volume (~177k chars) and line-fitting, not reverse engineering.

## Translation Pipeline (complete, tested round-trip)

### 1. Extract
`python3 tools/extract_text.py` — dumps every translatable string into `docs/text/`:
- `dialogue.tsv` (12,634) + `choice.tsv` (974) — event text, choices; `name.tsv` (592) — change-name commands
- `description.tsv` (226), `note.tsv` (28), `system.tsv` (116 — title/terms/messages), `plugins.tsv` (41 — plugin UI strings)
- `all.tsv` (merged, sorted by file) and `all.json` (master table keyed by stable IDs)
- Total: **14,611 strings / ~187k JP chars**. `script.tsv` is empty (no translatable strings in script calls).
- Columns: `id  file  context  type  japanese  translation`. Add `--all` to include non-Japanese strings; `--out` to change output dir.

### 2. Translate
Fill the `translation` column of a copy of `docs/text/all.tsv` (e.g. `docs/text/translated.tsv`).
Leave the `japanese` column untouched. Keep control codes intact: `\c[n]`, `\i[n]`,
`\v[n]`, `\N[n]`, `\n`, `\`, `\>`, `\<`, `%1` placeholders.

### 3. Check text fit
`python3 tools/check_text_fit.py docs/text/translated.tsv`
- MV 1.6.1 does **not** auto-wrap; characters wider than the message window are clipped.
- Measures every line with the real font (mplus-1m-regular.ttf, size 28):
  budget **780px** (816 − 2×18 padding), **612px** when a face image is shown (x=168).
- Resolves `\N[n]`/`\P[n]` from Actors.json (using the translated name when available),
  `\i[n]` icons (32px), `\G` currency; `\V[n]`/`\v[n]` are width *estimates* (flagged).
- Verified against the original Japanese: it flags 77 already-overflowing lines that the
  author shipped, confirming the measurement model.

### 4. Inject
`python3 tools/inject_text.py docs/text/translated.tsv`
- Applies rows whose translation is non-empty and differs from the Japanese.
- Syncs choice-branch text: branch commands (402) match by **index**, so their display
  text (`params[1]`) is mirrored from the translated 102 entry automatically.
- `type=script` rows are skipped unless `--apply-scripts` (code — dangerous).
- `type=note` rows are applied but listed under "Noted" for manual review.
- Backs up every modified file to `docs/text/backups/<timestamp>/` (`--no-backup` to skip).
- Tested round-trip on a copy: translations land on the correct IDs, JSON stays valid,
  and re-extraction shows exactly the translated rows.

### Known quirks / leftovers
- Choice branches (code 402) are matched by **index** (`params[0]`), not by text.
- `docs/text/plugin.tsv` (lowercase) is a stale leftover from an earlier run; ignore it.
