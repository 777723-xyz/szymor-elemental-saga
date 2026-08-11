#!/usr/bin/env python3
"""Fill batch 28: Raymond intro, Seiryu history, inn and family scenes."""
import csv
import os
import re

D = {
"彼と一緒にセイリューへ向かい、":
    "go with him to Seiryu,",
"どうした、ウィンよ、お前だけか。":
    "What's this, Win—you alone?",
"その頃にまだ闇のエレメントが":
    "I hope the Dark Element hasn't",
"復活していなければよいが…":
    "revived by then...",
"とにかく急ぐのだ。": "In any case, make haste.",
"ウィン、これを持っていけ。": "Win, take this with you.",
"ウィンは南の通行手形を受け取った！":
    "Win received the Southern Passage Permit!",
"それがあれば南の関所を越え、":
    "With it, you can pass the southern checkpoint",
"フレイムへと渡ることが出来る。":
    "and cross into Flame.",
"砂漠の魔物は手ごわいと聞く。":
    "The desert monsters are said to be formidable.",
"準備を怠るなよ。": "Don't neglect your preparations.",
"それともうひとつ…": "And one more thing...",
"フレイムまでの道のりを、": "On the road to Flame,",
"共にしてほしい者がいるのだ。":
    "there's someone I'd like you to take along.",
"レイモンド、参れ！": "Raymond, come forth!",
"ロイの説得は出来たのか…？":
    "Did you manage to persuade Roi...?",
"はっ、ここに！": "Sir, here!",
"ピピンはどうしている？": "How is Pipin?",
"この者は最近身体が鈍っているのでな。":
    "This one's body has grown sluggish lately.",
"走らせるために偵察兵にした。":
    "I made him a scout to keep him running.",
"この者の任地、フレイムまで共に向かってくれ。":
    "Travel with him to his post in Flame.",
"メシがうまいと評判のフレイム…":
    "Flame, famed for its good food...",
"楽しみです！！": "I can't wait!!",
"ウィンはこれまでの経緯を王に説明した":
    "Win explained everything that had happened to the king.",
"ホノオ王子…それはどうも…お疲れ様です。":
    "Prince Hono... thank you for your hard work.",
"我が城下町には自慢の宿屋があります。":
    "Our castle town boasts a proud inn.",
"是非ご利用くだされ…。": "Do make use of it...",
"もう少し待ってくれ、ウィンダムの王様！":
    "Hold on a moment, King of Windam!",
"こちとら毎日戦ってばかりでさあ…":
    "We've been fighting every single day...",
"クタクタなんだよなあ…": "we're exhausted...",
"ご武運をお祈りします。": "May fortune favor you.",
"おお、ホノオ王子！": "Oh, Prince Hono!",
"見事継承の試練を乗り越えられたとのこと、":
    "Having splendidly overcome the trial of succession,",
"お祝い申し上げますぞ。": "I offer you my congratulations.",
"ありがとよ、ウィンダムの王様！":
    "Thanks, King of Windam!",
"これでやっと本腰入れて勇者さまの":
    "Now I can finally get down to business",
"おしごとにとりかかれるぜ。": "as a proper hero!",
"おかえりー！": "Welcome back!",
"その顔…　珍しく難しい顔してどうした？":
    "That face... rarely do you look so troubled—what's wrong?",
"結構きつかったか…？": "Was it rough...?",
"…無事に戻ったみたいだな。安心した。":
    "...Looks like you made it back safe. I'm relieved.",
"『セイリューの歴史』": '"History of Seiryu"',
"かの地の特徴は、その豊かな自然と、何よりも住民たちの":
    "That land is marked by its rich nature and, above all, the skills",
"先祖から代々受け継いでいる、技術や知識の数々である。":
    "and knowledge its people have inherited from their ancestors.",
"かの地でしか栽培されないコメは、栄養があり美味で、":
    "The rice grown only there is nutritious and delicious, and",
"刀という剣の鋭さと頑強さは他の国に真似できない。":
    "the sharpness and strength of their katanas can't be matched elsewhere.",
"また、かの地には龍が住むという伝説があり、領民たちから":
    "A legend says a dragon dwells there, and the people",
"恐れられるのと同時に、愛されてもいる。":
    "both fear and love it.",
"おそらく水のエレメントを、龍という神獣にたとえて":
    "They likely worship the Water Element, likening it",
"信仰しているのだろう。": "to a divine beast: the dragon.",
"セイリューとは西の山奥にある国だが、国というよりも":
    "Seiryu is a nation deep in the western mountains, though in scale",
"その規模で考えると、集落に過ぎない。":
    "it's little more than a village.",
"昔から同じ領主のもとで、様々な農民、職人が、":
    "Since long ago, under the same lord, farmers and artisans",
"一種の宗教的な団結を持って支え合っている。":
    "have supported each other with a kind of religious unity.",
"あっ、いらっしゃい…": "Ah, welcome...",
"あの、忙しいんで…": "Um, I'm busy, so...",
"邪魔しないでもらえますか": "would you please not disturb me?",
"では明日の朝までごゆっくりご滞在下さいませ。":
    "Then please rest comfortably until tomorrow morning.",
"これはこれは騎士様。今日はどういったご用件でしょうか。":
    "Well, well, Sir Knight. What business brings you today?",
"おはようございます。": "Good morning.",
"おや？お手持ちのお金が料金に足りないようですね…。":
    "Oh? It seems you don't have enough money for the fee...",
"恐縮ですが、またの機会にご利用くださいませ。":
    "I'm sorry, but please avail yourself another time.",
"騎士様方の宿舎でなら無料で休めますが、":
    "At the knights' quarters you may rest free of charge, but",
"こちらでご宿泊なさると100Gの料金を頂くことになります。":
    "staying here will cost you 100G.",
"それでもよろしいですか？": "Is that still all right?",
"でも、絶対に無理をしたらいかんぞ！":
    "But never push yourself too hard, alright!",
"そういうときもあるだろう…。":
    "There are times like that...",
"どうだい、たまの休みには帰ってきて、":
    "How about coming home on your days off once in a while,",
"一緒にのんびり、夕食を食べようじゃないか！":
    "and having a relaxing dinner together!",
"おお、ウィン！よく来たな。": "Oh, Win! Good to see you.",
"仕事はうまくいっているかい？": "Is work going well?",
"そうかそうか！": "Is that so, is that so!",
"陛下や先輩の言うことをよく聞いて、":
    "Listen well to His Majesty and your seniors,",
"何でも素直に学ぶことだ。": "and learn everything with an open mind.",
"ああ、びっくりした…。": "Oh, you surprised me...",
"あんなにパンが嫌いだったのに…。":
    "He used to hate bread so much...",
"でも、お城のご飯ばかり食べていると、":
    "But after eating only castle food,",
"うちのパンが懐かしくなったでしょう？":
    "you must've gotten nostalgic for our bread?",
"いらっしゃい！…って、ウィンじゃないの！":
    "Welcome! ...Oh, if it isn't Win!",
"…うちのパンを買いに来たのかい！？":
    "...Did you come to buy our bread!?",
"またいつでもいらっしゃいよ、ウィン！":
    "Come by anytime, Win!",
"パパが今日もここのパンをお昼に食べたいから":
    "Dad says he wants this bread for lunch again today,",
"買ってこいって…": "so he sent me to buy some...",
"でも僕もこのお店のパン大好き！":
    "But I love this shop's bread too!",
"あと何回この店のパンを食べられるかのう…":
    "How many more times can I eat this shop's bread...",
"その前に歯がなくなってしもうたら…":
    "If I lose all my teeth first...",
"そうなるくらいなら死んだ方がマシじゃ！":
    "I'd rather die than let that happen!",
"あー、どうも…": "Ah, hello...",
"おつかれさまです…": "Good work today...",
"あー、いらっしゃいませ…": "Ah, welcome...",
"お買い物なさいますか…？": "Will you be shopping...?",
"どうにもこの店は辛気臭いねえ…":
    "This shop is dreary no matter what...",
"品揃えがこれじゃあ、客も来ないだろう":
    "With stock like this, no wonder customers don't come,",
"がねえ…　そもそも店主があれだもの…":
    "and besides, the owner is... well, you know...",
"おい！ウィンが困ってるだろう！":
    "Hey! You're making Win uncomfortable!",
"そいつはもう子供じゃないんだ！":
    "He's not a child anymore!",
"あらあら、そうだったねえ。": "Oh dear, that's right.",
"騎士様になったんだものねえ！":
    "He's a knight now, after all!",
"んー？": "Hm?",
"でも、ウィン。": "But, Win.",
"お休みのときにでも、気が向いたらいつでも":
    "Whenever you're off duty and feel like it,",
"遊びに来るんだよ？": "come visit, alright?",
"あら、ウィンじゃないか！": "Oh, if it isn't Win!",
"珍しいねえ。": "What a rare sight.",
"よかったら、一緒にご飯食べていくかい？":
    "Care to stay for a meal together?",
"遠慮しないでいいんだよ！": "Don't be shy!",
"おお、ウィン…よく来たな。": "Oh, Win... good of you to come.",
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
