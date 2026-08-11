#!/usr/bin/env python3
"""Fill batch 31: Roi's backstory (childhood, inheritance, loneliness)."""
import csv
import os
import re

D = {
"得た知識に過ぎん。": "knowledge I've pieced together, nothing more.",
"実際にどうなるのかは…誰にも分からんのだ。":
    "What truly happens... no one knows.",
"俺はまだ気になることがある…。":
    "There are still things I'm curious about...",
"過去に読んだ文献をもう一通り読み直してみる。":
    "I'll reread the documents I've studied before.",
"…だがその前に、もしよかったら、":
    "...But before that, if you wouldn't mind,",
"お前に聞いて欲しい話がある。":
    "there's a story I'd like you to hear.",
"聞いてくれる気になったなら、もう一度":
    "If you're willing to listen, speak to me",
"俺に話し掛けてくれ…。": "again...",
"…何も言うな、ウィン。": "...Don't say a word, Win.",
"…ピピンのことか。": "...You're thinking of Pipin.",
"すまなかった。": "I'm sorry.",
"俺があいつに、あんな言い方をしてしまった":
    "There was, in fact, a reason I spoke",
"のには、一応、理由があるんだ…。":
    "to him the way I did...",
"俺の、若い頃の昔話だ…。": "It's a tale from my youth...",
"お前は風の紋章の継承者だ。":
    "You are the inheritor of the Wind Crest.",
"話しておいてもいいのかも知れん…。":
    "Perhaps it's fine to tell you...",
"だが、長くなるぞ。": "But it will be long.",
"それでもよければ、聞くか？":
    "If you still want, will you listen?",
"わかった。": "Very well.",
"俺が風の紋章を継承したのは…":
    "I inherited the Wind Crest...",
"実は子供の頃だったんだ。": "when I was still a child.",
"ああ、まだ字も読めなかったくらい、幼い頃だ":
    "Yes, so young I couldn't even read yet.",
"そうだな…。": "Right...",
"いまは時間が惜しい。": "Time is precious now.",
"いつか機会があれば、聞いてくれ。":
    "Ask me again someday, if the chance comes.",
"この世界にまだほんの少しだけ残っていた、":
    "They were the few people in this world",
"俺の味方を　してくれるひとたちだった…":
    "who still took my side...",
"でも、その頃の俺は、そのありがたみも":
    "But back then, I didn't even appreciate",
"わかっていなかった…。": "that blessing...",
"誰でも同じ…他人が嫌いだった。":
    "Just like everyone—I hated others.",
"その頃ちまたを騒がしていた野盗の集団が、":
    "When word came that the bandit gang troubling",
"西の監視塔に集まっているという情報が入った":
    "the town at the time had gathered at the West Watchtower,",
"とき…": "that moment...",
"俺は内心ホッとしながら…":
    "I was secretly relieved as I...",
"街のひとたちをそのまま置いて、":
    "left the townsfolk behind",
"現場の指揮に向かったんだ。": "and headed off to lead the operation.",
"俺の父は…": "My father...",
"俺の父は家に帰る途中に、": "My father was attacked by a monster",
"魔物に襲われて死んだ。": "on his way home and died.",
"俺の父はどうも弱かったみたいだな…。":
    "My father was apparently rather weak...",
"頭はすごく良かったらしいんだが…":
    "They say his mind was brilliant, though...",
"ともかく、": "Anyway,",
"俺は父から、幼い頃に紋章を継承したんだ。":
    "I inherited the crest from my father as a child.",
"俺の手に紋章が刻まれてすぐに、":
    "Soon after the crest was etched into my hand,",
"父は死んだ。": "my father died.",
"まるで、とっくに死んでいたはずの父を、":
    "As if the crest had been keeping my father—who",
"紋章がぎりぎりこの世につなぎとめていたか":
    "should have died long before—tethered to this world",
"のように…すぐに死んだんだ。":
    "by the barest thread... he died immediately.",
"それからの俺は…": "From then on, I...",
"もう、子どもであることをやめた。":
    "stopped being a child.",
"毎日、昼は身体を鍛え、夜は寝ずに本を読み…":
    "Every day I trained my body by daylight and read through the night...",
"自分をひたすらに追い込んだ。": "driving myself relentlessly.",
"強くなる為に。それは父の遺言でもあったが…":
    "To grow strong. It was my father's dying wish, but...",
"何より俺はもう、紋章の継承者だったから。":
    "above all, because I was already the crest's inheritor.",
"将来は、騎士団長にならなければならない…":
    "I had to become Knight Commander someday...",
"世界の危機が来たら、それを防げる男に":
    "I had to become a man who could stop",
"ならなければならない…": "the world's crises...",
"その一心だったのさ。": "That single-minded drive was all I had.",
"そして俺は、天才と呼ばれるようになった…。":
    "And so, I came to be called a genius...",
"そう、ピピンと同じようなものだ。":
    "Yes, much like Pipin.",
"剣でも知識でも、騎士団の誰も、":
    "In swordsmanship or knowledge, no one in the order",
"俺にかなわなかったんだ。": "could match me.",
"既に継承者であったこともあって、":
    "Already being an inheritor, I became a candidate for Knight Commander",
"騎士になってすぐに騎士団長候補になった。":
    "right after becoming a knight.",
"だがな…": "But you see...",
"俺はその頃にはもう…": "by then, I had already...",
"ほとんど燃え尽きてしまったんだ…":
    "nearly burned out...",
"誰もが…俺のことを嫌いだった。": "Everyone... hated me.",
"歩いていても、聞こえてくるのは、":
    "Even as I walked, all I heard",
"俺に対する陰口や嫌みばかり…。":
    "was gossip and snide remarks about me...",
"俺の能力のことも…": "As for my abilities...",
"幼い頃に父から貰った紋章のおかげだと、":
    "everyone said they were thanks to the crest",
"みんなが言うのさ。": "I'd received from my father as a child.",
"勿論…紋章がその持ち主の能力を高めるなんて":
    "Of course... I'd never heard of a crest enhancing",
"話は聞いたことがなかったし…":
    "its holder's abilities...",
"きっと、周りの連中もそんなことは":
    "and surely the people around me",
"分かっていた…": "knew that too...",
"だけど、彼らからすれば、妬ましかったのさ。":
    "But from their perspective, they were just envious.",
"騎士になる大抵の連中は…":
    "Most who become knights...",
"将来騎士団長になること、継承者になることを、":
    "dream of one day becoming Knight Commander,",
"夢見ているものだからな…。":
    "or becoming an inheritor...",
"それを俺も分かっていたからこそ、":
    "And precisely because I understood that,",
"誰よりも努力し…自分を鍛えて、":
    "I worked harder than anyone... forged myself,",
"誰から見ても継承者に相応しい男になろうと":
    "striving to become a man worthy of the crest",
"してきたんだがな…。": "in everyone's eyes...",
"だがそうなった頃には…": "But by the time I did...",
"俺は誰からも嫌われていて…　そして…":
    "I was hated by everyone... and...",
"何より俺自身が…": "above all, I myself...",
"みんなのことを嫌いになってしまっていた…。":
    "had come to hate them all...",
"それどころか…": "Worse than that...",
"自分が騎士団長になったら…":
    "once I became Knight Commander, I even",
"あいつらを散々いじめてやろうとすら":
    "thought about tormenting them",
"思っていたのさ。": "mercilessly.",
"もうそれくらいしか…": "By then, that was about the only...",
"希望というか…　やりたいことがなかった…。":
    "hope, or... purpose I had left...",
"この世界を守りたいなんて、ちっとも":
    "I'd completely stopped feeling any desire",
"思えなくなっていたからな…。":
    "to protect this world...",
"そして…": "And then...",
"あれは俺が騎士団長になって間もない頃だ。":
    "It was not long after I became Knight Commander.",
"父と仲の良かった街のひとたちが、":
    "The townsfolk who'd been close to my father",
"俺の騎士団長就任のお祝いに、":
    "gathered at my house to celebrate",
"俺の家に集まったんだ。": "my appointment.",
"詳しくはわからないが…": "I can't say for certain, but...",
"もしかすると紋章は…": "perhaps the crest...",
"自らが失われそうなときに、少しだけ力を":
    "when it's about to be lost, exerts just a little",
"発揮するものなのかも知れない。": "of its power.",
"俺の父が死んだときも、まるで俺に継承する":
    "When my father died, it was as if it had only held",
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
