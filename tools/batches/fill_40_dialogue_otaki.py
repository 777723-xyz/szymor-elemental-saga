#!/usr/bin/env python3
"""Fill batch 40: Seiryu inn, sendoff, Otaki's legend begins."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"では、どうぞごゆるりと…": "Then please, make yourself at ease...",
"長旅だったでしょう。": "It must have been a long journey.",
"お疲れでしたら、どうぞ私どもの宿を":
    "If you're weary, please avail yourself",
"ご利用ください。": "of our inn.",
"一泊料金、皆さま合計で５０Ｇになります。":
    "The nightly rate for all of you comes to 50G.",
"悪い、ありがとう、オジリ。": "Sorry, and thanks, Ojiri.",
"いいのいいの、あなたたちが頑張らなきゃ":
    "Don't mention it—if you all don't fight on,",
"世界は終わりなんだろう？": "the world will end, right?",
"あら、ナガレ！久し振り！": "Oh, Nagare! Long time no see!",
"お金なんかいらないよ！": "No need to pay!",
"皆さん、お疲れでしょう。": "You must all be tired.",
"どうぞ休んでかれてくださいな。":
    "Please, do take your rest.",
"もちろん、お代はいりませんよ！":
    "Of course, there's no charge!",
"あ！ダメだよこんなところまで入ったら！":
    "Ah! You can't come in this far!",
"でも、一応、お客さんいらっしゃい！":
    "But still, welcome in!",
"すまないな、苦労をかけてる…":
    "Sorry for all the trouble...",
"ナガレが謝る事じゃないだろー？":
    "This isn't something for you to apologize for, right?",
"大丈夫、草とかいっぱい生えてるだろう？":
    "It's fine—plenty of herbs grow around here, right?",
"レパートリー自体はたくさんあるんだ！":
    "I've got plenty of recipes!",
"さすがキエヤマだな！": "As expected of Kiyeyama!",
"もう少しの辛抱だから、しっかり頼んだ！":
    "It's just a little longer—stay strong!",
"うーん…　コメがたりないなあ…":
    "Hmm... we're short on rice...",
"どうやってやり繰りしよう…":
    "How am I going to make it work...",
"…って、ナガレ！？": "...Huh, Nagare!?",
"あんた、なにしてんの、こんなところで！？":
    "What are you doing in a place like this!?",
"あんた、もしかしてそうやって毎回":
    "Wait—is that how you've been",
"旅人に教えてあげてんのか…？":
    "helping travelers every time...?",
"そうだよ。嫌になるときもあるけど、":
    "Yeah. There are times it wears on me, but,",
"まあ、最近はそんなに忙しくないし…":
    "well, I haven't been that busy lately...",
"みんなあたしの知らないところで色々":
    "Everyone's been working so hard",
"働いてくれてるんだねえ。": "behind my back...",
"おう、来たか。オタキ様もシズク様も、":
    "Oh, you're here. Lady Otaki and Lady Shizuku",
"アンタらが来てからじゃないと話さない":
    "refuse to speak until you arrive,",
"らしくて、ナガレが死にかけてる…。":
    "and Nagare's about to die of curiosity...",
"お金　1500G　を手渡された！": "Handed 1500G!",
"現金の方が便利だと思ってさ。":
    "Figured cash would be more convenient.",
"うちの店…　ああ、村の北の方に":
    "Our shop... ah, in the north of the village",
"うちの一族の店があるから、":
    "our clan has a shop—",
"そこで必要なものをそろえてから行きなよ。":
    "stock up there before you head out.",
"話は聞いてたよ、あんたたち。":
    "I've heard about you lot.",
"トリカゼ、ありがとう、恩に着る！":
    "Torikaze, thanks, I owe you one!",
"何言ってんだ、助け合うのがセイリューだろ？":
    "What are you saying—helping each other is Seiryu's way, right?",
"それにあんたはセイリューの頭領だ！":
    "Besides, you're the leader of Seiryu!",
"堂々とあたしらを使ってくんな！":
    "Use us without a second thought!",
"旅立ちだろ？": "You're setting out, right?",
"頭領って、野盗みたいな呼び方だな！":
    "'Leader' makes it sound like bandits!",
"これはあたし…というかあたしら鍛冶屋の":
    "This is a going-away gift from me—",
"一族からの餞別だ。": "rather, from our blacksmith clan.",
"少しでも役立ててくれ。": "Put it to good use, even a little.",
"心配すんな！オレとウィンもいる。":
    "Don't worry! Me and Win are here too.",
"絶対に大丈夫だ！": "It'll definitely be fine!",
"ああ、信じてるぜ！": "Yeah, I believe you!",
"ナガレちゃん、必ず生きて帰ってこいよ":
    "Nagare, make sure you come back alive.",
"当たり前だろ。トリカゼらしくない弱気だな。":
    "Of course. That timidity isn't like you, Torikaze.",
"ハハ…　だな？": "Haha... right?",
"皆さんお待ちかねですよ。": "Everyone's been waiting.",
"特に…何も教えてもらえないまま放置されてる":
    "Especially Nagare, who's been left in the dark",
"ナガレがね…": "without being told anything...",
"遅いぞあんたら…": "You're late...",
"話してくれ、オタキ様。": "Please tell us, Lady Otaki.",
"うむ…": "Indeed...",
"ホノオどのとウィンどのも、":
    "Lord Hono and Lord Win,",
"どうぞお聞き下され…。": "please, do listen...",
"これは本来セイリュー当主のみに伝えられる":
    "This is a secret meant only for Seiryu's head,",
"秘密じゃが…　": "but...",
"闇のエレメントの復活がはじまったいま…":
    "with the Dark Element's revival now begun...",
"もう隠す必要はないとわしは判断しますじゃ":
    "I judge there's no longer a need to hide it.",
"お、おう…": "O-Oh...",
"秘密って…いったい…": "A secret... about what...",
"代々セイリュー当主に口伝でのみ伝わる、":
    "A legend of this land, Seiryu, passed down only by word of mouth",
"この地セイリューの伝説じゃ":
    "from head to head, for generations.",
"その昔、この地にひとびとが集い集落を作る前":
    "Long ago, before people gathered here to form a village,",
"この地は日夜大雨が降り続き、川は溢れ":
    "this land was battered by rain day and night; rivers overflowed,",
"木は腐り、とてもひとが住める地ではなかった":
    "trees rotted, and it was no place for people to live.",
"その地にはじまりの水の者が現れた":
    "And there, the First Being of Water appeared.",
"はじまりの、水の者？": "The First Being of Water?",
"なんだそれ？？聞いたことないぞ。":
    "What's that?? Never heard of it.",
"そんな伝説、フレイムでも聞いたことがねえ。":
    "Never heard such a legend in Flame either.",
"なんだなんだ、どうなるんだ！？":
    "What, what—how does it go!?",
"うるさい！": "Quiet!",
"あんたら話の腰を折るんじゃない！":
    "You lot, stop interrupting!",
"ただでさえ長くなるんじゃ！！":
    "This is already going to be long!!",
"すんません…": "Sorry...",
"はじまりの水の者はとても疲れていた":
    "The First Being of Water was utterly weary.",
"よういらっしゃった、火と風の紋章の継承者":
    "Welcome, inheritors of the Fire and Wind crests,",
"のかたがた…": "the both of you...",
"長い旅の末にこの地に迷い込み":
    "After a long journey, it wandered into this land",
"遂には動けなくなって、洞窟の中で身をよこたえた":
    "and, at last unable to move, lay down within a cave.",
"何度も眠り、何度も目を覚ましたが":
    "It slept and woke, again and again,",
"すさまじい雨は全くやむ気配がなかった":
    "yet the fierce rain showed no sign of stopping.",
"死ぬこともできず、かといって身体も動かず":
    "Unable to die, yet unable to move either,",
"やがてはじまりの水の者は":
    "at length, the First Being of Water",
"何か食べ物でもないかと":
    "set out into the depths of the pitch-black cave,",
"真っ暗闇の洞窟の奥へと": "searching for anything to eat,",
"歩き出したのじゃ": "it began to walk.",
"わしが先々代当主、オタキですじゃ":
    "I am Otaki, head two generations back.",
"ちょっと待ってこの話、": "Hold on, this story—",
"龍の話か？龍出てくる話っぽいな！":
    "is it about a dragon? Sounds like a dragon story!",
"そうなのか？りゅう？": "Is it? A dragon?",
"なんだなんだどうなるんだ？？": "What, what—how does it go??",
"だまらっしゃい！！": "Silence!!",
"ナガレも黙って聞きなさい！！":
    "You too, Nagare—listen quietly!!",
"長くなると言っておるじゃろ！！":
    "I told you this would be long!!",
"真っ暗闇の中をふらふらと":
    "Wandering through the pitch black,",
"歩いていると…": "it walked on...",
"突然足元の感覚が、地面がなくなった":
    "when suddenly the ground beneath its feet vanished.",
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
