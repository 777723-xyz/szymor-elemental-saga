#!/usr/bin/env python3
"""Fill batch 23: Hono vs Nau, final Dafill confrontation."""
import csv
import os
import re

D = {
"この真剣勝負、受けて立つわ！": "I accept this serious duel!",
"ナガレ、勝負ッ……！！！！！": "Nagare, let's settle this!!",
"うおおおおおおお！！！！": "Whooooooa!!",
"ウィン、行ってくれ…": "Win, go on ahead...",
"すぐに、ナガレと一緒にオマエに追いつくぜ！":
    "I'll catch up to you with Nagare right away!",
"…そ、それが、アンタの本当の姿かよ…？":
    "...S-So that's your true form...?",
"ウィン…　またな！！": "Win... see you later!!",
"へへ…！": "Hehe...!",
"デカくなっても相変わらずみてえだな…":
    "Even all grown up, you're still the same...",
"アンタはよー！！": "aren't you!!",
"心づかいマジサンキュだぜ…": "I really appreciate the concern...",
"でもよ…　オレは結構ドタマに来てんだぜー…":
    "but man... this gets under my skin...",
"やたらデケーじゃねえか…　てことは、オイ…":
    "You're awfully huge now... which means, hey...",
"アンタとは正々堂々のマジバトルして、":
    "I fought you fair and square, all out,",
"その上で勝ったと思ってたのによーーー…":
    "and I thought I'd won—",
"アンタ実は本気じゃなかったんだもんなー…":
    "but you were never going all out, were you...",
"アンタは確かにマジメだけどよー":
    "You're certainly earnest, but",
"それならよー…": "that's exactly why...",
"そういうところは逆に良くないと思うぜ？":
    "I think that's a bad trait, you know?",
"オレ、結構キズ付いたからな！？":
    "It really hurt my pride, alright!?",
"でも今回ばかりは…": "But this time...",
"さすがにマジでやってくれるよなー……":
    "you'll seriously go all out, right......",
"ナウ――――――よおおおおーーー！！！？":
    "Naauuu—!?",
"………コクリ": "......(nod)",
"これでアンタとの…": "With this...",
"本当のマジで絶対最後のガチバトルだー！！":
    "is our truly, absolutely final real battle!!",
"いっくぜえええええええええーーー！！！！":
    "Here I go—!!!!",
"前にオレと戦ったときは…": "When you fought me before...",
"いつも手ェ抜いてたってことかよーーーー！？":
    "you were always holding back!?",
"ナァウゥーーーーーッ！！！！！": "Naauu—!!!!!",
"…ウィン！！　頼みがある…": "...Win!! I have a favor to ask...",
"…って、言わなくても分かると思うけどよー…":
    "...though I think you already know...",
"コイツを…　ナウーをオレに任せて…":
    "Leave this guy... Nau, to me...",
"ウィンは、先に進んでくれ！！":
    "Win, you go on ahead!!",
"この先は、もうダフィールとかって…":
    "Beyond here, there's only Dafill and the like—",
"四天王最弱の奴しかいないだろ…？":
    "the weakest of the Four Generals, right...?",
"それならウィンだけでも…": "If so, even just Win...",
"闇なんとかだか魔王だかも防げると思うんだ…":
    "could stop the Dark-whatever and the Demon King...",
"…は？　…なんだよそれ…": "...Huh? ...What are you saying...",
"ウィン、頼む…": "Win, please...",
"オレは自分の弱気を…　克服したい…":
    "I want to overcome... my own cowardice...",
"ナガレを信じないまま…　あそこに置いてきた":
    "I couldn't forgive myself for leaving Nagare back there",
"自分を…　こうでもしねえと許せねーんだ！！":
    "without trusting him... unless I do this!!",
"ウィン、オレのことも信じてくれ…":
    "Win, trust me too...",
"オレはナウーに一度勝ってる、完勝でな！":
    "I've beaten Nau before—a total victory!",
"デカくなってても…　負けるワケねえ！！":
    "Even grown huge... there's no way I'll lose!!",
"ウィン！　何よりもう時間がねーんだ！！":
    "Win! More than anything, we're out of time!!",
"…まあ、その時間のほとんども":
    "...well, most of that time was probably",
"オレが無駄口叩いて潰した気がするけどよー…":
    "wasted by my own chattering, but...",
"なおのこと、ここでオレにも…":
    "All the more reason—let me",
"ナガレみてえにカッコつけさせてくれよ…":
    "look cool here, like Nagare did...",
"頼む…　ウィン！！": "Please... Win!!",
"…アンタもいいだろう？": "...You don't mind, right?",
"オレとの本気での一騎打ち。":
    "A serious one-on-one with me.",
"その為にウィンを行かせてやっても…":
    "Letting Win go for that...",
"オレの知ってるアンタなら行かせてくれるぜ？":
    "the you I know would allow it, right?",
"それとも…　デカくなったらそんな心意気も、":
    "Or... now that you've grown, has that spirit",
"アンタからは、なくなっちまうのかー？":
    "left you entirely?",
"ただのゴミじゃないか、継承者でさえ…":
    "So he's nothing but trash, even as an inheritor...",
"まあ、いっかー…": "Ah well...",
"大魔王になったら、アッチに行けばいいや…":
    "Once I'm the Great Demon King, I can just go over there...",
"と、いうワケでーーー": "And so—",
"風の継承者くん　キミはもう…":
    "Wind inheritor, you're already...",
"…用済み　じゃあねーーーーー！！！！":
    "...unneeded. See ya—!!!!",
"そしてまだまだ闇のエレメントパワーは":
    "And the Dark Element Power keeps gathering",
"ボクのところに集まり続けている…":
    "to me, more and more...",
"このままでも十分にとんでもなく強いのに…":
    "Even as is, I'm already impossibly strong...",
"まだまだ強くなるんだよボクはーーー！！！":
    "but I'm only getting stronger!!",
"ちょうどいいからキミでボクの新しい力を":
    "Perfect timing—let me test my new power",
"試してあげるよーーーー！！！": "on you—!!",
"でも強過ぎてー…": "But I might be too strong...",
"うっかり１ターンで殺しちゃったら…":
    "if I accidentally kill you in one turn...",
"もう魔王になっちゃったよーーーーーーん！！":
    "then I'd already be a Demon King—!!",
"めんごねーーーーーー！！！！？":
    "Sowwy—!!!!?",
"…と、いう夢を見た…　こわーーー！！！":
    "...And that's the dream he had... scary—!!",
"あー　やっぱりー？": "Ah, as I thought?",
"これほどの闇のエレメントパワー相手だと…":
    "Against this much Dark Element Power...",
"継承者のキミでも全く歯が立たないんだねー？":
    "even you, the inheritor, can't put up a fight, huh?",
"………っ": "......Hmph",
"一応生きてるみたいだけど…":
    "Well, at least you're still alive...",
"さすがにもう戦えなさそうだなあ…":
    "though you look done fighting...",
"…つまんねーの！！": "...How boring!!",
"これからもっとパワーが増して…":
    "From here, my power will only grow...",
"本当の魔王に…": "until I become the true Demon King...",
"大魔王ダフィール様になるっていうのに…！！":
    "the Great Demon King Dafill!!",
"カンタンにくたばりやがってえええええ！！！":
    "And you go and croak so easily!!",
"まあいい…　まあ、いいさ！！":
    "Ah well... whatever!!",
"紋章が揃ったところで…":
    "Even with all the crests gathered...",
"ボクが全ての闇のエレメンタルパワーを":
    "once I claim all the Dark Elemental Power,",
"手に入れれば同じこと…　":
    "it'll all be the same...",
"オマエらなんて相手じゃないんだよーー！！":
    "you lot are no match for me!!",
"そんな時間は与えない…！": "I won't give you that time...!",
"お喋りに付き合うつもりもない！！":
    "Nor do I intend to chat with you!!",
"俺はガキの遊びに根気よく付き合ってやる":
    "I'm not the kind of adult who patiently plays along",
"ような、オトナじゃないんでな…！":
    "with children's games...!",
"ボクの操りの術でケンカさせたのに…":
    "I made you fight with my control spell...",
"キミたち随分と仲がいいじゃないか…":
    "yet you lot get along rather well, don't you...",
"…久し振りだな。": "...It's been a while.",
"ウィン！！　…生きているな？　　イヤシ！！":
    "Win!! ...You're alive, right? Heal!!",
"オマエは…　あのときの赤いの…だなー…？":
    "You... you're the red one from back then...?",
"…キサマにはいつか会いたいと思っていた。":
    "...I'd always hoped we'd meet again someday.",
"まさか、こんな絶好の機会が来るとはな…":
    "I never imagined such a perfect chance would come...",
"さすがの俺でも予想していなかったな。":
    "Even I didn't see this coming.",
"赤いの…　てめええええ………！！":
    "Red one... you......!!",
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
