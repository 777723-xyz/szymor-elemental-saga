#!/usr/bin/env python3
"""Fill batch 36: Roi's tragedy, Flame restaurant scenes."""
import csv
import os
import re

D = {
"けい…しょ…　けいしょうしゃ！": "Inhe... inheritor!",
"ぼくの手に…もんしょうがあるよ！":
    "On my hand... there's a crest!",
"ぼくはけいしょうしゃになったんだ！":
    "I've become the inheritor!",
"すごい！すごい！": "Amazing! Amazing!",
"おとうさん！": "Daddy!",
"ぼくの手にもんしょうが………":
    "My hand has a crest too......",
"おとう…さん………？": "Daddy......?",
"おとうさん…どうしたの、そのケガ…":
    "Daddy... what happened to that wound...",
"サクソンが全軍を指揮していたんだ。":
    "Saxon was commanding the whole army.",
"なぜ私の許可なしに、全軍を動かしたのです！":
    "Why did you move the whole army without my permission!",
"これはこれはロイ騎士団長…":
    "Well, well, Commander Roi...",
"あなたの手をわずらわせるのも悪いと思ってな":
    "I thought it improper to trouble your hands,",
"なあに、この程度の敵、私にお任せ下され。":
    "never you mind—leave enemies of this caliber to me.",
"団長は安心して家に帰り、市民とのお祝いを":
    "Go home at ease, Commander, and continue",
"お続け下され…": "your celebration with the citizens...",
"気合い負けするなーっ！": "Don't lose your nerve!",
"一気にかかれーーーーーいっ！！":
    "Charge all at once—!!",
"伝令！でんれーーーーーーーーーい！！":
    "Messenger! Message—!!",
"俺が現場に着いたとき…": "By the time I reached the scene...",
"既に戦闘が始まっていた。": "the battle had already begun.",
"代々何度も騎士団長を輩出している名門の男…":
    "A man of a distinguished house that produced Knight Commander after Knight Commander...",
"火の手があがっています…！": "Flames have risen...!",
"えーい、それがどうした！": "Bah, so what!",
"塔の外にいた野党が…森の中の家を":
    "The bandits outside the tower are attacking",
"襲っているようです…　　その…":
    "a house in the forest... that is...",
"ロイ騎士団長の家を…": "Commander Roi's house...",
"…なんだと": "...What did you say",
"兵の何人かを救出に向かわせるぞ！いいな！？":
    "I'm sending some soldiers to rescue them! Understood!?",
"騎士団長は私だ！命令には従ってもらう！":
    "I am the Knight Commander! You will obey my orders!",
"サクソン殿…！": "Lord Saxon...!",
"…兵は割けませんな。": "...I cannot spare the soldiers.",
"なんだと…！？": "What...!?",
"野盗の数が多いのです。": "There are too many bandits.",
"いま兵を減らすと、こちらが押されます…。":
    "If we thin our ranks now, we'll be overwhelmed...",
"ええい！なんだ、この忙しいときに！！":
    "Bah! What now, at such a busy time!!",
"あなたは…見殺しにするというのか…":
    "You... you'd let them die...",
"それも私のことが憎いからか!？":
    "Because you hate me that much!?",
"なにを…　この場を乗り切ってからであれば…":
    "What—... if we survive this moment...",
"あのひとたちだって、我々が守るべき市民！":
    "Those people are citizens we're sworn to protect!",
"それなのに、見殺しにするというのだな…":
    "And yet you'd abandon them...",
"あなたは…　私憎さに…！！":
    "Because you loathe me...!!",
"そんなに心配ならば、お前が行けばよかろう！":
    "If you're so worried, go yourself!",
"その風の紋章の力で、疾風となり、":
    "Become a gale with the Wind Crest's power",
"ひとりで助けに行かれればよい！！":
    "and go save them all on your own!!",
"何を…バカな…": "What... Don't be absurd...",
"兵は割けん…": "I can't spare the soldiers...",
"割けんのだ………": "I can't......",
"東の森に煙が…": "Smoke in the eastern forest...",
"ことはよく覚えている…": "I remember it all too well...",
"紋章よ、輝いてくれ、":
    "Crest, shine for me,",
"風のエレメントの力で、俺を疾風にしてくれ":
    "turn me into a gale with the Wind Element's power",
"…ってな": "...is what I prayed.",
"勿論、紋章は少しも輝かなかった。":
    "Of course, the crest didn't shine at all.",
"これが、俺の、おとぎ話に翻弄された一生さ。":
    "That is my life—tossed about by fairy tales.",
"何が紋章だ…　継承者だ………":
    "A crest, my foot... an inheritor......",
"俺には何も守れない…": "I can't protect a thing...",
"俺には何もない……": "I have nothing......",
"こんな…こんなもの………！！":
    "This... this thing......!!",
"そこからどうやって家までたどり着いたのか…":
    "How I made it home from there...",
"そのとき、ヤケになった俺は、自らの左手を":
    "In my desperation, I swung my sword, trying to",
"斬り落とそうと、剣を振り下ろした。":
    "hack off my own left hand.",
"だが、俺の左手は何度斬りつけても、":
    "But no matter how many times I struck,",
"切り落とされてはくれなかったんだ。":
    "my left hand refused to come off.",
"血は流れる、痛みもある…":
    "Blood flowed, and it hurt...",
"それなのに、左手はつながったままだった。":
    "and yet the hand stayed attached.",
"それはいまだに、よく覚えていないんだが…":
    "I still don't remember this clearly, but...",
"走りながら、野盗を何人か斬って…":
    "As I ran, I cut down several bandits...",
"その間ずっと、左手の紋章に祈り続けていた":
    "all the while praying to the crest on my left hand.",
"どうもいきなり失礼しました…。":
    "Forgive me for the sudden intrusion...",
"もし見つけられましたら、教えてください。":
    "If you find him, please let me know.",
"相応のお礼は必ずさせていただきます。":
    "I will surely reward you handsomely.",
"ぶしつけに失礼ですが…": "Pardon my rudeness, but...",
"あなたは耳の長い男を見たことが":
    "have you ever seen a man with long ears",
"ありませんか？": "around here?",
"あいよー　少しだけ待ってってねー！":
    "Coming right up—just wait a sec!",
"もうお腹いっぱいなのー？": "Full already?",
"まだまだだなー　また来てね！":
    "Not done yet—come again!",
"いろんなカレーや串焼きがあるよー":
    "We've got all kinds of curry and skewers~",
"お金が足りないじゃないの！":
    "You don't have enough money!",
"ちゃんとお金持ってきてから話かけて！":
    "Come talk to me after you've brought enough money!",
"お腹いっぱい食べてってねー": "Eat your fill now~",
"じゃあ何しに来たの！": "Then why did you come!",
"邪魔だから出てってー！": "You're in the way—get out!",
"全員分で50Gでいいよー！":
    "50G for everyone, alright!",
"ちーっす！　メシ中っすわ。":
    "Yo! Mid-meal here.",
"いやー兵隊になってからは毎日ここのメシ":
    "Man, ever since joining the army, eating here every day",
"食えるんでサイコーっすわ！": "is the best!",
"カレーばっかり食ってて飽きないかって？":
    "Bored of eating curry all the time, you ask?",
"いや、あんたカレーが何種類あると思ってる？":
    "No, how many kinds of curry do you think there are?",
"ほぼ無限だから、飽きるとかじゃないんだよ":
    "Practically infinite—boredom isn't a factor.",
"いやー　フレイムは食事もうまいが、":
    "Man, Flame's food is great,",
"酒もうまいですなー！この世の天国ですよ！":
    "and the drink too! It's heaven on earth!",
"ある程度お金のある人間にとってはね！":
    "For those with a bit of money, that is!",
"最近スパイスの買い付けに来る商人が増えて、":
    "Lately more merchants come to buy spices,",
"実入りがいいんだ。　こうしてたまには":
    "so business is good. Every so often,",
"いいモノ食えるようになったんだよねー":
    "I can even afford the good stuff now.",
"もういいのか…？": "That's all...?",
"ふーん、価値の分かる人間かどうか…":
    "Hmm, whether you know value when you see it...",
"次の機会にまた判断させてもらうよ。":
    "I'll judge again next time.",
"ほう…この店に客が来るとは珍しい。":
    "Oh... a customer in this shop, how rare.",
"みな貧乏人ばかりで、うちの価値のわかる":
    "Everyone's so poor, so few people",
"人間が少ないからな…。さあ、見てって…。":
    "appreciate our goods... Go on, take a look...",
"ほわわえ…": "Whoa...",
"どれも飲んだら若返りそうな薬じゃあ…":
    "These medicines look like they'd make you young again...",
"うむう　ゴミしか売ってないなあ…":
    "Hmm, only junk on sale here...",
"さすがはお金持ちの異国の方！":
    "As expected of a wealthy foreigner!",
"至福のひとときをお過ごしくださいー！":
    "Enjoy a blissful time—!",
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
