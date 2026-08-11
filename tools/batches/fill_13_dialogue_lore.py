#!/usr/bin/env python3
"""Fill batch 13: worldbuilding books (shamshir, curry, Seiryu, knight order)."""
import csv
import os
import re

D = {
"時代…？何を言っている！？": "An age...? What are you talking about!?",
"ひとの名前に対してもう少し敬意を払え！":
    "Show a little more respect for people's names!",
"礼儀以前の問題だぞ、そこは！！":
    "That's basic decency, you know!!",
"私には他にもたくさんやることがあるのだ…":
    "I have plenty of other things to do...",
"よく喋る魔物だぜ…": "Talkative monster, aren't you...",
"その減らず口、いますぐ…　　なに…！？":
    "That lip of yours, right now— ...What!?",
"お帰りかい。ありがとよ。": "Welcome back. Thanks.",
"いらっしゃい。少しばかり南の品も":
    "Welcome. I've got a few goods",
"置いているよ。": "from the south too.",
"騎士さま、ヘビに噛まれるみたいですぞ":
    "Sir Knight, I see you getting bitten by a snake.",
"えー　ああ　そう…": "Uh— oh, I see...",
"おー、騎士さま、ここでお会いしたのも運命！":
    "Oh, Sir Knight, meeting you here must be fate!",
"よかったら占ってさしあげましょうぞ！":
    "Shall I tell your fortune?",
"うーむ　むむむむ…　見えてきた": "Hmm, mmm... I can see it now.",
"ヘビに噛まれるのが見えるー…":
    "I see you getting bitten by a snake~...",
"はい、確かにお金はいただきましたよ。":
    "Yes, I've certainly received your payment.",
"ゆっくり休んでいきなされ。": "Rest easy here.",
"いらっしゃい、ここは国から国へと移動する":
    "Welcome. This is an inn for people traveling",
"もうとっくにお日様が昇っているよ。":
    "The sun's been up for a while now.",
"そろそろ出立なさったらどうだい？":
    "How about setting off soon?",
"行商人や旅人のための宿屋だよ。":
    "from country to country—merchants and travelers.",
"お金が足りないみたいだね…。":
    "Looks like you don't have enough money...",
"悪いけれど、また今度来てくださいね。":
    "Sorry, but please come back another time.",
"はいはい、一泊で５０Ｇだよ。": "Sure, sure, 50G a night.",
"休んでいきなさるかい？": "Would you like to rest?",
"西にも行けない、国にも帰れない…":
    "Can't go west, can't go home...",
"あー、ウィンダムに行ってみるかー":
    "Ah, maybe I'll try Windam...",
"ごはんまずいんだよなあ、あそこー":
    "though the food there is bad...",
"兄ちゃん一個でいいから買ってってよ！":
    "Big bro, buy just one, please!",
"また来てくれよ！": "Come again!",
"…クーン": "...Yip",
"『シャムシールの扱い』": '"Handling the Shamshir"',
"少ない力と動きで深く鋭く切り込めるのが特徴である。":
    "Its hallmark is deep, sharp cuts with minimal strength and movement.",
"その為、腕力だけでなく、技量によっても多様な使い方、":
    "Thus, depending on skill rather than brute force, it allows diverse",
"戦法をとれる。": "uses and tactics.",
"何より小回りが利き、素早さが上がる点が優れている。":
    "Above all, its agility and quick handling are its strengths.",
"シャムシールとはフレイム王国に古来より伝わる":
    "The shamshir is the most representative and beloved sword",
"最も代表的で最も愛されている刀剣である。":
    "passed down in the Flame Kingdom since ancient times.",
"他の国の刀剣類と比べると、刀身が反り返っており、":
    "Compared to other nations' blades, its blade curves back, and",
"『王家の方々の好きなカレー』":
    '"The Royal Family\'s Favorite Curries"',
"ホムラ王子は緑色、特にほうれん草ベースでたくさんの":
    "Prince Homura likes green curry, especially spinach-based",
"野菜が溶け込んだカレーを好む。油は決して入れ過ぎない。":
    "with plenty of vegetables melted in. Never overdo the oil.",
"辛さにも強くはない。野菜のうま味が決め手。王家の中では":
    "He can't take much heat either. The vegetables' savor is key. Among the royals,",
"母親譲りの好みなのかも知れない。":
    "it might be a taste inherited from his mother.",
"ホノオ王子は完全に辛党であり、油も大好きである。":
    "Prince Hono is a complete chili-head and loves oil.",
"しかし味音痴というわけではないので、ちゃんと辛く、":
    "But he's not tasteless—he wants it properly spicy,",
"濃く、うま味のあるものが望ましい。色は何でもＯＫ":
    "rich, and flavorful. Any color is fine.",
"のようである。": "Apparently.",
"フレイム王はもっぱら赤いカレーである。常に赤だけで":
    "King Flame exclusively eats red curry. Red alone is always",
"ＯＫ。しかし唐辛子をたくさん入れればいいというわけ":
    "fine. But it's not about loading it with chili peppers.",
"ではない。辛党なわけではなく、唐辛子の味が好きなのだ":
    "He's not a spice lover; he simply likes the taste of chili.",
"と思われる。油や他スパイスで調整せよ。":
    "Adjust with oil and other spices.",
"えっ？　牢屋じゃないよ。": "Huh? This isn't a jail.",
"ここは家畜小屋さ。": "It's a livestock shed.",
"『王のいないセイリュー』": '"Seiryu, the Land Without a King"',
"セイリューでは、大昔から、漁をしてきた一族、大工をして":
    "In Seiryu, since ancient times, there have been families of fishers, carpenters,",
"きた一族、作物を育ててきた一族、鍛冶をしてきた一族…":
    "farmers, smiths...",
"といった風な、複数の特権技術を持った一族がたくさん":
    "many clans each holding exclusive skills,",
"おり、それらの間での調停役といった感じである。":
    "and the lord acts as a mediator between them.",
"そういったそれぞれの分野のエキスパート達から困りごとや":
    "When those experts bring problems or new ideas to him,",
"新しいアイデアを相談されると、その解決策を他の":
    "he asks other experts to solve them—that's",
"エキスパートに領主がお願いするという形での統治である。":
    "how his governance works.",
"そして領主は代々早死にが多い。":
    "And the lords have, for generations, tended to die young.",
"セイリューには王がおらず代わりに領主という代表者が":
    "Seiryu has no king; instead, a representative called the lord exists,",
"存在するが、その統治の実態には他の王国とは違う点が":
    "but the reality of its rule differs from other kingdoms",
"多い。領主は代々同じ一族が継ぐが、独自の軍隊はなく、":
    "in many ways. The same clan inherits the lordship, but there's no standing army",
"税金もない。領民からの善意の寄付のみで生活している。":
    "and no taxes. They live solely on the people's goodwill donations.",
"『ウィンダム王国の騎士団とは』": '"The Windam Knight Order"',
"ウィンダム王国では、騎士が王に次いで最も地位が高く、":
    "In the Windam Kingdom, knights rank highest after the king,",
"法律上では市民の財産没収などの権限もあるが、試練に":
    "and legally have powers like seizing citizens' property, but since trials",
"おいて品行方正さや誇り高さも評価の対象となる為、":
    "also assess upright conduct and pride,",
"実際には蛮行は起こっていない。":
    "no such outrages occur in practice.",
"そして王の命令ひとつで騎士の階級は即時はく奪もできる。":
    "And a single royal order can instantly strip one of knighthood.",
"しかし騎士が自ら返上することも禁じられている。":
    "Yet knights are also forbidden from renouncing it themselves.",
"このように、実質的に騎士という階級は、特権階級とは":
    "Thus, while knighthood is a privileged class, it is, in effect,",
"いえ、厳しく制限された、象徴的でしかない階級とも言える。":
    "a strictly limited, merely symbolic rank.",
"ウィンダム王国では騎士団と自らが呼ぶ独特の制度がある。":
    "The Windam Kingdom has a unique system it calls the knight order.",
"煌びやかな鎧兜に身を包み、高い給料と身分を約束された":
    "Dressed in glittering armor and promised high pay and status,",
"特権階級であるが、世襲制ではなく、試験制度で選ばれる。":
    "they are a privileged class, yet not hereditary—chosen by examination.",
"『階級ということ』": '"On Social Classes"',
"この地における、階級の存在について、フレイム王国の":
    "One must say the people of the Flame Kingdom give little thought",
"人々は意識が少ないと言わざるをえない。確かに厳しい":
    "to social class. Truly, they aren't bound by harsh laws; everyone is free.",
"法律で縛られることもない、ひとびとはみな自由で、":
    "Everyone is free and unbound by harsh laws.",
"しかし、物乞いが努力することで商人たちのように金を":
    "But can a beggar, through effort, grow rich like the merchants?",
"儲けられる国だろうか？兵士が王族のような指揮官、":
    "Can a soldier become a commander or general like royalty?",
"将軍になれるだろうか？農民や大工に学問を学べるような":
    "Do farmers and carpenters get chances to study?",
"機会があるだろうか？": "Do they?",
"フレイム王国はとても栄えており、旅先の目的地としても、":
    "The Flame Kingdom prospers—as a travel destination,",
"商売の場所としても、剣術に、技術、特に食文化の豊かな":
    "a place of trade, of swordsmanship and craft, and above all",
"地としても大陸随一である。それなのに、貧しいひとたち、":
    "richest in food culture on the continent. Yet there are still poor people,",
"他の地で見られない物乞いのひともたくさんいる。":
    "and more beggars than anywhere else.",
"『継承の試練』": '"The Trial of Succession"',
"南の遺跡の試練で何をするか、何が起こるかは、":
    "What happens in the Southern Ruins' trial is known",
"継承者にしか分からない。つまり、国王にしか":
    "only to the inheritor—that is, only to the king.",
"分からない。そしてそこで何が起こったかは、":
    "And what happened there",
"生涯口外してはならない。": "must never be spoken of, for life.",
"本当に国王となる資質があるか、火の紋章の継承者としての":
    "It can only be said that it tests whether one truly",
"資格があるかどうかを、試される場なのだとしか言えない。":
    "has the makings of a king and the right to the Fire Crest.",
"フレイム王国の王となるもの、火の紋章の継承者となる者は":
    "Those who would become king of Flame and inheritor of the Fire Crest",
"必ず南の遺跡の試練を越えねばならない。":
    "must pass the trial of the Southern Ruins.",
"越えられない場合、挑戦しない場合には、次点の継承候補者":
    "Should they fail or refuse, the right passes",
"にその権利が移行する。": "to the next candidate.",
"『ウィンダム王国との戦争について』":
    '"On the War with the Windam Kingdom"',
"フレイム王国の兵士よりも優れています。":
    "Our soldiers surpass those of the Flame Kingdom.",
"しかし、装備や訓練に時間とお金をかけている分、":
    "But the time and money we pour into equipment and training",
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
