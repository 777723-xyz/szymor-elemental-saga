#!/usr/bin/env python3
"""Fill batch 14: Flame Kingdom, King Burn lore, element book, mushroom scene."""
import csv
import os
import re

D = {
"法律上では市民の財産没収などの権限もあるが、試験に":
    "Legally they can seize citizens' property, but exams...",
"動員できる兵数は我が軍の半分にもなりません。":
    "the troops they can field are no more than half of ours.",
"しかし、長期戦となった場合には、組織だった補給や":
    "However, in a prolonged war, organized supply lines and",
"騎士を中心とした兵士の練度と士気の差によって、":
    "the gap in training and morale around their knights",
"我が軍は敗北すると思われます。":
    "would likely lead to our defeat.",
"短期に集中した決戦でしか勝ち目はないでしょう。":
    "Our only chance is a decisive battle fought quickly.",
"国王陛下の命令の元、ウィンダム王国と戦争した場合に":
    "Should we go to war with the Windam Kingdom by His Majesty's order,",
"騎士団は定期的な軍事的訓練を行っており、その装備もまた":
    "the knight order trains regularly, and its equipment is",
"『バーン王』": '"King Burn"',
"砂漠の国であるフレイムは、大昔から様々な災禍に":
    "Flame, a desert nation, suffered calamity after calamity",
"見舞われ続けており、ひとびとの暮らしも、国の発展も、":
    "since ancient times, leaving both its people's lives and its growth",
"他国より遅れていたが、バーン王の築いた城壁により、":
    "behind other nations—until King Burn's walls finally",
"遂に安心して眠れる土地となった。":
    "made it a land where one could sleep in peace.",
"しかしその城壁の完成は、バーン王の使役した無数の民、":
    "But those walls were built with the blood-mixed sweat",
"無数の兵たちの、血の混じった汗によって成し遂げられた":
    "of countless people and soldiers driven by King Burn.",
"ものであった。": "That was the price.",
"歴代フレイム国王で最も優れ、最も冷酷だった王が、":
    "The greatest and most merciless king in Flame's history",
"バーン王である。": "was King Burn.",
"砂漠にはびこる野盗、毒蛇、そして砂漠オオカミ。":
    "Bandits, venomous snakes, and desert wolves plague the sands.",
"一年中吹き荒れている砂嵐…。": "Sandstorms rage all year round...",
"『我々のエレメントと呼ぶもの』": '"What We Call Elements"',
"そのエネルギーといった感覚で使っている言葉である。":
    "a word used with a sense of 'that energy'.",
"しかしこの自然というものは、火と水と風のみで成り立つ":
    "But is this nature truly built solely of fire, water, and wind?",
"世界であろうか？": "Is it?",
"この世界、自然、そして生き物の大元のエネルギーの全てが":
    "Is there any basis for thinking all the world's, nature's, and living things'",
"火と水と風のエレメントのみで成り立つと考える根拠がある":
    "root energies consist only of Fire, Water, and Wind Elements?",
"のだろうか。それ以外にもこの世界には闇のエレメントが":
    "Beyond them, a Dark Element is also thought to exist.",
"存在すると考えられている。では闇の恵みとは何か？":
    "So then, what is the Dark's blessing?",
"我々はこの土地を火と水と風のエレメントによって":
    "We believe this land was made and protected by the Fire, Water,",
"作られ守られていると考えている。それゆえに、この地を":
    "and Wind Elements. That is why we call it",
"エレメント大陸と呼ぶ。しかし、我々の使うこの、":
    "the Element Continent. But what exactly does this word",
"エレメントとは具体的に何を指す言葉なのだろうか？":
    "'element' refer to?",
"うお！？うわっ！！えっ！？": "Whoa!? Wah!! Huh!?",
"おまえもだまってねえで、なんとか言えよ！":
    "You too—don't just stand there, say something!",
"ふーん…あんた、かわいいな。": "Hmm... you're kinda cute.",
"う…うわ…そういうのはやめて…":
    "Wh-...Whoa... please don't do that...",
"それならむしろ黙っててくれ…": "Then rather, just stay quiet...",
"食事は、その一食で、あの乾いたパン何個分だろうか…。":
    "That one meal was worth how many of those dry pieces of bread, I wonder...",
"ありがとうと呟き、涙を流しながらひざまずいたのだ。":
    'He murmured "thank you" and knelt down, tears streaming down his face.',
"あんた本当アタマ悪そうな喋り方が…":
    "The way you talk really makes you sound dumb...",
"天才的だわ。": "it's genius.",
"あんだとー？": "What was that—?",
"まあ、喋り方っていうか、オレ、ホントに":
    "Well, it's not just the way I talk—I really am",
"頭悪いからな。でもズシンと来ねえかよ？":
    "dumb. But it hits you right here, doesn't it?",
"ことの経緯を説明した": "They explained the situation.",
"なんだとーーーーーーーーーーーー！！！！":
    "What did you say—!!!!",
"闇のエレメントが、本当に…": "The Dark Element, truly...",
"ただの伝説だと思っていたが…":
    "I thought it was just a legend...",
"ウィン殿。": "Sir Win.",
"火の紋章の継承者である我が息子、ホノオは…":
    "My son Hono, inheritor of the Fire Crest, is...",
"おや、これはこれは騎士どの。": "Oh, well, well, if it isn't a knight.",
"我が国伝統の継承の試練のため、南の遺跡に":
    "He's headed to the Southern Ruins for our kingdom's",
"向かったところなのだ…。": "traditional trial of succession...",
"最近のあそこは以前と違い魔物が増えたので、":
    "Lately that place has more monsters than before, so",
"本当は行かせたくなかったのだがな…":
    "I truly didn't want to let him go...",
"ただでさえ試練など中止したかったところに、":
    "I'd have liked to cancel the trial as it was, and now",
"ウィン殿からのこの報告…": "comes this report from Sir Win...",
"ああ、力ずくでも止めればよかったが、":
    "Ah, I should have stopped him by force, but",
"今更言っても詮無いことよ。": "it's no use saying so now.",
"まずは　お茶でもいかがかな？": "First, how about some tea?",
"ウィン殿、恐縮だが、そなたの力で…":
    "Sir Win, I'm ashamed to ask, but with your strength...",
"あの聞き分けのない我が息子を連れ戻して":
    "please bring back my headstrong son...",
"ほしい…。試練どころではないと分かれば、":
    "Once he realizes this is no time for trials,",
"あやつも頭を冷やすだろう。": "he'll cool his head.",
"ウィンはフレイム王に自己紹介をしてから":
    "After introducing himself to King Flame, Win",
"ウィン殿、お誘いしたお茶の時間が随分と":
    "Sir Win, I'm sorry our tea together has",
"遠のいてしまい恐縮だが…": "drifted so far away...",
"なにとぞ、息子を頼みます。": "Please, I beg you, take care of my son.",
"王子、必ず生きてお帰り下さい。": "Prince, please come back alive, I beg you.",
"お、おい…急になんかそういうのやめようよ…":
    "H-Hey... don't suddenly get all emotional...",
"ちょっと、キツイ…": "It's a bit much...",
"ホノオ王子、行かれるのですな。": "Prince Hono, so you're leaving.",
"当たり前だろ！オレは火の紋章の勇者様だぜ！":
    "Of course! I'm the hero of the Fire Crest!",
"とても、誇らしく、胸高鳴る思いです。":
    "It fills me with pride and a racing heart.",
"しかし…同時につらくてたまりません…。":
    "But... at the same time, it hurts so much...",
"よかったら世話は私にお任せください！":
    "If you like, please leave his care to me!",
"犬を見たことなかったのか…": "Have you never seen a dog before...?",
"ホノオ王子！あの犬は一体なんですか！？":
    "Prince Hono! What on earth is that dog!?",
"なにって…　犬は犬だろ？": "What? A dog's a dog, right?",
"とてもふさふさですし…": "It's so fluffy...",
"しかも賢いんですね…。": "And clever, too...",
"王子…ウィン殿たちお仲間の言うことを":
    "Prince... listen well to Sir Win and the others,",
"よく聞いて…あと…決してひとりで勝手な":
    "and above all... never take reckless action",
"行動をしないように。いいですね？": "on your own. Understood?",
"おいおい、他に言うことないか？": "Come on, is that all you have to say?",
"オレはこどもか！？": "Am I a child!?",
"あのキノコを奪い取らなければ…":
    "I must snatch that mushroom away...",
"ウィンはハリスの娘さんから、": "Win snatched",
"狂戦士のキノコを奪い取った！":
    "the Berserker Mushroom from Harris's daughter!",
"きゃあっっっ　わたしったら、いったい……？":
    "Eek!! What... what was I...?",
"よくわからないけれど、騎士様が助けて":
    "I don't quite understand, but you saved me,",
"くれたんですね…": "Sir Knight...",
"ハリスの娘さんは、血走った目でこちらを睨むと":
    "Harris's daughter glared at them with bloodshot eyes",
"雄たけびを上げた。": "and let out a roar.",
"え？キノコなんて食べてません！": "Huh? I haven't eaten any mushroom!",
"私はキノコを食べに来たのではなく、採りに":
    "I didn't come to eat mushrooms—I came to gather",
"来たのです！私は食べてませ―――――――ん":
    "them! I didn't eat anythiiiiing!",
"…その手には何やら真っ赤なキノコが握られている…":
    "...In her hand is clutched a bright red mushroom...",
"あのキノコはフレイムでのみ採れる狂戦士のキノコに":
    "That mushroom looks just like the Berserker Mushroom",
"そっくりだ…　": "that only grows in Flame...",
"…くっ": "...Hmph",
"はい、ありがとさん。": "Yes, thank you kindly.",
"またおいでー": "Come again~",
"え、客？": "Huh, a customer?",
"びっくりしたー　え？": "You startled me— huh?",
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
