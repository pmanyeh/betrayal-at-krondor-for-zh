# DIAL_Z23

109 records, 33 keyed nodes

## node 2300001  (DIAL_Z23#0)
- speaker=0  style=3  flags=paged-text
- effects:
    - ?wOp12 a1=38 a2=0
- branches:
    - [flag 0x0100 in [513..0]] -> node 4294901761
    - [flag 0x0101 in [593..0]] -> node 4294901761
- text: @4把門拉開。  撲鼻而來的下水道惡臭讓他一時反應不過來,他回頭望向@0,徵詢意見。「這裡臭死了,」他說道。「你確定準備好要進去了嗎?」

### (sub) DIAL_Z23#1
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - load teleport table 19
- text: 他們一步步走進那片惡臭瀰漫的黑暗之中……

### (sub) DIAL_Z23#2
- speaker=0  style=0
- effects:
    - ?wOp12 a1=39 a2=0

## node 2300002  (DIAL_Z23#3)
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [867..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0抬頭望向這條狹窄的樓梯。  這條路確實能往上走,但他不確定現在走這條路對不對。「你怎麼想,@4?」他問道。「你有興致爬那麼長一段路回去嗎?」

### (sub) DIAL_Z23#4
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 18
- text: 他們一步步走出那片惡臭瀰漫的黑暗……

## node 2300003  (DIAL_Z23#5)
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0100 in [1178..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4把柵欄拉開。  撲鼻而來的下水道惡臭讓他一時反應不過來,他回頭望向@0,徵詢意見。「那裡面臭死了,」他說道。「你確定準備好要進去了嗎?」

### (sub) DIAL_Z23#6
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - load teleport table 21
- text: 他們一步步走進那片惡臭瀰漫的黑暗之中……

## node 2300004  (DIAL_Z23#7)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [1287..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#8
- speaker=0  style=0
- effects:
    - SET flag 0x7541=1

### (sub) DIAL_Z23#9
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [1412..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 這道梯子通往ó上方。  「那裡就是通往王宮的路,」@4說道。「我們上去嗎?」

### (sub) DIAL_Z23#10
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 20
- text: 他們一步步走出那片惡臭瀰漫的黑暗……

## node 2300005  (DIAL_Z23#11)
- speaker=0  style=0
- branches:
    - [flag 0xc3b1 in [2133..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#12
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 12
- text: 水花從他們身上傾瀉而下。  他們踉蹌著穿過那道雷鳴般轟然作響的水簾,一頭撲倒在瀑布後方一塊濕滑的石板上。濕漉漉的髮絲垂在眼前,他們打量起這片陌生的新環境。  岩壁上鑿著一扇門,門框兩側各鑲著一個空蕩蕩的鐵製火盆。右側則有一處昏暗的小凹龕。  @4站起身湊近細看這個神秘的洞穴,發現裡頭有一副棋盤。「看起來像是有人準備下一盤棋,卻少了一顆騎士棋子。」

### (sub) DIAL_Z23#13
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 水花從他們身上傾瀉而下。  他們踉蹌著穿過那道雷鳴般轟然作響的水簾,一頭撲倒在瀑布後方一塊濕滑的石板上。濕漉漉的髮絲垂在眼前,他們打量起這片陌生的新環境。  岩壁上鑿著一扇門,門框兩側各鑲著一個空蕩蕩的鐵製火盆。右側則有一處昏暗的小凹龕。  @4站起身湊近細看這個神秘的洞穴,發現裡頭有一副棋盤。「看起來像是有人準備下一盤棋,卻少了一顆……ñ棋子。」  @0微微一笑。「你要是還沒ñ想通,那你腦子還真是跟樹墩一樣木。」

### (sub) DIAL_Z23#14
- speaker=0  style=6  flags=paged-text
- effects:
    - play sfx 49
    - play sfx 38
- branches:
    - [flag 0x0100 in [3117..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4點了點頭,取出他們在肯廷拉什那口井裡找到的騎士棋子。他把棋子放進空缺的位置,滿意地咧嘴一笑,大門隨即應聲而開。  「這要不是邀請函,我還真不知道什麼才算,」@4說道。「我們進去吧?」

### (sub) DIAL_Z23#15
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - load teleport table 23
- text: @4領著眾人前行。  沒過多久,他們便深入了這座洞穴……

## node 2300006  (DIAL_Z23#16)
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [3353..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 水流轟鳴聲灌滿了他們的耳朵。  「瀑布就在這條路的後方,」@4說道。「我們準備離開了嗎?」

### (sub) DIAL_Z23#17
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 22
- text: 他們加快了腳步。  穿過那扇門後,他們踏著水花衝過瀑布,來到對岸……

## node 2300037  (DIAL_Z23#18)
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0100 in [3794..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 樹枝不斷抽打著他們的臉。  @3一邊低聲抱怨著城堡工程師帶來的麻煩,一邊領頭走下這片長滿冷杉的山坡,終於來到一處大洞穴的洞口。「我就說我沒瘋吧,」他咕噥道。「看起來像個洞口。要不要進去看看?」

### (sub) DIAL_Z23#19
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - SET flag 0x0075=1
    - load teleport table 35
- text: 他們一步步走進黑暗之中……

## node 2300038  (DIAL_Z23#20)
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [4131..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0抬頭望向這條狹窄的樓梯。  這條路確實能往上走,但他不確定現在走這條路對不對。「你怎麼想,@4?」他問道。「你有興致爬那麼長一段路回去嗎?」

### (sub) DIAL_Z23#21
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 36
- text: 他們一步步走出黑暗……

## node 2300009  (DIAL_Z23#22)
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0100 in [4462..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4推了推書櫃。  書櫃順著一個特製的鉸鏈轉向一旁,露出一條向下傾斜、以木料鋪成的長通道。「這就是那條密道,」@4說道。「你覺得我們該從這條路離開嗎?」

### (sub) DIAL_Z23#23
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - load teleport table 27
- text: 他們走進了礦坑……

## node 2300010  (DIAL_Z23#24)
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [4773..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @0抬頭望向這條狹窄的樓梯。  這條路確實能往上走,但他不確定現在走這條路對不對。「你怎麼想,@4?」他問道。「你有興致爬那麼長一段路回去嗎?」

### (sub) DIAL_Z23#25
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 26
- text: 他們一步步走出黑暗……

## node 2300016  (DIAL_Z23#26)
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [5092..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4抬頭望向這條狹窄的樓梯。  這條路確實能往上走,但他不確定現在走這條路對不對。「你怎麼想,@0?」他問道。「你有興致爬那麼長一段路回去嗎?」

### (sub) DIAL_Z23#27
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - load teleport table 33
- text: 他們沒有被人發現。  慶幸自己活著逃出了地牢,@4心裡暗自記下,等到了更安全的地方,一定要向露西亞獻上感恩的禱告。眼下,他們還得先設法逃出薩薩戈斯的外圍防線……

## node 2300017  (DIAL_Z23#28)
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0100 in [5646..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 戈拉斯盯著歐文看。  「我們才剛從地牢逃出來,你就想ó回去?」這名莫瑞德人問道。「你在想什麼?」  男孩聳了聳肩。「這由你決定,戈拉斯。你想回那裡去嗎?」

### (sub) DIAL_Z23#29
- speaker=0  style=3  flags=reload-scr-between-pages
- effects:
    - load teleport table 34
- text: 戈拉斯嘆了口氣。  賭一把,相信男孩的直覺或許真能帶他們找對方向,兩人再次走進了薩薩戈斯地牢的黑暗之中……

## node 2300011  (DIAL_Z23#30)
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[4,2,1]
    - SET flag 0x0094=1
    - SET flag 0x0090=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#31
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 一道身影靠近。  那個身影從房間陰暗的角落朝他們走來。@0的心跳猛地加快了一瞬,但看出對方沒有要攻擊的意思,他才稍稍放鬆下來。

### (sub) DIAL_Z23#32
- speaker=3  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們兩個也太慢了。我還以為嘲弄幫又把你們給逮住了呢,詹姆士紳爵。一切都還好嗎?

### (sub) DIAL_Z23#33
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 侍從,先撇開這趟出行是機密要事、你根本不該知情這件事不談,也先不管我們現在正匆匆從下水道離開,而不是按規矩走正門——你到底是怎麼發現我們要來的?

### (sub) DIAL_Z23#34
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛,洛克利爾紳爵把我送到這裡以後,就說我可以回家了,結果我閒得發慌,決定來克朗多逛逛。可惜這裡也沒什麼特別有趣的事,所以我就想說回王宮看看。我昨晚ó試著去突襲探訪戈拉斯,卻發現守衛加倍了,還下令誰都不准見他。要不是我聽見牢房裡有人打呼,我大概還真會被騙過去。

### (sub) DIAL_Z23#35
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜戈拉斯不打呼吧。

### (sub) DIAL_Z23#36
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一點聲音都沒有。我發現情況不對勁以後,就去找洛克利爾,結果發現他神秘地不見了人影,儘管才剛送了一盤食物到他門口沒多久。最後我下來這裡,找林姆問了問,他告訴我你今天一早就來過這裡了。那時候我才意識到,亞魯莎打算悄悄把戈拉斯送出克朗多,不知道是為了什麼原因。

### (sub) DIAL_Z23#37
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定自己不是幹小偷這行的?你的想法跟我認識的一個嘲弄幫成員簡直如出一轍,讓人不太安心。

### (sub) DIAL_Z23#38
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼,我們準備好了嗎?我們該動身了吧。我們到底要去哪裡?

### (sub) DIAL_Z23#39
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你不能跟我們一起去,歐文。我們的任務太重要了……

### (sub) DIAL_Z23#40
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 安靜,莫瑞德人!這件事讓我來處理。

### (sub) DIAL_Z23#41
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可是我可能會給你們的任務帶來危險!誰知道我在這裡到提伯恩之間會不會被誰抓走?要是我現在回克朗多,搞不好會不小心跟人說溜嘴。再說,我ó就是王國東邊的人。我熟悉那一帶,說不定能幫上忙。

### (sub) DIAL_Z23#42
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管好壞,你似乎鐵了心要把自己的命運跟災難綁在一起。不過要是你這麼年輕就想找死,我又有什麼資格阻止你呢?想當年亞魯莎想溜出克朗多的時候,我也耍過同樣的把戲。

### (sub) DIAL_Z23#43
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧,侍從,你可以跟來,不過規矩先講清楚。第一,這裡我說了算,我說什麼你就照做,不准有異議。第二,不管什麼情況,都不准向任何人透露戈拉斯或我們任務的任何內容。要是有人問起,我們就照洛克利爾紳爵先前的說法——戈拉斯是ó精靈。第三,也是最後一條,不准自己隨便亂跑。就算你是要去尿尿,也得先問過我。都清楚了嗎?

### (sub) DIAL_Z23#44
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。你說什麼都行。

## node 2300012  (DIAL_Z23#46)
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 有人吹了聲口哨。  轉過身時,@4只覺得胃裡一沉,深怕他們又暴露在另一夥夜鷹會的攻擊範圍內。然而讓他大吃一驚的是,一位熟悉的朋友從陰影中走了出來……

### (sub) DIAL_Z23#47
- speaker=5  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 十二ó天神在上,洛克利爾,你的頭髮是怎麼回事!

### (sub) DIAL_Z23#48
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真有你的,吉米。我七個月沒見過你了,然後我才剛把你從一夥夜鷹會手裡救出來,你第一句話居然是問我頭髮怎麼染成這樣!這裡到底是怎麼回事?正門被砸壞了,下水道裡還有夜鷹會的人到處亂竄……

### (sub) DIAL_Z23#49
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó不是夜鷹會。是冒牌貨。有人一直想說服亞魯莎王子,說死亡公會在克朗多這裡東山再起,把下水道當成藏身處,希望藉此引來長槍騎兵隊下來把這裡掃蕩一空。而我猜,在幕後操盤的人真正的目的,是想順便讓長槍騎兵隊把嘲弄幫也一併連根拔起。

### (sub) DIAL_Z23#50
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼,想連根拔起盜賊公會?聽你以前當嘲弄幫時跟我說過的那些事,這聽起來可不容易啊。

### (sub) DIAL_Z23#51
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 更重要的是,我們現在知道了,自從我們搗毀了那夥人、平息了安妮塔公主那件事之後,有幾名夜鷹會的人逃去了羅姆尼。他們這陣子肯定不敢再踏進克朗多的街道。我一直在下面這邊四處查探,想多挖出點消息,結果就撞上了那幾個傢伙。  話說……你怎麼這麼快就回克朗多了,洛奇?我還以為你要再過四個月左右才會回來。

### (sub) DIAL_Z23#52
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我從北境帶回了壞消息。看來黑暗兄弟又蠢蠢欲動了。他們在薩薩戈斯上空豎起了穆爾曼達穆斯的戰旗,而且有一支莫瑞德大軍正在集結,準備攻打王國。這名莫瑞德人以前是他們的氏族酋長之一,裂界之戰對抗圖蘭尼人時還算得上是個英雄人物。我想亞魯莎王子應該會有興趣跟他談談。

### (sub) DIAL_Z23#53
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不喜歡這樣,洛奇。北方的莫瑞德人又蠢蠢欲動,又有人假冒死亡公會……我這預感麻煩的直覺告訴我,情況只會在好轉之前先變得更糟。  我猜你會出現在這裡,是想走我幾年前教你的那條路溜進王宮吧?

### (sub) DIAL_Z23#54
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯……我原本還在想得想辦法把柵欄撬開,不過要是你有鑰匙,那就省了我不少麻煩。

### (sub) DIAL_Z23#55
- speaker=5  style=0
- effects:
    - GIVE item 'G' cond=1 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)
- text: 鑰匙還在我身上。給你了。我自己有辦法進王宮。我打算再在下面多待一會兒,看能不能解開這個謎團。

## node 2300019  (DIAL_Z23#57)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯注意到了那幾個箱子。  他突然意識到他們手無寸鐵,便朝那些箱子比了比……

### (sub) DIAL_Z23#58
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我認為我們離開這間廳室之前,應該先檢查那些箱子裡裝了什麼。我們離開前可能會需要武器,我覺得那些儲物箱裡說不定裝著對我們有用的東西。

### (sub) DIAL_Z23#59
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是裡頭設了陷阱怎麼辦?

### (sub) DIAL_Z23#60
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 設陷阱有什麼意義?要是迪勒肯想要我們死,他早就有大把機會下手了,留我們活著對他也沒什麼好處。你儘管相信,要是迪勒肯真想讓我死,天一亮我早就沒命了。

### (sub) DIAL_Z23#61
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我一直在想這件事。為什麼要等?要是你跟迪勒肯真像你說的那樣是不共戴天的死敵,我猜他早該立刻把你吊死示眾了。薩薩戈斯這裡也沒剩什麼人可以看這場ó好戲,因為他大部分的支持者這時候應該都在東邊備戰。而且,牢房外面怎麼會沒有守衛?

### (sub) DIAL_Z23#62
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這件事,我或許知道一些內情。迪勒肯來我們牢房之前,我聽見守衛們低聲議論,說看守我們的納拉布已經從薩薩戈斯逃走了。要是他有理由ó逃走,那我只能猜想,他跟迪勒肯之間那份友好的結盟已經破裂了。要是真是這樣,我猜看守我們的人多半是被派去追捕納戈了。要是招惹到他,那可是相當危險的對手,萬一他決定反對這場對王國的攻勢,恐怕會惹出不少麻煩。

### (sub) DIAL_Z23#63
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 或許是這位ó納拉布放了我們。他說不定是在找盟友。

### (sub) DIAL_Z23#64
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 雖然納拉布跟我彼此毫無情誼可言,但這番推測或許不無道理。他的兄弟納戈是個法力不淺的法師,他自己說不定也有幾分本事,足以打開你的牢房。而且,他雖然絕不會直接出手幫我,但他很可能希望藉著我們逃脫製造一些混亂,好讓他自己趁機行事。

### (sub) DIAL_Z23#65
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就像趁著突襲把牛群從牛欄裡放出去一樣!大家忙著去追牛,根本沒發現小偷已經溜進屋裡了!

## node 2300020  (DIAL_Z23#67)
- speaker=0  style=3
- text: @4仔細查看了這道瀑布。  大體上看來,它跟其他瀑布沒什麼兩樣,但仔細一瞧,瀑布底部附近的草叢似乎被踩踏過,幾乎像是有人ó穿過瀑布走過去似的。

## node 2300021  (DIAL_Z23#68)
- speaker=0  style=3
- text: 前往地牢

## node 2300022  (DIAL_Z23#69)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但主題內容大多似乎跟ó魔法有關。

## node 2300023  (DIAL_Z23#70)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但主題內容大多似乎跟ó神學有關。

## node 2300024  (DIAL_Z23#71)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但主題內容大多似乎跟ó財經有關。

## node 2300025  (DIAL_Z23#72)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但主題內容大多似乎跟ó醫學有關。

## node 2300026  (DIAL_Z23#73)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但多數看起來像是各方學者或貴族的日誌手記。

## node 2300027  (DIAL_Z23#74)
- speaker=0  style=3
- text: @4端詳著這個書架。  架上不少書名不是褪色得無法辨讀,就是以外邦文字印製,但主題內容大多似乎跟ó軍事有關。

## node 2300036  (DIAL_Z23#75)
- speaker=0  style=3
- text: 前往薩斯

## node 2300039  (DIAL_Z23#76)
- speaker=0  style=3
- text: 前往薩斯地下礦坑

## node 2300028  (DIAL_Z23#77)
- speaker=0  style=3
- text: 返回地面

## node 2300029  (DIAL_Z23#78)
- speaker=0  style=3
- text: @4微微一笑。  薩斯的伊夏教團修士們窮盡心力也未能揭開宇宙間無數的奧秘,想想這條密道竟然瞞過了他們數百年之久,還真是有趣。

## node 2300030  (DIAL_Z23#79)
- speaker=0  style=6
- text: 這些書跟ó魔法有關。  @3順手抓起最近的一本書,開始翻閱書頁,希望能找到一部能讓他學習的咒語秘典。他翻著書頁,幾乎沒注意到一名祭司沿著走道走了過來,一把從他手裡抽走那本書,客氣地放回原處。  「這些書是禁止外借的,」祭司嚴肅地說道。「很久以前我們就學到教訓,得先確保初學者受過一定的訓練,才能讓他們接觸我們的魔法典籍。」  「我ó是受過一些訓練的,」@3才開口,便被祭司一記嚴厲的眼神鎮住,說不下去了。  「歡迎你去參觀我們其他的藏書,但ñ這一區是禁止進入的,」祭司說道,語氣裡...

## node 2300031  (DIAL_Z23#80)
- speaker=0  style=6  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 書架承載的重量幾乎快要超出極限。  一本本厚重的書,看起來都比@4能想像的還要古老,這一區大部分的著作似乎都跟神學或哲學有關。他對神明的歷史不像自己希望的那樣熟悉,便伸手拿了一本看起來沒那麼嚇人的書,開始讀了起來。

### (sub) DIAL_Z23#81
- speaker=0  style=0
- branches:
    - [flag 0x1fc2 in [20979..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#82
- speaker=0  style=6
- effects:
    - advance in-game time by 9000
    - SET flag 0x1fc2=1
- text: 他原本以為書名暗示的會是一本講述守護女神達拉的書,卻意外發現書裡收錄的其實是一份定期參加神殿禮拜者的姓名名冊。書裡還附有一頁特別的內容,似乎是達拉神殿祭司發布的一份公告。  á自á此á昭á告á天á下á,á永á誌á不á忘á。á…á…á…á…á…á…á…á…á…á…á…á…á…á…á…á…á…á á á願á達á拉á之á福á澤á,á降á臨á於á弗á蘭á德á爾á．á哈á夫á蓋á特á之á六á位á千á金á—á—á蒂á雅á、á安á德á麗á雅á、á吉á娜á、á莎á拉á、á綺á拉á、á拉á麗á...

### (sub) DIAL_Z23#83
- speaker=0  style=0
- branches:
    - [flag 0x1fc3 in [20979..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#84
- speaker=0  style=6
- effects:
    - advance in-game time by 7200
    - SET flag 0x1fc3=1
- text: 這是一本沉甸甸的厚重典籍,光是捧著就得費上不少力氣,書裡瀰漫著一股彷彿環繞著死亡女神林絲克拉格瑪的陰鬱氣息。令人意外的是,書中主張死者遺體應當火化,而非土葬,因為死後肉身已無足輕重。書末附近有一段簡短的文字,格外引人注意。  á…á…á一á旦á你á身á受á重á傷á,á幾á乎á能á觸á及á死á亡á女á神á的á容á顏á,á你á便á會á懸á於á一á種á不á死á不á活á的á狀á態á,á直á到á命á運á判á定á,á或á是á你á的á時á辰á已á到á、á該á踏á入á亡á者á的á殿á堂á,á...

### (sub) DIAL_Z23#85
- speaker=0  style=0
- branches:
    - [flag 0x1fc4 in [20979..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#86
- speaker=0  style=6
- effects:
    - advance in-game time by 10800
    - SET flag 0x1fc4=1
- text: 幸好這本講述純淨與治療之神頌恩的書,內容相對淺顯易讀,不過書裡講的頌恩神殿及其教義,他大多早已知曉。閤上書前,他特別留意到書中暗示,頌恩神殿提供的治療能力,比其他任何神殿都要廣泛強大。

### (sub) DIAL_Z23#87
- speaker=0  style=6
- effects:
    - advance in-game time by 21600
- text: 這是眾多探討至高神伊夏的書籍之一,書架上有數百本之多,這本內容艱澀難懂,字跡也潦草得幾乎難以辨認。他把書放到一旁,轉而看向架上其他的書。

### (sub) DIAL_Z23#88
- speaker=0  style=6
- effects:
    - advance in-game time by 7200
- text: 這本書用了大篇幅描述復仇之神卡胡利,以及王國一般百姓對他常有的誤解,接著簡短提到信徒必須完成的一連串懺悔儀式,其中包括一種名叫苦行贖身的奇特作法——信徒要挨餓,好讓自己配得上神殿的認可。書裡還列出一項事實:最常向這座神殿祈求的,其實是刺客。

### (sub) DIAL_Z23#89
- speaker=0  style=6
- effects:
    - advance in-game time by 900
- text: 才翻了幾頁,@4便看出這又是一本教義書,不過作者對宗教理論提出了幾個他先前未曾聽聞的新見解。翻完一個章節後,他把書放回了原位。  「這個架上或許還有內容更豐富的書,」他心想。

## node 2300032  (DIAL_Z23#90)
- speaker=0  style=6  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: @3皺起了臉。  眼前擺著的這些書全都跟財經理論有關,這個主題他父親早年就已經拿來把他煩得夠嗆。他原以為自己這輩子再也不會對這個主題感興趣,卻發現自己還是伸手拿起了其中一本。

### (sub) DIAL_Z23#91
- speaker=0  style=6
- effects:
    - advance in-game time by 1800
- text: 這是一本看起來相當嶄新的書,@3挑中了一本書名為《ñ貿ñ易ñ策ñ略ñ全書．第二卷》的書。書名下方,他注意到一張特別的字條黏在封面上:ñ珍稀孤本。  翻閱書頁時,迎面而來的是一張張表格與數字圖表,他猜這恐怕得花上好幾週才能弄懂,而他根本沒有時間可以浪費。不過,他總算在書的中段找到了一些有用的東西。  á…á…á聽á從á一á位á同á僚á的á建á議á,á我á決á定á在á此á列á舉á幾á間á王á國á境á內á最á出á色á的á商á店á範á例á,á這á些á例á子á能á優á雅á地á印á證á我...

### (sub) DIAL_Z23#93
- speaker=0  style=6
- effects:
    - advance in-game time by 450
- text: 他一翻開,就發現這只是一本簡單的帳冊,裡頭滿滿都是一排排的數字,他用手指劃過欄位時,心算起來怎麼也對不上。他啪地一聲闔上書,放回了架上。

## node 2300033  (DIAL_Z23#94)
- speaker=0  style=6  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 架上滿滿都是治療者的日誌手記。  這是薩斯令人歎為觀止的藏書中份量最龐大的一區,@4不禁有些卻步。不確定哪個書名或哪位作者對他最有用,他隨手抽了一本,開始讀了起來。

### (sub) DIAL_Z23#95
- speaker=0  style=6
- effects:
    - advance in-game time by 1350
- text: 跳過一段篇幅不短、討論各種藥草功效的內容後,他找到了一份列著幾種相當冷僻的藥水及其效果的清單,大多是他聞所未聞的東西。不過,清單上有一項倒是他過去在許多場合都用過的熟悉藥水。  á回á復á藥á水á總á覽á…á…á…á…á…á…á…á á á一á般á說á來á,á這á類á藥á水á的á用á法á,á在á群á島á王á國á的á尋á常á百á姓á間á早á已á廣á為á人á知á,á但á鮮á少á有á人á明á白á,á這á些á配á方á其á實á還á能á加á速á瀕á死á重á傷á者á的á癒á合á過á程á…á...

### (sub) DIAL_Z23#96
- speaker=0  style=6
- effects:
    - advance in-game time by 5400
- text: 很快地,他便被這本書吸引住了——這顯然是一本日誌,作者是一位曾隨波爾登某支較大規模的軍隊出征的治療者。雖然書裡實際上很少談到治療的具體作法,倒也記了幾則有用的資訊。  á…á…á相á較á之á下á,á草á藥á敷á劑á似á乎á能á帶á來á更á顯á著á的á療á效á,á但á也á僅á限á於á傷á者á能á爭á取á到á較á長á的á休á養á時á日á時á才á管á用á。á然á而á,á我á遇á到á的á病á患á大á多á已á瀕á臨á死á亡á邊á緣á,á更á需á要á回á復á藥á水á那á種á立á竿á見á影...

### (sub) DIAL_Z23#97
- speaker=0  style=6
- effects:
    - advance in-game time by 1350
- text: 這本書與其說是別的,不如說更像一本居家偏方與民俗療法的合集,書裡的內容他大多早有耳聞。實際來說,唯一稱得上有用的建議,就是生病時最好睡在旅店的室內,而不是硬撐著睡在冰冷堅硬的地上。

### (sub) DIAL_Z23#98
- speaker=0  style=6
- effects:
    - advance in-game time by 1350
- text: 這本書格外引人注意,因為它確實是在薩斯的高牆之內寫成的,內容設計成一本簡明手冊,教導讀者如何處置命危的傷患。  á應á盡á速á將á傷á者á送á往á旅á店á或á其á他á能á讓á其á安á睡á一á夜á、á避á開á夜á間á濕á寒á之á氣á的á地á方á。á安á頓á妥á當á後á,á建á議á施á以á四á劑á回á復á藥á水á與á一á次á草á藥á治á療á。á只á要á能á讓á傷á者á靜á養á三á日á不á受á打á擾á,á便á有á相á當á的á把á握á能á讓á他á從á「á瀕á死á」á的á狀á態á中á恢...

### (sub) DIAL_Z23#99
- speaker=0  style=6
- effects:
    - advance in-game time by 1350
- text: 這是架上最新的一本書,內容只探討一種新型解毒劑的施用方法,是由克朗多的納森神父所研發。  á…á…á緊á接á在á亞á魯á莎á．á康á多á因á登á基á為á克á朗á多á親á王á後á不á久á發á生á的á那á樁á不á幸á事á件á。á可á惜á的á是á,á自á那á時á起á,á邊á境á的á男á爵á們á便á屢á屢á發á現á這á種á毒á藥á被á大á量á使á用á,á如á今á更á是á在á莫á拉á埃á林á海á岸á及á北á境á各á地á大á規á模á採á收á提á煉á。á若á要á說á這á其á中á有á什á麼á...

### (sub) DIAL_Z23#100
- speaker=0  style=6
- effects:
    - advance in-game time by 1350
- text: 可惜他挑的這本書內容大多混亂又前後矛盾,他掙扎了將近半個鐘頭,最後還是放棄了,把書放回原處。  「ñ下一本……」他心想。

## node 2300034  (DIAL_Z23#101)
- speaker=0  style=0
- effects:
    - SET flag 0x1fcc=1
- branches:
    - [flag 0x1fc1 in [31917..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z23#102
- speaker=0  style=6
- effects:
    - SET flag 0x1fc1=1
- text: @4取下了一本書。  「有什麼有趣的東西嗎?」@5問道,從他肩後探頭張望。  @4指著書背上的字。「這是帕格寫的一本手記——書名叫《論馬克羅斯提出的跨空間裂界門理論》。」  「你認為這就是我們要找的書嗎?」  @4只是聳了聳肩回應,開始翻閱書頁,很快就發現這大部分是一份技術性文件,裡頭滿是圖表與成排的數字,旁邊還寫著古怪的簡寫註記。不管這本書講的是什麼,都遠比他目前讀過的任何魔法書籍都要進階高深。  「他乾脆用凱許語寫算了,」@4搖著頭說道。他在找索引時,發現了一則簡短的附註...

## node 2300035  (DIAL_Z23#104)
- speaker=0  style=6  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: @5微微一笑。  很高興能在這座地窖裡找到符合自己興趣的東西,他翻閱起一本似乎跟戰鬥技巧有關的書。

### (sub) DIAL_Z23#105
- speaker=0  style=6
- effects:
    - advance in-game time by 7200
- text: 這本書一開始像是普通的士兵手冊,看起來沒什麼值得一讀的內容,但就在他準備闔上書之際,卻在最後一章意外挖到了一座知識寶庫。  á這á最á後á一á章á,á是á特á別á為á那á些á做á足á準á備á、á也á熟á悉á戰á場á上á將á要á面á對á之á敵á的á士á兵á所á寫á。á只á要á在á開á戰á前á掌á握á足á夠á的á情á報á,á即á使á敵á人á佔á了á出á其á不á意á的á優á勢á,á只á要á你á了á解á他á們á天á生á的á弱á點á,á依á然á完á全á有á機á會á將á其á擊á敗á。á善...

### (sub) DIAL_Z23#106
- speaker=0  style=6
- effects:
    - advance in-game time by 5400
- text: 這本書出自一位法師之手,書中談到各種戰術理論時顯得有些頭腦混亂,過度仰賴間諜蒐集來的情報,或是某些寫在紙上好看、實戰中卻很少奏效的陣形。夾雜在一大段關於魔法強化攻城器械與戰場強化手段的冗長討論之間,他總算找到一段能轉述給@3聽的有用片段。  á有á一á招á相á當á簡á單á的á戰á術á,á最á早á是á在á卡á斯á對á抗á哥á布á林á的á那á場á戰á役á中á使á用á的á,á靠á的á是á一á道á有á時á被á稱á為á「á邀á請á術á」á的á法á術á。á研á習á法á術á的á法á師á們á...

### (sub) DIAL_Z23#107
- speaker=0  style=6
- effects:
    - advance in-game time by 3600
- text: 這本書內容相當專精,講的是敵人動用各種投射或魔法戰術時的應對之道。雖然他能理解大部分的概念,卻也明白要練到能純熟運用其中較高深的技巧,得花上好幾個月的功夫。到頭來,最實用的資訊竟是書中開頭的短短幾行。  á只á要á條á件á允á許á,á最á好á是á在á你á自á己á挑á選á的á戰á場á上á與á敵á人á交á鋒á,á確á保á你á握á有á出á其á不á意á的á優á勢á,á並á掌á控á任á何á可á能á扭á轉á戰á局á的á關á鍵á地á物á。á然á而á,á要á是á對á手á擅á長á魔á法á或á投...
