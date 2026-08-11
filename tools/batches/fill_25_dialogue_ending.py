#!/usr/bin/env python3
"""Fill batch 25: ending sequence, credits, NG+ prompt."""
import csv
import os
import re

D = {
"ダハハハハハハハハーーーッ！！！！":
    "Bwahahaha—!!!",
"あああぁぁぁぁアアアァァーーッ…！！！":
    "Aaaaaah—!!!",
"キ…モチ…ィイー……ッ！！！！！":
    "It... feels... GOOD......!!!!!",
"…陛下": "...Your Majesty",
"ちなみに、これはフレイム王も": "Incidentally, King Flame",
"言っていたことだ。": "said the same thing.",
"なに！？　フレイムの王が！？":
    "What!? The King of Flame!?",
"フレイム王は俺に、火の紋章の継承者選びを":
    "King Flame told me that choosing the Fire Crest's inheritor",
"俺に任せると言った…。": "was up to me...",
"ウィンをはじめ、継承者の者たちの働きにより":
    "Thanks to the efforts of Win and the other inheritors,",
"必ずしも王族が継承する必要はないと…。":
    "he said the inheritor need not always be royalty...",
"つまり…いまや紋章は権力の象徴ではない…":
    "In other words... the crests are no longer symbols of power...",
"本当に強く、持ち主が信頼できる者に受けつぐ":
    "they should pass to those who are truly strong,",
"べきものだとな…。": "and trusted by their holders...",
"見事、闇の復活は阻止された…":
    "Splendidly, the Dark's revival was stopped...",
"なるほどな…　お前の話、よくわかった。":
    "I see... I understand your point.",
"こうなれば…陛下、よろしいですな。":
    "If that's so... Your Majesty, if you'll allow it.",
"うむ…　最早お前の好きにするがいい！":
    "Indeed... From now on, do as you see fit!",
"では、ウィンよ。": "Then, Win.",
"お前はいまのまま、継承者でありながら、":
    "You may remain as you are—an inheritor",
"一般の騎士として勤めるがいい。":
    "serving as an ordinary knight.",
"しかし、ピピンの担当していた騎士隊長の座が":
    "However, the Knight Captain post Pipin held",
"空いている…　それをお前に任せる！":
    "is vacant... I entrust it to you!",
"よくやってくれたぞ！！": "Well done!!",
"………よかったな、ウィン。": "......Good for you, Win.",
"ウィン、ピピン！！": "Win, Pipin!!",
"…話はついたようだな。": "...It seems the discussion is done.",
"なら、俺はこれで失礼する。":
    "Then, I'll take my leave.",
"陛下…　騎士団長…　色々世話になりました…":
    "Your Majesty... Knight Commander... thank you for everything...",
"…がんばれよ、騎士隊長殿。":
    "...Do your best, Knight Captain.",
"ん？…これからの俺について、気になるのか？":
    "Hm? Curious about what I'll do now?",
"…暗黒大陸に行こうと思っている。":
    "...I plan to go to the Dark Continent.",
"俺なら、闇の瘴気の影響も受けないしな。":
    "The Dark miasma doesn't affect me, after all.",
"あそこに他に何があるのかを調べたいんだ。":
    "I want to find out what else is out there.",
"おいおい…心配するなよ…": "Hey, hey... don't worry...",
"俺を誰だと思ってるんだ？": "Who do you think I am?",
"じゃあな、ウィン。": "So long, Win.",
"どこへ行くつもりだ、騎士ピピン？":
    "Where do you intend to go, Knight Pipin?",
"話は終わっていない…": "The discussion isn't over...",
"これは、お前の始めた話だ。":
    "This is a matter you began.",
"戦士である継承者と…頭脳を使う騎士団長は、":
    "The warrior-inheritor and the brain-working Knight Commander—",
"別のものが務める方がいいのだろう？":
    "it's better they be different people, right?",
"であれば…　俺と同じか…それ以上に":
    "If so... there's a knight who's as sharp,",
"頭の切れる騎士がいる…": "or sharper, than me...",
"その者は頭がいいだけではなく、暗黒大陸に":
    "That one isn't just clever—he went to the Dark Continent",
"ひとりで向かい、窮地の継承者たちを救い、":
    "alone, saved the inheritors from a crisis,",
"闇の復活を阻止した…実績も申し分ない騎士だ":
    "and stopped the Dark's revival... his record is impeccable.",
"…あんた、まさか…": "...You... you don't mean...",
"…まさか？": "...Mean what?",
"何を言う…　お前の言葉に従えば、俺の判断も":
    "What do you mean... by your own logic, my decision",
"至極当然のものだろう。": "is only natural.",
"では…　陛下、お願いします。":
    "Then... Your Majesty, if you please.",
"うむ！！！！": "Indeed!!!!",
"闇の復活を阻止した継承者であるウィン！！":
    "Win, the inheritor who stopped the Dark's revival!!",
"そなたの功績を称え、それに応えるには…":
    "To honor your achievements, and answer them in kind...",
"騎士ピピンを、ウィンダム騎士団長に命ずる！":
    "I hereby appoint Knight Pipin as Windam Knight Commander!",
"…な…んだと…！？": "...Wh-What...!?",
"ピピン…やってくれるな？": "Pipin... you'll do it, right?",
"…いや、本当にいいのか…？":
    "...No, is this really alright...?",
"だって、俺は………": "Because I'm......",
"お前を騎士団長に任命せねばなるまい！":
    "I must appoint you Knight Commander!",
"騎士団長ピピン！！　継承者ウィン！！":
    "Knight Commander Pipin!! Inheritor Win!!",
"ふたりでこれからも我がウィンダム王国を":
    "Together, continue to support our Windam Kingdom",
"支えてくれ！！": "from now on!!",
"ウィンをこれより、ウィンダム騎士団長に":
    "From this moment, I hereby appoint Win",
"ウィンは大きく頷いた！！": "Win nodded firmly!!",
"…どうしてお前は…": "...Why are you...",
"そんなに嬉しそうなんだ…？　ウィン…":
    "so happy about this...? Win...",
"任命する！！": "as Windam Knight Commander!!",
"制作ツール　ＲＰＧツクールＭＶ":
    "Engine: RPG Maker MV",
"使用プラグイン作者様": "Plugin authors:",
"EnemyBreathing        Yana": "EnemyBreathing        Yana",
"TurnWindow         Yana": "TurnWindow         Yana",
"KZR_WindowStatusInBattle   ぶちょー様":
    "KZR_WindowStatusInBattle    Bucho",
"BattleBalaneCustom   　木星ペンギン様":
    "BattleBalanceCustom    Mokusei Penguin",
"PD_AdjustCharaSprite     しおいぬ様":
    "PD_AdjustCharaSprite      Shioinu",
"MakeScreenCapture　　トリアコンタン様":
    "MakeScreenCapture    Toriakontan",
"RetryBattle　　トリアコンタン様":
    "RetryBattle    Toriakontan",
"UCHU_MobileOperation    uchuzine様":
    "UCHU_MobileOperation    uchuzine",
"使用タイルセット作者様": "Tile set authors:",
"MV_hc_tilesets　　　リクドウ様":
    "MV_hc_tilesets    Rikudo",
"和風素材　　　　コミュ将様":
    "Japanese-style materials    Comyu-sho",
"主人公たちの顔グラフィック　文目ゆうき様":
    "Heroes' face graphics    Ayame Yuki",
"【エレサガ大王】": "[Elesaga Daio (Elesaga King)]",
"むにゃ　様": "Munya",
"(はじまりの二周目裏ボス撃破したもの)":
    "(for those who beat the second-playthrough hidden boss)",
"オリジナル版": "Original version",
"2002年　エレメンタルストーリー":
    "2002  Elemental Story",
"制作ツール　RPGツクール5": "Engine: RPG Maker 5 (95)",
"…急ですまんな、ウィン。": "...Sorry for the suddenness, Win.",
"リメイク版": "Remake",
"2019年　エレサガ　Elemental Saga　":
    "2019  Elesaga / Elemental Saga",
"制作ツール　RPGツクールMV": "Engine: RPG Maker MV",
"しかし陛下からのどうしてもとのお達しだ。":
    "But His Majesty insisted.",
"製作総指揮　西園寺ハムカツ":
    "Producer: Saionji Hamkatsu",
"2019　エレサガ制作委員会":
    "2019 Elesaga Production Committee",
"サンキューフォープレイング！！！！！！！！":
    "THANK YOU FOR PLAYING!!!!!!!!",
"このお話はこれでおしまいおしまい、だ！！！":
    "And so, this tale comes to an end!!",
"もう一回始めちゃう？？": "Want to start over?",
"それとも終わりにしちゃう？？？？":
    "Or call it done?",
"お前の実績と…そしてこの戦いをくぐり抜けた":
    "With your achievements... and having lived through this battle,",
"ここで終りにしてももう何も起こらないので、":
    "nothing more will happen if you end it here, so",
"のを、オススメしておくぞ！！":
    "I'd recommend finishing now!!",
"その実力、お前の就任に誰も反対する者はない。":
    "With that skill, no one will oppose your appointment.",
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
