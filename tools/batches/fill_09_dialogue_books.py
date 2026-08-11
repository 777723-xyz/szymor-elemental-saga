#!/usr/bin/env python3
"""Fill batch 09: lore books, complaint letters, garrison dialogue."""
import csv
import os
import re

D = {
"闇が膨らみ　　　　　　　闇が閉じ":
    "The darkness swells... the darkness closes",
"次元が　　　　　　　　　　歪んでいく":
    "the dimensions... warp apart",
"闇は開き　　　　闇は広がり":
    "the darkness opens... the darkness spreads",
"次元が　　　　　　戻る": "the dimensions... return",
"とてもじゃないですが無理です陛下…！":
    "It's quite impossible, Your Majesty...!",
"城下町のバリアフリー化　資材3460G 人手6845G":
    "Accessibility for the castle town - materials 3460G, labor 6845G",
"出来なくもないですが、車椅子使っている国民ゼロです…":
    "It's possible, but there are zero citizens using wheelchairs...",
"万金丹を　２個　渡された！": "Received 2 Mankintan!",
"二人とも、西の監視塔の見回りだろ？":
    "Both of you are on West Watchtower patrol, right?",
"お金を　５００Ｇ　渡された！": "Received 500G!",
"…万金丹？これは、毒消しの薬だな。":
    "...Mankintan? This is an antidote, isn't it.",
"そんな厄介な魔物がいるのか？": "There are monsters that nasty?",
"西の監視塔に忍び込んだ子供が魔物に襲われて、":
    "A kid who snuck into the West Watchtower was attacked by a monster,",
"ほれ、今回の支給品だ。受け取れ。":
    "Here, your provisions for this mission. Take them.",
"毒で死にかけたって話だ。": "and nearly died of poison, or so the story goes.",
"だから当然、毒への備えをしておいた。":
    "So of course, I prepared against poison.",
"…というか、報告いってないのか？":
    "...Wait, did you not report this?",
"…ったく。": "...Sheesh.",
"どうせサクソンが陛下に伝え忘れたんだろう。":
    "Saxon probably forgot to tell His Majesty again.",
"それ、ありうるなあ…。": "Yeah, that tracks...",
"まあ、何にしろ、気をつけてな。": "Well, anyway, stay safe.",
"足りないものは、その５００Ｇで何とか":
    "Whatever else you need, make do",
"用立ててくれ。": "with that 500G.",
"こんな任務、ささっと終わらせてくるさ。":
    "I'll wrap up this mission in no time.",
"必要なものがあったら、また来いよ。":
    "If you need anything, come back.",
"支給したもの以外で欲しいものがある場合は、":
    "If there's anything you want beyond what we issued,",
"自前で金を払ってもらうぜ。": "you'll be paying for it yourself.",
"さあ、何が欲しいんだ？": "So, what'll it be?",
"私の隣の家の人が夜中に歌を歌います。":
    "My neighbor sings in the middle of the night.",
"文句を言ったら笛を吹き出しました。":
    "When I complained, he started playing the flute.",
"彼は、音楽家になるんだそうです！助けて下さい。":
    "He says he's going to become a musician! Please help me.",
"ちょっと！仕事の邪魔をしないで下さい！":
    "Hey! Don't interfere with my work!",
"さっきからあなたはウロチョロと…":
    "You've been wandering around since a while ago...",
"何してるんです、本当に騎士なのか！？":
    "What are you doing? Are you really a knight!?",
"靴底がはがれました。先月は穴があきました。":
    "My shoe soles came off. Last month they got holes.",
"この国の靴は、もろすぎます！抜本的に解決してください！":
    "This kingdom's shoes are far too fragile! Please fix this fundamentally!",
"働き者ほど、靴代でお金がかかります！":
    "The harder you work, the more you spend on shoes!",
"早く行くぞ！": "Let's go, quickly!",
"おい！何読んでやがる！": "Hey! What are you reading!?",
"『スキルの勉強』": '"Studying Skills"',
"スキルポイントは、バトル中に敵を攻撃したり、":
    "Skill Points build up during battle by attacking enemies,",
"攻撃されたりすることで溜まるが、戦いながら探ると":
    "or by being attacked. If you probe as you fight,",
"よいだろう。ぼうぎょをすると大きく溜まるのは確かだ。":
    "you'll figure it out. Guarding definitely builds it up a lot.",
"使いたいスキルがあるときは活用するといいだろう。":
    "Use it when there's a skill you want to use.",
"使用できるスキルの種類は、武器ごとに違うが、":
    "The skills available differ by weapon, but",
"品質のよい武器ほど、使用できるスキルの種類が増える":
    "the better the weapon, the more skill types become available.",
"傾向にあるようだ。": "That seems to be the trend.",
"スキルとは、装備している武器ごとに使える特技のことで、":
    "Skills are special techniques usable with the weapon you have equipped.",
"スキルポイント（SP)を消費して使うことのできる、":
    "They cost Skill Points (SP) to use,",
"強力だったり、便利な技の数々である。":
    "and include powerful and handy techniques.",
"おお…騎士様…": "Oh... Sir Knight...",
"この度は娘たちが大変お世話になったそうで…":
    "I hear my daughters were greatly helped by you...",
"お礼と言ってはなんですが…": "It's not much of a thanks, but...",
"どうかこれをお受け取り下さい…": "please accept this...",
"孫と会えたいま、もう必要なくなりましたので":
    "now that I've been able to meet my grandchild, I no longer need it",
"あーいそがしい！いそがしい！": "Ah, so busy! So busy!",
"食糧庫のパンが最近減っている。何が起こっているんだ？":
    "Bread's been disappearing from the larder lately. What's going on?",
"誰かに調べて欲しいが、もしかしたら犯人が騎士団に":
    "I want someone to look into it, but the culprit might be in the knight order itself...",
"いるかも知れない…。誰に相談すればいいんだろう…。":
    "Who can I even talk to about this...",
"書きかけの手紙がある…": "There's an unfinished letter...",
"その後には知らない名前が五人くらい書いてある。":
    "After it are about five names I don't recognize.",
"騎士団長ロイ様へ": "To Lord Roi, Knight Commander",
"新たな騎士候補者のリストをお送りします。":
    "I send you the list of new knight candidates.",
"どの者も将来の楽しみな者たちです。":
    "They are all promising youths for the future.",
"いつもお手数をおかけしますが、ご確認ください。":
    "I apologize for the trouble as always; please review it.",
"『世界の武器』": '"Weapons of the World"',
"曲剣。フレイム王国のみで生産される、刃の反った剣。":
    "Curved sword: a blade with a curved edge, produced only in the Flame Kingdom.",
"振り回しやすく、素早さが少し上がる。":
    "Easy to swing, slightly raises agility.",
"刀。セイリューでのみ生産される。美しく鋭い剣。切れ味が":
    "Katana: produced only in Seiryu. A beautiful, sharp sword. Its edge is",
"抜群だが、取り回しが悪く、素早さが下がる。":
    "excellent, but it's hard to handle and lowers agility.",
"他に、大剣という、重くて凄まじい威力の剣や、":
    "There are also great swords—heavy blades of fearsome power—",
"短剣、刺剣、槍といった、突き刺す武器もある。":
    "and thrusting weapons like daggers, rapiers, and spears.",
"この三つは敵の急所を突きやすい（会心率があがる）が、":
    "These three hit enemy vitals easily (raising critical rate), but",
"槍は元の威力が他のふたつよりも高い分、素早さが下がる。":
    "spears have higher base power than the other two at the cost of agility.",
"このエレメント大陸には、大きく分けて次のような武器が":
    "On this Element Continent, the weapons that are widespread fall",
"普及している。": "roughly into the following types.",
"直剣。もっとも普通の剣で、主にウインダム王国で生産され":
    "Straight sword: the most ordinary sword, produced mainly in the Windam Kingdom.",
"ている。扱いやすい。": "Easy to handle.",
"『エレメンタルパワー』": '"Elemental Power"',
"かつて大昔、この大陸が生まれる前、紋章の力で闇の":
    "Long ago, before this continent was born, the power of the crests sealed the Dark",
"エレメントを彼方に封じ、火水風のエレメントの加護を":
    "Element far away, and this land flourished under the blessing of the Fire, Water, and Wind Elements—",
"受けてこの地が栄えたと伝わるが、その紋章の力が、":
    "or so the legends say. Just what that crest power",
"実際にどんなものだったのかは、よく分からない。":
    "truly was, however, is not well understood.",
"ただ、紋章の魔法の力、エレメンタルパワーは、継承者の":
    "Still, there are tales that the crests' magical power—Elemental Power—is",
"精神力そのものであるいう言い伝えもある。":
    "none other than the inheritor's very mental strength.",
"そうであるのなら、精神の弱いものが継承者になると、":
    "If that's so, then when someone weak of spirit becomes an inheritor,",
"魔法の力も弱まってしまうのかも知れない。":
    "their magical power might also weaken.",
"火、水、風、それぞれの紋章は、闇のエレメントが復活し、":
    "When the Dark Element revives, each crest—fire, water, and wind—",
"その力を強めるほどに、紋章も輝きを増し、不思議な魔法の":
    "glows brighter as it strengthens, granting the inheritor strange magical",
"力を紋章継承者に与えるという。": "power.",
"この魔法の力が、エレメンタルパワーである。":
    "That magical power is Elemental Power.",
"『怖くない！五分で怖くなくなる錬金術』":
    '"Don\'t Be Scared! Alchemy Without Fear in Five Minutes"',
"例えばみんながよく心配するのが、各ポーション類…":
    "What everyone worries about, for instance, are the potions and such—",
"飲み薬に使われている、材料のことだと思います。":
    "specifically, the ingredients used in the medicines.",
"確かに私たちは材料を教えません、隠していますが、":
    "It's true we don't reveal the ingredients; we keep them hidden, but",
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
