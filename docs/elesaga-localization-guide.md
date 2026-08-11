# Elesaga (エレサガ) — English Localization Guide & Naming Reference

**Status:** Phase 0 draft — pending user confirmation of the decision list (see
"Open decisions" at the end).
**Scope:** private-use English patch; source = `docs/text/all.tsv` (14,611 strings).

## Localization policy (user-approved)
1. **Target:** natural, classic JRPG English. The game is a "王道で熱くてかわいい"
   (classic, hot-blooded, cute) story-driven RPG — keep that warmth.
2. **Names:** romanize (Hepburn-style, no macrons). Katakana loanwords become
   their English etymon (`ファイア` → Fire, `チェインメイル` → Chain Mail).
   Kanji-compound words are translated to English meaning (`傷薬` → Healing Herb).
   Katakana personal names stay romanized (`ホムラ` → Homura).
3. **Fidelity:** keep as close to the original as possible; do NOT tone down any
   content.
4. **Control codes** (`\c[n]`, `\i[n]`, `\v[n]`, `\N[n]`, `%1`, …) are preserved
   untouched in every string.
5. **Speaker prefixes** (`ピピン：`) become `Name:` (half-width colon) at the
   start of the line.
6. **Line length:** English runs longer — lines that exceed the message window
   budget (780px / 612px with face) get `\n` breaks inserted by the fit checker.

## Main cast (proposed romanization)
| Japanese | Proposed | Notes |
|---|---|---|
| ウィン | Win | hero |
| ホノオ | Hono | 炎 (flame) — final 'o' kept but unmarked |
| ナガレ | Nagare | 流れ (flow/stream), wind crest |
| ピピン | Pipin | |
| ロイ | Roi | (decision: Roi vs Roy) |
| トリカゼ | Torikaze | |
| マハリ | Mahari | |
| レイモンド | Raymond | scout |
| サクソン | Saxon | acting knight-captain |
| フレイム王 | King Flame | ruler of Flame Kingdom |
| ウィンダム王 | King Windam | ruler of Windam Kingdom |
| ホムラ | Homura | |
| シズク | Shizuku | |
| オタキ | Otaki | 様 → Lady Otaki |
| アルドン | Aldon | |

## Antagonists / recurring
| Japanese | Proposed | Notes |
|---|---|---|
| ミケーネ | Mycenae | from the ancient city |
| ダフィール | Dafill | 魔王/大魔王 → Demon King / Great Demon King |
| ピケピケ | Pikepike | comic grand mage |
| ナウー / ナウ― | Nau | typo variant merged (both spellings exist in data) |
| 青龍 | Seiryu | also "Blue Dragon" alternative |
| ヤバミネーション | Yabamination | pun on やばい; keep the pun |
| ザイール | Zaire | |
| 操られたピピン | Brainwashed Pipin | enemy variant |
| 近衛兵ライトニング/ブロウニング/クリス | Royal Guard Lightning / Browning / Chris | |
| 騎士団長代行サクソン | Saxon, Acting Knight-Captain | prefix in dialogue |
| サチコ / サヨコ | Sachiko / Sayoko | |

## Speaker-prefix roles (used in dialogue)
`市民` Citizen · `近衛兵` Royal Guard · `宿屋の主人/女将` Innkeeper /
Innkeeper's Wife · `鍛冶屋主人` Blacksmith · `倉庫番` Warehouse Keeper ·
`物乞いの子` Beggar Boy · `料理人助手` Cook's Assistant · `大臣` Minister ·
`行政官` Administrator · `採石場の` Quarry … · `関所の見張り` Gate Watchman ·
`巡回兵/駐屯隊長/新米兵士/休憩中の兵士` Patrolman / Garrison Captain / Rookie
Soldier / Off-Duty Soldier · `偵察兵` Scout · `王宮の職人` Royal Craftsman ·
`古書収集家` Antiquarian · `行商人` Peddler · `錬金術師` Alchemist ·
`道具屋/武器屋` Item Shop / Weapon Shop · `城門係` Gatekeeper · `板前` Chef ·
`果物売りの少年` Fruit Boy · `旅の占い師` Traveling Fortune-Teller ·
`レストラン主人` Restaurant Owner · `野良犬` Stray Dog · `古いページ` Old Page ·
`？` ? · `若かりし頃のロイ` Young Roi · `ピケピケの声` Pikepike's Voice ·
`イヌ` Dog

## Kingdoms & geography
| Japanese | Proposed |
|---|---|
| エレメント大陸 / 光の大陸 / 暗黒大陸 | Element Continent / Continent of Light / Dark Continent |
| フレイム王国 / ウィンダム王国 / セイリュー | Flame Kingdom / Windam Kingdom / Seiryu |
| ウィンダム城下町, フレイム城下町 | Windam Castle Town, Flame Castle Town |
| 西の監視塔 | West Watchtower (1F–roof) |
| フレイムへの関所 | Gate to Flame |
| セイリュー領主の村 | Seiryu Lord's Village |
| 龍のお社 / お社の洞窟 / 龍の穴 | Dragon Shrine / Shrine Cave / Dragon's Lair |
| 呪われた洞窟 (2/3/4, 氷) | Cursed Cave (2/3/4, Ice) |
| 暗黒の塔 | Dark Tower |
| 光の柱 (二回目, ウィンダム, フレイム, セイリュー) | Pillar of Light (Second Visit, Windam, Flame, Seiryu) |
| 崩壊 / ＥＮＤ / 裏 | Ruined / END / Rear (map suffixes) |
| 南の旧坑道, 南の採石場, 南の遺跡 | Old Southern Mine, Southern Quarry, Southern Ruins |
| 砂漠の廃墟 | Desert Ruins |
| 騎士団駐屯本部 | Knight Order Garrison HQ |
| 旅人の宿 / マーケット / 寂れた民家 | Traveler's Inn / Market / Ramshackle House |

## Conventions for content classes
- **Skills:** translate meaning (Katakana → English etymon; kanji → meaning).
  Per-enemy variants keep the owner: `足払いナウー` → "Nau Leg Sweep",
  `ミケーネムチ振り回し` → "Mycenae Whip Swing".
  Key terms: ハヤテ Hayate · カマイタチ Kamaitachi · テッペキ Iron Wall ·
  シップウ Gale · イカヅチ Thunderclap · ツナミ Tsunami · バクハツ Explosion ·
  イヤシ Heal · イノチ Life · ドコンジョウ Guts · マンキンタン Mankintan ·
  真・つばめ返し True Swallow Reversal.
- **Items:** translate meaning. Elements: 力 Power / 守り Guard / 素早さ
  Swiftness / 魔力 Magic / 精神 Mind / いのち Life / 気力 Vigor / 風 Wind /
  火 Fire / 水 Water / 闇 Dark. Materials: ふつう Common / かなりいい Fine /
  きちょう Precious / さいこう Supreme / 究極 Ultimate.
- **Weapons/Armors:** katakana → English; **famous blades stay romanized**
  (decision): 村雨/ムラクモ Murasame/Murakumo · 蜻蛉斬 Tonbogiri ·
  にっかり青江 Nikkari Aoe · 藤四郎 Toshiro · 骨喰み Honebami · 脇差 Wakizashi ·
  打刀 Uchigatana · 青江の大太刀 Aoe's Odachi · ロイスペシャル Roi Special ·
  ゾモロドネガル Zomolod Negal (fantasy, romanize).
- **Enemies:** translate meaning (`人食いコウモリ` → Man-eating Bat,
  `雷牛` → Thunder Bull). Real animal names keep Japanese (マムシ Mamushi,
  ハブ Habu, アオダイショー Aodaisho, ヒノタマ Hinotama).
- **States:** 戦闘不能 Incapacitated · 防御 Guard · 不死身 Immortal · 毒 Poison ·
  暗闇 Blind · 沈黙 Silence · 激昂 Enrage · 混乱 Confusion · 魅了 Charm ·
  睡眠 Sleep · 猛毒 Venom · 転倒 Knock Down · 気絶 Stun · 魔力暴走 Magic Overload ·
  反撃の構え Counter Stance · ナウーの力 Power of Nau.
- **Classes:** 新米騎士 Novice Knight · 騎士隊長 Knight Captain ·
  Xの紋章の継承者 Inheritor of the X Crest · さいご Final ·
  忍者犬 Ninja Dog · 大地の勇者 Hero of the Land.

## Working files
- `docs/text/glossary.tsv` — full 611-entry glossary (DB + dialogue speakers),
  empty `proposed`/`notes` columns to fill during translation.
- `docs/text/all.tsv` — translation workspace (14,611 rows).

## Open decisions (awaiting user)
1. ロイ → **Roi** (default) or Roy?
2. Honorific 様 → **Lady/Lord** (default) or keep `-sama`?
3. フレイム王 / ウィンダム王 → **King Flame / King Windam** (default) or
   Flame King / the King of Windam?
4. Famous blades → **keep romanized** (default) or translate meanings?
5. ミケーネ → **Mycenae** (default) or Mykene?
6. ダフィール → **Dafill** (default) or Dafiel?
7. 青龍 → **Seiryu** (default) or Azure Dragon?
8. 操られたピピン → **Brainwashed Pipin** (default) or "Pipin, Possessed"?
9. Comic names ピケピケ→Pikepike, ヤバミネーション→Yabamination, ナウー→Nau —
   OK?
10. Anything else to add or override (names you already know from playing)?
