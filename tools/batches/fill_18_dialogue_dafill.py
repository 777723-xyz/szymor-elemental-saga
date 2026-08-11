#!/usr/bin/env python3
"""Fill batch 18: Dafill's illusion scene, Pipin's return."""
import csv
import os
import re

D = {
"オレは？　一応次の王様なんだけど…？":
    "What about me? I'm the next king, you know...?",
"我が兵たちにとって、ナガレ殿はいまや":
    "To my soldiers, you, Lord Nagare, are now",
"皆の救世主、戦場の女神です。":
    "everyone's savior, the goddess of the battlefield.",
"よかったら兵たちに声をかけてやって下され。":
    "If you would, please say a few words to the soldiers.",
"全軍の士気がおおいに上がると思います。":
    "I believe it would greatly lift the morale of the whole army.",
"派手なバケモノが…王の間に…！":
    "A flashy monster... in the throne room...!",
"仕方ない…　このままもうしばらく隠れていろ。":
    "Can't be helped... stay hidden a while longer.",
"あっ！　騎士さま、お待ちを…！！":
    "Ah! Sir Knight, wait...!!",
"ひ…ひい！　　…って、騎士さま…？":
    "E-Eek! ...Wait, Sir Knight...?",
"私にはこれしかできることがありません…":
    "This is all I can do...",
"たいしたものではないですが…お持ちください":
    "It's not much, but... please take it.",
"フン…　ないよりはいいだろう。":
    "Hmph... better than nothing, I suppose.",
"おい、料理人！　": "Hey, cook!",
"逃げ遅れたのか？": "Didn't make it out in time?",
"は…はい…　仕事を終えて戻ろうとしたら…":
    "Y-Yes... I was heading back after work, and then...",
"だはは！！": "Bahaha!!",
"いや、だからー　継承者じゃない人間なんて…":
    "No, see—people who aren't inheritors...",
"ボクにとっては、ハエ以下の存在なわけー":
    "are less than flies to me—",
"むしろハエよりずっとうるさいから…　":
    "actually, they're way noisier than flies...",
"もっとムカつくんだよねーーーーーー？？":
    "so they annoy me even more, you know??",
"んーーーーー？？": "Riiight??",
"キサマのそのクドい喋り方にはウンザリだ…":
    "I'm sick of your wordy way of talking...",
"もういい！　ダフィール、かかってこい！！":
    "Enough! Dafill, come at me!!",
"ウィン、さっきのバトルの感覚を忘れるな！":
    "Win, don't forget that feeling from the last battle!",
"俺が攻撃で、お前がサポートだ！！":
    "I attack, and you support!!",
"あーーー　やるのねーーー": "Awww, so we're doing this~",
"継承者がひとりってのが残念だったけど…":
    "Too bad there's only one inheritor, but...",
"まあ、いっかーーー！！": "well, whatever!!",
"じゃあ　いくよー": "Here I go~",
"せーの…": "Ready... set...",
"プレイボ―――――――ル！！": "Play ba——all!!",
"うわーーーなんだ！": "Whoa— what is this!",
"突然まものがたくさん…！":
    "Suddenly, a swarm of monsters...!",
"ぐおおおおおお！！": "Gwaaaaah!!",
"突然魔物の大群が！！！！！":
    "A huge horde of monsters, all at once!!!!",
"えーーーーい、戦えーーーーい！！":
    "Fight, I say—!!",
"くっ！！まずい…！　こうなっては…":
    "Guh! This is bad...! At this rate...",
"俺もどうにかして剣を抜かねば…！":
    "I've got to find a way to draw my sword...!",
"な、なにが起こっている！？":
    "Wh-What's happening!?",
"やめろ！　お前ら！！": "Stop it, all of you!!",
"人間はもはや私しかおらぬのか…！":
    "Am I the only human left...!",
"ええいっ！　ならば一匹でも多く道連れに…！":
    "Bah! Then I'll take as many of you with me as I can...!",
"ハーイ　みんながんばってーーー":
    "Hii, everyone, keep it up~",
"戦うのはボクじゃなくって　みなさんでーす！":
    "It's not me fighting—it's all of you!",
"クッ…！": "Hmph...!",
"これはキサマの仕業なのか…　ダフィール！！":
    "Is this your doing... Dafill!!",
"そうだよーん　ボクはひとっていうかー":
    "That's right~! I'm good at manipulating,",
"いきもの全般を操ったり惑わしたりするのが":
    "or rather, bewitching all living things,",
"得意なのさーーー": "you see~",
"この術は継承者には通用しないんだけどーーー":
    "This art doesn't work on inheritors, though~",
"ふつうのニンゲンだと効いちゃうワケー":
    "but it works fine on ordinary humans~",
"さあ継承者さーん　ふつうのニンゲンに":
    "So, Mr. Inheritor~ are you going to be",
"ころされちゃうよー？　いいのーーー？":
    "killed by ordinary humans? Is that okay~?",
"ハヤテの魔法でここを脱出するしかない…！":
    "We have no choice but to escape with Hayate's magic...!",
"おお…　ピピン！！　それに、ウィン！！":
    "Oh... Pipin!! And Win!!",
"どうせお前にこいつらは殺せないだろうが…":
    "You couldn't kill these people anyway...",
"なら、逃げるしかないだろ…！！":
    "so running is the only option...!!",
"逃げたらこいつらが助からないってんだろ…":
    "But if we run, these people won't be saved...",
"バカが…！！　相変わらずだな、お前は…！！":
    "You idiot...!! Always the same, aren't you...!!",
"…ったく　俺としたことがドジったもんだ…":
    "...Jeez, I can't believe I slipped up like this...",
"お前といると…　焼きがまわりっ放しだ！":
    "Being with you... brings me nothing but bad luck!",
"おい、赤いのさー": "Hey, red one~",
"ピピンだとーーー！？": "Pipin, you say—!?",
"なんでオマエ　大丈夫なんだー？":
    "Why are you unaffected?",
"オマエ、継承者じゃないだろ？":
    "You're not an inheritor, right?",
"なんでボクの術効いてないワケー？":
    "Why isn't my art working on you?",
"騎士を突然やめたきさまが…":
    "You, who quit being a knight all of a sudden...",
"…さあな。": "...Who knows.",
"キサマの術が、キサマの思っているよりも":
    "Maybe it's proof that your art isn't",
"全然大したことない証拠じゃないのか？":
    "nearly as impressive as you think.",
"やめやめーーー": "Stop, stop~",
"試合中断しまーーーーーーーーす":
    "Match suspended—!!",
"今更どの顔を下げてやってきたのだー！！？？":
    "How dare you show your face here now—!!??",
"フン…　無能のお前に代わって…":
    "Hmph... I've come to slay this monster",
"このバケモノを俺が退治しに来てやったのさ。":
    "in place of you and your incompetence.",
"はっ…！　俺は…一体…？":
    "Hah...! What... what was I...?",
"な…何が起こったんだ？　": "Wh-What happened?",
"ぐぬぬぬ…　きさまああああーーー！！":
    "Grrr... you—!!",
"どうした…？　なぜ皆　傷を負っている！？":
    "What's this...? Why is everyone wounded!?",
"…術を、解いたのか？": "...You dispelled the art?",
"ピピン…　ウィン…": "Pipin... Win...",
"何が起こった…？": "What happened...?",
"…そいつが幻惑の術みたいなものを使った。":
    "...That guy used some kind of illusion art.",
"それで、俺とウィン以外のお前らは…":
    "Because of it, everyone but me and Win...",
"味方を魔物と思って、同士討ちを始めたのさ。":
    "saw allies as monsters and started fighting each other.",
"な…なんと！": "Wh-What!",
"サクソン殿！　ここはこらえて下され！！":
    "Lord Saxon! Hold yourself together!!",
"そうなんだけどー": "That's true, but~",
"やめたーーーーーーー": "I'm stopping~",
"なぜやめた！？": "Why did you stop!?",
"もっといいこと思い付いたからさーーー":
    "Because I thought of something even better~",
"なに…？": "What...?",
"これはきっと、みんなも楽しめると思うなー":
    "I'm sure everyone will enjoy this~",
"なにを言っている…！": "What are you talking about...!",
"そこの赤いのさー　天才なんだってー？":
    "Hey, red one~ you're supposed to be a genius, right?",
"なのにずいぶんと…　": "And yet...",
"風の紋章の継承者ウィンと…":
    "The Wind Crest's inheritor, Win, and...",
"内に…　闇を抱えているみたいだねー…":
    "it seems you hold darkness within...",
"そういう子には…　とっておきのがあるのさ":
    "For kids like you... I've got something special.",
"今度はなんだ…？": "What now...?",
"天才騎士ピピンが来てくれたのであれば、":
    "Since the genius knight Pipin has come,",
"じゃあねー　みんなーーー": "well then, later, everyone~",
"ボクはあんまりみんなを楽しませてあげられ":
    "I couldn't entertain you all",
"なかったけどー": "that much, but~",
"この子がみんなを楽しませてくれるからーーー":
    "this one here will entertain you all~",
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
