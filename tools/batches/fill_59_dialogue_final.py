#!/usr/bin/env python3
"""Fill batch 59 (final): Flame succession, NG+ character select."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"ゆえに、闇の瘴気も薄まって、広がって、飛び散る！！":
    "Thus, the Dark miasma too thins, spreads, and scatters!!",
"なっ…": "Wh-...",
"お、親父！？": "D-Dad!?",
"ホノオ…お前も継承者になり、今回の戦いを":
    "Hono... now that you've become an inheritor and ended this war,",
"終えたなら、分かるはず…": "you should understand...",
"紋章を継承するということは…":
    "What inheriting a crest means...",
"重い使命を負うこと。": "is bearing a heavy mission.",
"王の責務と同時に負えるような軽い物ではない":
    "It is no light burden to carry alongside the duties of a king.",
"…そう…　かも知れねえ。": "...Yeah... maybe so.",
"俺はたまたま戦士だったから何とかなった…。":
    "I managed only because I happened to be a warrior...",
"もしアニキが継承していたらと考えると…":
    "When I think of if big bro had inherited it...",
"紋章は、最も優れた戦士にこそ継承しなければ":
    "The crests must be passed to the finest warriors—",
"ならん…　わしはそれがこの度よくわかった。":
    "this war has taught me that well.",
"そしてピピン殿…": "And Lord Pipin...",
"あなたはまさに、最も優れた戦士だ。":
    "you are exactly that: the finest warrior.",
"本来、我々ではなく、あなたにこそ…":
    "Truly, it is you—not us—who",
"紋章の未来を決める資格があるのだ。":
    "deserves to decide the crests' future.",
"おお…！！　ホノオ！！": "Oh...!! Hono!!",
"すぐに、その決心をつけろとは言わん…。":
    "I won't ask you to decide right away...",
"時間はたっぷりとあるのだ。": "There's plenty of time.",
"考えてもらえまいか…？": "Won't you think it over...?",
"……はあ…": ".........Sigh...",
"よくぞ帰った！！": "Welcome back!!",
"総監督　　　まりも": "General Director: Marimo",
"お帰りなさいませ、ホノオ王子！！":
    "Welcome home, Prince Hono!!",
"いやあ、立派になられましたな！！":
    "My, you've become quite the man!!",
"元々立派だっつーの！！": "I was already great!!",
"それには同意できませんが…":
    "I can't quite agree with that...",
"以前とは違う風格のようなものを、":
    "But you've certainly gained a certain bearing",
"確かに備えられましたな…。": "unlike before...",
"今日くらい悪口入れずに褒めてくれよ…":
    "For once, could you praise me without a jab...",
"いや、ホノオ！": "No, Hono!",
"お前は既に、フレイム王に相応しい男だ！":
    "You are already a man worthy of being King of Flame!",
"へへ、親父はちっと褒めすぎだな！":
    "Hehe, you're overpraising me, Dad!",
"わしもそろそろ身体が言うことを聞かん…":
    "My body no longer obeys me...",
"ならばこれを機に、お前に王位を継承したいと":
    "So I'd like to take this chance to pass the throne",
"考えているのだ…": "to you...",
"ちょ、ちょっと待ってくれよ親父！":
    "W-Wait a moment, Dad!",
"そんなに具合が悪いのか！？": "Are you that unwell!?",
"今日は調子がよく、こうして立っているが…":
    "Today I feel well enough to stand, but...",
"昨日まではずっと寝たきりだった…":
    "until yesterday, I was bedridden...",
"いまのわしに王の仕事は務まらんのだ。":
    "I can no longer perform the king's duties.",
"そ、そうだったのか…": "I-...I see...",
"スマン、親父…　オレ全然気づかなかったぜ…":
    "Sorry, Dad... I didn't notice at all...",
"…大事な話をしているところ悪いが…":
    "...Sorry to interrupt your important talk, but...",
"…俺の火の紋章をフレイムに返したい。":
    "...I'd like to return the Fire Crest to Flame.",
"しかしどうも…　": "But it seems...",
"うむ…。わしは勿論一度継承しておる…":
    "Indeed... I, of course, have already inherited once...",
"そして一族もわしとホノオしかおらぬのでな。":
    "and our family now consists only of me and Hono.",
"…どうすれば…？": "...What can we do...?",
"オレの子どもが出来るまで持っていてくれ！":
    "Hold onto it until I have a child!",
"…クッ！　やっぱりか…！":
    "...Hmph! Just as I feared...!",
"ていうかよー…": "And hey...",
"もしオレに、ナガレでも同じだけどさ、":
    "Even if I—same for Nagare—had a child,",
"子どもが出来たとしても…": "you know...",
"すぐには継承できないぞ？": "the child can't inherit right away, right?",
"だって、継承はこころから信頼している相手に":
    "Because a crest can only pass to someone you",
"しか出来ないからな。": "truly trust.",
"…な、んだと…！！！？": "...Wh-What...!!!?",
"しかし、二周目も用意した！！":
    "But I've also prepared a second playthrough!!",
"基本的には一周目と同じなんだが…":
    "It's basically the same as the first, but...",
"難易度その他、幾つかイベントの変更もある！":
    "difficulty and several events have changed!",
"いい意味でも、悪い意味でも何かが起こる！！":
    "Something will happen—for better or worse!!",
"ふつーに読み逃した本や手に入れそこなった":
    "You might also find books you missed or items",
"アイテムを探してもいいかもね！！！":
    "you failed to get!!",
"ではでは本当にこれで終わりーーー":
    "Well then, this really is the end—",
"どうせなら、一応二周目をはじめてセーブする":
    "Might as well start a second playthrough",
"二周目してくれてもいいんだからね！！":
    "and save it, you know!!",
"しかし、実は３周目も用意した！！":
    "But actually, I've even prepared a third playthrough!!",
"でも今度は変更はない！！はず！！！！":
    "Though this time, there are no changes!! ...probably!!!!",
"レベル９９にして作者にすくしょを見せよう！":
    "For those odd folks who take 'get to level 99",
"とかを本気にしちゃったちょっとおかしなひと":
    "and show the author a screenshot' seriously...",
"向け…かも知れない…": "this one might be for them...",
"ではではまたまたこれで終わりーーー":
    "And so, once again, this is the end—",
"どうせなら、一応三周目をはじめてセーブする":
    "Might as well start a third playthrough",
"３周目してくれてもいいんだからね！！":
    "and save it, you know!!",
"ここからは正体不明の世界の":
    "From here, a battle in an unknown world",
"まず火の紋章の継承者を":
    "First, choose the Fire Crest inheritor.",
"選んでください": "Select your Fire Crest inheritor.",
"ホノオ　…　バランス型　素早さと力がやや高め":
    "Hono    ... Balanced: agility and strength a bit high",
"フレイム王…　パワー型　力と体力多め":
    "King Flame ... Power: high strength and HP",
"ホムラ　…　魔力型　魔力高め　他低め":
    "Homura   ... Magic: high magic, low elsewhere",
"不可思議なダンジョンをひたすら進む":
    "pressing ever deeper through an eerie dungeon",
"次に水の紋章の継承者を選んでください":
    "Next, choose the Water Crest inheritor.",
"ナガレ　…　パワー型　力とぼうぎょ高め":
    "Nagare   ... Power: high strength and defense",
"シズク　…　魔力型　魔力高め　他低め　":
    "Shizuku  ... Magic: high magic, low elsewhere",
"ことになります": "that is what will happen.",
"オタキ　…　バランス型　力と魔力高め":
    "Otaki    ... Balanced: high strength and magic",
"次に風の紋章の継承者を選んでください":
    "Next, choose the Wind Crest inheritor.",
"ウィン　…　スピード型　素早さと会心率、回避率高め":
    "Win      ... Speed: high agility, crit, and evasion",
"ロイ　　…　バランス型　力と魔力高め":
    "Roi      ... Balanced: high strength and magic",
"サクソン…　パワー型　力と体力多め":
    "Saxon    ... Power: high strength and HP",
"最後に継承者ではないメンバーを選んでください":
    "Finally, choose a non-inheritor member.",
"ピピン　…　バランス型　力素早さ魔力など高め":
    "Pipin    ... Balanced: high strength, agility, magic",
"ウィンダム王…　パワー型　力と体力高め":
    "King Windam ... Power: high strength and HP",
"攻略メンバー４人を選んでください":
    "Choose your party of four.",
"トリカゼ　…　スピード型　力と素早さ高め":
    "Torikaze ... Speed: high strength and agility",
"マハリ　…　魔力型　魔力と素早さ高め":
    "Mahari   ... Magic: high magic and agility",
"メンバーは途中で変更できません":
    "Party members cannot be changed mid-run.",
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぜんドッグじゃなかったぞ…！？":
    "It was anything but a dog...!?",
"ウィン、中々やるじゃないか…お前。":
    "Win, you're quite something... you know that.",
"力のエレメントを手に入れた！": "Obtained a Power Element!",
"水のエレメントを手に入れた！": "Obtained a Water Element!",
"守りのエレメントを手に入れた！": "Obtained a Guard Element!",
"「うるさい！！問答無用だああああああ":
    '"Shut up!! No questions—',
"「いまの俺なら、もうお前たちには負けん！！":
    '"With my current self, I won\'t lose to you!!',
"　かかってこい！！！": " Come at me!!!",
"「待っていたぞ！！": '"I\'ve been waiting!!',
"　俺は何度でも蘇る！！": " I will be reborn again and again!!",
"ドラゴンバスターを手に入れた！":
    "Obtained a Dragon Buster!",
"藤四郎（大業物）を手に入れた！":
    "Obtained a Toshiro (Great)!",
"村雨を手に入れた！": "Obtained a Murasame!",
"50000\\G 手に入れた！": "Gained 50000G!",
"ロングソード（匠）を手に入れた！":
    "Obtained a Long Sword (Master's)!",
"骨喰みを手に入れた！": "Obtained a Honebami!",
"藤四郎を手に入れた！": "Obtained a Toshiro!",
"グレートソード（匠）を手に入れた！":
    "Obtained a Great Sword (Master's)!",
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
