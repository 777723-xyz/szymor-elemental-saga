#!/usr/bin/env python3
"""Fill batch 33: Roi's hut, tower run, desert checkpoint scenes."""
import csv
import os
import re

D = {
"感謝しろ、ロイ！！": "Be grateful, Roi!!",
"待て！ピピン！": "Wait! Pipin!",
"俺を知っているのか！？": "You know who I am!?",
"俺は一応騎士団長でな。": "I am, after all, the Knight Commander.",
"騎士たちのリストは把握している。":
    "I keep track of the knight roster.",
"ウィンはピピンと一緒に、事の経緯をロイに説明した":
    "Win, along with Pipin, explained everything to Roi.",
"…大魔道士ピケピケに、闇の結晶…":
    "...Grand Mage Pikepike, Dark Crystals...",
"最近の魔物の増加とも、符合する。":
    "It all aligns with the recent surge in monsters.",
"お前たちの話は分かった。": "I understand your tale.",
"信じがたいことだが…": "Hard as it is to believe...",
"闇のエレメントは復活するのかも知れない。":
    "the Dark Element may indeed revive.",
"…何の用だ？": "...What do you want?",
"…おとぎ話じゃ、なかったのか。":
    "...So it wasn't a fairy tale.",
"おとぎ話だったさ…。": "It was a fairy tale...",
"お前たちの話を聞くまではな。":
    "until I heard your story.",
"そうなると、急がねばならん。":
    "In that case, we must hurry.",
"大魔道士が復活しているのなら、":
    "If the Grand Mage has revived,",
"他の四天王も蘇り、各地で動き出している。":
    "the other Generals will rise too and begin moving across the lands.",
"紋章の継承者を集め、闇の結晶をやつらに":
    "If we don't gather the inheritors and stop the Generals",
"渡すのを防がねば、この大陸は急速に破滅へと":
    "from obtaining the Dark Crystals, this continent",
"向かうだろう…。": "will rush headlong into ruin...",
"左腕を出せ。おまえに、風の紋章を継承する。":
    "Extend your left arm. I hereby pass you the Wind Crest.",
"なっ……！": "Wh—...!",
"俺は…以前の負傷で、剣を握ることが出来ん。":
    "I... can no longer hold a sword, due to an old injury.",
"俺が騎士団長であり、次の候補者が未定だった":
    "Since I was Knight Commander and no successor was decided,",
"ことから、俺が継承者のままだったが…":
    "I remained the inheritor, but...",
"闇のエレメントが復活しようとしているいま、":
    "with the Dark Element about to revive,",
"俺が継承者のままでいるわけにはいかんのだ。":
    "I cannot remain the inheritor.",
"あんたがロイだな。": "You're Roi, aren't you.",
"だからだ…": "That's why...",
"急なのは承知の上だ。": "I know this is sudden.",
"しかし、ウィン…　おまえは騎士だ。":
    "But Win... you are a knight.",
"騎士であるのなら、いつでも国の…":
    "As a knight, you must always be ready to lay down",
"世界のためにその命を捧げる覚悟は出来て":
    "your life for your country... for the world...",
"いるはずだ…。　　さあ、左手を…":
    "You have that resolve... Come, your left hand...",
"な…　なんでウィンなんだ？":
    "Wh-...Why Win?",
"陛下から言われて、あんたを連れ出しに来た。":
    "His Majesty ordered us to come bring you out.",
"どうしてそいつが継承者なんだ！？":
    "Why is HE the inheritor!?",
"どうして俺じゃない！？": "Why not me!?",
"俺は………！": "I......!",
"俺は、そいつなんかよりもずっと強い！":
    "I'm far stronger than him!",
"騎士としての経験もずっと上だ！！":
    "I've got way more experience as a knight!!",
"それに、紋章の継承者は…":
    "Besides, the crest's inheritor is...",
"この国では騎士団長になるものだ…。":
    "the one who becomes Knight Commander in this country...",
"そんな重大な決断…人選なのに…":
    "For such a momentous decision... such a crucial choice...",
"どうして俺じゃなくて、ウィンなんだ！？":
    "why Win and not me!?",
"ロイ！！": "Roi!!",
"面倒だ、一気に上まで走り抜けるぞ！":
    "This is a drag—let's just sprint to the top!",
"…ひよっこのお前には、無理かも知れんな。":
    "...A rookie like you might not manage it.",
"慎重に進むのに、付き合ってやってもいい。":
    "I could go along with a careful approach.",
"…どうする？　お前が決めろ。":
    "...What'll it be? Your call.",
"ザコの相手は俺がする。": "I'll handle the small fry.",
"お前は遅れずに付いてくることだけを考えろ！":
    "Just focus on keeping up without falling behind!",
"…フン、人食いの魔物とは言え、":
    "...Hmph, man-eating monsters, they may be, but",
"ザコしかいないな。": "there's only small fry here.",
"そろそろ最上階への階段だ。":
    "The stairs to the top floor are just ahead.",
"ザコの魔物の気配もプンプンする…":
    "I can smell plenty of small-fry monsters...",
"ザコとのバトルにも付き合ってやる。":
    "I'll even tag along for the small-fry battles.",
"ヤバいと思ったらすぐに回復アイテムを使え。":
    "If things look bad, use a recovery item right away.",
"かなり魔物が入り込んでいるみたいだ。":
    "A lot of monsters have gotten in here.",
"ウィン、油断するなよ？": "Win, don't let your guard down, alright?",
"ウィンは頷いた。": "Win nodded.",
"しかもこの気配は…": "And this presence...",
"ウィンダム騎士団の管理する建物です":
    "This building is managed by the Windam Knight Order.",
"関係者以外の立ち入りを禁じます":
    "Entry by unauthorized persons is prohibited.",
"通行手形のないもの、通り抜けを禁ずる。":
    "Those without a permit may not pass.",
"ウィンダム騎士団": "Windam Knight Order",
"えっ！！！！！！！！！？？？？？？":
    "Huh!!!!!!???",
"いいんですか…本当に？": "Really... are you sure?",
"ありがとうございます！！": "Thank you so much!!",
"マジで参ったなあ…": "This is really rough...",
"ありがとう騎士さま！！": "Thank you, Sir Knight!!",
"あついったらないし…": "The heat is unbearable...",
"誰か通行手形をくれたりしないかなー…":
    "Won't someone just give me a permit~...",
"これじゃあウィンダムの親父に孫の顔を":
    "At this rate, I can't even show my grandkid's face",
"見せられないよー…": "to my old man in Windam~...",
"まいったなあ　あついったらないよー":
    "This is rough— the heat's unbearable~",
"騎士さま　ありがとう！！": "Sir Knight, thank you!!",
"お前らに構っているヒマは…そんなヒマはない":
    "I have no time to waste on you... no time at all.",
"そういう悪い子には少しだけオシオキを…":
    "Bad kids like you deserve a little punishment...",
"うん、オシオキをしちゃおうかなあああ？？":
    "Yeah, maybe I'll punish you a little~??",
"ほんのちびっとだけ相手してあげよう！！":
    "I'll play with you just a tiny bit!!",
"ホントに、ホントにちょびっとだけね！！？？":
    "Really, really just a tiny bit, okay!!??",
"こんなもんでいいかな？？": "Is this enough??",
"結構やるね、キミたちいいいい！！！":
    "Not bad, you lot—!!",
"これ以上構っているヒマは…ない！！！！":
    "I've no more time to spend on you... at all!!!!",
"…闇のエレメントがどうのとか言ってたな、":
    "...He was going on about the Dark Element,",
"アイツ…。": "that guy...",
"そんなおとぎ話を信じているなんて、":
    "To believe such a fairy tale,",
"ちょっとヘンなやつに違いない。":
    "he must be a bit off.",
"とは言え、そうとは言え…":
    "Even so, even so...",
"陛下に報告しなければならないな。":
    "we must report this to His Majesty.",
"ウィン、帰るぞ！": "Win, let's head back!",
"…な！？　　　あいつ、消えた！？":
    "...Wh—!? He disappeared!?",
"毎度ありがとさん。のんびりしていきな…。":
    "Thanks as always. Take it easy...",
"よお、あんた方、今日はここで休んでいくか？":
    "Yo, you folks, resting here today?",
"あんたがた、朝だよ。": "Hey, you two—morning.",
"道中気を付けてな。": "Be careful on the road.",
"金が足りないみたいだね…。":
    "Looks like you're short on cash...",
"砂漠は魔物も強いし、暑さもしんどいぞ。":
    "The desert's monsters are strong, and the heat is rough.",
"すまんがタダで泊まらせるわけには":
    "Sorry, but I can't put you up",
"いかないよ…。": "for free...",
"一泊５０Ｇだよ。": "50G a night.",
"よろしいかな？": "Is that all right?",
"南にあるという、コブラ酒ってのを":
    "I came to buy that southern specialty,",
"買いに来たんだが…　関所を通れなくって…":
    "the Cobra Sake... but the checkpoint won't let me through...",
"それで、ここで普通の酒を飲んだくれてる":
    "So I'm just drowning my sorrows in ordinary booze here",
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
