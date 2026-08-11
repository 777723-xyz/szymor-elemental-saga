#!/usr/bin/env python3
"""Fill batch 54: misc aftermath, spear advice, Pikepike's final gag."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"そうでしょう？": "Right?",
"確かに魔物がお金持ってるわけないですけど、":
    "True, monsters don't carry money, but",
"そんなところまでリアルにしなくてもなあ…":
    "they didn't have to make it that realistic...",
"そうですかー？": "Is that so?",
"まあ、店でまとめて売って、一気にお金持ちに":
    "Well, selling it all at a shop and getting rich",
"なるの、ちょっと楽しいですよね…":
    "all at once is kind of fun...",
"いちいち売るの面倒ですよねえ？":
    "Selling them one by one is a hassle, right?",
"…ロイ騎士団長がお呼びだ。": "...Commander Roi summons you.",
"先日の光の柱の件で、話があるらしい…。":
    "It seems there's word about the Pillar of Light...",
"…ウィン、外は危ないぞ。": "...Win, it's dangerous out there.",
"長居するのはよくないと、忠告させてもらう。":
    "I'd advise you not to linger long.",
"南の暗黒大陸に": "Over the southern Dark Continent,",
"巨大な光の柱が立つのを": "a colossal pillar of light",
"見るまでは…": "before they saw it rise...",
"いまはこんなところに用はないんじゃねーか？":
    "No business for you in a place like this now, is there?",
"な、なんだ！？　紋章がずっと光ってるぞ！？":
    "Wh-What!? The crest keeps glowing!?",
"ウィンたちのステータスが幾つかアップした！":
    "Some of the party's stats increased!",
"全員のステータスが幾つかアップした！":
    "Some of everyone's stats increased!",
"ありゃあ…　龍みてーな形してんなー？":
    "Well now... that's shaped like a dragon, huh?",
"ありゃあ…　イヌ…？みてーな形してんなー？":
    "Well now... that's shaped like a dog...?",
"かなり崩壊している…": "It's quite collapsed...",
"これ以上近付くのは危険だ。":
    "Getting any closer is dangerous.",
"ここも近々閉鎖されると思うよ…":
    "I think this place will be closed soon too...",
"火の岩もそうだけれど…":
    "Same with the fire rocks...",
"魔物の侵入を防げなくなってきたんだ。":
    "we can no longer keep monsters out.",
"閉店しました": "Closed",
"…と、書いてある": "...it says.",
"扉が打ちつけられていて開かない":
    "The door is nailed shut and won't open.",
"んー？あら、ウィンじゃないか！":
    "Hm? Oh, if it isn't Win!",
"元気だったかい？": "Been well?",
"あたしらは街に嵐がきたときに避難してきた":
    "We took shelter when the storm hit the town,",
"んだけれど…　この通りどこへも行けずじまい":
    "but... as you can see, we're stuck",
"になっちまったよ。バカだねえ": "with nowhere to go. Silly us.",
"おお、ウィン…！": "Oh, Win...!",
"勇者様なんだってなあ": "So you're a hero now, they say.",
"…立派になって！": "...You've become quite the man!",
"もう、以前のウィンとは見違えるのう…":
    "You're a far cry from the Win of old...",
"お前に会えて、希望が持てたぞ…":
    "Seeing you gives me hope...",
"この辺りはほとんど洪水の影響ないよ。":
    "This area's barely affected by the flood.",
"だけど、しばらく石堀りはお休みだな。":
    "But quarrying's on hold for a while.",
"魔物が増えてるから。": "Because of the monsters.",
"ああ、完成した橋なら、南に行けばすぐ分かる。":
    "Ah, the finished bridge—head south and you'll spot it right away.",
"編みかけのマフラーだ": "It's a half-knitted scarf.",
"ちなみに、転倒させられるスキルも、":
    "By the way, skills that can knock down enemies",
"使えるのは槍だけだ。": "can only be used with a spear.",
"転倒させれば味方全体の通常攻撃の威力が":
    "Knocking them down boosts the whole party's",
"増すから、EP節約にもなるぜ！":
    "normal attack power—saves EP too!",
"まあ確かに、スキルとかも他の武器の方が":
    "True, other weapons do have easier-to-use",
"使いやすかったりするよな。": "skills and such.",
"ウィン！　どうだい、槍は使ってる？":
    "Win! How's it going—using the spear?",
"だけどお前、紋章ですばやく動けるだろ？":
    "But you can move quickly with your crest, right?",
"だから槍の重さも気にならないはずだ。":
    "So the spear's weight shouldn't bother you.",
"重さが気にならないとなれば、槍は単純に、":
    "With no weight issue, the spear is simply",
"素の威力が高いダガー、レイピアと同じだ。":
    "a dagger or rapier with higher base power.",
"会心率を考えれば、実は最強の威力の武器":
    "Factoring in crit rate, it's actually one of",
"にもなるんだぜ？": "the strongest weapons around, you know?",
"いまはどっち派だい？": "Which side are you on now?",
"やっぱりな！": "Just as I thought!",
"特に紋章の力で素早く動けるお前なら、":
    "Especially with your crest-powered speed,",
"槍の取り回しの悪さもほとんど影響しないしな":
    "the spear's unwieldiness barely matters.",
"ウィン、いまのところ街は大丈夫だ。":
    "Win, the town's fine for now.",
"各家の見回りも計画通り出来ている。":
    "House-to-house patrols are on schedule.",
"略奪等の悪さも、一件もない。":
    "Not a single case of looting or mischief.",
"それより、お前んちの親御さん、城で":
    "Anyway, your parents work at the castle, don't they.",
"働いてるってな。みんなうまいパンが":
    "Everyone's delighted they can eat",
"食べられるってよろこんでるよ。":
    "their good bread.",
"すごく強そうなお酒が入っている":
    "It's full of terrifyingly strong liquor.",
"固いパンがたくさん入っている":
    "It's full of hard bread.",
"ウィンは蜻蛉斬を受け取った！": "Win received a Tonbogiri!",
"ウィンは本物の蜻蛉斬を受け取った！":
    "Win received a genuine Tonbogiri!",
"セイリューから支給されたライスボールで":
    "With the Rice Balls supplied by Seiryu,",
"我が兵たちの士気も上々！": "our soldiers' morale is high!",
"ここはわしらに安心してまかせい！":
    "Leave this to us without worry!",
"昨日なんかめちゃくちゃ火吐くイヌ来ました！":
    "Yesterday, a dog that spits fire like crazy showed up!",
"やばいっすよアレ！！": "That thing's no joke!!",
"ちょっと剣が足りないすねー":
    "We're a bit short on swords, you know~",
"魔物が固くってすぐ刃こぼれしちゃうんすよ":
    "The monsters are so tough, our blades chip right away.",
"は、はははは、はひいひいいいいいいいい！！！":
    "H-Hahaha, haaahiii!!!",
"あ…騎士さまお疲れ様です！！":
    "Ah... Sir Knight, good work out there!!",
"ぼく新人のトールです……！！":
    "I'm Thor, the new recruit......!!",
"ふわあああおおおおおおおおおおお！！":
    "Fwaaaaooooooh!!",
"よろしくおなながいいしままーーーす！！！":
    "Pleased to meet you, now I'll bow bow—!!!",
"刃こぼれした剣が乱雑にしまってある":
    "Chipped swords are stored here, carelessly.",
"中にはコメが入っている": "There's rice inside.",
"ツヴァイハンダーを手に入れた！":
    "Obtained a Zweihander!",
"グラディウスを手に入れた！": "Obtained a Gladius!",
"から生まれ出た闇の結晶に過ぎない…":
    "is merely a Dark Crystal born from...",
"から生れ出た闇の結晶に過ぎない…":
    "is merely a Dark Crystal born from...",
"ではではではー………": "Well then, then, then...",
"さらば！！": "Farewell!!",
"…なんだ？": "...What?",
"最後に………　一回でいい……":
    "At the end...... just once...",
"私の名前をちゃんと呼んでくれえええ………！":
    "call my name properly......!",
"…え、いや…　": "...Uh, well...",
"でもうまく呼べる気が一切しないんだよな…":
    "but I don't think I can say it right at all...",
"ごめん": "Sorry.",
"ゆっくり言うから……！！": "I'll say it slowly......!!",
"最後のちからを振り絞って…一回だけ言うから":
    "With my last strength... I'll say it just once,",
"よく…　聞いてね……　いい…か…？":
    "so listen... closely...... alright......?",
"…めちゃくちゃ強かったぜ…　ピ…ピｋ…！！":
    "...You were incredibly strong... Pi... Pik...!!",
"…え、お、おう…！": "...Eh, o-oh...!",
"わ…　私の名前は………………":
    "M-My name is..............",
"ピ………ＱＥ…　ピ……Ｑ………":
    "Pi...... QE... Pi...... Q.........",
"ウッ！！！！！！！！！！！！！！！！":
    "UGH!!!!!!!!!!!!!",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "dialogue.tsv"))


def norm(s):
    return re.sub(r"[ \u3000]+", " ", s).strip()


def main():
    keyed = {norm(k): v for k, v in D.items()}
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
    print("dialogue.tsv filled", filled, "remaining",
          sum(1 for r in rows if not (r.get("translation") or "").strip()))


if __name__ == "__main__":
    main()
