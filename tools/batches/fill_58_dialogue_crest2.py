#!/usr/bin/env python3
"""Fill batch 58: crest custody dilemma, reunion, credits."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"ゆえに、闇の瘴気も薄まって、広がって、飛び散る！！":
    "Thus, the Dark miasma too thins, spreads, and scatters!!",
"いまなら助けられるわ。": "We can still save them now.",
"…本当か！？": "...Really!?",
"本………！…　…々の魔力…元は……レメ…トパワー…":
    "Our........ magic... comes from... Elemental Power...",
"…れ…弱ま…ば、…々の残し……法…効果も消…る…":
    "...if it... weakens... our... remaining... spells... fade...",
"…他の奴が説明してくれないか？":
    "...Would someone else explain?",
"我々の魔法…　元は闇のエレメントパワー…":
    "Our magic... is rooted in Dark Elemental Power...",
"闇弱まれば…　我々の魔法の効果も消えるのだ":
    "If the Dark weakens... our spells' effects vanish too.",
"あ、あんたが説明してくれるとは思わなかったが…":
    "H-Honestly didn't expect you to explain it...",
"とにかく分かった…": "Anyway, understood...",
"そんなに透けてる…！！！？？？":
    "You're that see-through...!!!???",
"ウィン、いくぞ！！": "Win, let's go!!",
"ウィンは頷いた！！": "Win nodded!!",
"そのままにしておけ…　オススメできないよ…":
    "Leave it be... I wouldn't recommend it...",
"何が起こるか…　わたしにもわからん…":
    "What might happen... I don't know either...",
"アドバイスはしたからな…？":
    "I've given you my advice, alright...?",
"後で文句言われても…知らないよーーーーーん":
    "If you complain later... I'm not responsible~",
"あっちゃー…　だから言ったのにいいいい…":
    "Ah, geez... I told you so~",
"黒いイモ虫のようなものがはみ出ている…":
    "Something like a black caterpillar is sticking out...",
"えーと…　それはちょっと面白そうだなあ":
    "Hmm... that does look a bit interesting.",
"いや！　でもオススメはできないぞ！！　キケンだ！！":
    "No! But I can't recommend it!! It's dangerous!!",
"忠告はしたぞ　最低限の親切はしたからな？":
    "I warned you—I did my due kindness, right?",
"おそらく伝説のバトルが待っている事だろう…":
    "A legendary battle surely awaits...",
"どっちが勝つんだろう…　ちょっと楽しみ…":
    "I wonder who'll win... rather excited...",
"それではいってらっしゃーーーーーーい！！":
    "Well then, off you go—!!",
"えーと…　まだやってるの…？":
    "Um... you're still going...?",
"さすがにもう何も用意してないんだけど…":
    "I really have nothing left prepared...",
"ではでは伝説のバトルへどうぞ…":
    "Then off to the legendary battle...",
"もうよくない？": "That's enough, right?",
"ナウーは小さく頷いた": "Nau nodded slightly.",
"ウィンも小さく頷いた": "Win nodded slightly too.",
"…さようなら、ウィン君、ピピン君！！":
    "...Farewell, Win, and Pipin!!",
"制作・開発　　ＷＧＴ": "Production & Development: WGT",
"なんだか、また会える気がする…":
    "Somehow, I feel we'll meet again...",
"だからさよならは言わないわ。":
    "So I won't say goodbye.",
"さあ、早く行きなさいよ？": "Now, hurry along, alright?",
"…早く行きなさいよ、何してるの？":
    "...Hurry along now, what are you doing?",
"心配しなくてもあたしたちは直ぐに消えるわ。":
    "Don't worry—we'll vanish soon enough.",
"次に復活するときに、": "When we next revive,",
"あなたたちはもういないけれど…":
    "you'll no longer be around, but...",
"もう進むしかないとウィンは思った":
    "Win thought there was nothing to do but press on.",
"シナリオライター　西園寺ハムカツ":
    "Scenario Writer: Saionji Hamkatsu",
"おお！！　全員生きて帰ったのか…！！":
    "Oh!! You all made it back alive...!!",
"なんとめでたいのだあああああああああ！！！":
    "How wonderful—!!!",
"よう、サクソンのおっさん！！":
    "Yo, old man Saxon!!",
"橋の守り、ご苦労様だったぜー！！":
    "Good work guarding the bridge!!",
"良かった、ここのみんなも無事みたいだな。":
    "Glad to see everyone here's safe too.",
"クッ………": "Hmph.........",
"じゃあ、そこのピンクのやムラサキの…":
    "So, the pink one and the purple one there...",
"あたしのこと言ってんのかい？":
    "You talking about me?",
"ふざけんな、あたしは鍛冶屋の娘だよ！":
    "Don't mess with me—I'm a blacksmith's daughter!",
"セイリューでは当主の一族しか継承しては":
    "In Seiryu, only the head's family may inherit,",
"いけない決まりです。ピピンさんの場合は":
    "that's the rule. In Pipin's case, it's an",
"非常時ですから仕方ないとしても…":
    "emergency, so it can't be helped, but...",
"次の継承者となるとやはり…":
    "for the next inheritor, well...",
"ナガレの子どもになりますかねえ…。":
    "it would have to be Nagare's child...",
"じゃ、じゃあナガレ、早く子どもを作れ…":
    "Th-Then Nagare, hurry up and have a child...",
"一刻も早くこの紋章を…": "so we can pass this crest on as soon as possible...",
"よう…帰った…　よう帰ったな、ナガレ！":
    "Well... welcome back... welcome home, Nagare!",
"バカ！　まだ相手もいないってのに、":
    "Idiot! I don't even have a partner yet—",
"どうやって作るんだよ！？": "how am I supposed to have a child!?",
"まあ、しばらくはあんたが持っていてくれ。":
    "Well, just hold onto it for a while.",
"その間、こっちでも色々考えてみるからさ！":
    "We'll think of something on our end in the meantime!",
"水の紋章…いましばらくお預け致しますぞ、":
    "The Water Crest... I entrust it to you for now,",
"ピピン殿！！": "Lord Pipin!!",
"クッ………！！": "Hmph.........!!",
"ゲームデザイン　西園寺ハムカツ":
    "Game Design: Saionji Hamkatsu",
"おかえりなさい！": "Welcome back!",
"ナガレ―！！　心配したんだぞー！！":
    "Nagare—!! We were so worried!!",
"よかったー！！　よかったナガレー！！":
    "Thank goodness!! Thank goodness, Nagare!!",
"すごいよ…　すごいよナガレ！！":
    "You're amazing... amazing, Nagare!!",
"やっぱりナガレはすごいよ！！":
    "As I thought, Nagare is amazing!!",
"お、オレたちも結構がんばったぜ…！！":
    "H-Hey, we worked pretty hard too...!!",
"もちろんですじゃ！": "Of course!",
"継承者の方々、皆さまもご苦労様じゃった！":
    "Inheritors and everyone—good work!",
"へへへ、サンキュー！！": "Hehehe, thanks!!",
"…感動の再会中に悪いが…":
    "...Sorry to interrupt the moving reunion, but...",
"…ナガレ。別れる前に、水の紋章を返したい。":
    "...Nagare. Before we part, I'd like to return the Water Crest.",
"左手を出せ。": "Hold out your left hand.",
"…え？　ああ、でも…": "...Huh? Oh, but...",
"おい、ちょっと待て！": "Hey, wait a moment!",
"…もしかして、あんた知らないのか？":
    "...Could it be you don't know?",
"ハ…？　…何をだ？": "Hah...? Know what?",
"一度継承者になった奴は、ふたたび紋章を":
    "Once you've become an inheritor, you can never",
"継承出来ないんだよ。": "inherit a crest again.",
"ああ、やっぱりそうなのか。": "Ah, so that's how it is.",
"セイリューの言い伝えでもそうなんだよ。":
    "That's what Seiryu's traditions say too.",
"な…んだと…？": "Wh-What...?",
"オタキ様、姉さま、みんな…": "Lady Otaki, sis, everyone...",
"本当なのか…！？": "Is it true...!?",
"そ、そんなのは困るぞ…。": "Th-That won't do...",
"おい、ナガレ！　お前のばあさんや姉さん…":
    "Hey, Nagare! Your grandma and sister...",
"なんでもいい…　ほかに家族はいないのか！？":
    "Whatever—are there other family members!?",
"…ただいま帰りました！！": "...I'm home!!",
"オタキ様もシズク様も、既に元継承者だし…":
    "Lady Otaki and Lady Shizuku are already former inheritors, and...",
"そもそもふたりの年齢と病気があったから、":
    "it was precisely their age and illness that made",
"あたしが継承したんだぞ？": "me inherit, remember?",
"もしふたりが紋章を継承できるのだとしても…":
    "Even if they could inherit...",
"無暗に負担を強いる事になる。": "it would burden them needlessly.",
"だから、あたしは許可しない。": "So I won't allow it.",
"…俺が信頼している人間なんて、いないぞ…？":
    "...There's no one I trust, you know...?",
"せいぜいウィンや…あんたらくらいだ…":
    "At most, Win and... you lot...",
"…お、俺はどうすればいいんだ…":
    "...Wh-What am I supposed to do...",
"何かいい案はないのか！？": "Isn't there a good solution!?",
"帰ったぜ！　親父！！": "I'm back! Dad!!",
"…んなこと言われてもな…": "...Don't put me on the spot...",
"だからよ…　悪いとは思うんだが…":
    "So you see... I'm sorry about this, but...",
"あんた、結構長いこと、継承者のままだぜ！！":
    "you're going to stay an inheritor for quite a while!!",
"ピピン殿…　どうかホノオに世継ぎが誕生し…":
    "Lord Pipin... please hold the Fire Crest until Hono",
"育つまで、火の紋章をお預かりいただきたい。":
    "has an heir who comes of age.",
"困るんだがな…。": "That's a problem...",
"もし…！　ピピン殿がどうしても紋章を":
    "If...! Lord Pipin absolutely wishes to",
"手放したいとお思いであれば…、他の者に継承":
    "relinquish the crest... you may pass it on",
"してもらっても構わん。": "to someone else.",
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
