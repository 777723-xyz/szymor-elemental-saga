#!/usr/bin/env python3
"""Fill batch 12: buckler book, Flame desert crossing, Pikepike intro."""
import csv
import os
import re

D = {
"この世界の武器や防具は、種類自体はすくないが、":
    "The weapons and armor of this world are few in type, but",
"品質によって、普通のものや、優れたものが存在する。":
    "depending on quality, there are ordinary and excellent pieces.",
"当然、品質の良いものほど強力だったり頑丈だったり":
    "Naturally, higher quality means more power and sturdiness...",
"『バックラーとは』": '"About the Buckler"',
"通常の盾に比べれば、防御力は数段落ちるが、":
    "Compared to normal shields, its defense is several ranks lower, but",
"回避率が大きく上がるので、ただの軽くて弱い盾という":
    "it greatly raises evasion, so it's not just a light, weak shield.",
"わけではない。": "Not at all.",
"なので、通常の大きさの魔物や人間を相手にする場合には、":
    "So against monsters and humans of ordinary size,",
"通常の盾よりも有効な場面が多い。":
    "it's often more effective than a normal shield.",
"しかし、巨大な敵や、どうしても避けられない攻撃を":
    "However, against giant enemies or those with",
"用いてくる相手には、あまり有効ではない。":
    "unavoidable attacks, it isn't very effective.",
"相手に突きつけるように構える小型の盾で、":
    "A small shield held out toward the opponent,",
"中型、大型の盾とは異なった技術を要する。":
    "requiring different technique than medium or large shields.",
"受け止めるのではなく、受け流す、絡めとるなどして、":
    "Rather than blocking, it deflects and entangles,",
"回避やカウンターの布石にする盾である。":
    "serving as a setup for evasions and counters.",
"最近すっかり外に行くこともなくなってな。":
    "I've stopped going out entirely lately.",
"着る機会もなさそうだから、お前で有効活用":
    "Looks like I won't get to wear it, so put it to",
"してくれよ。": "good use yourself.",
"軽装鎧は、コートに比べれば素早さは下がるが、":
    "Light armor lowers agility compared to a coat, but",
"それ以上に防御力が上がるから、戦闘するなら":
    "raises defense more than that, so if you're going to fight,",
"ウィン！待ってたぞ！": "Win! I've been waiting!",
"ぜったいに着ておいた方がいいぞ。":
    "you should definitely wear it.",
"ハリスさんとこの娘さんの件、":
    "About Harris and his daughter's matter—",
"解決したらしいじゃないか。": "I heard it got resolved.",
"お前、自分の仕事があるのに助けてくれて":
    "You helped even though you had your own duties,",
"本当にありがとな！": "thanks a lot!",
"これ、俺からの気持ちだ、": "This is a token of my gratitude,",
"まあまあ、受け取ってくれよ！": "come on, just take it!",
"最近魔物に関する相談事が増えているんだ。":
    "Lately, more and more people come to me about monsters.",
"何かこの辺りに親玉とか、巣とかが":
    "Maybe there's a big monster or a nest",
"あるのかも知れないなあ…。": "around here somewhere...",
"この武器の売上の何割かは当然、騎士団に":
    "A cut of this shop's sales goes to the knight order, of course.",
"入るんだぜ？俺たち相手なら、少しは":
    "So when dealing with us, couldn't you cut",
"割引とかしてくれてもいいよなあ…。":
    "us a little discount...?",
"ここは交易や冒険者向けの武器、防具屋だ。":
    "This is a weapon and armor shop for traders and adventurers.",
"支給品とはちょっと違う品々を揃えてる。":
    "We stock things a bit different from standard issue.",
"ウィン、ちゃんと金は持ってきたか？":
    "Win, did you bring enough money?",
"それよりあんた、ロイさんだろ？":
    "More importantly, you're Roi, aren't you?",
"聞いての通り、闇のエレメントの復活が":
    "As you've heard, the Dark Element's revival",
"近付いております。": "draws near.",
"…は？": "...What?",
"ピピン。": "Pipin.",
"傷薬を　１個　手に入れた！": "Obtained a Healing Herb!",
"ぜんぜん普通じゃなかったぞ…！？":
    "It was anything but normal...!?",
"俺がいなかったら、お前は死んでいたろうな。":
    "If I hadn't been there, you'd be dead.",
"感謝しろ。": "Be grateful.",
"万金丹を　１個　手に入れた！": "Obtained a Mankintan!",
"ここから南…フレイム砂漠はマジで暑いぜ。":
    "South of here... the Flame Desert is seriously hot.",
"そんで魔物も強い。野盗も出る。":
    "And the monsters are strong. Bandits too.",
"ウィン、マジで気をつけて行けよ。":
    "Win, be really careful out there.",
"いやあまいったよー": "Man, this is rough.",
"こう入出国が厳しいとなると":
    "With entry and exit being this strict,",
"商売あがったりさー": "my business is going under.",
"おっ！ウィン、ちゃんと万金丹持ったか？":
    "Oh! Win, did you bring Mankintan?",
"ヘビがでるぞ、ヘビ！！": "Snakes, there'll be snakes!!",
"ウィンダムに来たらぜひ私の父に会いに来て":
    "When you come to Windam, please be sure to",
"下さい！": "visit my father!",
"必ずお礼はします！": "I'll repay you, I promise!",
"ありがとう！！": "Thank you!!",
"まいったのう…とてもじゃないが、":
    "This is a pickle... at this rate,",
"日が暮れる前に通れるようには":
    "there's no way I'll get through",
"ならなそうじゃのう": "before sundown.",
"騎士さまも　とおせんぼされたの？":
    "Did they stop you too, Sir Knight?",
"だったらうちの宿に泊まっていきなよ！":
    "Then stay at our inn!",
"ここはフレイム王国への関所だ。":
    "This is the checkpoint to the Flame Kingdom.",
"…おい、ウィン。なんでここへ来たんだ？":
    "...Hey, Win. Why did you come here?",
"それはまさに国王陛下の発行する通行手形！！":
    "That's the permit issued by His Majesty the King!!",
"ははーーーっ": "Yes, sir!",
"騎士ウィン様どうぞお通りくださいませー":
    "Sir Knight Win, please, right this way~",
"ウィンは通行手形を見せた！": "Win showed his permit!",
"もう塔から出ようか、それともまだ探索しようか…":
    "Should we leave the tower, or keep exploring...?",
"とは言え…そうとは言えだ！": "But still... and yet, but still!",
"やはり、やっぱり、闇の結晶を集めなければならない…":
    "Indeed, surely, I must gather the Dark Crystals...",
"そう言うことか…　面倒だなあああああああ！":
    "So that's how it is... what a pain in the ass!",
"…おいっ！": "...Hey!",
"…んんん？": "...Hmm?",
"お前、ここで何をしている？": "What are you doing here?",
"何者だ？答えろ！": "Who are you? Answer me!",
"…王国？　騎士団だと…？？":
    "...A kingdom? A knight order...??",
"あー　忌まわしき風の紋章の継承者が…":
    "Ugh, the accursed inheritor of the Wind Crest...",
"勝手に国などを作って…":
    "going and making a kingdom on your own...",
"威張っているのだな…！　この時代では！！":
    "how you swagger... in this age!!",
"時代…？": "An age...?",
"何を言っている！？": "What are you talking about!?",
"しかしその姿、ガイコツか…　魔物か？":
    "But that form of yours—a skeleton... a monster?",
"魔物…だとー？": "A monster, you say—?!",
"この大魔道士ピケピケ様に向かって…":
    "To me, the great mage Pikepike, of all people...",
"魔物だとぬかしたか！　そこの赤いの！！":
    "You dare call me a monster! You, the red one!!",
"私はこの世界を真に束ねる力、その担い手…":
    "I am the bearer of the power that truly rules this world...",
"闇のエレメント四天王筆頭…":
    "chief of the Four Dark Element Generals...",
"ふむ、ふむ…": "Hmm, hmm...",
"大魔道士……ピ！ケ！ピ！ケ！様であるぞ！！":
    "I am the great mage... Pi! Ke! Pi! Ke!!",
"ピ…　なんだって？": "Pi... what was that?",
"よく分からないが、魔物に騎士団の建物を":
    "I don't get it, but I can't let a monster",
"ウロウロさせとくわけにはいかん。":
    "wander around the knight order's building.",
"風のエレメントの力も、": "Feel the power of the Wind Element,",
"覚悟しろ！ぶっ殺してやる！":
    "and prepare yourself! I'll kill you dead!",
"何でもいいとは何だ！　失礼なやつだ！":
    "What do you mean 'whatever'! You rude thing!",
"私の名は、ピケピケだと言っている…":
    "I keep telling you, my name is Pikepike...",
"おぼえろ、ピケピケ様だ！！":
    "Remember it! Lord Pikepike!!",
"うるさい！！行くぞ！　ピ…　ピカピカ！！":
    "Shut up! Let's go! Pi... Pikapika!!",
"ほんの少しだが、確かに増しているようだなあ。":
    "It's only a little, but it's definitely increasing.",
"わざとやっているのか…！？":
    "Are you doing it on purpose...!?",
"わざとやっているのだったら許さんぞー！！":
    "If you're doing it on purpose, I won't forgive you!!",
"わざとじゃない！！": "I'm not!!",
"それよりも行くぞ！早くバトル準備しろ！":
    "Anyway, let's go! Get ready for battle, now!",
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
