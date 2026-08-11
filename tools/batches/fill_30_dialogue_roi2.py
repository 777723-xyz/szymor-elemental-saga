#!/usr/bin/env python3
"""Fill batch 30: mushroom search, restaurants, Roi's inheritance ceremony."""
import csv
import os
import re

D = {
"騎士様、お仕事の報告はちゃんとしてください。":
    "Sir Knight, please file proper reports on your work.",
"ほら、あたしの言った通りジャクリーンは":
    "See, just as I said, Jacqueline",
"教えてくれないなら、騎士団に報告しますよ。":
    "If you won't tell me, I'll report this to the knight order.",
"無事に帰って来ましたよ。": "She's come home safe.",
"えっ、騎士様が助けてくれたんですか！":
    "Huh, the Sir Knight saved her!",
"それはどうもありがとうございました！":
    "Thank you so much!",
"え、キノコ…？騎士様それは一体どんな":
    "Huh, a mushroom...? Sir Knight, what kind of",
"キノコだったんですか！？": "mushroom was it!?",
"あっ、この度はどうもお世話になりました…":
    "Ah, thank you so much for your help...",
"いまでも自分がどうなっていたのか、":
    "Even now, I can't quite remember",
"よく思い出せませんが…でも元気です！":
    "what came over me... but I'm fine now!",
"手の込んだ作りのブローチがある":
    "There's an intricately crafted brooch here.",
"贈り物だろうか": "It might be a gift.",
"ここでご飯を食べると、":
    "When I eat here,",
"早く家に帰りたくなるんだ。": "I start wanting to hurry home.",
"フッ…": "Heh...",
"僕はこの店ではコーヒーしか飲まないんだ。":
    "I only drink coffee at this establishment.",
"暗い顔でフォークやスプーンを":
    "All the while glancing sidelong at the poor citizens",
"口元に運んでいる、哀れな市民たちを横目にね":
    "carrying forks and spoons to their lips with grim faces.",
"ぐーーーーーーーーー（お腹の音）":
    "GRRRRR (stomach growling)",
"半分くらいつぶれている野菜だ":
    "Vegetables, about half of them crushed.",
"小麦粉か何かだと思う": "I think it's flour or something.",
"食器がたくさん入っている": "It's full of dishware.",
"美味しそうなお酒がたくさん入っている":
    "It's full of delicious-looking liquor.",
"ありがとうございます、すぐに用意しますよ。":
    "Thank you, I'll have it ready right away.",
"また食べにおいでね、ウィンくん…":
    "Come eat again, Win...",
"じゃなかった、騎士様！": "I mean, Sir Knight!",
"いらっしゃい！あらあら騎士様じゃないか！":
    "Welcome! Oh my, if it isn't the Sir Knight!",
"おやおや、お金が足りないみたいだね…。":
    "Oh dear, it seems you're short on money...",
"大丈夫かい、ウィン君？": "Are you alright, Win?",
"ちゃんとお給金はもらえているのかい…？":
    "Are you being paid properly...?",
"食べていくかい？": "Care to eat?",
"そうですか、": "I see,",
"じゃあまた今度食べに来て下さいねえ。":
    "then please come eat another time.",
"ウチの名物ランチ、全員で50Gになりますよ。":
    "Our signature lunch is 50G for the whole party.",
"何に使うのか　石がたくさん入っている":
    "It's full of stones—for some purpose.",
"少し変なにおいのする水だ": "Water with a slightly odd smell.",
"うーん…すごくお腹が減っていたんだが…":
    "Hmm... I was really hungry, but...",
"もういいかなあ": "maybe I'll pass.",
"……うーむ": "......Hmm",
"まあ、お腹はふくれたかなあ…":
    "Well, my stomach's full, I suppose...",
"ひとつだけ傷薬をもらっていくことにした！":
    "I decided to take just one Healing Herb!",
"備蓄された薬類がある": "There are stockpiled medicines here.",
"いや、パン屋の息子のお前になれて":
    "No way—if the baker's son can do it,",
"僕になれないわけないだろ…？": "then there's no way I can't, right...?",
"そうだろー　なあ　そうだろー":
    "Right~? Huh, right?",
"あっ、ウィン！じゃなかった騎士ウィンどの！":
    "Oh, Win! I mean, Sir Knight Win!",
"ぼくでも騎士になれるかなあ？":
    "Do you think I could become a knight too?",
"寝る前には勉強してるし…": "I study before bed...",
"筋トレも毎日かかしていないし…":
    "and I do my muscle training every day...",
"何か他にアドバイスあったら教えてくれよな？":
    "Got any other advice for me?",
"まず、敵の急所を点で突けるのが一番に違い。":
    "First, nothing beats being able to strike an enemy's vital point with pinpoint precision.",
"会心率が高く、防御力の高い敵に特に":
    "It's especially effective against enemies with high",
"有効だ。": "defense and critical rates.",
"重いのが嫌なら、レイピアやダガーもいい。":
    "If you dislike heavy weapons, a rapier or dagger works too.",
"そうか、うん。": "I see, yeah.",
"皆が剣ばかり使っている中で、すでに":
    "While everyone else uses only swords, you've already",
"ん、ウィン？": "Hm, Win?",
"槍の良さに": "noticed the merits",
"気付いているとはな。さすがだ。": "of the spear. Impressive.",
"君も槍よりも剣を使うかい？":
    "Do you prefer the sword to the spear as well?",
"君もか…": "You too, huh...",
"最近は皆、すっかり剣しか使わないが、":
    "Lately everyone uses nothing but swords, but",
"槍は有効な武器だぞ。": "the spear is a fine weapon.",
"キノコを採りに行ったらしいんだが、":
    "She went out to gather mushrooms, apparently, but",
"もう丸一日戻ってきていないらしい。しかし、":
    "she hasn't come back for over a day now. However,",
"人手が足りなくてすぐに捜索隊を出せない。":
    "we're too short-handed to send a search party right away.",
"もしよかったら見てきてくれないか？":
    "If you wouldn't mind, could you go look?",
"ウィンじゃないか。": "If it isn't Win.",
"助かるよ。きっと足をくじいたとか、そんな":
    "Thanks. I'm sure she just twisted her ankle or something, but...",
"ことだろうとは思うんだが…。お前が引き受け":
    "I'll let Harris know that you've",
"てくれたと、ハリスさんにも伝えとくよ。":
    "agreed to take it on.",
"何を勝手に面倒なこと引き受けてるんだ！？":
    "Why are you volunteering for troublesome tasks on your own!?",
"陛下から直々に下された任務があるだろ！":
    "You have a direct order from His Majesty, don't you!",
"行くなら、ひとりで行くんだな。":
    "If you're going, you're going alone.",
"こんなところで油売ってていいのか？":
    "Should you really be slacking off here?",
"俺は知らん…。": "I don't care...",
"そうだよなあ…。": "You're right...",
"とりあえず、俺の方でかき集めてみるよ。":
    "For now, I'll try to scrape together what I can on my end.",
"無理を言って悪かったな。":
    "Sorry for asking too much.",
"ここの仕事は俺たちに任せて、お前は自分の":
    "Leave the work here to us, and focus",
"任務に集中しろ。": "on your own mission.",
"なあに、心配すんなって…。":
    "Ah, don't worry about it...",
"いやあ、ちょっとな…": "Well, it's just...",
"ハリスさんちの娘さんが南の旧坑道へ":
    "Harris's daughter headed to the Old Southern Mine",
"チェインメイルを　１着　貰った！":
    "Received a Chain Mail!",
"チェインメイル(匠)を　１着　貰った！":
    "Received a Chain Mail (Master's)!",
"貯蓄用の飲料水だと思う": "I think it's drinking water stored up.",
"王国の騎士団のリストが入っている":
    "It contains a list of the kingdom's knight order.",
"俺のやり方が悪かったことは、分かっている…":
    "I know my methods weren't right...",
"さあ、手を差し出せ。": "Now, hold out your hand.",
"風の紋章を、お前に継承する。":
    "I hereby pass the Wind Crest to you.",
"ウィンは左手をロイに差し出した":
    "Win held out his left hand to Roi.",
"よし、そのまま、しばらくじっとしていろ…。":
    "Good, now stay still for a while...",
"ロイは自分の手のひらをウィンの手の甲にのせた":
    "Roi placed his palm upon the back of Win's hand.",
"…無事に、継承できたようだ。":
    "...It seems the succession succeeded.",
"おそらく、まだ自覚できるような力を":
    "You likely won't feel any power you can",
"感じることはないだろう…。": "perceive yet...",
"しかし紋章は、闇の力が強まるにつれて、":
    "But the crest is said to shine brighter as",
"その輝きを増すと言われる。": "the Dark power strengthens.",
"その力…": "That power...",
"エレメンタルパワーが、具体的に、":
    "Elemental Power—what it truly is, specifically,",
"どういった力なのかは、俺にも分からん。":
    "I don't know either.",
"紋章の力が強まったとしても…":
    "Even if the crest's power grows...",
"それは、闇の力もまた強まっている事を":
    "it also means the Dark power is growing",
"意味する。": "in turn.",
"とは言え…これは俺が古文書を調べて何とか":
    "That said... this is a reconstruction I managed",
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
