#!/usr/bin/env python3
"""Fill batch 56: Hono's confession, stone-prison duel with Nau."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"なにしてくれたんだああ！？ああああ！！？？":
    "What have you done—!? Aaaaah!!??",
"とっさにツナミを起こして…":
    "I conjured a Tsunami on the spot...",
"向かってくる冷気を全て相殺したのさ…":
    "and canceled out all the incoming cold...",
"つ…、ツナミだああああああ！！！？？":
    "A-A Tsunami—!!!??",
"ミケーネブリザード…　破れたり！！":
    "Mycenae Blizzard... broken!!",
"…ブリザードを打ち消すほど大きなツナミを…":
    "...A Tsunami vast enough to negate a Blizzard...",
"そう、そんなにまで強大な力を持ったのね…":
    "So, you've grown that powerful...",
"ナガレ…　かっこよすぎだぜーーーー！！":
    "Nagare... you're way too cool!!",
"…ウィン、ホノオ。": "...Win, Hono.",
"頼みがあるんだ。": "I have a request.",
"あ、えっ？　は？": "Ah, huh? What?",
"な、なんだよ、急に…？": "W-What is it, all of a sudden...?",
"時間がない、ミケーネをあたしに任せて、":
    "There's no time—leave Mycenae to me,",
"ふたりは先に行ってくれ！！":
    "you two go on ahead!!",
"…！！　な、ナガレ！！": "...!! N-Nagare!!",
"…お、オレ…　なんで大丈夫なんだ…？":
    "...Wh-Why am I... not affected...?",
"ミケーネならあたしだけで大丈夫だ！":
    "I can handle Mycenae alone!",
"さっきのを見たろ？　三人で戦う必要がない！":
    "You saw that earlier, right? No need for three of us!",
"い、いや…": "N-No...",
"でもオマエだけ残していくなんてよー…":
    "but leaving you behind alone...",
"ジャマなんだ、二人は！！": "You two would be in the way!!",
"あんたたち二人をツナミで守りながら戦う自信":
    "I'm not confident I can fight while shielding",
"がない！！": "you both with Tsunami!!",
"…またあの模様に乗ってみても、":
    "...Even if we step on that pattern again,",
"きっと一方通行なんだよな…。":
    "it's surely one-way...",
"わかってる…　バカなこと言ってるよなオレ…":
    "I know... I'm talking nonsense...",
"ナガレの思いに応えるためにも…":
    "To live up to Nagare's feelings...",
"オレたちは行くしかねえんだ…":
    "we have to go on...",
"止まってるヒマなんかねえ…":
    "There's no time to stop...",
"でもよ、ウィン…　": "But, Win...",
"オレ、気が付いちまったんだ…":
    "I've realized something...",
"さっきナガレに任せて先に進んだとき…":
    "When I let Nagare handle it and went ahead earlier...",
"オレはまるでナガレの言葉に納得して…":
    "I acted as if I was convinced by her words...",
"ナガレを信じて先に進んだつもりでいたけどよ…":
    "and thought I was trusting her and moving on, but...",
"ちがう…　全然ちがうんだ…":
    "that's not it... not at all...",
"オレはホッとしたんだよ…":
    "I was relieved...",
"あの恐ろしい氷の魔法と戦わずに済んで…":
    "that I wouldn't have to face that terrifying ice magic...",
"オレはミケーネが怖かったんだ…！！！！":
    "I was afraid of Mycenae...!!!!",
"なんてこった…　オレとしたことがよー…":
    "Damn... I can't believe I...",
"怖かっただけだった…　オレはアイツを信じて":
    "It was just fear... I didn't truly trust",
"任せたわけじゃなかったんだぜ…？":
    "her and leave it to her...?",
"そんな気持ちで…　アイツをひとりで":
    "With that feeling... I left her behind",
"置いてきちまった…　オレは…　オレは…":
    "all alone... I... I...",
"ウィンはホノオの肩をつかんで":
    "Win grabbed Hono by the shoulders",
"うなずいた": "and nodded.",
"ああ…　スマン…": "Ah... thanks...",
"ウィン、サンキュな…": "Win, thanks...",
"行くぜ、ウィン！！": "Let's go, Win!!",
"ハヤテの力で一気に頼む！！":
    "Use Hayate and get us there in one burst!!",
"もう、進むしかねえだろ…ウィン？":
    "We've no choice but to move on... right, Win?",
"どの道すぐにくたばるだろうよ…　ナウー…":
    "You'd croak soon enough anyway... Nau...",
"……ぐ…　ぐ…ふ…　": "......Ng... ng... hah...",
"…オレは行くぜ。　じゃあな、ナウー…":
    "...I'm going. So long, Nau...",
"…勝ったのか？": "...Did you win?",
"…アンタは最後まで、正々堂々だった…":
    "...You fought fair and square to the very end...",
"オレのわがまま…": "My selfish demand...",
"一騎打ちにも応じてくれた…。":
    "you even accepted the one-on-one...",
"敵ながら…": "Even as an enemy...",
"尊敬に値する戦士だったぜ…ナウー":
    "you were a warrior worthy of respect... Nau.",
"…獄滅…石牢陣…！！": "...Prison of Ruin... Stone Prison Array...!!",
"な…何をした…？": "Wh-What did you do...?",
"…我の…最強魔法…　石牢陣…":
    "...My... strongest spell... Stone Prison Array...",
"……っ…　ぐはっ…！！": "......Ngh... Gwah...!!",
"…ホノオ…": "...Hono...",
"その陣の中に入ったオマエは…　もう動けぬ…":
    "You who entered that array... can no longer move...",
"徐々に…　石となる…": "Slowly... you turn to stone...",
"マジか…　動けねえ…　足が…":
    "For real... I can't move... my legs...",
"石になっちまってる…！！！！":
    "they're turning to stone...!!!!",
"…我の　勝ちだ　ぐふっ！！":
    "...My victory. Guh!!",
"…さすがにその傷じゃあ…":
    "...With wounds like that...",
"だけどそれじゃあ強すぎるから…":
    "But that spell is too strong, so...",
"卑怯だから…　自分で禁止してたんだな…":
    "it's cowardly... that's why you banned yourself from it...",
"石化の魔法をよー…": "the petrification spell...",
"それでも最後には自分の美学よりも…":
    "And yet, in the end, you chose your mission",
"果たすべき使命の方を、選んだんだな…":
    "over your own aesthetics...",
"ナウー…": "Nau...",
"それに比べてオレは…　まただぜ…":
    "Compared to you, I... again...",
"使命を忘れて　トドメをさせずに…":
    "forgetting my mission, failing to finish you...",
"このザマだ…": "and look at me now...",
"もう身体の半分が石になっちまった…":
    "Half my body's already turned to stone...",
"どうしようも…ねえ……　くっそーーー…":
    "There's nothing... I can do...... damn it......",
"ナガレ…！　ウィン…！　すまねえ！！":
    "Nagare...! Win...! I'm sorry!!",
"オレはここまでっぽいぜ……　くっ…":
    "Looks like this is it for me...... ugh...",
"くっそおおおおーーーーッ！！！！！！":
    "Dammit—!!!!!!",
"こんなすげえ技があったなら…":
    "If you had a move this incredible...",
"しょっぱなに使えば、オレなんて相手にも":
    "you could've used it from the start, and I'd",
"ならなかったろうによー…": "never have been your match...",
"アンタまで時間稼ぎに出て来ちゃってよー…":
    "Even you came out here to buy time...",
"そんなんで計画大丈夫なのかー？":
    "Is your plan really going to hold up?",
"もうほとんど失敗なんじゃねーのー？？":
    "Hasn't it basically already failed??",
"アンタにはオレ、バシッと勝ってるし…":
    "I beat you soundly, after all...",
"今更またやり合うこともないんじゃねーの？":
    "There's no need to fight again now, is there?",
"へへ…　アンタかい…　ナウーーー！！！！":
    "Heh... So it's you... Nau—!!!!",
"どんどんエレメントパワーが集まってるじゃーん！！":
    "Elemental Power's gathering more and more—!!",
"ヤバッ！！　チョーやる気マンマン！！":
    "Whoa!! Super pumped up!!",
"気合いがハンパなーーーーい！！！！":
    "The energy's off the charts—!!!!",
"てことは、あんれええええええええ？？？":
    "Which means... hey—???",
"あっ　もしかしてキミさー……":
    "Oh, could it be that you're...",
"めちゃくちゃ急いでる感じですかーー？？？":
    "in a huge hurry or something??",
"あっ　そうなんだー": "Ah, I see~",
"アレでしょ？　": "It's that, right?",
"ボクが闇のエレメントと一体になってー…":
    "Me fusing with the Dark Element...",
"魔王になっちゃうのをー": "and becoming the Demon King—",
"止めないとだから？？": "you've gotta stop it, huh??",
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
