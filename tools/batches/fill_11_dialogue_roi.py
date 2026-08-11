#!/usr/bin/env python3
"""Fill batch 11: watchtower report to the king, Roi's summoning, inn notes."""
import csv
import os
import re

D = {
"ロイは気難しい男だ…。": "Roi is a difficult man...",
"説得は難しいかも知れないが、頼むぞ。":
    "He may be hard to persuade, but I'm counting on you.",
"どうした？": "What is it?",
"最上階に怪しいガイコツの男がいました。":
    "There was a suspicious skeleton-like man on the top floor.",
"奴は自分を闇のエレメントの担い手…":
    "He called himself the bearer of the Dark Element...",
"大魔道士ピ…ピ何とかと名乗りました…。":
    "some Grand Mage Pi... Pi-something...",
"よくぞ戻った、騎士ピピン、騎士ウィンよ。":
    "Welcome back, Knight Pipin, Knight Win.",
"大魔道士ピ…なんとかだと……！？":
    "A Grand Mage Pi... something, you say......!?",
"いや、わからん。そもそもピ何とかでは、":
    "No, I don't know it. Pi-something hardly",
"もし知っていたとしても、わからなそうだ…。":
    "gives you anything to go on...",
"きっと、ちょっと変なやつというだけだとは":
    "I'm sure he's just some odd fellow, but",
"思いますが、一応報告しました。": "I thought I'd report it anyway.",
"ふむ…。": "Hmm...",
"しかし、闇のエレメントの復活の予兆":
    "But this could be a sign of the Dark Element's",
"なのかも知れないな。": "revival.",
"ああ、やつはそんなことも言っていました。":
    "Yes, he did say something like that.",
"闇のエレメントの復活が近いとか何とか…":
    "That the Dark Element's revival was near, and so on...",
"闇の結晶を集めるとか何とか…":
    "That he'd gather Dark Crystals, and so on...",
"闇の結晶を集めるだと！！！！！？": "Gather Dark Crystals, you say!!",
"早速だが、調査結果を教えてくれ。": "Now then, tell me what you found.",
"以前ロイから聞いたことがある…。":
    "I've heard about this from Roi before...",
"この大陸には、闇の力が集まりやすい場所が":
    "There are places on this continent where dark power gathers easily,",
"あって…": "and...",
"闇のエレメント復活の際には、その場所に":
    "when the Dark Element revives, Dark Crystals",
"闇の結晶が現れるらしいと…": "are said to appear at those places...",
"ピピン、そしてウィンよ。": "Pipin, and you too, Win.",
"本当に闇のエレメントの復活が近いとするなら、":
    "If the Dark Element's revival truly is near,",
"風の紋章の継承者であるロイの力が必要だ。":
    "we need the power of Roi, the Wind Crest's inheritor.",
"…森の奥に引きこもっている、かつて天才と":
    "...The legendary knight who was once called a genius",
"呼ばれた、伝説の騎士、ロイ…":
    "but now lives secluded deep in the forest... Roi...",
"…そうだ、ピピン。": "...That's right, Pipin.",
"闇のエレメントに対抗できるのは、":
    "Only the inheritors of the Fire, Water, and Wind crests",
"火、水、風の紋章の継承者だけだ。":
    "can stand against the Dark Element.",
"そして、ロイはここ何十年も、山奥で古文書を":
    "And Roi has spent decades reading ancient texts",
"読み、研究を続けている。": "and researching in the mountains.",
"彼の力が、いまこそ必要なのだ。":
    "His power is needed now more than ever.",
"二人は急いでロイの元に向かい、":
    "Hurry to Roi's side, the two of you,",
"ここへ出てくるよう説得して参るのだ。":
    "and persuade him to come here.",
"塔の内部は人食いの魔物だらけでした。":
    "The tower was crawling with man-eating monsters.",
"俺は…": "As for me...",
"俺は残ります。": "I'll stay behind.",
"ウィンにだけ、行かせて下さい。": "Let Win go alone.",
"実はな、ピピン…": "You see, Pipin...",
"いちばんの大物、人食いイヌは倒しました。":
    "The biggest of them, the man-eating dog, was defeated.",
"このような事態になったときには、":
    "For situations like this,",
"ピピンを寄こすよう、以前ロイから":
    "Roi asked me beforehand to send Pipin",
"頼まれているのだよ。": "in such cases.",
"…な、んだと………？": "...Wh-What......?",
"この意味…": "The meaning of this—",
"分からないお前ではあるまい、ピピン。":
    "surely even you understand, Pipin.",
"火と水の紋章の継承者との合流を急げ。":
    "Hurry to meet up with the Fire and Water inheritors.",
"それまで私は国の防衛強化と情報収集に":
    "Until then, I'll focus on strengthening the kingdom's defenses",
"務める。": "and gathering information.",
"宿泊者たちの書き残しがある。読んでみようか…。":
    "Guests have left behind some notes. Should we read them...?",
"この国のごはんは美味しくない！":
    "The food in this country is not tasty!",
"このホテルの食事が美味しくないのかと思ったら、":
    "I thought it was just this inn, but",
"外のレストランも美味しくなかった！":
    "the restaurants outside weren't tasty either!",
"でもパン屋のパンは美味しかったなあ。":
    "But the bakery's bread was delicious.",
"宿舎に帰るのが嫌で、しょっちゅうここに泊まってる…。":
    "I hate going back to the barracks, so I'm always staying here...",
"一泊100Gもするから、そろそろお金がなくなってしまう。":
    "At 100G a night, I'll soon run out of money.",
"どうしよう…　でもピピンの嫌味が怖くて、胃が痛い…。":
    "What should I do... but Pipin's snide remarks scare me, and my stomach hurts...",
"騎士、やめようかな…。": "Maybe I should quit being a knight...",
"フレイムからここまで行商に来るのに丸ひとつきも":
    "It took me a full month to come all the way from Flame on business.",
"かかった。そんなに遠くないのに、手形がないせいで、":
    "It's not that far, but without a permit I",
"関所で長いことまちぼうけを食わされたからだ。":
    "was made to wait forever at the checkpoint.",
"なんでこの国はこんなに入国が厳しいんだ！？":
    "Why is this country so strict about entry!?",
"そうですか…": "I see...",
"では、お好きなだけ見て回って行って下さい。":
    "Then please, look around as much as you like.",
"水がたくさん入っている": "It's full of water.",
"そうだ、ウィン。": "Oh, Win.",
"外でおもしろい本を見つけたら、私に持って":
    "If you find an interesting book out there,",
"帰ってきてちょうだい。": "bring it back for me, won't you?",
"読む本がなくなって退屈しているのよ…。":
    "I've run out of reading material and I'm bored...",
"いらっしゃいませ騎士様！": "Welcome, Sir Knight!",
"水がたくさんはいっている": "It's full of water.",
"お腹いっぱい食べて、みんなのＨＰが回復した！":
    "Everyone ate their fill and recovered HP!",
"『七転び七起きれず』": '"Seven Falls, Can\'t Get Up Eight Times"',
"毒にかかったり、眠ってしまったり、混乱したり…":
    "Getting poisoned, falling asleep, being confused...",
"そういった状態異常は、すぐに死にはつながらないが、":
    "These ailments won't kill you right away, but",
"転倒は即死につながりかねない。":
    "a knockdown can be a death sentence.",
"しかも、薬を飲んで治したりもできない。":
    "What's more, you can't even cure it with medicine.",
"ドタバタしながら、少しでも早く起き上がれることを":
    "All you can do is flail about and pray you get up",
"祈るしかない…。": "as quickly as possible...",
"戦闘中に、転倒してしまったら大ピンチだ。":
    "If you get knocked down mid-battle, you're in big trouble.",
"しばらくなんの行動も取れなくなるし、":
    "You can't act for a while,",
"何よりも、防御力がゼロになってしまうのだ。":
    "and worst of all, your defense drops to zero.",
"『素早さの重要性』": '"The Importance of Agility"',
"もちろん、頑丈な防具を着れば、受けるダメージが減るし、":
    "Of course, sturdy armor reduces damage taken,",
"強力な武器を持てば、与えるダメージが増える。":
    "and a powerful weapon increases damage dealt.",
"しかし、素早さが低ければ、動く前にすべての敵から":
    "But if your agility is low, every enemy will attack",
"攻撃されるだろう。": "before you can move.",
"敵の中には強力な状態異常攻撃や、全体攻撃を持つものも":
    "Some enemies have powerful ailment attacks",
"多い。": "or group attacks.",
"そういった攻撃を浴びれば、強力な武器も防具も、":
    "If you're hit by those, even strong weapons and armor",
"殆ど役に立たない。": "are nearly useless.",
"戦闘中に、敵よりも早く動けるかどうかは、":
    "Whether you can act before your enemies in battle",
"素早さにかかっている。": "depends on agility.",
"しかし、頑丈な防具や、強い武器を持てば、その重さで":
    "But sturdy armor and strong weapons are heavy,",
"素早さは下がってしまう。": "and lower your agility.",
"『武器や防具の品質』": '"Weapon and Armor Quality"',
"するが、反面、重くなったりするものもあるので、":
    "On the other hand, some get heavier...",
"必ずしも、品質のいいものを装備すればいいという":
    "so equipping the highest quality gear isn't",
"ものでもない、かも知れない…。":
    "always the best choice, perhaps...",
"相手や場所、自分の役割によって、":
    "Depending on the enemy, the place, and your role,",
"バランスの取れた組み合わせにするのが良いだろう。":
    "a well-balanced setup is probably best.",
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
