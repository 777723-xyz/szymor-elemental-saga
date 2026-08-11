#!/usr/bin/env python3
"""Fill batch 26: castle town scenes, epilogue narration."""
import csv
import os
import re

D = {
"もちろんであります！！": "Of course, sir!!",
"そうか…　ざんねんだな………": "I see... what a shame......",
"残念だなあああああああああああ…………":
    "What a shaame......",
"でも、もしも気が変わったら…":
    "But if you ever change your mind...",
"クリア前のデータからまたクリアして…":
    "clear the game again from a pre-clear save...",
"よくぞ戻った！　騎士ウィン！！":
    "Welcome back! Knight Win!!",
"遊んでくれてありがとう！！！！！！！":
    "Thank you for playing!!!!!",
"ではでは………さらば！！": "And so... farewell!!",
"エレサガ　Elemental Saga　完　！！":
    "Elesaga / Elemental Saga — The End!!",
"異論ありません！": "No objections!",
"ウィンなら誰も反対する奴なんていません！！":
    "No one would oppose Win!!",
"そして…　ピピン！！": "And... Pipin!!",
"…お、おい、何て顔をしているんだ、ウィン。":
    "...H-Hey, what's with that face, Win.",
"お前なら立派な騎士団長になる…":
    "You'll make a fine Knight Commander...",
"俺が保証する。": "I guarantee it.",
"…お前、泣きそうな顔しているぞ…。":
    "...You look like you're about to cry...",
"そんなに騎士団長になるのが嫌なのか…？":
    "Is becoming Knight Commander really so awful...?",
"フン…　ったく………": "Hmph... honestly......",
"…陛下、ロイ騎士団長…":
    "...Your Majesty, Commander Roi...",
"騎士ではない俺が、意見を言ってもいいか…？":
    "May I, though no longer a knight, offer an opinion...?",
"…なんだ、ピピン？": "...What is it, Pipin?",
"度重なる魔族軍の侵攻も最早脅威と呼ばれなくなって":
    "The demon army's repeated invasions are no longer even called a threat,",
"魔族を、闇を駆逐した我々は、いまや彼らと比べて本当に":
    "having driven out the demons and the Dark, we must ask whether we are truly",
"正しいのであろうか。お互いの内に闇を生み出しそれを増幅":
    "righteous compared to them. Both sides have birthed darkness within and amplified it;",
"し合うようになった我々がそこに目を向けない限り、本当の":
    "unless we who have done so turn our eyes upon it, the true darkness will, in the end,",
"意味での闇は結局形を変えるだけでむしろ強大になるばかり":
    "only change its shape and grow all the more powerful.",
"数百年。我々は遂に闇を克服したと言ってよいだろう。":
    "After several centuries, one could say we finally overcame the darkness.",
"この大陸のどこにも光が満たされ、闇は駆逐された。":
    "Light fills every corner of this continent, and the darkness has been driven out.",
"彼らの魔法の力も我々の兵器の前には児戯に等しい。":
    "Even their magical power is child's play before our weapons.",
"しかしそうなって後、魔族を駆逐する兵器群を持て余した":
    "But once that came to pass, humanity, at a loss over the arsenal built to purge the demons,",
"人類は、互いに争い始めた。大陸に闇はない。全てが文明の":
    "began to war among themselves. There is no darkness on the continent. Everything is",
"明かりに照らされている。野生の魔物も近い将来大陸から":
    "lit by civilization's lights. Wild monsters, too, will vanish from the continent",
"姿を消すだろう。しかし、それは勝利ではなかった。":
    "in the near future. Yet that was not a victory.",
"この先、旧坑道。": "Beyond this point: the Old Mine.",
"危険につき、立ち入りを禁ずる。":
    "Entry forbidden due to danger.",
"王国騎士団": "The Kingdom's Knight Order",
"ウィンは先にセイリューへ行こうと思った":
    "Win decided to head to Seiryu first.",
"えーと…　": "Um...",
"先にセイリューの様子を見に行くんじゃ":
    "Weren't we supposed to check on Seiryu",
"なかったのか…？": "first...?",
"も、もちろんだぜ！": "O-Of course!",
"ウィン、オマエなんでこっち来たんだよ…？":
    "Win, why did you come this way...?",
"ここは…ロイの家だ。": "This is... Roi's house.",
"いまは奴に用はない…。行くぞ。":
    "No business with him now... Let's go.",
"何かの作物の種が入っている": "It's full of seeds for some crop.",
"まだ使えそうな古い食器類が捨てられている":
    "Old dishware, still usable, has been discarded here.",
"縄やつるはしなどが入っている": "It contains ropes, pickaxes, and such.",
"中は少し湿って　かびていた…":
    "The inside is slightly damp and moldy...",
"ここはウィンダム王国の城下町だよ。":
    "This is the castle town of the Windam Kingdom.",
"…笑えよ、ウィン！": "...Smile, Win!",
"ここのお花きれいでしょ？": "The flowers here are pretty, aren't they?",
"私が毎日お水あげてるんだ！":
    "I water them every day!",
"…遂にお金を貯めたぞ。": "...I've finally saved up the money.",
"このお金で僕は、エネルギーポージョンを":
    "With this money, I'm going to buy",
"買うんだ…　買うんだ…！": "an Energy Potion... buy one...!",
"近頃はもうすっかり戦争も起きないし、":
    "Wars don't happen at all these days,",
"お前さんみたいな男にこそ、騎士が":
    "and it's men like you who suit being knights",
"相応しい時代なのかも知れないなあ。":
    "in times like these, I suppose.",
"騎士や兵隊の世界は、厳しいだろう。":
    "The world of knights and soldiers must be tough.",
"とは言え、もう昔のような戦が起こる":
    "Still, this is no longer an era where",
"時代じゃないんだ。": "wars like the old days break out.",
"あんまり気張らんでもいいんだぞ。":
    "No need to push yourself too hard.",
"おや、ウィン、元気そうだね？":
    "Oh my, Win, you look well?",
"お前さんが騎士になったって聞いたときは":
    "When I heard you'd become a knight,",
"驚いたよ。優しい子だったからなあ。":
    "I was surprised. You were such a kind boy.",
"いまの若い子は知らないかも知れないねえ":
    "The young ones today might not know this,",
"この像は、先代国王の像なんだよ！！":
    "but this statue is of the previous king!!",
"勉強になったかい？": "Did you learn something?",
"この像は…　": "This statue...",
"この像は何の像か知っているかい？":
    "Do you know whose statue this is?",
"聞こえないねえ…": "Can't hear you...",
"異常なーし": "No anomalies~",
"ウィンの家の前異常なーし": "No anomalies in front of Win's house.",
"しかしここは、いいにおいがするぜー":
    "But man, it smells great here~",
"底から　キュアポーションを　１個手に入れた！":
    "Obtained a Cure Potion from the bottom!",
"中はからっぽだった": "It was empty inside.",
"魚のエサにつかう虫が入っている":
    "It contains worms used for fish bait.",
"擦り切れたレザーコートが入っている":
    "A threadbare Leather Coat is inside.",
"あせくさい　あまり調べたくはない…":
    "It smells of sweat. I'd rather not investigate further...",
"食器や調味料の類だ": "It's dishware and seasonings.",
"赤い野菜がたくさん入っている":
    "It's full of red vegetables.",
"小麦粉か何かだ": "It's flour or something of the sort.",
"緑色の野菜がたくさん入っている":
    "It's full of green vegetables.",
"いい匂いがする　お酒かもしれない":
    "It smells nice—might be liquor.",
"兵たちの為に常備されている薬類だ":
    "These are medicines kept on hand for the soldiers.",
"医療キットを　２個　渡された！": "Received 2 Medical Kits!",
"固いパンを　２個　渡された！": "Received 2 Hard Breads!",
"レイピアを　１本　渡された！": "Received a Rapier!",
"スピアを　１本　渡された！": "Received a Spear!",
"医療キットを　５個　渡された！": "Received 5 Medical Kits!",
"レイピア(名品)を　１本　渡された！":
    "Received a Rapier (Masterwork)!",
"スピア(名品)を　１本　渡された！":
    "Received a Spear (Masterwork)!",
"考える暇もないのです！": "I don't even have time to think!",
"ウィン殿は私がどれだけ忙しいか、ご存じない":
    "Sir Win, you have no idea how busy",
"のですな？": "I am, do you?",
"用がなければ出て行ってください！！":
    "If you've no business, please leave!!",
"これは騎士ウィン殿。": "Well, if it isn't Knight Win.",
"今日はどういったご用件ですかな？":
    "What business brings you today?",
"最近も何も常に私は忙しいのです！":
    "Lately, or rather always, I'm busy!",
"私の気分！？そんなこと分かりません！":
    "My mood!? I have no idea!",
"若くして騎士になったってのに、何て謙虚な…":
    "Made a knight so young, yet so humble...",
"ウィン、俺はお前を応援しているぜ！":
    "Win, I'm rooting for you!",
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
