#!/usr/bin/env python3
"""Fill batch 21: Pikepike's Dark Continent exposition (the Demon King plan)."""
import csv
import os
import re

D = {
"万金丹を多めに買っておいた方がよさそっす。":
    "Better to stock up on Mankintan.",
"今更引き返すつもりはねーけど。":
    "Not that I plan to turn back now.",
"ウィン、どうする？": "Win, what do you think?",
"入っちまってもいいかー？": "Should we just go in?",
"…ここから先は、進んだら全てが終わるまで、":
    "...Once we go past here, until everything's over,",
"もう戻れない気がするな…。":
    "I feel like we won't be able to go back...",
"確かに…　薬とか、もっと買っておいた方が":
    "True... we should stock up on more medicine",
"いいかも。": "and such.",
"なんだよそれ、カンか？": "What's that, a hunch?",
"そうだよ。": "Yeah.",
"おいおい…　なんだよココは！":
    "Whoa... what is this place!?",
"街…？　いや、城…？　があったのか…？":
    "A town...? No, a castle...? It was here...?",
"この地は未開の、無人の地のはずだ…":
    "This land is supposed to be uncharted and uninhabited...",
"もっと大昔にはここにひとが住んでいたのか？":
    "Did people live here in the distant past?",
"なんか建物とかも…見た事ねえ感じだ。":
    "And the buildings... they don't look like anything I've seen.",
"オレらもしかして、歴史上の大発見してる…？":
    "Are we making a huge historical discovery...?",
"そうかもな。": "Maybe.",
"色々教えてあげちゃっても構わないんだよねえ。":
    "I don't mind telling you all sorts of things, you know.",
"ホノオ、乗せられるなって！": "Hono, don't get roped in!",
"絶対にこいつは時間稼ぎしてるんだよ！":
    "He's definitely just buying time!",
"…青いのちょっと黙って！": "...Blue one, quiet down!",
"えっ？　でも知りたくないか？":
    "Huh? But don't you want to know?",
"知っても闇のエレメントが復活しちまったら":
    "Even if we know, it'd mean nothing if the Dark Element",
"意味がないだろう！": "revives!",
"それに、": "Besides,",
"そのあやしいガイコツが本当のことを":
    "there's no guarantee that shady skeleton",
"あたしたちに教えるなんて保証はない！":
    "would tell us the truth!",
"うおい青いの！　せめて名前で呼べよ！！":
    "Hey, blue one! At least call me by my name!!",
"この際ピカピカでもいいからさ…":
    "Even Pikapika would do at this point...",
"ガイコツってなんだよーくやしーーー！！":
    "Who's a skeleton—! So unfair!!",
"じゃ、じゃあ…": "Th-Then...",
"触りだけ！　触りだけ急いで教えてくれ…":
    "Just the gist! Hurry and tell us just the gist...",
"ピクピク！！": "Pikupiku!!",
"まあ、私は四天王筆頭…":
    "Well, I am the chief of the Four Generals...",
"なんでわざわざケイレンさせたんだよ！？":
    "Why'd you go and twitch the name like that!?",
"でもまだ名前呼ぼうとするだけこっちの子は":
    "But at least this one tries to say my name,",
"いい子だなあ…": "what a good kid...",
"触りだけ教えてくれ、ピコピコ。":
    "Just tell us the gist, Pikopiko.",
"つまり四天王最強の大魔導士…！":
    "So he's the strongest great mage of the Four Generals...!",
"いやお前のはわざとだろおおおおお！！？？":
    "No, yours is definitely on purpose—!!??",
"バトルになったら真っ先にやっつけるからな、":
    "If we fight, you're going down first,",
"青いのは！！！": "blue one!!",
"ごめんちょっと喋り疲れた…　いいや、":
    "Sorry, I'm tired of talking... ah well,",
"じゃあ触りだけなるべく急いで教えてやろう…":
    "I'll hurry and teach you just the gist...",
"ゴクリ…": "(gulp)...",
"ピ！　ケ！　ピ！　ケ！様だからなあ！！！":
    "It's Pi! Ke! Pi! Ke! to you!!!",
"あともう少しでこの土地と同じ毒の瘴気…":
    "Before long, the same poisonous miasma as this land—",
"闇インフルエンザがエレメント大陸全土に":
    "the Dark Flu—will spread across the entire",
"広がり、覆いつくす…！！":
    "Element Continent and cover it all...!!",
"そしてすべての人間が不治の病気にかかり…":
    "Then every human will fall to an incurable disease...",
"死んでしまうのだああああああああーー！！！":
    "and DIE—!!",
"……は？　はああああああ！？": "......What? Whaaa—!?",
"思っていた以上にヤバイじゃないか！！":
    "This is way worse than I thought!!",
"相手が病気じゃ…防ぎようも逃げようもない！！":
    "Against a disease... there's no guarding, no escaping!!",
"さらにさらにさーーらーーーにーーーー！！":
    "And further—furthermore—even more!!",
"我々四天王は王を戴くことにしたのだよ…":
    "We Four Generals have decided to crown a king...",
"そう、キミらと同じように…闇のエレメントの":
    "Yes, just like you—we'll build a Dark Kingdom",
"加護による闇の王国を作るのだあああああ！！":
    "blessed by the Dark Element!!",
"あ？　王ってなんだよ…？　国…？":
    "Huh? A king...? A kingdom...?",
"つまり本来はラスボスポジションッ…！！":
    "In other words, he's supposed to be the final boss...!!",
"闇のエレメントパワー…それ自体は膨大で、":
    "Dark Element Power... in itself, it's vast—",
"強大な自然の圧倒的エネルギー…":
    "an overwhelming energy of mighty nature...",
"だが…人格は持たない。": "But... it has no personality.",
"我々も四天王も、いわば闇のエレメントパワー":
    "We Four Generals are, so to speak, mere byproducts",
"たまたま人格を持った副産物に過ぎん。":
    "of the Dark Element Power that happened to gain personalities.",
"本当だったらもっと後で出てくるものなんだ。":
    "In truth, it should have appeared much later.",
"四天王だけでは…　闇のエレメントが世界から":
    "The Four Generals alone... couldn't stop the Dark Element",
"駆逐されるのを防げなかったのだ………":
    "from being driven out of the world......",
"…だ、か、ら、こ、そ！！！！":
    "...And, so, that's, why!!!!",
"だからこそ我々は闇のエレメントパワー自体に":
    "That's why we decided to give the Dark Element Power",
"人格を与える事にしたーーーーーーーー！！":
    "itself a personality—!!",
"膨大で強大な自然を司るパワー！！":
    "The power governing vast, mighty nature!!",
"それ自体が人格を持ち…":
    "When that power itself gains a personality...",
"全てを己の意思で律する王となる…":
    "it becomes a king ruling all by its own will...",
"大魔王の誕生だああああああああ！！":
    "The Great Demon King is born!!",
"う、うお…": "U-Whoa...",
"話がデカ過ぎて全然わかんねーぜ…":
    "This is all so huge I can't even follow...",
"この地をすべて人間の住めない土地にして…":
    "Turn this whole land into one where humans can't live...",
"魔王とやらの治める闇の王国を作る…":
    "and build a Dark Kingdom ruled by some Demon King...",
"そういうことかあああ、ピキピキーー！！":
    "So that's what it is, Pikipiki!!",
"フハハハハハハ！！　血管が浮き出るほどに、":
    "Bwahahaha!! You're so angry the veins are popping out,",
"物凄く怒っているな、青いのー！！！":
    "blue one!!!",
"ピ…？　なんだって？": "Pi...? What did you say?",
"…え、もしかしていまの私の名前…？":
    "...Huh, is that my name just now...?",
"しかし魔王を作る…闇のエレメンタルパワーに":
    "But to create the Demon King—to give the Dark Elemental Power",
"人格を与えるには…　強靭な精神をもつ":
    "a personality... requires a vessel with",
"依り代が必要だ…　よりしろな？":
    "a strong spirit... a vessel, right?",
"つまり四天王が身を捧げる必要があった！":
    "In other words, the Four Generals had to offer themselves!",
"我々のみが、闇の力を用いて意思を発揮できる":
    "Because we alone are unique beings who can exert will",
"特異な存在だからなーーーーー！！":
    "through the Dark power—!!",
"ぐはっ！　も、もうダメだ…":
    "Gah! I-I can't take it anymore...",
"ナガレーーー　かいせつをたのむーー！！！":
    "Nagare—! Please explain—!!",
"…闇のエレメントそれ自体に人格を与えて":
    "...To give the Dark Element itself a personality",
"魔王にするためには、強い人格をもつ四天王が":
    "and make it a Demon King, the Four Generals, with their strong personalities,",
"身代わりというか本体になる必要がある…":
    "must serve as the substitute—or rather, the body...",
"つまり、貴様たちがここ最近あたしらの国に":
    "In other words, you lot not showing your faces",
"姿を見せなかったのも、魔王になる為の準備を":
    "in our lands lately is because you were preparing",
"していたから…　そういうことだなピコピコ！":
    "to become the Demon King... that's it, isn't it, Pikopiko!",
"そういうことだ、青いの！！": "Exactly, blue one!!",
"物分かりの良さに免じて名前イジリについては":
    "For your quick understanding, I'll forgive the name-teasing—",
"この際もう面倒だし、いいよ、許す！！！！":
    "it's too much hassle anyway, fine, you're forgiven!!!!",
"時間が惜しいんだよ！": "We don't have time!",
"そんなことはさせないぜええええええ…":
    "I won't let you do that—!",
"ピ…ピキじゃなくて…ピｋッカ…":
    "Pi... not Piki... P-kka...",
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
