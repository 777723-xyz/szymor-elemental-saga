#!/usr/bin/env python3
"""Fill batch 57: Dafill's defeat, Generals' farewell."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"気合いがハンパなーーーーーい！！！！":
    "The energy's off the charts—!!!!",
"そんでそんでーーー": "And then, and then~",
"闇インフルエンザでみんなが死んじゃうのを":
    "I've gotta stop everyone from dying",
"防がないとだからーーー": "of the Dark Flu~",
"コレ正解だわー！！": "That's it, right!!",
"絶対に正解だとは思うんだけどーーーー":
    "I'm sure it's right, but~",
"一応確認しまーーーーーーす！！":
    "let me just confirm~!!",
"正解ですかーーーー？？？？？": "Is it right??",
"だはははははははは！！！！": "Bahahahaha!!!",
"やったーーーーーーだーいせーいかーい！！":
    "Yay, correct!!",
"そういうことだったらー…": "If that's how it is...",
"えーーー？　ホントにいいのーーー？？":
    "Ehh—? You're really okay with it??",
"大変ホントに申し訳ないんですけどーーー…":
    "I'm terribly, terribly sorry, but~...",
"オマエ…　チョーマヌケだよーーん！！！！":
    "You... are a total moron—!!!!",
"このパワーをボクがぜーんぶもらっちゃって！！":
    "I'm taking all this power for myself!!",
"…チッ！　なんだよー　来ちゃったじゃないかー":
    "...Tch! Oh great, they just had to show up.",
"アイツら…　意外と使えない奴らだったのねー":
    "Those guys... turned out to be useless after all~",
"…って、え？": "...Wait, huh?",
"ハ？　もしかして、キミひとりなの…？？":
    "Hah? Could it be... you're alone...??",
"ハァ…！！？？？？？": "Hah...!!?????",
"なになになになにー？？": "What what what what—??",
"えっ、どしたのんマジで！？": "Huh, what's wrong, for real!?",
"だははは！　キミひとり！！": "Bahaha! Just you alone!!",
"他のコはやられちゃったんだー！？":
    "The others got taken out!?",
"かわいそーーーーー！！": "How sad!!",
"えっ、じゃあ何？　ひとりでボクを倒しに？？":
    "Wait, so what? You came to beat me alone??",
"だははは！！": "Bahaha!!",
"ウィンは武器を構えた！": "Win readied his weapon!",
"いやいやムリだから！！": "No no, impossible!!",
"ひとりっていくら何でも…　プププー！！":
    "One person, no matter how—... pfft!!",
"しかもキミ、風の紋章のコじゃん…":
    "Besides, you're the Wind Crest one...",
"前に会ったコじゃん…": "the one I met before...",
"ボクの火の魔法も防げないじゃーーん！！":
    "you can't even block my fire magic—!!",
"マジで何しに来たの？": "Why did you even come?",
"理解に苦しむっていうか、いみふすぎーー！！":
    "I can't wrap my head around it—it makes no sense!!",
"ダフィ－－－ルッ…ファイアーーッ！！！！":
    "Dafiii—l... Fire—!!!!",
"バクハツ！！": "Explosion!!",
"堕天の炎に焼かれて…": "Burned by the Fallen Flame...",
"一瞬でホネになれ…": "become bones in an instant...",
"行くぞ、ウィン！！": "Let's go, Win!!",
"一気に行くぞ、ウィン！！": "Let's go all out, Win!!",
"も、申し上げます！！": "I-If I may report!!",
"暗黒大陸に…また光の柱が立ちました…！！":
    "A Pillar of Light... has risen over the Dark Continent again...!!",
"…なに！？": "...What!?",
"…ウィン…！！": "...Win...!!",
"陛下…！！": "Your Majesty...!!",
"お休み中失礼いたします…！":
    "Forgive me for disturbing your rest...!",
"光の柱が…": "The Pillar of Light...",
"ふたたび光の柱が観測されたとのことです！！":
    "Another Pillar of Light has been observed!!",
"おお…　あの地で一体何が起こっているのか…":
    "Oh... what in the world is happening on that land...",
"ホノオ…　無事でいてくれ…！":
    "Hono... please be safe...!",
"…ああ…　龍よ、お守りください…！":
    "...Ah... Dragon, please watch over them...!",
"ナガレーーーーーッ！！！！": "Nagare—!!!!",
"光の…柱だ…！！": "The Pillar... of Light...!!",
"…お前の負けだな、ダフィール。":
    "...You lose, Dafill.",
"愚かなことを…！！": "How foolish...!!",
"何っ…　四天王が…！？": "What... The Four Generals...!?",
"安心なさい、あたしらはもう消えるわ…":
    "Fear not, we will soon vanish...",
"そうねえ…　今回は千年くらいかしら？":
    "Indeed... a thousand years this time, perhaps?",
"ダフィ夫君が完全に闇のエレメントパワーと":
    "Because Lord Dafill never fully merged with",
"一体にならなかったことで………":
    "the Dark Elemental Power......",
"我々もまた、一体にはなれなかった…":
    "we too could not fully merge...",
"そしてまた、散り散りに飛び散って…":
    "And so we scatter once more...",
"またまた復活まで長い封印状態に陥る…":
    "and fall into a long, long sealed slumber until we revive again...",
"………なら、俺たちの勝ちってことで、":
    ".........Then that means we win,",
"いいんだな、四天王！！": "right, Four Generals!!",
"そうなるわ…": "It would seem so...",
"ダフィールがここまで自分を失うことを":
    "We never knew Dafill hated losing himself",
"嫌がっていると知らなかった……":
    "this much......",
"それがあたしたちの敗因かしら…":
    "Perhaps that was our undoing...",
"そう…だなあ。": "Yeah... I suppose.",
"あんたらは、またしばらくしたら復活する…":
    "You lot will revive again after a while...",
"しかし、こいつ…": "But this one...",
"ダフィールはどうなんだ…？": "what about Dafill...?",
"さあ…　大丈夫じゃないかしら。":
    "Who knows... he should be fine.",
"あたしたちを自分から追い出すほどに…":
    "He loves himself so much that he expelled",
"自分大好きちゃんなんだから…":
    "us of his own accord...",
"いやーーーー！？": "Naaaah!?",
"もしかしたら千年後には、ダフィ夫君こそが":
    "Who knows—a thousand years from now, Lord Dafill might well be",
"最強の四天王になっているかも知れんぞー！？":
    "the strongest of the Four Generals—!?",
"私とは全く違うな、このコは。":
    "This one's completely different from me.",
"こんな素直でまっすぐなコでも、":
    "I never knew someone so honest and straightforward",
"四天王やれるなんて知らなかったなあ！！":
    "could be a Four General!!",
"ピケピケ、あなたかなり薄くなってるわよ？":
    "Pikepike, you're getting pretty faint, you know?",
"千年後までもつの、それ…？":
    "Will that last a thousand years...?",
"ああ…　じゃあさすがに今回で卒業かも知れんなあ…":
    "Ah... then this is probably my graduation...",
"残念だけど、どのみち今回最後のつもりでいたし…":
    "A shame, but I was planning this to be my last anyway...",
"仕方ないなあ。": "Nothing to be done.",
"…そのようね。": "...So it seems.",
"なんか透けてるって段階も過ぎちゃってるし…":
    "You're well past the 'see-through' stage now...",
"おい、あんたらのコトはどうでもいい。":
    "Hey, I don't care about you lot.",
"…闇インフルエンザとかいう病気は？":
    "...What about that Dark Flu disease?",
"この大陸の人間は、いまどうなっている？":
    "What's become of the people on this continent?",
"集めた闇のエレメントパワーは飛び散って、また薄れた！！":
    "The gathered Dark Elemental Power has scattered and thinned again!!",
"ゆえに、闇の瘴気も薄まって、広がって、飛び散る！！":
    "Thus, the Dark miasma too thins, spreads, and scatters!!",
"お…らく、何…問題…ない…！":
    "P-Probably... no... problem...!",
"キミ…ちは助かった……よ！　おめ……う！…！…":
    "You... lot are... safe...... cong...ratulations...!...",
"声も、あまり聞こえなくなって来ている…":
    "I can barely hear his voice now...",
"分かりやすい死んで行き方だな…":
    "What an obvious way to go...",
"あんたらこそ、急ぎなさいよ。":
    "You lot should hurry yourselves.",
"闇のエレメントパワーは急速に弱まってる。":
    "The Dark Elemental Power is weakening fast.",
"つまり、紋章の力もどんどん弱まってる。":
    "Which means the crest's power is weakening too.",
"あのナガレとかいうサムライと…":
    "That samurai, Nagare, and...",
"火の紋章の継承者だった子…":
    "the one who was the Fire Crest inheritor...",
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
