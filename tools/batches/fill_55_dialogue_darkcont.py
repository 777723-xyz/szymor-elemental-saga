#!/usr/bin/env python3
"""Fill batch 55: Dark Continent descent, Mycenae rematch."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"よろしくおなながいいしままーーーーす！！！":
    "Pleased to meet you, now I'll bow bow—!!!",
"人間たちよ…　最後に………": "O, humans... at the end......",
"ひとつだけ………": "just one thing......",
"で…　次はどうすればいいんだ？":
    "So... what do we do next?",
"行き止まりに見えるぞ？": "Looks like a dead end?",
"発音が難しいんだよなあ…":
    "The pronunciation is just so hard...",
"アイツがいた後ろの地面に、":
    "On the ground behind where that guy stood,",
"なんだか青い模様が描かれているな。":
    "there's some kind of blue pattern drawn.",
"あれに乗ったら何か起こりそうじゃないか？":
    "Wouldn't something happen if we stood on it?",
"えー？　そんなことあるかよー？":
    "Huh? Would it?",
"他に何かヒントがあるわけでもないし、":
    "There's no other hint anyway, and",
"何より急がないといけないんだ。":
    "more than anything, we're in a hurry.",
"なんでもやってみよう！": "Let's just try it!",
"お、おう…！": "O-Okay...!",
"聞いたことのない発音なんだよ…":
    "It's a pronunciation I've never heard...",
"さようなら、ピＱＥピＱＥ…": "Farewell, PiQE PiQE...",
"うわっ、なんだよココはー…":
    "Whoa, what is this place...",
"いかにも、ここは闇の何かですって感じだな…":
    "This place screams 'dark something,' doesn't it...",
"しかしなんつーか…　静かだな。":
    "But man... it's quiet.",
"魔物の気配がしない…。": "No sign of monsters...",
"闇に近付いているはずなのに。":
    "Even though we should be nearing the Dark.",
"とはいえ、落ち着く場所ってワケでもねー…":
    "Still, it's not exactly a place to relax...",
"一応気を引き締めていこうぜ！":
    "Let's stay on our guard, alright!",
"ウィンはうなずいた": "Win nodded.",
"あ": "Ah.",
"あれ？　何も起こらねえぞ？": "Huh? Nothing happened?",
"一方通行なんだろうな。": "It's probably one-way.",
"どの道、もう引き返すわけにはいかない！":
    "Either way, we can't turn back now!",
"まあ他に道があるわけでもないしな…":
    "Well, there's no other path anyway...",
"急ぐぞ！　いつ闇いんふるなんとかが":
    "Hurry! The Dark Flu-whatever could start",
"始まってもおかしくねえ！！": "any moment!!",
"ウィンはうなずいた": "Win nodded.",
"あれ？　さっきと同じところじゃねえか！？":
    "Huh? Isn't this the same place as before!?",
"ちょっと違う気がする…　壁の色とか…":
    "It feels a bit different... the wall color and all...",
"ミケーネ…!!!": "Mycenae...!!!",
"…まさかピケピケが負けるなんて思わなったわ。":
    "...I never thought Pikepike would lose.",
"あたしたちの産み出そうとする闇の力が、":
    "The Dark power we seek to birth is greater",
"これまでのものよりも大きいのだから…":
    "than ever before, so...",
"継承者の力の増大もまた大きくて当然、か…":
    "it's only natural the inheritors' power grew too, I suppose...",
"ピケピケはアンタらの為にめちゃくちゃ":
    "Pikepike bought you all an enormous",
"時間稼いでから…　": "amount of time before...",
"死んだぜーーーーミケーネーーーー！！":
    "he died—!! Mycenae—!!",
"おバカめ！！　知ってるわよ！！":
    "You fool!! I know that!!",
"あんたは、なんでここにいるんだ！？":
    "And you—why are you here!?",
"闇いんふるやら魔王やらはまだなのか！？":
    "The Dark Flu and the Demon King—aren't they ready yet!?",
"ちっ………": "Tch.........",
"間に合っているならあたしはここにいないよ！":
    "If we were on schedule, I wouldn't be here!",
"なら、アンタも時間稼ぎに来たってワケかい？":
    "So you came to buy time too, huh?",
"へへ…アンタら、思ったよりも余裕ねえんだな":
    "Hehe... you lot aren't as relaxed as you thought.",
"やっぱりピケピケの存在は重要だったわ…":
    "Pikepike's presence really was crucial...",
"あたしたちだけで無理に闇の復活を早めるには":
    "To force the Dark's revival early on our own,",
"魔力が不足していたのよね…。":
    "we simply lacked the magic power...",
"黙れミケーネ！！": "Silence, Mycenae!!",
"話をする気はない！！": "I've no intention of talking!!",
"さっさとバトル準備をしろ！！":
    "Get ready for battle, now!!",
"あんだあ…このガキィ…？": "What was that... you brat...?",
"どうもてめえは無駄に頭が回るみてえだなあ…":
    "You've got a smart head on you, don't you...",
"早死にすんぞコラァ…？": "That'll get you killed early, punk...?",
"こっちはあんたに時間を稼がせたくないんだ、":
    "We don't want you stalling us,",
"当然だろ！！": "obviously!!",
"稼ぎたいならバトルで稼げ！":
    "If you want time, earn it in battle!",
"いくぞ、ミケーネ！！": "Here we come, Mycenae!!",
"まあ、あたしは別にいいんだけどねえ…":
    "Well, I don't really mind...",
"ウィン！　ホノオ！　問答無用でいくぞ！！":
    "Win! Hono! Let's go, no questions asked!!",
"いまのあたし達なら、こいつくらい…":
    "With our current strength, this one's...",
"きっと楽勝だ！！": "surely an easy win!!",
"お、おう！　そうだな…　さっさと倒すぜ！！":
    "O-Okay! Right... let's take her down fast!!",
"そう、仕方ないわ…": "Very well, it can't be helped...",
"そんなに急いでいるのね…　":
    "In such a hurry, are you...",
"あなたたちの…　死を": "to meet your... deaths",
"な…　コイツは…！！": "N-...This one is...!!",
"ミッッケェーーネッブリザーードッ！！！！":
    "Myyycenaeee—Bliiizzard!!!!",
"ああ…　早くしてくれ…　苦しいんだ…":
    "Ah... hurry up... it hurts...",
"………さらば、ミケーネ": ".........Farewell, Mycenae.",
"…秘剣！　つばめ返し！！":
    "...Secret art! Swallow Reversal!!",
"な…なんだと…！！？？": "Wh-What...!!??",
"つ、かまえた……": "Sh-Sh-she...",
"斬られながら…　剣を握るあたしの腕を…！？":
    "Even as she was cut... she caught the arm holding my sword...!?",
"直につかまれてのブリザードを…":
    "A Blizzard cast at point-blank range...",
"ツナミで防げはしまい…": "I can't block it with a Tsunami...",
"つばめ返し…返し！！": "Swallow Reversal... reversal!!",
"ごめん…ホノオ…！　ウィン…！！":
    "Sorry... Hono...! Win...!!",
"あ…　あたしの…　ま、負け…だ…":
    "Ah... my... d-defeat......",
"悪いけど、トドメを刺させてもらう。":
    "Sorry, but I'll finish you off.",
"さっきのだって殆どマグレなんだ！！":
    "Even that last one was mostly luck!!",
"だけど、あたしひとりなら…":
    "But if it's just me...",
"全く負ける気がしないんだよ。": "I don't feel like I could lose.",
"分かるな！？": "You get that!?",
"…わ、わかるけど…よ…": "...I-I get it... but...",
"いまだ！！　行け！！": "Now!! Go!!",
"…くっ！！": "...Ugh!!",
"ハァ…　ハァ…": "Hah... hah...",
"なめたマネしやがって………":
    "You dare mock me.........",
"ガキンチョどもがああああ！！！！！！":
    "You brats—!!!!!!",
"ナガレ…　死ぬなよ………": "Nagare... don't you die......",
"ウィン…　ホノオ…　無事だな？":
    "Win... Hono... you're safe, right?",
"あ、ああ…！　髪の毛ちょっと凍ったけどな！":
    "Ah, yeah...! My hair froze a bit, but!",
"よし…　間に合った！！": "Good... we made it!!",
"こ…ここの…グァガガガキィ…ててめええ…":
    "Th-This... Gwaaagh... y-you......",
"なあにしやがったあああああ！！！！？？？":
    "What did you do—!!!!???",
"あたしの最大出力ミケーネブリザードはあああ":
    "My maximum-output Mycenae Blizzard is",
"絶対零度ッ！！　その固さは永久凍土ッ…！！":
    "absolute zero!! As hard as permafrost...!!",
"いまのでてめえらは秒で全員カッチンコチンに":
    "That should've frozen you all solid",
"なってたハズなんだよー………　それをよー…":
    "in seconds...... and yet...",
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
