#!/usr/bin/env python3
"""Fill batch 48: Flame castle aftermath, rice-ball gags, Hono's plea."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"おっけーりょーーーかーーーーい": "Okkee—ay—!",
"ここはあたしがちゃーんと見張ってるから、":
    "I'm keeping a sharp eye on this place, so",
"あんたらは使命とか何とかを頑張んな！":
    "you lot go do your whole mission thing!",
"大丈夫…　ちょっと突き指しただけだよ":
    "I'm fine... just a little jammed finger.",
"どうやら魔物たちはこれで片付いたみたいだね":
    "Looks like the monsters are dealt with now.",
"しっかし…　一体何が起こったんだ…？":
    "But still... what on earth happened...?",
"ひでえことになってるじゃねえか…":
    "This is a damn mess...",
"ありがとう…　ナガレ…　みなさん…":
    "Thank you... Nagare... everyone...",
"マハリ！傷は！？　大事ないか！？":
    "Mahari! Your wound!? Are you all right!?",
"あっ！　騎士ウィンどの！": "Ah! Sir Knight Win!",
"おつかれさまです！": "Good work today!",
"いつ魔物がまた襲ってくるかビクビクです…":
    "I'm on edge, wondering when monsters will attack again...",
"ウィンダムの城下町、現在は異常なし！":
    "Windam Castle Town: currently no anomalies!",
"ウィン殿、ご武運をお祈りしております！":
    "Sir Win, I pray for your fortune in battle!",
"いい匂いがしなくなっちまった…":
    "The place doesn't smell nice anymore...",
"…って、ウィン！？": "...Oh, Win!?",
"あ、大丈夫、大丈夫！！": "Ah, it's fine, it's fine!!",
"お前のご両親なら、お城に避難してるぜ！":
    "Your parents took refuge in the castle!",
"無事だからな！！": "They're safe!!",
"フン、なりはデカくても…":
    "Hmph, big as they were...",
"俺たちの相手じゃなかったな。":
    "they were no match for us.",
"あーっ！！　　いた！！": "Ahh!! There they are!!",
"えっ！　ウィン！？　それに…ピピン！！？？":
    "Huh! Win!? And... Pipin!!??",
"おい、ピピン待ってくれ！！": "Hey, Pipin, wait!!",
"ウィンも、助けてくれ！！": "Win, help too!!",
"ふたりとも…すぐに城へ…　王の間へ…":
    "Both of you... quickly, to the castle... the throne room...",
"四天王を名乗る奴が…　王の間に現れて…":
    "Someone claiming to be a Four General... appeared in the throne room...",
"あのままじゃ、王もみんなも殺されちまう！！":
    "At this rate, the king and everyone will be killed!!",
"す、すごく大きなバケモノです……隊長…！":
    "It's a h-huge monster... Captain...!",
"た、隊長…　か、かかか…　加勢します…！！":
    "C-Captain... I-I-I'll... join you...!!",
"…下がれ！！": "...Fall back!!",
"こいつは、お前らの手には負えん！！":
    "You lot can't handle this one!!",
"こいつは俺に任せろ！！　": "Leave this one to me!!",
"…ん？": "...Hm?",
"…お前か。": "...It's you.",
"…手伝え、ウィン！": "...Help me, Win!",
"何をしてんだホノオ！？": "What are you doing, Hono!?",
"今更戻ってもどうしようもない！":
    "Going back now would be pointless!",
"早く上の階へ行くぞ！": "Quick, to the floor above!",
"…お、王子ぃぃぃ…": "...O-O-O Prince...",
"おい！しっかりしろ！": "Hey! Pull yourself together!",
"…は、はいぃぃ……": "...Y-Yes...",
"親父は無事なのか！？": "Is my dad safe!?",
"…わ、わかりません": "...I-I don't know.",
"おそろしく強い…　全身鎧の奴が…　上へ…":
    "An absurdly strong... full-armored man... went up...",
"なんだと…　まさか…！！": "What... no way...!!",
"知っている奴なのか…　ホノオ！？":
    "You know who it is... Hono!?",
"もしかしたら…な…": "Maybe... it's him...",
"くっそー…": "Damn it...",
"生きていてくれよ…　親父…！！":
    "Please be alive... Dad...!!",
"けっこう態度違くねーか…":
    "Their attitude's really different, huh...",
"あっ！　ナガレ様じゃないっすか！":
    "Oh! If it isn't Lady Nagare!",
"ちっす！　この前はあざっす！！":
    "Yo! Thanks for the other day!!",
"よう！　元気になったみたいでよかったぜ！":
    "Hey! Glad to see you're feeling better!",
"へ？　あ、王子　どうもっす": "Huh? Oh, Prince. Howdy.",
"えー？　あっ王子！": "Huh? Oh, Prince!",
"いやでもこのひとらに城ん中うろつかせたら":
    "But if we let these folks wander the castle,",
"何するかわかんないんすよー": "who knows what they might do~",
"だからって閉じ込めたら窮屈で仕方ねえ…":
    "But locking them up is so cramped and awful...",
"これが民を守る王国のやることかよ！":
    "Is this how a kingdom protects its people!?",
"あーダメダメ！　": "Ah, no no!",
"メシも寝床も人数分しっかり出してますし…":
    "We're providing food and beds for everyone...",
"王子、これは仕方ないんです。":
    "Prince, this can't be helped.",
"ウィンダムとかとは治安がちがうんですよ":
    "Our security situation differs from places like Windam.",
"………だからってよー……": ".........Even so...",
"アニキがいたならこういうとき…":
    "If big bro were here, in times like this...",
"もっといいやり方出来たんだろうな…":
    "he'd have found a better way...",
"こっから先は立ち入り禁止だし…":
    "Beyond this point is off-limits, and...",
"ホノオ！": "Hono!",
"あ、いや…別に弱音吐いたつもじゃりねえんだ…":
    "Ah, no... I didn't mean to sound so weak...",
"やっぱり普段から民にもっとしっかり食わせる":
    "I just realized we really need to make sure",
"必要があるんだなって思ったよ…":
    "the people eat properly, day to day...",
"出るのも禁止です！": "Leaving is also forbidden!",
"おいおい…町から避難してきた人間ここに":
    "Hey now... you're locking up the people who",
"閉じ込めてんのかよ！？　かわいそうだろ！":
    "fled the town here!? That's awful!",
"手間自体はそんなでもないんす。":
    "It's not that much trouble, honestly.",
"火降ってくるのが治まりさえすれば…":
    "If only the falling fire would stop...",
"そうか…　すまんな　さっさと闇の何とかを":
    "I see... sorry, we'll hurry and beat up",
"やっつけてくるぜ！": "the Dark-whatever!",
"あっ！　危ないっす！": "Ah! Watch out!",
"それ以上来ちゃダメっすよ！":
    "You can't come any closer!",
"城ん中、直せそうか？": "Can you fix the castle?",
"もともと石積み上げまくってるだけなんで、":
    "It's basically just stacked stone, so",
"あーーーわしの家畜小屋が…！！":
    "Aaaah—my livestock shed...!!",
"ニワトリたちがーーーー": "My chickens—",
"って、あれどうなってんの！？":
    "Wait, what's going on over there!?",
"ナ、ナガレ様のにぎったライスボール…":
    "A rice ball shaped by Lady Nagare's hands...",
"食べたいっす！！": "I want to eat it!!",
"あはは、平和になったらみんなで握ろう！":
    "Ahaha, once peace returns, we'll all make them together!",
"おい、オレの握ったライスボールはどうだ！？":
    "Hey, what about the rice ball I made!?",
"この前ライスボール食べたんだけどさー":
    "I ate a rice ball the other day, and—",
"王子が握ったらボールじゃなくて":
    "if the Prince made one, it wouldn't be a ball,",
"ナンになりそう　平たくなっちゃいそう":
    "it'd be a naan—flat as can be.",
"めちゃうま！　あれコメ手で握っただけ":
    "It was delicious! It's just rice shaped by hand,",
"なんだろ？　なんであんなにうまいの！？":
    "so why is it that good!?",
"セイリューのコメは柔らかいけど、握っても":
    "Seiryu rice is soft, yet even when pressed,",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"だから握ると逆に噛み応えが増すのさ。":
    "Shaping it actually makes it chewier.",
"思い悩む顔も他国にひとびとよりも少ない。":
    "The faces of its people seem less troubled than those of other lands.",
"どうなるかを調査した結果ををここに報告します。":
    "Here I report the results of my survey of how things would unfold.",
"だからよー…　オレがコイツを倒すんだから…":
    "That's why... I'm going to defeat this guy...",
"おまえは戦わなくていいって言ってんだよー！":
    "so I'm telling you, you don't need to fight!",
"頼む…　ナガレ…": "Please... Nagare...",
"おまえなら、みんなを助けられるだろ…？":
    "You could save everyone, right...?",
"おまえなら、ぜってーに親父たちを":
    "You'd absolutely save my dad and the others...",
"助けてくれる…　そう信じられるから、":
    "I believe that, so—",
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
