#!/usr/bin/env python3
"""Fill batch 32: Roi's apology, Pipin's departure scene."""
import csv
import os
import re

D = {
"為の時間を稼ぐために…": "just to buy it time...",
"紋章が父をほんの少しだけ生きながらえさせて":
    "the crest seemed to have kept my father alive,",
"いたように思えた。": "just barely.",
"…いや、とにかく": "...No, anyway,",
"自分でも思っていた以上に長話になって":
    "I've been talking far longer than",
"しまった…。　　すまん。": "even I expected... Sorry.",
"俺は、かつて…紋章継承者であり、":
    "I was once... an inheritor of the crest,",
"騎士団長でもあり…": "and the Knight Commander...",
"天才と呼ばれるくらいの力もあった。":
    "I even had power enough to be called a genius.",
"それなのに…": "And yet...",
"すべてに失敗したんだ。": "I failed at everything.",
"自分のことも、周りのことも…":
    "Myself, and everyone around me...",
"何が大事なのか分からなくなってしまった…":
    "I lost sight of what truly mattered...",
"ピピンには、そうなって欲しくなかった。":
    "I didn't want Pipin to end up that way.",
"ピピンなら、俺とは違う…":
    "I expected that Pipin—unlike me—",
"いい騎士団長になってくれると期待していた。":
    "would become a fine Knight Commander.",
"しかしそんなのは…": "But that was...",
"俺の勝手な期待だ…　": "nothing but my selfish expectation...",
"自分の出来なかったことを勝手に…":
    "I was projecting what I couldn't do myself",
"あいつに期待していたんだ。": "onto him.",
"………ウィン。": ".........Win.",
"もしピピンに会うことがあったら…":
    "If you ever meet Pipin...",
"俺が謝っていたと伝えて欲しい。":
    "tell him I apologized.",
"…。　ありがとな、ウィン…。":
    "...Thanks, Win...",
"きっと…　俺はこの話を、":
    "I suppose... I must have wanted",
"誰かに聞いて欲しかったんだ…":
    "someone to hear this story...",
"おかげで、少し楽になったよ。":
    "Thanks to you, I feel a bit lighter.",
"左手はつながったままだったが…":
    "Though his left hand remained intact...",
"剣を握ることはできなくなっていた。":
    "he could no longer grip a sword.",
"おう！言われなくても分かってるぜ。":
    "Oh! I know that without being told.",
"噂はフレイムまで届いているぜ！":
    "Word has reached even Flame!",
"天才騎士って呼ばれていたロイさんと、":
    "I always wanted to have a sword duel with",
"いつか剣の勝負をしてみたいと思ってた…":
    "Roi, the man called the genius knight...",
"んだけど…": "but...",
"いまのアンタ、剣が握れないんだってな。":
    "I hear you can't even hold a sword now.",
"おお、火の紋章の継承者、ホノオ王子ですな。":
    "Oh, Prince Hono, inheritor of the Fire Crest.",
"残念だぜ。": "That's a shame.",
"もし握れたとしても、フレイムの王子と":
    "Even if I could, dueling a prince of Flame",
"立ち会うなど恐れ多くて、出来るとは":
    "would be far too daunting—I don't think",
"思えんな。": "I could do it.",
"それよりも、王子、ウィン。":
    "More importantly, Prince, and Win.",
"セイリューへ急いでくれ。": "Hurry to Seiryu.",
"気になることがある…": "There's something on my mind...",
"私も急いで調べたいことがあるのだ。":
    "I too have things I need to investigate in haste.",
"風の紋章の継承者である、騎士ウィンと共に、":
    "Together with Knight Win, the Wind Crest's inheritor,",
"セイリューの水の紋章継承者と、少しでも":
    "please join up with Seiryu's Water Crest inheritor",
"早く合流してくだされ。": "as soon as possible.",
"言われなくても分かってるんだけど。":
    "I know that without being told.",
"噂はセイリューにも届いていた。":
    "Word had reached Seiryu as well.",
"天才騎士とほまれの高いロイさんと、":
    "The village's proudest warriors all buzzed about",
"いつか立ち合いがしてみたいと、":
    "wanting to cross blades someday with Roi,",
"村中の腕自慢が騒いでいたものだ。":
    "the knight famed as a genius.",
"剣が握れなくったって、城の兵たちに色々":
    "Even without a sword, you could still teach",
"おお、セイリューの領主、ナガレどのですな。":
    "Oh, Nagare, lord of Seiryu.",
"教えてやれることはあるんじゃないのか？":
    "the castle's soldiers all sorts of things, couldn't you?",
"…そうですな。いや、その通りです。":
    "...That's true. No, you're right.",
"しかしいまはその話よりも…":
    "But setting that aside for now...",
"少しでも早く、紋章の継承を急いでいただき":
    "I'd like you to hasten your crest's succession",
"たいのです。": "as soon as possible.",
"どうにも近いうちに何か起こる気がするのです":
    "I have a feeling something will happen before long.",
"ホノオ王子、騎士ウィンと共に、":
    "Prince Hono, together with Knight Win,",
"真の水の紋章継承を急いでくだされ。":
    "please hurry the true succession of the Water Crest.",
"『エレメントの本質』": '"The Essence of the Elements"',
"…と、書かれた本がある。読んでみようか…。":
    "There's a book on this. Should we read it...?",
"大昔のことばがほとんどで、ウィンには読めなかった…。":
    "It was mostly in ancient words, and Win couldn't read it...",
"『闇の四天王とは』": '"The Four Dark Generals"',
"……道士　…………": "......magi... ......",
"この四つの……唯…四天王……である":
    "these four... the only... Four Generals...",
"巨大な蛇の…女…士　…ケ……":
    "a giant serpent's... fe...male sa...ge... My...",
"……な鎧に……騎…　…ウ……":
    "in... dark armor... a knight... Na...",
"美し…化…血…………": "a beautiful... trans...formed... blood......",
"『騎士ロイ様へ』": '"To Lord Roi, Knight"',
"…と、書かれた手紙がある。読んでみようか。":
    "There's a letter with these words. Should we read it?",
"おい！勝手にいじるんじゃない！":
    "Hey! Don't go touching things on your own!",
"その目だ、ピピン。": "That look, Pipin.",
"お前のその目だ…。": "Those eyes of yours...",
"お前の目は…　かつての私と同じだ…。":
    "Your eyes... are the same as mine once were...",
"俺を連れ出しに…か。": "So you came to take me out...",
"……何を言っている…？": "......What are you talking about...?",
"ピピン、俺はお前の才能を買っていた。":
    "Pipin, I believed in your talent.",
"騎士団にお前を入れる最終決定も俺が下した。":
    "I made the final call to admit you into the order.",
"……だ、だったらなおのこと、どうして俺を":
    "......Th-Then all the more—why didn't you make",
"継承者にしない！？": "me the inheritor!?",
"お前の目は、自分が何を守りたいのかを":
    "Your eyes don't see what it is",
"分かっていない…。": "you want to protect...",
"自分のことしか考えていない…。":
    "You only think of yourself...",
"だから結局は、そう…": "And in the end, that's why...",
"お前は、自分自身のことすら分かっていない。":
    "you don't even understand yourself.",
"そんな男に、世界の命運は託せん。":
    "I cannot entrust the fate of the world to such a man.",
"陛下のことだ。用もなく俺を呼び出したりは":
    "Knowing His Majesty, he wouldn't summon me",
"き…きさま…！": "Y-You...!",
"だから俺はウィンを選んだ。":
    "That's why I chose Win.",
"ウィンも、以前から俺が期待していた":
    "Win too was a young man I'd had",
"若者だったからな。": "high hopes for since before.",
"しないはずだが、一応理由を聞かせて貰おう。":
    "He wouldn't, but I'll hear your reason anyway.",
"だが、ピピン。お前の力も必要だ。":
    "But Pipin. Your strength is needed too.",
"ウィンが見事継承者としての責務を果たせる":
    "See to it that Win fulfills his duty",
"よう、お前がしっかりと": "as inheritor—",
"うるさい！！": "Shut up!!",
"もういい…　どうでもいい…":
    "Enough... I don't care anymore...",
"俺は…騎士を辞める。": "I'm... quitting the knight order.",
"こんな国、出ていく。": "I'm leaving this country.",
"これは騎士団長からの命令だぞ。":
    "This is an order from the Knight Commander.",
"知らん。": "I don't care.",
"こんな侮辱、騎士団長といえども、":
    "Such an insult—even from the Knight Commander—",
"俺には許すことは出来ん…。":
    "I cannot forgive...",
"俺がここできさまを殺さずに去るだけでも…":
    "The mere fact that I'm leaving without killing you here...",
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
