#!/usr/bin/env python3
"""Fill batch 07: remaining freq>=3 dialogue lines (corrected single-line keys).

MV 1.6.1 stores each message line as a separate 401 command, so keys never
contain \\n control codes.
"""
import csv
import os

D = {
"ピピンと一緒なら、ウィンも色々勉強に":
    "With Pipin alongside you, Win will learn a great deal.",
"なるだろう。ピピン、ウィンをよろしくな。":
    "Pipin, take good care of Win.",
"人食いの獣が住み着いたっていう、":
    "A man-eating beast has moved in there, you said?",
"西の監視塔か。": "The West Watchtower, huh.",
"ここから先は、ウィンダム王とお妃さまの":
    "Past here are the bedchambers of King Windam and his queen...",
"寝室だぜ　…って、": "hey, you know—",
"なんだなんだ、騎士学校トップで卒業した":
    "What's this? You graduated top of the knight academy,",
"お前が、そんなパッとしない顔して。":
    "and you're wearing such a dull face.",
"そりゃあよかった！俺はお前ならきっと":
    "Glad to hear it! I'm sure you'll",
"騎士団長になると思ってるんだ。":
    "become Knight Commander one day.",
"どうしたんだ？ここは通行手形がないと":
    "What brings you here? Without a permit,",
"騎士でも通ることはできないぞ。":
    "even knights can't pass this way.",
"あにきが本を読みまくってすげえあたまいいのは":
    "Big bro reads tons of books and is super smart.",
"オレだってわかってる": "Even I know that.",
"ポケットに入っていたカラカラに乾いたパンを差し出して":
    "When I offered him the bone-dry bread from my pocket,",
"みると…物乞い、いや、彼は、僕に頭をさげてありがとう、":
    "he bowed his head and thanked me—",
"乾いたパンひとつで殺人者が刹那に善人になったのだ。":
    "With a single dry piece of bread, a murderer became a good man in an instant.",
"この任務を良い機会とし、ピピンから多くを":
    "Use this mission as a good opportunity to learn much from Pipin.",
"学ぶのだ。よいな…　下がれ。":
    "Understood... You're dismissed.",
"なあ、もしつらいことがあったら、":
    "Hey, if something's weighing on you,",
"ひとりで抱え込むんじゃないぞ…？":
    "don't shoulder it alone, alright...?",
"しかし、ウィン、お前なんだか顔つきが":
    "But Win, your expression seems different",
"変わったな…。": "somehow...",
"野盗が増えとると兵たちは一年中言うとるが、":
    "The soldiers talk all year about how the bandits are increasing,",
"別にいまはじまったことじゃない、昔から":
    "but it's nothing new—since long ago",
"一定数おるんじゃ。":
    "there's always been a steady number of them.",
"急ぎ、西の森に住むロイを訪ね、事の次第を":
    "Hurry to the western forest, visit Roi who lives there,",
"伝え、城に出てくるよう説得するのだ。":
    "tell him what's happened, and persuade him to come to the castle.",
"てめえウィン…俺がちょっと目を離したスキに":
    "You little—! Win... while I wasn't looking,",
"なに勝手に読んでんだよーーー":
    "what are you reading on your own!?",
"やっぱ兄貴はすげえ…　何がすげえのかは":
    "Big bro really is amazing... I can't quite say what's so amazing,",
"よく分からねえんだが…やっぱ兄貴はすげえ。":
    "but big bro really is amazing.",
"本来次期国王は、紋章を継承したあとにすぐ":
    "Normally, the next king must, right after inheriting the crest,",
"南の遺跡へひとりで赴き、試練を果たさねば":
    "journey alone to the Southern Ruins and complete the trial",
"ならん…": "—that's the rule...",
"しかし最近南の遺跡に魔物が増えたのと、":
    "But with monsters increasing in the Southern Ruins lately,",
"何より王子が死んでしまうのを恐れて、":
    "and above all fearing the prince might die,",
"王は今回の試練を見送るつもりだったのだ…":
    "the king intended to skip the trial this time...",
"狩場に魔物が出まくってて、しばらく":
    "Monsters are swarming the hunting grounds, so for a while",
"ここは通行止めにさせてもらってる。":
    "this way's closed to traffic.",
"まだ村まで結構遠いし、魔物も出るから":
    "The village is still pretty far, and monsters appear, so",
"気を付けてねー": "be careful now~",
"こうやってまた、たまには顔見せに来てよね、":
    "Come show your face once in a while, okay,",
"ナガレ。": "Nagare?",
"ああ、それならオレとウィンの紋章を":
    "Oh, that's because my crest and Win's",
"光らせてるからだ。": "are shining.",
"任務に取り掛かる前に、支給品を受け取るのを":
    "Before you start your mission, don't forget to",
"忘れるなよ。": "pick up your provisions.",
"ウィンさん、魔物をたおしたときにたまに":
    "Win, sometimes when you defeat monsters,",
"手に入る、魔物の素材とか財宝…":
    "you get monster materials or treasure...",
"西の監視塔なら、毎月サクソン団長代行が":
    "As for the West Watchtower, Acting Commander Saxon",
"見回りを命じられているはずだからな。":
    "should be ordered to patrol it every month.",
"確かに前回の見回りでは異常なかったのだ！":
    "It's true that nothing was abnormal during the last patrol!",
"魔物どころか、ねずみ一匹さえ、クモ一匹さえ":
    "Not a single monster—not even one mouse,",
"いなかったのだ！！": "not even one spider!!",
"もしかすれば、闇のエレメントの復活が":
    "Perhaps the revival of the Dark Element is",
"近いのかも知れぬ…": "near...",
"ん？西の監視塔に人食いの魔物が出たから":
    "Hm? A man-eating monster appeared at the West Watchtower, so",
"調査に行く、だと…？": "you're going to investigate...?",
"自分の能無しを、おとぎ話で誤魔化すなんて、":
    "Covering up his own incompetence with fairy tales—",
"恥知らずにもほどがある。":
    "the shamelessness knows no bounds.",
"南の国のフレイムや、西の山奥のセイリューでは、":
    "In the southern land of Flame and in Seiryu, deep in the western mountains,",
"辺境の田舎に、いつのまにか大きな城が建っていて":
    "it's said that great castles suddenly rose in remote countryside,",
"王国が出来ていたので驚いたと伝わっている。":
    "and kingdoms were born before anyone could be surprised.",
"そういう噂が、ウィンダム王国以外でもそれなりに":
    "Such rumors are believed to a fair degree",
"信じられている。": "outside the Windam Kingdom as well.",
"大昔からある国だと伝わるが、実際にどのくらい大昔から":
    "The kingdom is said to have existed since ancient times, though",
"あるのかは、あまりよく分からない。":
    "how ancient exactly isn't well known.",
"色々な本や言い伝えから、500年くらい前には、":
    "From various books and legends, it seems that around 500 years ago,",
"国王がいて、兵士がいて、街があったらしい。":
    "there was a king, soldiers, and a town here.",
"この戦いで大手柄を挙げることで、あのロイを差し置いて":
    "If I distinguish myself in this battle, ahead of that Roi,",
"わしが騎士団長になれないものか…。ううむ。":
    "perhaps I can become Knight Commander... Hmm.",
"代々何度も騎士団長、そして風の紋章を受け継いできた":
    "My family has inherited the position of Knight Commander and the Wind Crest",
"我が一族…。わしもその栄誉が欲しかったのに、あのロイ":
    "for generations... I too wanted that honor, but because of that man Roi,",
"とかいう男がいるせいで…。悔しい。": "How frustrating.",
"ウィンよ。直ちにお前が継承者になった事を":
    "Win. Report your succession to King Windam at once,",
"ウィンダム王に報告し、そののち、": "and afterwards,",
"急いでフレイム王国とセイリューに向かえ。":
    "hurry to the Flame Kingdom and to Seiryu.",
"闇のエレメントに対抗するには、":
    "To stand against the Dark Element,",
"火、水、風、全ての紋章の力が必要なのだ。":
    "the power of all the crests—fire, water, and wind—is needed.",
"いやー困りました。": "Oh dear, this is a problem.",
"まさかセイリューの橋が壊れるなんてね。":
    "I never expected the Seiryu bridge to break.",
"虫の知らせみたいなの感じるなあ。":
    "I have a sense of foreboding...",
"もし品を気に入ったら、また来てください。":
    "If you like anything, please come again.",
"壊れていた橋が直ったらしいです。":
    "It seems the broken bridge has been repaired.",
"よかった…これで帰ることができる…":
    "Thank goodness... now I can go home...",
"あそこの店からいい匂いがするんだー":
    "That shop over there smells great!",
"くんくん　何の匂いかわからないけれど":
    "sniff sniff... I can't tell what it is,",
"うまそうな匂いだぜー！": "but it smells delicious!",
"魔物が増えたってんで、最近は行商人も":
    "With monsters on the rise, even the peddlers",
"めっきり来なくなったなあ。": "have stopped coming lately.",
"…ックーン": "...Yip",
"どけちー！！": "Move it!!",
"なんで1Gも渡せないんだよドケチーーー！！！":
    "Why can't you spare even 1G, you cheapskate!!?",
"考えてみろよ　その1Gもらったら俺がどんだけ":
    "Think about it—if I got that 1G, just how happy",
"よろこぶとおもうんだ？": "do you think I'd be?",
"にーちゃーん": "Big bro!",
"あんたのこと神様だと思うぞ！":
    "I'll think of you as a god!",
"お前のたったの1Gが俺にわたすだけで":
    "Just by giving me a single 1G of yours,",
"お前を神様にするんだぞ！？": "you'd make yourself a god, you know!?",
"その価値がわからないのかお前はーーーー！！":
    "Can't you see that value!?",
"少しでいいからお金めぐんでくれなーい？":
    "Could you spare a little money?",
"あっす": "Yo.",
"なんか今年は特に暑い気がしないか？":
    "Don't you think it's especially hot this year?",
"あたしの気のせいかねえ…": "Or maybe it's just me...",
"あんまり活気がないって？": "Not much hustle and bustle, you say?",
"みんな暑くて外に出たがらないのよ。":
    "Nobody wants to go outside in this heat.",
"お天気なのにもったいないと思わない？":
    "Don't you think it's a waste, with such nice weather?",
"最近スパイスが高いわねーーー": "Spices are so expensive lately...",
"野菜も高いし…　なのに使えるお金は":
    "Vegetables are pricey too... yet the money we can spend",
"変わらないし…": "never changes...",
"ありがとうとと呟き、涙を流しながらひざまづいたのだ。":
    'He murmured "thank you" and knelt down, tears streaming down his face.',
"私も試練には反対したのだが…": "I opposed the trial as well, but...",
"ホノオ王子は勝手に行ってしまった。":
    "Prince Hono went off on his own.",
"まったく…思慮の浅いお方で頭が痛い…。":
    "Good grief... that thoughtless boy gives me a headache...",
"サクソン殿！": "Lord Saxon!",
"………えっ？": "......Huh?",
"見たことのない薬類が入っている":
    "It's full of medicines I've never seen before.",
"おう！": "Oh!",
"…え？": "...Huh?",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "dialogue.tsv"))


def norm(s):
    return s.strip(" \u3000")


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
