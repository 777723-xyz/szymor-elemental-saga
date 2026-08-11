#!/usr/bin/env python3
"""Fill batch 38: Hono's trial climax, Seiryu meeting, ink-crest gag."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"敬語だって全然使えなくて…":
    "I couldn't even manage polite speech...",
"結局、みじめになっただけだったぜ。":
    "In the end, I just ended up pathetic.",
"ウィン！いるのか、オレのアニキがそこに…！":
    "Win! Is he there—is my big bro...!",
"つらい思いをしたんだな、ホノオ。":
    "You've suffered, haven't you, Hono.",
"ああ…　オレはアニキになれねんだよ…":
    "Yeah... I could never become him...",
"僕が生き返って、ちゃんと王になるよ。":
    "I'll come back to life and properly become king.",
"生き返るって…": "Come back to life...",
"一体どうやって？": "How, exactly?",
"ホノオ、おまえのその火の紋章だ。":
    "Hono, with your Fire Crest.",
"おまえのその紋章をぼくに継承すれば、":
    "If you pass your crest to me,",
"ぼくは生き返る…。": "I'll be revived...",
"おまえがずっと望んでいた世界になる…":
    "It'll be the world you've always wanted...",
"ぼくが王になって、この国をよくできる…":
    "I'll become king and make this country better...",
"…これが、試練てことか？": "...So this is the trial, huh?",
"そうだよ、ホノオ。": "That's right, Hono.",
"ここは死人の魂の通り道…":
    "This is a passageway for dead souls...",
"ここでなら、死者に継承して復活させることができる":
    "Here, one can pass a crest to the dead and revive them.",
"さあ、考えてくれ、ホノオ…":
    "Come on, think it over, Hono...",
"なあ、ホノオ。": "Hey, Hono.",
"僕が生き返ったらどうする？":
    "What'll you do once I'm back?",
"そんでオレは、剣を振り回して":
    "Then I'd just swing my sword around",
"走り回っていればいい…。": "and run about...",
"そう、それこそオレの望んだ未来だった…。":
    "Yes, that was the future I'd wished for...",
"その未来が手に入るんだよ、ホノオ。":
    "That future is within reach, Hono.",
"さあ、ぼくに紋章を継承しよう。":
    "Come, pass the crest to me.",
"そして二人の夢を叶えよう。":
    "And let's make both our dreams come true.",
"ウィンは叫ぼうとしたが声が出ない":
    "Win tried to shout, but no voice came out.",
"うっ…　　ううっ…": "Uh... ...Uuh...",
"ホノオ、どうして泣くんだ？": "Hono, why are you crying?",
"うっ…　それはよう…": "Uh... it's because...",
"オマエがアニキの偽物だとわかって":
    "I've realized you're a fake,",
"心から悲しんでるからだよーーー！！":
    "and it breaks my heart—!!",
"なんだって！？": "What!?",
"くそー！！！": "Damn—!!!",
"ホントにアニキかもって思ったのによー！！":
    "I actually thought you might be the real him!!",
"いやいや、ホノオ！": "No no, Hono!",
"ぼくホムラだから！！": "I'm Homura!!",
"あのなー試練さんよーーー": "Hey, Trial-san~",
"アニキはオレのことをバカにしたことは":
    "Big bro never once",
"一度もねえんだよ…": "made fun of me...",
"オレがマジで気にしているマジでマジでの":
    "Even my 'for real, for real' tic that I'm",
"口癖のことを…": "so self-conscious about...",
"俺らしいとか絶対に言わねえんだよ、":
    "the real him would never say it suits me,",
"本物ならよーーーーーーー！！": "if he were real—!!",
"ぐっ！": "Guh!",
"あとなー試練さんよーーー": "And another thing, Trial-san~",
"…ホムラ兄貴が王になって、この国を":
    "...If Homura had become king and made this country",
"アニキはよー…": "Big bro...",
"王になりたくなかったんだよ…":
    "he never wanted to be king...",
"アニキは王になりたくなかった…":
    "He never wanted the throne...",
"アニキはいつも…": "He was always...",
"オレに王になれと言っていたんだ…":
    "telling me to become king...",
"…オレにだけよーーー！！！":
    "...and only to me—!!",
"だから、アニキなら、本物のアニキなら…":
    "So if you were really him...",
"どんどん良くする。": "make it better and better.",
"王になりたいなんて言わねえんだよ！！":
    "you'd never say you want to be king!!",
"マジでよーーーーーーーー！！！！":
    "For real—!!!!",
"ぐわーーーーーーーーーーー": "Gwaaaaah—",
"…もう振り向いても大丈夫そう？":
    "...Safe to turn around now?",
"なあ、ウィン。": "Hey, Win.",
"オレの試練ぶり、どうだった？":
    "How'd I do on the trial?",
"合格！！！！！！！！！": "Passed!!!!!!!",
"こんなのに付き合わせて悪かったな…":
    "Sorry for dragging you through that...",
"さあ、親父にどやされに行くか！":
    "Come on, let's go get scolded by the old man!",
"へ…？": "Huh...?",
"ん？　おい、ナガレ。": "Hm? Hey, Nagare.",
"誰か来たぞ。": "Someone's coming.",
"うん…　なんかすごく強そうなひとたちだ…":
    "Yeah... they look really strong...",
"手伝ってもら…": "Maybe they can he—",
"うるせえ！！　よそもんなんぞ邪魔だ！":
    "Shut up!! Outsiders are nothing but a nuisance!",
"あたしらだけで十分だろうが…":
    "We can handle it on our own...",
"行くぞ、トリカゼ！マハリ！":
    "Let's go, Torikaze! Mahari!",
"そりゃそうだ。": "That's true.",
"ちょっとまっとけよー　よそもんさんがたー":
    "Hold on a second, you outsiders~",
"えー！？": "Huh!?",
"大丈夫かなあ…　ぼくの剣術で…":
    "I wonder if I'll be okay... with my swordsmanship...",
"うおおお！？": "Whoaa!?",
"なんだあのデッカイ魔物はー！！":
    "What IS that giant monster—!!",
"俺らは火と風の紋章の継承者の、ホノオと":
    "We're the inheritors of the Fire and Wind crests—",
"ウィンだ。": "Hono and Win.",
"闇のエレメントが復活しようとしてる。":
    "The Dark Element is about to revive.",
"つ、つええ…": "S-So strong...",
"それで、水の継承者と合流する為に、":
    "And to meet up with the Water inheritor,",
"オレたちはここに来たのさ！": "we came here!",
"ウィンとホノオは左手の紋章をナガレに見せた":
    "Win and Hono showed Nagare the crests on their left hands.",
"本当みたいだな…。": "Seems it's true...",
"じゃああたしも…": "Then I'll show you mine too...",
"ナガレはウィンとホノオに紋章を見せた":
    "Nagare showed her crest to Win and Hono.",
"あたしがセイリュー当主であり、":
    "I'm the head of Seiryu,",
"水の紋章の継承者さ！": "and the Water Crest's inheritor!",
"あんたが継承者か！": "So you're the inheritor!",
"これは頼りに………　　っておい":
    "This is a relief...... wait, hey,",
"あんたの紋章…　なんか違くねえか？":
    "your crest... something's off, isn't it?",
"なんだよ、違うって…": "What do you mean, off...",
"いやいや、本当にあたしが継承者だし…":
    "No no, I really am the inheritor...",
"おいおい、変なケチ入れんじゃねえぞ。":
    "Hey now, don't go nitpicking.",
"ナガレはれっきとした継承者さ。": "Nagare's a proper inheritor.",
"本当です。": "It's true.",
"ナガレは先日、前当主のシズク様から、":
    "Just the other day, Nagare underwent the formal succession",
"正式な紋章継承の儀式を行いました。":
    "from the previous head, Lady Shizuku.",
"その通り！！": "Exactly!!",
"これ以上あたしと紋章を侮辱するなら、":
    "Insult me and my crest any further,",
"おまえたち、ただじゃおかねえぞ…":
    "and you won't get off easy...",
"いやでもよ…": "No, but...",
"なあ、もしかして、それ墨か…？":
    "Hey, wait—is that ink, by any chance...?",
"墨か何かで書いてあるのか…？":
    "Drawn with ink or something...?",
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
