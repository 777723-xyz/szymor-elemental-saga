#!/usr/bin/env python3
"""Fill batch 05: all unique choice strings (841 rows, 114 unique)."""
import csv
import os

C = {
"ハヤテを使おう": "Use Hayate",
"使わなくていいや": "No, let's not",
"旅の宿屋": "Traveler's Inn",
"フレイム城": "Flame Castle",
"ウィンダム城": "Windam Castle",
"読まない": "Don't read it",
"読んでみる": "Read it",
"ちがうよ": "That's not it",
"セイリュー": "Seiryu",
"そうだよ": "That's right",
"休んでいく": "Rest here",
"休まない": "Don't rest",
"ありがとう": "Thank you",
"うん": "Yeah",
"いい感じ": "Feels good",
"ぼちぼち": "Getting along",
"泊まりたい": "I'd like to stay",
"ちょっと寄ってみただけ": "Just stopping by",
"泊まらせてもらいます": "We'll stay then",
"やっぱりやめます": "Actually, never mind",
"そのままにしておく": "Leave it as is",
"やめてよ": "Stop it",
"もちろん": "Of course",
"元気だよ": "I'm fine",
"別行動なんだ": "We're splitting up",
"どうぞ": "Go ahead",
"いただきます": "Dig in",
"遠慮しておきます": "I'll pass",
"引っ張ってみる": "Pull it",
"敬礼を返す": "Return the salute",
"おじぎをする": "Bow",
"疲れたー": "I'm beat",
"読んでみよう": "Let's read it",
"そんなことはない": "That's not true",
"いやだ": "No way",
"まだです": "Not yet",
"そうでもない": "Not really",
"違うよ": "That's wrong",
"読んでしまう": "Read it anyway",
"読む": "Read",
"読んでみない": "I won't read it",
"売ってるよ": "We do sell it",
"えっ　なんのこと": "Huh? What do you mean?",
"申し訳ございません": "I apologize",
"陛下とお話させて下さい": "Please let me speak with His Majesty",
"食べます": "I'll eat it",
"また今度来ます": "I'll come again",
"出よう": "Let's leave",
"探索しよう": "Let's search",
"占ってください": "Tell my fortune",
"また今度で": "Some other time",
"そうだね": "Yeah, you're right",
"もう大丈夫ですよ": "We're fine now",
"キノコの食べ過ぎ注意です": "Careful not to eat too many mushrooms",
"出発しよう": "Let's set out",
"まだ準備しよう": "Let's get ready first",
"入ろう": "Let's go in",
"引き返そう": "Let's turn back",
"取り出してみる": "Take it out",
"これで終りにする": "Let's end it here",
"知ってる": "I know",
"知らない": "I don't know",
"最近どうですか": "How are you these days?",
"用はありません": "No business here",
"そちらこそご苦労様です": "Likewise, thanks for your hard work",
"調べてる": "Looking into it",
"ぜんぜん": "Not at all",
"元気です": "I'm well",
"あんまり": "Not much",
"わからない": "I don't know",
"ダメ": "No good",
"君に会いに来たんだ": "I came to see you",
"どうもしないよ": "Nothing much",
"はい": "Yes",
"いいえ": "No",
"狂戦士のキノコです": "It's a Berserker Mushroom",
"内緒です": "It's a secret",
"どうかな": "I wonder",
"わかった": "Got it",
"ちょっと無理かな": "That might be a stretch",
"何か困りごとないか？": "Any trouble?",
"ごめんなさい": "I'm sorry",
"聞きます": "I'll listen",
"聞きません": "I won't listen",
"走り抜ける": "Run through",
"慎重に進む": "Proceed carefully",
"この通行手形あげます": "I'll give you this permit",
"大変ですね": "That's rough",
"なんで？": "Why?",
"そんなことない": "That's not true",
"行ってくる": "I'm off",
"戻る": "Go back",
"出る": "Leave",
"もう少しだけ": "Just a bit more",
"いいですよ": "Sure",
"お断りします": "I'll decline",
"持ってます": "I have it",
"持ってません": "I don't have it",
"ダメだよ": "No way",
"大丈夫": "It's fine",
"きつい": "Too much",
"分かります": "I understand",
"分かりません": "I don't understand",
"パン買います": "I'll buy bread",
"パンいらない": "No bread for me",
"あげます": "I'll give it",
"あげられないな": "I can't give it",
"そんなことないよ": "That's not true",
"槍派だね": "You're a spear man",
"槍は使わない": "I don't use spears",
"よろしく": "Nice to meet you",
"しっかりしろ": "Pull yourself together",
"一応二周目をはじめる": "Start a 2nd playthrough",
"一応３周目をはじめる": "Start a 3rd playthrough",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "choice.tsv"))


def main():
    with open(PATH, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    filled = 0
    for r in rows:
        t = C.get(r["japanese"])
        if t:
            r["translation"] = t
            filled += 1
    with open(PATH, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print("choice.tsv filled", filled, "/", len(rows))
    missing = sorted({r["japanese"] for r in rows if not (r.get("translation") or "").strip()})
    if missing:
        print("missing:", missing)


if __name__ == "__main__":
    main()
