#!/usr/bin/env python3
"""Fill batch 52: bridge completion, Windam gathering."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"そのため、橋が落とされてから、誰もその地に":
    "And so, since the bridge was dropped, no one has",
"近付こうとしなくなったのだ。": "dared approach that land.",
"我々の得体の知れない脅威の眠る地…":
    "A land where unknown threats slumber for us...",
"それが、暗黒大陸なのだ。": "that is the Dark Continent.",
"感謝します。": "Thank you.",
"なぜこうも早く準備が出来たのです？":
    "How were you able to prepare so quickly?",
"我々は、やっと動き出したところで…":
    "We were just getting started...",
"へへへ！": "Hehehe!",
"切れ者のロイさんを出し抜いてやったぜ！！":
    "We beat the sharp-witted Roi to it!!",
"…面目ない。": "...My apologies.",
"いやいや、マジにしないでくれよロイさん…":
    "No no, don't take it seriously, Roi...",
"皆さんも、南の大陸に光の柱が立つのを":
    "You all saw the Pillar of Light rise",
"見られたかと思います。": "over the southern continent, I'm sure.",
"我が一族の先々代当主、オタキ様はすぐに":
    "Our clan's head two generations back, Lady Otaki, said at once",
"暗黒大陸に橋をかけねばならないと言いました":
    "that a bridge to the Dark Continent must be built.",
"アンタらもアレ見て、すぐあそこに行かないと":
    "Didn't you lot see that and think you had to go",
"って思わなかったのかよ？": "there right away?",
"…重ね重ね面目ない。": "...I'm twice over embarrassed.",
"我々が橋の建設の準備をしている間に、":
    "While we were preparing the bridge's construction,",
"既にフレイムからの兵の一団がこちらに":
    "a group of soldiers from Flame had already",
"到着しました。": "arrived.",
"資材も人員も確保できたので、急いで建設を":
    "With materials and hands secured, we began",
"開始したんです。": "construction in haste.",
"…なるほど。": "...I see.",
"その為、こうしてウィンダム王国への":
    "For that reason, I apologize for the delay in",
"連絡が遅れたことをお詫びします。": "contacting the Windam Kingdom.",
"ウィンならハヤテの力があるんだから…":
    "With Win's Hayate power...",
"別にこっちから連絡に行かなくても、":
    "we figured he'd come on his own, without us",
"向こうから来るって思ったんだよなー？":
    "sending word—right?",
"…ま、まあな。": "...W-Well, sure.",
"オレらに顔見せにも来ねーで、":
    "Without even showing your face to us,",
"オマエなにやってたんだよ、ウィン？":
    "what've you been up to, Win?",
"…ウィンを責めないでやっていただきたい。":
    "...I'd ask you not to blame Win.",
"軍の指揮権は俺にある。": "The army's command is mine.",
"い、いや…　責めてなんかいねーよ！":
    "N-No... I'm not blaming him!",
"ただ、少し気になっただけさ！":
    "I was just a bit curious!",
"それよりだ！": "Anyway!",
"橋も出来て、三人も揃ったんだ！":
    "The bridge is done and all three of us are here!",
"さっさと闇のなんたらを全部やっつけに":
    "Let's hurry and crush the Dark-whatevers",
"いこーぜ！　ウィン！！": "already! Win!!",
"フレイム王国とセイリューの迅速な動きに":
    "I thank the Flame Kingdom and Seiryu from",
"こころより感謝する！": "the bottom of my heart for their swift action!",
"うお！なんかかっこいい…！":
    "Whoa! That sounded cool...!",
"あはは…": "Ahaha...",
"橋はセイリューの南…": "The bridge is south of Seiryu...",
"採石場の裏の川にある。": "on the river behind the quarry.",
"しかし、道中の魔物も以前よりずっと":
    "But the monsters along the way have grown",
"強くなっている…。": "far stronger than before...",
"ウィン、身体はなまってないか？":
    "Win, your body hasn't gone soft, has it?",
"ウィンなら心配ねーよ！": "No worries about Win!",
"どこへだって風の速さで飛んでいくぜ！":
    "He'll fly anywhere at the speed of wind!",
"どうもー　王様！": "Howdy, King!",
"ウィン、久し振りだな！！": "Win, long time no see!!",
"ご無沙汰しております、ウィンダム国王。":
    "It's been a while, King of Windam.",
"おお…　フレイム王子のホノオ殿下と、":
    "Oh... Prince Hono of Flame, and",
"セイリュー領主ナガレ殿…！": "Lady Nagare, lord of Seiryu...!",
"なんと！": "My word!",
"こうなると、紋章の継承者がそろい踏みですな！":
    "All the crest inheritors together, then!",
"…ちょうどいま、おふたりの元へウィンを":
    "...I was just about to send Win to the two of you...",
"行かせようとしていたところなのだが…":
    "but...",
"しかし…　ここへは、なぜ…？":
    "However... why are you here...?",
"ロイ騎士団長、橋は完成しましたよ。":
    "Commander Roi, the bridge is complete.",
"な、なんと…！": "Wh-What...!",
"橋の警備の方も万端だぜ！": "The bridge guard is all set too!",
"フレイムは城の守りに割く兵が":
    "Flame has more than enough soldiers",
"十分に足りてるんでねー": "to spare for guarding the castle,",
"とはいえ…　": "though...",
"あいつらには随分と工事を手伝って":
    "they helped so much with the construction",
"もらったので、かなり疲れているんです。":
    "that they're rather worn out.",
"なので…騎士団の方々にもご協力いただけると":
    "So... it would help if the knight order",
"助かります。": "could lend a hand.",
"も！　もちろんですぞーーー！！":
    "O-Of course—!!",
"行け！！　サクソン！！": "Go! Saxon!!",
"とは言え、きついときはきついって言えよ？":
    "Still, if it's tough, say it's tough, alright?",
"継承者は誰よりも我慢しなきゃいけないって、":
    "No one ever said the inheritor has to endure",
"誰かに言われたわけでもないだろ？": "more than anyone, right?",
"まあ、そんなもんだよなー。": "Yeah, that's just how it is.",
"俺は、お前がいつも通りに受け答えしてくれて、":
    "For me, the fact that you answered just as you always do",
"それだけでも安心したぜー": "was enough to put me at ease.",
"さすがっていうか…　本当か？":
    "Impressive... or wait, really?",
"まあ、暗い顔してたってしょうがないけどさ。":
    "Well, moping about wouldn't help anyway.",
"一体どんな危険が待ち受けているのか…":
    "What perils await, I wonder...",
"俺には皆目見当もつかんが…": "I haven't the faintest idea, but...",
"ウィン、無事を祈る。": "Win, I pray for your safety.",
"なんでだ、仕事だろう？": "Why!? It's a mission, right!?",
"まさかウィン、": "Don't tell me, Win,",
"お前、陛下の話を聞いてなかったのか？":
    "you weren't listening to His Majesty?",
"…　と、ピピンなら言うところだな。":
    "...is what Pipin would have said.",
"南の暗黒大陸だってな…": "The southern Dark Continent, huh...",
"そんな場所があるなんて、俺は初耳だった。":
    "I'd never even heard such a place exists.",
"お、俺は…　この部屋を守るのが仕事だ…":
    "M-My job is... to guard this room...",
"王からそう命じられている！！":
    "His Majesty ordered it!!",
"こんな非常時でも…　か？": "Even in a crisis like this...?",
"そ、そうだ…": "Y-Yes...",
"俺がここを動くのは、国王陛下から…":
    "The only one who can order me from this spot is...",
"ここをどけと命令されたときだけだ！":
    "the King himself!",
"ウィン…！　それに…　ピピン！？":
    "Win...! And... Pipin!?",
"フン…": "Hmph...",
"…まさに適材適所ってやつだな。":
    "...Truly the right man in the right place.",
"融通の利かない男だが、警備をさせるには":
    "Stubborn as he is, for guard duty there's",
"これほど信用できる人間はいまい。":
    "no one more trustworthy.",
"どうしてここに！？": "Why are you here!?",
"お前こそ、ここで何をしている…？":
    "The question is, what are YOU doing here...?",
"王の間に敵がいる…　知っているはずだ。":
    "There's an enemy in the throne room... you should know that.",
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
