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
- Escapes in the translation column are unescaped when applied: `\n` becomes a real
  newline (the engine's line break — a literal `\n` is swallowed by MV and long lines
  get clipped), `\t` a tab, `\\` a literal backslash.
- Tested round-trip on a copy: translations land on the correct IDs, JSON stays valid,
  and re-extraction shows exactly the translated rows.

### 5. Rebuild the English build
The English build (`build/english/www`) is **not part of the repo** — it is a
generated artifact (gitignored) and can be reproduced from the tracked sources:
- `www/` — the original Japanese game, plus the committed English-side engine/UI
  fixes: `js/plugins/EndGme.js` (title-screen "Close Game" parameter key),
  `js/rpg_scenes.js` (3-line help window), `js/rpg_managers.js` (mobile audio:
  use OGG wherever the browser can decode it — see Known quirks),
  `index.html` (<title>Crest Story</title>).
- `docs/text/translated.tsv` — the full translation table (extracted rows + English).
- `tools/` — the pipeline scripts.

**Fresh rebuild** (all other files are byte-copies of `www`):
```sh
mkdir -p build/english
cp -r www build/english/
python3 tools/inject_text.py docs/text/translated.tsv \
    --data build/english/www/data \
    --plugins build/english/www/js/plugins.js
```
The injector touches **only** `www`-copy paths: `data/*.json` (dialogue, choices,
database texts, troop names, System terms, …) and `js/plugins.js` (plugin
parameter values).
Everything else must come from the `cp -r www` step, which is also what carries the
EndGme / help-window / index.html fixes above.

**Incremental rebuild** (only translations changed): re-run the same
`inject_text.py` command against the existing `build/english/www` — it overwrites
the translated fields in place and does not need the copy step. Modified files are
backed up to `docs/text/backups/<timestamp>/`; pass `--no-backup` to skip.

**Verify**
- `python3 tools/check_text_fit.py docs/text/translated.tsv` — 0 overflowing
  dialogue lines (budget 780px / 612px with face).
- The regenerated data itself can be measured with the same font (dialogue ≤ 4
  lines, item/skill/weapon/armor descriptions ≤ 3 help-window lines, actor
  profiles ≤ 2 status-window lines).
- Playtest by opening `build/english/www/index.html` in a browser.

**Note:** RPG Maker MV serializes actor profiles into save files, so an old save
created with a previous build keeps showing the old profile text. Start a new
game (or discard old saves) after a rebuild.

### Known quirks / leftovers
- Choice branches (code 402) are matched by **index** (`params[0]`), not by text.
- `docs/text/plugin.tsv` (lowercase) is a stale leftover from an earlier run; ignore it.
- The `EndGme` plugin (title-screen "Close Game" command) originally read its
  parameter via `PluginManager.parameters('gameEnd')` although the plugin is
  registered as `EndGme`, so the entry always fell back to the Japanese default.
  The key is fixed in `www/js/plugins/EndGme.js` (and mirrored in the build); a
  freshly copied build must carry that fix too.
- The `UCHU_MobileOperation` plugin's virtual-button images were missing
  (`img/system/DirPad.png`, `ActionButton.png`, `CancelButton.png`), which made
  Android builds show a blurry "Button Image was Not Found" error screen
  (`Graphics.printError` blur filter). Re-created 2026-08-11 as simple square
  PNGs in `www/img/system/`; they ride along via the `cp -r www` copy step.
- Mobile audio fix (2026-08-11): `AudioManager.audioFileExt()` in
  `www/js/rpg_managers.js` forced `.m4a` on any mobile UA
  (`canPlayOgg() && !Utils.isMobileDevice()`), but the project ships only OGG
  (and Android Chrome can decode OGG). That made mobile browsers silent while
  "Desktop site" mode worked. The check is now just `if (WebAudio.canPlayOgg())`
  so OGG is used wherever the browser can decode it. Mirrored in the build
  (`build/english/www/js/rpg_managers.js`, CRLF) — a fresh `cp -r www` copy must
  carry this fix too.

### Translation progress (FINAL)
- **18,460 / 18,461 strings translated.** The single untranslated string is the
  disabled SceneGlossary plugin's config blob.
- The Japanese filter of `extract_text.py` was widened to CJK punctuation, so
  punctuation-only dialogue ("…。", "？：", "？？？" ...) is now extracted and
  translated (491 rows added; "…。" -> "...", "？：" -> "?:", etc.).
- Troop names are extracted (`TROOP<n>_name`) and applied by the injector —
  138 named troops (12 troops have no name). They were previously translated
  by hand in the build only, so a rebuild lost them.
- Full coverage of the RPG Maker MV text surface, including:
  - Map/CommonEvent/Troop event commands (dialogue, choices, names, scripts)
  - DB name/description/note, use messages (message1/2), state messages
    (message1-4), actor nickname/profile
  - System terms/messages, elements/types, switches, variables
  - Map display names, event names/notes, MapInfos names, plugin parameters
- Quality gates passed: **0 in-game text rows remain Japanese**; all JSON valid;
  round-trip verified (re-extraction of the English build shows English).
- Only remaining Japanese: invisible dev metadata (tileset/animation names),
  RetryBattle plugin script identifiers (code — must not be translated), and the
  U+3000 indentation spacers inside Japanese scrolling-text layout.
- Line fitting (Phase 2 + 2026-08-11 rewrap): `wrap_text.py` now uses a balanced
  (minimum-raggedness) wrap that avoids single-word orphan lines, re-optimizes
  existing breaks, and also fits item/skill/weapon/armor descriptions to the
  3-line help window (message boxes cap at 4 lines). Verified: **0** overflowing
  lines, **0** rows over the line caps, and byte-identical text (breaks only move).
- Newline fix (2026-08-11): the injector used to store literal `\n` in the data,
  which MV renders as nothing, so long English lines overflowed the message window
  and were clipped. The injector now writes real newlines; the regenerated build was
  measured on the actual data (15,765 dialogue commands) with **0** overflows.
- Layout polish (2026-08-11): actor profiles were condensed to fit the status
  window's 2-line profile area; the menu/battle help windows were enlarged to 3
  lines (`new Window_Help(3)` in `www/js/rpg_scenes.js`); em-dashes are spaced
  (" — "); `index.html` <title> is "Crest Story" (it used to show the Japanese
  title until Scene_Boot set `document.title`).
- English build: `build/english/www` (gitignored, fully rebuildable — see
  "### 5. Rebuild the English build" above). Playtest by opening
  `build/english/www/index.html` in a browser.

### Baked-in image text audit (OCR-verified, 2026-08-11)
- `img/titles1/CrossedSwords.png`, `img/titles2/Medieval.png`: no text — the title
  string is drawn at runtime from `System.json` `gameTitle`, so it is translated
  by the pipeline (row `SYS_gameTitle`).
- `img/system/GameOver.png` ("GAME OVER") and `MadeWithMv.png` ("Powered by MV"):
  already English.
- No Japanese image assets need manual retouching.
- Optional manual text: `www/ridomi.txt` / root `02_ReadMe.txt` (Japanese
  distribution readmes) and the NW.js credits page (`credits/credits_nw.html`).
