#!/usr/bin/env python3
"""Fill batch 49: Hono's solo duel with Nau, Mycenae's rescue."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"いやでもこのひとらに城ん中うろうろさせたら":
    "But if we let these folks wander the castle,",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"オレは戦いに集中できる…　":
    "I can focus on the battle...",
"だからオマエもオレを信じてくれ…":
    "so you trust me too...",
"オレはコイツに…　絶対に勝つ！！":
    "I will... absolutely beat this guy!!",
"…あんたがそこまで言うんだ":
    "...If you're willing to go that far,",
"…わかった。そいつはあんたに任せる。":
    "...fine. I'll leave him to you.",
"やっぱりアンタだったなあ………":
    "So it really was you, after all......",
"ナウーーーーーーーーーッ！！！！！！":
    "Naaaau—!!!!!!",
"ホノ…オ…": "Ho...no...",
"親父…！大丈夫か！！": "Dad...! Are you all right!!",
"すまぬ…ホノオ…": "Forgive me... Hono...",
"街を…　城を守れなかった…":
    "I couldn't protect the town... or the castle...",
"そんなこと、いまはいい！！":
    "That doesn't matter right now!!",
"おい、親父、死ぬんじゃねえぞ！！":
    "Hey, Dad, don't you dare die!!",
"………急所は、外してある": ".........The vitals were spared.",
"へー………": "Heh...",
"…わかったぜ、アンタの考えてることがよー":
    "...I get it, I know what you're thinking.",
"ナガレ！": "Nagare!",
"親父にイヤシの魔法をかけてくれ！":
    "Cast your Heal spell on my dad!",
"たぶん…他のみんなも全員生きてるぜ":
    "Probably... everyone else is alive too.",
"…ちょっと待ってくれ！": "...Wait a second!",
"あんたひとりで勝てる相手なのか、それは！？":
    "Is that something you can win alone!?",
"さあ、どうかな…": "Who can say...",
"でもよー　コイツきっと、オレとサシで":
    "But hey, this guy clearly wants",
"やりたいんだと思うぜー…": "a one-on-one with me...",
"頼む、ナガレ。": "Please, Nagare.",
"コイツはオレに任せて…　親父と…、":
    "Leave him to me... and heal Dad and",
"みんなを回復してやってくれ！":
    "everyone!",
"…そ、それはいいとしても！":
    "...E-Even so!",
"ここの全員にイヤシの魔法を使ったら…":
    "If I use Heal on everyone here...",
"あたしのエレメントパワーがもたない…":
    "my Elemental Power won't hold out...",
"多分なくなっちまう…": "it'll probably run out...",
"あたしが戦えなくなるぞ！！":
    "Then I won't be able to fight!!",
"おお…　これが紋章の魔法か…！":
    "Oh... so this is the crest's magic...!",
"さてと…　待たせたなー…": "Now then... sorry to keep you waiting...",
"ナウ―よーーーーーーーーーーー！！！！":
    "Nau—!!!!",
"アンタの言いたいことは顔を見るだけで":
    "I can read what you want to say",
"わかるんだぜー？": "just from your face, you know?",
"今度こそ1対1の戦いで我を倒して見せろ…　":
    "'This time, defeat me in a one-on-one...'",
"…火の紋章の勇者よ！！": "...hero of the Fire Crest!!",
"そう顔に書いてあるぜ、ナウ――――！！！！":
    "That's written all over your face, Nau—!!!!",
"こっちもこのときを待ってたんだ…":
    "I've been waiting for this moment too...",
"さあ、勝負だぜ！！　ナウ―！！":
    "Come on, let's settle this!! Nau!!",
"………（ゆっくりと頷いてから武器を構える":
    ".........(It slowly nods, then raises its weapon.)",
"うおおおおおおおおおお！！！！":
    "Wooooooaaaaah!!",
"王様…いま助けます…": "Your Majesty... I'll heal you now...",
"……………ッ！！　……見事なり…":
    ".........! ......Splendid...",
"イヤシ！！！！！！！！！": "Heal!!!!!!!",
"やったぜーーーーーーーーー！！！！":
    "We did it—!!!!",
"四天王を…": "A Four General...",
"本当にひとりで倒しやがった…　ホノオ…！":
    "he really took one down alone... Hono...!",
"さて、ナウ―…　": "Now then, Nau...",
"とどめを刺させてもらうぜ…":
    "I'll finish you off now...",
"消えられたら困るからよー…":
    "can't have you vanishing on us...",
"…何をしてる、ホノオ…！": "...What are you doing, Hono...!",
"消えられたら、追えなくなる…":
    "If he vanishes, we won't be able to follow...",
"早くトドメを刺すんだ！！":
    "Hurry and finish him!!",
"そうだよなあ…": "Yeah, you're right...",
"そうなんだけどよー…": "I know, but...",
"なんか…　情が移っちまって…":
    "I've somehow... grown attached to him...",
"剣に力が入らねえんだ…": "I can't put my strength into the blade...",
"バカ！　ホノオのバカヤロー！":
    "Idiot! Hono, you big idiot!",
"もういい…　": "Enough...",
"あんたが出来ないなら、あたしが…！":
    "If you can't, then I will...!",
"私も遊んであげたいところなんだけれど…":
    "I'd like to play with you all too, but...",
"ごめんなさい、そんな時間はないの。":
    "sorry, there's no time.",
"この辺りで、ナウ―は返してもらうわ。":
    "I'll be taking Nau back about now.",
"いま、こいつを失うわけにはいかないのよ。":
    "I can't afford to lose him now.",
"そうはさせるかーー！！": "Like we'll let you—!!",
"あら、いいの？": "Oh, you won't?",
"いまここで…": "If I do it here...",
"私のミケーネブリザードを放って…":
    "letting loose my Mycenae Blizzard...",
"この部屋に転がっている連中を、":
    "the ones lying around this room—",
"…改めて、皆殺しにしてあげてもいいのよ？":
    "...I could slaughter them all over again, if you'd like?",
"じゃあそういうことで…": "Then it's settled...",
"ナウ―は連れて行かせてもらうわ。":
    "I'll be taking Nau with me.",
"計画に支障がでるわ…　ナウー、行くわよ。":
    "It'd hamper the plan... Nau, we're leaving.",
"…な、なに！？": "...Wh-What!?",
"まだ…ピンピンしてやがるのかよ…？":
    "You're... still kicking...?",
"あなたたち…強いわ。": "You lot... are strong.",
"あたしたちの予想を軽く超えるほどにね…。":
    "Far beyond what we expected...",
"きっとまた会うことになる…":
    "We'll surely meet again...",
"そのときが、本当の最後になるわ。":
    "and that will be the true end.",
"随分と一方的にナウーを可愛がってくれた":
    "You gave Nau quite the one-sided",
"みたいね…": "beating...",
"いくらナウーが正々堂々の真体バトルを":
    "As much as Nau imposes fair, all-out battles",
"自分に課しているとはいえ…": "on itself...",
"一方的過ぎたわ。": "it was far too one-sided.",
"へへ…！！": "Hehe...!!",
"それだけオレが強くなったってことだぜ！":
    "That just means I've gotten that strong!",
"あら、そんなに？": "Oh, is that so?",
"あたしとナウー、同時に相手にできるかしら？":
    "Can you handle me and Nau at once?",
"なんだって…！？": "What...!?",
"本当はそんな時間ないんだけれど…":
    "I truly don't have time, but...",
"あなたたちには借りがあるからねえ…":
    "I owe you a debt, you see...",
"ここで返させてもらうわ…！！":
    "so I'll repay it here...!!",
"な、ナガレ…": "N-Nagare...",
"オレひとりじゃ無理だ…！！":
    "I can't do it alone...!!",
"そんなことは分かってるよ！！":
    "I know that!!",
"…やるしかない…！！": "...We've no choice...!!",
"ナウー？　もうさっきの傷は癒えたわね？":
    "Nau? Your earlier wounds have healed, right?",
"…次はもう少しだけ本気でやってちょうだい":
    "...this time, try a little harder, won't you?",
"来るぞ…！！": "Here they come...!!",
"…やったぞ！！": "...We did it!!",
"…さすがに時間切れね。": "...Out of time, as expected.",
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
