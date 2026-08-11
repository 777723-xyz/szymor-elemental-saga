#!/usr/bin/env python3
"""Fill batch 27: Windam misc scenes, king's orders."""
import csv
import os
import re

D = {
"騎士ウィン殿に敬礼！": "Salute to Sir Knight Win!",
"まだ若いのに何て立派な敬礼だろう…":
    "Such a fine salute for one so young...",
"ウィン、今度俺に教えてくれ！": "Win, teach me it sometime!",
"おう、ありがとよ！": "Oh, thanks!",
"とは言えずっとここに立っていると飽きるよ。":
    "Still, standing here all day gets boring.",
"外に出られるお前が羨ましいや。":
    "I envy you, getting to go outside.",
"お勤めごくろう！騎士ウィン殿！":
    "Good work out there, Sir Knight Win!",
"ハハハ！相変わらず素直なやつだなあ。":
    "Hahaha! As straightforward as ever.",
"騎士殿、ご武運を祈るぜ！":
    "Sir Knight, may fortune be with you!",
"孫の顔を見せに娘がフレイムから来てくれて":
    "My daughter came all the way from Flame to show me",
"いるのじゃが、関所を通れず立ち往生している":
    "her child, but she's stuck at the checkpoint",
"そうなんじゃ…。何とかならんかのう…。":
    "and can't get through... Isn't there anything to be done...",
"うちの店の雨漏りを直してくれるって話を":
    "It's been two weeks since the minister said he'd",
"してから、もう二週間が経つんだよ。":
    "fix the leak in my shop.",
"大臣は本当に覚えているのかねえ？":
    "Does the minister even remember, I wonder?",
"ここに魚がいるの知ってたか？": "Did you know there are fish here?",
"知らないだろう。": "You didn't, did you.",
"この前の休暇で釣った魚をここに放したら":
    "I released the fish I caught on my last holiday here,",
"増えちゃったんだ。内緒だぞ？":
    "and they multiplied. Keep it secret, alright?",
"おっ、ウィンじゃないか？": "Oh, if it isn't Win?",
"知ってるよ。お前外で仕事だろ？":
    "I know. You're out on duty, right?",
"それより、この前誘った釣りの件なんだが、":
    "Anyway, about the fishing trip I mentioned,",
"考えておいてくれよな。楽しいぞ！":
    "keep it in mind, alright? It's fun!",
"お前も休憩か？": "Taking a break too?",
"…なんの休憩だよ？": "...What break?",
"俺は魚にエサやってんの。": "I'm feeding the fish.",
"ウィンは　ダガー（良質）　を受け取った！":
    "Win received a Dagger (Fine)!",
"ウィンは　マンゴーシュ　を受け取った！":
    "Win received a Main Gauche!",
"騎士様のおかげで血をみなくて済みました。":
    "Thanks to you, Sir Knight, no blood had to be shed.",
"おじいちゃんたら　": "Grandpa says",
"わたしをママのちいさいころに":
    "I look just like Mommy did",
"そっくりだって言うんだよー": "when she was little!",
"この度は本当にありがとうございました…":
    "Thank you so much for everything...",
"こうして父に娘を会わせることもできました！":
    "Thanks to you, a daughter could meet her father!",
"通行手形をお返ししますね。":
    "I'll return your permit now.",
"ウィンは通行手形を返してもらった！":
    "Win got his permit back!",
"しかし親父いつまで娘とあそんでるんだよ…":
    "But Dad, how long are you gonna play with your daughter...",
"ちょっとばかし、臭いけどな。":
    "It stinks a little, though.",
"いいねえ　若いってのは。": "Ah, youth is a wonderful thing.",
"でも、無理すんなよ。そこのベッドなら、":
    "But don't push yourself. That bed over there—",
"いつでも使って大丈夫だからな？":
    "you can use it anytime, alright?",
"ふいーつかれたーーー": "Phew, I'm beat~",
"お、ウィン、お前も疲れたのか？":
    "Oh, Win, tired too?",
"それなら隣のベッドで休んで行けよ。":
    "Then rest in the next bed over.",
"宿屋と違って、タダだぜ。": "It's free, unlike an inn.",
"ちょっと、騎士さん、どいてちょうだい！":
    "Excuse me, Sir Knight, move aside!",
"ふんづけちゃうから！": "I'll step on you!",
"あーいそがしいいそがしい　って、":
    "Ah, so busy so busy—hey,",
"俺なんで手伝わされてるの？": "why am I helping out here?",
"おいおい、いいのかそれで？": "Hey now, is that alright?",
"たくさん本を読むと、この世界での暮らしが、":
    "If you read lots of books, life in this world",
"さらに、もっと豊かになると思うぞー":
    "will become all the richer, I tell you~",
"お前、本棚とかちゃんと調べているか？":
    "Hey, are you properly checking the bookshelves?",
"世の中いろいろな本があって面白いよなー":
    "There are all kinds of books out there—interesting, huh?",
"俺も本棚を見つけると、しごとサボって":
    "When I spot a bookshelf, I end up slacking off",
"ついつい読んじまうんだよー": "and reading it, you know~",
"吾輩は現在王国の財政の記録をつけているの":
    "I am currently keeping the kingdom's financial records,",
"であーる！": "yessir!",
"食事の時間までにテーブルを整えないと":
    "I must set the tables before mealtime,",
"いけないんです…話し掛けないで下さい！":
    "so please don't talk to me!",
"異常なーしっ　って、当たり前だっての。":
    "No anomalies... well, of course not.",
"おいウィン！これが兵卒のしごとなのか！":
    "Hey Win! Is this what a soldier's job is!",
"つらすぎるー": "It's too harsh~",
"ちゃんと売ってますか？": "Are you selling properly?",
"うん、よかったのう！": "Mm, good to hear!",
"なんだ…体の具合でも悪いのか？":
    "What's wrong... feeling unwell?",
"何か思いつめていたり…？": "Something weighing on your mind...?",
"あ、いや！": "Ah, no!",
"別に心配しているわけではないぞ！":
    "It's not like I'm worried about you!",
"…ウィン。ロイに会ったか？": "...Win. Did you meet Roi?",
"気にするな！": "Never mind!",
"やつは…元気そうだったか？":
    "Did he... seem well?",
"そ、それならよかった！": "Th-Then that's good!",
"…ウィン、": "...Win,",
"お主は風の紋章の継承者となった。":
    "you have become the inheritor of the Wind Crest.",
"ということは当然、次の騎士団長はおぬし。":
    "Which naturally makes you the next Knight Commander.",
"おぬしのような新米には…重責じゃ。":
    "A heavy burden for a rookie like you...",
"気負い過ぎることなく、いつでも王やわし…":
    "Don't overstrain yourself—lean on the king, on me...",
"そしてロイを頼るのだぞ？":
    "and on Roi whenever you need.",
"50Gを見つけた！　が…": "Found 50G! But...",
"泥棒になるので元に戻した": "being a thief isn't right, so I put it back.",
"サクソン騎士団長代行のお弁当があったが…":
    "There was Acting Commander Saxon's bento, but...",
"ウィンは黙って　もとに戻した":
    "Win silently put it back.",
"下痢止めの薬を見つけたが…":
    "Found some diarrhea medicine, but...",
"黙ってもとに戻した": "silently put it back.",
"俺、ちょっとあいつ苦手だし…":
    "I just can't deal with that guy...",
"わからないってお前…": "Come on, you know...",
"何かあったのか？": "Did something happen?",
"あっ、俺の相手はいい！陛下が待ってるぞ！":
    "Ah, don't mind me! His Majesty's waiting!",
"あっ、ウィンおかえり！": "Ah, Win, welcome back!",
"…ピピンはどうしたんだよ？": "...Where's Pipin?",
"そうなのか…？": "Is that so...?",
"まあいっか…": "Ah well...",
"…分かった。": "...Understood.",
"ウィンよ…紋章の継承者としての責務、":
    "Win... see that you fulfill your duty",
"見事果たしてみせよ。": "as the crest's inheritor.",
"闇のエレメントが復活するのであれば、":
    "If the Dark Element is to revive,",
"我々も急ぎ準備が必要だ。": "we too must prepare in haste.",
"兵はサクソンにまとめさせ、城壁、そして":
    "Have Saxon rally the soldiers; the walls, and",
"ん？": "Hm?",
"街の防備を固めねばなるまい…":
    "the town's defenses must be reinforced...",
"ウィン、お前は早速南のフレイム王国に向かい、":
    "Win, head at once to the Flame Kingdom in the south",
"闇のエレメントの復活をフレイム王に告げよ。":
    "and tell King Flame of the Dark Element's revival.",
"そして火の紋章の継承者…": "Then, the Fire Crest's inheritor...",
"おそらく王子のホノオ殿がそうだ…":
    "likely Prince Hono...",
"彼と一緒にセイリューに向かい、":
    "go with him to Seiryu,",
"水の紋章の継承者とも会うのだ。":
    "and meet the Water Crest's inheritor as well.",
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
