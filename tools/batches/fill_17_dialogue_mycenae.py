#!/usr/bin/env python3
"""Fill batch 17: Mycenae escape, crest inheritance, Windam siege aftermath."""
import csv
import os
import re

D = {
"嫌な予感がする…": "I have a bad feeling...",
"出るって、ガキの頃によく言われたけど…":
    "Since I was a kid, they always said they appeared, but...",
"これから何が起こるのか…": "What's about to happen...",
"わかっていない感じに見えるんだけれど？":
    "You don't seem to have any idea, do you?",
"何が起こる…？": "What's going to happen...?",
"あなたたちが、これだけ早く継承者を揃えた":
    "Because you gathered the inheritors this quickly,",
"ものだから…": "...",
"もう少し知っているのかと思ったけれど、":
    "I thought you might know a bit more, but",
"何も知らないのね。": "you know nothing, do you.",
"な、なんだよ…": "Wh-What...?",
"何が起こるってんだよーーー！？": "What's gonna happen!?",
"おっと！": "Whoa!",
"まだ全然なんとかなるわね。": "It's still completely manageable.",
"はあ、おかげですっかり頭が冷えたわ。":
    "Well, thanks to that, I've completely cooled down.",
"そうなったら、ここで時間を潰してられない。":
    "In that case, I can't waste time here.",
"背中を見せたら、後ろから叩っきるぜ！！":
    "Show me your back, and I'll cut you down from behind!!",
"あっ！！　消えるぞコイツ！！": "Ah!! She's disappearing!!",
"消える…？": "Disappearing...?",
"コイツら、四天王は、倒しても消えて":
    "These Four Generals—even when you defeat them, they vanish",
"どっかにいっちまうんだよ！！":
    "and get away somewhere!!",
"前のときもそうだったぜ！！": "It was the same last time!!",
"なんだと…　なら、早くトドメを…！！":
    "What... Then hurry and finish her off...!!",
"そういうこと…": "That's right...",
"じゃあね、あなたたち。": "Well then, farewell.",
"また会えることを願ってるわ…　本当よ。":
    "I hope we meet again... truly.",
"えーい！！邪魔をするなああああああああ！！":
    "Bah!! Stop interfering—!!",
"さあ、青龍！": "Come, Seiryu!",
"急いでわたしに、紋章を…！！":
    "Hurry and give me the crest...!!",
"ナガレは、イヤシとイノチとテッペキの魔法をおぼえた！":
    "Nagare learned the Heal, Life, and Iron Wall spells!",
"この力が…　本当の紋章の力か…！！":
    "This power... so this is the crest's true power...!!",
"ええい…みすみす継承させてしまうとは…":
    "Dammit... letting her inherit it right under our noses...",
"あたいとしたことが、とんだ大失態だ…！！":
    "What a colossal blunder on my part...!!",
"だからもちろん、手加減はできないし…":
    "So of course, I can't hold back...",
"そして当然、手加減する気もない。":
    "And naturally, I've no intention of holding back.",
"つまり、あたしもあんたを…":
    "In other words, I might just",
"ころしちまうかも知れねえぞ、ってことだ…":
    "end up killing you too...",
"…わかってるよなあーーーーーー！！？":
    "...You get that, right—!?",
"あんだあ？この小娘がああああああああ！":
    "What was that, you little wench—!",
"ちょっと生き返ったからって、":
    "Just because she came back to life,",
"えらくちょうしくれやがってよお……！！":
    "she's putting on airs......!!",
"上等じゃねえかコラーーーーーー！！！！":
    "Fine by me, bring it—!!!!",
"しにてえやつはまとめてかかってこいや…":
    "Anyone who wants to die, come at me all at once...",
"コラああああああああああ！！！！！！！！":
    "Heeeeeey!!!!!",
"こ、こええ………！！": "S-Scary......!!",
"よし…　じゃあ行くか！": "Alright... let's go!",
"ウィン…　あんたには礼を言いたいが…":
    "Win... I want to thank you, but...",
"いまは言わないぞ。": "not now.",
"オレもだ、ウィン！": "Me too, Win!",
"…ここからは、ウィンと、オレたちで別行動だ":
    "...From here, Win splits off from us",
"だって、またすぐに集まって、":
    "Because we'll gather again soon",
"闇のエレメントを倒さないとだからな！":
    "to defeat the Dark Element!",
"よし、行こう！": "Alright, let's go!",
"おう！！": "Yeah!!",
"出発するなら、先にここで買い物を済ませて":
    "Before we set out, let's finish our shopping here",
"おこう。向こうに着いたらそれどころじゃない":
    "first. Once we get there, we might not",
"可能性もあるからな。": "have the chance.",
"うん…": "Yeah...",
"とりあえず、屋敷の中へ…": "For now, let's head inside the estate...",
"村のみんなが集まってるよ": "Everyone in the village is gathering.",
"いまいくぜー！！": "I'm coming!!",
"…マハリ！！": "...Mahari!!",
"ナガレ！みなさん！": "Nagare! Everyone!",
"僕だけでは勝てそうにありません！！":
    "I can't win on my own!!",
"助けてください！！": "Please help!!",
"行くぞ、ウィン！": "Let's go, Win!",
"いまは何も考えず、上を目指そう…":
    "For now, don't think—just head upward...",
"お前の知ってる敵が来ているんだろ…？":
    "An enemy you know is coming, right...?",
"ああ…！": "Yeah...!",
"…城自体はかなり持ちこたえたみたいだね。":
    "...The castle itself seems to have held up pretty well.",
"燃える岩がたくさん降ってきたってのに…":
    "Even with all those burning rocks raining down...",
"街の方もこれぐらい頑丈に作っておけば…":
    "If the town had been built this sturdy...",
"あんなひでえことにならなかったのによー…":
    "it wouldn't have ended up so ruined...",
"…お、王子　": "...O-Oh, Prince",
"あいつ…　めちゃくちゃ強いです…":
    "That guy... he's insanely strong...",
"ああ…知ってるさ…": "Yeah... I know...",
"もしかして…　武器とか買いに来ました…？":
    "You wouldn't happen to be... here to buy weapons...?",
"…っ！　ミケーネ………！！": "...! Mycenae......!!",
"ナウ―…　ピケピケがカンカンだよ？":
    "Nau... Pikepike is furious, you know?",
"計画は伝えてあるはずだ。":
    "You should have been told the plan.",
"なぜこんなことをして時間を潰している？":
    "Why are you wasting time on this?",
"し…　しまった…！": "Ugh... caught...!",
"おまえがさっさとトドメを刺さないからだ！":
    "It's because you didn't finish her off quickly!",
"ホノオ！！": "Hono!!",
"ぐ…　すまん…！": "Guh... sorry...!",
"また会ったわね、あなたたち…": "We meet again, you lot...",
"お遊びが過ぎるよ、ナウ―！": "You've been playing too much, Nau!",
"ホノオはゾモロドネガルを受け取った！":
    "Hono received a Zomolod Negal!",
"あたしは水の紋章の力を持つものとして、":
    "As one who holds the Water Crest's power,",
"当然のことをしただけです。": "I only did what was right.",
"しかしフレイム王は…": "But King Flame...",
"まだお身体の具合が優れぬ様子で…":
    "still seems to be in poor health...",
"心配です。": "I'm worried.",
"ナガレ殿、　四天王の襲撃の際は、":
    "Lord Nagare, when the Four Generals attacked,",
"わしのは寿命でしょうな。": "I thought my time had come.",
"ナガレ殿のおかげで傷はすっかり完治しておる":
    "Thanks to you, Lord Nagare, my wounds are fully healed.",
"ひとり残すホノオが心配です…":
    "I worry about Hono, left alone...",
"世継ぎどころか、あやつにはいまだ妻もなく…":
    "He has no heir, not even a wife yet...",
"ナガレ殿のようなお強い方が、あやつの近くに":
    "If a strong one like you, Lord Nagare, were by his side,",
"おってくれたなら、何の心配もないのだが…":
    "I'd have nothing to worry about...",
"あはは、そうですね。": "Ahaha, right.",
"親父ー？　そういうのやめろな？": "Hey, Dad? Cut that out, will you?",
"ナガレ殿のおかげで、城の者たちの殆どが":
    "Thanks to you, Lord Nagare, most of the castle folk",
"いまは元気になりました。": "have recovered now.",
"このご恩、わしだけでなく皆忘れないでしょう":
    "This debt—not just I, but everyone, will remember it.",
"ああ…　はい、わかりました。": "Ah... yes, understood.",
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
