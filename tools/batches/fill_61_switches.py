#!/usr/bin/env python3
"""Fill batch 61: switch/variable names and actor nicknames."""
import csv
import os
import re

S = {
"ポーションをもらう": "Received Potion",
"王様と話す": "Talked to King",
"サクソンと話す": "Talked to Saxon",
"サクソンの部屋出た": "Left Saxon's Room",
"ストロングと話した": "Talked to Strong",
"ピピンに教えてもらう": "Learned from Pipin",
"固いパン１個": "Hard Bread x1",
"レザーコート１着": "Leather Coat x1",
"イヌ倒した": "Defeated Dog",
"ロイを訪ねる": "Visit Roi",
"ピケピケ消える": "Pikepike Vanishes",
"ピケピケと会った": "Met Pikepike",
"旧坑道でピピン外れる": "Pipin Leaves at the Old Mine",
"旧坑道クリア": "Old Mine Cleared",
"ピピン離脱": "Pipin Departs",
"キノコ解決": "Mushroom Resolved",
"ポーション貰う": "Got Potion",
"ジョセフ解決": "Joseph Resolved",
"ロイに会え": "Go See Roi",
"ロイと話す": "Talk to Roi",
"ピピン歩く": "Pipin Walks",
"ピピン去った": "Pipin Left",
"王に報告に行け": "Report to the King",
"オープニング終わり": "Opening Done",
"ロイの父倒れる": "Roi's Father Falls",
"伝令くる": "Messenger Arrives",
"ロイ手を切る": "Roi Cuts His Hand",
"ロイの長話終わり！": "Roi's Long Talk Done!",
"フレイムへ行け": "Go to Flame",
"傷薬一個": "Healing Herb x1",
"万金丹一個": "Mankintan x1",
"南通れる": "South Passable",
"通行手形あげた": "Gave the Permit",
"フレイムへ出た": "Left for Flame",
"手形返った": "Permit Returned",
"ダガー貰った": "Got the Dagger",
"ホノオに会え": "Go See Hono",
"ナウ―倒す": "Defeat Nau",
"試練しよう": "Do the Trial",
"試練開始": "Trial Started",
"ホムラ登場": "Homura Appears",
"ホノオ考える": "Hono Thinks",
"ぐわーーー": "Gwaaaah",
"試練終り": "Trial Ended",
"ホムラ語る": "Homura Speaks",
"王様ごめん": "King's Apology",
"いぬおっけー": "Dog OK",
"いぬかくにん": "Dog Checked",
"火牛しぼう": "Flame Bull Dies",
"ナガレあーーー": "Nagare Aaaah",
"当主の家へ": "To the Head's House",
"オタキ長話おわり": "Otaki's Tale Done",
"トリカゼおかね": "Torikaze's Money",
"マハリお米": "Mahari's Rice",
"お社ばくは": "Shrine Blown Up",
"ヒノタマげきは": "Hinotama Defeated",
"すきだからな": "Because I Like You",
"便利だな": "Handy, Huh",
"落ちた": "Fell Down",
"引き締める": "Staying Sharp",
"ちい！": "Tch!",
"ミケーネきえる": "Mycenae Vanishes",
"青龍死す": "Seiryu Dies",
"村に帰る": "Return to the Village",
"トリカゼ救出": "Torikaze Rescued",
"トリカゼ休め": "Torikaze Rests",
"マハリ救出": "Mahari Rescued",
"マハリ休め": "Mahari Rests",
"行って参ります": "Off We Go",
"別行動": "Splitting Up",
"生きていてくれよ": "Stay Alive",
"ああ": "Yeah",
"ナガレたすけろ": "Save Nagare",
"あたしが！": "I Will!",
"連れていかれる": "Taken Away",
"フレイム終わり": "Flame Arc Done",
"アクマ倒した": "Fiend Defeated",
"パンもらった": "Got Bread",
"いったん休憩": "Taking a Break",
"ダフィール終わり": "Dafill Done",
"突入する！": "Charging In!",
"ダフィール消える": "Dafill Vanishes",
"光の柱へ": "To the Pillar of Light",
"ロイが呼んでる": "Roi Summons",
"ロイのところへ": "To Roi",
"王の間にはいる": "Enter the Throne Room",
"レイモンド去る": "Raymond Leaves",
"ないぜーーー": "No Need!",
"三人集結": "Three Gather",
"レイストックもらう": "Got Restock",
"蜻蛉斬もらう": "Got the Tonbogiri",
"ソロモドネガルもらう": "Got the Zomolod Negal",
"そういうのやめろ": "Cut That Out",
"マンゴーシュもらう": "Got the Main Gauche",
"奇書もらう": "Got the Rare Tome",
"奇書あげる": "Gave the Rare Tome",
"ヤバミ倒した": "Yabamination Defeated",
"暗くかがやく倒した": "Darkly Shining Defeated",
"ラストダンジョン": "Last Dungeon",
"不気味な洞窟": "Eerie Cave",
"廃墟": "Ruins",
"ピケピケ変身": "Pikepike Transforms",
"ピケピケに会う": "Meet Pikepike",
"出し切った": "Poured It All Out",
"ピＱＥ": "PiQE",
"ミケーネへ": "To Mycenae",
"いくぞ！": "Let's Go!",
"ブリザード": "Blizzard",
"しぬなよ": "Don't Die",
"ミケーネにかつ": "Beat Mycenae",
"いっきに": "All at Once",
"ナウー変身": "Nau Transforms",
"ナウ―倒す": "Defeat Nau",
"ナウー死す": "Nau Dies",
"くっそー": "Dammit",
"じゃあねー": "See Ya",
"大魔王倒した": "Great Demon King Defeated",
"大魔王ダウン": "Great Demon King Down",
"ウィンいくぞ": "Win, Let's Go",
"二周目開始！！": "Second Playthrough Started!!",
"ホムラ消える": "Homura Vanishes",
"ホムラおわり": "Homura Done",
"物干竿もらう": "Got the Clothes Pole",
"次元戻る": "Dimensions Return",
"裏ボス撃破": "Hidden Boss Defeated",
"伝説撃破": "Legendary Defeated",
"雑談の乱数": "Chat random value",
}

N = {
"セイリューの若き当主": "Young Head of Seiryu",
"セイリュー領主の一人娘": "Only Daughter of Seiryu's Lord",
"自他ともに認める天才騎士": "A Self-Proclaimed and Widely Acknowledged Genius Knight",
"フレイム王国の王子": "Prince of the Flame Kingdom",
"食べるの大好き": "Loves to Eat",
"天才と呼ばれる若き騎士": "A Young Knight Called a Genius",
"ウィンダム騎士団長代行": "Acting Commander of the Windam Knight Order",
"フレイム王国の国王": "King of the Flame Kingdom",
"若き騎士": "Young Knight",
"セイリューの前当主": "Former Head of Seiryu",
"セイリューの長老": "Elder of Seiryu",
"セイリュー鍛冶屋の娘": "Daughter of Seiryu's Blacksmith",
"セイリュー農家の息子": "Son of Seiryu's Farmer",
"炭鉱夫": "Coal Miner",
"セイリュー領主": "Lord of Seiryu",
"フレイム王子": "Prince of Flame",
"元騎士隊長": "Former Knight Captain",
"奇書": "Rare Tome",
}

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches"))


def norm(s):
    return re.sub(r"[ \u3000]+", " ", s).strip()


def fill(fname, table):
    path = os.path.join(BASE, fname)
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    keyed = {norm(k): v for k, v in table.items()}
    n = 0
    for r in rows:
        if (r.get("translation") or "").strip():
            continue
        t = keyed.get(norm(r["japanese"]))
        if t:
            r["translation"] = t
            n += 1
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(fname, "filled", n, "remaining",
          sum(1 for r in rows if not (r.get("translation") or "").strip()))


if __name__ == "__main__":
    fill("switch.tsv", S)
    fill("miscname.tsv", N)
