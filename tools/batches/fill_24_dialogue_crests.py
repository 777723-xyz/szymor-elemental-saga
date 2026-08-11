#!/usr/bin/env python3
"""Fill batch 24: Pipin's dual crests, final Dafill, legendary Bandit."""
import csv
import os
import re

D = {
"…と、いう夢を見た…　こわーーーー！！！":
    "...And that's the dream he had... scary—!!",
"その両手の輝きは……　まさか…………！！":
    "That glow in both hands... no way......!!",
"ピピンの右手には火の紋章が…":
    "In Pipin's right hand, the Fire Crest...",
"左手には水の紋章が輝いている！！":
    "and in his left, the Water Crest shines!!",
"…託された。": "...They were entrusted to me.",
"あいつらから託されたんだ…": "They were entrusted to me by them...",
"ふたつの紋章を継承者から…　このオレがな。":
    "Two crests, from the inheritors... to me, of all people.",
"チクショーーーー！！！！！": "Damn it—!!!!!",
"な、なななな…？": "Wh-Wh-Wh-What...?",
"意味ねえじゃんかよアイツらーーーー！！！！":
    "Then their sacrifice meant nothing—!!!!",
"役立たずがああああああーー！！！！":
    "You useless—!!!",
"ウィン…　俺は散々、お前に迷惑をかけた…":
    "Win... I've caused you nothing but trouble...",
"正直なところ、気まずいったらないんだが…、":
    "Honestly, it's terribly awkward, but...",
"…俺と一緒に戦えるな？": "...You'll fight alongside me, right?",
"何が起こった…！！？？": "What happened...!!??",
"ウィンは大きく頷いた！": "Win nodded firmly!",
"ダハハハハハハハハーーッ！！！！":
    "Bwahahahaha—!!",
"なーんだ…": "Oh my...",
"全然、自我…？　保てちゃってるんですケド…":
    "I can... keep my sense of self... no problem at all...",
"…チッ！！": "...Tch!!",
"ああああぁぁぁぁアアアァァーーッ…！！！":
    "Aaaaaaah—!!!",
"キ…モチ…ィイ…ッ！！！！！":
    "It... feels... GOOD......!!!!!",
"コレはもう明らかに…":
    "This is clearly...",
"ボクは最強の存在になってしまったァーッ！！":
    "I've become the strongest being—!!",
"ザーンネーーーンッ！！": "Too bad for you!!",
"闇インフルエンザでオマエら人間は滅び…":
    "The Dark Flu will wipe out you humans...",
"この大陸に闇の王国を築きまーーーす！！":
    "and I'll build a Dark Kingdom on this continent!!",
"そしてこの地に溢れ…満ち続ける闇の力を":
    "And with the Dark power that fills and overflows this land,",
"もとに……": "as its foundation......",
"すべての世界を僕にひざまずかせる時代が":
    "The era of all worlds kneeling before me",
"決定しましたーーーーー確定でーーす！！！！":
    "is hereby decided—final!!",
"…闇インフルエンザ…？": "...Dark Flu...?",
"すべての人間が滅びるだと…！？":
    "All humans will perish, you say...!?",
"…ウィン！！　まだ終わっていない！！":
    "...Win!! It's not over yet!!",
"顔をあげろ！！": "Look up!!",
"このガキンチョはいまや…":
    "This brat is now...",
"全ての闇のエレメントパワーと一体なんだろ？":
    "one with all the Dark Element Power, right?",
"それなら…　闇のエレメントパワーから生じた":
    "If so... maybe all the disasters born of the",
"災厄のすべても…　コイツを倒せば消えるかも":
    "Dark Element Power will vanish if we defeat him",
"しれん…": "...",
"ダハハハハハ！！！！そうかもーーー！！！！":
    "Bwahahaha!! Maybe—!!",
"いまのボクは勝手に…　":
    "Right now, I'm...",
"闇のエレメントパワーを全て吸い込んでしまう":
    "a black hole, so to speak, that automatically",
"いわばブラックホール状態！！":
    "sucks in all the Dark Element Power!!",
"そのボクがいなくなれば、集まったパワー…":
    "If I were gone, the gathered power...",
"フシュルウウウウゥゥゥゥゥアアーッ！！！！":
    "HssssssssAAAAH—!!!!",
"そして集まろうとしていたパワーも…":
    "and even the power that was gathering...",
"全て別次元に吹き飛んでしまうと思うよ？":
    "would all be blown away to another dimension, I think?",
"だけど無理だなあああああ！！！！":
    "But it's impossible—!!",
"だって…ボクがもっとも究極の存在だから…":
    "Because... I am the ultimate being...",
"溢れるダークパワーそのものだからねーー！！":
    "the overflowing Dark Power itself!!",
"お喋りの時間はないと言ったろう？":
    "I told you there's no time for talk, didn't I?",
"ダフィール…　本当のラストバトルを始めよう":
    "Dafill... let's begin the true final battle.",
"バトルになるかも怪しいなーーーー":
    "I doubt this will even be a battle~",
"そんなに時間が惜しいなら………":
    "If you're so short on time......",
"一瞬で終りにしてやルォォァァーーアア！！":
    "then I'll end this in an instant—!!",
"「何度も会ってるだろ！俺とお前らは！！！！":
    '"We\'ve met plenty of times, you and I!!!!"',
"「……………誰ですか？": '".........Who are you?"',
"「お前まで分からないのか……": '"You don\'t know me either......',
"　それはなんか、ちょっとショックだろ………":
    " that's... honestly a bit of a shock......",
"　何でもいい　さっさとかかってこい！":
    " Whatever—just come at me!",
"「クソ―! ムカつく奴らだぜ！":
    '"Damn! What an annoying bunch!"',
"　ああ！もういい！！": " Ah! Enough!!",
"　俺はバンデッドだ！！": " I am a Bandit!!",
"「最初は新米だったが、その後熟練に至り…":
    '"At first I was a rookie, but I rose to skilled...',
"　遂には伝説のバンデッドとなった！！":
    " and at last became the Legendary Bandit!!",
"「いまの俺なら、もうお前たちも負けん！！":
    '"With my current self, I won\'t lose to you!!',
"　伝説級の俺の強さに震えるがいい！！":
    " Tremble before my legendary strength!!",
"「あれ？　どこだよ、ここ…？":
    '"Huh? Where is this...?"',
"「おまえら…　どうしてここにいる？":
    '"You lot... why are you here?"',
"黒い蛇のようなものがはみ出ている…":
    "Something like a black snake is sticking out...",
"「わからないよ…　一体全体何が起こって…":
    '"I don\'t understand... what on earth is happening...',
"「ックックックッ…　": '"Heh heh heh...',
"「やっぱりな…": '"Just as I thought...',
"　俺だけじゃなかったみたいだ…":
    " looks like I'm not the only one...",
"　何度も戦い…　そしてここにたどり着いたのは…":
    " After fighting again and again... I've ended up here...",
"「まだ他にもなんかいるのか！？":
    '"There\'s something else too!?"',
"「こんなとこ　早く出たいのに！！":
    '"I want to get out of this place quickly!!',
"　何でもいい　さっさと出てこい！！":
    " Whatever—come on out already!!",
"「フッ…": '"Heh...',
"　いいだろう…そろそろ俺も…":
    " fine then... it's about time I...",
"「おまえらに勝てるだろうからな！！":
    '"since I can beat you all!!',
"「お前それ最初のセリフと同じじゃねえか！":
    '"That\'s the same line as your first one!"',
"キュアポーションを手に入れた！":
    "Obtained a Cure Potion!",
"ショックポーションを手に入れた！":
    "Obtained a Shock Potion!",
"申せ！　ピピン！": "Speak! Pipin!",
"…俺は前から思っていた。": "...I've thought this for a while.",
"なぜ、継承者は必ず騎士団長にならねば":
    "Why must the inheritor always become",
"ならないのか…。": "the Knight Commander...",
"騎士団長は、兵たち全てをまとめあげ、":
    "The Knight Commander must unite all the soldiers,",
"城や街の守りを日々管理、監督せねばならん…":
    "and manage and supervise the defenses of castle and town daily...",
"身体よりも頭を使う仕事だ。":
    "It's a job for the mind, not the body.",
"その点、継承者は、戦士であればいい。":
    "The inheritor, by contrast, need only be a warrior.",
"いざとなったときに、闇の力と戦う為に、":
    "To fight the Dark power when the time comes,",
"強いものがならねばならん…それなら…":
    "a strong one must take the role... if so...",
"騎士団長と継承者は…求められる能力が違う":
    "the Knight Commander and the inheritor require different abilities,",
"のだから、別々の者がやればいいと俺は思う。":
    "so I think different people should fill the roles.",
"ウィンはこのままで問題ない…。":
    "Win is fine just as he is...",
"頭もよく経験豊富なロイ…":
    "The clever, experienced Roi...",
"あんたが騎士団長のままでいいだろう。":
    "you should stay Knight Commander.",
"…ほう。": "...Oh?",
"確かに…": "Indeed...",
"騎士団長の仕事だけを考えれば、":
    "Considering only the Knight Commander's duties,",
"継承者を無理に団長に据える必要はない！":
    "there's no need to force the inheritor into the role!",
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
