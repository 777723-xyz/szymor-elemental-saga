#!/usr/bin/env python3
"""Fill batch 16: Nagare's blade, Dragon Shrine descent, Mycenae scene."""
import csv
import os
import re

D = {
"つばめ返しの威力は確かに上がったが…":
    "The Swallow Reversal's power certainly improved, but...",
"普通に使う刀としての性能には自信がない…":
    "I'm not confident in it as a normal blade...",
"だから、ナガレ、お前が実戦で使ってみて、":
    "So, Nagare, use it in real combat and",
"その使い勝手をあとで俺に教えて欲しい。":
    "tell me how it handles afterwards.",
"ひと振り目は当主であり、継承者であるお前に":
    "The first swing is for you, as head of the family and inheritor.",
"その手間賃代わりの、タダってわけだな？":
    "So it's free, in lieu of labor costs, right?",
"そういうわけでもない。": "Not exactly.",
"鍛冶屋として継承者のお前にしてやれることが":
    "As a smith, this is about all I can do",
"これくらいしかないんだ。": "for you, the inheritor.",
"託そう。": "I entrust it to you.",
"そうか、邪推して悪かったよ！": "I see, sorry for the doubt!",
"あんたの気持ちと一緒に、有難くいただくよ！":
    "I'll gratefully accept it, along with your feelings!",
"今回大太刀を作ってみて気付いたんだが、":
    "Making this odachi taught me that",
"刀にももっと色々なバリエーションを":
    "there's room for many more variations",
"増やせそうだ…。": "of blades...",
"物干し竿みたいなの以外に、ちゃんと普通の刀も":
    "Besides the clothes-pole ones, there are proper",
"置いている…。": "normal blades too...",
"………どの薬も高過ぎる。": "......All these medicines are too expensive.",
"でもキラキラしていて綺麗だ…。":
    "But they're so sparkly and pretty...",
"そのためにも買い物して協力してください！":
    "So please help out by shopping!",
"いらっしゃい！セイリューにも":
    "Welcome! Opening an alchemist's shop",
"錬金術師のお店開くの夢だったんだ！":
    "in Seiryu was my dream!",
"近々あたらしい刀も完成するから、":
    "A new blade will be finished soon, so",
"またしばらくしたら覗きに来てみな。":
    "come by and check it again in a while.",
"刀を新調するのかい？少しは防具も":
    "Getting a new blade? I handle a little",
"扱っているよ。まあ見ていきな。":
    "armor too. Take a look around.",
"毎度あり！": "Thanks as always!",
"ここはよろず屋っていうか、薬屋だよ。":
    "This is a general store—or rather, a medicine shop.",
"万金丹が他の国で買うより安いから、":
    "Mankintan is cheaper here than in other countries, so",
"まとめ買いしていったらどうだい？":
    "why not stock up?",
"お化け…！？": "A ghost...!?",
"えっ、これお化けだったのか！こええ！！":
    "Huh, so this IS a ghost! Scary!!",
"むしろ、空中に浮いてる火がお化け以外の":
    "More to the point, what else would a flame floating in the air",
"なんなんだよ？": "be but a ghost?",
"来るぞ…　　あんたら、構えろ！":
    "Here they come... You lot, take your stances!",
"なんだこれ…？火が浮いているぜ…":
    "What is this...? Fire floating in the air...",
"嫌な预感がする…": "I have a bad feeling...",
"お社の近くにヒノタマっていうお化けが":
    "Since I was a kid, they always said hinotama ghosts",
"出るって、ガキの頃にによく言われたけど…":
    "appear near the shrine, but...",
"本当だったとはな。": "so it was true.",
"それより…": "Anyway...",
"なんだ？": "What?",
"こっから龍のいるっていう洞窟に入れるのか？":
    "Can we get into the dragon's cave from here?",
"そういう話だったろう。": "That's what they said, right.",
"で…　だからどうやって入るんだ？？":
    "So... then how do we get in??",
"着いたよ。": "We're here.",
"お社をぶっ壊すしかないだろう？":
    "We'll have to smash the shrine, right?",
"そんなことしていいのかよ！？":
    "Are we allowed to do that!?",
"いいも何も、それしかないだろう。":
    "Allowed or not, it's the only way.",
"ここが龍のお社だ。": "This is the Dragon Shrine.",
"洞窟ふさぐために作られているんだから、":
    "It was built to seal the cave, so",
"これがある限り、洞窟に入れない。":
    "as long as it stands, we can't enter the cave.",
"そうだけど…": "I guess so, but...",
"もったいないな、こんな立派な建物壊すのは…":
    "What a waste, destroying such a fine building...",
"いらねえよ、もう…　こんなもん。":
    "This thing's useless now, anyway...",
"………そうか？": "......Is that so?",
"さあ、ホノオ、とっととやれ。": "Come on, Hono, get on with it.",
"あんたの魔法で爆発させればすぐだろう？":
    "One explosion from your magic and it's done, right?",
"…ああ、ちょっと待ってろ。": "...Yeah, hold on a sec.",
"…で？": "...So?",
"しっかし…　かなり魔物の気配がするぜ…":
    "Man... I sense quite a few monsters...",
"明るいからって油断すんなよー…":
    "Don't let your guard down just because it's bright...",
"で…　どうすんだこれ…。": "So... what do we do with this...",
"落っこちるのかよ…？": "We're falling...?",
"当たり前だろう？": "Of course?",
"落っこちながら龍の頭に、": "We'll all drive our swords into",
"みんなで剣をぶっ刺すのさ！": "the dragon's head as we fall!",
"例の落っこちると龍がいるって穴…":
    "That hole where they said falling in means facing a dragon...",
"いやいやいやいや…": "No no no no...",
"本気で言ってるのか冗談なのか分からんから…":
    "I can't tell if you're serious or joking...",
"…もちろん冗談だよ。": "...Of course it's a joke.",
"屋敷から長い縄を持ってきてる。":
    "I brought a long rope from the estate.",
"これを伝って降りるぞ。": "We'll climb down this.",
"あ、そうですか…。": "Oh, right...",
"これだろうな…。": "This must be it...",
"しかしそれだって、十分におっかねえなー…。":
    "But even so, this is scary enough...",
"…結構降りたが…まだ全然下が見えねえぞ。":
    "...We've climbed down a fair bit... but I still can't see the bottom at all.",
"…水の者だかなんだかも、": "...Even the Water guy, or whoever,",
"落っこちながら考え事をしていたらしいから、":
    "was said to have been lost in thought while falling, so",
"相当に深い穴なんだろうな。": "this must be a really deep hole.",
"少しひかりが見えてきた…！": "I can see a little light...!",
"そろそろ着くみたいだぞ！": "Looks like we're almost there!",
"…やっとかー": "...Finally~",
"ちょっと待て…　": "Hold on...",
"…なんか下から話し声がしねえか…？":
    "...Do you hear voices from below...?",
"………本当だ。": "......I do.",
"…龍じゃなくてひとがいる？": "...There are people down there, not a dragon?",
"龍が話す？そうだとしても、誰と…？":
    "A dragon that talks? Even so, with whom...?",
"そうだろうな。": "Probably.",
"おわーーーっ！？": "Whoaaaa!?",
"お、おちるーーーー！！！！": "W-We're faaaaalling!!!!",
"他にそれらしい穴はなかった…": "There was no other hole like this...",
"間違いないだろう。": "No doubt about it.",
"穴が見えてきた…": "The hole's come into view...",
"きっとあれに落ちたら龍がいる…。":
    "If we fall into that, the dragon's surely there...",
"みんな、気を引き締めた方がいい。":
    "Everyone, better steel yourselves.",
"ここまでだ！ミケーネ！！": "This is the end, Mycenae!!",
"やったぜ！！": "We did it!!",
"これで弱まったんだな？": "That weakened her, right?",
"そうね…。": "Yes...",
"最強の闇の結晶である青龍が手に入らなかった":
    "Not getting Seiryu, the strongest Dark Crystal, is a real loss, though.",
"のは、大きいわ。": "It's a big blow.",
"じゃあこれで、復活を阻止できたのか…？":
    "So with this, we've stopped the revival...?",
"…あなたたち、一体どこまで知っているの？":
    "...Just how much do you lot know?",
"う…。": "Uh...",
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
