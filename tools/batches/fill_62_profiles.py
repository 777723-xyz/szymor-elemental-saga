#!/usr/bin/env python3
"""Fill batch 62: actor profiles.

Escaping-proof: no literal backslashes in this file.
- keys: continuous prose (line-break sequences are stripped during matching)
- values: "@@@" is replaced with the \\n control code at runtime
"""
import csv
import os
import re

BS = chr(92)  # backslash
NL = BS + "n"  # the \\n control code
STRIP_NL = re.compile(BS + BS + "+n")  # one or more backslashes followed by n


def norm(s):
    s = STRIP_NL.sub("", s)
    return re.sub(r"[ \u3000]+", " ", s).strip()


P = {
"西の山奥の国セイリュー領主の娘。幼い頃より領民の悪童と悪さばかりして育った。粗暴な面もあるが人望が厚く人気者。":
    "Daughter of the lord of Seiryu, a land deep in the western mountains.@@@"
    "Raised raising mischief with the villagers' brats since childhood.@@@"
    "Brash at times, yet well-liked and popular.",
"類稀な頭脳と剣術で天才の名を欲しいままにしている騎士。伝説的な騎士であるロイを超える才能とも言われている。":
    "A knight whose rare intellect and swordsmanship have won him the name@@@"
    "of genius. Some say his talent even surpasses the legendary knight Roi.",
"フレイム王国の第二王子だったが兄の急逝により次期国王となった。兄と真逆で性格は豪放磊落、学問より剣術が好き。":
    "Once the second prince of the Flame Kingdom, he became the next king@@@"
    "upon his brother's sudden death. The polar opposite of his brother:@@@"
    "bold and free-spirited, preferring swordsmanship to study.",
"その類まれな身体性能と槍の扱いで将来を期待されていたが、食べ過ぎてどんどん太るので心配されている若き兵士。":
    "A young soldier whose extraordinary physique and spearplay promised@@@"
    "a bright future--though his ever-growing appetite worries everyone.",
"幼い頃に父より風の紋章を継承した若き騎士。それを抜きにしても天才的な頭脳と剣術を持つ。":
    "A young knight who inherited the Wind Crest from his father in@@@"
    "childhood. Even setting that aside, his intellect and swordsmanship@@@"
    "are genius-level.",
"ウィンダム王国騎士団に代々騎士団長を輩出している名門。その怪力と胆力で戦場を駆け巡った歴戦の勇士。":
    "Of a distinguished house that has produced generation after@@@"
    "generation of Windam Knight Commanders. A battle-hardened warrior who@@@"
    "has roamed the battlefield on monstrous strength and nerve.",
"フレイム王国の王。伝説の王であるバーン王に匹敵すると言われるほどの剣の使い手だった。":
    "King of the Flame Kingdom. A swordsman said to rival@@@"
    "the legendary King Burn.",
"庶民の出だが父母が無理をして入学させてくれた士官学校を首席で卒業。将来を期待されている新米騎士。":
    "Of common birth; his parents strained themselves to put him through@@@"
    "the officer academy, which he graduated at the top of his class.@@@"
    "A rookie knight with a promising future.",
"フレイム王国の第一王子。弟のホノオのような剣術や体術の才能には恵まれなかったが、類まれな頭脳と洞察力を持つ。":
    "First prince of the Flame Kingdom. Lacking his younger brother@@@"
    "Hono's gifts in sword and body, he instead possesses rare@@@"
    "intellect and insight.",
"西の山奥の国セイリュー領主の娘。幼い頃より身体が弱く、剣術よりも本を読んだり植物を愛でて育った。":
    "Daughter of the lord of Seiryu. Frail since childhood, she grew up@@@"
    "loving books and plants rather than the sword.",
"セイリューの元当主人。一体どれほど長生きをしているのか誰も分からない。膨大な知識と尋常でない剣の腕を持つ。":
    "A former head of Seiryu. No one knows just how long she has lived.@@@"
    "She commands vast knowledge and extraordinary skill with the sword.",
"ウィンダムの王。幼い頃より武術全般に優れ、騎士団の騎士たちにも厳しい鍛錬を求める。年齢不詳。":
    "King of Windam. Master of all martial arts since childhood, he@@@"
    "demands rigorous training of his knights. Age unknown.",
"セイリューの鍛冶屋の一族の娘。家業に殆ど関わらず、悪さと剣術にだけ励んで育った。気性は激しいが心根は優しい。":
    "Daughter of Seiryu's blacksmith clan. Barely involved in the family@@@"
    "trade, she grew up devoted to mischief and swordsmanship.@@@"
    "Fierce-tempered, yet kind at heart.",
"セイリュー農家の一族の男子。幼い頃より何をやらせても器用だった。なぜか村の者の中では悪童とばかり仲が良い。":
    "A boy of Seiryu's farming clan. Handy at everything since childhood.@@@"
    "For some reason, he's closest friends with the village's worst brats.",
"かつて天才騎士として王国に名を轟かせた男。いまは森の中の生家に籠り隠遁生活を送っている。":
    "A man once famed across the kingdom as a genius knight. Now he@@@"
    "lives in seclusion in his family home deep in the forest.",
"火と水の紋章を両手に宿した天才騎士。かつての部下ウィンと二人で最終局面に挑む。":
    "A genius knight bearing the Fire and Water crests in his two hands.@@@"
    "He faces the final battle alongside his former subordinate, Win.",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "profile.tsv"))


def main():
    keyed = {norm(k): v.replace("@@@", NL) for k, v in P.items()}
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
    print("profile.tsv filled", filled, "remaining",
          sum(1 for r in rows if not (r.get("translation") or "").strip()))


if __name__ == "__main__":
    main()
