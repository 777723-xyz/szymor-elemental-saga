#!/usr/bin/env python3
"""Fill batch 35: prologue narration, young Roi's childhood."""
import csv
import os
import re

D = {
"なんとか勝てたんだ。": "We managed to win.",
"しかし、逃げられた…。": "But they got away...",
"親父…　伝説だったことが、":
    "Dad... the thing that was just a legend...",
"いま現実に起こってるんだろ…？":
    "it's really happening now, isn't it...?",
"最早、疑う余地はないな…": "There's no room for doubt now...",
"帰ったぜーーー": "I'm back~",
"闇のエレメントが復活しつつあるのだ。":
    "The Dark Element is beginning to revive.",
"すぐに西のセイリューへと向かい、":
    "Head at once to Seiryu in the west",
"水の紋章の継承者と合流するのだ。":
    "and join up with the Water Crest's inheritor.",
"わしもその間、防備を固めよう…":
    "I too will strengthen our defenses in the meantime...",
"しかしその前に、ホノオよ…":
    "But before that, Hono...",
"なんだよ、急ぎなんだろ？": "What? We're in a hurry, right?",
"わしはお前に謝らなければならん。":
    "I must apologize to you.",
"はっ！？な、なんで…": "Hah!? Wh-Why...",
"わしは…お前は王になりたくないのだと、":
    "I... had thought you didn't want to become king,",
"思っていた…": "you see...",
"な…なにを…": "Wh-...What...",
"思えばわしも重臣たちも…":
    "Come to think of it, both I and my ministers...",
"お前の兄、ホムラばかりを褒め、":
    "praised and doted on your brother Homura",
"かわいがっていた。": "and him alone.",
"そして誰よりも…": "And more than anyone...",
"ばかもの！！": "You fool!!",
"お前がホムラを慕っていた…。":
    "You adored Homura...",
"そのホムラが幼くして死に…":
    "And when Homura died young...",
"お前が唯一の王子になってから、":
    "once you became the only prince,",
"わしらは手のひらを返して":
    "we did an about-face",
"お前を大事にするようになったのだ。":
    "and began to treasure you.",
"そ、そんなの今更もういいだろ…？":
    "Th-That's all water under the bridge now...?",
"おい、こんなところに何をしに来たんだ？":
    "Hey, what are you doing coming here?",
"任務はどうした？": "What about your mission?",
"どうしても行くってのなら…":
    "If you absolutely must go...",
"俺はここで待っているぞ。": "I'll wait here.",
"行きたければ、一人で行ってこい。":
    "If you want to go, go alone.",
"…ったく、お前は世話の焼ける奴だ！":
    "...Jeez, you're such a handful!",
"もう少しだけ待ってやるが…":
    "I'll wait a little longer, but...",
"あんまり遅かったら、俺一人で仕事を":
    "if you take too long, I'll finish the job",
"済ませてくるからな。": "on my own.",
"気は済んだか？": "Had enough?",
"さっさとここを出るぞ。": "Let's get out of here, quickly.",
"けいしょ…　けいしょうしゃ！":
    "Inhe... inheritor!",
"うーん　ほかは　むずかしい文字ばっかりで":
    "Hmm, the rest is all hard words",
"ぜんぜんわからないや…": "and I can't understand it at all...",
"だけどここに書いてあるのが、":
    "But I know what's written here is",
"ぼくのおとうさんのことだってことはわかる！":
    "about my daddy!",
"だってぼくのおとうさんは":
    "Because my daddy is",
"ウィンダム王国の騎士団長で、":
    "the Knight Commander of the Windam Kingdom,",
"もんしょうのけいしょうしゃだから！":
    "and the inheritor of the crest!",
"あっ！": "Oh!",
"おとうさんがかえってきた！":
    "Daddy's come home!",
"闇のエレメントが復活するとき":
    "When the Dark Element revives,",
"おとうさん…そのケガどうしたの…？　":
    "Daddy... what happened to that wound...?",
"…お父さーーーーーん！！": "...Daddyyy!!",
"世界は闇に覆われ、魔物が跋扈する":
    "the world is shrouded in darkness and overrun by monsters.",
"しかし、何百年もの間": "Yet for hundreds of years,",
"闇のエレメントは復活しなかった":
    "the Dark Element did not revive.",
"その間に言い伝えは忘れられていった":
    "In that time, the old tales were forgotten.",
"紋章の継承者も実質的には　":
    "And in practice, the crest's inheritors",
"それぞれの国の権力者に継承され":
    "passed their crests to the powers that be,",
"単なる権威の象徴でしかなかった":
    "reducing them to mere symbols of authority.",
"それを防ぐことのできる唯一の力が":
    "The only power that could prevent it was",
"エレメントの紋章を": "the inheritors who carried",
"受け継いだ　継承者たちであると…　　":
    "the Element crests...",
"作られたと伝わる": "was said to have been forged.",
"それぞれのエレメントの加護の証である":
    "On this continent, where three nations blessed by",
"紋章の力を受け継いだ三つの国が栄えるこの大陸には":
    "the crests—marks of each Element's blessing—flourish,",
"恐ろしい言い伝えがあった…":
    "there was a fearsome old tale...",
"エレメント大陸": "The Element Continent",
"この大陸は火、水、風のエレメントの加護によって":
    "This continent was forged by the blessing of the Fire, Water, and Wind Elements,",
"何が天才だ…　ガキの頃に親父からもらった":
    "Some 'genius'... it's all thanks to the crest his old man",
"紋章のおかげだろうに…": "gave him as a kid...",
"紋章は代々騎士団長が継承するはずなのに…":
    "The crest is supposed to pass to the Knight Commander...",
"こいつはガキの頃に継承しちまったから…":
    "but he inherited it back when he was a brat, so...",
"最初から俺たちに出世の道はなかったんだよな":
    "there was never any path to promotion for us from the start.",
"紋章のおかげでこんな若造が騎士団長ね…":
    "So this young whippersnapper gets to be Knight Commander thanks to a crest...",
"こいつのせいで騎士団の格も地に堕ちたぜ…":
    "His fault the order's prestige has sunk into the dirt...",
"せいぜいがんばれよ、天才騎士団長さん…":
    "Good luck with that, Mr. Genius Knight Commander...",
"俺らはアンタに忠誠なんて誓わないぜ…":
    "We won't be pledging you any loyalty...",
"風の紋章の継承者ロイよ。": "Roi, inheritor of the Wind Crest.",
"闇のエレメントの復活に備え":
    "To prepare for the Dark Element's revival,",
"それぞれの紋章の継承者のもとに":
    "so that whenever that time comes,",
"人々は助け合い": "people may support one another",
"いつ、そのときが来ても万全に":
    "and fight at full strength",
"戦えるよう": "together with the inheritors,",
"いまこれより、そなたをウィンダム騎士団の":
    "from this moment, I appoint you",
"古い言い伝えを語り継がねばならない":
    "The ancient tale must be passed down, they said.",
"しかしいまやそんな大昔の言い伝えは":
    "Yet now, such age-old legends are",
"単なる物語…": "nothing but stories...",
"騎士団長に命ずる。": "Commander of the Windam Knight Order.",
"…は、謹んで承ります": "...Yes, I humbly accept.",
"エレサガ": "Elesaga",
"そんなものは、おとぎ話に過ぎなかったんだ…":
    "Such things were nothing but fairy tales...",
"おとうさん…！！": "Daddy...!!",
"ロ…ロイ…　すまん…": "R-...Roi... I'm sorry...",
"なにが…？": "For what...?",
"おとうさん…おいしゃ…　おいしゃに…":
    "Daddy... the doctor... call the doctor...",
"もう…手遅れだ…": "It's... too late...",
"俺は…死ぬ…": "I'm... going to die...",
"なにいってるの…": "What are you saying...",
"おとうさんは、けいしょうしゃなんだ…":
    "Daddy, you're the inheritor...",
"おとうさんは…": "Daddy is...",
"もんしょうの…ゆうしゃさまなんだから…":
    "the hero of the crest...",
"しぬわけないでしょ…！！":
    "there's no way you'd die...!!",
"ロイ…　左手を…　出しなさい…　早く…":
    "Roi... your left hand... give it to me... quickly...",
"え…　なに…？": "Huh... what...?",
"ロイ…　強く…　なれ…　俺よりも…強く":
    "Roi... grow strong... stronger than... me...",
"えっ？": "Huh?",
"おとうさん…　ぼくの手…":
    "Daddy... my hand...",
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
