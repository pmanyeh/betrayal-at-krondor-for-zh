# DIAL_Z00

481 records, 284 keyed nodes

## node 332  (DIAL_Z00#0)
- speaker=0  style=0
- effects:
    - frame/rect style override x=60 y=35 w=200 h=55
- text: 左鍵點擊以儲存書籤檔。  右鍵點擊以取消。

## node 333  (DIAL_Z00#1)
- speaker=0  style=0
- effects:
    - frame/rect style override x=60 y=35 w=200 h=55
- text: 已取消書籤。

## node 334  (DIAL_Z00#2)
- speaker=0  style=0
- effects:
    - frame/rect style override x=60 y=35 w=200 h=55
- text: 正在儲存書籤……

## node 327  (DIAL_Z00#3)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [2467..0]] -> node 0 (no jump)
    - [flag 0x7530 in [2673..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 318  (DIAL_Z00#7)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 那些人朝他們衝了過來。  雖然他不確定那些收費者一旦被硬闖過關卡會做出什麼反應，但@4沒料到他們的反擊會如此猛烈……

## node 310  (DIAL_Z00#8)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - apply status/condition to party idx=1 amt=75
- text: 那些人朝他們衝了過來。  他們從衣袍裡掏出奇怪的小包，朝@5和@3扔出一團團惡臭的物質。@5起初一頭霧水，仔細一看才明白怎麼回事。  「這是奎格人的戰術！」@4大喊。「他們扔的是帶病的腐土！我們得撂倒他們！」

## node 313  (DIAL_Z00#9)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 空氣起了漣漪。  彷彿眼前世界不過是一張被猛地扯開的簾幕，四個身影憑空浮現在他們眼前，全是全副武裝的莫瑞德人。其中一名刺客，衣著比左右兩側的同伴更為精緻，齜牙咧嘴地開口。「óGorath, ólwychan óchoi ónekkad ósedu óDelekhan! Baka'al eledhel!」  「戈拉斯？」@4疑惑地瞥了一眼同伴，只見那莫瑞德人拔出了自己的武器，漆黑的目光緊盯著眼前排開的同族。  「準備應戰，」戈拉斯冷冷地啞聲道。「這可不是普通的荒野游兵，而是一名...

## node 308  (DIAL_Z00#10)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 納馮扯開了外袍。  底下露出死亡公會的熟悉制服，黑色戰袍上繡著一隻金鷹。「我平常不會穿得這麼厚重，」他咧嘴一笑，拔出武器。「但你們打斷了我原本要辦的一件事……」

## node 314  (DIAL_Z00#11)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [5046..0]] -> node 0 (no jump)
    - [flag 0x7530 in [5291..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 320  (DIAL_Z00#15)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @0驚恐地大喊。  「天啊！他們憑空冒出來的！」他指著眼前逐漸成形的身影說道。「拿起武器！我們遭到襲擊了！」

## node 321  (DIAL_Z00#16)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 前方有麻煩了。  莫瑞德戰士察覺了他們的存在，準備發動攻擊，戈拉斯朝歐文喊道：「除非我們能想辦法改變外貌，否則這座城鎮會要了我們的命。」  歐文面色凝重地點頭，準備好隨時應戰或逃命……

## node 335  (DIAL_Z00#17)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4用力嚥了口口水。  心臟在胸口狂跳，他望著敵人一步步逼近。他強忍著轉身逃跑的衝動，逼自己保持鎮定，逼自己不露出恐懼——儘管幾乎要被排山倒海的驚慌淹沒。

## node 20  (DIAL_Z00#18)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [6758..0]] -> node 0 (no jump)
    - [flag 0x7530 in [7359..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#19
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#20
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1驚訝地大喊。  衝上前去的同時，@4試著判斷對手接下來會有什麼舉動、該如何應對每一種可能。雖然出其不意占了上風，但這場戰鬥的結果還遠遠未定。

### (sub) DIAL_Z00#21
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1驚訝地轉過身來。  看樣子他完全被殺了個措手不及。就算他ñ早料到會遭到攻擊，也絕對沒想到對方會如此全副武裝、身手了得；儘管如此，他仍保持戒備，@4知道這一戰絕不會輕鬆。

### (sub) DIAL_Z00#22
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1咧嘴一笑。  側身避開突襲、試圖搶占高處，他朝@4搖了搖手指，語帶嘲弄，雙眼閃著嗜血的期待。  「好啊，」@4邊說邊擺出戰鬥架勢，「那就用硬碰硬的方式解決。」

### (sub) DIAL_Z00#23
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那名刺客是個傭兵。  @4從@1那張冷硬的臉看得出來，他追殺他們並非為了報復什麼舊怨，也不是為了討債。他來，只因為酬金的顏色與數目都對了。  為了這筆錢，無論勝負，他都會拼死一戰……

## node 21  (DIAL_Z00#24)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [8013..0]] -> node 0 (no jump)
    - [flag 0x7530 in [8521..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#25
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#26
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4衝了上去。  對手猝不及防，一陣手忙腳亂後才終於擺出防禦架勢。@4趁著這稍縱即逝的優勢，迅速下達幾道指令，準備投入戰鬥。

### (sub) DIAL_Z00#27
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 這次攻擊完全出乎意料。  敵人瞪大雙眼，手忙腳亂。@4不想浪費這稍縱即逝的優勢，迅速下達幾道指令，戰鬥就此展開。

### (sub) DIAL_Z00#28
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#29
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人並未感到意外。  事實上，他們似乎迫不及待接受挑戰，迎向這次落空的突襲。  「武器準備好！」@4大喊。「看來這一仗得照ñ他們的規矩打了。」

### (sub) DIAL_Z00#30
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人早已等在那裡。  「他們看見我們了！」@4大喊。他將注意力分成兩處：一是自己的雙腳，確保站姿與平衡；二是對手，思忖著他們怎麼會沒被嚇到。  這些念頭轉眼被拋到腦後，敵人已經衝入了他們的陣中。

### (sub) DIAL_Z00#31
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#32
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4努力理清思緒。  敵人步步逼近，他的注意力分成兩處：一是自己的雙腳，確保站姿與平衡；二是對手，思忖著他們怎麼能這麼快追上來。  這些念頭很快被拋到腦後，敵人已經衝入了他們的陣中。

### (sub) DIAL_Z00#33
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4用力嚥了口口水。  心臟在胸口狂跳，他望著敵人一步步逼近。他強忍著轉身逃跑的衝動，逼自己保持鎮定，逼自己不露出恐懼——儘管幾乎要被排山倒海的驚慌淹沒。

## node 324  (DIAL_Z00#34)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [9840..0]] -> node 0 (no jump)
    - [flag 0x7530 in [10274..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#35
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#39
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 22  (DIAL_Z00#42)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [11249..0]] -> node 0 (no jump)
    - [flag 0x7530 in [11462..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#43
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 受驚的@1轉身面對他們。  見到那生物眼中閃過的凶光，@4皺起眉頭，但他不願浪費這稍縱即逝的優勢，隨即衝上前去，準備應戰。

### (sub) DIAL_Z00#44
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1轉身面對他們。  顯然這次攻擊早在對方預料之中，@4大聲咒罵，一邊盤算著是該繼續衝鋒還是先撤退重整。無論如何，他知道這一戰是躲不掉了。

### (sub) DIAL_Z00#45
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1的嘴角滴著唾涎。  「我以前養的狗也會這樣流口水，」@4調侃道。接著語氣一沉：「不過那通常表示牠餓了，聞到了想ñ吃ð的東西……」

## node 23  (DIAL_Z00#46)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [12008..0]] -> node 0 (no jump)
    - [flag 0x7530 in [12262..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#47
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那些生物發出嚎叫。  猝不及防的突襲讓牠們憤怒地掙扎亂動，@4的胃揪成一團。儘管身經百戰，他始終無法擺脫那股彷彿即將喪命的詭異預感……

### (sub) DIAL_Z00#48
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 優勢已經失去。  @4舉手示意眾人停下，一邊思索新的對策，胃裡揪成一團。儘管身經百戰，他始終無法擺脫那股彷彿即將喪命的詭異預感……

### (sub) DIAL_Z00#49
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4聽見一陣聲響。  知道即將遭到攻擊，他站穩腳步等待著，胃裡揪成一團。儘管身經百戰，他始終無法擺脫那股彷彿即將喪命的詭異預感……

## node 24  (DIAL_Z00#50)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [12850..0]] -> node 0 (no jump)
    - [flag 0x7530 in [13082..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#51
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 對方沒料到他們會出現。  見對手似乎只有一人，且被他們的接近打了個措手不及，@4欣然喊道：「我們能通過嗎？」  @1的回應是慌忙摸索武器。

### (sub) DIAL_Z00#52
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1早已等在那裡。  「沒人能偷襲得了我，」他邊喊邊靈活地欺身而上。「應戰，否則就受死！」

### (sub) DIAL_Z00#53
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 眼前的@1根本聽不進道理。  「應戰！」他邊喊邊靈活地欺身而上。「應戰，否則就受死！」

## node 25  (DIAL_Z00#54)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [13395..0]] -> node 0 (no jump)
    - [flag 0x7530 in [13631..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 26  (DIAL_Z00#58)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [14326..0]] -> node 0 (no jump)
    - [flag 0x7530 in [14632..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 217  (DIAL_Z00#62)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [15283..0]] -> node 0 (no jump)
    - [flag 0x7530 in [15592..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#63
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他們殺了@1一個措手不及。  衝上前去的同時，@3拼命回想自己那點少得可憐的神殿法術知識，懊悔當初沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，他們已逼近那張灰白面孔的生物。

### (sub) DIAL_Z00#64
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股寒意竄過@3的脊背。  @1並未因這次攻擊而感到意外，此刻他正拼命回想自己那點少得可憐的神殿法術知識，懊悔當初沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，那張灰白面孔的生物已來到他們之中，用早已失去生氣的雙眼斜睨著他們……

### (sub) DIAL_Z00#65
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股寒意竄過@3的脊背。  眼見一隻@1朝他們逼近，他拼命回想自己那點少得可憐的神殿法術知識，懊悔當初沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，那張灰白面孔的生物已來到他們之中，用早已失去生氣的雙眼打量著他們……

## node 218  (DIAL_Z00#66)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [16400..0]] -> node 0 (no jump)
    - [flag 0x7530 in [16712..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#67
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他們殺了對手一個措手不及。  衝上前去的同時，@3拼命回想自己那點少得可憐的神殿法術知識，懊悔當初沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，他們已逼近那些灰白面孔的生物。

### (sub) DIAL_Z00#68
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股寒意竄過@3的脊背。  敵人早已等著他們來襲，此刻他正拼命回想自己那點少得可憐的神殿法術知識，懊悔沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，灰白面孔的生物已來到他們之中，用早已失去生氣的雙眼斜睨著他們……

### (sub) DIAL_Z00#69
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股寒意竄過@3的脊背。  眼見敵人步步逼近，他拼命回想自己那點少得可憐的神殿法術知識，懊悔沒多花時間研讀關於米德凱米亞死神林絲克拉格瑪的典籍。  不消幾秒，灰白面孔的生物已來到他們之中，用早已失去生氣的雙眼打量著他們……

## node 219  (DIAL_Z00#70)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [17524..0]] -> node 0 (no jump)
    - [flag 0x7530 in [18250..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#71
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#72
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他們悄悄向前移動。  越走越近，@4認出眼前的身影分明是個女子，帶著一種令人隱隱不安的媚態。  「你嚇到我了，」她開口喊道，豐潤的雙唇勾起一抹笑意。「或許我不殺你，讓露西亞女神拿你來取樂。」  @4這才驚覺他們面對的是露西亞女神的信徒——那位時而仁慈、卻常常反覆無常又殘酷的女神。

### (sub) DIAL_Z00#73
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1還沒準備好。  慶幸沒被發現，@4趁勢逼近，同時提高警覺留意是否還有其他攻擊者。確認對方只有一人後，他們便擺出了戰鬥姿態。

### (sub) DIAL_Z00#74
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#75
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那人朝他們撲了過來。  顯然這次突襲失敗了。那人像瘋子般把劍舞得虎虎生風，大喊：「應戰！應戰，否則就受死！」

### (sub) DIAL_Z00#76
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那人看見他們走近。  他腳步輕盈得驚人，對著空氣連續揮劍，然後喊道：「練練手，這條路上最近搶劫案不少，想確保自己有備無患。」  @4點了點頭。「聽起來挺明智。是誰在鬧事？」  那人反手一轉，把武器指向@4。「我！」

### (sub) DIAL_Z00#77
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#78
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那人朝他們微笑。  他腳步輕盈得驚人，對著空氣連續揮劍，然後喊道：「練練手，這條路上最近搶劫案不少……想確保自己手感還在。」  @4點了點頭。「聽起來挺明智。是誰在鬧事？」  那人反手一轉，把武器指向@4。「我！」

### (sub) DIAL_Z00#79
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4察覺到不對勁。  一個面露呆滯的傢伙搖搖晃晃地走來，那副醉醺醺的步伐顯然是喝多了凱許麥酒或奎格白蘭地。醉漢半瞇著眼抬頭盯著@4，接著伸手去拔劍。「你！是ñ你ð！當初把我扔在凱許那個鬼地方等死，是不是？！現在我要討回這筆帳，你這頭蠢豬！」

### (sub) DIAL_Z00#80
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一名男子走近。  「我是來跟你談談的，」他開口道。「有人出錢打聽你們的下落。要是你們出得起更高的價錢，或許我能被說服ñ忘了曾見過你們。」  「散播謠言的傢伙！」@4怒氣沖沖地逼近那人。「你都跟他們說了什麼？」  「我還沒說多少……我是說ñ還沒ð，」那人尖叫道，這才驚覺自己的貪念已蓋過了理智。他狗急跳牆，拔出了劍……

## node 220  (DIAL_Z00#81)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [20173..0]] -> node 0 (no jump)
    - [flag 0x7530 in [20690..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#82
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#83
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 對手大吃一驚。  這群烏合之眾的首領對同伴聲嘶力竭地下令，語氣中夾雜著恐懼與憤怒。@4抓住先發制人的機會，迅速下達幾道指令，戰鬥就此展開。

### (sub) DIAL_Z00#84
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 不知是誰或什麼東西發出了警告的尖叫。  等聲音傳到同伴耳中時，@4早已看清局勢，擺好架勢準備先發制人。不消幾秒，戰鬥就此展開。

### (sub) DIAL_Z00#85
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#86
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人並未感到意外。  「我不記得允許過你們來這裡。」一個牛脖子般粗壯的大漢朝他們逼近，雙拳緊握。「轉身滾開。」  「我們不想惹麻煩，只是路過而已，」@4回答。  話音剛落，那人隨即轉身打了個響指，片刻後戰鬥就此展開。

### (sub) DIAL_Z00#87
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一群人蹣跚朝他們走來。  這是ñ紅顎獵神ð圭斯瓦神的信徒，隊伍雜亂無章地移動著，空洞的雙眼下方，眼窩塗著血色的漩渦紋樣。  一個高大的身影張開三指的手掌——那是祭司階級特有的儀式性殘缺——啞聲道：「今日，圭斯瓦神欽定你們將成為他的獵物……」

### (sub) DIAL_Z00#88
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#89
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人注視著他們走近。  「站住，」一個鷹隼面孔的男子說道，舉起紋著黃色螺旋圖案的手掌。「脫下衣物、交出財物，我們就此互不相干。」  @4摸了摸下巴。「非得動手不可嗎？應該還有別的辦法吧。」  「沒有，」首領咕噥道。「恐怕沒有了……」

### (sub) DIAL_Z00#90
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4微微一笑。  兩名男子手持武器面對面站著，滿是鬍碴的臉漲得通紅，互相大聲辱罵。  「你們現在收手還來得及，這種場面我見多了，」@4說，「我可不會插手救你們哪一個的命，也不會把我的錢袋交給你們任何一個。」  「那好，」其中一人冷笑道。「那就來硬的！」

### (sub) DIAL_Z00#91
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一群人蹣跚朝他們走來。  這是ñ紅顎獵神ð圭斯瓦神的信徒，隊伍雜亂無章地移動著，空洞的雙眼下方，眼窩塗著血色的漩渦紋樣。  一個高大的身影張開三指的手掌——那是祭司階級特有的儀式性殘缺——啞聲道：「今日，圭斯瓦神欽定你們將成為他的獵物……」

## node 248  (DIAL_Z00#92)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [22692..0]] -> node 0 (no jump)
    - [flag 0x7530 in [22885..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#93
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 突襲奇襲成功了！  毫無防備的@1慌忙摸索武器，@4則咬緊牙關，做好了應戰的準備。

### (sub) DIAL_Z00#94
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @0踉蹌了一下。  @4朝他投去不滿的一瞥，這時@1已拔出武器，準備迎戰這次落空的突襲。

### (sub) DIAL_Z00#95
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一名孤身的@1站在他們面前。  對手叉腰而立，看來對這次攻擊早有準備，讓@0不禁猜想附近是否還有援軍。無論如何，他判斷這名@1訓練有素，就算獨自一人也絕非易與之輩。

## node 249  (DIAL_Z00#96)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [23354..0]] -> node 0 (no jump)
    - [flag 0x7530 in [23622..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#97
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人向後一跳。  見敵人拼命應付這次攻擊，@4信心大增。從他們恢復鎮定的速度來看，他猜測對方訓練有素，絕非易與之輩。

### (sub) DIAL_Z00#98
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @0踉蹌了一下。  @4朝他投去不滿的一瞥，這時敵人已擺出防禦姿態，準備迎戰這次落空的突襲。

### (sub) DIAL_Z00#99
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他們並不是孤軍作戰。  對手看來對這次攻擊早有準備，讓@0不禁猜想附近是否還有援軍。無論如何，從他們的架勢判斷，這些人訓練有素。

## node 272  (DIAL_Z00#100)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [24054..0]] -> node 0 (no jump)
    - [flag 0x7530 in [24360..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#101
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1發出不悅的噴氣聲。  牠伸長橄欖色鱗片覆蓋的脖子，用蛇一般的眼睛迎向衝來的攻擊者。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。@4慶幸他們占了先機。

### (sub) DIAL_Z00#102
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1察覺了他們的接近。  牠伸長橄欖色鱗片覆蓋的脖子，用蛇一般的眼睛迎向衝來的攻擊者。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。@4懊悔沒能出其不意。

### (sub) DIAL_Z00#103
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股油膩的惡臭瀰漫在空氣中。  一隻@1氣喘吁吁地立在他們面前。牠伸長橄欖色鱗片覆蓋的脖子，用蛇一般的眼睛打量@4，接著把銳利的目光轉向@0。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。

## node 273  (DIAL_Z00#104)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [25023..0]] -> node 0 (no jump)
    - [flag 0x7530 in [25415..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#105
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 對方沒料到他們會出現。  慶幸出其不意站在自己這邊，多少能扳回這場實力懸殊的較量，@0擺出了攻擊姿態。  「我們得殺了他們，至少也得把他們趕跑，」@4低聲道。「現在要是掉頭，他們只會像逮老鼠一樣撲上來。」  @0苦笑一聲。「我看老鼠的勝算還比我們大……」

### (sub) DIAL_Z00#106
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人已經聞到了他們的氣味。  優勢已失，@4大喊：「我們得應戰了，現在要是掉頭，他們只會像逮老鼠一樣撲上來。」  @0苦笑一聲。「我看老鼠的勝算還比我們大……」

### (sub) DIAL_Z00#107
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人悄悄逼近。  「我們得應戰了，」@4說。「要是掉頭，他們只會像逮老鼠一樣撲上來。」  @0苦笑一聲。「我看老鼠的勝算還比我們大……」

## node 278  (DIAL_Z00#108)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [25940..0]] -> node 0 (no jump)
    - [flag 0x7530 in [26178..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 279  (DIAL_Z00#112)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [26764..0]] -> node 0 (no jump)
    - [flag 0x7530 in [27117..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 280  (DIAL_Z00#116)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [27950..0]] -> node 0 (no jump)
    - [flag 0x7530 in [28088..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 283  (DIAL_Z00#120)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [28702..0]] -> node 0 (no jump)
    - [flag 0x7530 in [28946..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 319  (DIAL_Z00#124)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [29465..0]] -> node 0 (no jump)
    - [flag 0x7530 in [29850..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 284  (DIAL_Z00#128)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [30727..0]] -> node 0 (no jump)
    - [flag 0x7530 in [30958..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#129
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人大喊出聲。  衝上前去的同時，歐文試著判斷敵人接下來會有什麼舉動、該如何應對每一種可能。雖然占了上風，但這場戰鬥的結果還遠遠未定。

### (sub) DIAL_Z00#130
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人早已等在那裡。  意識到優勢已失，歐文將注意力分成兩處：一是自己的雙腳，確保站姿與平衡；二是對手，思忖著他們怎麼會沒被嚇到。  他下定決心，做好了應戰的準備。

### (sub) DIAL_Z00#131
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 敵人站在他們面前。  歐文抓緊手邊唯一的防身武器，站穩腳步等待著，胃裡揪成一團。儘管身經百戰，他始終無法擺脫那股彷彿即將喪命的詭異預感……

## node 285  (DIAL_Z00#132)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [31589..0]] -> node 0 (no jump)
    - [flag 0x7530 in [31847..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#133
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1大喊出聲。  衝上前去的同時，歐文試著判斷她接下來會有什麼舉動、該如何應對每一種可能。雖然出其不意占了上風，但這場法術之戰的結果還遠遠未定。

### (sub) DIAL_Z00#134
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 這次衝鋒早在對方預料之中。  她從容不迫得彷彿在等待喝茶的客人，打量他們的眼神就像在挑選待買的豬隻，接著把手舉過頭頂。  「我不歡迎不速之客，」她冷冷地說。「看來得教教你們規矩了……」

### (sub) DIAL_Z00#135
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一名女巫站在他們面前。  歐文抓緊手邊唯一的防身武器，站穩腳步等待著，胃裡揪成一團。他祈禱她的法術不敵自己，但這個念頭並未帶來多少安慰，他緊握法杖，準備應戰。

## node 286  (DIAL_Z00#136)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [32504..0]] -> node 0 (no jump)
    - [flag 0x7530 in [32794..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#137
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1發出不悅的噴氣聲。  牠伸長橄欖色鱗片覆蓋的脖子，用蛇一般的眼睛迎向他們。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。歐文慶幸他們占了先機。

### (sub) DIAL_Z00#138
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1察覺了他的接近。  牠伸長橄欖色鱗片覆蓋的脖子，用蛇一般的眼睛迎向他們。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。歐文懊悔沒能出其不意。

### (sub) DIAL_Z00#139
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 一股油膩的惡臭瀰漫在空氣中。  一隻@1氣喘吁吁地立在他面前。牠伸長橄欖色鱗片覆蓋的脖子，把銳利的目光轉向他們。雖不及體型更大的龍族親戚那般可怕，單是一隻牛蜥就足以殺死體型兩倍於自己的生物。

## node 287  (DIAL_Z00#140)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [33401..0]] -> node 0 (no jump)
    - [flag 0x7530 in [33668..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#141
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那些@1大喊出聲。  衝上前去的同時，@4試著判斷對手接下來會有什麼舉動、該如何應對每一種可能。雖然出其不意占了上風，但這場戰鬥的結果還遠遠未定。

### (sub) DIAL_Z00#142
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 那些@1早已等在那裡。  意識到優勢已失，@4將注意力分成兩處：一是自己的雙腳，確保站姿與平衡；二是對手，思忖著他們怎麼會沒被嚇到。  這些念頭轉眼被拋到腦後，那些@1已拔出武器、擺出防禦姿態。

### (sub) DIAL_Z00#143
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他們被認出來了。  懊惱明明差一點就能瞞過守衛，戈拉斯警告歐文做好最壞的打算。「我被認出來了，」他大喊。「他們肯定接到命令要殺我們兩個！」

## node 288  (DIAL_Z00#144)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [34296..0]] -> node 0 (no jump)
    - [flag 0x7530 in [34650..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 328  (DIAL_Z00#148)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @3努力理清思緒。  他努力嚥下喉間突如其來的哽塞感，心臟狂跳不止，逼自己深呼吸、逼自己保持鎮定。敵人步步逼近，他強忍著腹中那股灼熱、令四肢發麻的疼痛。但憑著老練士兵的反應，他把恐懼拋到腦後，準備投入戰鬥。

## node 27  (DIAL_Z00#149)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 一顆小石子從崖壁滾落。  被這看似無緣無故的動靜弄糊塗了，@0抬頭望了一眼，又低頭看向地面。仔細一瞧，他才發現那顆「小石子」其實是一顆黯淡無光的黃銅鈕扣！  他還來不及喊出聲，伏擊者已從天而降……

## node 28  (DIAL_Z00#150)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 他們正被監視著。  不確定監視者的位置在哪，@4猛地轉身，正好看見一個身影從樹後現身！

## node 29  (DIAL_Z00#151)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 岸邊的水面平靜地拍打著。  一陣微風吹起，水面泛起漣漪，粼粼波光映照出水底的青蛙、魚群……以及某個龐然大物。ñ太ñ大ð了。  @0踉蹌著從水邊退開，水面驟然炸開，他大喊：「我們被埋伏了！」

## node 221  (DIAL_Z00#152)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4倒抽一口氣。  他強忍著心中湧起的恐懼，一股寒意竄過全身，如重錘般擊中胸口，逼出了肺裡的空氣。他正努力喘過氣時，猛然發現自己已遭到攻擊！

## node 241  (DIAL_Z00#153)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 四周一片寂靜。  事實上，靜得ñ有些過頭，這個念頭一浮現，一股寒意便竄遍了@4全身。他正要出聲示警，話還沒說出口，一隻碩大的@1已朝他們衝來。  「我們遭到攻擊了！」他尖叫道。

## node 242  (DIAL_Z00#154)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 他完全沒料到這一擊。  @4又氣又惱地低吼，一隻@1已衝入他們的陣中。  「我們被埋伏了！」他大喊。

## node 243  (DIAL_Z00#155)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @4根本沒機會敲門。  毫無預警，一隻@1從小屋另一側朝他們衝來，抱著不是你死就是我活的決心。  「小心！」@4尖叫著擺出戰鬥架勢。「有埋伏！」

## node 274  (DIAL_Z00#156)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 聽起來像是遠方的戰鼓聲。  @4停下腳步側耳傾聽，臉上滿是疑惑。他正要開口說起這詭異的聲響，一陣涼風忽然在他身邊捲起陣陣塵土。  他抬頭一看，驚恐地發現那聲響根本不是戰鼓，而是一對巨大翅膀的拍動聲！那生物落了地，擺出了戰鬥架勢……

## node 281  (DIAL_Z00#157)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: 有什麼東西滑行而過。  那是個陌生的聲響，@4並不熟悉，但他確實聽見了。他轉頭想找出聲音的來源，卻沒能成功。  正要轉身離開，卻猛然發現自己已與一隻@1正面相對。「有埋伏！」他喊道。

## node 289  (DIAL_Z00#158)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 屋內有什麼東西滑行而過。  「我不太喜歡ñ那個ð聲音，」@4說。「也許我們該——」話還沒說完，門已猛然被撞開。他猛然發現自己正與一隻蛇形生物對峙，那生物顯然打定主意要讓他們再也無法來煩牠。

## node 291  (DIAL_Z00#159)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 濃煙從地底滲出。  @0驚恐地從那座被褻瀆的墳墓邊後退，只見濃煙開始盤旋成一團帶著火花的漩渦……

## node 30  (DIAL_Z00#160)
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 31  (DIAL_Z00#164)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 眾人同時鬆了口氣。  「我想我們過關了，」@4說。「但還是提高警覺，可能還有其他陷阱。」

## node 107  (DIAL_Z00#165)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - SET flag 0x7540=2
- text: 鮮血從@4的唇邊湧出。  「敗了……」他吐出這句話，徒勞地抓撓著地面，生命一點一滴流逝。「竟輸給……一群……蠢東西。真蠢……真是……該死地蠢……」  幾天後，他們的屍體才被人發現。

## node 322  (DIAL_Z00#166)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 這場戰鬥贏了。  「不知道你怎麼想，但剛才有那麼一刻我真的不敢確定結果會怎樣，」@4擦著額頭的汗水對@5說。「我們走吧。」

## node 32  (DIAL_Z00#167)
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 305  (DIAL_Z00#172)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=11)
- text: 那些生物ñ消失ð了。  深怕那些生物會從背後冒出，@1猛地轉身，卻發現那些懾人的幻影確實已消失回原本的地方。  「牠們走了，」他說，聲音因方才的力竭而仍帶著沙啞。「我們繼續走吧。」

## node 129  (DIAL_Z00#173)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 這場戰鬥贏了。  「搜搜屍體找補給，」@4提議，接著補充：「動作快點。要是外頭還有埋伏，可別讓他們逮個正著。」

## node 306  (DIAL_Z00#174)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4眨了眨眼。  儘管那生物已經消失，他仍不敢鬆懈，但快速環顧四周後確認它已不見蹤影。「我想牠走了，」他說。「我們繼續走吧。」

## node 130  (DIAL_Z00#175)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 敵人逃跑了。  「我不太喜歡這種感覺，」@4說。「說不定還有更多敵人埋伏著。要是他們回頭找我們，最好確保我們早已不在這裡。」

## node 131  (DIAL_Z00#176)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=1 sub=11)
- text: @倒抽一口氣，撐起身子查看自己的傷勢。  「我看得改改計畫了，」@說。「我這傷是要命的。你們別管我，走吧……」  「沒人會被拋下，」@1憤怒地反駁。「一個都不行！收拾東西，我們走。路上我們會幫你找個治療者。」

## node 33  (DIAL_Z00#177)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - SET flag 0x7540=2
- text: @倒抽一口氣。  劇痛耗盡了他的力氣，他爬不起身，卻隱約感覺攻擊者正逐漸逼近，或許是要了結他，或許另有更不堪的打算。  「混帳……」@4低語，視線漸漸模糊。「願林絲克拉格瑪……詛咒ñ你ð……」  死亡來得很快……

## node 34  (DIAL_Z00#178)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 他們拔腿就跑。  @3咒罵自己的腳總愛踩到坑坑洞洞，但他跌跌撞撞繼續前進，心中滿是恐懼——生怕自己再也找不到安全之地，再也沒有一刻不被人惦記著要活活宰了他。這念頭令人麻木，但他仍奮力前行，直到與同伴會合、脫離險境。

## node 35  (DIAL_Z00#179)
- speaker=0  style=0
- text: 這感覺很可恥。  有那麼一刻，他動了逃跑的念頭——轉身離開，再也不為在乎的人或事以身犯險。他只想遠離這幅可怕的景象，但同伴一動不動地倒在地上、血流不止。他無法拋下朋友，任其送死。

## node 303  (DIAL_Z00#180)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=1 sub=10)
- text: 他們被困住了。  心跳聲在耳中轟鳴，@4逼自己停下……逼自己冷靜思考片刻；這僅僅幾秒的舉動卻彷彿過了一輩子那麼長。盤點局勢後，他很快意識到逃跑是徒勞的。  至少此刻，撤退是不可能的。

## node 309  (DIAL_Z00#181)
- speaker=0  style=0
- text: 撤退是不可能的。  側翼很可能還有其他敵人埋伏。一旦被前後夾擊，他們將腹背受敵，直至防線崩潰。  「唯一的路就是ñ正面突破，」@4果斷地說。「就算沒有另一批敵人埋伏，他們攔著我們，恐怕也是不想讓我們接近某樣東西。」

## node 132  (DIAL_Z00#182)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @仔細打量對手。  雖然他可能大幅誤判了@1的部分能力，但有幾件事他確信無疑：

## node 133  (DIAL_Z00#183)
- speaker=0  style=0  flags=paged-text
- effects:
    - frame/rect style override x=259 y=98 w=38 h=18
- branches:
    - [flag 0x0104 in [0..0]] -> node 4294901761

## node 41  (DIAL_Z00#184)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 42  (DIAL_Z00#186)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 43  (DIAL_Z00#188)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 44  (DIAL_Z00#190)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，彎腰查看地上的東西。片刻後他站起身，開口說道……

## node 45  (DIAL_Z00#192)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- text: 這棟房子一片漆黑。  「我不太喜歡這光景，」@0評估著情勢說道。「我的直覺告訴我，我們一敲門，就會有什麼東西像巨魔的臭味一樣纏上我們。」

## node 46  (DIAL_Z00#193)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 222  (DIAL_Z00#195)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道。

## node 244  (DIAL_Z00#197)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- text: 這棟房子一片漆黑。  「我不太喜歡這光景，」@0評估著情勢說道。「我的直覺告訴我，我們一敲門，就會有什麼東西像巨魔的臭味一樣纏上我們。」

## node 275  (DIAL_Z00#198)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 282  (DIAL_Z00#200)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- branches:
    - [always] -> node 0 (no jump)
- text: @0停下腳步，凝視著遠方。沉思片刻後，他轉過身開口說道……

## node 290  (DIAL_Z00#202)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- text: @0走近那棟古怪的居所。  他微微側著頭，目光緊盯著地面聆聽，雙眼像魚缸裡的魚一樣來回轉動。  終於他抬起頭：「我不敢肯定，但我強烈感覺我們在這裡會很不受歡迎。」

## node 292  (DIAL_Z00#203)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
- text: 鏟子閃著微光。  他們正要開始挖掘，@0卻舉手示意暫停。他在墓碑底部彎下腰，撿起一顆紅色小球，在食指與拇指間搓動。  「是蠟，」片刻後他說道。「有人在這座墳上點過蠟燭……或許是想驅趕惡靈。要是我們繼續挖，我建議做好承擔後果的準備。」

## node 47  (DIAL_Z00#204)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=12)
    - ?wOp12 a1=52 a2=0
    - play sfx 53
- branches:
    - [always] -> node 0 (no jump)
- text: 一隻鳥倏地飛上天空。  環顧四周尋找那動物驚慌的源頭，@0低聲道……

## node 271  (DIAL_Z00#206)
- speaker=0  style=5
- text: 這把鎖的金屬表面曾經大概像鏡子一樣反光，如今卻只是一道鏽蝕斑駁的屏障，將他們擋在門外。

## node 79  (DIAL_Z00#207)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [49378..0]] -> node 0 (no jump)
    - [flag 0x7530 in [48848..0]] -> node 65537
    - [flag 0x7530 in [48976..0]] -> node 131074
    - [flag 0x7530 in [49163..0]] -> node 196611

### (sub) DIAL_Z00#208
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0試了試門。  「鎖得很緊，」他說。「要不要試著把它打開？」

### (sub) DIAL_Z00#209
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0試了試門。  「這棟建築看來已經棄置了，離開前還特地上了鎖，」他說。「要不要試著把它打開？」

### (sub) DIAL_Z00#210
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 梯子往上通向天花板上一個幽暗的小洞。爬了幾階後，@0轉頭朝下方的同伴喊道：「上面有個上鎖的柵欄。要試著打開嗎？」

### (sub) DIAL_Z00#211
- speaker=0  style=0
- branches:
    - [flag 0xcb26 in [49407..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#212
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @3凝視著那口箱子。  他全神貫注地閉上雙眼，在腦海中描繪箱子的模樣，仔細端詳木紋與金屬箍，畫面漸漸清晰逼近，直到他不再只是看著箱子，而是看進了ñ箱子裡面。  「我相信這是安全的，」他終於開口。「要試著打開嗎？」

### (sub) DIAL_Z00#213
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 箱蓋紋絲不動。  「看來是上了鎖，」@0說。「要試著打開嗎？」

## node 86  (DIAL_Z00#214)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [49976..0]] -> node 0 (no jump)
    - [flag 0x7530 in [50393..0]] -> node 65537
    - [flag 0x7530 in [50817..0]] -> node 131074
    - [flag 0x7530 in [51234..0]] -> node 196611

## node 80  (DIAL_Z00#219)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [51720..0]] -> node 0 (no jump)
    - [flag 0x7530 in [52057..0]] -> node 65537
    - [flag 0x7530 in [52397..0]] -> node 131074
    - [flag 0x7530 in [52740..0]] -> node 196611

## node 81  (DIAL_Z00#224)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [53152..0]] -> node 0 (no jump)
    - [flag 0x7530 in [53276..0]] -> node 65537
    - [flag 0x7530 in [53414..0]] -> node 131074
    - [flag 0x7530 in [53538..0]] -> node 196611

## node 82  (DIAL_Z00#229)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [53763..0]] -> node 0 (no jump)
    - [flag 0x7530 in [53893..0]] -> node 65537
    - [flag 0x7530 in [54023..0]] -> node 131074
    - [flag 0x7530 in [54153..0]] -> node 196611

## node 245  (DIAL_Z00#234)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [54352..0]] -> node 0 (no jump)
    - [flag 0x7530 in [54614..0]] -> node 65537
    - [flag 0x7530 in [54887..0]] -> node 131074
    - [flag 0x7530 in [55148..0]] -> node 196611

## node 83  (DIAL_Z00#239)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x7530 in [55479..0]] -> node 0 (no jump)
    - [flag 0x7530 in [55687..0]] -> node 65537
    - [flag 0x7530 in [55882..0]] -> node 131074
    - [flag 0x7530 in [56090..0]] -> node 196611

## node 84  (DIAL_Z00#244)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [56268..0]] -> node 0 (no jump)
    - [flag 0x7530 in [56400..0]] -> node 65537
    - [flag 0x7530 in [56532..0]] -> node 131074
    - [flag 0x7530 in [56664..0]] -> node 196611

## node 85  (DIAL_Z00#249)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [56845..0]] -> node 0 (no jump)
    - [flag 0x7530 in [57041..0]] -> node 65537
    - [flag 0x7530 in [57237..0]] -> node 131074
    - [flag 0x7530 in [57433..0]] -> node 196611

## node 63  (DIAL_Z00#254)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [57658..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 64  (DIAL_Z00#257)
- speaker=0  style=0
- text: @打了個呵欠。  「我們需要休息，」他說著四處尋找紮營的好地方。「要是再這樣不睡下去，遇到路上的意外，我們恐怕應付不來。」

## node 325  (DIAL_Z00#258)
- speaker=0  style=0
- text: @0跪倒在地。  傷勢太重讓他無法起身，眼睜睜看著另一個人倒在自己身旁，卻無力相助。是朋友？還是敵人？光憑聲音他分辨不出。  「我們該……」@4低語，吸進滿口塵土，視線漸漸模糊。「我們早該……更……小心……」  死亡靜靜降臨……

## node 65  (DIAL_Z00#259)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [58662..0]] -> node 65537
    - [flag 0x7530 in [58837..0]] -> node 131074

### (sub) DIAL_Z00#261
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=10)
    - bind speaker-name slot (kind=1 sub=11)
    - bind speaker-name slot (kind=2 sub=13)
- text: @0感到一陣暈眩。  「我不太舒服，」他喘息道，一手按著滲血的側腹。「我這傷……可能會要命。」轉頭一看，@1也是同樣光景，臉色蒼白如屍。「也許你們該丟下我們。我們只會拖慢大家的腳步。」  @2搖了搖頭。「我們會找到治療者、神殿，或ñ隨便什麼ð辦法。這ó絕不會是我們的終點。」

## node 246  (DIAL_Z00#262)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [59288..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 326  (DIAL_Z00#265)
- speaker=0  style=0
- text: 沒人願意提起這件事。  看著彼此眼中呆滯的神色與逐漸浮現的病態蒼白，顯然他們都染上了某種凶猛的瘟疫。@4默默祈禱能盡快找到神殿，免得眾人都死於此病。

## node 247  (DIAL_Z00#266)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [60314..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 71  (DIAL_Z00#269)
- speaker=0  style=6
- text: @撥動魯特琴的弦。  「在你開始之前，我想你該知道我們的娛樂經費已經花光了，」酒館老闆低聲道。「你要是在這彈，也只是自娛自樂罷了。」

## node 73  (DIAL_Z00#270)
- speaker=0  style=6
- text: @與魯特琴搏鬥。  才一開始彈奏，他就覺得自己與其說是在演奏，不如說是在跟一頭體型百倍於己的野獸搏鬥。曲調一次次從他指間溜走，墜入一片刺耳的噪音深淵。  「ñ出去、ñ出去、ñ出去ð，」酒館老闆邊說邊從@手中一把奪過魯特琴。「慶幸這群客人今天心情還沒更糟。給他們點時間冷靜下來，你再回來，不過下次ñ只能ð是來吃飯的。」

## node 88  (DIAL_Z00#271)
- speaker=0  style=6
- effects:
    - bind speaker-name slot (kind=1 sub=19)
- text: 幸運眷顧了他們。  儘管他磕磕絆絆地彈著《ñ這ñ王國ñ是我的ð》的和弦，@技藝生疏，卻被酒館裡醉醺醺的客人隨節奏敲擊酒杯的喧鬧聲給掩蓋過去。  「那真是……ó有趣ð，」酒館老闆說。「我還沒聽過這首歌被折磨得這麼慘。算你走運，今晚客人都醉了。雖然違背我的判斷，他們卻ó堅持要我付你錢。拿去吧。」老闆從錢袋裡取出@1枚錢幣，遞給了@。

## node 89  (DIAL_Z00#272)
- speaker=0  style=6
- effects:
    - bind speaker-name slot (kind=1 sub=19)
- text: @彈奏起來。  他沉浸在音樂的流動之中，偶爾彈錯一兩個音，但整體而言，把《ñ這ñ王國ñ是我的ð》這首他唯一熟記於心的曲子彈得像模像樣。  「彈得不錯，」酒館老闆對@微笑道，遞給他@1。「改天要再來彈一曲。」

## node 90  (DIAL_Z00#273)
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @彈奏起來。  他的手指在魯特琴的指板上輕巧滑動，在《ñ這ñ王國ñ是我的ð》的和弦間流轉，樂音充盈胸臆，也引領著他向前。他輕聲唱起了副歌……

### (sub) DIAL_Z00#274
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: ó這ó王國ó是我的 ó以ó我ó的ó鮮血ó為代價 ó誓ó守ó護ó她ó抵禦ó任何ó來犯之敵

### (sub) DIAL_Z00#275
- speaker=0  style=6
- effects:
    - bind speaker-name slot (kind=1 sub=19)
- text: 終於彈完整首曲子，他發現聽眾們都愣在原地，鴉雀無聲，目光全落在他身上。  「太美了，」酒館老闆說。他伸手探入錢袋，取出@1枚錢幣放進@的手中。

## node 101  (DIAL_Z00#276)
- speaker=0  style=0  flags=?flag0x100
- text: 有什麼東西動了一下。  「我改變主意了，我們ñ別在這睡，」@4低語，一邊收拾行囊。「我有種不安的感覺，好像有人在盯著我們。盡量安靜地收拾東西，我們走。」

## node 240  (DIAL_Z00#277)
- speaker=0  style=0
- text: 左鍵點擊這顆石頭，時間將開始流逝，好讓隊伍休息。當時間走到你選定的位置時，隊伍就會醒來。

## node 237  (DIAL_Z00#278)
- speaker=0  style=0
- text: 左鍵點擊這個按鈕會離開紮營選項。

## node 238  (DIAL_Z00#279)
- speaker=0  style=0
- text: 左鍵點擊這個按鈕，時間將開始流逝，好讓隊伍休息。他們會持續睡眠，直到每位成員都恢復健康為止。

## node 239  (DIAL_Z00#280)
- speaker=0  style=0
- text: 左鍵點擊這個按鈕會停止時間的流逝。

## node 329  (DIAL_Z00#281)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊此區域會觀看該章節的場景。

## node 330  (DIAL_Z00#282)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕會離開目錄頁面。

## node 105  (DIAL_Z00#283)
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [64139..0]] -> node 0 (no jump)
    - [flag 0x7530 in [65003..0]] -> node 65537
    - [flag 0x7530 in [364..1]] -> node 131074
    - [flag 0x7530 in [1499..1]] -> node 196611
    - [flag 0x7530 in [2289..1]] -> node 262148
    - [always] -> node 0 (no jump)

## node 323  (DIAL_Z00#290)
- speaker=0  style=6
- text: 左鍵點擊某項技能，可以ñ提高或ñ降低角色專注學習該技能的程度。

## node 294  (DIAL_Z00#291)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=160 h=30
- text: 第一章：ñ踏入ñ黑暗ñ之ñ夜 護送戈拉斯前往克朗多！

## node 295  (DIAL_Z00#292)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=205 h=30
- text: 第二章：ñ夜鷹ñ會ñ之ñ影 前往羅姆尼的黑羊酒館！

## node 296  (DIAL_Z00#293)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=245 h=30
- text: 第三章：ñ望ñ遠鏡ñ與ñ蜘ñ蛛 解開望遠鏡與蜘蛛之謎！

## node 297  (DIAL_Z00#294)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=168 h=30
- text: 第四章：ñ死亡ñ印ñ記 逃離北境！

## node 298  (DIAL_Z00#295)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=185 h=30
- text: 第五章：ñ血ñ染ñ河ñ川 堅守北衛城！

## node 299  (DIAL_Z00#296)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=133 h=30
- text: 第六章：ñ叛變 尋找馬克羅斯之書！

## node 300  (DIAL_Z00#297)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=178 h=30
- text: 第七章：ñ漫漫ñ長ñ路 摧毀莫瑞德人的裂界機！

## node 301  (DIAL_Z00#298)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=152 h=30
- text: 第八章：ñ遠方ñ之ñ地 救出帕格與蓋米娜！

## node 302  (DIAL_Z00#299)
- speaker=0  style=0
- effects:
    - frame/rect style override x=12 y=160 w=222 h=30
- text: 第九章：ñ狂神ñ之ñ怒 阻止馬卡拉抵達生命石！

## node 315  (DIAL_Z00#300)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法建立重要的資料檔案！  您的磁碟空間可能不足。

## node 311  (DIAL_Z00#301)
- speaker=0  style=0
- effects:
    - frame/rect style override x=134 y=16 w=167 h=89
- text: 左鍵點擊這個按鈕，選取與此符號相關的法術。

## node 312  (DIAL_Z00#302)
- speaker=0  style=0
- effects:
    - frame/rect style override x=134 y=16 w=167 h=89
- text: 左鍵點擊這個按鈕以結束法術選取。

## node 254  (DIAL_Z00#303)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取普通弩箭。

## node 255  (DIAL_Z00#304)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取精靈弩箭。

## node 256  (DIAL_Z00#305)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取圖蘭尼弩箭。

## node 257  (DIAL_Z00#306)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取燃燒弩箭。

## node 258  (DIAL_Z00#307)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取淬毒弩箭。

## node 259  (DIAL_Z00#308)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取淬毒精靈弩箭。

## node 260  (DIAL_Z00#309)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取淬毒圖蘭尼弩箭。

## node 261  (DIAL_Z00#310)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕以選取附魔弩箭。

## node 262  (DIAL_Z00#311)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕會顯示更多箭矢種類。

## node 263  (DIAL_Z00#312)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕會讓目前角色休息一回合。

## node 264  (DIAL_Z00#313)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕可讓目前角色發射弩弓。

## node 265  (DIAL_Z00#314)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕可讓目前角色施展法術。

## node 266  (DIAL_Z00#315)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕可讓目前角色防禦一回合。

## node 267  (DIAL_Z00#316)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕可讓目前角色查看一名敵人。

## node 268  (DIAL_Z00#317)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕會進入自動戰鬥。

## node 269  (DIAL_Z00#318)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕會讓全體隊伍嘗試戰術撤退。

## node 270  (DIAL_Z00#319)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=24 w=243 h=72
- text: 左鍵點擊這個按鈕可查看目前角色的物品欄。

## node 331  (DIAL_Z00#320)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=13 y=11 w=294 h=101
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要中止本局遊戲並返回主選單嗎？

## node 115  (DIAL_Z00#321)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可開始新遊戲。

## node 111  (DIAL_Z00#322)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要開始新遊戲嗎？

## node 117  (DIAL_Z00#323)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可儲存目前進行中的遊戲。

## node 112  (DIAL_Z00#324)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要刪除目錄清單中目前選取的目錄，以及其中包含的所有遊戲存檔嗎？

## node 113  (DIAL_Z00#325)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要刪除遊戲清單中目前選取的存檔嗎？

## node 122  (DIAL_Z00#326)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可刪除選取的目錄及其中包含的所有遊戲存檔。選取的目錄會在目錄清單中反白顯示。

## node 123  (DIAL_Z00#327)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可刪除選取的遊戲存檔。選取的存檔會在遊戲清單中反白顯示。

## node 124  (DIAL_Z00#328)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可儲存目前選取或文字框中命名的遊戲。

## node 125  (DIAL_Z00#329)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可取消所有選取並返回選項畫面。

## node 126  (DIAL_Z00#330)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 目前沒有可刪除的選取目錄。

## node 127  (DIAL_Z00#331)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 選取的目錄無法完全刪除，該目錄中可能含有無法辨識的子目錄。

## node 134  (DIAL_Z00#332)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法建立存檔目錄！  您的磁碟空間可能不足。

## node 135  (DIAL_Z00#333)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 目前沒有可刪除的選取遊戲存檔。

## node 146  (DIAL_Z00#334)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 您輸入的目錄名稱無效。目錄名稱不得超過八個字元，且僅能包含字母與數字。作業系統保留的名稱同樣無效。

## node 147  (DIAL_Z00#335)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  已無多餘空位可建立新的存檔目錄。若要騰出新空位，必須先刪除既有目錄。

## node 148  (DIAL_Z00#336)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法建立新的存檔目錄！  您的磁碟空間可能不足。

## node 149  (DIAL_Z00#337)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  目前目錄已滿。您必須從此目錄中刪除一筆存檔，或另建新目錄。

## node 150  (DIAL_Z00#338)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  您的磁碟空間可能不足。

## node 151  (DIAL_Z00#339)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  選擇儲存選項前，您必須先輸入存檔的檔案名稱。

## node 152  (DIAL_Z00#340)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  選擇儲存選項前，您必須先輸入目錄名稱。

## node 153  (DIAL_Z00#341)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存遊戲！  選擇儲存選項前，您必須先輸入目錄名稱與存檔的檔案名稱。

## node 116  (DIAL_Z00#342)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可還原先前儲存的遊戲，繼續進行。

## node 136  (DIAL_Z00#343)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可還原目前選取的遊戲存檔，繼續進行。

## node 137  (DIAL_Z00#344)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可取消所有選取並返回選項畫面。

## node 138  (DIAL_Z00#345)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 沒有可還原的存檔！

## node 139  (DIAL_Z00#346)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 此目錄中沒有可還原的存檔！

## node 118  (DIAL_Z00#347)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可變更您的偏好設定檔。

## node 114  (DIAL_Z00#348)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要將所有偏好設定還原為預設值嗎？

## node 140  (DIAL_Z00#349)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕會將目前的偏好設定變更為您的選擇，檔案將自動儲存至磁碟。

## node 141  (DIAL_Z00#350)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可取消您所做的所有變更，並返回選項畫面。

## node 142  (DIAL_Z00#351)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可自動將每項偏好設定還原為預設狀態。

## node 316  (DIAL_Z00#352)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 無法儲存偏好設定檔！  您的磁碟空間可能不足。

## node 119  (DIAL_Z00#353)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕會前往目錄頁面。

## node 120  (DIAL_Z00#354)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可離開遊戲並返回 DOS 命令列。

## node 110  (DIAL_Z00#355)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 確定要離開遊戲並返回 DOS 嗎？

## node 121  (DIAL_Z00#356)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可返回目前進行中的遊戲。

## node 128  (DIAL_Z00#357)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕可返回目前進行中的遊戲。

## node 143  (DIAL_Z00#358)
- speaker=0  style=0  flags=?flag0x100
- text: 尚未選取或建立書籤所在的目錄。您可以透過「儲存遊戲」選項來選取或建立目錄。

## node 144  (DIAL_Z00#359)
- speaker=0  style=0  flags=?flag0x100
- text: 無法儲存書籤！  您的磁碟空間可能不足。

## node 158  (DIAL_Z00#360)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4小心翼翼地打開那個輕薄的帆布行囊。  祈禱裡頭的東西還沒被哪個貪婪的旅人捷足先登，他往裡頭窺探……

## node 93  (DIAL_Z00#361)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這是個袋子。  以輕薄的帆布材質縫製而成，看起來似乎ñ能裝下不少東西。

## node 78  (DIAL_Z00#362)
- speaker=0  style=0
- branches:
    - [flag 0x1fbf in [0..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#363
- speaker=0  style=0  flags=random branch (RND over choices)
- effects:
    - SET flag 0x1fbf=1
    - timer upsert kind=4 sub=8127 (3600)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 94  (DIAL_Z00#367)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: @0 皺起眉頭。  「是具屍體，」他說。「也許該搜一搜。」

## node 95  (DIAL_Z00#368)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
    - bind speaker-name slot (kind=1 sub=17)
- text: 「我想他死了，」@0說著，打量@1的屍體。

## node 250  (DIAL_Z00#369)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=1 sub=17)
- text: @1沒注意到他們。  「誰知道他是想殺我們，還是只是隨便走走，」@4說。「還是盡量避開他比較好。」

## node 251  (DIAL_Z00#370)
- speaker=0  style=0
- text: 他們決定發動攻擊。  快速確認過計畫後，@4定下了一套簡單的策略。  「那就這麼辦，」他說。「希望我們的接近不會被發現，不然這優勢就白費了。」

## node 252  (DIAL_Z00#371)
- speaker=0  style=0
- text: @5搖了搖頭，難以置信地盯著@3。  「沒錯，那ñ就是我們挑中的那群人，」他說。「你剛才沒在聽嗎？現在給我安靜，照計畫走，不然優勢就沒了。」

## node 304  (DIAL_Z00#372)
- speaker=0  style=0
- text: @4數了數人數。  儘管他在歷次冒險中屢次以寡敵眾，他也明白對手的數量足以輕易壓垮他們。「這麼多人我們對付不了。也許該換個戰術繞過他們。」

## node 96  (DIAL_Z00#373)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
- branches:
    - [flag 0x7530 in [13423..1]] -> node 0 (no jump)
    - [flag 0x7530 in [13515..1]] -> node 65537
    - [flag 0x7530 in [13807..1]] -> node 131074
    - [flag 0x7530 in [13955..1]] -> node 196611
    - [flag 0x7530 in [14114..1]] -> node 262148
    - [flag 0x7530 in [14522..1]] -> node 327685
    - [flag 0x7530 in [14679..1]] -> node 393222
    - [flag 0x7530 in [14843..1]] -> node 458759
    - [flag 0x7530 in [15024..1]] -> node 524296
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#374
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「私人住宅，」@0說。「不確定裡面有沒有人。」

### (sub) DIAL_Z00#376
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「應該是某種店鋪，」@4猜測道，試著透過陰暗的窗戶看清裡頭。「不確定他們在賣什麼。」

## node 156  (DIAL_Z00#384)
- speaker=0  style=0  flags=?flag0x100
- text: @4向前踏了一步。  「我們得從ñ正面ð接近這棟房子，」他果斷地說。

## node 159  (DIAL_Z00#385)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4撥開灌木叢茂密的枝條。  嚐了一顆深色的小漿果後點點頭，朝其他人喊道：「能吃。幫我看看這裡夠不夠湊成一小包……」

## node 160  (DIAL_Z00#386)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @3撥開灌木叢茂密的枝條。  這些帶色的小漿果讓他的指尖感到一陣暖意，他立刻認出它們具有恢復體力的效用。他招呼其他人過來：「幫我看看這裡的漿果夠不夠裝滿一個備用藥瓶……」

## node 161  (DIAL_Z00#387)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4撥開灌木叢茂密的枝條。  嚐了一顆深色的小漿果後點點頭，朝其他人喊道：「味道有點怪，但幫我看看這裡夠不夠湊成一小包……」

## node 162  (DIAL_Z00#388)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這些葉子色澤黯淡。  呈現暗淡的棕色與赭色，這叢灌木看起來不怎麼起眼，但也許能結出可食用的漿果。

## node 163  (DIAL_Z00#389)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這些葉子色澤黯淡。  呈現暗淡的棕色與赭色，這叢灌木看起來不怎麼起眼，但也許能結出派得上用場的漿果。

## node 164  (DIAL_Z00#390)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這些葉子色彩繽紛。  呈現鮮豔的紅色與橙色，這叢灌木美得令人屏息。

## node 165  (DIAL_Z00#391)
- speaker=0  style=0  flags=?flag0x100
- text: 灰燼已經冷了。  @4擦去手上的污垢，搖了搖頭。「顯然有人或什麼東西在這紮過營，但很難說是什麼時候。」

## node 166  (DIAL_Z00#392)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這處小營火只剩幾塊焦黑的木頭和一圈小石頭。

## node 167  (DIAL_Z00#393)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 設計相當標準。  @4饒富興味地檢視這座投石機，注意到它與王國使用的型號極為相似。他曾多次見過這類裝置把超過五十磅重的石塊，拋擲到球道兩倍遠的距離之外。

## node 190  (DIAL_Z00#394)
- speaker=0  style=0  flags=?flag0x100|paged-text
- effects:
    - bind speaker-name slot (kind=0 sub=15)
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @3一把抓住@0的肩膀。  突如其來的舉動嚇了@0一跳，他停下腳步抬頭望向同伴。「怎麼了？」  「這口箱子，」@3答道。「給我一點時間。」他全神貫注，眼前的畫面疊上了另一幅景象，唯一的不同是多了一個跪在箱子前的人影，手裡拿著一皮囊的石腦油。  「它ñ被動了手腳ð，」@3因法術的效果而略顯恍惚地說道。「有人動了機關，蓋子一掀就會爆炸。要試著解除它嗎？」

## node 191  (DIAL_Z00#395)
- speaker=0  style=0
- text: 陷阱已被解除。  @4鬆了口氣，輕輕掀開箱蓋。

## node 192  (DIAL_Z00#396)
- speaker=0  style=0
- text: 有什麼東西發出了喀嗒聲……  ……緊接著箱子ñ轟然炸開，火光與碎片四處橫飛……

## node 317  (DIAL_Z00#397)
- speaker=0  style=0
- branches:
    - [flag 0xcb26 in [17881..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#398
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @3凝視著那口箱子。  他全神貫注地閉上雙眼，在腦海中描繪箱子的模樣，仔細端詳木紋與金屬箍，畫面漸漸清晰逼近。直到他不再只是看著箱子，而是看進了ñ箱子裡面。  「我相信這是安全的，」他終於開口。「要試著打開嗎？」

### (sub) DIAL_Z00#399
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 這口箱子已經燒焦了。  提防著第一次把箱子燒得焦黑的陷阱可能沒有完全解除，@3望向同伴。「還要冒險ó現在ð打開它嗎？」

## node 193  (DIAL_Z00#400)
- speaker=0  style=0
- text: @4咬緊牙關。  儘管大家已同意該打開這箱子，他私下仍擔心前一個使用者或許留下了什麼不太愉快的驚喜……

## node 194  (DIAL_Z00#401)
- speaker=0  style=0
- text: @4咬緊牙關。  儘管大家已同意該打開這箱子，他私下仍擔心前一個使用者或許留下了什麼不太愉快的驚喜……

## node 91  (DIAL_Z00#402)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「看來有人遺失了一口箱子，」@4說。「或許值得查看一下。」

## node 92  (DIAL_Z00#403)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「是口箱子，」@0說。「上頭似乎裝了個特殊的鎖。」

## node 195  (DIAL_Z00#404)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「看來有人遺失了一個箱子，」@4說。「或許值得查看一下。」

## node 87  (DIAL_Z00#405)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4咬緊牙關。  儘管大家已同意該打開這箱子，他私下仍擔心前一個使用者或許留下了什麼不太愉快的驚喜……

## node 7  (DIAL_Z00#406)
- speaker=0  style=0  flags=paged-text
- effects:
    - bind speaker-name slot (kind=0 sub=13)
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0把箱蓋掀起一條縫。  「看來是沒鎖的，」他說。「要打開嗎？」

## node 8  (DIAL_Z00#407)
- speaker=0  style=0
- text: 箱蓋紋絲不動。  「不行，」@0說。「唯一能打開這口箱子的辦法，就是靠一套開鎖工具。」

## node 9  (DIAL_Z00#408)
- speaker=0  style=0
- text: @微微一笑。  收起開鎖工具，他朝箱子比了個手勢。「這還挺容易的。來把箱蓋打開吧。」

## node 10  (DIAL_Z00#409)
- speaker=0  style=0
- effects:
    - advance in-game time by 900
- text: 折騰了半個小時後，@厭惡地扔下工具。  「看來我那點開鎖的皮毛顯然不夠用，」他說。「這鎖太複雜了，我打不開。」

## node 168  (DIAL_Z00#410)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 石柱裡似乎ñ住著什麼東西。  一股被監視的感覺，加上柱子內部搏動的詭異光芒，都讓@4覺得該謹慎面對這處陌生的遺跡。

## node 169  (DIAL_Z00#411)
- speaker=0  style=0  flags=?flag0x100
- text: 這玉米還太嫩了。  丟開手中摘下的玉米穗，@4聳了聳肩。「吃ñ這個只會讓我們鬧肚子。我們走吧。」

## node 170  (DIAL_Z00#412)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: @4盯著那片玉米田。  雖然還嫩得不能吃，看起來倒是挺不錯。

## node 171  (DIAL_Z00#413)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 這隻動物已經死了。  @4剝著這生物的屍體，小心避開陷阱的鐵齒，設法割下足夠的肉打包成一份乾糧……

## node 172  (DIAL_Z00#414)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這隻動物已經死了。  牠被獵人的陷阱夾住，看起來倒在地上沒多久。

## node 99  (DIAL_Z00#415)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
- text: @0盯著那扇門。  「立起屏障，不外乎是想把人關在裡面，或擋在外面，」他喃喃自語。「不知道這扇門是哪一種。」

## node 100  (DIAL_Z00#416)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
- text: 「這扇門太結實了，聽不出裡面的動靜，」@0說道。「只能親自進去看看另一頭是什麼了。」

## node 157  (DIAL_Z00#417)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - DAMAGE Health+Stamina of member#4 by -768
- text: @3笑了出來。  @4立刻朝這位樂不可支的同伴投去惡狠狠的一瞥，一點也不覺得自己撞頭關門這件事有什麼好笑的。  「我想你退後一步，你的ñ腦袋會輕鬆一點，」@3用居高臨下的語氣建議道。  「你再笑，我就拿你的腦袋當攻城槌用，」@4回嘴道。

## node 98  (DIAL_Z00#418)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 「這是某種隧道入口，」@0說。

## node 196  (DIAL_Z00#419)
- speaker=0  style=0  flags=paged-text
- effects:
    - bind speaker-name slot (kind=0 sub=7)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 轉向@0，@1說：「要不要挖開這座墳墓？」

## node 66  (DIAL_Z00#420)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=7)
    - bind speaker-name slot (kind=1 sub=13)
- text: 跟@1簡短討論過後，@0搖了搖頭。  「我知道莫瑞德間諜會拿墳墓當秘密藏物點，」他說，「但一想到可能誤挖到死人，我就渾身不自在！再說，我們需要鏟子，用劍挖只會把劍毀了。」

## node 67  (DIAL_Z00#421)
- speaker=0  style=0
- text: 這番挖掘十分累人。  站在及腰深的坑洞裡，@0用鏟尖撬開松木棺蓋。棺蓋終於打開時，他臉上浮現出一種鬆一口氣又帶著失望的複雜神情。  「奇怪，」@0說。「沒有屍體。」

## node 68  (DIAL_Z00#422)
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
- text: 一個小時過去了。  渾身沾滿泥垢與墓土，@0滿臉嫌惡地掀開沉重的棺蓋查看內容物。一股濃烈的氨氣味從腐爛的遺體中撲面而來，他當場乾嘔。  「只是具屍體，」他噁心地說。

## node 69  (DIAL_Z00#423)
- speaker=0  style=0
- text: 濃煙從地底滲出。  @0驚恐地從那座被褻瀆的墳墓邊後退，只見氣體開始盤旋成一團帶著火花的漩渦……

## node 173  (DIAL_Z00#424)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這讓他著了迷。  平時並不陰鬱的@4，這回卻讓自己細細端詳起墓碑，以及上頭刻著的姓名與墓誌銘。

## node 174  (DIAL_Z00#425)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這座梯子看起來夠堅固，撐得住一個成年人的重量而不會斷裂。

## node 15  (DIAL_Z00#426)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 泥土底下埋著什麼東西。  「這個洞不夠大，裝不下一個人，應該不是墳墓，」@4說。「可能是藏糧食或補給的密窖。我們看看吧。」

## node 155  (DIAL_Z00#427)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這一小堆泥土看來像是有人最近在這裡挖過洞。但不清楚裡頭是否真的埋著什麼值錢的東西。

## node 175  (DIAL_Z00#428)
- speaker=0  style=0  flags=?flag0x100
- text: 這番搜索徒勞無功。  @4無奈地把石頭重新堆好，心裡多少鬆了口氣，至少石堆底下沒有什麼陷阱在等著他們。

## node 176  (DIAL_Z00#429)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: @4起了疑心。  儘管看起來無傷大雅，這堆石頭可能代表著各種可能性；陷阱、寶藏、墳墓、箱子……ñ什麼都有可能ð。

## node 197  (DIAL_Z00#430)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z00#431
- speaker=0  style=0  flags=paged-text
- effects:
    - SET flag 0x1fd3=1
- branches:
    - [flag 0x0100 in [0..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 一道深坑在他們面前張著大口。  小心翼翼不敢靠得太近以免摔下去，@4搖了搖頭。「唯一過去的辦法就是ñ盪過去，」他說。抬頭瞥見天花板上一個小掛鉤，他點了點頭。「看來遇上這困境的不只我們。我想可以把繩子繫在上頭，要試著盪過去嗎？」

## node 198  (DIAL_Z00#432)
- speaker=0  style=0  flags=?flag0x100
- text: 一道深坑在他們面前張著大口。  小心翼翼不敢靠得太近以免摔下去，@4搖了搖頭。「唯一過去的辦法就是ñ盪過去，」他說。抬頭瞥見天花板上一個小掛鉤，他嘆了口氣：「要是有條繩子，我們大概就能盪過這道深坑了。」

## node 276  (DIAL_Z00#433)
- speaker=0  style=0  flags=?flag0x100
- text: 繩子磨損了。  「這下好繩子沒了，」@4說著，把那段沒用的麻繩丟進坑裡。「希望我們不用再過這道坑了。」

## node 277  (DIAL_Z00#434)
- speaker=0  style=0
- text: @4手腳亂舞。  他最後的印象，是一道幽暗的豎井，與迎面而來的堅硬泥地……

## node 177  (DIAL_Z00#435)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這道深邃的坑洞橫貫狹窄的通道。  站在坑邊，@4很快判斷這坑太寬跳不過去，也太深，爬下去太過冒險。

## node 178  (DIAL_Z00#436)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4的指尖一陣刺麻。  他抓緊那些造型古怪的水晶，使盡全力拉扯……

## node 179  (DIAL_Z00#437)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這些水晶很ñ古怪ð。  與@4在米德凱米亞見過的任何東西都不同，這些結構彷彿有股內在能量在脈動著。

## node 180  (DIAL_Z00#438)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 裂界機發出嗡嗡聲。  這裝置由兩根插入地面的杖柱構成，頂端各有一個金屬蕈狀物，有時會浮現出等在門另一端的莫瑞德人身影……

## node 181  (DIAL_Z00#439)
- speaker=0  style=0  flags=?flag0x100
- text: @4悶哼一聲。  儘管他一再使勁想把稻草人從地裡拔出來，它卻紋絲不動。

## node 182  (DIAL_Z00#440)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 它正逐漸散架。  從人偶衣衫裡漏出的稻草看來，這個稻草人顯然是走投無路的農夫倉促拼湊而成的。

## node 183  (DIAL_Z00#441)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - bind speaker-name slot (kind=0 sub=15)
- text: 好奇心佔了上風。  掀開覆蓋在骨架上的厚重獸皮，@0冒險朝裡頭望去……

## node 184  (DIAL_Z00#442)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這是一台攻城器械。  大小約莫足以掩護三名士兵，外層覆蓋著一層去毛的厚重獸皮。塔頂附近開有幾道狹縫，讓弓箭手能對來犯的敵人射擊。

## node 97  (DIAL_Z00#443)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
    - bind speaker-name slot (kind=0 sub=13)
- text: 「我猜這是個路標，」@0說。

## node 185  (DIAL_Z00#444)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這塊石板很古怪。  比一個成年矮人略大一些，這塊石頭看起來十分古老，@0不禁猜想它是否曾是某種古老宗教儀式的一部分。

## node 186  (DIAL_Z00#445)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4小心翼翼地靠近那截樹樁。  見它是中空的，他往裡頭看去……

## node 187  (DIAL_Z00#446)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: 這裡曾經是一棵樹。  橡木的樹幹早已腐朽發霉，只剩下一層中空的樹皮外殼。

## node 188  (DIAL_Z00#447)
- speaker=0  style=0
- effects:
    - play sfx 64
    - play sfx 64
    - play sfx 64
- text: 他們從這口小井打了些水，貪婪地大口喝下。  接著只稍作停留，把水囊裝滿，便收拾行囊準備離開。

## node 189  (DIAL_Z00#448)
- speaker=0  style=0
- effects:
    - frame/rect style override x=35 y=35 w=250 h=70
- text: @4端詳著這口井。  他原本希望井邊或許會有個標示，寫明水質好壞，但無論怎麼找，都看不到任何這樣的資訊。

## node 154  (DIAL_Z00#449)
- speaker=0  style=0  flags=?flag0x100
- text: @0聳了聳肩。  「這應該不是什麼重要的東西，」他邊說邊轉身離開。

## node 199  (DIAL_Z00#450)
- speaker=0  style=0  flags=?flag0x100
- text: @5驚訝地看著。  濃密的霧氣從@3的嘴裡滾滾湧出，彷彿他腹中燃著一團可怕的火，煙霧驚慌失措地急欲逃離他的身體。  不到一分鐘，這片區域已完全籠罩在濃霧之中。

## node 200  (DIAL_Z00#451)
- speaker=0  style=0  flags=?flag0x100
- text: 一道人造光芒驅散了黑暗。  @3搖了搖頭，拚命想打破自己的專注狀態。他快速眨眼，讓雙眼適應這詭異的人造光線。  「我沒事，我們走吧。」

## node 201  (DIAL_Z00#452)
- speaker=0  style=0  flags=?flag0x100
- text: 頭頂上，星光驟然一閃。  @3在頭頂大幅一揮手，光芒如閃爍的塵埃般在他們周圍浮現。他快速眨眼，讓雙眼適應這詭異的人造光線。  「跟天上借點光，」@3解釋道。「我們走吧。」

## node 202  (DIAL_Z00#453)
- speaker=0  style=0  flags=?flag0x100
- text: @3並未感覺到任何不同。  一切似乎如常，只是身體周圍隱約多了一層微光。他舉起手擺動手指，@5在一旁饒富興味地看著。  「我看你的法術恐怕沒生效，」他說。「或許該再試一次。」  「但它ñ確實生效了。你看不出效果，是因為這道法術是專門針對莫萊伍夫設計的。我們走吧。」

## node 203  (DIAL_Z00#454)
- speaker=0  style=0  flags=?flag0x100
- text: @3感覺腦中有什麼轉動了一下。  彷彿他的大腦突然翻了個面，腦海中的思緒手忙腳亂地想從混亂中恢復秩序、找回平衡。  終於，畫面開始成形，接著……是文字與字母，只是這些並非他熟悉的思路。那是ñ莫瑞德語ð！

## node 204  (DIAL_Z00#455)
- speaker=0  style=0  flags=?flag0x100
- text: @3低聲唸誦咒語。  知道這法術的效果除了自己以外沒人看得見，@3唸完後解釋道：「在效果消失之前，我能……感應到……箱子是否有陷阱。」

## node 209  (DIAL_Z00#456)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - advance in-game time by 1800
- text: @3唸咒失敗了。  抱著一絲希望，他試圖唸完剩下的咒語，卻為時已晚地意識到已無力回天。「搞砸了，」他咬牙低罵。「完全是浪費時間。」

## node 212  (DIAL_Z00#457)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - advance in-game time by 1800
- text: @3唸咒失敗了。  抱著一絲希望，他試圖唸完剩下的咒語，卻為時已晚地意識到已無力回天。「搞砸了，」他咬牙低罵。「完全是浪費時間。」

## node 215  (DIAL_Z00#458)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - advance in-game time by 1800
- text: @3唸咒失敗了。  抱著一絲希望，他試圖唸完剩下的咒語，卻為時已晚地意識到已無力回天。「搞砸了，」他咬牙低罵。「完全是浪費時間。」

## node 216  (DIAL_Z00#459)
- speaker=0  style=0
- effects:
    - frame/rect style override x=134 y=16 w=167 h=89
- text: 您選取的角色不會施展法術！

## node 11  (DIAL_Z00#460)
- speaker=0  style=0
- text: 這口莫瑞德箱子構造粗糙，外層以鐵條加固，若不解開字鎖機關就休想打開；從箱面上的刮痕判斷，先前已有人為此吃盡苦頭才學到教訓。

## node 12  (DIAL_Z00#461)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
    - bind speaker-name slot (kind=0 sub=16)
- text: @0仔細看著莫瑞德提示牌上凸雕的符文，那上頭的文字是解開這道棘手字鎖唯一的希望。

## node 13  (DIAL_Z00#462)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=16)
    - frame/rect style override x=37 y=64 w=243 h=72
- text: @0揉了揉太陽穴。  這些莫瑞德文字對他來說簡直如同無法翻越的高牆。在他解開這道謎題之前，箱子裡的東西只能暫且按兵不動。

## node 14  (DIAL_Z00#463)
- speaker=0  style=0
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
    - bind speaker-name slot (kind=0 sub=2)
    - bind speaker-name slot (kind=1 sub=6)
    - bind speaker-name slot (kind=2 sub=13)
- text: 箱子傳出一聲悶響。  確認法術鎖已經解開，@2掀開了那扇大木蓋……

## node 205  (DIAL_Z00#464)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊轉盤可將其轉到下一個位置，每個轉盤上有四個字母。

## node 206  (DIAL_Z00#465)
- speaker=0  style=0  flags=?flag0x100
- effects:
    - frame/rect style override x=37 y=64 w=243 h=72
- text: 左鍵點擊這個按鈕以離開謎題並返回主畫面。

## node 223  (DIAL_Z00#466)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕，若前方無障礙物，隊伍將向前移動一步。

## node 224  (DIAL_Z00#467)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕，若後方無障礙物，隊伍將向後移動一步。

## node 225  (DIAL_Z00#468)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會讓隊伍向左轉。

## node 226  (DIAL_Z00#469)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會讓隊伍向右轉。

## node 227  (DIAL_Z00#470)
- speaker=0  style=0  flags=?flag0x100
- text: 當這個按鈕啟用時，畫面上會出現一小段道路標示。左鍵點擊可讓隊伍自動沿著道路前進，再次左鍵點擊則恢復自由移動。

## node 228  (DIAL_Z00#471)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕可讓一名法術使用者施展法術。

## node 232  (DIAL_Z00#472)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會顯示俯視地圖。

## node 229  (DIAL_Z00#473)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕可讓隊伍紮營。

## node 230  (DIAL_Z00#474)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會將目前遊戲儲存為書籤。要還原先前儲存的書籤，請從選項選單使用「還原遊戲」選項。

## node 231  (DIAL_Z00#475)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會顯示選項選單。

## node 233  (DIAL_Z00#476)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會縮小地圖檢視。

## node 234  (DIAL_Z00#477)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會放大地圖檢視。

## node 235  (DIAL_Z00#478)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會顯示米德凱米亞的完整地圖。

## node 236  (DIAL_Z00#479)
- speaker=0  style=0  flags=?flag0x100
- text: 左鍵點擊這個按鈕會返回世界檢視畫面。

## node 336  (DIAL_Z00#480)
- speaker=0  style=0
- text: 一切結束了。  帕格凝視著馬卡拉的屍身靜靜躺在堅硬的石地上。躲避著幾乎要壓垮痛楚與疲憊的悲傷，他轉頭望向歐文，見那男孩跪倒在地。帕格正要上前扶他起身，卻注意到一道詭異的光芒正瀰漫整個密室……
