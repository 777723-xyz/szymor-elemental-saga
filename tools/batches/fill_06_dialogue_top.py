#!/usr/bin/env python3
"""Fill batch 06: highest-frequency dialogue lines (Windam prologue etc.).

Keys are matched after stripping leading/trailing (ASCII + full-width) spaces,
so centering spaces in the source are tolerated; English lines are left-aligned.
"""
import csv
import os

D = {
"持ち出して役に立つようなものは何も見つけられなかった…":
    "There was nothing worth taking with us...",
"ハヤテを使えば目的地にすぐに行けるな":
    "If we use Hayate, we'll reach our destination in no time.",
"…と、ウィンは思った": "...Win thought to himself.",
"…と、表紙に書かれた本がある。読んでみようか…。":
    "There's a book with these words on the cover. Should we read it...?",
"ウィンは頷いた！": "Win nodded!",
"ここでなら休んでいくことが出来る。": "You can rest here.",
"休んでいこうか…。": "Should we rest...?",
"ああ。": "Yeah.",
"引き出しをこっそり開けてみると…": "When we quietly opened the drawer...",
"ウィンは頷いた": "Win nodded",
"…仕事か？": "...More work?",
"扉が打ちつけられていて開けられない":
    "The door is nailed shut and won't open.",
"バンデッド": "Bandit",
"…それなら安心だ。": "...Then I'm relieved.",
"ピピンと一緒なら、ウィンも色々勉強に\nなるだろう。ピピン、ウィンをよろしくな。":
    "With Pipin alongside you, Win will learn a great deal.\nPipin, take good care of Win.",
"なんでだ！仕事だろう！？": "Why!? It's a mission, right!?",
"まさかウイン、": "Don't tell me, Win,",
"お前、陛下の話を聞いてなかったのか！？":
    "you weren't listening to His Majesty!?",
"俺も聞いていた、仕事だよな？ウィン。":
    "I heard it too. It's a mission, right, Win?",
"知っていて聞いた俺が悪かったよ。":
    "Fine, my bad for asking when I already knew.",
"…しかしピピンは怒り過ぎだ。うるさい。":
    "...But Pipin's overreacting. So loud.",
"…クッ": "...Ugh",
"どうして俺が怒られたんだ…": "Why did I get scolded...",
"人食いの獣が住み着いたっていう、\n西の監視塔か。":
    "The West Watchtower, where a man-eating beast is said to have moved in, huh.",
"ピピンも一緒なんだな？": "Pipin's coming along, right?",
"ここから先は、ウィンダム王とお妃さまの\n寝室だぜ　…って、":
    "Past here are the bedchambers of King Windam and his queen... hey,",
"お前そんなこと知ってるだろ。あっち行った。":
    "you already know that. Let's go.",
"…と、表紙に書かれた本がある。読んでみようか。":
    "There's a book with these words on the cover. Should we read it?",
"よう、ウィン。最近どうだ？": "Yo, Win. How's it going?",
"闇のエレメントの復活…": "The revival of the Dark Element...",
"クッーン！ッっクーン！": "Yip! Yip!",
"しかし変な鳴き声の犬だぜ…": "What a weird bark for a dog...",
"どこの自称天才さんの話だ？おい？":
    "Who's this self-proclaimed genius, huh?",
"げっ！いたのかピピン！！": "Gah! Pipin, you're here!!",
"ま、とりあえず、ウィン！がんばれよ！":
    "Well, anyway, Win! Do your best!",
"…ピピンもな。": "...You too, Pipin.",
"なんだなんだ、騎士学校トップで卒業した\nお前が、そんなパッとしない顔して。":
    "What's this? You graduated top of the knight academy, and you're wearing such a dull face.",
"最近実家のパン食べてないのか？":
    "Haven't been eating your folks' bread lately?",
"そりゃあよかった！俺はお前ならきっと\n騎士団長になると思ってるんだ。":
    "Glad to hear it! I'm sure you'll become Knight Commander one day.",
"あんな性格の悪い自称天才でなく…":
    "Not some mean-spirited self-proclaimed genius like that guy...",
"それよりも…　最上階から物音がする。":
    "Anyway... there's a noise from the top floor.",
"誰かいるかも知れない。調査するぞ。":
    "Someone might be there. Let's investigate.",
"あれ、ウィンじゃないか。": "Oh, if it isn't Win.",
"どうしたんだ？ここは通行手形がないと\n騎士でも通ることはできないぞ。":
    "What brings you here? Without a permit, even knights can't pass this way.",
"おっと失礼、よかったら少し品を見て下さい！":
    "Oh, pardon me! Have a look at my wares!",
"じいやなんか　なさけないと言って泣いた":
    "Grandpa cried, saying I was pathetic",
"オレが、いつまでたっても本を読まないから":
    "Because I never read any books, no matter how much time passed",
"あにきが本を読みまくってすげえあたまいいのは\nオレだってわかってる":
    "I know big bro reads tons of books and is super smart",
"だけどなんかよめないんだよオレは":
    "But somehow I just can't read them",
"みんなオレをアニキとくらべてダメなやつだって言う":
    "Everyone says I'm a hopeless loser compared to big bro",
"アニキをみならえって言う": "They tell me to be more like big bro",
"だけどアニキだけはそんなこと言わないし":
    "But big bro is the only one who never says that",
"『くっそーーー！！！！』": '"Daaamn!!!!"',
"アニキだけはオレに本をよまなくてもいいって言う":
    "Big bro is the only one who says I don't have to read",
"だけどアニキちがうんだよ": "But big bro, you're wrong",
"オレだって本を読みたいんだよ": "I want to read books too",
"アニキみたいになりたいんだ": "I want to be like you, big bro",
"くっそーーーーーーーーーーー": "Daaaaamn————",
"オヤジにめちゃくちゃどなられた": "Dad yelled at me like crazy",
"だいじんにもせっきょうされた": "Even the minister lectured me",
"ポケットに入っていたカラカラに乾いたパンを差し出して\nみると…物乞い、いや、彼は、僕に頭をさげてありがとう、\n乾いたパンひとつで殺人者が刹那に善人になったのだ。":
    "When I offered him the bone-dry bread from my pocket... the beggar — no, he bowed his head and thanked me. With a single piece of dry bread, a murderer became a good man in an instant.",
"乾いたパン一つにその力があるのに、僕らが毎日食べている":
    "If one dry piece of bread holds that much power, then the meals we eat every day—",
"『日記　というよりも覚書のようなもの』":
    '"A Diary — or Rather, Some Scraps of Notes"',
"昨日の朝、散歩をしていたら突然物乞いに襲われた。":
    "Yesterday morning, while out for a walk, I was suddenly attacked by a beggar.",
"恐怖を必死で抑えながら語りかけたが全く要領を得ない。":
    "I spoke to him while desperately suppressing my fear, but he made no sense at all.",
"…ホノオ。": "...Hono.",
"ウィンはうなずいた！": "Win nodded!",
"ふたりとも、気を引き締めていくのだ！！":
    "Both of you, stay sharp!!",
"この任務を良い機会とし、ピピンから多くを\n学ぶのだ。よいな…　下がれ。":
    "Use this mission as a good opportunity to learn much from Pipin.\nUnderstood... You're dismissed.",
"そうか…。": "I see...",
"なら、なんでそんな難しい顔をしてるんだ？":
    "Then why the long face?",
"なあ、もしつらいことがあったら、\nひとりで抱え込むんじゃないぞ…？":
    "Hey, if something's weighing on you, don't shoulder it alone, alright...?",
"…また仕事か？": "...Work again?",
"どんな仕事かはあえて聞かないさ。":
    "I won't bother asking what it is.",
"しかし、ウィン、お前なんだか顔つきが\n変わったな…。":
    "But Win, your expression seems different somehow...",
"すまん、冗談さ、ウィン。": "Sorry, just kidding, Win.",
"止めてくれよ。お前なら、きっと出来るさ。":
    "Come on. You've got this, I'm sure.",
"これはこれは次期騎士団長どの…":
    "Well, well, if it isn't the future Knight Commander...",
"紋章の継承おめでとうございます":
    "Congratulations on inheriting the crest",
"浮かれている場合か、若造。": "This is no time to be giddy, boy.",
"…がんばれよ。": "...Do your best.",
"野盗が増えとると兵たちは一年中言うとるが、\n別にいまはじまったことじゃない、昔から\n一定数おるんじゃ。":
    "The soldiers talk all year about how the bandits are increasing, but it's nothing new — there's always been a steady number of them.",
"え…？": "Huh...?",
"そう…": "I see...",
"ダフィールはぐったりと倒れて動かない":
    "Dafill lies limp on the ground, unmoving.",
"「だ、誰だ…！？": '"Wh-Who are you...!?"',
"ウィンは先にフレイム王に会おうと思った":
    "Win decided to see King Flame first.",
"何かのメモ…": "A note of some kind...",
"ピピンへの苦情の手紙やメモがたくさん置いてある…":
    "A pile of complaint letters and notes about Pipin...",
"ピピンに嫌みを言われて傷付いた…":
    "Pipin said something nasty and hurt me...",
"ピピンが俺の剣術をバカにした…":
    "Pipin mocked my swordsmanship...",
"ピピンが俺の喋り方をバカにした…":
    "Pipin mocked the way I talk...",
"ピピンが小鳥に話し掛けていた…":
    "Pipin was talking to a little bird...",
"読んでみようか…。": "Should we read it...?",
"…は": "...Yes",
"ウィンよ、ピピンをよろしく頼む。": "Win, I entrust Pipin to you.",
"急ぎ、西の森に住むロイを訪ね、事の次第を\n伝え、城に出てくるよう説得するのだ。":
    "Hurry to the western forest, visit Roi who lives there, tell him what's happened, and persuade him to come to the castle.",
"ご存知なのですか？": "You know of him?",
"だから…": "That's why...",
"…いいだろう。": "...Very well.",
"…ックーン！": "...Yip!",
"よしよし、ちゃんとメシもらってるみたいだな！":
    "There, there, looks like you're being fed well!",
"左　ホノオ王子の部屋　右　ホムラ王子の部屋":
    "Left: Prince Hono's room  Right: Prince Homura's room",
"てめえウィン…俺がちょっと目を離したスキに\nなに勝手に読んでんだよーーー":
    "You little—! Win... while I wasn't looking, what are you reading on your own!?",
"おまえなにだまってんだよ…": "What are you not saying...?",
"なに黙ってんだよーーーーーー！！":
    "Why aren't you saying anything!?",
"食事はその一食で、あの乾いたパン何個分だろうか…。":
    "That one meal was worth how many of those dry pieces of bread, I wonder...",
"やっぱ兄貴はすげえ…　何がすげえのかは\nよく分からねえんだが…やっぱ兄貴はすげえ。":
    "Big bro really is amazing... I can't quite say what's so amazing... but big bro really is amazing.",
"何かこう、胸にズシンと来るんだ…":
    "Something just hits me right in the chest...",
"本来次期国王は、紋章を継承したあとにすぐ\n南の遺跡へひとりで赴き、試練を果たさねば\nならん…":
    "Normally, the next king must journey alone to the Southern Ruins right after inheriting the crest and complete the trial...",
"しかし最近南の遺跡に魔物が増えたのと、\n何より王子が死んでしまうのを恐れて、\n王は今回の試練を見送るつもりだったのだ…":
    "But with monsters increasing in the Southern Ruins lately, and above all fearing the prince might die, the king intended to skip the trial this time...",
"うおおおおおおおおおおお！": "Woooooaaaaah!",
"ヒソヒソ…": "(whisper whisper)...",
"狩場に魔物が出まくってて、しばらく\nここは通行止めにさせてもらってる。":
    "Monsters are swarming the hunting grounds, so this way's closed to traffic for a while.",
"ああ、迷い込んだみたいだね。":
    "Yeah, looks like they wandered in.",
"ここはただの採石場だ。何もないよ。":
    "This is just a quarry. Nothing here.",
"お茶を飲んで、みんなのＨＰが回復した！":
    "Everyone drank tea and recovered HP!",
"まだ村まで結構遠いし、魔物も出るから\n気を付けてねー":
    "The village is still pretty far, and monsters appear, so be careful now~",
"こうやってまた、たまには顔見せに来てよね、\nナガレ。":
    "Come show your face once in a while, okay, Nagare?",
"うん、ありがとう！": "Yeah, thank you!",
"必要なものがあったら買って行け。":
    "If you need anything, buy it before you go.",
"ホノオ；": "Hono:",
"おい、なんでこんなに明るいんだ。":
    "Hey, why is it so bright in here?",
"真っ暗闇って話だったはずだが…。":
    "I thought this place was supposed to be pitch black...",
"ああ、それならオレとウィンの紋章を\n光らせてるからだ。":
    "Oh, that's because my crest and Win's are shining.",
"…そうなのか？": "...Is that so?",
"あ、そう…　べ、便利だな…": "O-Oh... H-Handy, huh...",
"…ああ。": "...Yeah.",
"よっしゃー！": "Alright!",
"じゃあいくかーーーー！": "Then let's go—!",
"いいから！　早くバトルしろ！！":
    "Just hurry up and fight!!",
"ヒールポーションを手に入れた！": "Obtained a Heal Potion!",
"「この際なにが出てきても驚かん…":
    '"At this point, nothing could surprise me..."',
"…街には入らない方がいい、ウィン…":
    "...Better not go into town, Win...",
"あのとき、燃え盛る岩がたくさん降ってきて…":
    "Back then, burning rocks rained down in droves...",
"この街はがれきの山になってしまったんだ。":
    "This town was reduced to a mountain of rubble.",
"フン…！": "Hmph...!",
"任務に取り掛かる前に、支給品を受け取るのを\n忘れるなよ。":
    "Before you start your mission, don't forget to pick up your provisions.",
"どこで受け取れるかって？": "Where? You ask?",
"お前本当にここの騎士か！？":
    "Are you really a knight of this castle!?",
"…そこ曲がった先の、とっちらかった部屋だ。":
    "...It's the messy room past that corner.",
"…と、表紙に書かれた本がある。読んでみようか？":
    "There's a book with these words on the cover. Should we read it?",
"ウィンさん、魔物をたおしたときにたまに\n手に入る、魔物の素材とか財宝…":
    "Win, sometimes when you defeat monsters, you get monster materials or treasure...",
"随分と焦ってるようだが、それも当然だな。":
    "You look quite flustered, and rightly so.",
"西の監視塔なら、毎月サクソン団長代行が\n見回りを命じられているはずだからな。":
    "As for the West Watchtower, Acting Commander Saxon should be ordered to patrol it every month.",
"ええい、ピピンめ、無礼なあああああ！！":
    "Bah! Pipin, you insolent—!",
"確かに前回の見回りでは異常なかっ��のだ！":
    "It's true that nothing was abnormal during the last patrol!",
"わしは忙しいのだウィン！邪魔を…":
    "I'm a busy man, Win! Don't bother—",
"魔物どころか、ねずみ一匹さえ、クモ一匹さえ\nいなかったのだ！！":
    "Not a single monster — not even one mouse, not even one spider!!",
"どうだかね…。": "Who can say...",
"しつこいぞ、ピピン！し、しかし…":
    "Persistent, aren't you, Pipin! B-But...",
"もしかすれば、闇のエレメントの復活が\n近いのかも知れぬ…":
    "Perhaps the revival of the Dark Element is near...",
"ん？西の監視塔に人食いの魔物が出たから\n調査に行く、だと…？":
    "Hm? You're going to investigate the West Watchtower because a man-eating monster appeared there...?",
"そ、それは大変だのう！": "T-That is serious indeed!",
"気を付けて行ってまいれよ！": "Do go carefully!",
"…サクソンめ、なにが闇のエレメントだ。":
    "...That Saxon, what's this about a Dark Element.",
"自分の能無しを、おとぎ話で誤魔化すなんて、\n恥知らずにもほどがある。":
    "Covering up his own incompetence with fairy tales — the shamelessness knows no bounds.",
"『ウィンダム王国の歴史』": '"History of the Windam Kingdom"',
"南の国のフレイムや、西の山奥のセイリューでは、\n辺境の田舎に、いつのまにか大きな城が建っていて\n王国が出来ていたので驚いたと伝わっている。":
    "In the southern land of Flame and in Seiryu, deep in the western mountains, it's said that great castles suddenly rose in remote countryside, and kingdoms were born before anyone could be surprised.",
"そういう噂が、ウィンダム王国以外でもそれなりに\n信じられている。":
    "Such rumors are believed to a fair degree outside the Windam Kingdom as well.",
"とにかくこの国では何でも風のエレメントのおかげである。":
    "In any case, in this country, everything is thanks to the Wind Element.",
"…と表紙に書かれた本がある。読んでみようか…・":
    "There's a book with these words on the cover. Should we read it...?",
"大昔からある国だと伝わるが、実際にどのくらい大昔から\nあるのかは、あまりよく分からない。":
    "The kingdom is said to have existed since ancient times, though how ancient exactly isn't well known.",
"色々な本や言い伝えから、500年くらい前には、\n国王がいて、兵士がいて、街があったらしい。":
    "From various books and legends, it seems that around 500 years ago there was a king, soldiers, and a town here.",
"『サクソンの日記』": '"Saxon\'s Diary"',
"領内を荒らし回っていた野盗の集団を、遂に追い詰めた。":
    "At last, I cornered the bandit gang that had been ravaging the territory.",
"この戦いで大手柄を挙げることで、あのロイを差し置いて\nわしが騎士団長になれないものか…。ううむ。":
    "If I distinguish myself in this battle, perhaps I can become Knight Commander, ahead of that Roi... Hmm.",
"もうずっとわしが騎士団長代行のままだ。":
    "I've been Acting Knight Commander all this time.",
"実質的にはわしが騎士団を率いているとはいえ…":
    "Even if in practice I lead the knight order...",
"紋章のないわしにいざとなった時に国を守れるだろうか…":
    "Without a crest, can I really protect the country in a crisis...?",
"…と、表紙に書かれた本がある。読んでみようか…":
    "There's a book with these words on the cover. Should we read it...",
"代々何度も騎士団長、そして風の紋章を受け継いできた\n我が一族…。わしもその栄誉が欲しかったのに、あのロイ\nとかいう男がいるせいで…。悔しい。":
    "My family has inherited the position of Knight Commander and the Wind Crest for generations... I too wanted that honor, but because of that man Roi... How frustrating.",
"…はい。": "...Yes.",
"騎士ウィン、お前にはまだ実戦経験が少ない。":
    "Knight Win, you still lack real combat experience.",
"しかし…": "However...",
"は…？": "Huh...?",
"俺はてっきりケンカでもしたのかと。":
    "I figured you two had gotten into a fight.",
"よう、ウィン。あれ、ピピンは…":
    "Yo, Win. Huh, where's Pipin...",
"うんてウィン…": "Umm, Win...",
"なんだお前ら、ケンカしたかー？":
    "What's this, you two fighting?",
"ちがうってなんだよ…": "It's not what you think...",
"おい！手を隠すなって！": "Hey! Don't hide your hand!",
"ウィン、聞いたぞ！": "Win, I heard!",
"おまえ…　紋章を継承したって…！":
    "You... inherited the crest...!",
"てことはお前…将来の騎士団長じゃねえか…":
    "That means you... you're gonna be Knight Commander someday...",
"出世早すぎるだろ！すげえな！":
    "Talk about a fast promotion! Amazing!",
"またのご利用をお待ちしております。":
    "We look forward to your next visit.",
"ありがとうございます！": "Thank you!",
"本当にありがとうございました。": "Thank you so much.",
"おい、ウィン！勝手に読まないでくれよ！":
    "Hey, Win! Don't go reading on your own!",
"ウィンよ。直ちにお前が継承者になった事を\nウィンダム王に報告し、そののち、\n急いでフレイム王国とセイリューに向かえ。":
    "Win. Report your succession to King Windam at once, and afterwards hurry to the Flame Kingdom and to Seiryu.",
"闇のエレメントに対抗するには、\n火、水、風、全ての紋章の力が必要なのだ。":
    "To stand against the Dark Element, the power of all the crests — fire, water, and wind — is needed.",
"頼んだぞ、ウィン。": "I'm counting on you, Win.",
"…くっ！": "...Guh!",
"ウィン…": "Win...",
"…犬の声？": "...A dog's bark?",
"どこにいるんだ？　　　うわっ！": "Where is it?    Whoa!",
"なんちゅう荒れっぷりだ…": "What a disaster zone...",
"…なんだいまの化け物は…": "...What was that monster...",
"放置してから数カ月どころじゃないぞ、これは":
    "This place has been abandoned for way more than a few months.",
"おい、お前、本気で言っているのか？":
    "Hey, are you serious?",
"自分の力の程度も把握できていないとはな…。":
    "You don't even know your own strength...",
"先が思いやられる奴だぜ…。": "What a worrying guy...",
"しかし…　": "However...",
"私はしばらくここで足止めですから…":
    "I'll be stuck here for a while...",
"もし品を気に入ったら、また来てくださいね！":
    "If you like anything, please come again!",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "dialogue.tsv"))


def norm(s):
    return s.strip(" \u3000")


def main():
    if not os.path.exists(PATH):
        # create from the master for future batches
        import csv as _csv
        with open(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                                "docs", "text", "translated.tsv")),
                  encoding="utf-8") as fh:
            master = list(_csv.DictReader(fh, delimiter="\t"))
        rows = [{"id": r["id"], "japanese": r["japanese"]}
                for r in master
                if r["type"] == "dialogue"
                and not (r.get("translation") or "").strip()]
        with open(PATH, "w", encoding="utf-8", newline="") as fh:
            w = _csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                                delimiter="\t")
            w.writeheader()
            w.writerows(rows)
    with open(PATH, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    keyed = {norm(k): v for k, v in D.items()}
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
    print("dialogue.tsv filled", filled, "/", len(rows))


if __name__ == "__main__":
    main()
