#!/usr/bin/env python3
"""Fill batch 39: ink-crest reveal, Nagare's crisis, Shizuku/Otaki backstory."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"…オレにだけよーーーー！！！":
    "...and only to me—!!!",
"あんたの紋章…　なんか違うくねえか？":
    "your crest... something's off, isn't it?",
"は？": "Huh?",
"そうだよ。毎朝墨入れするのが、継承者の":
    "Right. Retracing the ink every morning is",
"役目だからな。": "the inheritor's duty.",
"……え？": "......Huh?",
"ふーっ…": "Phew...",
"いやいやいやいやいやいやいやいや…":
    "No no no no no no no no...",
"いやいやいやいやいやいや…　は？？":
    "No no no no no no... Huh??",
"紋章は書いたり消えたりとかじゃないから！":
    "Crests aren't drawn and erased like that!",
"こいつで終りみたいだな。": "Looks like this is it for her.",
"勝手に刻まれて、消えないから！！":
    "They get etched on their own and never fade!!",
"何かもう、バシッてなるから！！":
    "They just go 'zing' and appear!!",
"え…　なに？　何を言っているんだあんた…":
    "Huh... what? What are you saying...",
"だってあたしが継承者で…紋章が…":
    "But I'm the inheritor... and the crest...",
"わかったわかった！": "Alright, alright!",
"じゃあオレとウィンの紋章こすってみろ！":
    "Then try rubbing mine and Win's crests!",
"そんな馬鹿な…": "That's absurd...",
"ナガレはウィンとホノオの紋章をこすった！":
    "Nagare rubbed the crests on Win and Hono!",
"そんな馬鹿な………": "That's absurd......",
"いたいいたい…　もうわかったろ…":
    "Ow, ow... see, got it now...",
"消えない…　消えないぞ…": "It won't fade... it won't fade...",
"消えない…！消えない！！そんな……！！":
    "It won't fade...! It won't!! How......!!",
"いたいいたい！！！いたいってのーーー！！！":
    "Ow ow!!! I said it hurts—!!!",
"消えない！！真っ赤になっても消えない…！":
    "It won't fade!! Even all red, it won't fade...!",
"まっかっかになるまでこするんじゃねえ！！":
    "Don't rub it until it turns beet red!!",
"いやー、久々に見たナガレちゃんの刀さばき、":
    "Man, Nagare's swordsmanship, which I haven't seen in ages—",
"………どういうことだ？": ".........What does this mean?",
"あたしの紋章はこいつらのと違う…？":
    "My crest is different from theirs...?",
"じゃあおまえ、その紋章、ちゃんと光るか？":
    "Then hey—does your crest even glow?",
"魔法は使えるのか？": "Can you use magic?",
"光る…って？": "Glow... what do you mean?",
"ていうか、ま、まほう……？": "And... m-magic......?",
"惚れ惚れするねえ。": "Simply captivating.",
"…な？": "...See?",
"光った…　めちゃくちゃ光った……":
    "It glowed... it blazed up......",
"そう、光るし…": "See, they glow...",
"オレは魔法で爆発起こせるし、ウィンは何か":
    "I can set off explosions with magic, and Win can",
"体中風をまとって超速くなったりできるぞ。":
    "wrap himself in wind and move at super speed.",
"ぼくの剣も敵にちゃんと効いてよかった…":
    "I'm glad my sword actually worked on the enemy...",
"お前の剣だって相当のもんだぞ。":
    "Your swordplay is quite something too.",
"ナガレとばかり比べているから、":
    "It's just that you're always comparing yourself",
"自分じゃ分からないんだろうけどさ。":
    "to Nagare, so you can't see it.",
"ああっ！そういえば……": "Ah! Speaking of which...",
"ああ、よそもんさん、待たせたね。":
    "Ah, sorry to keep you outsiders waiting.",
"もう片付いたよ。": "It's all taken care of.",
"おう、あんたらの剣術すげえな！":
    "Whoa, your swordsmanship is incredible!",
"見惚れちまったぜ…": "I was spellbound...",
"セイリューの剣を見たのは初めてかい？":
    "First time seeing Seiryu swordsmanship?",
"あんたらの太刀筋が全然見えなかったぜ…。":
    "I couldn't even see your blade strokes...",
"…そっちの金髪の方は、そうでもなかった":
    "...Though the blond one over there wasn't quite",
"みたいだけど…　": "up to that standard...",
"へ？": "Huh?",
"マジか、ウィン…？": "For real, Win...?",
"自己紹介が遅れたな。": "I'm late with introductions.",
"あたしはセイリュー当主のナガレだ。":
    "I'm Nagare, head of Seiryu.",
"なっ、あんたが！？": "Wh—You're...!?",
"なんだよ？": "What?",
"見えないってかい？": "You couldn't see it?",
"ハハハ！": "Hahaha!",
"ナガレのお行儀が悪いからだねえ。":
    "That's Nagare's bad manners for you.",
"うるせえぞ、おまえら！": "Shut up, you lot!",
"いや、あんたが当主なら話が早い！":
    "No, if you're the head, then things are simple!",
"ナガレ大丈夫！？": "Nagare, are you okay!?",
"あああああああーーーーーーーーーーー！！！":
    "Aaaaaah—!!!",
"お、おい…　大丈夫かそれ…？":
    "H-Hey... is she gonna be okay...?",
"おまえ！ナガレをそれとか言うな！！":
    "You! Don't call her 'that'!!",
"いや、でも…": "No, but...",
"水の紋章がないと闇のエレメントの復活阻止":
    "Without the Water Crest, stopping the Dark Element's revival",
"あーーーーーーーーーーーーーっ！！":
    "Aaaah—!!",
"できないから、ヤバいんじゃねえか…？":
    "is impossible, so aren't we in trouble...?",
"でも…　もしかしたらシズク様やオタキ様が":
    "But... maybe Lady Shizuku or Lady Otaki",
"何か知っているんじゃないかな…": "knows something...",
"あ、そうかも…": "Ah, maybe...",
"そのしずく…？様と、お…たき？様ってのは？":
    "This Lady Shi...zuku? and La...dy Otaki?",
"オタキ様は先々代当主、シズク様は先代当主で、":
    "Lady Otaki is the head two generations back, and Lady Shizuku the previous one—",
"ナガレのお姉さまになります。":
    "they're Nagare's elder sisters.",
"オタキ様がご高齢の為、長女のシズク様に":
    "With Lady Otaki aging, the crest passed to eldest daughter",
"継承したのですが、そのシズク様もご病気で…":
    "Lady Shizuku, but she too fell ill...",
"それでナガレが、この若さで継承することに":
    "And so Nagare, at this young age, came to",
"なったんです。": "succeed her.",
"もともと身体の弱かったシズク様をナガレは":
    "Nagare worried terribly about Lady Shizuku,",
"すごく心配していたから、": "who had always been frail,",
"自分が継承者になって喜んでいたのに…":
    "and was so glad to become the inheritor...",
"かわいそうなナガレ…": "Poor Nagare...",
"ふーん…　": "Hmm...",
"じゃあ、もしかしたら本当の継承者は、":
    "Then maybe the real inheritor is",
"そっちの二人のどっちかなのかもな…":
    "one of you two...",
"ちがーーーーーーーーーう！！！！！！":
    "That's wr—!!!!!!",
"継承者はあたしだ！！！！": "I'm the inheritor!!!!",
"あああああーーーーーーーーー！！！":
    "Aaaaaah—!!!",
"ナガレ、大丈夫だよ。": "Nagare, it's okay.",
"まだ君が偽物だと決まったわけじゃない。":
    "It's not yet decided that you're a fake.",
"ナガレ！？": "Nagare!?",
"とりあえず家に帰ろう、ナガレ。":
    "For now, let's go home, Nagare.",
"シズク様たちに聞いてみれば何かわかるさ！":
    "Ask Lady Shizuku and the others—they'll know something!",
"と、いうわけで…": "And so...",
"ぼくらはナガレを彼女の家に運びます。":
    "we'll carry Nagare to her home.",
"あなたたちも後で来てください。":
    "Please come along afterwards.",
"彼女たちセイリュー当主の家は、":
    "The Seiryu head's house is",
"この先すぐの橋を右に渡ったところです。":
    "just past the bridge ahead—turn right after crossing.",
"目立つ家なので、すぐわかると思います。":
    "It's a conspicuous house, so you'll spot it at once.",
"おう、わかった！": "Oh, got it!",
"なんか色々と、すまなかった…":
    "Sorry about all the trouble...",
"上流土砂崩れのため通行禁止中":
    "Passage closed due to landslide upstream.",
"はい、確かに50Gいただきました。":
    "Yes, I've received the 50G.",
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
