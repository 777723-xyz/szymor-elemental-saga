#!/usr/bin/env python3
"""Fill batch 44: dragon aftermath, splitting up plan."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"そんな私に教えたら、何をするか分からない。":
    "If you'd told me, there's no knowing what I might have done.",
"だから、話せなかった…。": "That's why I couldn't tell you...",
"…そういうことなのですね？":
    "...So that's how it was?",
"…そうじゃ。": "...Yes.",
"あーーーーーーーーーーーーーーー！！！！！":
    "Aaaaaaaah!!!!!",
"うお！？　まただ！": "Whoa!? Not again!",
"ああああああああああああ！！！！！":
    "Aaaaaaaah!!!!!",
"あたしはなんてバカだったんだーーーーー！！":
    "What an idiot I've been!!",
"お、おい…おまえそんな大声…":
    "H-Hey... with that voice of yours...",
"少しはみんなの迷惑をかんがえ…":
    "think a little about the trouble you're causing everyone...",
"まるで、友をなくしたような顔をしておるな…":
    "You look as though you've lost a friend...",
"いまなら分かるーーーーーーーー！！！！":
    "Now I understand—!!!!",
"あたしは何も考えてなかったーーーーーー！！":
    "I never thought about anything—!!",
"当主としてどころか！！！！！！！":
    "Not just as the head!!!!!",
"人間として浅はかだったーーーーーー！！！":
    "I was shallow as a human being!!",
"オタキ様の気持ちも…代々当主の気持ちも…":
    "Lady Otaki's feelings... the feelings of all the heads...",
"龍の気持ちも…　何も考えたことがなかった。":
    "and the dragon's feelings... I never once considered them.",
"みんなそれぞれが、自分の大事なもの…":
    "Each of you was earnestly thinking about what mattered",
"すべきことを、真剣に考えていたのに…":
    "most to you, and what had to be done...",
"龍をぶちのめすとか、食べるとか言っていた":
    "When I remember how I talked about beating up",
"あたしを思い出すと…": "and eating the dragon...",
"死にたくなるほど恥ずかしい。":
    "I'm embarrassed enough to die.",
"いや…それが、": "No... actually,",
"はたから見てると結構おもしろいぞ…？":
    "from an outsider's view, it was pretty funny...?",
"オタキ様、あたしは、父さまや、オタキ様…":
    "Lady Otaki—with the crest I inherited from the dragon,",
"代々の当主と、龍から受け継いだこの紋章で、":
    "and from my fathers and from you, heads across the generations,",
"必ずや使命を果たします！":
    "I will surely fulfill my mission!",
"……わかるのか？　オタキ様には…？":
    "......Can you see it? Can you, Lady Otaki...?",
"よく言った！よく言ってくれたぞ、ナガレ！":
    "Well said! Well said, Nagare!",
"そうとなれば、すぐ行動じゃ。": "Then let us act at once.",
"村はわしらに任せい！": "Leave the village to us!",
"おまえさん方はどうするんじゃ？":
    "What will you lot do?",
"セイリューがこの有り様だと、":
    "With Seiryu in this state,",
"正直オレも自分の国が心配です…。":
    "honestly, I'm worried about my own country too...",
"ウィンの国だって…　なあ？": "And Win's country... right?",
"そうでしょうね…。": "Indeed...",
"では、お二人は一度、それぞれのお国を":
    "Then why don't the two of you return",
"見に行かれてはどうですか？": "to your own lands for a time?",
"そうさせてもらえるとありがてえ…。":
    "That would be a great help...",
"ナガレはどうするの？": "What about you, Nagare?",
"わからんよ。": "I don't know.",
"あたしは…正直ここにいたいよ…":
    "Honestly... I'd rather stay here...",
"だけど…": "But...",
"ここの敵は当面片付けたようだし、":
    "The enemy here seems dealt with for now,",
"村のみんなも無事だと分かった。":
    "and I've confirmed the village is safe.",
"二人のどちらかに付いて行こうと思う。":
    "I think I'll go with one of you.",
"それなら…オレに付いてきてほしい。":
    "Then... I'd like you to come with me.",
"なんとなく思ったことを言ったまでじゃ。":
    "I was only voicing a passing thought.",
"ウィン、悪いけど、いいか？": "Win, sorry, but okay?",
"ウィンがいいなら、あたしもいいよ。":
    "If Win's fine with it, so am I.",
"ホノオの国は火の国だろ。": "Hono's land is the land of Fire.",
"あたしの水の力が役に立ちそうだ。":
    "My water power could come in handy.",
"助かる…　恩に着るぜ！ウィン！ナガレ！":
    "Thanks... I owe you one! Win! Nagare!",
"ウィンならハヤテの魔法であたしたちよりも":
    "With Hayate's magic, you could reach Windam",
"速くウィンダムまで辿り着けるだろうし、":
    "faster than us, and",
"万が一のときには撤退もできるだろ？":
    "if worst comes to worst, you can retreat, right?",
"しかしの…": "However...",
"とりあえず、この計画で行こう。":
    "For now, let's go with this plan.",
"そうと決まったなら、早速出発をし！":
    "If it's settled, then set out at once!",
"このお屋敷の中に、村のお店のひとたちも":
    "The village's shopkeepers are gathered",
"集まっています。": "inside this estate.",
"季節外れの突然の大雨…　そして洪水…":
    "The unseasonable downpour... and the flood...",
"買い物を済ませてから行くとよいでしょう。":
    "Better to finish your shopping before you go.",
"では、行って参ります！": "Then, we're off!",
"村のことはお願いします！": "The village is in your hands!",
"お社の奥で、なにか大きなことが起こった結果":
    "I figured something momentous must have happened",
"じゃろうとは思ったが…": "in the shrine's depths...",
"龍は…、はじまりの水の者のことを、":
    "The dragon called the First Being of Water...",
"友だちだと言っていた…": "its friend...",
"そのこどもであるあたしに、いつか紋章を":
    "and promised that someday, to me—that child's descendant—",
"返す約束もしていたって…": "it would return the crest...",
"オタキ様…　": "Lady Otaki...",
"ぜんぜん言い伝えと違うじゃないか！！":
    "That's nothing like the old tale at all!!",
"そうじゃったのか…　なるほどの…":
    "So that's how it was... I see...",
"そして、ナガレよ。よう、無事で…":
    "And Nagare—good to see you safe...",
"龍があたしたちのともだちなら…":
    "If the dragon was our friend...",
"どうして父さまたちはあんなに早死にを":
    "then why did my fathers all die",
"したんだよ！！": "so young!!",
"わしは、じかに龍にあっとらんし、":
    "I never met the dragon directly,",
"おまえみたいに、話もきいとらん。":
    "nor did I ever speak with it as you did.",
"だから、ナガレ…": "So, Nagare...",
"おまえのその問いに、正しく答えてやることが":
    "I cannot give you a correct answer",
"わしには出来んのじゃよ。": "to that question.",
"でも…　オタキ様は…": "But... Lady Otaki...",
"龍の祟りだと言っていたじゃないか…":
    "you said it was the dragon's curse...",
"…父さまが逝くまでの間は、当主は毎日、":
    "...Until Father passed, the head went to the shrine every day,",
"お社にお供え物を運んで、拝んでいた…":
    "carrying offerings and praying...",
"それがよくないことだと、オタキ様が言って…":
    "You said that was ill-advised, Lady Otaki, and...",
"それからは、やらないことにしたんだろ？":
    "after that, you all stopped, right?",
"…そんなことがあったのか…":
    "...So something like that happened...",
"オタキ様、みんなは無事なんだな…？":
    "Lady Otaki, everyone's safe, right...?",
"わかった…": "Understood...",
"わしの知っていることを、全て話そう、ナガレ。":
    "I'll tell you everything I know, Nagare.",
"じゃが、ナガレや…。": "But Nagare...",
"これはわしの考えじゃ、思いつきじゃ。":
    "This is only my own theory, my guess.",
"本当のことは、わしにもわからん。":
    "The truth, I don't know either.",
"そのつもりで、聞くのじゃ。": "Keep that in mind as you listen.",
"村のことは任せなさい！": "Leave the village to us!",
"くれたの。": "he gave it to me.",
"そうか…　よかった…！": "I see... what a relief...!",
"とりあえず、いまはまず、オタキ様と話を…":
    "For now, first, let's talk with Lady Otaki...",
"お帰りなさい、みなさん…　ナガレ。":
    "Welcome back, everyone... Nagare.",
"姉さま！村のみんなは！？":
    "Sis! What about everyone in the village!?",
"皆、無事です…": "Everyone's safe...",
"上流の村の方々が、すぐに洪水を知らせて":
    "The folk of the upstream villages alerted us",
"村のみんなはこの屋敷に集まっています。":
    "to the flood at once, and everyone's gathered here.",
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
