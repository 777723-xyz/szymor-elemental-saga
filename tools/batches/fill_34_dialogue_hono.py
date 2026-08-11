#!/usr/bin/env python3
"""Fill batch 34: checkpoint NPCs, Hono's trial aftermath, King Flame's confession."""
import csv
import os
import re

D = {
"ほんのちょびっとだけ相手してあげよう！！":
    "I'll play with you just a tiny bit!!",
"ってわけさ　ヒック": "And that's how it is... hic.",
"あ、そこにいる行商人からライスボール":
    "Oh, have you tried buying Rice Balls",
"買ってみた？　美味しいよー": "from the peddler over there? They're tasty~",
"だけどセイリューだとあの半額で買えるんだ":
    "But in Seiryu, you can get them for half that price.",
"最近盗人が多いんだ。": "There've been a lot of thieves lately.",
"あんたも気をつけてくれよ！":
    "You watch out too, alright!",
"なら、うちに来い。": "Then come to my place.",
"誰かに声掛けとくからよ。":
    "I'll tell someone about you.",
"オレの部屋使えよ！": "Use my room!",
"…ックー？": "...Yip?",
"何だお前…ひとりぼっちなのか？":
    "What's with you... all alone?",
"あっ、きしだ！": "Oh, it's the knight!",
"かっくいいいい！": "So coool!",
"もっとめぐんでくれやーーーーーーー":
    "Give me a bit more, won't ya—",
"見回り中にスリに財布とられたんだよーーー":
    "A pickpocket swiped my wallet during patrol—",
"次の給料までくらせないんだよーーーーー":
    "I can't eat until next payday—",
"うわあああああああああ": "Waaaaaah",
"あんちゃーーーん": "Big bro~",
"めぐんでくれやーーーー": "Spare a little something—",
"1Gてあんちゃーーーーん": "Just 1G, big bro~",
"うぃーす、あー、早く休憩なんねえかなー":
    "Yo... ah, when's break time gonna come~",
"ハラ減ったあ": "I'm hungry~",
"すいません、ぼく、仕事中はすごく集中する":
    "Sorry, but I concentrate intensely during work,",
"ので、話し掛けないでーーー": "so please don't talk to me~",
"軍隊は最高だな！　": "The army's the best!",
"国からお金もらってのんびりできるんだから！":
    "Getting paid by the country and taking it easy!",
"うーん　むにゃむにゃ…": "Umm... mumble mumble...",
"はっ！！　えっ！？？": "Hah!! Huh!??",
"なんでオレ寝顔のぞかれてんの！！？？":
    "Why are you staring at my sleeping face!!??",
"意味をセイリューのひとも知らないらしいぜ":
    "Even the Seiryu folks don't know what it means.",
"そうかー？": "Is that so~?",
"まんきんたんだぜ？　毒消しってよりなんか":
    "Mankintan, huh? It sounds more like money or",
"お金というか宝石みたいな響きだなあ":
    "a gem than an antidote, doesn't it?",
"この前ヘビに噛まれてさーーー":
    "Got bitten by a snake the other day—",
"万金丹で治したんだけど、": "cured it with Mankintan, but,",
"まんきんたん？　変な名前だよなーーー？":
    "Mankintan? What a weird name, huh?",
"セイリューの？　特産？　らしいけどさー":
    "It's a Seiryu specialty or something, apparently~",
"いろんな情報を集める事だからな！":
    "Gathering all sorts of info is the job!",
"早速しごとにとりかかるぜ！": "Time to get to work!",
"じゃあな、ウィン！": "See ya, Win!",
"ウィン！　俺はここまでだ！": "Win! This is where we part!",
"俺の仕事は、フレイムの城下町で":
    "My job is to scope out the curries—I mean,",
"いろんなカレーを…じゃなかった！":
    "survey the various dishes in Flame's castle town—no wait!",
"思い悩む顔も、他国のひとびとよりも少ない。":
    "and the faces of its people seem less troubled than those of other lands.",
"どうなるかを調査した結果をここに報告します。":
    "Here I report the results of my survey of how things would unfold.",
"漠然と火の恵み、水の恵み、風の恵み…自然からの恩恵、":
    "Vaguely, the blessings of Fire, Water, Wind... the gifts of nature,",
"あ…　あ…　アニキ…！！？": "Ah... Ah... Big bro...!!?",
"アニキ…　": "Big bro...",
"あっ…！！": "Ah...!!",
"なんだったんだ…　まぼろし…？":
    "What was that... a vision...?",
"ウィン、オマエさっきの見たか？":
    "Win, did you see that just now?",
"ありがとうと呟き、涙を流しながらひざまづいたのだ。":
    'He murmured "thank you" and knelt down, tears streaming down his face.',
"…来たよ。": "...He's here.",
"ホノオは南の遺跡に継承の試練に向かった。":
    "Hono has gone to the Southern Ruins for the trial of succession.",
"いまからなら追いつけるだろう。":
    "If we leave now, we can catch up.",
"ウィン殿、あいつを連れ戻して来て下され。":
    "Sir Win, please bring him back.",
"皆が止めるのを聞かず、勝手に出て行った":
    "He left on his own, ignoring everyone's pleas.",
"お前は強かった。": "You were strong.",
"わしらのことも、ホムラのことも、":
    "Overcoming everything—us, and Homura,",
"自分で乗り越えた…": "on your own...",
"お前という強い王子を持つことができた…":
    "To have a prince as strong as you...",
"わしら全員の誇りなのだ、お前は。　":
    "you are the pride of all of us.",
"親父…。": "Dad...",
"ものの態度か！！": "What kind of attitude is that!!",
"だが…わしは誇りに思いながらも、":
    "But... even as I felt proud,",
"お前を信じられなかったのだ…。":
    "I couldn't bring myself to trust you...",
"お前はいまだにこころの中では…":
    "In your heart, even now, you—",
"王になりたくないのではないか…":
    "don't you truly not want to be king...?",
"ホムラがいたならと思っているのではないか…":
    "don't you wish Homura were still here...?",
"もしそうであったなら…": "If that were so...",
"試練を乗り越えることはできない…":
    "you could never pass the trial...",
"あれは…自らが王になるのだという意思が":
    "because it can never be cleared without the will",
"なければ、決して合格できないからな…。":
    "to become king oneself...",
"あはは…えー　まあ、そうなの…か？":
    "Ahaha... um, well, is that... so?",
"だから…お前が試練に行くのを…":
    "That's why... when you went for the trial...",
"わしはあれほどに止めたのだ…恐れたのだ。":
    "I stopped you so insistently... because I feared it.",
"だがお前は試練を乗り越えた。":
    "But you overcame the trial.",
"しっかりと、王になる覚悟を持っていた。":
    "You had the resolve to become king, firmly.",
"持っていてくれた…。": "You had it...",
"ああ、持ってるぜ。": "Yeah, I've got it.",
"安心しな！": "Don't worry!",
"でもよー…": "But hey...",
"そんなお前を信じてやれないで、本当に":
    "I'm truly sorry I couldn't trust you—",
"すまなかった、ホノオ。": "forgive me, Hono.",
"そしてもう今後二度と…": "And from now on, never again...",
"わしはお前を疑わんと誓う。":
    "I swear I shall never doubt you.",
"お前は偉大な王になる。そして…":
    "You will become a great king. And...",
"闇のエレメントの復活も阻止してくれるだろう":
    "you will stop the Dark Element's revival, I'm sure.",
"ちゃんと試練は合格したぜ。":
    "I passed the trial fair and square.",
"もちろんだぜ！": "Of course!",
"もう言うことはない。": "I've nothing more to say.",
"行くがよい、火と風の勇者よ！":
    "Go forth, heroes of Fire and Wind!",
"このウィンが証人でもあるんだぜ！":
    "This Win here can vouch for it!",
"それ以外にも…　まあ…": "Besides that... well...",
"色々世話になったけど…": "you've helped me a lot, but...",
"ウィン殿、今回の件、フレイム王として":
    "Sir Win, as King of Flame, I thank you",
"深く感謝しますぞ。": "deeply for this.",
"そして、ホノオ…": "And, Hono...",
"試練、ご苦労だった…": "the trial... you worked hard...",
"ああ。これでオレは正真正銘の次期国王だな。":
    "Yeah. Now I'm the true, legitimate next king.",
"そんで…": "And...",
"正真正銘の紋章継承者にもなったみてえだぜ":
    "it seems I've become a true crest inheritor too.",
"おお…紋章が輝いている…！":
    "Oh... the crest is shining...!",
"よう、親父！": "Yo, Dad!",
"ああ、試練の前に、闇の四天王とかってのに":
    "Yeah, before the trial, we were attacked by the so-called",
"襲われたんだが、オレとウィンの紋章の力で":
    "Four Dark Generals, but with the power of mine and Win's crests,",
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
