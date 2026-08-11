#!/usr/bin/env python3
"""Fill batch 42: crest plan discussion, Shizuku's illness, gifts."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"なあナガレよー…": "Hey, Nagare...",
"おまえ、なんでそんなに龍をぶちのめす":
    "why do you keep going on about",
"ばかり言ってるんだ？": "beating up the dragon?",
"…あ？": "...Huh?",
"だってよー…": "Well...",
"大事なのは水の紋章を継承することだぞ？":
    "What matters is inheriting the Water Crest, right?",
"あたしの紋章、やっぱり偽物なのか！？":
    "So my crest really is a fake!?",
"水の紋章がねえと、": "Without the Water Crest,",
"闇のエレメントに対抗できねえんだからよー。":
    "we can't stand against the Dark Element.",
"その為なら、龍と話し合うとか、お願いして":
    "For that, wouldn't you first consider talking to",
"返してもらうとか先に考えるもんじゃねのか？":
    "the dragon, or asking it to give it back?",
"………っ。": ".........",
"こいつらのはあたしのと違う！":
    "Theirs is different from mine!",
"ホノオどの…その件については、":
    "Lord Hono... regarding that matter,",
"ナガレをあまり責めないでやってください…。":
    "please don't blame Nagare too much...",
"詳しくはいま話せませんが…":
    "I can't go into detail now, but...",
"いつか、ご理解いただける日が来ると":
    "I believe the day will come when you",
"思いますので…　なにとぞ…": "will understand... I beg you...",
"え…　ああ、はい…。": "Huh... ah, yes...",
"光るし、魔法使えるし…消えないんだぞ！？":
    "They glow, they work magic... and they don't fade!?",
"そろそろ…この話もしまいにしよう。":
    "Let's... bring this talk to an end.",
"ナガレ。おまえはこれから龍のお社に向かい、":
    "Nagare. You will now head to the Dragon Shrine,",
"その奥の洞窟から、龍の元を目指すのじゃ。":
    "and make your way through the cave beyond to the dragon.",
"ホノオどの、ウィンどの、": "Lord Hono, Lord Win,",
"あなたがたもご協力願えますな？":
    "will you lend your aid as well?",
"水の紋章の継承は、あなたがたにとっても":
    "The succession of the Water Crest is, for you too,",
"いま最も大事なことがらのはず。":
    "surely the most crucial matter at hand.",
"どうぞお二方、こちらへ。": "Please, both of you, this way.",
"二人とも、知っていたのか！？": "You two knew!?",
"ああ！その点はもちろんだぜ！": "Yeah! Of course we did!",
"ありがとうございますじゃ。": "Thank you kindly.",
"それとも、二人とも知らないのか！？":
    "Or do neither of you know!?",
"ナガレよ、決して無茶をするでないぞ。":
    "Nagare, never act rashly.",
"おまえの使命は、龍を倒すことではない…。":
    "Your mission is not to slay the dragon...",
"水の紋章を継承し、真の継承者となり…":
    "but to inherit the Water Crest, become the true inheritor...",
"闇のエレメントの復活を止めることなの":
    "and stop the Dark Element's",
"じゃからな。": "revival.",
"知らないのだったら、闇のエレメントとの":
    "If you don't know, then the battle",
"では、ホノオどの、ウィンどの。":
    "Lord Hono, Lord Win.",
"ナガレをよろしく頼みましたぞ。":
    "I entrust Nagare to your care.",
"戦い、どうなるんだ！？": "against the Dark Element... what becomes of it!?",
"お社の場所なら当然あたしが知っているから、":
    "Of course I know where the shrine is, so",
"あんたらはついてくるだけで大丈夫さ。":
    "you lot just need to follow along.",
"本物の紋章の力があるんだろ？":
    "You've got the power of real crests, right?",
"なあに、龍だってきっと大したことないさ。":
    "Ah, the dragon's probably not all that tough anyway.",
"ビビらないでくれよな。": "Don't chicken out on me.",
"…おう。": "...Yeah.",
"こら、ナガレ！": "Hey, Nagare!",
"客人の前で怒鳴るのはおよしなさい！":
    "Don't shout in front of our guests!",
"あたしの紋章が偽物なら、": "If my crest is a fake,",
"あたしは継承者としても当主としても偽物だ！":
    "then I'm a fake inheritor and a fake head!",
"姉さまは知っていたのか！？":
    "Sis, did you know about this!?",
"ナガレ、あなたは本物の当主であり、":
    "Nagare, you are the true head,",
"継承者です。ただ、これにはわけが":
    "and the true inheritor. It's just that there's",
"あるのです…": "a reason for this...",
"だからそのワケを早く教えろってあたしは…":
    "Then tell me the reason already! I—",
"姉さま！！": "Sis!!",
"ゴホンゴホン…ゴホッゴホッ…":
    "Cough, cough... cough, hack...",
"姉さま、大丈夫か！？": "Sis, are you okay!?",
"さあ、もっと楽な格好をしてくれ…":
    "Come, make yourself more comfortable...",
"ごめんなさい…　大丈夫よ…　":
    "I'm sorry... I'm fine...",
"シズク、やっぱりわしから話すよ。":
    "Shizuku, I'll be the one to tell them after all.",
"おまえさんはそこで楽にしていなさい。":
    "You rest easy there.",
"つらかったら席を外してよいからの。":
    "If it grows hard, you may leave the room.",
"ありがとうございます、オタキ様。":
    "Thank you, Lady Otaki.",
"万金丹を　5個": "5 Mankintan",
"ライスボールを　3個": "3 Rice Balls",
"手渡された！": "handed over!",
"いくつか余っていた薬と…":
    "Some medicine we had to spare, and...",
"うちで採れたコメで作ったごはんです。":
    "rice made from our own harvest.",
"旅先で食べてくださいね。": "Please eat it on your travels.",
"なんとか間に合いました…。":
    "We managed to make it in time...",
"いつもマハリの家からは色々もらってるのに…":
    "We're always receiving so much from Mahari's family...",
"ありがとうな。助かるよ！":
    "Thanks. This helps a lot!",
"うちの一族は、ナガレたちはもちろん、":
    "Our clan exists to feed Nagare, of course,",
"村のみんなを食べさせるためにある家だからね。":
    "but also the whole village.",
"当然のおしごとをしているだけだよ。":
    "We're just doing what's natural for us.",
"ちょっと今年は不作で、あまりたくさん":
    "This year's harvest was poor, so I'm sorry we can't",
"あげられないのが申し訳ないけれど…":
    "give you more...",
"こんなものしかありませんが、":
    "It's all we have to offer, but",
"最近魔物や害虫が多いのも、きっと":
    "The recent surge in monsters and pests is surely",
"闇のエレメントの影響なんだろうな。":
    "the Dark Element's doing.",
"大丈夫。": "Don't worry.",
"あたしが紋章を継承して闇のエレメントとかを":
    "Once I inherit the crest and beat the stuffing out of",
"ぶちのめせば、またみんな腹いっぱいコメを":
    "the Dark Element, everyone can eat their fill of rice",
"食えるようになるさ！": "again!",
"持って行って下さい。": "Please take it with you.",
"そうだね！ナガレ、気を付けてね！":
    "Right! Nagare, be careful!",
"ホノオさんとウィンさんも、お気をつけて！":
    "And you too, Hono and Win!",
"おう！まかせとけって！": "Yeah! Leave it to us!",
"傷薬を　5個": "5 Healing Herbs",
"最近お社の周りは、強い魔物が出る。":
    "Lately, strong monsters appear around the shrine.",
"お二方もいらっしゃるから大丈夫かも知れない":
    "With you two along, you might be fine,",
"けれど…　気を付けて。": "but... be careful.",
"俺たちセイリューの民が使う、つばめ返し…":
    "The secret art we Seiryu folk use—Swallow Reversal...",
"その秘剣を極限まで高められる刀を設計したら":
    "when I designed a blade that could push that secret art to its limit,",
"こうなった…。": "this is what happened...",
"ナガレは物干し竿を受け取った！":
    "Nagare received a Clothes Pole!",
"秘剣つばめ返しを極限まで高められる刀を設計":
    "When I designed a blade to push the secret art of Swallow Reversal",
"したらこうなった…。": "to its limit, this is what came of it...",
"この形の刀を、大太刀と名付けた。":
    "I've named this shape of blade the odachi.",
"ナガレは青江の大太刀を受け取った！":
    "Nagare received Aoe's Odachi!",
"コメの蓄えはなんとか全部持ち出せたけど…":
    "We managed to haul out all the stored rice, but...",
"田んぼに植えていた分は全滅だねえ…。":
    "the crop planted in the paddies is a total loss...",
"だけどいまあるコメはちゃんとみんなと":
    "But we'll share what rice we have with everyone,",
"分け合うから安心しな！": "so don't worry!",
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
