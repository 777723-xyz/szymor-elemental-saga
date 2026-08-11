#!/usr/bin/env python3
"""Fill batch 53: castle town aftermath, rare book gift."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"雨漏りどころじゃなくなっちゃったね…":
    "It's gone well past a leak now...",
"でもお城が無事でよかったよ…　うん…":
    "But I'm glad the castle is safe... yeah...",
"だよな…。": "Yeah...",
"でもオレ、あのとき、なんかグッと来たぜ…":
    "But man, that moment really hit me...",
"お前は正しかったと思うよ！":
    "I think you were right!",
"ウィン！　大丈夫か！？": "Win! Are you all right!?",
"ピピンの件…　大変だったな。":
    "The Pipin matter... that must've been rough.",
"マジかよ…お前、タフだなあ。":
    "For real... you're tough, man.",
"なんだか、自分が偉くなった気がするよな！":
    "Makes you feel all important, huh!",
"いや、あんた元々王子さまだから…。":
    "No, you were already a prince...",
"あーいそがしいいそがいい！": "Ah, so busy, so busy!",
"継承者さまって、なにげに初めて言われた。":
    "I've been called 'inheritor-sama' for the first time in a while.",
"忙しいんですよーーー！！！！！！！！！":
    "I'm busy—!!!!!!!",
"私はあなたの騎士団長就任の際については、":
    "As for your appointment as Knight Commander,",
"断固反対させていただきますからね………":
    "I shall firmly oppose it......",
"覚悟しておいてくだされ！！！！！！！！":
    "Be prepared for that!!!!!!!",
"騎士どの…": "Sir Knight...",
"さすがにいまは、お分かりいただけるはず…":
    "Surely now, you must understand...",
"お分かりになるなら、なぜ！！？":
    "If you understand, then why!!?",
"わたしに！？　話しかけたのです？？？？":
    "Me!? You spoke to me???",
"あんなに立派だったお城が…":
    "That magnificent castle...",
"ひどいもんだねえ…": "what a mess...",
"南の空が真っ赤に燃えるのを見たという者も":
    "Some say they saw the southern sky",
"おるとか…　": "burn bright red...",
"じゃが、この子らにそんなことは言えん…":
    "But I can't say such things to these children...",
"わたし、マイ、よろしくね！": "I'm Mai, nice to meet you!",
"フレイムの王子のオレがこんなに元気だぜ！":
    "I'm the Flame prince, and I'm full of energy!",
"きっとみんなも元気だ！": "Everyone's surely fine too!",
"わーい、王子さまだ！": "Yay, it's the prince!",
"フレイムの家族が気になるけれど…":
    "I'm worried about my family in Flame, but...",
"しばらくはここを出られないみたいで…":
    "it seems I can't leave here for a while...",
"俺たちにはおまえにしてやれないんだからさ":
    "There's nothing we can do for you, you know.",
"おっ、疲れたかー？": "Oh, tired?",
"おまえが来たら、優先してベッドを":
    "When you come, we'll give you",
"オレらはまだまだ元気だぜ！":
    "We're still full of energy!",
"おっ、おまえら！": "Oh, you lot!",
"俺たちにはおまえらにしてやれないんだからさ":
    "There's nothing we can do for you, you know.",
"疲れたかー？": "Tired?",
"おまえらが来たら、優先してベッドを":
    "When you come, we'll give you",
"宿に置いてきた食材…もう全部腐ってしまった":
    "The ingredients I left at the inn... they've all",
"ろうなあ…。": "rotted by now, surely...",
"帰宅許可が出るまで、城から出られないんです…":
    "I can't leave the castle until I'm given leave to go home...",
"こいつ本当に兵士かよ、極めてるぞ。":
    "Is this guy really a soldier? He's extreme.",
"わーいおしろだおしろだーーーー！！":
    "Yay, a castle, a castle—!!",
"ありがとう、ウィン！": "Thanks, Win!",
"お城のみんながお腹いっぱいでいられるよう、":
    "So everyone in the castle can eat their fill,",
"私もがんばるから、ウィンもがんばんなさい！":
    "I'll do my best too—you do your best as well!",
"あら、まだパンが嫌いなの？": "Oh, still not fond of bread?",
"騎士様になって、普段いいものばかり":
    "Now that you're a knight, are you eating",
"食べているのかしら！？": "nothing but the fine stuff!?",
"元気そうね…　よかった！！":
    "You look well... what a relief!!",
"ほら、パン持っていきなさい！": "Here, take some bread!",
"あ、でもお金は貰うよ！": "Ah, but I'll take your money!",
"おとなだからね、自分のお金で払おう！":
    "You're an adult now—pay with your own money!",
"ウィン！！　無事だったな！！":
    "Win!! You're safe!!",
"よかった！！": "What a relief!!",
"父さんたちもこの通り元気だ！":
    "Your dad and the others are all well, see!",
"心配しないで、仕事に精を出しなさい。":
    "Don't worry—just focus on your duties.",
"こんな時代だけど、夢は諦めてないんです…":
    "Troubled times as these, but I haven't given up my dream...",
"お金貯めて、大きなラボを作るんだ！":
    "I'll save up and build a big lab!",
"めっちゃ在庫少なくなっちゃったんだけど…":
    "My stock's gotten awfully low, but...",
"仕方ない！　騎士様には売っちゃいます！":
    "Oh well! I'll sell to the Sir Knight anyway!",
"吾輩は現在王国の被害状況を調べているので":
    "I am currently surveying the kingdom's damage,",
"あーる！": "yessir!",
"他国の情報もまとめているのであーる！":
    "I am also compiling intel on other lands, yessir!",
"民が苦しんでいるときに、領主だけいいモン":
    "When the people suffer, the lord can't be the only",
"食っていいわけないだろ。当たり前だ。":
    "one eating well. That's only natural.",
"え…？　あ、そうか…　そう、だよな…。":
    "Huh...? Ah, right... yes, that's true...",
"そうだぞ。": "Exactly.",
"うげ…　ただでさえこの国のメシは、その…":
    "Ugh... this country's food was already, well...",
"あれだってのによー…　": "you know...",
"あっ、すいません…　フレイムのホノオ殿下…":
    "Ah, sorry... Prince Hono of Flame...",
"フレイムはもっとひどいんでしたね…。":
    "Flame's is even worse, isn't it...",
"セイリューの木材や石材を川で運べば…":
    "If we float Seiryu's lumber and stone down the river...",
"ここもフレイムもすぐに復興できるかも知れない":
    "both this land and Flame could be rebuilt quickly.",
"そんなことができるのか、ナガレ！？":
    "Can you do that, Nagare!?",
"うん。だけど、この悪天候と魔物の増加が":
    "Yeah. But not until the bad weather and",
"止まってからじゃないと無理だ。": "surge of monsters stop.",
"闇のエレメントだな…　とにかくよー":
    "It's the Dark Element... well, anyway—",
"み、みなさんのご武運をお祈りしております！":
    "I-I pray for your fortune in battle!",
"あーいそがしいいそがしい！": "Ah, so busy, so busy!",
"どの食器もクロスも綺麗で見るのに忙しい！":
    "All these dishes and cloths are so clean, I'm busy inspecting them!",
"ヒマじゃのう…": "So bored...",
"家に帰りたいんじゃがのう…": "I wish I could go home...",
"魔物が出るっていうんで、街に入れんのじゃあ":
    "They say monsters appear, so I can't get into town",
"あなたほど世界中を飛び回っても見つからない":
    "Even flying around the world like you, you'd never",
"のね…": "find another...",
"ウィンは首を振った": "Win shook his head.",
"…なにこれ。": "...What is this?",
"こんな装丁の本なんて見たことない…。":
    "I've never seen a book bound like this...",
"なんて綺麗で頑丈な…どこで作られた本なの？":
    "So beautiful and sturdy... where was it made?",
"…分からないのね？": "...You don't know, do you?",
"どういうことかしら…　しかも新しく見えるし":
    "How strange... and it looks new, at that.",
"ウィン…　この本て、私にくれるの？":
    "Win... are you giving me this book?",
"ありがとう！　ウィン！！": "Thank you! Win!!",
"じゃあ早速読むから、しばらく私に近付かない":
    "I'll start reading right away, so don't come near me",
"ようにしてね！！": "for a while!!",
"そ！　そう……………": "R-Right......",
"ものすごく…貴重なもののようだしね…":
    "It seems... extremely valuable...",
"…今後夜道に気を付けてとだけ言っておく…":
    "...I'll just say this: be careful on the roads at night...",
"ウィンは奇書を取り出して見せた":
    "Win took out the rare tome and showed it.",
"あっちいけ！！！！": "Go away!!!!",
"じゃますんなっていっただろ！！！！！？？":
    "I told you not to bother me, didn't I!!!??",
"ちゃんと売ってますよね？": "You are selling properly, right?",
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
