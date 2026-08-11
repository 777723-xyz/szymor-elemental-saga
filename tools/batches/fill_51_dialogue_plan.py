#!/usr/bin/env python3
"""Fill batch 51: Dark Continent expedition plan briefing."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"来いよーー？": "Come on~?",
"赤いのーーーーーーと金髪ーーーーー！！？？":
    "The red one and the blond—!!??",
"さすがに時間を食いすぎちゃったなー　更に、":
    "I've taken too long, and moreover,",
"ボクら以外のみんなを退屈させちゃったねー？":
    "I've bored everyone but ourselves~?",
"お待たせーーー": "Sorry for the wait~",
"さっきのより面白い方を操ることにしたからー":
    "I've decided to control someone more amusing than before.",
"俺の全てを掠め取っていった生意気なガキめ…":
    "You insolent brat who robbed me of everything...",
"…よくも俺の紋章継承を………":
    "...how dare you take my crest succession......",
"騎士団長の椅子を………": "and the Knight Commander's seat......",
"束になって来たって…　かないっこねえんだ。":
    "Even all together, you can't win.",
"俺の目的を…　俺の居場所を…":
    "My purpose... my place...",
"かすめ取っていった生意気なガキめ…！":
    "you insolent brat who stole it all...!",
"…よくも俺の名誉を…": "...how dare you take my honor...",
"騎士団長の椅子を……": "and the Knight Commander's seat......",
"束になって来ても、かないっこないんだからな":
    "Even all together, you can't beat me.",
"俺の目標を…　俺の居場所を…！":
    "My goal... my place...!",
"ウィンはロイスペシャルを受け取った！":
    "Win received Roi Special!",
"ウィンは本物のロイスペシャルを受け取った！":
    "Win received a genuine Roi Special!",
"その危険な暗黒大陸に、": "To that perilous Dark Continent,",
"これよりそなたは向かうのだ。": "you are to set out now.",
"あの光の柱が現れてから、異常気象や魔物の":
    "Since that Pillar of Light appeared, the abnormal weather",
"襲来も多少マシになった…": "and monster attacks have eased somewhat...",
"闇のエレメントの復活が、止まったのかとも":
    "I thought perhaps the Dark Element's revival had",
"思ったが…　そう考えるのは楽観に過ぎる。":
    "stopped... but that's far too optimistic.",
"闇の四天王は、何かを計画していると、":
    "The Four Dark Generals told us they were",
"我々に言い残していった…": "planning something...",
"そしてあの日以来…": "And since that day...",
"四天王は我々の前に、姿を現していない…":
    "the Four Generals haven't shown themselves to us...",
"つまりあの地で！四天王どもが悪だくみを…":
    "Which means, on that land! The Generals must be",
"闇のエレメントの復活の準備をしているに":
    "scheming... preparing for the Dark Element's",
"違いないのだー！！": "revival—!!",
"サクソン！！": "Saxon!!",
"なぜ最後のセリフだけロイから奪った！！":
    "Why did you steal only the last line from Roi!!",
"いいっ！！？？": "Huh!!??",
"い、いや！　わしは決してそんなつもりで…！":
    "N-No! I never meant to...!",
"陛下、よいのです。": "Your Majesty, it's fine.",
"俺はそんなの気にしませんし…":
    "I don't mind such things...",
"サクソン殿には決して悪気はありませんよ。":
    "Lord Saxon means no harm.",
"……………そうか。": ".........I see.",
"は、はいぃ……！": "Y-Yes......!",
"…と、いうわけでだ。": "...And so.",
"陛下、ウィンが参りました。": "Your Majesty, Win is here.",
"ウィン、この作戦には大きな2つの障害がある。":
    "Win, this operation faces two major obstacles.",
"まずひとつは、橋だ。": "The first is the bridge.",
"暗黒大陸に渡るには、橋をかけねばならん。":
    "To reach the Dark Continent, a bridge must be built.",
"そこで、セイリューの方々に資材の供出を":
    "For that, we must ask the people of Seiryu",
"依頼しなければならん。": "to supply materials.",
"橋の工事には、フレイム王国にも協力を":
    "We also intend to seek cooperation from",
"あおぐつもりだ。": "the Flame Kingdom for the construction.",
"そして橋の工事中と完成後は…":
    "And during and after the construction...",
"騎士団を半分に割き、それを警護に当てる。":
    "we'll split the knight order in half to guard it.",
"警護の指揮は、サクソン殿にお願いした。":
    "I've asked Lord Saxon to command the guard.",
"お任せあれ！！": "Leave it to me!!",
"頼もしいぞ、サクソン！": "Reliable as ever, Saxon!",
"俺は前線にいっても足手まといだろうし、":
    "I'd only be a burden at the front lines, so",
"本国の騎士団の指揮に当たり、防備を固める。":
    "I'll command the order at home and shore up our defenses.",
"もうひとつの障害だが、それは毒だ。": "The other obstacle is the poison.",
"うむ。": "Indeed.",
"さっきも言ったが、大昔の言い伝えによれば、":
    "As I said, according to ancient lore,",
"暗黒大陸に渡ると病気になるという…":
    "crossing to the Dark Continent brings illness...",
"しかし闇の力に耐性のある継承者なら…":
    "But an inheritor with resistance to the Dark's power...",
"影響を受けないかもしれない。":
    "might not be affected.",
"こればかりは半ば賭けになるが、":
    "It's half a gamble, but",
"やはり影響があったとなれば、作戦は":
    "if you are affected, the operation",
"即時中止して構わない。": "may be called off at once.",
"だからといって、少し無理そうだという位で":
    "Still, a knight who gives up at the first sign",
"諦める騎士であっては困るがな、ウィン！":
    "of difficulty would be a problem, Win!",
"いや、相手は正体のわからない毒気…":
    "No—the foe is an unknown miasma...",
"病気です。": "a disease.",
"騎士と言えども、無理は厳禁と考えます。":
    "Even for a knight, overexertion must be forbidden.",
"そうか。わかった。": "I see. Understood.",
"随分と説明が長くなったが…": "The briefing grew rather long, but...",
"ウィン、分かったな。": "Win, you understand?",
"セイリューとフレイムへの応援依頼については、":
    "As for requesting support from Seiryu and Flame,",
"ハヤテの力を使えるウィンに頼みたい。":
    "I'd like to rely on you, who can use Hayate.",
"話が終わったのであれば、ウィン、":
    "If the talk is done, Win,",
"いますぐ旅立つのだ！！": "depart at once!!",
"まずはセイリューへと…": "First, to Seiryu...",
"その必要ならないぜーーーーーーーー":
    "No need for that—",
"風の紋章の継承者…　": "Inheritor of the Wind Crest...",
"そして我が王国の騎士、ウィンよ。":
    "and knight of our kingdom, Win.",
"そなたに重大な任務を与える…":
    "I entrust you with a grave mission...",
"南の暗黒大陸に向かい、光の柱の立った地を":
    "Head to the Dark Continent in the south and",
"調べるのだ！！": "investigate the land where the Pillar of Light rose!!",
"ええい！　ウィン、何とか申せ！":
    "Bah! Win, say something!",
"陛下…　やはり俺から順序立ててウィンには":
    "Your Majesty... I think it best that I explain",
"説明した方がよろしいかと…。":
    "things to Win in order...",
"南の暗黒大陸については、この国では":
    "Regarding the southern Dark Continent, most in",
"ほとんどのものが、まず、その存在すら":
    "this kingdom don't even know of its existence,",
"知りません。　きっと、ウィンも…。":
    "let alone anything else. Surely Win too...",
"むう、わしもロイどのから教えられるまでは":
    "Hmm, I myself had never heard of it",
"聞いたこともなかったからのう…。":
    "until Lord Roi taught me...",
"…そうか。　では、ロイ、頼む。":
    "...I see. Then, Roi, if you will.",
"は。": "Yes.",
"ウィン、お前も先日、南の山脈の空…":
    "Win, the other day, you too saw, in the sky over the southern mountains...",
"そこに、巨大な光の柱が立つのを見ただろう。":
    "a colossal pillar of light rising there, didn't you.",
"あの場所は、かつて暗黒大陸と呼ばれていた、":
    "That place is an uncharted, uninhabited, forgotten land",
"未開の、無人の、忘れ去られた土地なのだ。":
    "once called the Dark Continent.",
"かつてあの地に橋をかけたが、そこから大量の":
    "Long ago, a bridge was built to that land, but a flood of",
"凶暴な魔物が流れ込み、この大陸のひとびとが":
    "vicious monsters poured across, and many people of",
"たくさん死んだのだ。": "this continent died.",
"しかも橋を渡り、向こう側へ渡ったものは、":
    "Moreover, all who crossed the bridge to the other side",
"すべて何かの病気にかかり、すぐに死んで":
    "fell to some illness and died",
"しまったという…。": "almost at once...",
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
