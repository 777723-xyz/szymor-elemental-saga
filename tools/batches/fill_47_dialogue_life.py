#!/usr/bin/env python3
"""Fill batch 47: Life revival, Mycenae defeat, aftermath."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"5ターンだ。": "Five turns.",
"5ターン以内に皆殺しにしてやる…。":
    "I'll slaughter you all within five turns...",
"…っく、くっそーーーーーー！！！":
    "...Ngh, damn it—!!",
"水の紋章よ！": "Water Crest!",
"ぼくの最後のエレメンタルパワーで、":
    "With my last Elemental Power,",
"この魔法を発動してくれ…": "let this spell be cast...",
"イノチ！！！！！！！！！！！！！":
    "LIFE!!!!!!!!!!!!!!!",
"うおおおおおおおおおおおおおお！！":
    "Woooooooooaaaaah!!",
"…う、うーん　": "...U-Unh...",
"な…ナガレ…！！": "N-...Nagare...!!",
"生き返りやがった…": "She came back...",
"青龍…　": "Seiryu...",
"てめえ………！！": "You......!!",
"ホノオ！ウィン！": "Hono! Win!",
"ミケーネを抑えるんだ！！":
    "Hold Mycenae down!!",
"その間に、あたしは青龍から紋章を継承する！":
    "Meanwhile, I'll inherit the crest from Seiryu!",
"お！？": "Oh!?",
"お、おう…　わかったぜ！！":
    "O-Okay... got it!!",
"うわあああああああああああ！！":
    "Waaaah!!",
"ちい…！！": "Tch...!!",
"龍が…！！": "The dragon...!!",
"いる…！！": "You're alive...!!",
"ええ、龍よ。": "Yes, dragon.",
"何千年もこの地の闇の力を司り…":
    "Ruling this land's dark power for millennia...",
"我々闇のエレメントの力の復活を":
    "you who awaited the revival of our",
"待ち続けていた…　最強の闇の結晶…":
    "Dark Element's power... the strongest Dark Crystal...",
"それが…": "And that is...",
"龍！！！": "the dragon!!!",
"ええ、だからそう言っているんだけれど…":
    "Yes, that's what I keep saying...",
"誰なのあなたたちは？": "But who are you lot?",
"私、いまからこの青龍さんと大事な用が":
    "I have important business with this Seiryu",
"あるんだけれど…": "right now...",
"…え？　誰こいつ…？": "...Huh? Who's this...?",
"あ、誰かいる…。": "Oh, someone's here...",
"ちょっと、まさかいま気付いたの…？":
    "Wait, you're only noticing now...?",
"私も龍ほどとは言えなくとも、結構派手な方の":
    "I'm not as flashy as the dragon, but I thought",
"つもりでいたんだけれど…": "I was rather conspicuous...",
"…いや、だからオマエ誰だ？":
    "...No, I said—who are you?",
"突然うえから落っこちといてきて…":
    "You come falling out of the sky all of a sudden...",
"こういう扱いされるのちょっと納得いかない…":
    "I can't quite accept being treated like this...",
"…そこは分かっておいてね？":
    "...Do keep that in mind?",
"私は闇の四天王、ミケーネ！":
    "I am Mycenae, of the Four Dark Generals!",
"いまからこの青龍さんの力を吸収して、":
    "Now I'll absorb this Seiryu's power",
"さっさと闇の力を開放しようというところよ！":
    "and get on with releasing the Dark power!",
"四天王だーーーーーーーーーーー！？":
    "A Four General—!?",
"そんなことはさせないぞ、ミケーネ！":
    "We won't let you, Mycenae!",
"こっちにもその龍に大事な用があるんでな！":
    "We've got important business with that dragon too!",
"そういうあなたたちは…": "As for you lot...",
"ふうん…　なるほどね。": "Hmm... I see.",
"紋章の継承者のようね。": "You're crest inheritors, it seems.",
"あなたたちから、火と風のエレメントパワーを":
    "I sense Fire and Wind Elemental Power",
"感じるわ。": "from you.",
"させるかーー！！": "As if we'd let you—!!",
"………負けたわ。": ".........I lose.",
"わかった…！！": "Fine...!!",
"さあ…　みんなでミケーネを…　たおすんだ…！":
    "Come... let's all... bring down Mycenae...!",
"よくもあたしを殺してくれたなあ…":
    "You really killed me, didn't you...",
"ミケーネ…！！": "Mycenae...!!",
"てめえ、もう覚悟、できてるよなあ…？":
    "You're ready for this, right...?",
"あたしは紋章の力をまだ使ったことがないんだ":
    "I've never used the crest's power yet.",
"でもそんなこと言ってる場合じゃねえ…":
    "But this is no time to hold back...",
"ウィン、オレたちも行くぞ！！": "Win, we're going too!!",
"何言ってるかわかんねえ…！！":
    "I don't know what you're saying...!!",
"う、ウィン、オレたちも行くぞ！！":
    "U-Win, we're going too!!",
"やらせるかああああああーーッ！！！！":
    "We won't let you—!!",
"くおおおおおらああああ！！！！": "Rrraaaah!!",
"………信じられない…": ".........Unbelievable...",
"この短期間でここまでの力を持っているとは…":
    "To have gained this much power in such a short time...",
"おっけーりょーーかーーーい": "Okkee—ay—!",
"この感覚…なんて清々しい気分なんだ…":
    "This feeling... how refreshing it is...",
"内から静かにこんこんと湧き出る鋭気…":
    "Vitality welling up quietly from within...",
"さあ…　": "Now...",
"みんなでミケーネを…　ぶっ飛ばせーーー！！":
    "let's all... blast Mycenae away—!!",
"よくもあたしを殺してくれたよなあ…":
    "You really went and killed me, huh...",
"おい、ミケーネ…！！": "Hey, Mycenae...!!",
"てめえ…もう覚悟、できてるよなあ…？":
    "You... you're ready for this, right...?",
"あたしは紋章の力をまだ使ったことがない…":
    "I've never used the crest's power...",
"うるせえんだよピーピーガーガーと…":
    "Shut up with all your squeaking and squawking...",
"耳障りなんだよ、てめえのその甲高い声が…":
    "that shrill voice of yours is grating...",
"御託は良いから、さっさとかかってこい！！":
    "Spare me the speeches—just come at me!!",
"ちくしょテメコラァぁあああああん！！！？？":
    "Damn you—!!??",
"上等だ秒で始末したらぞおおオアァァン！？？":
    "Fine, I'll finish you in seconds—!!??",
"ほら…な？": "See...?",
"みすみす逃がしてしまうとは…":
    "To let her slip away like that...",
"うかつだった…！！": "how careless...!!",
"宿はなんとか営業中だぜ。":
    "The inn's somehow still open for business.",
"営業中っていうか、避難所みたいなもんだけど":
    "Well, 'open' more like a shelter, but still.",
"ここはあたしがちゃーーんと見張ってるから、":
    "I'm keeping a sharp eye on this place, so",
"あんたらは使命かとかを頑張んな！":
    "you lot go do your whole mission thing!",
"雨、やみそうにないですね…":
    "The rain doesn't look like it'll stop...",
"あ、いえ、すいません…": "Ah, no, sorry...",
"別に変な意味で言ったんじゃ…":
    "I didn't mean it in a weird way...",
"…ご武運をお祈りしています！":
    "...I wish you luck in battle!",
"そんなことより、トリカゼ！": "Anyway, Torikaze!",
"傷は深いのか！？": "How bad's the wound!?",
"え…？　ああ、ちょっとねんざしただけさ！":
    "Huh...? Ah, just a little sprain!",
"それより…　あんたの家の方を頼む…":
    "More importantly... take care of your own home...",
"マハリが守っているはずだが…　":
    "Mahari should be guarding it...",
"助かったぜ…　": "Thanks...",
"わかった！": "Got it!",
"トリカゼはここで休んでいろ！いいな！":
    "Torikaze, rest here! Understood!",
"トリカゼ！大丈夫か！？": "Torikaze! Are you okay!?",
"ちゃんと紋章…ぶんどってきたんだな…":
    "You really did take the crest back, didn't you...",
"ナガレちゃん…": "Nagare...",
"あんたの家の方を頼む…": "Take care of your own home...",
"マハリが守っているはずだ…　":
    "Mahari should be guarding it...",
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
