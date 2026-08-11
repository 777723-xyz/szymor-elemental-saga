#!/usr/bin/env python3
"""Fill batch 45: crest immunities, sword philosophy, dragon's farewell."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"買い物する必要があれば、": "If you need to shop,",
"ここで済ませるとよいでしょう": "it'd be best to do it here.",
"自分を強いと感じられたのさ。":
    "that's when I feel strongest.",
"そうか…　いや、でもおまえのいまの動き、":
    "I see... no, but your movements just now—",
"多分オレらみたいに動き回るより、きっと":
    "they're probably far stronger than rushing about",
"ぜんぜん強いぞ…？": "like we do...?",
"ああ、そんなことは分かってるさ。":
    "Yeah, I know that.",
"結局自分が身に着けたモンに感謝はしてるし、":
    "In the end, I'm grateful for what I've learned,",
"さっきのバトルで気付いたことがある。":
    "and something hit me in that battle just now.",
"後悔もない。": "I have no regrets.",
"ただ、これから先、あんたらの戦い方に文句":
    "But from here on, I might complain about your fighting",
"つけるときもあるだろうけれど…でも本当は、":
    "style now and then... but the truth is,",
"あんたらの戦い方を好きだからな、ってことだ。":
    "I love the way you fight.",
"あ…　はい…。　　　　？":
    "Ah... yes...?",
"結構すごいことだぞこれは…":
    "This is actually quite something...",
"へえ…なんだよ？": "Huh... what is it?",
"あんたらの紋章は、": "Your crests...",
"同じタイプというか…同じ属性の攻撃から、":
    "they seem to protect you from attacks of",
"あんたらを守っているみたいだな。": "the same type—the same element.",
"火をまとった攻撃はホノオにはあまり効かない":
    "Fire-wreathed attacks don't do much to Hono,",
"そして、風というか雷をまとった攻撃も、":
    "and wind—or rather, lightning—wreathed attacks",
"ウィンにはあまり効いていなかった。":
    "barely affected Win either.",
"たいしたことなかった…": "It wasn't much at all...",
"…えっ！　マジで！？": "...Huh! For real!?",
"気付いてなかったとはな…。":
    "So you never noticed...",
"あんたどんだけ必死で暴れてるんだよ。":
    "How desperately were you two thrashing around in there.",
"マジか…いや、紋章の力ならありえそうだし…":
    "For real... well, it'd make sense as the crest's power...",
"実際オレも火の攻撃は、あまり痛くなかった…":
    "Honestly, fire attacks didn't hurt me much either...",
"よかった…　こ、こわかったぜ…！":
    "What a relief... t-that was scary...!",
"マジか！": "For real!",
"すげえじゃねえか！": "That's amazing!",
"いや、それより、バトル中にそんなところまで":
    "No, more importantly—during a battle, you noticed all that?",
"見ているナガレ！　おまえすごいな…":
    "Nagare, you're incredible...",
"戦いの最中は決して興奮せず、自然体でいろ。":
    "Never get excited mid-battle; stay natural.",
"理想は無の心で、戦場を正確に観察しろ…":
    "The ideal is an empty heart, precisely observing the field...",
"剣を教わる一番最初から、":
    "From the very first sword lesson,",
"あたしらはそう教わるんだよ。": "that's what we're taught.",
"あんたらみたいに、血走った目で走り回ったり":
    "We don't run around with bloodshot eyes",
"しない。": "like you two.",
"なんだよ、二人して？": "What is it, the both of you?",
"いや…　なんかズシッときた…":
    "No... it just hit us hard...",
"あんたもかい？": "You too?",
"あれだけ大暴れしといて、怖かったってかい…":
    "After all that rampaging, you were scared, huh...",
"ふうん…。": "Hmph...",
"でもね、あんたらの戦い方を変えろとは、":
    "But hey, I won't tell you to change",
"あたしは言わないからな。": "your fighting style.",
"むしろさっきのお化けの方に同情したくなるね":
    "If anything, I feel sorry for that monster just now.",
"え…？　そう…なの？": "Huh...? Really...?",
"うん。": "Yeah.",
"あたしはあんたらみたいな戦い方の方が好きだし、":
    "I prefer your way of fighting,",
"落ち着くんだよ。": "it puts me at ease.",
"小さい頃…": "When I was little...",
"村のみんなから剣を教えられるときにさ…":
    "when the villagers were teaching me the sword...",
"こころを静かに、行儀よく、無駄な動きをせず、":
    "'Keep your heart calm, behave, waste no movement,",
"ひとにやさしく、平和を祈り…　みたいな、":
    "be kind to others, pray for peace'—like that...",
"何を教えてもらってるんだか分からない、":
    "I couldn't make sense of what I was being taught,",
"セイリューの剣術が嫌で嫌で仕方なかったんだ。":
    "and I hated Seiryu's swordsmanship with all my heart.",
"あたしはむしろ、夢中になって叫んで、走って、":
    "For me, it was when I was shouting, running,",
"剣を振り回しているときの方が…":
    "and swinging my sword in a frenzy that I...",
"上手に動けていると感じられた。":
    "felt I moved best.",
"ウィンのハヤテでスピードを上げ、":
    "Boost speed with Win's Hayate,",
"オレのキョウセンシで腕力を上げ…":
    "boost strength with my Warrior,",
"そしてナガレのテッペキで落ちたときも安心…":
    "and with Nagare's Iron Wall, falls are safe...",
"という作戦で、縄を見事登り切ったぜーーー！":
    "With that plan, we climbed the rope splendidly!",
"しかし本当に便利だな、紋章の力って…。":
    "But really, how handy is the crest's power...",
"戦い以外にも、色々役に立ちそうだ。":
    "It'd be useful for all sorts of things beyond battle.",
"…だけど、これからどうすんだ？":
    "...But what do we do now?",
"ミケーネを…四天王を追う。そして倒す。":
    "We pursue Mycenae... the Four Generals. And defeat them.",
"どこにいるのかも分からんぞ？":
    "We don't even know where they are?",
"…とりあえず、村に帰ろう。":
    "...For now, let's go back to the village.",
"姉さまたちに継承が済んだことを伝えたい。":
    "I want to tell my sisters the succession is done.",
"ああ、そうだな！": "Yeah, right!",
"…と、いうことでだ。": "...And so.",
"ナガレのアイデアで、": "We go with Nagare's idea.",
"あたしたちにはそう伝わってるんだよ。":
    "That's how it's been relayed to us.",
"そうだったな…。": "Right...",
"あれ、おかしいな…": "Huh, that's strange...",
"ぼくは怒ってなんかないよ": "I'm not angry at all.",
"だって…": "Because...",
"そうだ！": "Right!",
"友だちなんだから…！だから…":
    "You're my friend...! So...",
"友だちのこどもたちの　きみたちもぼくの友だちだよね？":
    "You, my friend's children—you're my friends too, right?",
"ああ…　友達だぜ！": "Yeah... We're friends!",
"龍！": "Dragon!",
"おい、龍、大丈夫か…？": "Hey, dragon, you okay...?",
"よかった…": "Good...",
"最後に　友だちとの約束を守れて…":
    "In the end, I could keep my promise to my friend...",
"そして新しい友だちにも会えたんだ…":
    "and even meet new friends...",
"よかった…　": "Good...",
"…龍？　おい…　死んだのか…":
    "...Dragon? Hey... did you die...",
"待ってくれ…　": "Wait...",
"あんたにはまだまだ聞きたいことがある…":
    "There's still so much I want to ask you...",
"龍！！": "Dragon!!",
"ナガレ…　やめろ。": "Nagare... stop.",
"静かに眠らせてやろうぜ。": "Let him rest in peace.",
"だって…　こいつに聞かないと分からない…":
    "But... if I don't ask him, I'll never know...",
"分からないことだらけで、死んじまうなんて…":
    "How can he die with so much left unanswered...",
"龍の涙　を手に入れた": "Obtained a Dragon's Tear.",
"…で、どうやってここから出るんだ？":
    "...So how do we get out of here?",
"ぼくは　もうそろそろ　死んでしまう…":
    "I will soon die...",
"もともと、死にかけていたのを…":
    "I was already on the verge of death...",
"友達が紋章で助けてくれていたから…":
    "my friend was keeping me alive with the crest...",
"それがなくなったら、もう　死んでしまうんだ":
    "once that's gone, I'll finally die.",
"あんたがあたしに…": "You, to me...",
"本当に消えちまいやがった…！":
    "He really went and vanished...!",
"紋章を継承してくれたからなのか…？":
    "Was it because he passed the crest to me...?",
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
