#!/usr/bin/env python3
"""Fill batch 63: map event names/notes and display names."""
import csv
import os
import re

M = {
"泥棒はずれ": "Thief (Missed)",
"入り口": "Entrance",
"玉座の護衛右": "Throne Guard Right",
"玉座の護衛左": "Throne Guard Left",
"固いパン１個": "Hard Bread x1",
"ピピンに教えてもらう": "Learn from Pipin",
"サクソンの部屋出る": "Leave Saxon's Room",
"王の寝室の護衛本体": "King's Bedroom Guard (Main)",
"王の寝室の護衛ゆか": "King's Bedroom Guard (Floor)",
"民家": "House",
"ウィンダムの錬金術師": "Windam Alchemist",
"ウィンダム入り口兵": "Windam Gate Soldier",
"城下町北の巡回兵": "North Castle Town Patrolman",
"ウインダム城一階": "Windam Castle 1F",
"ウィンダムの大臣": "Windam Minister",
"ウィンダム城二階": "Windam Castle 2F",
"ウィンダム城三階": "Windam Castle 3F",
"宿屋の娘": "Innkeeper's Daughter",
"ウィンダム城バルコニー": "Windam Castle Balcony",
"パン屋父": "Baker Father",
"ウィンの母": "Win's Mother",
"パン屋の客1": "Bakery Customer 1",
"パン屋の客2": "Bakery Customer 2",
"道具屋の客": "Item Shop Customer",
"じいさん": "Old Man",
"ウィング": "Wing",
"錬金術師の店": "Alchemist's Shop",
"レストラン主人": "Restaurant Owner",
"駐屯本部": "Garrison HQ",
"駐屯隊長": "Garrison Captain",
"西の監視塔　一階": "West Watchtower 1F",
"西の監視塔　四階": "West Watchtower 4F",
"南の関所": "South Checkpoint",
"せきしょの　ひと": "Checkpoint Person",
"南の関所の見張り": "South Checkpoint Watchman",
"ドミトリー": "Dmitri",
"マックス": "Max",
"カイル": "Kyle",
"フレイム王　崩壊後": "King Flame (Post-Collapse)",
"廃墟": "Ruins",
"リマル": "Rimal",
"ロイの家入り口": "Roi's House Entrance",
"城下町花畑": "Castle Town Flower Garden",
"錬金術師の横": "Beside the Alchemist",
"釣をしてるひと": "Fishing Person",
"像の左": "Left of the Statue",
"オープニング最後": "Opening (Final)",
"ハリス": "Harris",
"ハリスの奥さん": "Harris's Wife",
"ハリスの娘さん": "Harris's Daughter",
"レストラン": "Restaurant",
"武器屋": "Weapon Shop",
"ピピン去る": "Pipin Departs",
"西の監視塔　最上階": "West Watchtower Top",
"ピケピケ初見": "Pikepike First Sight",
"E旧坑道入り繰り": "Old Mine Entrance (E)",
"旧坑道のピピン": "Pipin at the Old Mine",
"キノコ事件": "Mushroom Incident",
"オープニング１": "Opening 1",
"子供ロイ": "Young Roi",
"サクソン回想": "Saxon Flashback",
"ロイ西の監視塔": "Roi at West Watchtower",
"伝令": "Messenger",
"フレイムのレストラン": "Flame Restaurant",
"フレイムの道具屋": "Flame Item Shop",
"フレイムの宿屋": "Flame Inn",
"フレイムの武器屋": "Flame Weapon Shop",
"フレイムの民家": "Flame House",
"ガダ": "Gada",
"試練ホノオ": "Hono's Trial",
"流れ": "Flow",
"セイリューの宿屋": "Seiryu Inn",
"よろずや": "General Store",
"ぶきや": "Weapon Shop",
"セイリューよろず屋": "Seiryu General Store",
"セイリューの錬金術師の店": "Seiryu Alchemist's Shop",
"ヒノタマ": "Hinotama",
"ナガレ死体": "Nagare (Body)",
"デニー": "Denny",
"ウマル": "Umaru",
"自動実行": "Auto-Run",
"ジョッシュ": "Josh",
"ウィンダム王　崩壊後": "King Windam (Post-Collapse)",
"ロイ　崩壊後": "Roi (Post-Collapse)",
"サクソン崩壊後": "Saxon (Post-Collapse)",
"コッコ": "Kokko",
"ステイ": "Stay",
"ハング": "Hang",
"ロール": "Rohr",
"隠しダンジョン": "Hidden Dungeon",
"警備所": "Guard Post",
"警備所サクソン": "Saxon at the Guard Post",
"不気味な洞窟": "Eerie Cave",
"左ピロシキン": "Left: Piroshkin",
"右カメマル": "Right: Kamemaru",
"正面真ん中ヘヴィ": "Front Center: Heavy",
"たきびした": "Campfire (Down)",
"たきびみぎ": "Campfire (Right)",
"正面左スカイ": "Front Left: Sky",
"正面右クロウ": "Front Right: Crow",
"しだるた": "Sidarta",
"おうさま": "The King",
"どこかの大陸": "Some Continent",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "mapmeta.tsv"))


def norm(s):
    return re.sub(r"[ \u3000]+", " ", s).strip()


def main():
    keyed = {norm(k): v for k, v in M.items()}
    with open(PATH, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    filled = 0
    for r in rows:
        if (r.get("translation") or "").strip():
            continue
        t = keyed.get(norm(r["japanese"]))
        if t:
            r["translation"] = t
            filled += 1
    with open(PATH, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print("mapmeta.tsv filled", filled, "remaining",
          sum(1 for r in rows if not (r.get("translation") or "").strip()))


if __name__ == "__main__":
    main()
