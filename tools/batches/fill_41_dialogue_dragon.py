#!/usr/bin/env python3
"""Fill batch 41: the dragon legend, shrine's origin."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"はじまりの水の者は": "The First Being of Water",
"洞窟の奥で穴に落ちたのじゃな":
    "fell into a pit deep within the cave.",
"私が先代当主のシズクです。": "I am Shizuku, the previous head.",
"深い穴じゃった": "It was a deep pit.",
"はじまりの水の者は落ちながら":
    "As it fell, the First Being of Water",
"さすがに死んでしまうだろうと思った":
    "was certain it would die.",
"しかし気付くと生きていた":
    "Yet when it came to, it was alive.",
"そちらの現当主、ナガレの姉でございます。":
    "I am the elder sister of Nagare, the current head.",
"濡れた岩肌の上で目を覚ましたのじゃ":
    "It awoke upon wet, bare rock.",
"そして目を見開いた": "And then it opened its eyes wide.",
"目の前に大きな龍がいたのじゃ":
    "Before it loomed a great dragon.",
"それだけではない": "And that was not all.",
"龍の左目に　はじまりの水の者が":
    "Deep in the dragon's left eye—",
"腰に履いていた刀が深々と":
    "the sword at the First Being of Water's waist",
"突き刺さっていたのじゃ": "had been driven, deep.",
"はじまりの水の者が助かったのは":
    "The First Being of Water survived",
"龍の目に刀が突き刺さったからだったのじゃ":
    "because its sword had pierced the dragon's eye.",
"うおおおおおおおおおおお！！": "Woooooaaah!!",
"どうも…オレはホノオ。": "Howdy... I'm Hono.",
"やっぱり龍が出てくる話だったな！":
    "Just as I thought—it's a dragon story!",
"あんたらもう少し静かに聞けないのかい…":
    "Can't you two listen a little more quietly...",
"これはあてっこクイズとかじゃないんじゃぞ…":
    "This isn't a guessing game, you know...",
"龍は泣いた　啼いた": "The dragon wept—it cried out.",
"で、こっちがウィンです。": "And this here's Win.",
"何千年と生きてきて　": "Having lived thousands of years,",
"エレメントを守り続けてきて": "ever guarding the Elements,",
"その結果がこれか": "and this is what comes of it.",
"龍は弱っていた": "The dragon was weakening.",
"はじまりの水の者の刀が": "The First Being of Water's blade",
"とどめになってしまったようじゃった":
    "seemed to have dealt it a fatal blow.",
"憐れに思った水の者は": "Moved by pity, the Being of Water",
"自分の紋章を": "passed its own crest",
"龍に継承したのじゃ": "to the dragon.",
"自分の犯した罪のせめてもの償いにとな…":
    "As atonement, however small, for the wrong it had done...",
"うおおおおおおおおおおお！？": "Woooooaaah!?",
"てことは…てことはだ…": "Which means... which means...",
"紋章は龍が持っているってことか！？":
    "the crest is with the dragon!?",
"そうなのかオタキ様！！": "Is that so, Lady Otaki!!",
"そうじゃな…そうじゃが…": "That's right... but...",
"もう少しで終わるんじゃ…黙ってなさい！！":
    "We're almost done... now hush!!",
"あーーーー！龍に会いたいーーーーー！！":
    "Aaaah—! I want to meet the dragon—!!",
"水の者から紋章を継承した龍は":
    "The dragon, having received the crest from the Being of Water,",
"元気になったのじゃ": "regained its strength.",
"しかし潰れた目は元に戻らなかった":
    "Yet its ruined eye never recovered.",
"龍は云った": "The dragon spoke:",
"お前の過ちを赦すことはできない":
    "'I cannot forgive your transgression.",
"しかしお前のその慈悲のこころに":
    "But in return for that compassion of yours,",
"少しだけ応えてやる": "I shall grant you but a little.",
"ウィンはおじぎをした": "Win bowed.",
"これからお前を地上に": "I shall return you to the surface,",
"帰してやるが": "but",
"帰ったら必ず地上の洞窟を塞ぎ":
    "once back, you must seal the cave,",
"二度と人間が迷い込まぬよう": "so that no human ever",
"穴から落ちてこぬようにしろと":
    "wanders in and falls down this pit again.'",
"地上に帰った水の者は約束を守り":
    "Returned to the surface, the Being of Water kept its promise:",
"洞窟をふさぎ": "it sealed the cave",
"そこにお社を建てたのじゃ": "and built a shrine upon it.",
"二度と龍の上からひとが落ちぬようにとな…":
    "So that none would ever fall upon the dragon again...",
"そうするとやがて": "And in time,",
"雨はやみ、川は穏やかになり": "the rains ceased, the rivers calmed,",
"木々は青々と育ち": "the trees grew lush,",
"この地は豊かになったのじゃ": "and this land became bountiful.",
"自己紹介が済んだんだから、もういいだろ？":
    "Introductions are done, so can we move on?",
"おわりじゃ！": "That's the end!",
"本題だ！": "On to the main point!",
"うおおおおおおおおおおお……お？":
    "Woooooaaah... uh?",
"よしわかった、早く龍をぶちのめしに行くぞ！":
    "Alright, understood—let's go beat up that dragon!",
"うおおお…　あ、そういう話か、これ？":
    "Whoaa... oh, so that's how it is?",
"ナガレ！そうやってすぐ村の守り神である":
    "Nagare! It's because you always talk about",
"龍を、ぶちのめすとか、食べるとか":
    "beating up or eating the dragon—the village's guardian—",
"言っておるから、この話をしなかったんじゃ！":
    "that we never told you this story!",
"クスクス…": "Hehe...",
"…え？なに笑ってんの姉さま？": "...Huh? What's so funny, sis?",
"そんなナガレが当主になった途端に、":
    "That the moment a Nagare like you became head,",
"この度の事態…闇の復活が起こるとはのう…":
    "this crisis—the Dark's revival—should occur...",
"いらっしゃいましたね。": "You've arrived.",
"ナガレ…": "Nagare...",
"これも龍の思し召しかも知れぬの。":
    "Perhaps this, too, is the dragon's will.",
"わしやシズクでは、とてもじゃないが、":
    "For me or Shizuku, going to meet the dragon is",
"龍に会いになど行けぬからの。":
    "quite simply out of the question.",
"…そうか。セイリュー当主はいざとなったら、":
    "...I see. So when the time comes, the Seiryu head must go",
"龍から本物の紋章を奪い返しに行かないと":
    "and take the true crest back",
"だったんだな…。": "from the dragon...",
"そういうことじゃ…。": "That's right...",
"ナガレよ。セイリュー当主が代々伝えてきた":
    "Nagare. What the Seiryu heads have passed down",
"のは、このときの為だったのじゃ。": "was for this very moment.",
"洞窟の奥にいるという龍と会うなど…":
    "Meeting the dragon said to dwell in the cave's depths...",
"初代の水の者以来、誰もしたことのないこと。":
    "none has done it since the First Being of Water.",
"何が起こるかも分からん…": "None can say what will happen...",
"そもそも龍から紋章を奪い返すなどという":
    "Whether we can even take the crest back",
"ことが、本当に出来ることかも分からんのじゃ。":
    "from the dragon—that itself is uncertain.",
"そうだよ！紋章は、本当にこころから":
    "Right! Crests can only be passed to someone you",
"信頼した相手にしか継承できないはずだ！":
    "truly, wholeheartedly trust!",
"龍から奪い返すなんて…": "Forcibly taking it back from a dragon...",
"それこそ龍をぶちのめすなんて…":
    "And beating up the dragon at that...",
"そんなことして、紋章を継承できるとは":
    "I can't imagine the crest would accept",
"とても思えないぞ…？": "such a thing...?",
"え…？そうなの…か？": "Huh...? Is that... so?",
"ああ。だからこそ、紋章の奪い合いみたいな":
    "Yeah. That's why my big bro and dad said",
"争いごとも、いままでに起こったことが":
    "there's never been a conflict over",
"ないって、オレのアニキや親父も言ってた。":
    "snatching crests.",
"そうなのだとすると…": "If that's the case...",
"龍に会えたとしても、一体どのように":
    "Even if we meet the dragon, how on earth",
"紋章を継承するのでしょうか…？": "are we to inherit the crest...?",
"なんだよ…　せっかく龍をぶちのめせると":
    "Damn... and here I thought we could",
"思ったのに…": "beat up the dragon...",
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
