#!/usr/bin/env python3
"""Fill batch 29: Pipin origins book, Dark Continent lore, food book."""
import csv
import os
import re

D = {
"なんにもないが、ゆっくりしていきなさい。":
    "There's nothing here, but take your time.",
"しかし、大きくなったのう…": "My, how you've grown...",
"騎士の恰好もよく似合っておるわい。":
    "That knight's uniform suits you well.",
"『ある天才騎士の軌跡』": '"The Path of a Certain Genius Knight"',
"彼はその剣術、頭脳において、他を圧倒していた。":
    "He overwhelmed others in both swordsmanship and intellect.",
"しかし、ピピンがどこから来た男なのかを知るものは、":
    "Yet none in the knight order knew where Pipin came from...",
"騎士団にはいなかった…": "not a single one...",
"少なくとも筆者の周りに知る者はいなかった。":
    "At least, no one I knew did.",
"彼には、その能力だけでなく、ひとと違う特徴があった。":
    "Beyond his abilities, he had a feature unlike any other.",
"彼の耳は、とても細長く、とがっている。":
    "His ears were very long, slender, and pointed.",
"そのような耳をした者を、我々は他に見たことがない。":
    "We've never seen anyone else with ears like that.",
"彼は一体、何者なのか。どこからやってきたのだろうか…。":
    "Just who is he? Where did he come from...?",
"天才と呼ばれる騎士がいる…":
    "There is a knight called a genius...",
"呼ばれるだけでなく自分でもそう呼ぶのだが…":
    "and he calls himself that, not just others...",
"その男の名を、ピピンという。": "That man's name is Pipin.",
"騎士になったってのに、それじゃあ":
    "Even as a knight, that's just—",
"あら、ウィン。今日はどうしたの？":
    "Oh, Win. What brings you today?",
"いままでと変わらないじゃないの…。":
    "You haven't changed a bit, have you...",
"はたらきなさいよ。": "Go on, work.",
"そういうのはいいから。": "Enough of that.",
"どうせなんとなくヒマでぶらぶらしている":
    "You're just wandering around bored",
"だけなんでしょう？": "anyway, aren't you?",
"小麦粉か何かが入っている": "It contains flour or something of the sort.",
"『暗黒大陸』": '"The Dark Continent"',
"大昔にセイリューの南から暗黒大陸への橋が作られたが、":
    "Long ago, a bridge to the Dark Continent was built south of Seiryu, but",
"そこから大量の恐ろしい魔物が雪崩れこんだ。":
    "a flood of terrifying monsters poured across it.",
"そして橋を渡って向こう側へ行ったものはみな病気になって":
    "And all who crossed the bridge to the other side fell ill",
"すぐに死んでしまった。": "and died soon after.",
"それ以来、橋は落とされ、誰もその土地へ行こうと":
    "Since then, the bridge was dropped, and no one has tried",
"しなくなった。": "to go there.",
"いまではその地の存在を知る者も稀である。":
    "Now, few even know that land exists.",
"この大陸のずっと南…": "Far to the south of this continent...",
"かつて暗黒大陸と呼ばれていた土地がある。":
    "there is a land once called the Dark Continent.",
"そう呼ばれるようになった理由は、":
    "It came to be called that because",
"恐ろしい魔物がたくさんおり、そして空気が毒だからだ。":
    "it teems with terrible monsters, and its very air is poison.",
"たくさんの手紙だ。": "A great many letters.",
"国内宛ての手紙だけではなく、フレイム王や":
    "Not just letters addressed within the kingdom—some are",
"セイリューの領主に宛てたものまである":
    "addressed to King Flame and the lord of Seiryu.",
"いい匂いがする　お茶の葉かもしれない":
    "It smells nice—might be tea leaves.",
"調べているところを見られたら大変だ":
    "It'd be trouble if someone caught me looking.",
"『歴代騎士団長』": '"The Knight Commanders of Old"',
"筆者が把握している歴代団長の名とその実績を":
    "Looking over the names and deeds of the commanders",
"俯瞰してみても、大体その通りである。":
    "I know of, it holds true by and large.",
"ただ、現騎士団長であるロイ団長は、騎士団長の証である":
    "However, Commander Roi was special: in a crisis during his childhood,",
"紋章を、幼い頃に危機的状況において半ば強制的に":
    "he was half-forced to inherit the crest, the mark of the Knight Commander.",
"継承された点において、特別であった。":
    "That made him an exception.",
"ウィンダム騎士団の団長の選出基準であるが、":
    "As for how the Windam Knight Order selects its commander—",
"主に能力（戦闘技術、実務能力、学問など）で候補となり、":
    "candidates are primarily chosen by ability (combat skill, practical competence, scholarship, etc.),",
"それに実績を加味した上で選出されることが多い。":
    "and then selected with their achievements also weighed in.",
"『世界の美味しいごはん』": '"Delicious Food of the World"',
"カレーは辛いのに食べるのをやめることが出来ず、":
    "Curry is spicy, yet you can't stop eating it;",
"辛みの中にも色々な野菜のうま味が凝縮されており、":
    "the savor of many vegetables is concentrated within the heat,",
"とても美味だという。しかも、カレーには色々な種類が":
    "and it's said to be delicious. What's more, there are many kinds—",
"あり、赤いのや、黄色いの、みどり色のもあるという。":
    "red, yellow, even green ones.",
"そしてもうひとつが、セイリューでしか育てられない":
    "Another is rice—a grain that can only be grown",
"コメという穀物を蒸したもの。": "in Seiryu—steamed.",
"もちもちとした食感の中に、みずみずしく爽やかな甘みが":
    "Within its chewy texture is a fresh, refreshing sweetness",
"凝縮されているという。": "concentrated, they say.",
"そしてその蒸したコメを手で丸めた携帯食…":
    "And the portable food made by shaping that steamed rice by hand—",
"ライスボールが何よりも有名だ。": "the Rice Ball—is the most famous of all.",
"絶品の味なのに、持ち歩くことができ、しかも歩きながら":
    "It tastes exquisite, yet you can carry it, and even eat it",
"でも食べられることから、旅人たちの憧れである。":
    "while walking—making it the envy of travelers.",
"たくさんのひとがよく挙げるものには以下がある。":
    "The foods most people name are the following.",
"フレイム王国のカレー、": "The Flame Kingdom's curry,",
"そして、セイリューのライスボール…その主原料である":
    "and Seiryu's Rice Balls... that is, the rice,",
"コメである。": "their main ingredient.",
"『わたしのゆめ』": '"My Dream"',
"だけど、もじをおぼえるのは　たいへんです":
    "But learning letters is hard work.",
"たいへんだから　あまり本をかいたり　よんだりするひとが":
    "Because it's hard, I think there aren't many people",
"せかいには　すくないと　おもいます":
    "in the world who write or read books.",
"だからわたしは　しょうらいだれでももじをおぼえられる":
    "So in the future, I want to write easy-to-understand books",
"かんたんで　わかりやすい　本を　かきたいです":
    "that anyone can use to learn their letters.",
"そして　もっと　せかいのれきしを　みらいにのこせる":
    "And I hope I can leave more of the world's history",
"ように　できたらいいなとおもいます":
    "for the future.",
"わたしのゆめは　本をかくことです。":
    "My dream is to write books.",
"わたしは本がだいすきです。": "I love books.",
"しらないことが　たくさんわかるからです。":
    "Because they teach me so many things I didn't know.",
"またのご来店をお待ちしております！":
    "We look forward to your next visit!",
"どうぞ今後もごひいきに！！":
    "Do continue to patronize us!!",
"当店のポーションは効き目抜群です！！":
    "Our potions are extremely effective!!",
"どうぞお買い求めください！！":
    "Please do give them a try!!",
"底に何かのカギがあった": "There was some kind of key at the bottom.",
"大事な物だと思って元に戻した":
    "It seemed important, so I put it back.",
"ウィンは本棚から100Gのへそくりを見つけた！":
    "Win found 100G of hidden savings in the bookshelf!",
"ウィンは黙ってへそくりを元にもどした…":
    "Win silently put the hidden savings back...",
"干した果物類が入っている": "It's full of dried fruits.",
"ああ…　本当にこの国の騎士は市民を":
    "Ah... do the knights of this kingdom truly intend",
"守るつもりがあるのだろうか…。":
    "to protect the citizens...?",
"おお、騎士様！": "Oh, Sir Knight!",
"私の娘の救助は？行って下さるのですか！？":
    "What of my daughter's rescue? Will you go!?",
"…俺たちは陛下直々の任務を遂行中だ。":
    "...We're carrying out His Majesty's direct orders.",
"人助けなら他の奴に頼め。":
    "Ask someone else for your charity work.",
"ショックポーションを　１個　貰った！":
    "Received a Shock Potion!",
"なんだ、違うんですか。": "What, it's not that?",
"じゃあ何しに来たんですか？": "Then why did you come?",
"娘が無事に帰って来ました！": "My daughter came home safe!",
"騎士様がお助け下さったのですね！？":
    "The Sir Knight saved her, didn't he!?",
"これはささやかでお礼です。": "This is a small token of thanks.",
"よかったらお使い下さい。": "Please use it if you'd like.",
"これからは娘がうっかりキノコを食べて":
    "From now on, I'll make sure my daughter doesn't",
"暴れないように気を付けさせます。":
    "carelessly eat mushrooms and go wild.",
"なあに、娘はそろそろ帰ってきますとも。":
    "Oh, my daughter will be home any moment now.",
"ハリスは心配し過ぎなんですよ。":
    "Harris worries too much.",
"あの砂漠の戦士が戦の前に食べるという…？":
    "That mushroom the desert warriors eat before battle...?",
"それを食べて娘はすごく強くなっていた":
    "So eating it made my daughter incredibly strong",
"んですか！？": "did it!?",
"私も食べたかった…": "I wanted to eat it too...",
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
