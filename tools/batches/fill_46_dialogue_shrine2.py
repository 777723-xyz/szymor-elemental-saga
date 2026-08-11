#!/usr/bin/env python3
"""Fill batch 46: dragon's tale, Mycenae showdown at the shrine."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"でも　それは　約束だから…": "But... it's a promise...",
"約束…？": "A promise...?",
"そう　ぼくの　初めての友達との　約束…":
    "Yes... a promise with my first friend...",
"ぼくは　ずっと　ひとりでここにいた…":
    "I've been here all alone...",
"ずっと昔に　目が覚めてから　ずっとここで…":
    "ever since I awoke, long, long ago...",
"ある日　大昔だけどね…　ミケーネがやってきて…":
    "One day—ancient history now—Mycenae came...",
"ぼくから　力を奪っていった…": "and took my power...",
"そしてぼくは　だんだんと死んでいったんだ…":
    "And little by little, I began to die...",
"苦しかった…　怖かった…": "It was painful... and frightening...",
"そして　さみしかった…": "And lonely...",
"ぼくは　いったい　なんで　生きていたんだろうって…":
    "I wondered why I was even alive...",
"ここで目覚めて…　そして　とつぜん　力を奪われて…":
    "Awakening here... then suddenly having my power stolen...",
"そして　死んでいくなんて…": "only to wither away...",
"おい、それより…　龍はどうなったんだ…？":
    "Hey, more importantly... what happened to the dragon...?",
"それが…　闇の結晶ってことなのか…？":
    "So that... is what a Dark Crystal is...?",
"わかんない　わかんないよ": "I don't know... I don't know.",
"ミケーネがそう呼ぶけど　ぼくは…　ぼくだ":
    "Mycenae calls me that, but I... am me.",
"だんだん　くるしくなくなって　眠たくなって…":
    "The pain slowly faded, and I grew drowsy...",
"このままぼくは　しんでしまうんだなと思った…":
    "and I thought: so this is how I'll die...",
"そうしたら…": "But then...",
"そうしたら…　あの友達が降って来たんだ！":
    "But then... that friend came falling down!",
"…はじまりの水の者だな。": "...The First Being of Water.",
"そう…　ぼくの友だち…": "Yes... my friend...",
"友だちは　ぼくの目を覚ましてくれた":
    "My friend woke me up.",
"すごく　痛くて　目が覚めたんだ":
    "I woke from the terrible pain.",
"…急にひとが落ちてきて、":
    "...Because someone suddenly fell on you,",
"アンタの目に、刀が刺さったからか？":
    "and a sword pierced your eye?",
"そう！　すごい！": "Yes! Amazing!",
"ちゃんと伝わっているんだね！":
    "It's been passed down properly!",
"友だちが　伝えてくれていたんだね！":
    "My friend made sure it was!",
"でも待ってくれ、龍…": "But wait, dragon...",
"ちょっと聞いていた話と違うんだ。":
    "That's not quite the story we heard.",
"龍は怒って、それを許す代わりに、":
    "We heard you were angry, and in exchange for forgiveness,",
"水の者から紋章を奪ったって…": "you took the crest from the Being of Water...",
"だけど、おかしいわね。": "But something's odd.",
"水のエレメントパワーを感じないわ。":
    "I don't sense any Water Elemental Power.",
"人数は足りているのに、どういうことかしら？":
    "There are enough of you, so what's going on?",
"…っ！！": "...!!",
"そんなの関係ねー！！": "That doesn't matter!!",
"オマエなんぞ、二つで足りるってんだよー！！":
    "Two crests are plenty to deal with you!!",
"さあて、それはどうかしら？": "Now, is that so?",
"私の最も得意とする魔法も、氷…水の力。":
    "My most favored magic is ice—the power of water.",
"継承者のお二人さんはともかく…":
    "The two inheritors might be fine, but...",
"とてもじゃないけれど、そこのお嬢さんには":
    "that young lady there simply couldn't",
"耐えられないと思うわ。死ぬわよ。":
    "withstand it. She'd die.",
"………あたしのことは気にしないでくれ！":
    ".........Don't worry about me!",
"龍と話すには、ミケーネを倒すしかない！！":
    "To talk with the dragon, we must defeat Mycenae!!",
"くそーーーー！！": "Damn—!!",
"ナガレ、ぜってーに無理すんなよ！！":
    "Nagare, absolutely don't overdo it!!",
"そう、やるって言うのね。": "So, you mean to fight.",
"でも絶対に無理だと思うわ…だって…":
    "But I'm sure it's impossible... because...",
"こっちは更に…": "I've got even more...",
"この青龍さんも味方なのだから！":
    "this Seiryu on my side!",
"………なん、だと…！？": ".........Wh-What...!?",
"言ったでしょう…青龍さんは闇の結晶なの。":
    "I told you... Seiryu is a Dark Crystal.",
"当然、私の味方だわ。": "Naturally, he's on my side.",
"じゃあ、遊んであげる…": "Then, let me play with you...",
"逃げられるなんて思わないでね。":
    "Don't think you'll escape.",
"ケンカを先に吹っ掛けてきたのは…":
    "After all, it was you who started",
"そっちなんだから…！": "the fight...!",
"ちょっと、青龍さん！": "Hey, Seiryu!",
"どういうことなの！？": "What's the meaning of this!?",
"めちゃくちゃ痛かったんだけど！？":
    "That hurt like crazy, you know!?",
"あなた、戦う気はあるの！？":
    "Do you even intend to fight!?",
"四天王のミケーネが命令しているのよ！":
    "I, Mycenae of the Four Generals, am commanding you!",
"さあ、青龍さん。": "Now, Seiryu.",
"お、お前の味方になって…た、戦う気なんてない！":
    "I-I have no intention of fighting... on your side!",
"最強の闇の結晶よ…。": "The strongest Dark Crystal...",
"………な、に？": ".........Wh-What?",
"ミケーネの味方をして…": "To side with Mycenae...",
"あの子たちと戦うつもりなんて…ないんだよ！":
    "I have no intention of fighting those children!",
"…どういうこと？": "...What do you mean?",
"いまこそ私の力となり、闇の復活を…":
    "Now is the time to become my power, and the Dark's revival—",
"青龍…　それは…　水の紋章…！？":
    "Seiryu... that is... the Water Crest...!?",
"どうりで、何かおまえから不思議な力を":
    "No wonder I sensed a strange power from you—",
"感じたのだ…　闇の力ではないものを…":
    "something that wasn't dark power...",
"…龍よ！その紋章をあたしに継承してくれ！！":
    "...Dragon! Pass that crest to me!!",
"きみは…？": "You are...?",
"あたしはセイリューの当主だ！":
    "I am the head of Seiryu!",
"その紋章の本来の持ち主…": "the true owner of that crest...",
"はじまりの水の者の末裔だ！！":
    "a descendant of the First Being of Water!!",
"きみが…！？": "You...!?",
"すごい…　本当に来てくれたんだね！":
    "Amazing... you really came!",
"ぼくの友達の…そのこどもたちが！！":
    "The children of my friend!!",
"は…じ…ま…り…の…": "The... first...",
"み…ず…の…も…の…　だと…？":
    "being... of... water...?",
"おい、コラ…": "Hey, hold on...",
"てめえ…　本当にあれの子孫なのか…？":
    "you... are you really that one's descendant...?",
"…そうだ！セイリュー当主ナガレ…":
    "...Yes! I'm Nagare, head of Seiryu...",
"正真正銘、はじまりの水の者のまつ…":
    "the legitimate descendant of the First Being of Water...",
"…な、なにした…？": "...Wh-What did you do...?",
"あたいの最強魔法、ミケーネブリザードの":
    "My strongest spell—a concentrated form of",
"一点集中凝縮版…　ミケーネビームさ。":
    "Mycenae Blizzard... the Mycenae Beam.",
"水の紋章継承者ならまだしも、":
    "An inheritor of the Water Crest might survive,",
"ふつうの人間なら、即死だ。":
    "but an ordinary human would die instantly.",
"…て、てめえ………！！！！":
    "...Y-You......!!!!",
"…って、何これ？": "...Wait, what is this?",
"アレをあたいに思い出させたのが悪いんだよ。":
    "It's your fault for making me remember that thing.",
"しかもその子孫ってんだからな…":
    "And a descendant of it, at that...",
"殺しちまうよ、そりゃあ。": "Of course I'd kill her.",
"…おい、ナガレ…マジでか…":
    "...Hey, Nagare... is this for real...",
"おまえ、マジで死んでんのかよ…おい！！":
    "Are you really dying... hey!!",
"もういいよ、青龍も、てめえらも…":
    "Enough. Seiryu, all of you...",
"まとめて殺してやる。終わりにしてやるよ。":
    "I'll kill you all and put an end to this.",
"ただし、本気になったあたいに…":
    "But against me, in full earnest...",
"勝てると思うなあ…": "don't think you can win...",
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
