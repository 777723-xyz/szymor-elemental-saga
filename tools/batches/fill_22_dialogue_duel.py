#!/usr/bin/env python3
"""Fill batch 22: Pikepike's final scene, Nagare vs Mycenae duel."""
import csv
import os
import re

D = {
"この子いい子だな…": "What a good kid...",
"一生懸命名前言おうとしてるじゃないか…":
    "He's trying so hard to say my name...",
"いや、ていうかなんで言えないんだあああ！？":
    "No wait, why can't you say it!?",
"お喋りはその辺にして、さっさとバトルしろ、":
    "Enough talk—get to the battle already.",
"しかしおかしいぞ…": "But something's odd...",
"魔王になることを急いでいるんなら、":
    "If you're in a hurry to become the Demon King,",
"どうして貴様はここにいる…？":
    "why are you still here...?",
"四天王最強のお前が、ラスボスであるお前が…":
    "You, the strongest of the Four Generals—the final boss—",
"なぜここで時間を稼いでいるんだ？":
    "why are you buying time here?",
"…魔王にならなくていいのか？":
    "...Don't you need to become the Demon King?",
"ピカピカ！": "Pikapika!",
"いやーもう…　私は長く生き過ぎたんだ。":
    "Ah, well... I've lived far too long.",
"皆は私に魔王になれと言ったよ…。":
    "They all told me to become the Demon King...",
"闇のエレメントの復活の為に、文字通り":
    "Because I literally did the most to revive",
"もっとも骨を折ってきたのが私だからな！！":
    "the Dark Element!!",
"だが私はもう疲れた…　くるぴー！！":
    "But I'm tired... so tired!!",
"新しい闇の時代は、あいつらに託すつもりだ…":
    "I'll leave the new age of darkness to them...",
"くーっ　まただッ！！": "Ugh! Again!!",
"それに…　ここまで闇の復活に同調し、":
    "Besides... you've resonated with the Dark's revival this far,",
"自然の力を操る力までを持ってしまった":
    "and even gained power over nature itself—",
"キミたちを止められるのは…":
    "the ones who can stop you...",
"もう私しかいない！！！！": "are none but me!!!!",
"キミたちを止められるのは、私しかいない！！":
    "Only I can stop you!!",
"だから…最強のアンタが時間稼ぎに":
    "So... the strongest one wasting time...",
"ひとの名前くらいちゃんと覚えろ！！":
    "At least learn people's names properly!!",
"出向いたってワケか…": "So that's why you came...",
"他の四天王に未来を託して…！":
    "entrusting the future to the other Generals...!",
"ほらあたしの言った通りじゃないか！":
    "See, just as I said!",
"時間稼ぎだった！！": "It was stalling!!",
"自分の夢の叶うところを、自分で見られなくても":
    "He's fine never seeing his dream come true himself,",
"いいってんだな…　叶うなら！！":
    "as long as it comes true!!",
"失礼だろうがああああああああ！！":
    "That's so rude—!!",
"そのとおおおおおおおり！！！！":
    "Exactly—!!",
"おい！だから感心してる場合じゃない！":
    "Hey! This is no time to be impressed!",
"これ以上時間稼ぎに付き合ったらダメだろ！？":
    "We can't let him keep stalling!",
"青いの！！　もう大丈夫だ！！":
    "Blue one!! It's fine now!!",
"十分に稼がせてもらったぞーーーーー！！":
    "I've bought enough time—!!",
"あと少しで、新たな光の柱が立あああつ！！":
    "Soon, a new Pillar of Light will ris—!!",
"そうしたら闇インフルエンザが全土に広がり…":
    "Then the Dark Flu will spread across the land...",
"闇のエレメントによる王国が誕生するのだ！！":
    "and a kingdom of the Dark Element will be born!!",
"ウィン！ホノオ！！": "Win! Hono!!",
"バトル準備しろ！！": "Get ready for battle!!",
"お、おう！！": "O-Okay!!",
"いや、ごめん…　違うんだよ、":
    "No, sorry... it's not what it looks like,",
"これで最後だ…　マジで最後だ…":
    "this is the last one... for real, the last...",
"絶対にこれで本当のマジで最後にするのだ…":
    "I swear this is truly, absolutely the final one...",
"お前たち、継承者たちに………":
    "The era of you inheritors...",
"いじわるされまくる時代はなーーーーー！！":
    "endlessly teasing me—that era is over!!",
"いくぞおおおおおおおおおお！！":
    "Here I come—!!",
"ちょっと聞き取りにくいんだ…　":
    "It's a bit hard to make out...",
"もう一回いいか？": "Could you say it once more?",
"…ピケピケ": "...Pikepike",
"えっと…よくわからんから…":
    "Um... I can't quite get it, so...",
"ピカピカでいいな！！": "I'll just go with Pikapika!!",
"うおーい待っていたぞおうおおおお…":
    "Heeey, I've been waiting—!",
"なんでだろう…　私の名前は、何…？":
    "Why is it... what even is my name...?",
"キミらのお国ではなんか恥ずかしい言葉とか":
    "In your country, is it something embarrassing",
"だったりするのか…？　不安になってきた":
    "or rude...? I'm getting worried.",
"あー　でもそこのキミ！！": "Ah, but you there!!",
"そこの金髪の子は、前に一度会ったよね？":
    "You, the blond one—we've met once before, right?",
"覚えてるーーーーーー？？": "Remember—??",
"紋章の継承者たちよおおおおーーーーー！！":
    "O, inheritors of the crests—!!",
"え、ウィン、コイツと知り合いなのか？":
    "Huh, Win, you know this guy?",
"ウィンは紋章を継承する前":
    "Win explained that before inheriting the crest,",
"ピピンと一緒に西の監視塔に　":
    "he had gone to the West Watchtower",
"行ったことを話した": "with Pipin.",
"ピピンか…　": "Pipin, was it...",
"ウィンダムで操られて暴れたあの天才騎士だな":
    "That genius knight who went on a rampage under control in Windam.",
"まあまあ！　そう慌てなさんなって…":
    "Now, now! Don't get so flustered...",
"私たちがココで何をしているかとかー…":
    "About what we're doing here...",
"これからキミたちの世界に何が起こるかー…":
    "and what's about to happen to your world—",
"本当はラスボスで！四天王のリーダーである！":
    "I, the true final boss and leader of the Four Generals!",
"このピケピケ様がああああ、":
    "the great Pikepike, will",
"くわしく説明してあげようと思ってーーーー":
    "explain it all in detail—",
"出て来やがったなー　見たことないやつ！！":
    "So you finally show yourself, you stranger!!",
"わーざわざ！！": "Specially!!",
"一番最初に来てあげてるんだよー！！？？？":
    "I came all this way first—!!???",
"えっ…？　教えてくれるのか！？":
    "Huh...? You'll tell us!?",
"四天王最強の私だから。当然キミたちを！！":
    "As the strongest of the Four Generals, of course!",
"ここで殺せるワケ。どうせ死ぬキミたちになら":
    "I can kill you right here. To you, who'll die anyway,",
"だ……出し切ったああああああああああああ":
    "I've...... poured it all out—!!",
"千年くらい鍛え続けてきた私の魔力…":
    "The magic I've honed for a thousand years...",
"そして夢…　願い…　熱い思い………":
    "my dreams... my wishes... my burning passion......",
"すべて出し切ったああああああああ！！！！":
    "I've poured it ALL out—!!!",
"世界よ…………グッドバイ！！！！！！！！！":
    "World... good... bye!!!!!!!",
"狂戦士のキノコを手に入れた！":
    "Obtained a Berserker Mushroom!",
"さあ、一対一だ、ミケーネ…": "Come, one-on-one, Mycenae...",
"あんたには青龍のときの貸しもある…　それを":
    "You still owe me from the Seiryu incident... and",
"いまここで、きっちり返してもらう…！！":
    "I'll collect it right here and now...!!",
"ナガレ、って言ったわね…": "Nagare, was it...",
"あなた、ブリザードを封じてすでに勝った気で":
    "You think sealing my Blizzard means you've already won,",
"いるみたいだけれど…": "don't you...",
"あなたのツナミもあたしには効かない…":
    "Your Tsunami won't work on me either...",
"ブリザードで同じように相殺できるわ。":
    "I can cancel it out with my Blizzard just the same.",
"だから…あなたとあたしの戦いは、":
    "So... our battle will be",
"離れろーーーーー！！": "Stay back—!!",
"ほとんど魔法なしの、純粋な決闘になる。":
    "a pure duel, nearly without magic.",
"あなた、相当剣術に自信あるようだけれど…":
    "You seem quite confident in your swordsmanship...",
"…あたしもかなり得意なのよね、剣も鞭も。":
    "...I'm rather good too, with both sword and whip.",
"知っているさ。": "I know.",
"あんたは得物を使っても只者じゃない。":
    "Even armed, you're no ordinary fighter.",
"身のこなしを見れば分かる。": "I can tell from your movements.",
"フフフ…　そう。": "Heheh... is that so.",
"じゃあ始めましょうか…。": "Then let's begin...",
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
