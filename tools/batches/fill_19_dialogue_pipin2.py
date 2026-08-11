#!/usr/bin/env python3
"""Fill batch 19: Pipin's brainwashing, storm narration, Roi's rapier."""
import csv
import os
import re

D = {
"このバケモノを俺が退治しに来てやったのさ。":
    "I've come to slay this monster in place of you and your incompetence.",
"やめたーーーーーーーー": "I'm stopping~",
"じゃあねーーーー": "Later~",
"四天王ダフィールをも、きっと倒せますぞ！！":
    "We can surely defeat even Dafill, one of the Four Generals!!",
"ぐぬぬ…": "Grrr...",
"陛下…　構いませんな？": "Your Majesty... you don't mind?",
"へーーーーー！！": "Ohhh—!!",
"キミが？　そっちの金色のが継承者ー？":
    "You? The gold-haired one over there is the inheritor?",
"…そこまでだ、バケモン": "...That's enough, monster.",
"そんでー？　ナニナニ？？": "So—? What, what??",
"そっちの赤いのが…": "The red one over there is...",
"てんさい…　きし…？　　　　ハ？？？":
    "a genius... knight...? Wha???",
"よくわかんないけどーーーーー":
    "I don't get it, but~",
"ふつうの人間なワケねー": "there's no way he's an ordinary human~",
"フン！": "Hmph!",
"それなら…　俺が普通かどうか、試してみろ！":
    "Then... try me, and see if I'm ordinary!",
"いやいやいや　だはははは！！":
    "No no no— bahahaha!!",
"えーーー？　継承者は　ひとり？":
    "Hmm? Only one inheritor?",
"ひとりだけーーーーーー？？？":
    "Just one—??",
"ウィン！　おまえだけなのか！？":
    "Win! Are you the only one!?",
"継承者がウィンだけでも…": "Even with only Win as the inheritor...",
"ピピンもいるのだ！　負けるわけがないわい！":
    "Pipin is here too! There's no way we'll lose!",
"それは違う…！　ピピン…！": "That's not it...! Pipin...!",
"もしお前が大事なものを奪われたとしたなら…":
    "If someone took what you hold dear...",
"それを奪ったのは俺だ…　ウィンではない！！":
    "then I'm the one who took it... not Win!!",
"この子とは…　一体…？": "This one here... who is she...?",
"…貴様はウィンの次だ。": "...You're next after Win.",
"そこでおとなしく首を洗って待っていろ。":
    "So wash your neck and wait there patiently.",
"くっ…　ピピン…！": "Guh... Pipin...!",
"ピピンを倒せ！　ウィン！！":
    "Defeat Pipin! Win!!",
"殺してもかまわん！！": "You may kill him!!",
"…陛下！　ピピンは操られているのです！":
    "...Your Majesty! Pipin is being controlled!",
"ピピンは正気なら、決してこのようなことを":
    "If Pipin were in his right mind, he would never",
"する男ではありません！！": "do something like this!!",
"だからといってどうせよと言うのだ！":
    "Even so, what would you have us do!",
"このままではウィンも、我々も殺されるのだ、":
    "As things stand, both Win and the rest of us will be killed.",
"ウィンよ！　紋章の力を持つお前なら、":
    "Win! With the power of the crest, you",
"ピピンを倒すこともできるはずだ…":
    "should be able to defeat Pipin...",
"ウィンよ、ピピンを倒すのだ！！":
    "Win, defeat Pipin!!",
"くっ…！": "Guh...!",
"なにか…　なにか手はないのか…！":
    "Isn't there... isn't there any way...!",
"…お喋りは終わったか？": "...Done talking?",
"なら、始めさせてもらう。": "Then let me begin.",
"ウィン…　死ねえええええええええ！！":
    "Win... DIEEEEEE!!",
"ウィンは力いっぱいピピンを抱きおさえた！":
    "Win grabbed Pipin and held him with all his might!",
"……ウィン、どの…！": "......Win, you...!",
"…どけっ！！": "...Get off!!",
"…む！まだ操られているのか…！？":
    "...Hm! Still under control...!?",
"…操りの術は解けたようだな、ピピン…":
    "...It seems the control spell has lifted, Pipin...",
"…俺に触るな…！！": "...Don't touch me...!!",
"…もう、ほっといてくれ　ウィン…":
    "...Just leave me alone, Win...",
"消えた…！": "He's gone...!",
"あの日から始まった嵐と魔物の度重なる襲来は":
    "The storms and monster attacks that began that day",
"それから一週間を過ぎても": "showed no sign of letting up",
"治まることはなかった": "even a week later.",
"ウィンダムには風と雷が…":
    "Wind and lightning struck Windam...",
"セイリューには大雨と洪水が…":
    "heavy rain and floods struck Seiryu...",
"フレイムには燃え盛る岩の雨が…":
    "and rain of burning rocks struck Flame...",
"連日のように襲い掛かっていた": "day after day.",
"これらの異常気象が": "Even knowing these unnatural weathers",
"闇のエレメント復活によるものだとは分かりながらも":
    "stemmed from the Dark Element's revival,",
"我々はどうすればよいのか分からなかった…":
    "we had no idea what to do...",
"継承者たちの紋章の輝きは増していた":
    "The inheritors' crests shone ever brighter,",
"それはいまも尚、闇の力が": "proving that the Dark Element's power",
"強まり続けていることを示していた":
    "was still growing stronger.",
"しかし、あの日以来": "And yet, since that day,",
"闇の四天王が現れる事もなく":
    "the Four Dark Generals never appeared,",
"我々はいたずらにときを": "and we only let the time slip",
"失い続けていた…": "away in vain...",
"まさか…　ピピン…！！": "No way... Pipin...!!",
"あやつ…なにかおかしなことを言い捨てて…":
    "That guy... spat out something strange and...",
"横取りしてくれたなあ…　ウィン………ッ！！":
    "you stole it from me... Win......!!",
"な、なんてことだ…　ピピンが…":
    "Wh-What a disaster... Pipin has been...",
"操られたというのかーーーーーー！！？？":
    "controlled—!??",
"ザコどもは俺の邪魔をするなよ…":
    "Stay out of my way, you small fry...",
"この子がみんなを楽しませる、と…":
    "She said this one would entertain everyone...",
"俺の獲物は…　貴様だけだ…ウィン":
    "My prey... is only you... Win.",
"ときは来た！　もはや語るべきことはない！":
    "The time has come! There's nothing left to say!",
"紋章の勇者たちよ　ゆけい！！":
    "Heroes of the crests, go forth!!",
"これは若い頃に名工が俺の為に鍛えてくれた":
    "This rapier was forged for me by a master smith in my youth,",
"レイピアなんだが…": "but...",
"レイピアとしてはとても重く大きく、":
    "it's far too heavy and large for a rapier, and",
"俺にはついぞ扱い切れないまま…":
    "I could never quite handle it...",
"そして剣を握れなくなってしまった。":
    "And then I lost the ability to hold a sword at all.",
"ウィン、お前に譲りたいものがある。":
    "Win, there's something I want to pass on to you.",
"しかしいまのお前なら…": "But with you as you are now...",
"きっとこの剣の強さを引き出せるかも知れん。":
    "you might just be able to bring out this blade's true strength.",
"良かったら受け取ってくれ。":
    "Please take it, if you'd like.",
"暗黒大陸には、強力な魔物と毒以外にも、":
    "On the Dark Continent, beyond its powerful monsters and poisons,",
"他にどんな脅威があるのか誰も知らない。":
    "no one knows what other threats await.",
"…細心の注意を払って臨んでいただきたい。":
    "...Please approach with the utmost caution.",
"ていうかさー": "Speaking of which~",
"すまんが、そうだ。": "I'm sorry, but yes.",
"信用していないわけじゃない。":
    "It's not that I don't trust you.",
"そこはご理解いただきたい、殿下。":
    "I'd ask you to understand that, Your Highness.",
"お、　おお…？": "O-Oh...?",
"おい、別に王の部屋でなくとも、":
    "Hey, this doesn't have to be the king's room—",
"単純にプライベートの空間だ。":
    "it's simply a private space.",
"なぜ入ろうとする？": "Why are you trying to come in?",
"ウィンや、オレらでもか？":
    "Even us, Win and me?",
"お前たちのために一級品の品だけは、":
    "For you lot, I've set aside only the finest goods,",
"俺の独断で抑えてある…。": "on my own judgment...",
"でも金だけは持ってきてくれよな。":
    "But bring money, alright?",
"無料の支給品はもう当分回せないと思ってくれ":
    "Consider it understood that free provisions won't come around for a while.",
"すまんな、これでも俺は全体を見てちゃんと":
    "Sorry, but I do look at the big picture and",
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
