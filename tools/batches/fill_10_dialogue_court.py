#!/usr/bin/env python3
"""Fill batch 10: court scene (King Windam/Pipin/Win), crest lore books."""
import csv
import os
import re

D = {
"決して危なかったり汚かったりするものは使っていません。":
    "We never use anything dangerous or unclean.",
"私たちは、材料がバレると売れなくなるから、隠して":
    "We don't hide the ingredients because they'd stop selling",
"いるのではないのです！とても専門的で、難易度の高い":
    "if they got out! We just don't want people casually copying",
"製法で作るものなので、皆さんに気軽に真似をされて、":
    "our highly specialized, difficult methods and",
"大怪我したり病気になって欲しくないだけなのです！":
    "ending up badly injured or sick!",
"錬金術師と呼ばれる（というより自分たちで呼んでいる）":
    "It's been about a hundred years since people called alchemists—",
"ひとたちが、正体の分からない薬を大変な高額で売り出す":
    "or rather, who call themselves that—began selling unknown medicines",
"ようになって百年くらいでしょうか。":
    "at exorbitant prices.",
"でも効き目が凄いから、みんな本当は憧れているでしょう？":
    "But since they work wonders, everyone secretly admires them, right?",
"読みかけの本がある…": "There's a half-read book...",
"騎士は国王の命令に絶対に背いてはいけません。":
    "Knights must never disobey the king's orders.",
"次に、騎士団長の命令にも背いてはいけません。":
    "Next, they must not disobey the Knight Commander's orders either.",
"命令を聞かないと、騎士をやめさせられます。":
    "Disobey orders and you'll be stripped of your knighthood.",
"騎士をやめると、ただの兵士か、市民になります。":
    "If you lose your knighthood, you become a mere soldier or a citizen.",
"『この世界の紋章』": '"The Crests of This World"',
"この紋章は、闇のエレメントが復活する際に輝き出し、":
    "These crests begin to shine when the Dark Element revives,",
"闇のエレメントによって世界が暗闇に覆われ、魔物に":
    "and are said to prevent the world from being shrouded in darkness and",
"溢れるのを防ぐことが出来ると言われている。":
    "overrun by monsters at the Dark Element's hands.",
"紋章は、持ち主が最も信頼している人間へと継承される。":
    "A crest passes to the person its holder trusts most.",
"しかし紋章が輝いたのを誰も見たことがない為、現実には":
    "But since no one has ever seen a crest shine, in practice",
"権力者が継承している。フレイム王国では代々国王が、":
    "those in power inherit them. In the Flame Kingdom, the king;",
"セイリューでは領主が、ウィンダムでは騎士団長である。":
    "in Seiryu, the lord; and in Windam, the Knight Commander.",
"…という本がある。読んでみようか…。":
    "There's a book on this. Should we read it...?",
"エレメント大陸は火と水と風のエレメントによって":
    "The Element Continent is a land forged by the Fire, Water, and Wind Elements,",
"作られた土地で、エレメントの加護の証である紋章が、":
    "and crests—marks of the Elements' blessing—are",
"それぞれの紋章継承者の手の甲に刻まれる。":
    "engraved on the back of each inheritor's hand.",
"『恐怖！闇のエレメント復活！』":
    '"Terror! The Dark Element Returns!"',
"よし！ここで水の紋章の出番です。水の紋章の勇者が":
    "Alright! Now it's the Water Crest's turn! When the hero of the Water Crest",
"片手を振りかざすと、大きな津波があらわれました。":
    "raised a hand, a great tsunami appeared.",
"火はまたたくまに消えました。しかし、闇のエレメントも":
    "The fire vanished in an instant. But the Dark Element was",
"流されてしまい、どこにいったか分かりません。":
    "washed away too, and no one knows where it went.",
"このままでは世界は暗黒に包まれ、魔物が増え、ひとの":
    "At this rate, the world will be swallowed by darkness, monsters will multiply, and the land will",
"住めない土地になってしまう！しかし気付けば風の勇者が":
    "become uninhabitable! But wait—the hero of Wind is gone!",
"いません。なんと！風の紋章のハヤテの力で疾風となった":
    "What!? Transformed into a gale by the Wind Crest's Hayate,",
"風の勇者が闇のエレメントを追いかけています！":
    "the Wind hero is chasing after the Dark Element!",
"そのスピードはすさまじく、火の勇者と水の勇者は":
    "His speed is incredible, and the Fire and Water heroes were",
"置いていかれました。最早闇のエレメントも風の勇者も":
    "left behind. Now no one knows where the Dark Element",
"どこにいるのか分かりません。さあ二人はどうやって合流":
    "or the Wind hero are. How will those two meet up again!?",
"するのか！？次回をおたのしみに！": "Stay tuned for next time!",
"火を噴く火の紋章！ぎゃーーーーーーーーー闇のエレメント":
    "The Fire Crest breathes flame! Gyaaaaah—the Dark Element",
"は燃えました。風の紋章がカマイタチを呼び、火はもっと":
    "burned! The Wind Crest summoned a Kamaitachi, and the fire blazed",
"激しくなりました。いかん！火が凄くて闇のエレメントが":
    "even fiercer. Oh no! The flames are so intense we can't",
"よく見えない！近付くこともできません。":
    "even see the Dark Element! We can't get close!",
"吾輩は王国書記官のデアール卿であーる。":
    "I am Lord Dear, the kingdom's scribe, yessir.",
"よかったー　あれ、騎士であるあなたが":
    "Oh good~ ...but as a knight,",
"持っていても、何の役にも立ちませんし、":
    "it would be of no use to you anyway,",
"そりゃ売りますよね。　よかったー":
    "so of course you'd sell it. Oh good~",
"あー…　素材や財宝はためこんでも、":
    "Ah... hoarding materials and treasure",
"俺ら兵士や騎士には、役に立ちません。":
    "doesn't do us soldiers or knights any good.",
"お店で売ってお金に変えた方がいいですよ？":
    "Better to sell them at a shop and turn them into money, right?",
"…そうか。": "...I see.",
"なので、風のエレメントの加護で出来たお城と国である、":
    "And so—as this castle and kingdom were made through the blessing of the Wind Element—",
"これがお前の初めての戦闘任務となる。":
    "this will be your first combat mission.",
"西の監視塔に人食いの魔物が巣くっている":
    "There are reports of a man-eating monster",
"という報告があった。": "lurking in the West Watchtower.",
"この調査、そして魔物の討伐を、お前に命ず。":
    "I command you to investigate and slay the monster.",
"陛下…ウィンだけでなく、": "Your Majesty... you summoned not only Win,",
"俺のこともお呼びになられたのは？": "but me as well?",
"勿論、ウィンの初陣を助けてもらう為だ。":
    "Of course—to help Win through his first battle.",
"天才騎士と誉れの高いお前であれば、":
    "As a knight renowned as a genius,",
"新米騎士のウィンにとってこれ以上ない":
    "there could be no better support",
"助けとなるであろう。": "for the rookie knight Win.",
"…まあ、陛下のご命令とあれば…":
    "...Well, if it's Your Majesty's command...",
"仕方がありません。": "I have no choice.",
"ピピンよ。お前もひとの上に立つ立場。":
    "Pipin. You too stand in a position above others.",
"面倒臭がらずに、部下の面倒も見られるように":
    "Don't be so reluctant—learn to take care of",
"なってくれないと困る。": "your subordinates.",
"騎士ウィンよ。": "Knight Win.",
"騎士ウィン、お前にはまだ実戦経験がない。":
    "Knight Win, you have no real combat experience yet.",
"お前の働きに期待しているぞ。": "I expect great things from you.",
"下がれ。": "You may leave.",
"…すまぬが少し考え事をしているのだ。":
    "...Forgive me, but I'm lost in thought.",
"ひとりになりたい。": "I wish to be alone.",
"またの機会にしてくれ。": "Some other time, please.",
"以前サクソンに西の塔の見回りを命じたが、":
    "I ordered Saxon to patrol the western tower before,",
"あれからまだ、ひとつきも経っていない。":
    "and not even a month has passed since.",
"こんな短期間に多くの魔物が巣くうものか…":
    "How could so many monsters have nested there in so short a time...",
"恐れながら、陛下。": "If I may be so bold, Your Majesty.",
"サクソン騎士団長代行のこと、きっと報告だけ":
    "As for Acting Knight Commander Saxon, I'm sure he",
"して、見回りはしていません。":
    "only filed the report and never actually patrolled.",
"ありそうなことだ…。": "That does sound like him...",
"いつもあの者の尻拭いをさせてすまないが、":
    "I'm sorry to always make you clean up after him, but",
"ピピン、任せたぞ。": "Pipin, I leave it to you.",
"…なぜまだここにいる？": "...Why are you still here?",
"ピピン、お前の今回の仕事は、ウィンの":
    "Pipin, your task this time is to",
"サポートだ。色々と教えてやるように。":
    "support Win. Teach him everything you can.",
"お前には西の塔の調査に向かうよう命じた。":
    "You've been ordered to investigate the western tower.",
"少しは仲良くするのだぞ。": "Try to get along with each other.",
"王に向かってそうあからさまに嫌な顔をするな。":
    "Don't make such an obvious face of disgust toward your king.",
"お前なりのやり方でいいが、努力はしろ。":
    "Do it your own way if you like, but put in the effort.",
"隊長たるもの、部下の教育も仕事の内だ。":
    "As a captain, teaching your subordinates is part of the job.",
"私にはお前と雑談するような暇はないぞ。":
    "I have no time for chit-chat with you.",
"…努力します。": "...I'll do my best.",
"長話は終わりにしよう。": "Let's end this long talk.",
"陛下、それは逆ですよ。": "Your Majesty, you've got it backwards.",
"なんで俺がこいつに面倒を見られにゃならんの":
    "Why do I have to be the one looking after",
"です！": "this kid!?",
"この意味、": "The meaning of this—",
"分からないお前ではあるまい、ピピン！":
    "surely even you understand, Pipin!",
"いや、分かりませんが…": "No, I don't understand, but...",
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
