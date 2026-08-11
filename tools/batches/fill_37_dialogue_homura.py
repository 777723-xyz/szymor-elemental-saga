#!/usr/bin/env python3
"""Fill batch 37: Flame hotel, Dragon's Tear, Hono's trial with Homura."""
import csv
import os
import re

D = {
"ハーイ　異国の方たちー！": "Hii, visitors from foreign lands!",
"お目覚めですかー？": "Aroused from your slumber?",
"ぜひぜひまたご宿泊くださいませー！":
    "Do please stay with us again!",
"おまえら金持ってないじゃん":
    "So you lot don't have any money, huh.",
"あなた方の為の高級ホテルへようこそ！":
    "Welcome to the luxury hotel prepared just for you!",
"なんだ　金持ちじゃないのか": "What, not rich after all?",
"そうですね、まだ日も高いですしねー！":
    "Right, the sun's still high too, isn't it!",
"またのお越しをお待ちしておりますよ！":
    "We await your next visit!",
"こんなに素敵なホテルが一泊200Ｇです！":
    "A wonderful hotel like this is just 200G a night!",
"勿論ご宿泊ですよね？": "You'll be staying, of course?",
"………なんだよこれ、うますぎだろ":
    "......What is this, it's way too good.",
"ここの飯うますぎだよ！！": "The food here is amazing!!",
"来年またお金貯めて来る！！":
    "I'll save up and come back next year!!",
"仕事で来たのだけれど…": "I came for work, but...",
"外は暑過ぎて、ちょっとここを出る気に":
    "it's so hot outside, I just can't bring myself",
"なれないんだよね…": "to leave here...",
"俺は任務中で忙しいんだ！": "I'm busy on a mission!",
"これも偵察！　カレーうめええええ！！！！":
    "This is reconnaissance too! And the curry is delicious—!!!!",
"もっと情報を集めないと！！！！！":
    "I need to gather more intel!!!!!",
"『龍の涙』": '"The Dragon\'s Tear"',
"その美しさは妖しいほどで、見る者を必ず魅了するという。":
    "Its beauty is bewitching, said to captivate all who see it.",
"しかし、話に聞くばかりで、現存するものは存在しない。":
    "Yet it exists only in tales; none remain in the world.",
"もしかするとそれには、その宝石にまつわる一種の伝説が":
    "Perhaps that is because of a certain legend",
"関係しているのかも知れない。": "surrounding the gem.",
"龍の涙には、握りしめて三日三晩祈ると愛する死者を":
    "It is said that if you grip a Dragon's Tear and pray for three days and nights,",
"蘇らせた後砕けるという言い伝えがあるのだ。これだけ有名":
    "it revives a beloved dead one, then shatters. So famous is this tale that its absence",
"なのに現存しないのは、発見されるたびに誰かが愛する者を":
    "from the world may be because, each time one is found, someone truly",
"実際に生き返らせているからかも知れない。": "brings a loved one back to life.",
"ここ数十年は発見されたことがないと思われるが、":
    "None seem to have been found in recent decades, but",
"昔のセイリューで稀に発掘されることがあったと伝わる、":
    "long ago, it's said, they were occasionally unearthed in Seiryu—",
"透き通った青い宝石、龍の涙。":
    "the translucent blue gem, the Dragon's Tear.",
"おお…なんと美しい…！": "Oh... how beautiful...!",
"これぞ本物の龍の涙に違いない…！！":
    "This must be a genuine Dragon's Tear...!!",
"お前さん、どうかその宝石を譲ってくれまいか":
    "You there, would you part with that gem?",
"わしの秘蔵する最も貴重な本…":
    "I'll trade my most precious hidden tome...",
"内容の危険さゆえ誰にも見せたことのないものだ":
    "one I've never shown anyone, for its dangerous contents.",
"ありがたい！では、これが例の奇書だ…":
    "Most grateful! Then this is the famed rare tome...",
"ウィンは奇書を手に入れた": "Win obtained the rare tome!",
"そ、そうか…": "I-...I see...",
"しかし、お前さんが必要なくとも、本の好きな":
    "But even if you've no use for it, any book lover",
"人間であれば絶対に欲しがるものだからな…":
    "would absolutely want it...",
"1000\\G 手に入れた！": "Gained 1000G!",
"シャムシール（良質）を手に入れた！":
    "Obtained a Shamshir (Fine)!",
"あいつの後ろとか言ってたな…":
    "He said something about behind him...",
"椅子がある…　あれに座るのかな。":
    "There's a chair... I guess I sit in it?",
"ウィン、って言ったよな。": "He said 'Win,' didn't he.",
"こんなことしている場合じゃないってことは、":
    "I know this isn't the time for, well, this.",
"分かってる。": "I get it.",
"だけどオレ、この試練をちゃんと…":
    "But I want to properly...",
"乗り越えたいんだ。": "overcome this trial.",
"もう少し付き合ってくれよ、頼む。":
    "Bear with me a little longer, please.",
"ちょっとおい！　待て！！": "Hey! Wait!!",
"恩に着るぜ！！": "I owe you one!!",
"とりあえず、あそこの椅子に座ってみるか…":
    "For now, let's try sitting in that chair...",
"そうか。": "I see.",
"でも俺は試練を済ますまでは、ここを":
    "But I'm not leaving this place",
"出る気はないぜ。": "until I finish the trial.",
"消えちゃったよ…": "He vanished...",
"…じゃあなに？": "...So what was that?",
"試練の…声みたいなこと…？":
    "Like... a voice of the trial...?",
"試練を受けよ　火の勇者よ…":
    "Undergo the trial, hero of Fire...",
"うわ！えっ？": "Whoa! Huh?",
"いまの、ウィン、お前の声か？":
    "That just now—Win, was that you?",
"ウィンは首を横に振った": "Win shook his head.",
"この椅子に座ると試練が始まるのかな…？":
    "Does the trial begin when I sit in this chair...?",
"さっきの鎧がすごく試練ぽかったけど…":
    "That armor earlier really seemed like the trial, but...",
"こっちが本物らしい…": "this seems to be the real thing...",
"何が起こるかわからないから、":
    "Since we don't know what'll happen,",
"ウィンはちょっと離れていてくれ。":
    "stand back a little, Win.",
"え…　そんな…　まさか…":
    "Huh... no way... it can't be...",
"振りむいてはいけない、ホノオ！":
    "Don't turn around, Hono!",
"振り向いたら、僕は消えてしまう…":
    "If you turn, I'll vanish...",
"マジかよ…　その声…　その声はよ…":
    "For real... that voice... that voice is...",
"アニキの…　ホムラ兄貴の声じゃねえか…":
    "it's big bro's... Homura's voice, isn't it...",
"なぜかウィンはまったく動けない！":
    "For some reason, Win can't move at all!",
"ホノオ、お前に会いたかった。": "Hono, I wanted to see you.",
"お前と話したいことが、たくさん残っていた…。":
    "There was so much I still wanted to tell you...",
"オレだってそうだよ…": "Me too...",
"だけどアニキ…アンタは死んだ。":
    "But big bro... you died.",
"試練てのは、死んだ人間と会うことなのか！？":
    "Is the trial about meeting the dead!?",
"そうみたいだ…。": "It seems so...",
"継承の試練で何が起こるのか、それは秘密。":
    "What happens in the trial is a secret.",
"だから真実を知るのは常に王のみ…。":
    "Which is why only the king ever knows the truth...",
"そうだな。": "Right.",
"…しかしアニキと話すことになるなんて、":
    "...But never in my wildest dreams did I think",
"さすがのオレでも全く想像してなかったぜ…":
    "I'd end up talking with you, big bro...",
"そうさ、ホノオにもわからないことは、":
    "That's right—what you don't understand, Hono,",
"僕にも、誰にだってきっとわからないのさ。":
    "I likely don't understand either, nor anyone.",
"…マジでアニキなのか？": "...Is it really you, big bro?",
"そうやって、わけのわからねえ褒め方すんの、":
    "Praising me in that baffling way—",
"マジでホムラ兄貴っぽいんだ…":
    "that's so like Homura...",
"マジでマジでってたくさん言うのも、ホノオらしいよ。":
    "Saying 'for real, for real' so much is just like you, Hono.",
"オレはずっとアニキみてえになりたいと":
    "I always wanted to become like you,",
"思ってた。": "big bro.",
"誰にでも優しくて…": "Kind to everyone...",
"難しい本をたくさん読んでいて…":
    "Reading all those difficult books...",
"誰もが立派だと褒めるアニキみてえに…":
    "Admired by all as a fine man, like you were...",
"だからアニキが死んでから大変だったんだ。":
    "So it was so hard after you died.",
"オレはたくさん本を読んでみた。": "I tried reading lots of books.",
"みんなに敬語使って話してみたりもした。":
    "I even tried speaking politely to everyone.",
"オレは…": "I...",
"誰よりも優しくて頭のいいアニキが…":
    "I was really looking forward to you—",
"この国の王になるのが、オレはマジで":
    "so kind and smart, more than anyone—",
"楽しみだったんだよ…": "becoming king of this country...",
"アニキの真似をし始めたオレを見て…":
    "When they saw me imitating you...",
"みんなは余計にがっかりした…。":
    "everyone was all the more disappointed...",
"いくら本を読んでも何も頭に入らねえし…":
    "No matter how much I read, nothing stuck in my head...",
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
