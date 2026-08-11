#!/usr/bin/env python3
"""Fill batch 08: Flame Kingdom storyline dialogue."""
import csv
import os

D = {
"万金丹を超える、便利でしかも安い薬を":
    "To develop a medicine even more useful than Mankintan, and cheap to boot,",
"開発するため、日夜研究の毎日！":
    "I research day and night!",
"えっ！？": "Huh!?",
"あっ！！": "Ah!!",
"それなら…": "In that case...",
"おーい！！": "Heyyy!!",
"あたしだけじゃちょっとキツイんだ…":
    "I can't handle this on my own...",
"助太刀してくれーーー！！": "Give me a hand—!!",
"なんかすげえヤバイ感じだな…！": "This feels seriously bad...!",
"とにかくトリカゼに助太刀しよう！急げ！":
    "Either way, let's help Torikaze! Hurry!",
"お、おい…　なんだこりゃあ…！":
    "H-Hey... what the heck is this...!",
"川が氾濫した！？　みんなは大丈夫なのか！？":
    "The river flooded!? Is everyone okay!?",
"いまここを離れるわけにはいかねえ！！":
    "I can't leave here now!!",
"親父…　みんな…　生きていてくれ…！":
    "Dad... everyone... please be alive...!",
"…ナイフ？": "...A knife?",
"オマエ、一体どっからこんなモンを…？？":
    "You, where on earth did you get something like this...??",
"まあいいや、コレはオレがもらっとくぜ！":
    "Whatever, I'll be taking this!",
"フッーン！ッっフーン！": "Hmph! Hmph!",
"クーンックー！": "Yip yip!",
"ホノオはマンゴーシュを手に入れた！":
    "Hono obtained a Main Gauche!",
"しかし変な鳴き声の犬…": "But what a weird bark for a dog...",
"って、オマエなんでそんなモン咥えてんだ！？":
    "Hey, why are you carrying something like that in your mouth!?",
"ホノオは犬からそれを奪い取った！":
    "Hono snatched it from the dog!",
"…なに？": "...What?",
"…なんだって？": "...What did you say?",
"………ッ": "......Hmph",
"無事に帰ってくれ…　ホノオ。": "Come home safe... Hono.",
"当たり前だろ？　あ、それより、":
    "Of course, right? Oh, anyway,",
"アレ、あるか？": "you still have it, don't you?",
"む、なんのことだ？": "Hm? What do you mean?",
"おお…　遂に継承者が揃ったか…。":
    "Oh... at last, all the inheritors are gathered...",
"王に代々受け継がれる、この国の宝剣だよ。":
    "It's the treasured sword of this kingdom, passed down through its kings.",
"ちょっとばかし前倒しにして…": "A little ahead of schedule...",
"アレをオレにくれないか？": "could you give it to me?",
"無論かまわんが…": "I don't mind at all, but...",
"一応しきたりでは王になるときに渡すものだ。":
    "By tradition, it's meant to be given when one becomes king.",
"しかし、なぜ急ごうと思った…？": "But why the hurry...?",
"…暗黒大陸に渡るのだな？": "...You're crossing to the Dark Continent, aren't you?",
"オレ戦いだと夢中になっちまって、あと先を":
    "When I get into a fight, I get so caught up",
"考えなくなっちまうところがあるからよ…":
    "that I stop thinking ahead, you see...",
"けど…　右手に王の剣があれば…":
    "But... if I hold the king's sword in my right hand...",
"ソレを見る度に思い出せるんじゃねえかと":
    "I figured every time I look at it,",
"思ってな…　大事なことを。": "I'd remember... what matters most.",
"そうか…　よくわかった。": "I see... I understand.",
"ありがとよ、親父！": "Thanks, Dad!",
"代わりに俺のシャムシールを親父に渡そうか？":
    "How about I give you my Shamshir in return?",
"それはやめておこう。形見にもらうようで…":
    "Better not. It'd feel like a keepsake from the dead...",
"弱気になりそうだからな…。": "it would make me lose heart...",
"あ、そう………": "Ah, right...",
"じゃあ親父、ちょっくら行ってくるぜ！":
    "Well then, Dad, I'm heading out!",
"うむ、我が息子に武運を！":
    "Indeed, may fortune favor my son in battle!",
"ああ！　行ってくるぜ、親父！": "Yeah! I'm off, Dad!",
"そうか…　": "I see...",
"ウィン、きさまどこへ行くつもりだ！？":
    "Win, where exactly do you think you're going!?",
"王の間へ行かなくていいのか！？":
    "Don't you need to go to the throne room!?",
"よし。": "Alright.",
"…突入する！": "...Charging in!",
"…ならさっさと済ませろ！": "...Then hurry up and get it done!",
"…これから突入するが、": "...We're about to charge in, but",
"…その前に、装備の点検、回復等…":
    "...before that, check your gear, heal up...",
"ひととおり済ませてあるだろうな？":
    "you've done all that, right?",
"ウィン…！": "Win...!",
"いやいやいやいやいや…": "No no no no no...",
"こんなときだからこそ、よからぬことを":
    "Precisely in times like these, there are those",
"考えるやつも出てくるんでな。": "who'd plot mischief.",
"以前にも増して、警備を強化している。":
    "We've strengthened security more than ever.",
"先にロイに会いに行こうと、ウィンは思った":
    "Win decided to go see Roi first.",
"人数は足りないが…": "We're short on numbers, but...",
"未知の魔物が相手では、数を揃えればいいという":
    "against unknown monsters, numbers alone aren't",
"ものでもなかろう…": "necessarily the answer...",
"闇が膨らみ": "The darkness swells,",
"闇が閉じ": "the darkness closes,",
"次元が": "the dimensions",
"歪んでいく": "warp apart.",
"しかしよく見ると、ダフィールの口の中から":
    "But look closely—from inside Dafill's mouth,",
"闇は開き": "the darkness opens,",
"闇は広がり": "the darkness spreads,",
"次元が": "the dimensions",
"戻る": "return to normal.",
"「いいか…　終わりじゃない…":
    '"Listen... this isn\'t the end...',
"　俺は何度でも蘇って…お前らの前に現れる！":
    " I'll be reborn again and again... and appear before you!",
"　何度でもだ…　　　　　ぐはあッ！！！！":
    " Again and again... GWAH!!!!",
"「誰だっオマエは！？": '"Who the heck are you!?"',
"看板には、": "The sign reads,",
"『騎士団駐屯本部』": '"Knight Order Garrison HQ"',
"と、書いてある。": "written in bold.",
"なんだって？": "What did you say?",
"レザーコートを　一着　手に入れた！":
    "Obtained a Leather Coat!",
"固いパンを　１個　手に入れた！": "Obtained a Hard Bread!",
"おい、勝手に触るんじゃねえ！":
    "Hey, don't touch that without asking!",
"『ここ最近の事件と報告』": '"Recent Incidents and Reports"',
"・西の監視塔の見回りについて": "- About patrolling the West Watchtower",
"他国との戦争の為に作られた西の塔ですが、定期的に":
    "The western tower was built for wars with other nations, but bandits",
"泥棒や魔物が住み着くので、見回りが大変です。":
    "and monsters regularly move in, making patrols a hassle.",
"壊してしまってはどうでしょう。":
    "Perhaps we should just demolish it.",
"・騎士と兵士の槍嫌いについて":
    "- About knights and soldiers hating spears",
"王国では戦争の為に槍の訓練が推奨されていますが、":
    "The kingdom recommends spear training for war, but spears are",
"槍は重くて長いので、兵はおろか、騎士でさえ全然":
    "heavy and long, so not just soldiers—even knights aren't",
"練習していません。槍のイメージアップが必要です。":
    "practicing at all. Spears need a better image.",
"…と、書かれた本がある。読んでみようか？":
    "There's a book with these words written in it. Should we read it?",
"・フレイムからの野盗、ごろつき、密売人の流入":
    "- Influx of bandits, thugs, and smugglers from Flame",
"関所の警備の強化をしています。通行手形の発行手続きを":
    "We've strengthened security at the checkpoint. We've made the permit",
"複雑にして、料金も値上げしました。":
    "issuing process more complicated and raised the fees.",
"街のパトロールも増やしました。":
    "We've also increased town patrols.",
"『色々な見積もりリスト』": '"Various Estimates List"',
"城内宿舎の改築　資材6540G　人手5800G":
    "Renovating castle barracks - materials 6540G, labor 5800G",
"出来ます。ベットの数が元々足りていませんしね…。":
    "It can be done. The number of beds has never been enough...",
"各区画への公衆トイレ設置　資材4500G　人手7200G":
    "Public toilets in each ward - materials 4500G, labor 7200G",
"各区画でなくとも一個か二個でもいいです。切実に…。":
    "Even one or two would do, not per ward. We beg you...",
"武器庫の掃除　資材800G　人手300G":
    "Cleaning the armory - materials 800G, labor 300G",
"陛下からストロングに御自ら命令してください！":
    "Please order Strong to do it yourself, Your Majesty!",
"軍馬の購入　資材？？？　人手？？？":
    "Purchasing warhorses - materials ???, labor ???",
"一体いつからこの大陸には馬がいなくなったのでしょう…":
    "Just when did horses disappear from this continent, I wonder...",
"バルコニーの改修　資材5136G　人手107050G":
    "Renovating the balcony - materials 5136G, labor 107050G",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "dialogue.tsv"))


def norm(s):
    return s.strip(" \u3000")


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
