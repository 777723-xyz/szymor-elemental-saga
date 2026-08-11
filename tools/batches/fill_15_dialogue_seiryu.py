#!/usr/bin/env python3
"""Fill batch 15: Southern Ruins trial, Seiryu village homecoming."""
import csv
import os
import re

D = {
"お、おい…急になんかそういうの、よそうよ…":
    "H-Hey... let's not suddenly get all... you know...",
"大丈夫、ここ道具屋。": "No worries, this is the item shop.",
"ちゃんと手入れをしろよ…。": "Take good care of it...",
"いい武器は一生物だ…。": "A good weapon lasts a lifetime...",
"…客か。": "...A customer.",
"お前さん…　龍の涙を持っていたりしないか？":
    "You there... you wouldn't happen to have a Dragon's Tear?",
"ほとんど伝説上の宝石じゃ…": "It's practically a legendary gem...",
"もし本物を持ってきてくれたら…":
    "If you bring me a real one...",
"わしの秘蔵する、ある奇書と交換してもよい…":
    "I might trade it for a certain rare tome I keep hidden...",
"だが、信用できる者にしか、その本を":
    "But it'd be best to hand that book only",
"渡さない方がよいぞ…": "to someone you can trust...",
"あー、多分、お前の力はそんなものかとか、":
    "Ah, things like 'so that's about all the power you've got,'",
"ウィンはハヤテとカマイタチの魔法をおぼえた！":
    "Win learned the Hayate and Kamaitachi spells!",
"ホノオはバクハツとキョウセンシの魔法をおぼえた！":
    "Hono learned the Explosion and Warrior spells!",
"な、なんだ！？": "Wh-What!?",
"紋章が光り出して…何か魔法をおぼえた！！":
    "The crest started glowing... and I learned a spell!!",
"勝てるんじゃないか…コレなら…":
    "With this... maybe I can win...",
"なんかそういうことを言っている顔だな…":
    "You've got that look on your face...",
"何だかさっきまでのオレとは違う感じだぜ！":
    "I feel different from the me of a moment ago!",
"…我は闇の四天王のナウ―…":
    "...I am Nau, one of the Four Dark Generals...",
"紋章の勇者たちよ…　その力見せてみよ…":
    "Heroes of the crests... show me your power...",
"しゃ…しゃべったーーーーーーーーーーー！！":
    "It... it talked—!!",
"勝ったぜー！！": "I won!!",
"…ピンピンしてない？": "...You're still kicking, huh?",
"…で、どうなんだろ、試練の方は…":
    "...So, how's the trial going, anyway...",
"やっぱり不合格か？": "Did you fail after all?",
"…………試練は": "............The trial",
"（また喋った…）": "(It talked again...)",
"…………我は試練、関係ない":
    "............The trial, I care not for it",
"…………試練は、我の後ろに": "............The trial lies behind me",
"わかってるって…　オレは絶対にこの試練を":
    "I know, I know... I absolutely have to",
"乗り越えないといけないんだ…":
    "overcome this trial...",
"まだまだ諦めねえぜ…！！": "I'm not giving up yet...!!",
"……………………（汗": "............(sweat)",
"……と、言う夢を見た。": "...And that's the dream he had.",
"ぜえ…ぜえ…": "Hah... hah...",
"コレ絶対に無理だ…　オレは勝てない…":
    "This is absolutely impossible... I can't win...",
"………（ホノオの背後を指差す":
    ".........(He points behind Hono)",
"くそーーー　つえーーー！！": "Damn— so strong—!!",
"え？": "Huh?",
"うしろ…？": "Behind...?",
"ん？　お前誰だ？": "Hm? Who are you?",
"城の奴らが連れ戻しに来させたのか？":
    "Did the castle folks send you to bring me back?",
"ったく…　まあ、でも…": "Jeez... well, but...",
"オレぜんぜん試練越えられなかったからなあ。":
    "I couldn't get past the trial at all, you know.",
"このまま帰るのなんて、ダセえけど…":
    "Going back like this is lame, but...",
"仕方ないか。": "Guess it can't be helped.",
"よし、じゃあかえ…": "Alright, let's head ba—",
"うわあ！なんだ、おい！？": "Whoa! What the—!?",
"まだやるのかよ！？": "Are you seriously still going!?",
"オレは試練あきらめて…": "I've given up on the trial...",
"任せておいてくれると助かるよ。":
    "I'd be glad if you left it to me.",
"分かった。でも、狩り以外でも何か助けが":
    "Got it. But if you need help with anything beyond hunting,",
"いるなら、気兼ねしないで話してくれよ？":
    "don't hesitate to say so, alright?",
"北の村でもか…。助けはいらないのか？":
    "In the northern village too...? You don't need help?",
"ああ、むしろ狩人たちの邪魔になるから、":
    "Nah, in fact we'd just get in the hunters' way, so",
"道中どうぞお気をつけて…":
    "please do be careful on the road...",
"お手持ちのお金がたりませんね…":
    "You don't have enough money...",
"セイリューに行きたい？": "You want to go to Seiryu?",
"ここも一応セイリューだけど。":
    "This is Seiryu too, technically.",
"わかってるよ、領主の村に行きたいんだろ。":
    "I know, you want to go to the lord's village.",
"ここからどんどん北に行けば着くよ。":
    "Head north from here and you'll reach it.",
"大きな村が見えてくるからすぐ分かる。":
    "You'll see a big village, so it's easy to tell.",
"お前こんなところに何しに…？":
    "What are you doing in a place like this...?",
"ちょっと寄り道しただけさ。": "Just taking a little detour.",
"それよりなんだよ、その驚きようは？":
    "Anyway, why the surprise?",
"いや…　あの悪ガキが突然きれいになって":
    "Well... that little brat suddenly showed up all clean,",
"やって来るもんだからこころの準備が…":
    "and I wasn't prepared for it...",
"え、本当にナガレなんだよな？":
    "Wait, you're really Nagare, right?",
"褒められてんだか貶されてんだかわからん！":
    "I can't tell if that's a compliment or an insult!",
"よう、バモヤシ。おひさ！": "Yo, Bamoyashi. Long time no see!",
"うお！？ナガレ！？": "Whoa!? Nagare!?",
"旅人かい？": "A traveler, are you?",
"なにもなくってガッカリしただろ。":
    "Bet you're disappointed there's nothing here.",
"まあ、よかったらお茶でも飲んでいけば？":
    "Well, why not have some tea if you like?",
"あ、ナガレじゃん。": "Oh, it's Nagare.",
"せっかく来たんだし、よかったら":
    "Since you came all this way, why not",
"お茶でも飲んでいけば？": "have some tea?",
"セイリューとの連絡に用いられている手紙類だ":
    "These are letters used to keep in touch with Seiryu.",
"あらいらっしゃい。": "Oh, welcome.",
"コメならここでは買えないよ。": "You can't buy rice here.",
"領民で分けあっているものだから。":
    "It's shared among the villagers.",
"だけど宿の食事とか、あと行商人から":
    "But you can get it in inn meals, or buy portable",
"携帯食のライスボールが買えたりするから、":
    "rice balls from the peddlers,",
"食べることはできるんだよ。": "so you can still eat.",
"はい…": "Yes...",
"龍のお社は村を出て東へ向かえば見えてきます。":
    "Leave the village and head east, and the Dragon Shrine will come into view.",
"それと…": "Also...",
"旅立ちの前に、部屋の外にいる、":
    "Before you set out, try talking to",
"トリカゼとマハリに話し掛けてみて下さい。":
    "Torikaze and Mahari, who are outside the room.",
"何やら用意してくれているものがあるようです。":
    "It seems they've prepared something for you.",
"きっともう少しの辛抱さ！": "A little more patience, surely!",
"ちゃんとごはん食べて元気出そう！":
    "Eat properly and keep your spirits up!",
"えらいことになったね…": "This is quite the situation...",
"でも、こういうときの為にも薬類は":
    "But it's for times like this that we stock",
"たくさん揃えてあるよ！": "plenty of medicines!",
"まだ新作の刀は出来ていない…。": "The new blade isn't done yet...",
"洪水のせいで鍛冶場に行けなくなっちまった":
    "The flood kept me from getting to",
"からな…": "the forge...",
"ちょうど洪水の前に、": "Just before the flood,",
"行商人が置いて行った他国の武具もあるぞ。":
    "a peddler left behind some foreign arms.",
"な、なんだーーー！？": "Wh-What the—!?",
"この洗濯物を干す棒みてーな刀はよ！？":
    "This blade looks like a clothes-drying pole!",
"ナガレ、遂に新作が完成したぞ。":
    "Nagare, the new blade is finally done.",
"そ、そうなんだ…？": "R-Really...?",
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
