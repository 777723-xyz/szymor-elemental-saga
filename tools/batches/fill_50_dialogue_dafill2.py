#!/usr/bin/env python3
"""Fill batch 50: Hono aftermath, food support, Dafill's reveal."""
import csv
import os
import re

D = {
"1000\\G 手に入れた！": "Gained 1000G!",
"ぜんぶつぶれたりせず弾力があるんだ。":
    "it doesn't crush—it stays springy.",
"いくらナウーが正々堂々の肉体バトルを":
    "As much as Nau imposes fair, all-out battles",
"これ以上パワーを消耗したら…":
    "If I drain any more power...",
"………くそっ……": ".........Damn...",
"親父…　すまん。": "Dad... sorry.",
"四天王を逃がしちまった…":
    "I let a Four General get away...",
"わしにお前を責める資格はない…":
    "I've no right to blame you...",
"お前は…よくやった。": "You... did well.",
"…そうだと、いいな………":
    "...I hope so......",
"ホノオ！　あんたも早く手当を手伝え！":
    "Hono! You help with the treatment too!",
"薬は持ってるだろ！？": "You've got medicine, right!?",
"お、おう…！！": "O-Okay...!!",
"ホノオは本物のゾモロドネガルを受け取った！":
    "Hono received a genuine Zomolod Negal!",
"漠然と、火の恵み、水の恵、風の恵み…自然からの恩恵、":
    "Vaguely, the blessings of Fire, Water, Wind... the gifts of nature,",
"我が王国はまだまだナガレ様…そしてセイリュー":
    "Our kingdom has yet to fully repay Lady Nagare",
"の皆様へのご恩をお返ししきれません。":
    "and all the people of Seiryu.",
"お力になれることがあれば何でもお申しつけを！":
    "If there's anything we can do, please command us!",
"おお…　ナガレ様！": "Oh... Lady Nagare!",
"我が軍の兵はお役に立ちましたでしょうか？":
    "Did our soldiers prove useful?",
"ええ、とても助かりました。": "Yes, they helped greatly.",
"これで暗黒大陸に渡ることができます。":
    "With this, we can cross to the Dark Continent.",
"大臣のご尽力のおかげです": "It's all thanks to your minister's efforts.",
"足りているとは恐れながら申せません…。":
    "I hesitate to say it's enough...",
"しかし、コメは栄養価が高い上、腹持ちが良く、":
    "But rice is nutritious and filling, and",
"そのおかげで、兵や民たちはまだまだ元気です。":
    "thanks to that, our soldiers and people remain hale.",
"それを聞いて少し安心しました…。":
    "Hearing that puts my mind at ease...",
"セイリューでも食料は不足気味なので、":
    "Seiryu itself is running short on food, so",
"これ以上の支援は出来そうにないもので…。":
    "further aid may not be possible...",
"これはこれはナガレ様、ご機嫌うるわしゅう。":
    "Well, well, Lady Nagare, in good spirits I see.",
"存じ上げております…。": "We are well aware...",
"我が国でも少ない材料で多くの人数分用意できる":
    "Our country too is inventing new dishes that feed many",
"新料理を発明中です。": "from few ingredients.",
"うお！マジかよ！？": "Whoa! For real!?",
"どんな料理なんだろうな、楽しみだぜー":
    "What kind of dish, I wonder—can't wait~",
"…殿下。いまは非常時ゆえ許しますが…":
    "...Your Highness. I'll permit it given the emergency, but...",
"教育的説教がどんどんたまっておりますので、":
    "my educational lectures are piling up, so",
"覚悟しておいて下され。": "please be prepared.",
"えっ！　なんでだよ？": "Huh!? Why?",
"オレ怒られるようなことそんなにしてるか！？":
    "Am I doing anything worth scolding!?",
"あはは、あたしとオタキ様みたいだ。":
    "Ahaha, just like me and Lady Otaki.",
"これは行政官シダルタ殿、ご挨拶ありがとう":
    "Lord Sidarta, Administrator, thank you for the",
"ございます。　セイリューからの食料支援は":
    "greeting. Is the food support from Seiryu",
"足りていますか？": "sufficient?",
"…来るよ。": "...Here they come.",
"陛下…": "Your Majesty...",
"まさか、こやつのことを…？":
    "You don't mean... you know of this one...?",
"…ボクのことを、知っているの？":
    "...Do you know who I am?",
"…いや、知らんな": "...No, I don't.",
"やっぱりココって…": "So this place really is...",
"バーーーカ！！しかいないのーーーー！！？？　":
    "full of idiots—!!??",
"だははは！": "Bahaha!",
"本当にキミたちは…": "You lot truly...",
"ボクの思い通りに動いてくれるねー！":
    "move just as I expect, don't you!",
"素直っていうか、バカっていうかー？":
    "Obedient, or just stupid~?",
"ぬわにいいいいいいいいいいい！？":
    "Whawhawhawha—!?",
"皆！　うかつに近づくな！　距離を取れ！":
    "Everyone! Don't approach carelessly! Keep your distance!",
"ろ、ロイどの！！": "L-Lord Roi!!",
"これだけ囲んでしまえば、一気に倒せますぞ！":
    "Surround him like this and we can take him down at once!",
"いまのうちに全員で…": "Let's all strike now—",
"サクソン殿、待たれよ。": "Lord Saxon, hold.",
"この敵はただ者ではない…":
    "This enemy is no ordinary foe...",
"この者は、闇の四天王…": "This one is a Four Dark General...",
"さきほどそう名乗ったはず！":
    "he named himself as such moments ago!",
"こ、こんな派手なだけの若造があああ？":
    "Th-This flashy brat alone...?",
"皆の者、ロイに従え！": "All of you, obey Roi!",
"ロイの命令を、我の命令と思え！！":
    "Consider Roi's orders as mine!!",
"…ロイ、すまぬ、ここは、頼む…":
    "...Roi, forgive me, but I leave this to you...",
"仕方ありませんな…": "It can't be helped...",
"しかし、オレにも作戦などはありませんぞ…":
    "But I have no plan either, you know...",
"兵たちよー！　囲めーい！！":
    "Soldiers! Surround him!!",
"…うむ": "...Mm.",
"へー？": "Oh?",
"少しはちゃんとしたおつむの子も、":
    "So there are a few with proper brains",
"いるんだーーー？": "around here~?",
"こやつを決して逃がすなーー！！":
    "Never let him escape—!!",
"ご明察ーーー！": "Perceptive—!",
"ボクこそは闇の四天王最弱かつ最強の…":
    "I am the weakest yet strongest of the Four Dark Generals...",
"堕天の炎…　ダフィールさーーー！！":
    "the Fallen Flame... Dafill—!!",
"…なに！": "...What!",
"…闇の四天王…　最弱、かつ最強…":
    "...A Four Dark General... the weakest, yet strongest...",
"…堕天の炎…　ダフィールだと…！！？":
    "...The Fallen Flame... Dafill, he says...!!?",
"風のエレメントの加護で突然出来たお城と国である、":
    "The castle and kingdom that suddenly arose through the Wind Element's blessing—",
"美味しいパンを　３個　もらった！":
    "Received 3 Delicious Breads!",
"高級医療キットを　３個　もらった！":
    "Received 3 Premium Medical Kits!",
"ウィンさま…　": "Master Win...",
"私はいつも、ウィンさまのお家のパンの味を":
    "I always use the taste of your family's bread",
"お手本に、パンを作ってるんです…":
    "as my model when baking...",
"やっと、近い味が作れたと思います…！":
    "I think I've finally managed to get close...!",
"よかったら、いつかご感想をお聞かせ下さい…":
    "If you'd like, please let me know what you think someday...",
"みんな目を覚ませ…！！":
    "Everyone, wake up...!!",
"俺たちは同士討ちをしている…！！":
    "We're fighting each other!!",
"さすがに時間を食いすぎちゃったからー":
    "Well, it's taken too long, so—",
"最後まで見られないのは残念なんだけどーーー":
    "I'm sorry I can't watch to the end, but—",
"もっと面白い方を操ることにしたよー":
    "I've decided to control the more amusing one.",
"みんな目を覚ませー！！": "Everyone, wake up!!",
"俺たちは同士討ちをしている！！":
    "We're fighting among ourselves!!",
"キミ…　何者だい？": "You... who are you?",
"どういう意味だ…？": "What do you mean...?",
"ちょっとだけ試させてもらっていいかなー？":
    "Mind if I test you a little?",
"肉弾戦はボクの苦手とするところなんだケド…":
    "Close combat isn't my forte, but...",
"ひさびさにー": "it's been a while since I've",
"ボクの炎で焼けるニンゲンの匂いをかいで":
    "wanted to smell humans burning",
"みたくなったからーーーー！！！！？":
    "in my flames—!!!!?",
"フン、いいだろう。": "Hmph, very well.",
"俺もバケモノの血が何色なのかを、":
    "I too wanted to see what color",
"確かめてみたくなったからな。":
    "a monster's blood is.",
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
