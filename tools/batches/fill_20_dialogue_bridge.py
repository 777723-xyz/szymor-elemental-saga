#!/usr/bin/env python3
"""Fill batch 20: post-collapse towns, crest power surges, bridge to dark continent."""
import csv
import os
import re

D = {
"このバケモノを俺が退治しに来てやったのさ。":
    "I've come to slay this monster in place of you and your incompetence.",
"レイピアとしてはとても重い上に大きく、":
    "It's far too heavy and large for a rapier, and",
"管理しているつもりだよ。": "I try to manage things, you know.",
"ちょっと、どいてちょうだい！": "Excuse me, move aside!",
"…って継承者さま！　失礼しましたーーー！！":
    "...oh, Inheritor-sama! Forgive me—!!",
"いやー…　": "Well...",
"儲かってるのにあんまり嬉しくないですね…":
    "Business is booming, but I can't say I'm happy about it...",
"さすがにこれだけみんなが大変そうだと…":
    "With everyone struggling this much...",
"あー、どうも…　道具屋です。": "Ah, hello... Item shop here.",
"なんか街が崩壊してからの方がめっちゃ":
    "Ever since the town collapsed, we've had way more",
"お客さん来て…　もうかってます…":
    "customers... business is great...",
"フレイムのみんなは大丈夫かなあ…？":
    "I wonder if everyone in Flame is okay...?",
"いいねえ　若いってのは！": "Ah, youth is a wonderful thing!",
"でも、遠慮すんなよ。このくらいしか、":
    "But don't hold back. This is about all",
"それなら隣のベッドで休んで行けよ？":
    "In that case, rest in the next bed over, why don't you?",
"使わせるように言われているからな！":
    "I've been told to let you use it!",
"こっちの皿はこっち！　この器はこっち！":
    "This plate goes here! This bowl goes here!",
"速い、俺速い！　まるで風の紋章を使う":
    "I'm fast, I'm fast! Just like Win",
"ウィンのように！": "using the Wind Crest!",
"この食堂もすっかり使われなくなりました…":
    "Even this dining hall has fallen into disuse...",
"王でさえ、いまは兵と同じ食事を食べて":
    "Even the king now eats the same rations",
"らっしゃいます。": "as the soldiers.",
"城の壊れた部分を調べて回っているんだけれど":
    "I've been checking the castle's damaged sections, and",
"ひどいなあ…": "it's awful...",
"ぜんぶ直るのに何年かかることやら…":
    "How many years will it take to repair everything...",
"ウィン！　面白い本は見つかった？":
    "Win! Did you find any interesting books?",
"ひ、ひでえ目にあった…": "I-I had a terrible time...",
"きっとこの先、もっと酷い目が待ってる…":
    "Surely worse awaits ahead...",
"何が起こるか分からないな…。": "You never know what will happen...",
"うお！　めちゃくちゃ紋章が光った！！":
    "Whoa! The crest just blazed up!!",
"…なんだ？　急に身体に力が漲るような…":
    "...What is this? Strength suddenly surging through my body...",
"これは…": "This is...",
"ウィンはシップウの魔法をおぼえた！":
    "Win learned the Gale spell!",
"ホノオはダイバクハツの魔法をおぼえた！":
    "Hono learned the Great Explosion spell!",
"ナガレはイヤシノアメの魔法をおぼえた！":
    "Nagare learned the Healing Rain spell!",
"なんだよ突然…この急激なパワーアップ感は…":
    "What's with this sudden... surge of power...",
"いまならどんな敵が相手でも負ける気が…":
    "Right now I feel like I could beat any enemy...",
"ちょっと黙れ、ホノオ！！": "Quiet, Hono!!",
"あ！？　なんだよ急にーーー！？":
    "Ah!? What's your problem—!?",
"紋章は闇の力が強まるのに合わせて、":
    "The crests shine brighter and grow stronger as",
"その輝きを増して、力を強めるんだろ…？":
    "the Dark power strengthens, right...?",
"あたしたちがこんなに急に強くなるってこと…":
    "So for us to get this strong this suddenly...",
"それはつまり…": "means that...",
"あ…　闇のエレメントの力が急に":
    "Ah... the Dark Element's power is suddenly",
"めちゃくちゃ強くなってるってこと…か…":
    "getting ridiculously strong... is what it means...",
"あれ…？　なんか暗く………": "Huh...? It's gotten dark......",
"げえっ！？　な、なんだありゃああああ！！":
    "Whoa!? Wh-What the heck is that!!",
"なんかデッカイ化け物が……！！":
    "Some giant monster......!!",
"降って来たあああああああ！！":
    "It's falling on us!!",
"おい、まただ！　さっきよりも激しい…！":
    "Hey, again! Even more intense than before...!",
"ウィンはイカヅチの魔法をおぼえた！":
    "Win learned the Thunderclap spell!",
"ホノオはドコンジョウの魔法をおぼえた！":
    "Hono learned the Guts spell!",
"ナガレはマンキンタンとツナミの魔法をおぼえた！":
    "Nagare learned the Mankintan and Tsunami spells!",
"なんだこの感じ…　オレ強過ぎになったぞ！！":
    "What is this feeling... I've gotten way too strong!!",
"…まるで神様にでもなったような、か…？":
    "...It's like I've become a god or something...?",
"そんな感じだぜナガレ！": "Exactly, Nagare!",
"いまならもう、どんなバケモンが出てきても":
    "Right now, no matter what monster shows up,",
"全く負ける気がしねーぜ！！": "I don't feel like I could lose!!",
"バカ！　あたしらが強くなるほど…":
    "Idiot! The stronger we get...",
"闇の力も同じように強まってるんだ！":
    "the Dark power grows just as much!",
"だから喜んでる場合じゃないんだぞ！":
    "So this is no time to celebrate!",
"あ、ああ…　そうだったな…！":
    "Ah, right... that's true...!",
"しかしこの無敵感は、確かにちょっとな…":
    "But this feeling of invincibility is honestly...",
"不気味なくらいだぜー………": "downright eerie.......",
"…こりゃまたスゲーのが飛んで来たぜ。":
    "...Well, here comes another huge one.",
"あれもさっさと片付けて、闇も封じて…":
    "Let's deal with that one quick, seal away the Dark...",
"これを終わりにするぞ！！": "and end all this!!",
"これからあんなのがガンガンこの大陸に":
    "From now on, things like that will keep slamming",
"飛んでくるってんだろ…？": "into this continent, right...?",
"急がねえと…": "We'd better hurry...",
"あたし、なぜかちっとも怖くないんだ…":
    "Oddly enough, I'm not scared at all...",
"何だかもう、村のみんなとの暮らしも…":
    "Somehow, even life with everyone back in the village...",
"遠くに感じる…": "feels so distant...",
"そんなん言うなよ、ナガレ！": "Don't say that, Nagare!",
"くっそーーーー………": "Dammit.......",
"さっさと行こうぜ！　ウィン！！": "Let's go already! Win!!",
"俺は歴戦の勇士なんで、こんな任務軽いっすよ":
    "I'm a battle-hardened veteran, so this mission's a breeze.",
"どうも状態異常使ってくる魔物が多いね。":
    "There sure are a lot of monsters using ailments.",
"万金丹を多めに買っておいた方がよさそうっす。":
    "Better stock up on Mankintan.",
"ライスボールとか万金丹とか、売っている街で":
    "Did you know rice balls, Mankintan, and the like",
"微妙に値段違うの知ってるか？": "cost slightly different amounts by town?",
"びっくりしたよー": "I was surprised.",
"この前セイリューの錬金術師の店に行ったら、":
    "The other day I went to the alchemist's shop in Seiryu, and",
"ちょっと割引してましたよ？": "they had a small discount.",
"行ってみてくださいっす。": "You should go check it out.",
"紋章の継承者だと、暗黒大陸の病気が効かない":
    "Is it true that ailments of the Dark Continent don't work",
"って本当か？　羨ましいな…": "on crest inheritors? Lucky...",
"誰も見たことのない土地へ行けるんだからな。":
    "You get to go where no one's ever set foot.",
"騎士団のみんな、橋の警備よろしくな！":
    "Knight Order, the bridge guard is in your hands!",
"け、継承者の皆様に…敬礼！":
    "S-Salute to the inheritors...!",
"おっ！　なんだそれ！": "Oh! What's that!",
"騎士団はそうやってあいさつすんのか！？":
    "Is that how the knight order greets people!?",
"継承者御一行様、お通りー！": "Make way for the inheritors—!",
"この巨大な槍はわしが若い頃から愛用していた":
    "This great spear has been my beloved weapon",
"すごく強力な槍だ！": "since my youth—a very powerful spear!",
"我が一族に代々伝わる品だ！": "It's been passed down my family for generations!",
"ん？　確かにこの槍は大事なものだが…":
    "Hm? This spear is indeed precious, but...",
"いまはそれよりも、少しでもお前たちの力に":
    "right now, more than that, I must give you anything",
"なるものは何でも渡さねばなるまい！":
    "that can be of any help!",
"なーに！　遠慮はいらんぞ！": "What! No need to hold back!",
"平和になったら返してくれればいいのだ！":
    "Just return it once peace is restored!",
"そうだ、ウィン！": "Oh, right, Win!",
"お前に良いものをやろう！": "I'll give you something good!",
"にっかり青江を手に入れた！": "Obtained Nikkari Aoe!",
"まー、どのみちここまで来といて、":
    "Well, having come this far,",
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
