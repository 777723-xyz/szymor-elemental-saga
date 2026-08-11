#!/usr/bin/env python3
"""Fill batch 43: dragon's truth, Otaki's confession, aftermath."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ただ、問題は来年からの収穫だね…":
    "The problem, though, is next year's harvest...",
"…ちょっと休ませてくれ。": "...Let me rest a bit.",
"朝からずっと外の瓦礫を片付けていて":
    "I've been clearing debris outside",
"くたくたなんだ。": "since morning; I'm exhausted.",
"そのためにも早く世界を救ってください！":
    "So for that, please save the world quickly!",
"命あってのものだねっていうからねー！":
    "After all, you need to be alive to enjoy things!",
"助けてもらったお礼に、薬の在庫は":
    "As thanks for your help, I'll sell our medicine stock",
"格安でお分けさせてもらいますよ！":
    "at rock-bottom prices!",
"慣れているからな。その点では安心ていうか…":
    "I'm used to it, so in that sense, rest easy...",
"それでダメならどっちにしたってダメさ…。":
    "If that doesn't work, nothing would...",
"きっと大丈夫さ…": "It'll surely be fine...",
"この洪水もいつまでも続かない。":
    "This flood won't last forever.",
"続けさせない…　あたしたちが！":
    "We won't let it—not us!",
"みんなに洪水のこと知らせに来てから、":
    "Ever since I came to warn everyone about the flood,",
"北に帰れなくなってしまった。":
    "I can't get back north.",
"北の村のみんなは…　大丈夫そうなのか？":
    "Is everyone in the northern village... okay?",
"この辺りの連中よりはずっと天災や魔物にも":
    "They're far better than folks around here at handling",
"…うん。オタキ様、姉さまをお願いします。":
    "...Yeah. Lady Otaki, please take care of my sister.",
"ナガレよ…": "Nagare...",
"つらい役目を任せることになってすまぬの…。":
    "I'm sorry to burden you with such a painful task...",
"しかしじゃ、おまえなら必ずや、":
    "But I have faith that you will surely",
"龍から紋章を継承し、使命を果たせると":
    "inherit the crest from the dragon and",
"信じておる…。": "fulfill your mission...",
"…わしが幼子のころには、":
    "...When I was a little girl,",
"当主が毎日お社に供え物を持って拝みに行く…":
    "the head offering tribute at the shrine every day—",
"そういう習慣は、まだなかったのじゃよ。":
    "that custom didn't exist yet.",
"そもそも、お社には誰も近づいちゃならん…":
    "In fact, no one was allowed to approach the shrine...",
"そういうしきたりだったのじゃ。":
    "that was the rule.",
"龍の元に再びひとが落ちぬようにとお社を":
    "The shrine was built so none would fall to the dragon again,",
"建てたのじゃから、それは当然じゃった。":
    "so it was only natural.",
"じゃがある日…": "But one day...",
"ああ、無事じゃ、安心せい。": "Ah, I'm fine, rest easy.",
"わしの父さまが…": "My father...",
"毎日こそこそと、お社に行き始めたのじゃ…。":
    "began sneaking off to the shrine every day...",
"誰もが不審に思ったものじゃ…。":
    "Everyone found it suspicious...",
"お社に近付いちゃならんと、普段から村の皆に":
    "The very head who was always telling the villagers",
"言って聞かせている、その当主自身が、":
    "never to approach the shrine was himself",
"毎日お社に足を運んでいるのじゃからな…。":
    "going there every day...",
"わしは一度、父さまに聞いてみた。": "Once, I asked my father,",
"なぜお社に行くのか…": "why he went to the shrine...",
"上流のものが、すぐに知らせてくれたお陰じゃ":
    "Thanks to those upstream alerting us at once,",
"村の皆に気味悪がられていても行くのか、とな":
    "'Even with the whole village finding it eerie, you still go?'",
"父さまは…しばらくわしの目をみつめて":
    "My father... gazed into my eyes for a while,",
"黙っていたが…ふと逸らして、ポツリと言った":
    "was silent... then looked away and murmured:",
"お社に不憫な子がおって": "'There's a pitiful child at the shrine,'",
"それがかわいそうなんじゃと…":
    "'and I can't bear to leave it be.'",
"それって…": "That means...",
"そのときのわしは、信じんかったよ。":
    "I couldn't believe it then.",
"不憫な子がおるなら、村に連れてくればよいと、":
    "Even as a child, I thought: if there's a pitiful child, just bring it to the village,",
"子ども心にも思ったのじゃでな。":
    "that's what I felt.",
"その明くる日じゃった…": "And it was the very next day...",
"父さまは倒れた。": "that my father collapsed.",
"布団の中で毎日みるみるうちに細うなった…。":
    "In his bed, he withered away day by day...",
"しばらくして…": "Some time later...",
"わしの兄さまが当主になった。": "my elder brother became head.",
"そして、やはり兄さまも…": "And just like Father, my brother too...",
"毎日お社に通うたんじゃ。": "began visiting the shrine daily.",
"それからは、ずーっとじゃ。": "And it continued, endlessly.",
"次の兄さまも、わしの夫も、わしの息子も…":
    "The next brother, my husband, my son...",
"みーんな、お社に通うようになったんじゃ。":
    "all of them began going to the shrine.",
"それが正式に当主のお役目になったのは…":
    "It became an official duty of the head...",
"して、ナガレ…": "and so, Nagare...",
"わしの夫の代じゃったのう。": "in my husband's generation.",
"それまでは立場が弱くて、文句を言えんでおった":
    "Until then, my position was too weak to complain,",
"わしも…　夫にはさすがに言うたのじゃ。":
    "but to my husband, I finally said it.",
"あんたらは、お社の、龍の瘴気に当てられとる":
    "'You're all being affected by the dragon's miasma",
"んじゃ。だから皆早死にするんじゃとな。":
    "at the shrine. That's why you all die young.'",
"えっ、オタキ様が！？": "Huh, Lady Otaki said that!?",
"無事に水の紋章を継承できたようじゃの。":
    "It seems you've successfully inherited the Water Crest.",
"そうじゃ！わしは言うたぞ、ナガレ。":
    "That's right! I told him, Nagare.",
"それでもじゃ…　夫はよわよわしく…":
    "And yet... my husband, frail as he was...",
"じゃが、優しい顔でこう言うた…":
    "with a gentle face, said this...",
"そうだとしても、タキ…": "'Even if that's so, Taki...",
"あの子には俺しかともだちがおらんのだ":
    "that child has no friend but me.'",
"とな…": "he said...",
"…そんな…！": "...That's...!",
"えっと…　でもよ…でも、オタキ様…":
    "Um... but still... Lady Otaki...",
"当主がバタバタと早死にする原因が、本当に":
    "Is the cause of the heads dying off so young really",
"龍のしょ…しょうき？とかなのか…？":
    "the dragon's mi—miasma...?",
"無論、証拠はない…。": "Of course, there's no proof...",
"最初に、わしにもわからんと言うたじゃろ！":
    "I told you from the start I don't know!",
"え、いや、そうだけどさー": "Huh, no, I know, but—",
"でも龍はすげーいいヤツだったぜ！？":
    "but the dragon was a really good guy!?",
"…龍は、闇の結晶だと、四天王のミケーネが":
    "...Mycenae of the Four Generals said the dragon",
"言っていた。": "was a Dark Crystal.",
"うん。だけど…龍は死んでしまった。":
    "Yeah. But... the dragon died.",
"だから、龍にそんなつもりがなくても…":
    "So even if the dragon meant no harm...",
"近くにいる人間に何らかの悪影響を与えていた":
    "it's possible it was having some adverse effect",
"っていう可能性はある…。": "on nearby humans...",
"そ、そうなのか…？": "I-Is that... so...?",
"わしも、ナガレと同じように考えたのじゃ。":
    "I too had wondered, just as Nagare does.",
"ようお帰りになられましたな、継承者の皆様。":
    "Welcome back, inheritors all.",
"殺したんじゃない…　殺したんじゃないけど…":
    "It wasn't that I killed it... not that I killed it, but...",
"じゃから、わしの代からは、":
    "And so, from my generation onward,",
"その習慣をやめたのじゃよ。": "I put an end to that custom.",
"あのままお社への参拝を続けておったら、":
    "Had we kept making pilgrimages to the shrine,",
"この家はなくなると思うたからの。":
    "I feared this house would be destroyed.",
"そうだったのか…。": "So that's how it was...",
"オタキ様…　あたし、オタキ様の考え、":
    "Lady Otaki... I think your reasoning,",
"合っていたと思います。": "was right.",
"殺したのと、同じだったかも知れない…。":
    "It may well have been the same as killing it...",
"ナガレにそう言ってもらえたなら、わしも":
    "If Nagare can say that, then I too",
"長生きした甲斐があったわい…。":
    "have lived long enough...",
"そして…それをあたしに内緒にしていたのも、":
    "And... the reason you kept it from me...",
"あたしが父さまたちが早死にしたことの恨みを、":
    "was that I'd been venting my resentment over my fathers' early deaths",
"わけも考えずただ龍の存在にぶつけていたから…":
    "at the dragon itself, without a second thought...",
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
