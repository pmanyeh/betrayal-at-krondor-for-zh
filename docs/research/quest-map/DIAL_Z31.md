# DIAL_Z31

595 records, 248 keyed nodes

## node 3100272  (DIAL_Z31#0)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#1
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [2679..0]] -> node 4294901761
    - [flag 0x0101 in [2564..0]] -> node 4294901761
- text: 酒館老闆在門口迎接了他們。  領著他們走進一片桌椅之間，他拿出一疊墨跡未乾、寫滿各式餐點飲品名稱的紙頁，最上頭還寫著酒館的名號——「ñ翡ñ翠ñ貓ð」。  「挺講究吧？」酒館老闆語帶得意地說道。「聽說這玩意兒就快在各家酒館客棧裡蔚為風潮了。我記得這東西叫做ñ菜單ð。可惜這陣子上頭列的東西我都還備不齊。兩位大爺，要不要先來點吃的墊墊肚子？」

### (sub) DIAL_Z31#2
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 酒館老闆微微一笑：「反正今天也沒什麼像樣的東西好吃。祝兩位順心。」

## node 3100273  (DIAL_Z31#4)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100274  (DIAL_Z31#5)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1e79 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#6
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1e79=1
- text: @4敲了敲那間小木屋的門，接著耐心等候有人應門。幾秒鐘後，一名婦人現身，領著他們進屋。「兩位大爺，除非真有要緊事，不然我實在抽不出空聊天。我還得趕完幫凱吉斯店老闆採的蘑菇——他昨天治療藥水差點就用罄了，你們也知道那句老話：『你能要我的命，卻吃不了我的肉。』」  「這說法真古怪，」@0說。「是什麼意思？」  「老實說，我也不知道，」婦人咧嘴一笑，臉上頓時亮了起來。「這是凱文男爵以前常掛在嘴邊的話。我從沒弄懂過。兩位大爺，恕我失陪，我真得繼續趕路了。」

## node 3100275  (DIAL_Z31#7)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1e7a in [3637..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#8
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: @4用力搥了搥門。  沒有人應聲。  眼看那醉漢是不打算堂堂正正出來理論了，他聳聳肩，轉身離開。「看來他是不會來開門了，」他說著，摸了摸頭上還隱隱作痛的地方。「我們走吧。」

### (sub) DIAL_Z31#9
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 0
    - (on-exit) play sfx 0
    - SET flag 0x1e7a=1
    - DAMAGE Health+Stamina of member#4 by -2560..-768
- text: 門猛地被推開。  一名四十來歲、雙眼惺忪、渾身酒氣的男子朝他們冷笑。「哼，你們想幹嘛？」他吼道。「有話就說！」  「我們是想向您打聽點路。」  「打聽路？打聽路？！」男子雙眼冒火，一把從地上抓起一只酒瓶。「我這就『指』給你們看！」  @4還沒反應過來，就感覺到酒瓶重重砸在自己的腦門上……

## node 3100277  (DIAL_Z31#10)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100278  (DIAL_Z31#11)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100279  (DIAL_Z31#12)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1e7b in [4502..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#13
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
- text: @4敲了敲窗玻璃。  「她沒回應，」他說。

### (sub) DIAL_Z31#14
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1e7b=1
    - SET flag 0x0003=1
    - GIVE gold +100
- branches:
    - [always] -> node 0 (no jump)
- text: @4敲了敲那間小屋的門，過了幾分鐘，一名怒氣沖沖的婦人出現在窗邊，開始對著他們破口大罵……

### (sub) DIAL_Z31#15
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你那該死的金幣自己留著吧！我已經決定了——我不走。

### (sub) DIAL_Z31#16
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們為什麼會希望你離開？

## node 3100280  (DIAL_Z31#18)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1e7c in [5020..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#19
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4微微一笑。  「盧肯把門鎖上了，」他說。「這也怪不得他。」

### (sub) DIAL_Z31#20
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [5293..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#22
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1a52=1
    - SET flag 0x1e7c=1
- branches:
    - [flag 0x0100 in [6272..0]] -> node 4294901761
    - [flag 0x0101 in [7156..0]] -> node 4294901761
- text: 一名男子邀請他們進屋。  「請進，請進。我叫盧肯，」他一邊自我介紹，一邊拍了拍客人的肩膀。「幸會幸會。我已經好一陣子沒有訪客了。你們知道嘛，住在這種地方挺孤單的，孩子們也不常下山來看我。兩位有孩子嗎？他們啊，真是奇妙的小傢伙，而且……」  @4猛地抓住盧肯的手腕，狠狠一擰，逼得他痛得手指一鬆，一枚閃亮的金幣應聲落地。眾人震驚地看著那枚金幣噹啷滾落在地上，一時鴉雀無聲。  「你從我錢包裡摸走這個的時候，我差點都沒察覺，」@4說。「你這小偷手腳不差，可惜還不夠好。」  「別殺我，...

### (sub) DIAL_Z31#23
- speaker=0  style=6
- effects:
    - RAISE Lockpick of party by 1280
    - advance in-game time by 10800
- text: @4挑了挑眉。  「好吧，盧肯，」他說。「你可以教我們，但要是我們出去時身上的東西比進來時還少……」  「不會不會，絕對不會。我向你保證。你們先坐一下，我馬上回來，去把我練習用的鎖拿來，馬上回來。」  「想得美，不行。你留在這裡。」@4把盧肯按回座位上。「只要告訴@5練習鎖放在哪，讓他去拿就行了。然後我們就開始上課……」  盧肯認清自己逃不掉了，於是花了大半天的時間講解示範，最後才把練習鎖收起來。  「就這樣了，」他嘟囔著，抹去額頭上的汗水。「我懂的全都教完了。」  「這樣就...

## node 3100281  (DIAL_Z31#25)
- speaker=0  style=0
- branches:
    - [flag 0x1e7d in [7420..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#26
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: 沒有人應門。  @4聳聳肩。「看來他沒興趣再談那些卷軸的事了。真不知道那塊告示牌是怎麼回事。」

### (sub) DIAL_Z31#27
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 0
    - SET flag 0x1e7d=1
    - SET flag 0x0004=1
- text: 門開了一條縫。  「手伸出來，」一個聲音下令道。  「你說什麼？再說一遍？」@4問道。  「把你的手伸出來，」那聲音又從黑暗中重複了一遍。「手心朝上，大拇指張開。別輕舉妄動。」  @4覺得有點好笑，還是照做了，伸出雙手讓這名陌生人檢查。對方一聲令下，他又把手翻過來，靜候屋內那個聲音的裁決。  「你過關了，」屋裡的聲音終於開口，語氣卻聽不出半點如釋重負。「好，仔細聽著，別多問。」  「剛才驗手是怎麼回事？」  「我說了別多問，」那聲音厲聲喝道。「這麼說吧，我知道我可以信任你——...

## node 3100282  (DIAL_Z31#28)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4推開了門。  「看起來像是間廢棄的酒館，」@5環顧房間說道。「說不定前任屋主留下了什麼能用的東西。」

## node 3100283  (DIAL_Z31#29)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x9c42 in [8879..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#30
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [9413..0]] -> node 4294901761
    - [flag 0x0101 in [9273..0]] -> node 4294901761
- text: 米歇爾領著他們進屋。  屋子雖小，卻布置得十分雅緻，對一個看似平民的人來說，家具品味相當不俗。  「你們需要我的服務，」她開口道。「你們病了。」  @4在椅子上動了動身子。「妳說得倒是挺篤定……」  「你們身上有病徵。我可以治好你們，但需要報酬。二十五枚金幣。你們付得起嗎？」

### (sub) DIAL_Z31#32
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [9647..0]] -> node 4294901785
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#34
- speaker=0  style=6
- effects:
    - TAKE gold -250
    - apply status/condition to party idx=1 amt=-100
- text: 錢貨兩訖。  「很好，」她從@4手中接過錢，說道。「躺下休息片刻，我這就替你們治療。」  她打開一小瓶透明液體的塞子，讓病人一一嗅過，再分別在每個人頭上輕拍一下。「你們都治好了。可以走了。」

## node 3100284  (DIAL_Z31#35)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100285  (DIAL_Z31#37)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f8b in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#38
- speaker=0  style=6
- effects:
    - SET flag 0x1f8b=1
- text: 這戶人家的主人很健談。  @4小心翼翼不透露他們此行的細節，把話題引到鎮上的居民身上。「這裡的人都是好人，除了那個女巫醫米歇爾。希望你們沒打算去找她。」  「為什麼？」@4問道。  「她是條毒蛇，」男子說。「她跟我說我快死了，可你猜怎麼著？我後來好了。是啦，我難受了三四天，還以為自己真要死了，結果沒事，活得好好的。跟你們說，我看她跟『蒼白』歐諾八成有什麼勾當。他負責散播某種瘟疫，她再開些假藥來『治療』。真是缺德。」

## node 3100286  (DIAL_Z31#39)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100287  (DIAL_Z31#40)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#41
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [11664..0]] -> node 4294901761
    - [flag 0x0101 in [11186..0]] -> node 4294901761
- text: 他們走進一間歡樂的大廳。  彷彿是從地板裡冒出來似的，一名中年男子突然現身，領著他們到一張靠近熊熊爐火的桌邊坐下。  「傑佛瑞，這間酒館的老闆，」他笑容可掬地說道。「今天要不要嚐點吃的？」

### (sub) DIAL_Z31#42
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 酒館老闆聳聳肩。  他在桌邊坐下加入他們，眾人談笑風生地打鬧了將近一個鐘頭，其他客人才陸續上門。  「……結果打開一看，裡頭竟然是四隻雞！」傑佛瑞說完放聲大笑，拍了拍桌子起身，朝門口走去。「我不是要趕人，只是店裡客滿桌少，若不介意的話……」  「當然不介意，」@4微笑道。「我們反正也該上路了。」

## node 3100288  (DIAL_Z31#44)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100289  (DIAL_Z31#45)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [flag 0x1e7e in [12543..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#46
- speaker=0  style=6
- effects:
    - SET flag 0x1e7e=1
- text: 一名男子踉踉蹌蹌地走了出來。  「我是莫瑞……鎮上的葬儀人……哪個傢伙翹辮子了？」他問道，隨即改口：「我是說……哪位往生了？」  「聽你這口氣，倒不太像相信死後有來生的人。」  「墳場裡唯一還算熱鬧的事，都是活人搞出來的，」他呵呵一笑。「就上個月，我還跟拉姆特那邊看墳場的挖墳人聊過。他說有人跑進他的墳場裡，挖了座新墳！墓碑底下埋的是誰，他自己都不知道。」  「他怎麼不乾脆挖開來看看？」@4問道。  他敲了敲自己的腦袋。「他怕會招來鬼魂。要我說，全是些裝神弄鬼的無稽之談。死了就...

### (sub) DIAL_Z31#47
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: 沒有人應門。  「他大概是醉倒在裡頭了，」@4想起那人先前的模樣，說道。「就讓他睡吧。」

## node 3100290  (DIAL_Z31#48)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f94 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#49
- speaker=0  style=6
- effects:
    - SET flag 0x1f94=1
- text: 一名婦人正要出門。  「我實在沒空聊，」她一邊繫上圍裙一邊說。「我丈夫伊森又出門幫『三丘人』撿破爛去了，我得幫他看店。他每次回來總是滿懷抱著別人弄丟或隨手丟掉的東西。有空再來坐坐！」  沒過多久，她便匆匆離去，消失在視線之外。

## node 3100291  (DIAL_Z31#50)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4推開了門。  「這裡沒人住了，」@4環顧房間說道。「說不定原本住這裡的人留下了什麼能用的東西。」

## node 3100292  (DIAL_Z31#51)
- speaker=3  style=0
- text: 這絕對不是個好主意。這是我姑姑家。雖然我也很想找機會解釋一下自己為什麼會跟莫瑞德人一起旅行，但我想我們還是離開比較好。

## node 3100293  (DIAL_Z31#52)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4緊張地四下張望，這時@0正敲著門。  「看來沒人在，」他說。「算我們走運。」

## node 3100294  (DIAL_Z31#53)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f7b in [14358..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#54
- speaker=0  style=6
- effects:
    - play sfx 0
    - SET flag 0x1f7b=1
- text: @5指了指那間屋子。  「我不知道，」@3回答了那個沒人問出口的問題。「我只知道那不是親戚家……」  「這樣就夠了，」@5說。他轉身大步走向門口，輕輕敲了敲門，@3則留意著街上的動靜。  過了片刻，一名衣衫不整的男子應門。他們聊了一會兒，得知這名男子昨晚大半夜都在試圖闖進一間最近倒閉的洗衣店。  「老闆關店的時候，一直沒把我送洗的一套盔甲還給我。你們要是進得去，那套盔甲就歸你們了。我累壞了，容我先去睡了。」

### (sub) DIAL_Z31#55
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4敲了敲門。  「滾開！」屋裡傳來一聲怒吼。「我要睡覺！」  @4本想再敲一次，但轉念一想，還是決定他們該離開了。

## node 3100295  (DIAL_Z31#56)
- speaker=0  style=0
- text: 鎖被順利撬開後，@4推開門走進這棟小屋。  「看起來這裡以前是間洗衣店，不過顯然已經倒閉了，」他說。「我們四處看看吧。」

## node 3100296  (DIAL_Z31#57)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100297  (DIAL_Z31#58)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [flag 0x9c44 in [15999..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#59
- speaker=0  style=0
- effects:
    - (on-exit) play sfx 0
- branches:
    - [flag 0x1e7f in [15874..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#60
- speaker=0  style=6  flags=reload-scr-between-pages
- effects:
    - SET flag 0x1e7f=1
- text: @4倒抽了一口氣。  眼前灰濛濛的空間裡，斷頭在空中打轉，殘肢斷臂胡亂揮舞，發出一陣好似……廚房餐具碰撞般的聲響？湊近一看，他才發現那些「肢體」其實根本不是屍塊，而是一堆鏽跡斑斑、吊掛在店舖屋梁上的破舊盔甲零件。  「喂，你們小心點！這些東西可能會整個砸到咱們頭上！」一名矮小的男子從店舖後方走出來，手指間還緊緊夾著一根火柴。「早該先敲個門的。我在樓上差點沒聽見你們進來——不過我看得出你們為什麼會上門。你們這身盔甲的狀況可不太妙。再挨一下，你們就會變得跟上頭那堆東西一樣了。我這...

### (sub) DIAL_Z31#62
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 屋裡傳出一個聲音朝他們吼道。  「滾開！我現在忙得很，非常忙！」  @4上前一步，清了清喉嚨：「我們只是想聊聊……」  「你耳朵裡塞了蠟嗎？我說了我很忙！要修盔甲的話可以留著過幾天再來——現在請你們滾開！」  「既然我們的盔甲都完好無損，那就不打擾了，」@4說著轉身離去。

## node 3100298  (DIAL_Z31#63)
- speaker=0  style=0
- branches:
    - [flag 0x1f82 in [17165..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#64
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f82=1
- branches:
    - [always] -> node 0 (no jump)
- text: 敲門沒人應答，他們便湊近一扇沾滿灰燼的窗玻璃朝小屋裡窺看。  屋內的泥地上散落著森森白骨，宛如被遺忘的玩具——彷彿是某位早已瘋狂的死神隨手丟棄的玩物。遠處牆邊，一顆顆空洞的頭骨雜亂堆疊，毫無章法可言。

### (sub) DIAL_Z31#65
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是什麼地方？

### (sub) DIAL_Z31#66
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是座停骸所。墳場放滿了，得空出地方給新的屍體，舊的骸骨就搬來這裡堆放。我們進去看看吧。

## node 3100299  (DIAL_Z31#69)
- speaker=0  style=0
- text: 花了好一番工夫，才讓大家重新站穩腳跟。  「看看屋裡有沒有留下什麼東西，」@4說。

## node 3100300  (DIAL_Z31#70)
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#71
- speaker=0  style=6
- effects:
    - play sfx 0
    - apply status/condition to party idx=1 amt=21
- text: 門把上掛著一張紙條。  「無論如何，旅人們務必避免接觸歐諾——人稱『蒼白』歐諾，」@0唸出聲來。「一種來歷不明的瘟疫已經讓三人病倒。請務必避免接觸……」  門猛地打開。  「……他。」@0這才把話說完，只見一名二十來歲、面容憔悴的男子出現在門口，臉上摀著一條沾血的手帕。「你就是歐諾？」  「沒——錯，」他隔著手帕喘著氣說。「你……你正站在……我家門前。快滾，免——免得你們也染上。」  「你到底得了什麼病？」  男子搖了搖頭。「不知道，郎中不知道，神父也不知道。沒人知道。唯一活...

## node 3100301  (DIAL_Z31#72)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#73
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
- text: 一個三百磅重的瘋子應了門。  「哼，」那滿身油污的農夫自言自語道，上下打量了@4一眼。「早該猜到這是哪個外地人搞的鬼。」  「搞什麼鬼？」@4追問道。  「別裝傻了！這十個晚上你們一直在西邊搞那些……乒乒乓乓的動靜，害我睡不著！」  @4搖了搖頭。「恐怕是誤會一場。真的。我們這就不打擾您了。」

## node 3100368  (DIAL_Z31#74)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1fd2 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#75
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [19603..0]] -> node 4294901761
    - [flag 0x0101 in [20187..0]] -> node 4294901761
- text: @4猶豫了一下。  他注意到門楣上方精雕細琢的招牌，唸出聲來——「á戴á維á奧á特á．á陶á特á姆á—á—á博á學á多á聞á、á凡á事á可á垂á詢á請á教」  「還不只如此，」一個渾厚的聲音答道。「史學家、哲學家、數學家，什麼我都懂一點。」那位文士從屋簷下走出來，意味深長地看了@5一眼，繼續說道。「我目前正在研究戰術兵法，也許你們會有興趣幫忙。」  「那我們能得到什麼好處？」@3輕聲問道。    「情報，」文士答道。「你們說一個鐘頭，接著換我說一個鐘頭。題目隨你們挑。有興趣嗎...

### (sub) DIAL_Z31#76
- speaker=0  style=6
- effects:
    - SET flag 0x1fd2=1
    - RAISE Scouting of party by 1792..2304
- text: 文士靜靜聆聽。  等到@5終於說得口乾舌燥，他便反問對方對王國境內活動的刺客了解多少，接著把自己所知的一切娓娓道來。  「大概就是這些了，」文士說完，雙手交疊放在膝上。「有幫助嗎？」  「比你想的還有用，」@4說。「我想我們現在更懂得如何提防埋伏了。不過也該上路了。」  文士點點頭。「我也有事要忙。有個助手不知出了什麼事，我可能得離開一陣子。旅途平安。」

## node 3100303  (DIAL_Z31#78)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這棟建築物發出令@4心生不安的嘎吱聲響。  「你留在外面，」他對@0說。「這地方感覺不太對勁。我進去看看。」一分鐘後他回來時，臉色十分凝重。

### (sub) DIAL_Z31#79
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你發現了什麼？

## node 3100304  (DIAL_Z31#81)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4敲了敲門。  他靠在門框上等了好一會兒，側耳留意屋裡是否有動靜。眼看確實沒人要來應門，他聳聳肩，後退了幾步。  「看來沒人在，」@4說。

## node 3100331  (DIAL_Z31#82)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - END conversation, result=65535
- text: @4敲了半天門，卻沒人應答。  他繞著屋子走了一圈，宣布道：「不是屋裡的人溜出去了，就是他們存心不理我們，要不然就是睡得跟死人一樣沉。不管是哪種情況，我看我們還是繼續趕路比較划算。」

## node 3100332  (DIAL_Z31#83)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 店舖打烊了。  「他們明天總得回來開店做生意吧，」@4無奈地說。「我們只好趕在日落前再來堵他們了。」

## node 3100361  (DIAL_Z31#84)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - play sfx 0
- text: 門鈴響了一聲。  @4才剛把門推開，店老闆已經迎上前來領他進屋……

## node 3100333  (DIAL_Z31#85)
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - END conversation, result=65535
- text: @4敲了敲酒館的門。  眼看沒人要來應門，@4聳聳肩。「看來平民百姓對亞魯莎親王的法令倒是奉行得很徹底。這裡的門只在正午到午夜之間開放，」他嘆了口氣說。「不過我猜總得有人確保農夫不會該下田時還在喝酒。有時候他還真是把日子過得一點ó樂趣都不剩……」

## node 3100362  (DIAL_Z31#86)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: @4嗅了嗅鼻子。  才剛踏進酒館門口，他就聞到一股熟悉卻淡淡的鹼皂氣味，還有底下那股本該被蓋過去、更為刺鼻的味道。畢竟客人喝得酩酊大醉的地方，哪個精明的老闆不會隨時備著個打掃的小廝呢……

## node 3100363  (DIAL_Z31#87)
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - ?wOp12 a1=0 a2=0
- text: @4推開了門。  穿門而過時，他注意到門上沒有門閂，這多半表示這間客棧是由當地領主特許經營，用以保障旅人的安全。但願這也意味著客棧裡的陳設同樣可堪一用……

## node 3100334  (DIAL_Z31#88)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 神殿的大門緊閉著。  @4退開幾步，聳聳肩。「我想神職人員偶爾也是要睡覺的，」他說。「看來我們得等到早上才能見到任何人了。」

## node 3100364  (DIAL_Z31#89)
- speaker=0  style=0
- text: 香煙裊裊繚繞。  @4邁步穿過神殿的廊柱，走向那扇厚重的木門——大門緊閉，既擋住了日光，也維護著殿內進行中儀式的隱私。他拉了拉門邊垂掛的流蘇繩索，靜候守門人回應……

## node 3100335  (DIAL_Z31#90)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 大門紋風不動。  「他們晚上關門了，」@4說。「我們走吧。」

## node 3100336  (DIAL_Z31#91)
- speaker=0  style=0
- text: 他們受到熱情款待。  一番閒聊、喝了幾口麥酒之後，他們婉拒了主人進一步的招待。「您真是太客氣了，」@4一邊說一邊拿起行囊。「我看我們該重新上路了。」

## node 3100311  (DIAL_Z31#92)
- speaker=0  style=0
- text: 一名婦人領著他們進屋。  一番閒聊、喝了一壺熱茶之後，他們婉拒了女主人進一步的招待。「真希望能多陪您坐坐，」@4說，「不過正事要緊。我們……還有支商隊在等著我們呢。」

## node 3100312  (DIAL_Z31#93)
- speaker=0  style=0
- text: 門依然閂著。  「我有種不受歡迎的感覺，」@4說，嘴角泛起一絲淺笑。「不過話說回來，我想起我們好像做了什麼事惹惱了這裡的住戶。」

## node 3100365  (DIAL_Z31#94)
- speaker=0  style=0
- text: 門依然緊閉。  「滾開，」屋裡傳來一聲怒吼。「別來煩我。」  @4聳聳肩，示意大家可以走了。

## node 3100349  (DIAL_Z31#95)
- speaker=0  style=6
- text: @4搖了搖頭。  「抱歉，」他說。「我們現在幫不上忙。」  婦人咬了咬下唇，「好吧，不過如果你們改變主意，歡迎再回來。」

## node 3100350  (DIAL_Z31#96)
- speaker=0  style=6
- text: @4搖了搖頭。  「抱歉，」他說。「我們現在幫不上忙。」  男子嘆了口氣，「好吧，不過如果你們改變主意，歡迎再回來。」

## node 3100313  (DIAL_Z31#97)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100314  (DIAL_Z31#98)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100002  (DIAL_Z31#99)
- speaker=0  style=0
- text: 這棟搖搖欲墜的農舍，想必曾經住過一戶小小的人家。如今卻已淪為廢墟，或許是地力耗盡，又或許是幾十年前的一場旱災所致。  「這裡什麼都找不到，」@4說。「我們走吧。」

## node 3100003  (DIAL_Z31#100)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ede in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#101
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1ede=1
- branches:
    - [flag 0x0100 in [25904..0]] -> node 4294901761
    - [flag 0x0101 in [25815..0]] -> node 4294901761
- text: 「請進！請進！」一名穿著鮮豔圍裙、彬彬有禮的年輕婦人喊道，替他們撐開了小屋的門。  一名年輕男子跪在石砌壁爐前，正往劈啪作響的爐火裡添幾根小柴。他抬頭微笑道：「當然歡迎！我們才剛吃完飯，不過今天運氣好釣了不少魚，還夠分給大家吃。」  @4的鼻子動了動，聞著空氣中還殘留的烤海鱸魚與新鮮麵包香氣，忍不住有些心動。「這提議真誘人，不過恐怕我們得趕路了，」他說。「討口清水喝就夠了。」  「那是自然。不過要不要帶點乾糧上路？我可以讓蘿拉琳幫你們每人準備一小份——至少夠撐個兩天。她的手藝...

### (sub) DIAL_Z31#103
- speaker=0  style=6
- effects:
    - GIVE item 'H' cond=2 to party (cost 0)
- text: 年輕男子微笑著朝妻子招了招手。他走到她身邊幫忙準備乾糧，中途還停下來，煞有介事地比手劃腳，講了一段還算逼真的「差點就釣到大魚」的故事。  備妥之後，他們把幾份包好的乾糧遞給@4，他欣然收下。「你們真是太客氣了，」他說。

## node 3100004  (DIAL_Z31#104)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f84 in [20144..32815]] -> node 4294901761
    - [flag 0x1f86 in [28206..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#105
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f86=1
- branches:
    - [flag 0x0100 in [27121..0]] -> node 4294901761
    - [flag 0x0101 in [26958..0]] -> node 4294901761
- text: @4大聲敲了敲門。  不一會兒，一名衣著考究的男子前來應門，一邊說話一邊用絲質手帕拭去額頭的汗水：「今天天氣真不錯，是吧？我是塔德．奎斯托。兩位是來上課的嗎？」他挑起眉毛，滿懷期待。  「上課？」@4問道。  男子隨即轉身進屋，拿了一把鈍頭的花劍出來。「兩位是來學習劍術精髓的嗎？」他問道，話音未落便耍了幾個漂亮的招式。「我可以給你們上一堂速成課，只要七十五枚金幣。怎麼樣？」

### (sub) DIAL_Z31#106
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 0
- text: 「唉，好吧。那就下次有機會再說了，」他說。「容我先失陪，還得準備上課。」說完他二話不說便把門關上。

### (sub) DIAL_Z31#107
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [27150..0]] -> node 4294901835
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#108
- speaker=0  style=6
- effects:
    - advance in-game time by 3600
    - SET flag 0x1f84=1
    - TAKE gold -750
    - RAISE Melee Acc of party by 1280
- text: 「太好了！哦，你們願意接受我的提議，真是讓我太高興了，」他興奮地說。  @5跟著塔德走進這間小屋，心裡不免有些懷疑對方的真本事——畢竟這隻昂首闊步的孔雀，看起來這輩子大概沒真正打過架。  然而塔德領著他們鑽研劍術要訣，疑慮很快便一掃而空。儘管他實戰經驗或許不多，眾人卻都看得出他確實是箇中高手。他甚至還能給@3一些關於徒手近戰時如何運用木杖的指點。  這堂課上了好幾個鐘頭，結束時大家都累壞了，但都認為這筆錢花得值得。

### (sub) DIAL_Z31#110
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [27121..0]] -> node 4294901761
    - [flag 0x0101 in [26958..0]] -> node 4294901761
- text: @4敲了敲塔德家的門。  他笑臉相迎。「歡迎回來。是為了上課的事嗎？」

## node 3100005  (DIAL_Z31#111)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1edf in [20112..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#112
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - (on-exit) play sfx 0
    - SET flag 0x1edf=1
- text: 屋裡傳出一陣騷動。  過了一會兒，一名十三歲上下、體格結實的男孩把門大大推開。「你們要是找我哥哥，他現在不在家。」  「其實不是找他，」@4答道。「你父母在家嗎？」  男孩頓了一下才開口。「我爹娘一年前被殺了。我跟米契幾個月前搬來這裡，跟塔德．奎斯托學劍。我們要找出殺他們的那些混帳強盜，把他們的心挖出來餵狗！」  @4本想勸他把這種事交給更年長、更有本事的人去做，但見男孩神情堅決，話到嘴邊還是嚥了回去。他改口問道：「塔德劍術很厲害嗎？」  「什麼，你開玩笑吧？他可是天下第一！...

## node 3100008  (DIAL_Z31#113)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee0 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#114
- speaker=0  style=6
- effects:
    - play sfx 0
    - (on-exit) play sfx 0
    - SET flag 0x1ee0=1
- text: 這棟房子年久失修。  深綠色的苔蘚爬滿了半扇門，前方木板上也有好幾大片。門緩緩開啟，@4的目光重新聚焦在門上。  一股濃重的霉臭味撲面而來，一名老婦人出現在門口。她披著一件破爛的披肩，一雙扭曲變形的腳上，兩隻鞋子還不成對。  「你是那些『陰影人』的一份子？我最恨那些陰影人了！」她嘶啞著嗓子說。  她臉上輕蔑的神情忽然轉為驚恐。「他們無所不在，你知道嗎！說不定這會兒就正從我的門縫溜進來！」這念頭顯然把她嚇壞了，她二話不說便閃身回屋，砰地一聲把門甩上。

## node 3100366  (DIAL_Z31#115)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x27 mask=0x4e mode=47 chapters=8)] -> node 6160
    - [always] -> node 0 (no jump)

## node 3100012  (DIAL_Z31#116)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x27 mask=0x4e mode=47 chapters=8)] -> node 6160
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee1 in [30650..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#117
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
    - SET flag 0x1ee1=1
- text: @4站著一動不動，等候回應。幾秒後，一名體態豐腴的婦人來應門，一手還抱著個小孩，架在腰間。  「我丈夫還有雜務要忙。你們先去『陌生人』酒館等等，他忙完說不定會過去找你們。」  他還沒來得及回話，門就砰地一聲關上了。門的另一側，@4隱約聽見一名男子有氣無力地抗議：「可是奶油球，我真沒見過那些人啊。」緊接著是一聲悶響，然後一聲被摀住的驚叫，接著便是一片寂靜。

### (sub) DIAL_Z31#118
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100013  (DIAL_Z31#119)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x27 mask=0x4e mode=47 chapters=8)] -> node 6160
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee2 in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#120
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1ee2=1
- text: 門開了，@4一眼對上一名小男孩瞪得老大的雙眼。  「嗨，小傢伙。你媽媽是不是——」  一個新的身影出現在門口，是名年輕婦人。她向訪客們問好，並自我介紹，男孩則躲進她的裙擺後方。一番簡短卻沒什麼收穫的交談後，她給了他們一些水。  準備離開時，@0彎下腰揮手道別，男孩興奮地叫了一聲，隨即躲進屋裡不見了。

## node 3100016  (DIAL_Z31#121)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100017  (DIAL_Z31#122)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee3 in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#123
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1ee3=1
- branches:
    - [flag 0x0100 in [31709..0]] -> node 4294901761
    - [flag 0x0101 in [31617..0]] -> node 4294901761
- text: 這間小屋的主人，一位自稱「柯維」的農夫，邀請他們進屋。  他們閒聊了幾分鐘，話題天南地北，柯維的妻子則忙著張羅些東西讓他們帶著上路。  「要不要給幾位壯小伙子弄點吃的？」她問道。

### (sub) DIAL_Z31#125
- speaker=0  style=6
- effects:
    - GIVE item 'H' cond=2 to party (cost 0)
- text: 農夫微笑著朝妻子招了招手，走到她身邊幫忙準備乾糧。  備妥之後，他們把幾份包好的乾糧遞給@4，他欣然收下。「你們真是太客氣了，」他說。

## node 3100018  (DIAL_Z31#126)
- speaker=0  style=0
- branches:
    - [flag 0x1ee3 in [32380..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100024  (DIAL_Z31#129)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee4 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#130
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1ee4=1
- text: @4才剛敲門，屋裡立刻傳來一陣慌亂的騷動聲，接著歸於寂靜。他又敲了一次。還是沒動靜。  「哈囉？」一片死寂。「有人在嗎？我們只是疲憊的旅人，只想耽誤您一點時間，討口水喝而已。」@4耐心等了片刻，接著板起臉說：「聽著，我們知道你在裡面。剛才的動靜我們都聽見了。」  終於，隔著緊閉的門，一個男人有氣無力地應了聲：「我們知道你們是誰派來的。等我們湊到錢，欠的稅一定補齊。」  不管他們怎麼解釋澄清，都無法讓那人相信真相。門依然緊閉。

## node 3100025  (DIAL_Z31#131)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee5 in [33880..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#132
- speaker=0  style=6
- effects:
    - SET flag 0x1ee5=1
- text: 門吱呀一聲開了。  「日安，」一名二十五歲上下的婦人說道。「幾位大爺是什麼風把你們吹來萊頓的？」  @4瞥了@0一眼，接著實話實說：「只是路過而已。不知能否討口水喝？」  「城中心的路邊有口井，」她說。  @4察覺她大概對跟陌生男子交談有些戒心，便謝過她的指點，向她道別。

## node 3100026  (DIAL_Z31#134)
- speaker=0  style=0
- branches:
    - [flag 0x1ee6 in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#135
- speaker=0  style=6
- effects:
    - SET flag 0x1ee6=1
- text: @5正要敲前門，忽然聽見屋裡傳出一陣古怪的咆哮聲，持續了幾秒後停下，接著又響了起來。  「以伊夏神之名，這是——」@5側耳貼在門上聽了聽，忽然恍然大悟，微微一笑，轉身便走。  @3滿臉疑惑地看著他。「我們要走了？聽起來裡頭像是有頭野獸，說不定該進去看看有沒有人需要幫忙。」  「就算裡頭是帕格那樣的大法師，恐怕也治不好那種打呼聲。走吧，讓他好好睡吧。」

## node 3100027  (DIAL_Z31#136)
- speaker=0  style=0
- text: @4環顧這座小穀倉，看牲畜種類如此繁雜，猜想這大概是公用財產，說不定是萊頓鎮民共有的。  他四處翻找了幾分鐘，接著說：「這裡沒什麼值得留意的。我們走吧。」

## node 3100029  (DIAL_Z31#137)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100337  (DIAL_Z31#138)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100032  (DIAL_Z31#139)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#140
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [35753..0]] -> node 4294901761
    - [flag 0x0101 in [35636..0]] -> node 4294901761
- text: 屋主是名五十歲上下、蓄著鬍子的男子，顯然老遠就看見@4走近，門在他來得及敲門之前就先打開了。  「日安，大爺們！鄙人巴克．勞許。請問幾位怎麼稱呼？」  @4得體地做了自我介紹，男子熱情地朝他們微笑，接著說道：「這一季河裡的漁獲挺豐盛。幾位大爺要不要嚐嚐我曬的乾鱒魚？要不然買把我親手打的鏟子——或是一支火把也行？」

### (sub) DIAL_Z31#141
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「你們可不知道自己錯過了什麼，」男子說。「不過或許改天你們會再回來。」

## node 3100035  (DIAL_Z31#143)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ee8 in [33880..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#144
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1ee8=1
- text: 一名三十歲上下的美麗婦人應了@4的敲門聲。  她手裡拿著一本皮面書走到門口，@4越過她望進屋裡，看見四五個年齡不一的孩子。  「恐怕兩位大爺對我的課來說年紀太大了，」她說。  「呃……是啊……那好吧，我們就不打擾了。再會，女士。」  門關上後，@4轉頭對@0說：「別用那種眼神看我。老師總是讓我渾身不自在。」

## node 3100036  (DIAL_Z31#145)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1eea in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#146
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1eea=1
- text: @4站在木門前，忍不住多看了幾眼這棟房子的做工。跟同類房子相比，這棟顯然建得格外扎實，用料也十分講究。他敲了敲這扇結實的門。  片刻後，一名魁梧的男子出現在門口，一頭沙色的頭髮在微風中輕輕飄動。  「你們是為了房子的事來的嗎？沒人蓋得比我好！」他自豪地說。  @4後退了一步。「我們只是在欣賞您的手藝。做得真好。可惜我們只是路過而已。」  他們跟男子聊了幾分鐘，得知鎮子另一頭有座神殿，便告辭離去。

## node 3100038  (DIAL_Z31#147)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1eeb in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#148
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1eeb=1
- text: 小屋前門上掛著一塊字跡粗糙的招牌，寫著「二手雜貨大出清」。@4敲了敲門，等候有人應門。  一名高瘦、面色陰沉的男子現身，領著他們進屋。「兩位是來買東西的吧？」他咧著一口參差發黃的牙齒問道。  「那得看你賣的是什麼了，朋友，」@0答道。他們跟著男子走到一張大木桌前，桌上堆滿了十來樣物品，大多是些破爛雜物，但其中一樣吸引了@4的目光。「跟我說說這個東西吧。您是從哪弄來的？」他拿起一枚看起來被踩過不只一次的破損徽章，問道。  男子神色緊張地打量著他們。「就在這附近撿到的。你們要買嗎...

## node 3100039  (DIAL_Z31#149)
- speaker=0  style=0
- branches:
    - [flag 0x1eec in [19999..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#150
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
    - SET flag 0x1eec=1
    - DAMAGE Health+Stamina of member#0 by -3840
- text: 這棟房子顯然已無人居住。儘管如此，@4仍覺得敲個門比較保險。他指節才剛觸到木門，門便輕易地開了。  他眨了好幾下眼睛，才讓視線適應昏暗的光線。「看起來沒什麼特別的東——」  話音未落，一團瘦骨嶙峋的毛球突然從屋裡竄出，狠狠抓花了@0的臉。  「該死！」@4叫道。「這貓一定被困在裡頭好幾天了！」他喘了口氣，隨即過去查看@0的傷勢。

## node 3100040  (DIAL_Z31#151)
- speaker=0  style=6
- text: 這棟房子透著一股說不出的怪異。  @4也說不上是哪裡不對勁，但這棟屋子有種夢境般的氛圍。還是說，那其實是場惡夢？他幾乎記不得自己敲過門，只確定沒有人應答。

## node 3100041  (DIAL_Z31#152)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1eed in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#153
- speaker=0  style=6
- effects:
    - SET flag 0x1eed=1
- text: @3站在一扇雕工精緻的門前，上前一步。「這些是魔法符文，」這位法師說道，「顯然是用法術刻上去的……」  「不是，就是把普通的獵刀刻的。」  一個瘦小的老人身影從屋角繞了出來，聲音正是他發出的。「我剛才在後頭忙雜事。不過你說符文是魔法倒是說對了，是我自己刻上去的。在下弗拉爾．威根。」  @3很高興遇上另一位法師，微笑道：「用法術刻的話應該省事多了，弗拉爾。」  「我猜你說得沒錯。不過我可不是法師。有天賦的是我弟弟，他幾年前過世了。」老人凝視著門片沉默了片刻，忽然又振奮起來，說道...

## node 3100042  (DIAL_Z31#154)
- speaker=0  style=0
- branches:
    - [flag 0x1eed in [40653..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#155
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
- text: 這口井看起來很普通，卻總覺得有點不對勁……  @0湊近想仔細瞧瞧，忽然感覺一股強大的能量竄入體內，痛得他猛然彈開。  「看來，」@0揉著刺痛的肩膀說，「有人不希望我們太靠近這口井。或許我們該去跟那邊那戶人家談談。」

### (sub) DIAL_Z31#156
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [41268..0]] -> node 4294901761
    - [flag 0x0101 in [41050..0]] -> node 4294901761
- text: 「防護咒解除了，小夥子們。」弗拉爾雖自稱不是法師，卻總有本事神不知鬼不覺地冒出來。「這咒語得留著，不然野獸跟白吃白喝的傢伙就要上門了。」  他揮了幾下手，示意他們上前。「來吧，別怕。這口井裡的水能讓你們藥到病除……只要二十五枚金幣。要不要試試？」

### (sub) DIAL_Z31#158
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - RAISE Health+Stamina of party by 25600
- text: 這治療之水顯然開始發揮效果了。  弗拉爾湊近了些。「感覺挺不錯吧？很快就能活蹦亂跳了。謝謝你們的惠顧，小夥子們。」  他揮了揮那雙滿是老繭的手，便轉身走回屋裡。

## node 3100044  (DIAL_Z31#159)
- speaker=0  style=0
- branches:
    - [flag 0x1eef in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 門上掛著一條黑色緞帶。  @4後退一步，皺著眉盯著那條緞帶，似乎在思考該怎麼做才好……

### (sub) DIAL_Z31#160
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你幹嘛用那種眼神看這棟房子？那條黑緞帶是什麼意思？

### (sub) DIAL_Z31#161
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這條緞帶是『瘟病』的標記——說白了就是警告別人別靠近，不過看起來最近有人搜過這間屋子……大概是在找什麼東西……

### (sub) DIAL_Z31#162
- speaker=240  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [42236..0]] -> node 4294901761
    - [flag 0x0101 in [42156..0]] -> node 4294901761
- text: 我們該進去看看嗎？

### (sub) DIAL_Z31#164
- speaker=0  style=6
- effects:
    - apply status/condition to party idx=1 amt=50
    - GIVE gold +340
- text: 空氣中瀰漫著死亡的氣味。  一走進屋內，就看得出有人徹底搜查過這裡。  @4沒發現什麼值得留意的東西，轉身正要離開。「走吧，我們離開這裡。現在可能已經太——」話說到一半，他忽然頓住，目光落在房間角落一塊變色的地板上。  他三步併作兩步穿過小屋，小心翼翼地用劍尖撬開那塊木板，接著伸手指探進去用力拉扯了幾下。木板應聲裂開，「喀啦」一聲鬆脫。@4緩緩伸手探進那個漆黑的方洞，興奮地掏出一只小袋子。他把袋裡閃亮的東西倒在地上，開始清點。  「三十四枚金幣！」他說。「這大概是這戶不幸人家...

## node 3100045  (DIAL_Z31#165)
- speaker=0  style=0
- branches:
    - [flag 0x1ef0 in [20150..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#166
- speaker=0  style=6
- effects:
    - SET flag 0x1ef0=1
    - GIVE gold +12
- text: 穀倉裡又霉又暗。  眾人瞇著眼、摸索著四處搜尋，@0忽然喊了一聲。「這裡。我好像發現了什麼。」  牆壁半腰處刻著一個小小的「x」記號，記號下方的泥土地面微微隆起。  眾人合力挖掘，幾呎深處便找到一只腐朽的木箱，裡頭裝著一只小皮囊，裝有十二枚銀幣。

## node 3100049  (DIAL_Z31#167)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [44810..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#168
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: @4敲了好幾次門，漸漸認定家裡沒人。「走吧，」他朝@0的方向說道。「看起來這裡沒人在。」  正當他準備離開時，屋裡傳出一陣窸窸窣窣的聲響，引起了他的注意。  「哈囉！有人在嗎？」他喊道。  又過了幾秒，四周仍是一片寂靜，他再度準備離開。這時一聲沙啞的低語讓他停下腳步，只是他聽不清門另一側那個聲音在說什麼。  「請大聲一點。我們只是路過，不過想跟您聊聊，」@4說。  「等太陽從天上消失了再回來，」那聲音嘶啞地說，「我再告訴你們露莎姬的事。」最後這個詞說得格外陰森刺耳。  @4試...

### (sub) DIAL_Z31#169
- speaker=0  style=0
- branches:
    - [flag 0x1ef2 in [44839..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#170
- speaker=0  style=6
- effects:
    - SET flag 0x1ef2=1
- text: 雲隙間掛著一輪蒼白如燈的月亮。  「進來吧，」一個粗啞的聲音說道。  他們推門走進這間小屋，屋裡點著近百支蠟燭。牆上的陰影瘋狂舞動，這幅景象令人分神，過了好一會兒@4才注意到地上盤腿而坐的一名古怪老婦。  雙方沒有交談，一行人逕自走過房間，在她面前的地板上坐下。  「我來說說露莎姬的事。」老婦一邊開口，一邊輕輕前後搖晃著身子，粗啞的嗓音漸漸唱誦般地起伏。「純真已逝。已逝。春花被奪去了肉身的歡愉，死亡女神奪走了她們的初吻。她們的初吻。」  燭光在她濕潤的雙眼裡閃爍，她繼續說道。...

## node 3100050  (DIAL_Z31#171)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ef3 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#172
- speaker=0  style=6
- effects:
    - SET flag 0x1ef3=1
- text: 一名中年婦人在門口迎上了@4。  「日安，兩位——」他才開口，話就懸在半空中，沒能說完。  「請進！哎呀，兩位真是一表人才！我叫伊麗莎白。你們成家了嗎？我妹妹卡洛琳是個可愛的姑娘，我看她跟你們正合適呢。要不要見見她？哎呀，這個先不提了。快請進，請進。」  婦人硬是把他們拉進屋裡，@0驚訝於她說起話來竟能一口氣不停，中間好像從沒換過氣。  「我丈夫要是在家肯定也會同意，他在雜貨鋪工作，就是路邊那間店，你們知道的。生意做得挺不錯，所以我們才蓋得起這棟房子。這房子還是他特地為我蓋的...

## node 3100051  (DIAL_Z31#173)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ef4 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#174
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1ef4=1
- text: @4敲了敲那扇小木門，隨後退開幾步，打量起這棟房子跟四周環境。「黑沼鎮看起來挺友善的，」他說。  門開了，他的目光轉向一名嬌小的婦人，對方一把抱住了他。「哎呀。你真是個可人兒？我叫卡洛琳，你叫什麼名字？」@4還沒來得及回答，她已經把大夥兒全都招呼進了屋。  屋裡擺滿了各式各樣的小擺設雜物，看得出是幾十年來積攢下來的。眾人互相介紹，她則用角落小木桌上的一只水罐，替他們把水袋一一裝滿。  「你們看見住在路那頭的那個瘋老太婆了嗎？」她上氣不接下氣地問。「她只在晚上出來。我妹妹伊麗莎...

## node 3100052  (DIAL_Z31#175)
- speaker=0  style=0
- branches:
    - [flag 0x1ef5 in [20150..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#176
- speaker=0  style=6
- effects:
    - SET flag 0x1ef5=1
- text: 穀倉裡瀰漫著酒味。  眾人四處查看，發現一名男子靠著遠處的牆坐著，身旁擺著一瓶凱許麥酒。瓶子已經打開，一半的酒似乎灑在穀倉地上，被一小堆新鮮乾草吸乾了，混雜出一股相當刺鼻的氣味。  另一半的酒顯然灌進了瓶子主人的肚子裡，此刻他正不省人事，鼾聲如雷。  「走吧，」@4說。「讓他睡到醒為止。」

## node 3100055  (DIAL_Z31#177)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ef7 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#178
- speaker=0  style=6
- effects:
    - TAKE gold -250
    - SET flag 0x1ef7=1
- text: @5正要敲門，忽然聽見一名婦人尖聲呼救。  「現在沒人能救得了妳了！哈哈哈哈！」一個粗野的男聲轟然響起。「死亡女神即將——」  話還沒說完，@5後退幾步，用肩膀猛地撞向房門。門「喀啦」一聲裂開，撞擊的衝力讓他一時失去平衡，但他很快穩住身形，一邊拔劍一邊迅速掃視房間。  他發現自己正跟一個衣衫不整、戴著假髮的男子四目相對。房裡再沒有別人。  「你把她怎麼了？」@5質問道。  男子上氣不接下氣地結結巴巴回答：「什……什麼……我……我把誰怎麼了？」  「那個女人。我們聽見有個女人在...

## node 3100056  (DIAL_Z31#179)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f3a in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#180
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - (on-exit) play sfx 0
    - SET flag 0x1f3a=1
- text: 一名頭頂微禿、眼神銳利的男子應了@4的敲門聲。  「兩位是想在普蘭克石鎮待上一陣子嗎？」他問道。「我這正好有間房子——每月才三十枚金幣！」  「抱歉，我們只是路過。能否請您說說住在您房子裡的那些房客？」@4問道。  「其中一間住著個自稱演員的傢伙，另一間眼看就要空出來了。那個沒用的龍痴混蛋，這回可把我的錢給坑光了！日安！」這話題顯然戳中了他的痛處，因為他氣沖沖地甩上門，結束了這場對話。

## node 3100057  (DIAL_Z31#181)
- speaker=0  style=0
- branches:
    - [flag 0x1f83 in [50665..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#182
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
- text: @4用力敲了敲門。  他等了一會兒，又敲了一次。仍不見回應，他轉身準備離開：「看來這位寶石商朋友不在家。」

### (sub) DIAL_Z31#183
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0104 in [51550..0]] -> node 4294901761
    - [flag 0x0105 in [52676..0]] -> node 4294901761
- text: 一名笑容滿面的男子應了門。  「請進，請進！」他咧嘴笑道。「我有樣東西要給你們瞧瞧！」  @4好奇地跟著男子走進屋裡。他領著眾人來到一張桌前，桌上擺著個用布蓋著的笨重物件。男子動作誇張地一把掀開布罩，露出一台造型古怪的金屬機器，頂端有個漏斗，側邊還裝著一支木製搖柄。  「這是什麼？」@0問道。「這是台寶石轉化機。目前它只能把紅寶石變成綠寶石，不過我正在研究一套配方，能把紅寶石變成ñ鑽石ð。對了！你們要不要幫我測試看看？想不想試試手氣？」

### (sub) DIAL_Z31#184
- speaker=0  style=0
- branches:
    - [flag 0xc389 in [51579..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#185
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1f83=1
    - REMOVE item '9' cond=0
    - GIVE item '7' cond=2 to member#6 (cost 0)
- branches:
    - [flag 0x0100 in [51550..0]] -> node 4294901761
    - [flag 0x0101 in [52082..0]] -> node 4294901761
- text: @4遞給男子一顆紅寶石。  「嗯，這顆正合適，」男子舉起紅寶石端詳一番，說道。他把寶石丟進機器頂端的漏斗狀開口，開始轉動搖柄。  搖了幾圈後，機器發出一陣古怪的咔嗒聲，一顆小鑽石落到桌上。男子撿起了它。  「太棒了！成功了！既然你們都在這兒了，要不要順便把你們身上的紅寶石也一起轉化了？」

### (sub) DIAL_Z31#186
- speaker=0  style=0
- branches:
    - [flag 0x1f83 in [52111..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100060  (DIAL_Z31#190)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x7537 in [20112..32815]] -> node 65537
    - [flag 0x1f80 in [20112..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#191
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f80=1
- text: 一名體格壯碩的男子應了@4的敲門聲。  他熱情地邀請他們進屋。閒聊了幾分鐘後，他主動提出替他們的水袋添些清水，這番好意他們欣然接受。正當眾人準備告辭時，男子的語氣忽然變得凝重起來。  「幾位大爺在外頭可得小心。我最近聽見一些古怪的聲響——說不定是那些『紡蛛』又從冬眠裡醒過來了。」  @4有些疑惑，「紡蛛？」  「就是體型碩大的蜘蛛！科瓦利斯伯爵已經派人去巡邏西邊那四片地了，希望能趕在那些蜘蛛在這一帶站穩腳跟之前解決掉牠們，不過還是提高警覺的好。」

## node 3100062  (DIAL_Z31#192)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1fc7 in [54342..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#193
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1fc7=1
- branches:
    - [flag 0x0100 in [54677..0]] -> node 4294901761
    - [flag 0x0101 in [54562..0]] -> node 4294901761
- text: @4急促地敲了敲門。  一名皮膚黝黑的男子在門口迎接他們，臉上帶著幾分疑惑。「這裡的消息傳得真快，」他一邊說一邊讓他們進屋。「沒想到這麼快就有人聽說我們的事了。」  「聽說什麼事？」@4問道。  「我們種的藥草，」一名婦人探頭進屋說道。「科瓦利斯伯爵說這一帶土壤肥沃，准許我們在這裡採集藥草。自從堡裡出了那件事之後，他認為這樣安排最妥當，免得白白浪費了這片好地。要不要瞧瞧我們製的藥？」

### (sub) DIAL_Z31#194
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [54677..0]] -> node 4294901761
    - [flag 0x0101 in [54562..0]] -> node 4294901761
- text: 一對年輕夫婦在門口熱情地迎接他們。  「你們好。又來看看我們的藥草了嗎？我們保證這是這一帶最上乘的藥草製品。要不要再看一次？」

### (sub) DIAL_Z31#195
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「唉，好吧。要是哪天你們需要藥草，歡迎再來找我們。日安。」

## node 3100063  (DIAL_Z31#197)
- speaker=0  style=0
- branches:
    - [flag 0x1ef8 in [54879..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#198
- speaker=0  style=0
- branches:
    - [flag 0x1f8e in [188..32768]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#200
- speaker=0  style=0
- effects:
    - SET flag 0x1ef8=1
- branches:
    - [flag 0xc3a2 in [55242..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#201
- speaker=0  style=6
- effects:
    - GIVE item '\x19' cond=90 to member#6 (cost 0)
    - SET flag 0x1f8e=1
- text: @4朝井底的黑暗中望去。  「下面有個亮晶晶的東西——看起來像是金屬。」他的聲音在井壁間迴盪。「遞把劍跟一些繩子給我。」  @0照他的話取來了東西。接著他看著@4小心翼翼地把繩子綁在劍柄末端，垂進井裡。傳出幾聲金屬碰撞聲，還夾雜著幾句咒罵，然後@4把劍拉了上來。  劍柄上，竟垂掛著一條莫瑞德七鰓鰻！

## node 3100065  (DIAL_Z31#203)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ef9 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#204
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1ef9=1
- branches:
    - [always] -> node 0 (no jump)
- text: @4在前門大聲敲了好幾次，正準備轉身離開時，一個沙啞的聲音從門縫底下傳了出來。

### (sub) DIAL_Z31#205
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你好，朋友。我們想跟您聊聊。方便讓我們進去嗎？

### (sub) DIAL_Z31#206
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啥？你們想幹嘛？

### (sub) DIAL_Z31#207
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是說我們想跟您聊一下，順便討點清水裝滿水袋。

### (sub) DIAL_Z31#208
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啥？你們想要ñ魚水給你們的ñ乳牛ð喝？

### (sub) DIAL_Z31#209
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是，我是說我們想要些ñ清ñ水裝滿我們的ñ水袋ð……而且我們想跟您談談。」

### (sub) DIAL_Z31#210
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啥？

### (sub) DIAL_Z31#211
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們可以進去跟你們談談嗎？

### (sub) DIAL_Z31#212
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 親愛的，他們想幹嘛？  他們說想進來跟我們一起睡。  他們想看我們的鴨子？我們才沒養鴨子呢。怎麼會——

## node 3100066  (DIAL_Z31#214)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1efa in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#215
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1efa=1
- text: @3用手背敲了敲門。  「來了，等等，稍等一下，」屋裡傳出一個興高采烈的聲音。「好了，我來了。」門大大敞開，一名蓄著大鬍子的魁梧男子走出來加入他們。  @3清了清喉嚨，說道：「若能耽誤您一點時間，我們想跟您聊聊。」  這時，那魁梧男子正狐疑地打量著@5。「等等，」他說，臉上綻開一抹像火山爆發般的燦爛笑容，「是陸洛雇你們來的吧？」男子仰頭大笑起來。「噢，這下可有好戲看了！」  他依舊笑個不停地退回屋裡，任憑他們再怎麼追問都不肯答話。

## node 3100067  (DIAL_Z31#216)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1efb in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#217
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [58898..0]] -> node 4294901761
    - [flag 0x0101 in [58670..0]] -> node 4294901761
- text: @5正要敲門，指節卻撲了個空——門已自行往外盪開，退出了他的觸及範圍。  眾人接受了這神秘的邀請，緩緩走進屋內。四面牆上都是架子，架子上堆滿了書。@3的目光落在房間角落一支木杖上。  「啊，你已經找到我的『雷霆杖』了。看得出你很喜歡它。」聲音來自房間角落一名坐在椅子上的男子，桌上堆滿的紙張幾乎遮住了他蜷縮的身影。「在下蕭拉爾。向我證明你的價值，我便把它給你。」  「你在玩什麼把戲？」@5質問道。  這名法師瞇著眼，緩緩答道：「不是把戲。」他轉頭凝視著@3。「答對三個問題，我的...

### (sub) DIAL_Z31#219
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1efb=1
- branches:
    - [flag 0x0100 in [59747..0]] -> node 4294901761
    - [flag 0x0101 in [59313..0]] -> node 4294901761
- text: 「很好！」法師說道。「來，坐到我面前，我們開始吧。」  @3依言照做，這讓@5頗為不悅，他默默在一旁坐下，一手刻意按在劍柄上。  「第一個問題，@3，是這樣的：我們偉大的帕格號稱同時精通大道法術與小道法術。這真有可能嗎？」

### (sub) DIAL_Z31#220
- speaker=0  style=6
- effects:
    - TAKE gold -10000
- text: 「很遺憾，朋友。你沒通過我的考驗。」蕭拉爾在空中揮了揮手，喃喃唸誦咒語。一陣無形的能量席捲整個房間，金幣一枚接一枚憑空浮現，叮叮噹噹地落進房間角落一只大玻璃罐裡。  「你這個賊！」@5喊道。「把我們的金子還回來！」  @3伸手攔住他。「別這樣，@5。這個問題出得公平。我們該走了。」

### (sub) DIAL_Z31#221
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [59313..0]] -> node 4294901761
    - [flag 0x0101 in [60082..0]] -> node 4294901761
- text: 「很好，朋友，」蕭拉爾喃喃道，「你還剩兩個問題。」他在椅子上動了動身子，翻了翻桌上的文件，接著說道：「龍族君王曾統治這顆星球。其中一名瓦爾赫魯——德拉肯柯林，自稱『鷹之王』。我這麼說可屬實？」

### (sub) DIAL_Z31#222
- speaker=0  style=6
- effects:
    - GIVE item '\x02' cond=30 to member#5 (cost 0)
- text: 「你又答對了，」法師說道，笑容變得冷冽。「現在只剩最後一個問題——答對了，我的法杖就歸你。」  @5冷冷地盯著這名法師，不喜歡他臉上那股彷彿要噴湧而出的邪火。  忽然，@3放聲大喊：「我的眼睛！你這黑暗惡魔對我的眼睛做了什麼？我看不見了！」@5瞬間跳起身，拔劍出鞘。  「等等！我根本沒動你的眼睛！」蕭拉爾嚇了一跳，結結巴巴地說。「你看不見我嗎？」他一邊喊一邊在空中胡亂揮舞雙手。  @3咧嘴一笑。「抱歉，是我搞錯了。是的！我看得清清楚楚。」他朝法師眨了眨眼。「我還真傻，還以為你...

## node 3100068  (DIAL_Z31#223)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1efc in [61901..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#224
- speaker=0  style=6
- effects:
    - SET flag 0x1efc=1
- text: 一名滿臉倦容的婦人在門口迎接他們。「日安，旅人們。有什麼能為你們效勞的嗎？」  「能否請您說說肯廷拉什這個地方？我們對您住的這裡挺好奇的，」@4和氣地問道。  「唉，兩位大爺。這裡算是個不錯的地方，不過最近井邊常有些鬼鬼祟祟的傢伙晃來晃去。」她頓了頓，指向附近一片田地，「我丈夫正在那邊收割穀物。讓我想想，還有什麼能跟你們說的呢？對了！千萬小心那個住在路那頭的法師，他老愛騙人的錢；他會問三個問題，前兩個很簡單，但從沒人答對過最後一題。」  他們謝過婦人抽空相談，便繼續趕路。

## node 3100069  (DIAL_Z31#226)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1efd in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#227
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - (on-exit) play sfx 0
    - SET flag 0x1efd=1
- text: 屋裡傳出的敲擊聲，恰好與@4敲在小前門上的叩門聲相互應和。  不一會兒，一名蓄著長鬚的年輕男子前來應門。  「什麼事？沒看見我正忙嗎？」他們越過男子望去，只見一大塊花崗岩前，一名美麗的女子彷彿正從石頭中綻放而出，如同嬌嫩的花朵迎向陽光。  「你在雕刻一名女子？」@0問道。  男子不耐煩地把重心從左腳換到右腳，語帶譏諷地說：「不，其實我是想用一塊大石頭蓋住一個臉色蒼白、動也不動的女人。」說完便粗魯地在他們面前甩上了門。  @4轉身離去。「藝術家！」他忿忿地啐了一口。

## node 3100070  (DIAL_Z31#228)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1efe in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#229
- speaker=0  style=0
- effects:
    - SET flag 0x1efe=1
    - RAISE Health+Stamina of member#4 by 0..5120
- branches:
    - [always] -> node 0 (no jump)
- text: @4正要敲門，忽然直起身子，臉上綻開一抹燦爛的笑容，退後幾步端詳起整棟房子。

### (sub) DIAL_Z31#230
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我認得這地方！一年前我去北衛城看朋友的路上，就是在這棟房子借宿的。當時這裡住著一位名叫瑟琳德拉的美麗姑娘。我們一起吃了頓晚飯，處得還挺投緣，半夜她還偷偷溜進我房裡……」

### (sub) DIAL_Z31#231
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
- text: 他滿懷期待地敲了敲門，臉上笑容燦爛。片刻後，一名美麗的年輕女子應了門。  「什麼事？我能不能——@4？」她唇邊掠過一抹認出對方的微笑，卻迅速被滿臉憂色取代。「我是——」話還沒說完，一雙碩大的手便將她推到一旁，其中一隻攥成拳頭，結結實實揍在@4臉上。  等他視線恢復清楚，那名女子已站在他面前。「來見見我丈夫吧，我把你的事都跟他說了。」

## node 3100072  (DIAL_Z31#232)
- speaker=0  style=0
- branches:
    - [flag 0x753a in [20139..32815]] -> node 4294901761
    - [flag 0x1eff in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#233
- speaker=0  style=6
- effects:
    - play sfx 0
    - SET flag 0x1eff=1
- text: 這是個寂靜的夜晚，唯有蟋蟀的鳴叫聲，為這片死寂帶來一絲生氣。  窗子透出點點燭光，屋裡似乎有人在走動。@4敲了敲門，一陣窸窸窣窣後，一名頭髮灰白的矮小男子前來應門。  「今晚真美，是吧？萬里無雲，」小個子男子心不在焉地說道，隨即留著門敞開，逕自走回屋裡。  他們跟了進去。  屋內散落著各式圖表，@5注意到屋頂居然沒有蓋。找到男子時，他正躺在地上仰望星空。他一邊回答他們的幾個問題，一邊自顧自地做著筆記，但眾人並未從中得到什麼重要或有用的訊息。  他們悄悄地自行離去，盡量不再打擾...

## node 3100073  (DIAL_Z31#234)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f00 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#235
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f00=1
- text: 屋裡傳出陣陣鴿鳴聲，而且為數不少。  @4耐心等候有人應門。幾秒後，一名滿臉雀斑的男孩前來開門，領他們進屋。  一名和藹的男子站在一只幾乎佔滿整個房間的大鐵絲籠子旁，籠裡養滿了鴿子。他正輕撫著一隻小鴿子，想哄牠回籠裡去。「來吧，」他溫柔地說。「乖，進去吧。」那隻鳥卻不肯配合。  「咳。」@4清了清喉嚨，男子驚訝地抬起頭，手中的鴿子趁機飛脫，在天花板附近盤旋起來。  「該死。這些鳥跟小孩沒兩樣，怎麼講都不聽。」角落裡，那名男孩笑了笑。「我聽說有個叫『主人之意』的法術，據說能驅使...

## node 3100074  (DIAL_Z31#236)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f01 in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#237
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f01=1
- text: @4敲門時，一股新鮮麵包的香氣撲鼻而來，饞得他肚子咕嚕作響。  等了一會兒，一名矮胖的男子前來應門。他臉頰跟鼻樑上都沾著麵粉，一邊說話一邊用手背抹了抹。「有什麼事嗎？」他問道。  @4注意到屋裡有名婦人，同樣滿身麵粉。「我們不是有意打擾，」他說，「只是聞到麵包香，想說順道過來看看——」  「抱歉，我們跟『燭匠的笑臉』的塔巴爾有獨家約定。要買吃的得去那邊才行。就在路那頭，應該不難找。好了，我們真得回去忙了。」

## node 3100077  (DIAL_Z31#238)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[13] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 769
    - [event_bitmap_hi[13] (xor=0x20 mask=0x0c mode=1 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#239
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [2611..1]] -> node 4294901761
    - [flag 0x0101 in [2284..1]] -> node 4294901761
- text: 門上刻著一些古怪的符號。  @4狐疑地端詳著這些符文，接著大聲敲門。  前來應門的男子自我介紹是卡胡利神殿的主教。  「凡夫俗子並不喜歡我，」他說。「他們不理解我行事背後那份至高無上的正義。凡是違反律法者，都必得承受神明的懲罰。」  主教接著滔滔講述起自己當年如何一路修行成為主教，以及當地神殿嚴格奉行的『虔信律則』。  @4禮貌地點點頭，問道：「能否請您說說這些律則？」  主教看出他們有興趣，便反問了一個問題：「若兩位願意捐獻給神殿——就說五十枚金幣好了——我想我是可以被說服...

### (sub) DIAL_Z31#240
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4故作不感興趣地打了個哈欠。  「我們的錢還是自己留著吧，多謝。恐怕您那些律則也沒那麼重要。再說，我們的ñ捐獻要是被視為王室的默許，恐怕亞魯莎親王跟萊亞姆王對貴教信徒睚眦必報的作風，一向都不甚苟同。」

### (sub) DIAL_Z31#241
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [2907..1]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#242
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4皺了皺眉。  「恐怕我話說得太早了，我們手頭目前有點緊，」他說。「不過要是您能——」  男子打斷了@4的話，神情嚴肅地看著他。「等你們回來的時候，想知道的答案自然會告訴你們。」

### (sub) DIAL_Z31#243
- speaker=0  style=6
- effects:
    - TAKE gold -500
    - event_bitmap_hi[13] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: @4遞給主教五十枚金幣。  「卡胡利神殿感謝你們的捐獻，」他說。「現在請隨我來，我這就教你們我們的虔信律則。」

### (sub) DIAL_Z31#244
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 主教領著他們走進一間小房間。  他站在一座臨時搭起的祭壇後方，開始講述——有時甚至像是在咆哮——偉大的卡胡利神，那位復仇的戰神、解開謎團直指真相之神。他們聽得興致缺缺，直到主教終於開始講述起虔信律則。  「意志之服從，」他開口道。「未先斷絕與王國及君主一切羈絆者，不得被視為ñ卡胡利真正的信徒。」  主教繼續說著，@4緊張地環顧四周。  「肉身之苦行。凡未先滌淨自身一切ñ肉慾者，不得踏入卡胡利神殿一步，方能淨化己身以迎卡胡利神意之降臨。」  「最後，服事之從屬。未先通過水簾試煉...

## node 3100078  (DIAL_Z31#246)
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [4826..1]] -> node 4294901761
    - [flag 0x0101 in [4648..1]] -> node 4294901761
- text: @5從行囊裡取出水袋，俯身探向井邊。  一股怪異的氣味竄入他的鼻腔，他狐疑地又嗅了一次。氣味似乎是從井裡傳出來的。他又俯身湊近了些，想看清底下的水，卻怎麼也無法從那片幽暗中辨認出什麼。  @3走近時，他抬手示意對方止步。「我看這口井裡的水不太對勁。」  「你打算試喝看看嗎？」@3問道。

### (sub) DIAL_Z31#248
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - apply status/condition to member#5 idx=2 amt=55
- text: 這井水味道糟透了。  @5幾乎是水一入口就立刻吐了出來，這才注意到井邊躺著一隻死鳥。「該死！」他朝天大吼一聲。  沒過幾秒，他的嘴已開始發麻，他不停朝地上吐口水，用衣角擦拭著舌頭。「我看這毒性不輕，幸虧頌恩神保佑，我沒真的吞下去，不然大概當場就沒命了。」他勉強擠出一絲苦笑。「現在只能慢慢等死了。」

## node 3100321  (DIAL_Z31#249)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[17] (xor=0x43 mask=0x15 mode=1 chapters=-)] -> node 4278256640
    - [event_bitmap_hi[17] (xor=0x40 mask=0x17 mode=1 chapters=-)] -> node 4278255873
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#251
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - event_bitmap_hi[17] bitop
- branches:
    - [flag 0x0100 in [7236..1]] -> node 4294901761
    - [flag 0x0101 in [6790..1]] -> node 4294901761
- text: @4嗅了嗅空氣。  屋裡飄出的香氣簡直像天堂一樣，饞得他敲門時肚子直咕嚕叫。  片刻後，一名穿著鮮豔圍裙的姣好婦人前來迎接。她邀請他們進屋，還端出剛出爐的糕點招待，眾人欣然接受。  「我叫蒂雅．哈夫蓋特，」她告訴他們。「我是弗蘭德爾．哈夫蓋特的次女。」她接著說起亡夫的事，還有她如今看上的一名北衛城士兵。  「他負責維修保養北衛城的兵器。也許你們能教教我這門手藝，好讓我在他面前露一手。我可以把亡夫的十字弓送給你們，反正我ñ用不著它。你們願意教我嗎？」

### (sub) DIAL_Z31#253
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [7236..1]] -> node 4294901761
    - [flag 0x0101 in [6790..1]] -> node 4294901761
- text: 蒂雅在門口迎接他們。  「你們回來是要教我那堂課了嗎？」她熱情地問道。「下次遇上一群巨魔，我丈夫留下的那把老十字弓說不定能派上用場。你們願意教我兵器保養的手藝嗎？」

### (sub) DIAL_Z31#254
- speaker=0  style=0
- effects:
    - advance in-game time by 7200
    - read Weaponcraft -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [7770..1]] -> node 4294901815
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#256
- speaker=0  style=6
- effects:
    - event_bitmap_hi[17] bitop
    - GIVE item '\x1f' cond=100 to member#7 (cost 0)
- text: 課程開始了。  蒂雅興致勃勃地聽著@5講解自己的劍是如何保養得如此鋒利完好。  將近一個鐘頭後，課程結束，她打開床底下的木箱，取出一把做工精美的木十字弓，微笑著遞給@5，向他道謝。  眾人也謝過她，隨後告辭離去。

## node 3100079  (DIAL_Z31#257)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f04 in [20147..32815]] -> node 4294901761
    - [flag 0x1f03 in [9220..1]] -> node 4294901761
    - [flag 0x1f02 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#258
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1f02=1
- text: @4敲了敲門。  一名紅髮男子開了門，戒備地打量他們一番。似乎滿意後，便邀請他們進屋，還幫忙把水袋裝滿。  「能否請您說說世界之齒山下的丹肯營地？」@4故作無心地問道。  「你們想知道什麼樣的消息？要是為了路那頭那群人的事，跟你們說吧，我看他們八成沒成功。」  @4順著話接下去，「哦？怎麼說？」  「這個嘛，」男子答道，「聽說北邊最近動靜不小。他們至少被三批哥布林纏上了。好不容易想出辦法解決了哥布林，結果又被巨魔盯上！」  「他們想出辦法對付哥布林了？」@0難以置信地問。「怎...

### (sub) DIAL_Z31#259
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1f04=1
- text: 紅髮男子敲了三次門後才應門。  「什麼事？——噢，又是你們這幾位，」他說。  @4叉著腰站在門口。「我們去跟路那頭您那些朋友談過了，可『黃金寶藏』根本不是暗號。」  男子愣了一下，接著語速飛快地說：「噢，對啦，真抱歉！讓我想想……那暗號是什麼來著？他們找我入夥的時候跟我說是……噢，我想起來了。是『鑽石』。對，就是這個。」  @4冷冷地盯著他。「希望這次你說對了。要不然，我們會再來找你——下次可就沒這麼客氣了。」

## node 3100080  (DIAL_Z31#260)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1faf in [20147..32815]] -> node 4294901761
    - [flag 0x1fad in [11939..1]] -> node 4294901761
    - [flag 0x1f02 in [12210..1]] -> node 0 (no jump)
    - [flag 0x1f04 in [10529..1]] -> node 4294901761
    - [flag 0x1f02 in [9979..1]] -> node 4294901761

### (sub) DIAL_Z31#261
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: @4敲了敲那扇滿是刀痕的木門。  片刻後，屋裡傳出一個宏亮的男聲。「暗號是什麼？」對方厲聲問道。  「黃金寶藏，」@4自信滿滿地答道。  「那不是暗號！暗號是什麼？」  @4一時語塞，頓了頓。那宏亮的聲音又重複了一遍，他心裡盤算著要不要亮出王國公務的名義硬闖進去，但一想到裡頭可能有十來個持械的漢子，便打消了這念頭。  「現在怎麼辦？」@0一邊問，一邊從門邊退開。

### (sub) DIAL_Z31#262
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1fad=1
- branches:
    - [always] -> node 0 (no jump)
- text: @4又敲了敲門，指節都快跟這扇門混熟了。  「你們想幹嘛？」那聲音吼道。  「我們知道暗號。是『鑽石』。」  一陣停頓，@4覺得自己聽見裡頭傳來竊竊私語聲。接著那宏亮的聲音又響起：「你們可以進來了。」

### (sub) DIAL_Z31#263
- speaker=0  style=6
- effects:
    - play sfx 0
    - GIVE item '\x85' cond=22 to member#5 (cost 0)
- text: 傷痕累累的門開了，他們獲准進屋。屋裡擠了十來個男人，大半手裡都握著劍，其中幾個還帶著新傷。  簡短交談之後，他們得知這群人計畫進入北境，尋回一批據傳藏在那裡的貴重寶藏。他們遭遇到的抵抗遠比預期猛烈，因此正招募更多身強力壯的人手，準備再度出擊。  不過@4真正感興趣的，是他們究竟怎麼解決掉那麼多哥布林的。  「我們找了個法師來幫忙，就這麼回事！」一名男子回答@4的提問時得意地說。「用法術把那些哥布林的腦子都燒了個乾淨，效果好得很，簡直把牠們逼瘋了。可憐的萊昂諾，那咒語對殺死他的...

### (sub) DIAL_Z31#264
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1faf=1
- text: @4敲了敲門。  「暗號是鑽石，」他淡然說道。  「不對，」屋裡傳出一個聲音。「我們換過暗號了。滾開。」  @4聳聳肩，示意大家可以走了。

### (sub) DIAL_Z31#265
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
- text: @4敲了敲門，卻沒人應答。  他能聽見屋裡傳出動靜，而且方才走近時就注意到，泥地上留著大小不一的許多腳印。  一個洪亮的聲音忽然問道：「暗號是什麼？」把他的思緒拉了回來。  @4看了看@0，對方只是聳聳肩，他便轉回頭對著門說：「暗號？」  「沒有暗號就別想進來。趕快滾，不然我們就要動手了！」

## node 3100081  (DIAL_Z31#266)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f05 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#267
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f05=1
- text: 一名雙眼哭紅的婦人應了@4的敲門聲。  「太好了，你終於——噢，抱歉。我還以為是我哥哥。他這幾天要來跟我一起住一陣子。」  她邀請他們進屋，說起自己的愛人最近在北衛城要塞附近的一場邊境衝突中被巨魔殺害了。  @0溫和地問道：「這麼說，他是個士兵？」  她點點頭，眼眶又蓄滿了淚水。「朋友們一直送吃的來，多得我根本吃不完。要是還有剩，你們可以拿一些。」

## node 3100082  (DIAL_Z31#268)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[20] (xor=0x2c mask=0x34 mode=1 chapters=-)] -> node 4278256386
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#269
- speaker=0  style=0
- branches:
    - [flag 0x1ecb in [50920..32813]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#270
- speaker=0  style=0
- effects:
    - read Strength -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [13649..1]] -> node 4294901790
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#272
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4推了推穀倉的門，門卻紋風不動。  明明看不出任何鎖具，眾人試了一次又一次，這扇木門依然牢牢緊閉。  終於，一番苦戰、無數次咬牙咒罵之後，隨著一聲刺耳的呻吟聲，鏽蝕的鉸鏈總算鬆脫了！

### (sub) DIAL_Z31#273
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f06 in [20150..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#274
- speaker=0  style=6
- effects:
    - SET flag 0x1f06=1
    - GIVE gold +90
- text: 丹肯營地的公用穀倉跟一般常見的差不多，裡頭養的也是牛、羊、雞這類尋常牲畜。儘管如此，@4還是覺得該進去看看。  顯然這穀倉已經有段時間沒清理過了，那股臭味幾乎令人難以忍受。  他正要離開時，眼角餘光瞥見一絲亮光，便用腳撥開一些泥土和乾草。光線昏暗看不清楚，他索性彎下腰湊近細看。  起初只看見一枚金幣，但仔細一瞧才發現，一只小布袋裡竟灑出了整整九枚這樣的小寶貝。  「好吧，看來我得替王國徵用這筆錢了，」@4喃喃自語道。「看起來擺在這裡也有一陣子了，想必不會有人發現少了這些。」

## node 3100316  (DIAL_Z31#275)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100085  (DIAL_Z31#276)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f07 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#277
- speaker=0  style=6
- effects:
    - SET flag 0x1f07=1
- branches:
    - [always] -> node 0 (no jump)
- text: 前門上滿是深深的刮痕，像是被劍刃劃過的。  @5拔劍在手，小心翼翼地走進屋內。屋子外觀雖然飽經風霜，卻遠比被洗劫一空的屋內完好——一張小木桌跟兩把椅子的殘骸，東倒西歪地散落在屋子各處。  簡單搜索一番，沒發現什麼值得留意的東西，他們便決定離開。

### (sub) DIAL_Z31#278
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是盜賊幹的嗎？

## node 3100086  (DIAL_Z31#280)
- speaker=0  style=0
- branches:
    - [flag 0x1f08 in [20150..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#281
- speaker=0  style=6
- effects:
    - SET flag 0x1f08=1
- text: 穀倉門內躺著一具羊的殘骸，扭曲的軀體混雜著鮮血、骨頭與羊毛，慘不忍睹。  @3張大了嘴，呼吸急促。顯然這頭牲畜是被刀刃剖開的，凶手衝著牠的肉而來。真正讓他心裡發毛的，是這番殺戮手段的殘暴程度——鮮血四濺，牆上和天花板上都黏著一絲絲風乾的肉屑，想必是刀刃在這隻毫無反抗之力的動物身上狠狠劈砍時，濺飛上去的。  穀倉裡其他牲畜的下場也大同小異。  @5心想真是奇怪，眼前這幅景象竟不比戰場上見過的死人來得更令人震撼。猶豫片刻後，他決定是時候該離開了。

## node 3100087  (DIAL_Z31#282)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x7537 in [20139..32815]] -> node 327685
    - [flag 0x1f09 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#283
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f09=1
- text: @4敲了敲門。這扇門似乎比一般的要大上一些，等到屋主應門，他才明白為什麼——那名男子身高跟戈拉斯不相上下，這個發現讓人跟莫瑞德人雙方都有些不自在。  「鄙人墨菲，兩位大爺有什麼事嗎？」  @4仰頭望著這名男子，反問了一個問題：「能否請您說說沃夫拉姆這個地方？」  墨菲聳了聳他那寬闊的肩膀，望向鎮上其他建築。「這個嘛，路那頭就是『狼牙』酒館，要吃要喝都行。武器可以去『達拉之武』找，以前還有間客棧，不過已經關了。現在我們拿來吊死犯人用。那是我的差事。」  @4嚥了口口水，比自己預...

## node 3100088  (DIAL_Z31#284)
- speaker=0  style=0
- branches:
    - [flag 0x753a in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#285
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
- branches:
    - [flag 0x0100 in [18489..1]] -> node 4294901761
    - [flag 0x0101 in [18066..1]] -> node 4294901761
- text: @4敲了敲門，耐心地退後幾步等候。  屋裡毫無動靜，他正要更大聲地再敲一次，門卻開了。一名瘦弱矮小、雙手泛綠的男子站在他們面前，滿是皺紋的臉上帶著探詢的神情。  「日安，先生，」@4說道。他這才注意到，這名矮小男子戴著手套。他身後隱約可見幾只咕嘟冒泡的罐子，還有幾只裝滿彩色粉末的小木碗。  「好一個適合品嚐死亡的日子。要不要瞧瞧我這些可口的小東西？也許你們想買點什麼……」男子嘶啞地低聲說道。

### (sub) DIAL_Z31#286
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 這位煉金術士臉上閃過一絲失望。「唉，真可惜我們沒能……做成生意……那就下次吧。」  「是啊，下次吧，」@4附和道。  「那至少讓我幫你們的水袋添點清水吧，」他說。  @4點了點頭，正要伸手去拿行囊，忽然又改變了主意。「呃，不用了，沒關係。我們才剛裝滿。不過還是謝謝您的好意。」

## node 3100090  (DIAL_Z31#288)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f0b in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#289
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f0b=1
- text: @4敲了敲木門，順道讀了讀門上那塊雕工精緻的小招牌，上頭寫著：『心懷喜悅而入，願喜悅充滿吾家。』  一名年輕婦人應了門，@4望見她身後有幾個小孩，還有一名男子坐在小桌前，正用羽毛筆小心翼翼地在一張泛黃的羊皮紙上寫字。男子抬起頭望了他們一眼。  「什麼事？」  寒暄過後，男子告訴他們自己是名文士，正在替北衛城的加博特男爵撰寫一份重要文件。他不肯讓他們過目，但@4猜測那多半是一份記錄北境莫瑞德人活動日益頻繁的官方報告。  他們謝過男子，讓他繼續忙自己的事去了。

## node 3100322  (DIAL_Z31#290)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[38] (xor=0xb1 mask=0x53 mode=1 chapters=-)] -> node 4278256128
    - [flag 0x7537 in [19544..1]] -> node 196610
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#291
- speaker=0  style=0
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - event_bitmap_hi[38] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: @4氣沖沖地敲了敲門。  屋裡傳出一陣咕噥聲跟咒罵聲。終於門開了，一名蓄著幾綹灰鬍的矮小男子走出來加入他們……

### (sub) DIAL_Z31#292
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呸！我就猜這法術可能會出岔子！ñ本ñ來沒人該躲得過我那些小寵物的。看來我得重新召喚幾隻——

### (sub) DIAL_Z31#293
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們差點就被您那些小寵物給ó殺了。這可不是招待友善訪客該有的方式。

### (sub) DIAL_Z31#294
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó先別提我根本沒邀你們的事！不過要是你們真受傷了，我也不是故意要牽連無辜。只是這年頭上門的客人，都是打北境來的。

### (sub) DIAL_Z31#295
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您在北境有朋友？

### (sub) DIAL_Z31#296
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 朋友？才不是呢。上門的訪客沒一個是我歡迎的。多半是老貝利可汗派來的哥布林，想偷我的法術書跟配方。牠們就是看不慣我插手替北衛城的加博特男爵施法辦事。我原本指望這些幻術能有點效果，可看樣子連隻蚊子都嚇不跑，得再多下點工夫才行。來，讓我給你們點東西，好讓你們自己療傷。

### (sub) DIAL_Z31#297
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不必了，我們沒事……

### (sub) DIAL_Z31#299
- speaker=0  style=0
- branches:
    - [flag 0x753a in [20112..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100092  (DIAL_Z31#300)
- speaker=0  style=0
- branches:
    - [flag 0x1f0c in [20154..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#301
- speaker=0  style=6
- effects:
    - SET flag 0x1f0c=1
- text: 這頂小帳篷裡瀰漫著濃重的死亡氣息。  @4屏住呼吸，掀開帳篷入口的簾布。一具腐爛的屍體癱倒在泥地上，四周散落著各式木製與金屬工具。  「看起來像個礦工，」@4盡量不用鼻子呼吸，飛快說道。「我們看看這裡有沒有能用的東西。」

## node 3100323  (DIAL_Z31#302)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[19] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 4177592320
    - [event_bitmap_hi[19] (xor=0x9c mask=0x55 mode=1 chapters=-)] -> node 4278272000
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#303
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#304
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [22943..1]] -> node 4294901761
    - [flag 0x0101 in [22804..1]] -> node 4294901761
- text: 迎接@4敲門聲的，是一陣咯咯的笑聲。  門被兩名婦人小心翼翼地從裡頭拉開。她們看起來相當緊張，一邊自我介紹一邊咯咯笑個不停。  「我是吉娜．哈夫蓋特，這是我妹妹安德麗雅，」年長的那位開口道，強忍著笑意接著說：「希望你們不是專程來聽我們演奏的。」  「演奏？」@4問道。  「我跟妹妹以前常為路過的孤單士兵拉小提琴，不過最近客人不多，樂器也走音了。對了！你們有調音叉嗎？要是有調音叉，我們可就感激不盡了。」  她看出@4面露猶豫，補充道：「我們拿不出多少錢，不過有位士兵留下了一條皮...

### (sub) DIAL_Z31#306
- speaker=0  style=0
- branches:
    - [flag 0xc384 in [22972..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#307
- speaker=0  style=6
- effects:
    - event_bitmap_hi[19] bitop
    - GIVE item 'c' cond=1 to member#6 (cost 0)
    - REMOVE item '4' cond=0
- text: @4答應了這筆交易。  他從行囊裡取出一支銀色調音叉，遞給兩姊妹，兩人興奮地咯咯笑了起來。她們一起退到屋子另一頭，幾分鐘後拿著一條皮綁腿回來。  交易完成後，@4謝過她們的招待，便告辭離去。

## node 3100094  (DIAL_Z31#309)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f0d in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#310
- speaker=0  style=6
- effects:
    - advance in-game time by 5400
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f0d=1
- text: 應@4敲門聲而來的，是一名老者，滿臉皺紋，身形卻依然保持著軍人般的挺拔。  他自我介紹是伊爾蘭，曾任高堡的劍術大師，接著滔滔講起自己多年來的戰績與征戰故事。眾人聽得津津有味，尤其是他提到近來得知的幾場邊境衝突時。  最後，老者講得筋疲力竭，便告退去小睡片刻。

## node 3100095  (DIAL_Z31#311)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f0e in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#312
- speaker=0  style=6
- effects:
    - SET flag 0x1f0e=1
- text: 「今天天氣真好，你們說是不是？」一名和藹的婦人前來應門，說道。  「是啊，確實不錯，」@4答道。「我們想耽誤您跟您丈夫一點時間，聊聊天。」  「抱歉，馬庫斯現在出門打獵去了。或許我能幫上忙。」  「其實我們想知道，您最近有沒有注意到……什麼不尋常的事情？」@4問道。  「唔，你這麼一說，倒真有一件。馬庫斯上次打獵時發現了三只古怪的箱子，說上頭刻著些奇怪的文字。」  原本心不在焉摳著指甲縫裡泥垢的@0，一聽到箱子的事立刻豎起了耳朵。  「您還記得他說是在哪找到的嗎？」@4問道。...

## node 3100324  (DIAL_Z31#313)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[19] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 257
    - [event_bitmap_hi[19] (xor=0x34 mask=0x63 mode=1 chapters=-)] -> node 4278288384
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#314
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#315
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [26198..1]] -> node 4294901761
    - [flag 0x0101 in [20157..32815]] -> node 4294901761
- text: 一名姣好的婦人應了門。  一番寒暄後，她讓他們進了這間雖小卻布置雅緻的家。眾人得知她名叫莎拉．哈夫蓋特，丈夫是名商人，正外出經商。  「我們是來找一袋穀物的，不知能否請您幫忙，」@4問道。  婦人看似有些猶豫。「這個嘛，兩位大爺，我這裡是有幾袋穀物，可要是我丈夫回來發現少了，肯定會大發雷霆。不過要是你們能幫我找份仲夏節的禮物，我倒是可以勻出一袋。」  「我不確定我們ñ能幫上什麼忙，」@4說。  「他老唸叨著想要一條皮綁腿，你們要是能找到，我就給你們一袋穀物。這樣成交嗎？」

### (sub) DIAL_Z31#316
- speaker=0  style=0
- branches:
    - [flag 0xc3b3 in [26227..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#317
- speaker=0  style=6
- effects:
    - event_bitmap_hi[19] bitop
    - GIVE item '<' cond=1 to member#6 (cost 0)
    - REMOVE item 'c' cond=0
    - SET flag 0x1a37=1
- text: @4點了點頭。  「哦，真高興我們談成了，」莎拉說。「我丈夫收到這份禮物一定樂壞了。」  她走到房間角落，從一堆穀物袋裡抽出一袋。  @5上前幫忙，「來，我幫您。」  她道了謝，跟著他回到其他人身邊完成交易。眾人匆匆道別，她叮囑他們路上小心，目送他們走出門口，重新踏上大路。

## node 3100098  (DIAL_Z31#319)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f0f in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#320
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f0f=1
- branches:
    - [flag 0x0100 in [28104..1]] -> node 4294901761
    - [flag 0x0101 in [28023..1]] -> node 4294901761
- text: @4敲了敲門。  不一會兒，一名身材壯碩的婦人應了門，客套寒暄幾句後，便領著他們進屋。「我丈夫在另一個房間忙著做一雙新鞋，我去跟他說一聲你們來了。」  她隱沒到一道布簾後方——那顯然是用來區隔屋子起居區跟工作區的。布簾再度掀開，一名笑容滿面的男子走了進來。  「哎呀，大爺們。是來買鞋的嗎？也許想給你們的女伴也帶一雙，嗯？我正在設計一款給時髦仕女穿的新鞋樣式。」他舉起一雙鞋跟細長、約兩吋高的鞋子。  @4皺了皺眉。「穿上這個，豈不是整天都像在下坡走路？」  老人看了看@4，又看...

### (sub) DIAL_Z31#321
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「唉，或許改天你們會再來看看我們吧，嗯？」

## node 3100099  (DIAL_Z31#323)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f10 in [20149..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#324
- speaker=0  style=6
- effects:
    - SET flag 0x1f10=1
- text: 前來應門的是一名彎腰駝背的男子，正用一塊沾滿污漬的布擦著手。  「歡迎來到艾爾德角。是來買陶罐的嗎？品質可好著呢，」男子咧嘴笑道。  「我相信是的，不過我們只是路過的旅人，用不上這些東西。能否請您說說這座鎮子？」@4問道。  男子放下抹布，用手臂內側跟手腕擦了擦額頭。「這個嘛，這裡有間叫『古茲』的雜貨鋪，還有間叫『皇家臥榻』的客棧。零零星星幾戶人家……沒什麼特別的……怎麼這麼問？」  @4微微搖頭：「沒什麼，就是好奇問問。多謝您撥空，先生。日安。」

## node 3100102  (DIAL_Z31#325)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f11 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#326
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f11=1
- text: 這棟房子年久失修，破損嚴重，不過看起來似乎有人居住，@4便大聲敲門，退後幾步等候。  屋裡傳出一個女聲喊道：「是誰？」  「王國公務，我們需要跟您談談，」@4語氣堅定地說。  門緩緩開啟，一名婦人現身，見到門外站著的他們，神情又驚又慌。「兩位大爺，求求你們，我們沒有惡意。這房子是我們發現的時候就已經荒廢了。」  她那件破舊的衣裙在微風中輕輕飄動，緊張的聲音也跟著微微顫抖。  @0注意到——或者說察覺到——她懷有身孕。「我們不是為這件事來的。能否請您說說這一帶的情況？有沒有什麼...

## node 3100325  (DIAL_Z31#327)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[19] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 4177592320
    - [event_bitmap_hi[19] (xor=0x67 mask=0x75 mode=1 chapters=-)] -> node 4278259712
    - [event_bitmap_hi[19] (xor=0x7a mask=0x75 mode=1 chapters=-)] -> node 4278263808
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#328
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#329
- speaker=0  style=0
- effects:
    - event_bitmap_hi[19] bitop
    - GIVE item '4' cond=4 to member#6 (cost 0)
    - GIVE item ':' cond=100 to member#6 (cost 0)
    - GIVE item 'N' cond=12 to member#6 (cost 0)
- branches:
    - [flag 0x1fb6 in [30143..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#332
- speaker=0  style=6
- effects:
    - SET flag 0x1fb6=1
    - ?wOp12 a1=0 a2=0
- text: 一名和善的婦人應了門。  她自我介紹是拉莉莎．哈夫蓋特，弗蘭德爾．哈夫蓋特之女。閒聊片刻後，她又透露自己獨居，穀倉那扇生鏽的門一直讓她頭疼不已。  「若能幫我把門打開，我會ñ萬分感激的！」她真誠地微笑道。  @4答應會設法看看。她替他們的水袋補滿清水後，眾人便告辭離去。

## node 3100326  (DIAL_Z31#333)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[19] (xor=0x25 mask=0x4e mode=47 chapters=8)] -> node 4278263808
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#334
- speaker=0  style=0
- effects:
    - read Strength -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [32277..1]] -> node 4294901790
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#335
- speaker=0  style=6
- effects:
    - play sfx 0
    - (on-exit) play sfx 0
    - event_bitmap_hi[19] bitop
- text: @4推了推穀倉門。  「這門卡住了，」他對@0說。「過來幫我一把，看能不能推開。」  兩人合力推門，先是持續施力，接著又猛力撞擊。  終於，幾分鐘的努力後，門開始鬆動。隨著一聲刺耳的金屬呻吟，鉸鏈鬆脫，門朝穀倉內盪開。

### (sub) DIAL_Z31#336
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
- text: @4推了推穀倉門。  「這門卡住了，」他對@0說。「過來幫我一把，看能不能推開。」  兩人合力推門，先是持續施力，接著又猛力撞擊。  折騰了幾分鐘，時間一半用來撞門、一半用來咒罵，兩人終於放棄了。

## node 3100105  (DIAL_Z31#337)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f12 in [20152..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#338
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [33588..1]] -> node 4294901761
    - [flag 0x0101 in [33447..1]] -> node 4294901761
- text: 「莫瑞德人的氏族大多過著遷徙的生活，像這樣有房屋的小聚落並不多見，眼前這頂帳篷才是更常見的居所，」@5低聲道。  他朝帳篷裡喊了一聲，卻無人回應。「主人似乎不在。或許我們該進去看看，」他說。

### (sub) DIAL_Z31#340
- speaker=0  style=6
- effects:
    - GIVE item 'H' cond=7 to member#7 (cost 0)
    - GIVE item '\x19' cond=93 to member#7 (cost 0)
    - SET flag 0x1f12=1
- text: @5謹慎地四下張望一番，接著掀開帳篷簾布，悄悄溜了進去，@3則留在外頭把風。  地上鋪著一張睡墊，一只小箱子裡裝著些許糧食。帳篷壁上有樣東西吸引了他的目光，他湊近細看，原以為是某種訊息，結果不過是塊污漬。他後退一步，一腳踩在睡墊中央的硬物上，掀開睡墊一看，底下竟藏著一條莫瑞德七鰓鰻！

## node 3100106  (DIAL_Z31#341)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f13 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#342
- speaker=0  style=6
- effects:
    - SET flag 0x1f13=1
- text: 雖然聽不懂莫瑞德語，但帳篷裡傳出的大聲說話聲，聽起來像是一戶小家庭住在裡頭。  「莫瑞德人治家挺嚴格的，」@5聽著裡頭嚴厲的斥責聲，說道。「或許我們該挑個更合適的時機再來。」

## node 3100107  (DIAL_Z31#343)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f14 in [20152..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#344
- speaker=0  style=6
- effects:
    - SET flag 0x1f14=1
- text: 一名老邁的莫瑞德人應了他們的呼喚。儘管眼前這群人組合古怪，他還是讓他們進了帳篷。  他用王國語跟他們說話。「你們身上穿的東西是戰場上奪來的？還是代表著真正的效忠？」  @5趕忙答道：「我們來自王國，不過我們只臣服於兩樣東西：金子跟銀子。」  這名莫瑞德人似乎對這答案感到滿意，又或者只是累得懶得計較。他示意眾人坐下。  簡短交談後，他們得知他是特地來拉格蘭姆等死的。他年事已高，跟不上族人遷徙的腳步，又不願獨自留在拉格蘭姆，於是決意漫步走入森林，讓生命像風穿過林梢般悄然逝去。  ...

## node 3100108  (DIAL_Z31#345)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f15 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#346
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f15=1
- text: @5大聲敲了敲門。  原以為會是名莫瑞德人應門，眾人倒有些訝異——來開門的竟是個牛壯的彪形大漢。  他狐疑地打量他們一番，開口道：「伊夏神的母親啊！瞧瞧這是誰。王國的狗兒也來討骨頭了，」他朝@3冷笑一聲，接著咆哮道：「你們最好滾回自己該待的地方去！這裡沒你們這種人的活兒幹。快滾！」  為免招惹全鎮的人都撲上來，@5同意還是離開為妙。

## node 3100317  (DIAL_Z31#347)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[25] (xor=0xd6 mask=0x8e mode=1 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#349
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[25] (xor=0xf3 mask=0x8e mode=1 chapters=-)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#350
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#351
- speaker=0  style=6
- effects:
    - GIVE item 'x' cond=21 to member#5 (cost 0)
    - GIVE item '\x1c' cond=100 to member#5 (cost 0)
    - GIVE gold +1500
    - event_bitmap_hi[25] bitop
- text: 門虛掩著。  @5試著推門進屋，卻感覺有什麼東西擋住了門。他稍微用力一推，門才勉強又開了一些。  朝昏暗的房間望去，只見地上倒著一具男性莫瑞德人的身影。克洛戴克的屍體蜷縮成胎兒般的姿勢，雙手似乎正緊掐著自己的喉嚨。  「這名工程師手藝確實高明，」他說。「那發投石機彈藥看來效果十足。快搜這房間。」  搜索了幾分鐘後，@3喊道：「我好像找到東西了。」  角落一張木製書桌後方，藏著一把林絲克拉格瑪之劍、一只裝有一百五十枚金幣的小袋子，以及一份部隊命令。這下莫瑞德人的攻擊計畫可要亂了...

## node 3100318  (DIAL_Z31#352)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[25] (xor=0xb4 mask=0x4e mode=47 chapters=8)] -> node 16896
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#353
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [37845..1]] -> node 4294901761
    - [flag 0x0101 in [37672..1]] -> node 4294901761
- text: 一名古怪的老精靈應了門。  他挑起眉毛，狐疑地瞪著派特魯斯，說：「什麼事！？是吟遊詩人艾隆派你們來為我獻唱的嗎？」

### (sub) DIAL_Z31#354
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 0
- text: 「那你們幹嘛來煩我！？」那莫瑞德人尖聲吼道。  他們還沒來得及分辯，他已經氣沖沖地衝回屋裡，砰地一聲甩上厚重的木門。

### (sub) DIAL_Z31#355
- speaker=0  style=6
- effects:
    - bind speaker-name slot (kind=0 sub=6)
    - read Barding -> dlg-result (sel=2)
- branches:
    - [flag 0x753d in [38205..1]] -> node 4294901830
    - [flag 0x753d in [38234..1]] -> node 4294901815
    - [flag 0x753d in [38263..1]] -> node 4294901800
    - [always] -> node 0 (no jump)
- text: 「那好，進來吧！」他招呼眾人進屋。「我正忙著呢，不過有音樂陪著我做事效率好多了。有助於思考！」  「您在忙些什麼樣的工作？」派特魯斯問道。  那莫瑞德人皺起眉頭。「你們是來唱歌的還是來問東問西的？角落有把魯特琴——自己拿去彈。」

### (sub) DIAL_Z31#356
- speaker=0  style=0
- effects:
    - play sfx 0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#357
- speaker=0  style=0
- effects:
    - play sfx 0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#358
- speaker=0  style=0
- effects:
    - play sfx 0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#360
- speaker=0  style=6
- effects:
    - event_bitmap_hi[25] bitop
    - play sfx 0
- text: 派特魯斯彈得亂七八糟。  以他的程度來說，這倒是輕而易舉。幸好，這正是老莫瑞德人愛聽的調調。他咕噥了幾句，說自己「彈得更好」，聽起來心情頗為愉悅，不一會兒便滔滔講起自己的工作。  「我ñ本來在替克洛戴克隊長打造一台投石機，可那愛龍成癖的傢伙做完了卻不肯付錢。所以我就好好『修理』了他一頓……拆掉了一個關鍵齒輪，現在那玩意兒完全動不了了。」  這名莫瑞德人笑了起來，接著又露出狡黠的笑容繼續說道：「我後來把它搬到他家射程範圍內，裝上了魔法毒藥。哪天我把那個齒輪裝回去，克洛戴克隊長就...

## node 3100113  (DIAL_Z31#361)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f16 in [20152..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#362
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f16=1
- text: 應戈拉斯敲門聲而來的莫瑞德人，臉上有一道從眼睛上方一路延伸到下巴底下的長長疤痕。他用莫瑞德語向他們打招呼。「在下格拉萊克。你們來此何事？」  戈拉斯問能否進屋，這名莫瑞德人勉強答應了。領他們進屋時，歐文注意到他的右腿幾乎使不上力。  他一瘸一拐地走進屋內，向戈拉斯解釋自己這番殘疾：「當年我跟隨穆爾曼達穆斯攻入王國領土。我們攻打一座固若金湯的要塞，就在終於攻破的那一刻，地獄業火將我們吞沒。從此我再也無法征戰。我的同胞如今追隨新的首領，此刻正籌備新一輪的攻勢！我血液裡燃燒著加入他...

## node 3100114  (DIAL_Z31#363)
- speaker=0  style=0
- branches:
    - [flag 0x1f17 in [42699..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#364
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1f17=1
- branches:
    - [flag 0x0100 in [42040..1]] -> node 4294901761
    - [flag 0x0101 in [41767..1]] -> node 4294901761
- text: 小小的井口冒出陣陣蒸氣。  歐文把雙手懸在井口上方，能感覺到底下水面傳來的熱氣。  「把飲水的井挖在離河這麼近的地方，倒是有點怪，不過我聽過這種特殊井水的傳說。據說井水具有輕微的治療效果。我們要不要喝一口？」

### (sub) DIAL_Z31#366
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - RAISE Health+Stamina of party by 2560..3840
- text: 戈拉斯從井裡舀了些水，等它稍微涼一些後啜了一小口。這水讓他覺得暖和，也沒有奇怪的味道或氣味。他等著看嘴巴或舌頭會不會出現麻痺的徵兆，過了幾分鐘依然安然無恙，便招呼歐文跟他一起喝。  這水讓歐文從內心感到一股暖意，幾分鐘後他覺得自己精神了不少。  「我們帶點這麼好的水上路吧，」戈拉斯說著，從行囊裡取出水袋。  「不行！」歐文說。「照那個傳說的說法，這水喝多了可能有毒。我們還是再喝一口就上路吧。」

### (sub) DIAL_Z31#367
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [43003..1]] -> node 4294901761
    - [flag 0x0101 in [42881..1]] -> node 4294901761
- text: 那口井靜靜矗立在他們面前，透著一股不祥的氣息。  戈拉斯想起歐文關於喝太多水的警告。「我們該再喝一口嗎？」他問道。

### (sub) DIAL_Z31#369
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - DAMAGE Health+Stamina of party by -7680..-5120
    - apply status/condition to member#5 idx=2 amt=10
- text: 戈拉斯又從井裡舀了些水，稍微放涼後喝了一口。味道跟先前一樣。他又等了幾分鐘，才招呼歐文再喝一口。  歐文正把水杯舉到唇邊、正要喝下時，戈拉斯忽然把杯子從他手中打落，水灑了一地。  「可是你剛才不是說要再喝一——」歐文才開口，注意到戈拉斯臉色發白，便住了口。  「恐怕你說對了，年輕的朋友。好東西有時也不能貪多。我們該走了。」

## node 3100118  (DIAL_Z31#370)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100119  (DIAL_Z31#372)
- speaker=0  style=6
- text: 戈拉斯望著這口小井，不由得想起它落成的那一天。井坑才剛挖好，天就下起雨來，一連下了好幾個鐘頭，讓收尾的工作變成一團泥濘濕滑的爛攤子。  他想起朋友卓艾列克一個踉蹌摔進一大灘泥水裡，忍不住微微一笑。當時大家笑得多開心啊！  笑容卻漸漸淡去——他想起卓艾列克追隨穆爾曼達穆斯離去的那一天，從此再也沒有回來。  「走吧，」戈拉斯說。「我們把水袋裝滿，離開這個地方。」

## node 3100120  (DIAL_Z31#373)
- speaker=0  style=0
- branches:
    - [flag 0x1f18 in [20146..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#374
- speaker=0  style=6
- effects:
    - SET flag 0x1f18=1
- text: 這頂小帳篷跟其他的看起來沒什麼兩樣。  歐文掀開前簾往裡頭望去。  「留下這些帳篷的人，走得肯定挺匆忙的，是吧？」他問道。  戈拉斯正掃視著遠方，聞言搖了搖頭。「是啊，這確實透著古怪。進去看看吧，說不定他們走得匆忙，留下了什麼東西。」

## node 3100338  (DIAL_Z31#375)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: @4走近那頂小帳篷。  「從這帳篷封起來的樣子看，」他低聲說，「我猜就算ñ真有人在裡頭，恐怕也不想現在被打擾。」

## node 3100121  (DIAL_Z31#376)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f19 in [45791..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#377
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1f19=1
- text: 戈拉斯敲了敲木門，耐心地等候回應。  門開了，他低頭一看，是個小孩子。孩子見到戈拉斯，雙眼睜得老大；見到歐文，眼睛睜得更大了，隨即躲回屋裡，這時孩子的母親走上前來。  她用莫瑞德語跟戈拉斯交談，語氣彷彿與他相識，卻不時朝歐文皺眉。  她讓孩子端來些清水，又跟戈拉斯多說了幾句話，便關上了門。  「她丈夫跟這一帶大多數男丁都跟著迪勒肯出征去了。婦孺只能自己想辦法過活。」  「你們族人就這麼輕易拋下一切嗎？」歐文問道。  戈拉斯神情黯然地轉向這名年輕法師：「他們別無選擇。」

### (sub) DIAL_Z31#378
- speaker=0  style=0
- effects:
    - (on-exit) play sfx 0
- text: 一張熟悉的女性面孔應了門。  @4跟那名婦人聊了一會兒，門關上後便退了開來。「她沒有新消息可以告訴我們。」

## node 3100122  (DIAL_Z31#379)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f1a in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#380
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
    - SET flag 0x1f1a=1
- text: 戈拉斯朝那扇門皺了皺眉，轉身正要離開。  「等等！」歐文喊道。「你要去哪？你認識住在這裡的人還是怎樣？」  戈拉斯有些不耐煩地轉過身，走回門前，輕輕敲了敲門。  「看起來這裡沒——」話還沒說完，門就吱呀一聲開了，打斷了他。門在他身後，所以只有歐文能看見戈拉斯臉上那副痛苦的表情。他緩緩轉過身去。  那名女性莫瑞德人一眼就認出了他，顯然兩人相識。她朝戈拉斯露出一抹曖昧的笑容，不由分說便把他拉進屋裡，留下歐文獨自站在門外。  幾分鐘後，戈拉斯倒退著走出屋子，一邊點著頭。  「那是怎...

## node 3100126  (DIAL_Z31#381)
- speaker=0  style=0
- branches:
    - [flag 0x1f1b in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#382
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1f1b=1
- text: 戈拉斯敲了敲門，儘管他確信不會有人應答。  門似乎沒上鎖，他用肩膀使勁一撞，便把門撞開了。  屋裡擺著一張小桌子、幾把椅子，還有幾張小床。屋主顯然把所有方便攜帶的東西都帶走了。  「四處看看吧，歐文。說不定能找到什麼能用的東西。」

## node 3100127  (DIAL_Z31#383)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[23] (xor=0x63 mask=0xb9 mode=1 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#385
- speaker=0  style=0
- branches:
    - [flag 0x1978 in [47766..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#386
- speaker=244  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [47907..1]] -> node 4294901761
    - [flag 0x0101 in [49243..1]] -> node 4294901761
- text: 這應該就是『納拉爾之肋』了。我們找到的紙條上寫著，要把一顆綠寶石放進頂端的凹槽裡。你怎麼看？

### (sub) DIAL_Z31#387
- speaker=0  style=0
- branches:
    - [flag 0xc388 in [47936..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#388
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
    - SET flag 0x1a7a=1
    - SET flag 0x1a7b=1
    - event_bitmap_hi[23] bitop
    - REMOVE item '8' cond=1
    - ACTION: mark region encounter #0 defended (roster killed)
- text: @4取出一顆綠寶石，小心翼翼地捧到石板前。離石板還有好幾步遠時，寶石在他手中就開始發燙，等他走到石板前，寶石已經劈啪作響，像被敲擊的燧石般迸出點點火花。他費了好大力氣才沒讓它滑落塵土之中。  他強忍著隨每一寸靠近而愈發劇烈的疼痛，把綠寶石硬塞進石板頂端的凹槽裡。  一股能量爆發，將他猛地震倒在地。  眾人遮住雙眼，抵擋著石板上湧出的漩渦般光芒，只見它閃爍搏動、發出尖嘯與哀鳴，感受到那股比雷雨風暴更加猛烈的能量灼燒、竄流全身。  這一切來得突然，結束得也一樣突然。眾人仍渾身顫抖...

### (sub) DIAL_Z31#389
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 眾人仔細檢視著這塊石板。  石板另一側，他們的目光被頂端一處焦黑凹槽裡幾點閃亮的綠色斑點所吸引。

## node 3100359  (DIAL_Z31#393)
- speaker=0  style=0
- text: @4走近石板。  他仔細端詳了好幾分鐘，手指劃過石面上十二個無法辨識的符文。「看起來就是塊普通的大石板，」他說。「我原本還期待它有點什麼別的名堂。畢竟它這麼顯眼，我還在想會不會哪裡有個凹槽或溝痕。說不定是某種標記……」

## node 3100367  (DIAL_Z31#394)
- speaker=0  style=0
- text: 帕格注意到房間角落的生命石。  馬卡拉搶先一步到了！他飛快瞥了歐文一眼，心中浮現一個念頭——要是這名圖蘭尼至尊法師釋放出瓦爾赫魯那股駭人的力量，這個世界將失去多少純真。他不由自主地打了個寒顫，隨即將注意力轉回馬卡拉身上。

## node 3100129  (DIAL_Z31#395)
- speaker=0  style=0
- branches:
    - [flag 0x1f1c in [20002..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#396
- speaker=0  style=6
- effects:
    - SET flag 0x1f1c=1
- text: 帳篷敞開著，裡頭卻空無一人。  戈拉斯在外頭把風，歐文則進去查看。帳篷一側牆邊堆著幾疊木材跟一些木工工具，另一側放著幾只未完工的箱子。  「有發現什麼嗎？」戈拉斯在外頭喊道。  「沒有，就一些木材跟工具。看起來像是有人在做箱子。」  沉默片刻後，歐文聽見戈拉斯說：「是啊，也可能是在拆箱子。」

## node 3100130  (DIAL_Z31#397)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f1e in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#398
- speaker=0  style=6
- effects:
    - SET flag 0x1f1e=1
- text: 走近帳篷時，歐文聽見裡頭傳出有人在忙活的聲音。  聲音忽然停了下來。戈拉斯用莫瑞德語喊了聲招呼，片刻後，一名矮小的莫瑞德人加入了他們。  「哎呀，我這位神出鬼沒的朋友，」他說，「我聽說你被重新抓回去了，看來你又一次躲過了迪勒肯的手掌心。綠心氏族其他人怎麼樣了？」  戈拉斯朝這名莫瑞德人身後的帳篷瞥了一眼，緩緩答道：「有些逃了，有些被迪勒肯強徵入伍。老朋友，那你呢？你的故事是什麼？」  「我沒有任何效忠對象。我這艘船，向來只聽那個最不容易害我送命的船長掌舵。如今我替即將到來的大...

## node 3100132  (DIAL_Z31#399)
- speaker=0  style=0
- branches:
    - [flag 0x1f1f in [20154..32815]] -> node 4294901761
    - [flag 0x1f20 in [52790..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#401
- speaker=0  style=6
- effects:
    - SET flag 0x1f1f=1
    - GIVE item '\x85' cond=20 to member#5 (cost 0)
- text: 站在這座建於法師故居殘垣上的帳篷裡，歐文感受到跟先前在井邊一樣的古怪力量。  循著先前在腦海中閃過、如今依然烙印其中的畫面指引，他走到帳篷東北角開始挖掘。戈拉斯也加入幫忙，才挖下幾吋，指尖便觸到一只小箱子的木製邊框。  把箱子從泥土中挖出來後，歐文往裡頭一看……箱裡只有一卷魔法卷軸，他趕忙取出，隨後兩人便離開了。

## node 3100133  (DIAL_Z31#402)
- speaker=0  style=0
- branches:
    - [flag 0x1f20 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#403
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [54095..1]] -> node 4294901761
    - [flag 0x0101 in [53998..1]] -> node 4294901761
- text: 站在這口井前，歐文感到一陣異樣，彷彿有千百雙眼睛正盯著他，凝視著他，灼燒著他的靈魂。他不由自主地打了個寒顫。  「據說這口井蘊藏著特殊的力量，只是很少有人能真正喝下井水，」戈拉斯說。  「為什麼？」歐文問道，仍舊顫抖著。  戈拉斯緩緩轉身，低頭看向歐文。「因為它非常危險——而且唯有修習法術之人才能承受它的力量而不受傷害。這由你自己決定，年輕的朋友。你想喝這口井的水嗎，歐文？」

### (sub) DIAL_Z31#405
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f20=1
- text: 歐文喝了一口這神奇的井水。  起初似乎沒什麼變化，只有心臟強烈地跳動著——而且早在水碰到嘴唇之前，那陣心跳就已經開始了。接著，色彩緩緩在他眼前旋轉，宛如一道長著翅膀的彩虹，時而俯衝、時而翱翔，在空中織出一幅幅絢麗的光與色的圖案。愈轉愈快，交融碰撞，終於凝聚出一幅影像。歐文不敢眨眼，深怕哪怕只是一瞬間的閉眼，這一切就會消失無蹤。  接著它「開口」了——不是用言語，而是用一連串意象與畫面湧入歐文的腦海。它們像蜂群一樣在他腦中嗡嗡亂竄，直到他覺得自己再也承受不住，才終於消散。  「...

## node 3100136  (DIAL_Z31#406)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f21 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#407
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f21=1
- text: 一名年輕的女性莫瑞德人應了戈拉斯的敲門聲。  「你幹嘛把這條王國的狗帶到我家門口？」她用莫瑞德語質問道，目光盯著歐文。  「他是我養的……寵物，」戈拉斯答道。「他會耍些法術小把戲逗我開心。」  這話讓兩人都覺得挺好笑，忍不住放聲大笑。歐文聽不懂這語言，只能一臉困惑地站在一旁。  「哈勒克這邊有什麼消息？」戈拉斯問道。  「能打仗的都往北去薩薩戈斯了。迪勒肯自己也在耍些法術把戲。聽說六人議會的法力相當高強。」  他們又聊了一會兒，歐文則在一旁坐立不安。門終於關上後，歐文問道：「...

## node 3100138  (DIAL_Z31#408)
- speaker=0  style=0
- branches:
    - [flag 0xcb24 in [50888..32813]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100139  (DIAL_Z31#410)
- speaker=0  style=0
- branches:
    - [flag 0x1fb7 in [56317..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#411
- speaker=0  style=6
- effects:
    - SET flag 0x1fb7=1
- text: @3在門前遲疑了一下，還沒敲門。  屋裡傳出幾個男人用外語爭論的聲音，忽然，一個聲音蓋過了其他人。「……你們得說慢一點。你們也知道我這語言說得多爛。拜託，拜託……」  另一個聲音接話：「那我們就用王國語說吧。問題還是沒解決。這些雙足飛龍很可能會掙脫我們用來束縛牠們的法術。這些爬蟲類意志相當頑強。」  「還不至於，」又一個聲音說道。「就算真的失控，我們還是能靠那個小道法術重新掌控牠們，叫什麼來著？『主人之意』。不過那需要實體媒介，對吧？牠們的一顆蛋？」  爭論的聲調沉寂了好一陣...

## node 3100140  (DIAL_Z31#413)
- speaker=0  style=0
- branches:
    - [flag 0x1f22 in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#414
- speaker=0  style=6
- effects:
    - SET flag 0x1f22=1
- text: 這些帳篷的位置，恰好卡在一支從薩薩戈斯南下、朝高堡駐軍進發的大軍必經之路上。  戈拉斯掀開簾布，往帳篷裡瞧了瞧。「歐文，我在外頭把風，你進去看看。」  歐文依言照做。他讓雙眼適應帳篷內昏暗的光線，開始仔細搜索……

## node 3100142  (DIAL_Z31#415)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f23 in [20154..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#416
- speaker=0  style=6
- effects:
    - SET flag 0x1f23=1
    - GIVE gold +250
- text: 帳篷裡傳出一陣窸窸窣窣的聲響。  戈拉斯謹慎地靠近，正要低聲跟歐文說些什麼，忽然停下腳步，緊皺的眉頭透露出深深的戒備。  毫無預警地，一名體型碩大的哥布林從帳篷裡撲出，一把抓住戈拉斯。兩人扭打成一團，被拖回了帳篷內。歐文還來不及上前幫忙，一聲清脆的骨折聲響起，戰鬥便結束了！  歐文衝進帳篷，只見戈拉斯正提著一具已經斷氣的哥布林屍體，牠的頭以極其詭異的角度扭向一側。屍體悶悶一聲摔落在泥地上。  眾人徹底搜查了屍體與帳篷，在角落找到一只小箱子，裡頭裝著二十五枚金幣，還有一份待售物...

## node 3100143  (DIAL_Z31#417)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f24 in [20154..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#418
- speaker=0  style=6
- effects:
    - SET flag 0x1f24=1
- text: 歐文跟戈拉斯小心翼翼地潛近帳篷，往裡頭窺看。帳篷本身看似出自莫瑞德人之手，裡頭那幾樣物品卻不是。  「這裡沒什麼值錢的東西，」戈拉斯低聲道。「不過這肯定是哥布林的居所。這一帶我們得格外小心才行。」

## node 3100148  (DIAL_Z31#419)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100252  (DIAL_Z31#420)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f25 in [60825..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#421
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f25=1
- text: 他們敲了敲門，等候回應。  一陣窸窸窣窣的聲響後，門開了，一名矮人出現在他們眼前。「哎呀，真是稀客。是什麼風把兩位小夥子吹來這麼遠的地方？」  他邀請他們進屋，還提供清水裝滿水袋。他問起他們的旅程，眾人簡短說明了一番。  「這麼說，你們也聽說精靈那邊出的麻煩事了？」他問道。  「麻煩事？」歐文疑惑地問。  「沒錯。真是見鬼的事！小龍一直在攻擊艾爾凡達。戰帥托馬斯已經竭盡全力抵擋，可畢竟一個人能做的有限。」  他又多聊了些這些攻擊事件，還提到麥克莫丹卡達爾裡出現的一種怪異的岩石...

## node 3100157  (DIAL_Z31#423)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f26 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#424
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=0 a2=0
- branches:
    - [flag 0x0100 in [61857..1]] -> node 4294901761
    - [flag 0x0101 in [19966..32815]] -> node 4294901761
- text: 歐文敲了敲門。一股帶著山胡桃木香氣的煙斗煙霧從門縫底下鑽出，輕輕繚繞在他腳邊。  煙味才剛飄進鼻腔，門就猛地打開，一名笑容滿面的矮人迎了上來，「好日子啊！進來吧，小夥子們，一起來玩。」  從他左肩望過去，能看見另外幾名矮人圍坐在一張小木桌旁，正把幾顆小方石往桌上擲。  互相介紹過後，他們受邀加入這場遊戲。「只要五枚金幣，怎麼樣？」

## node 3100158  (DIAL_Z31#425)
- speaker=0  style=6
- text: 「我看這幾個俊小子是怕了，」一名矮人說道。「當初就不該找他們來玩。」  眾人在一陣噓聲跟嘲弄中離去。

### (sub) DIAL_Z31#426
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [61886..1]] -> node 4294901765
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#427
- speaker=0  style=6  flags=paged-text
- effects:
    - TAKE gold -50
- branches:
    - [flag 0x0100 in [62317..1]] -> node 4294901761
    - [flag 0x0101 in [19966..32815]] -> node 4294901761
- text: 眾人圍在桌邊，歐文也分到一顆骰石，數到三後大家一起把石頭擲到桌上。  「克拉普卡！」一名矮人喊道，一把抓起歐文擲出的骰石。「你輸了，小夥子。」他把所有的錢幣都摟進懷裡。  「什麼？！」歐文喊道。  「那是雙龍啊！誰先喊出『克拉普卡』並搶到對方的骰石，誰就贏，」那矮人說。「要不要再來一局？」

### (sub) DIAL_Z31#428
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [62346..1]] -> node 4294901765
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#429
- speaker=0  style=6  flags=paged-text
- effects:
    - TAKE gold -50
- branches:
    - [flag 0x0100 in [62842..1]] -> node 4294901761
    - [flag 0x0101 in [19966..32815]] -> node 4294901761
- text: 「好樣的！錢都丟進盆裡，把石頭撿起來。」  眾人再次數到三，把骰石擲上桌。  這次兩名矮人興奮地跳了起來，喊道：「沃卡，沃卡！」他們撿起骰石又擲了一次。第二輪擲完，一名矮人猛地一拳砸在桌上，另一名則咧嘴笑著把所有錢幣摟進懷裡。  「唉呀，沃卡骰。要不要再賭一把手氣，小夥子們？」

### (sub) DIAL_Z31#430
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [62871..1]] -> node 4294901765
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#431
- speaker=0  style=6  flags=paged-text
- effects:
    - TAKE gold -50
- branches:
    - [flag 0x0100 in [63229..1]] -> node 4294901761
    - [flag 0x0101 in [19966..32815]] -> node 4294901761
- text: 「很好。我看你的運氣要轉了，」那矮人說。  眾人第三次把骰石擲上桌，骰面上古怪的紋路隨著骰石在桌上彈跳翻轉，看得眼花撩亂。  「留桌！」一名矮人歡快地喊道。「所有錢幣留在桌上。要不要再來一局？」

### (sub) DIAL_Z31#432
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [63258..1]] -> node 4294901765
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#433
- speaker=0  style=6
- effects:
    - SET flag 0x1f26=1
    - GIVE gold +1500
- text: 歐文又往桌上丟了五枚金幣。數到三後，他再次擲出骰石。  這回骰石落定後，全場一片驚愕的寂靜，矮人們個個瞪大眼睛盯著桌面。  「唉呀！」一名矮人喊道。「不可能！」其他人也紛紛附和，很快便用歐文聽不懂的語言竊竊私語、爭論不休。  最後，在其他人厭惡的目光中，最先來應門的那名矮人開了口：「小夥子，你擲出了龍。」見對方似乎沒聽懂這話的分量，他又接著說：「你擲出了龍，我們大家全擲出了沃卡！」  「這麼說我們贏了？」歐文仍一頭霧水地問道。  「乾脆殺了我算了。沒錯！你們全贏走了！」其他矮...

## node 3100160  (DIAL_Z31#435)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100161  (DIAL_Z31#436)
- speaker=0  style=6
- text: 這棟房子似乎已經荒廢。  眾人撬開前門，小心翼翼地走了進去。屋裡擺著各式各樣的家具，想必是因為太重或太笨重而搬不走。儘管看起來沒什麼值錢的東西，這棟房子還是值得仔細搜一搜……

## node 3100162  (DIAL_Z31#437)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f28 in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#438
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f28=1
- text: 歐文用拳側敲了敲門。  片刻後，屋裡傳出一個男聲：「你們想幹嘛？」  「能否請您給我們一些清水裝滿水袋？」歐文問道。  「路那頭有口井。現在別煩我。」  看來再多聊也是白費工夫，眾人便離開了。

## node 3100253  (DIAL_Z31#439)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f29 in [60825..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#440
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f29=1
- text: 第一次敲門沒人應答，歐文又敲了一次。  終於，一個帶著濃重矮人口音的沙啞聲音應了聲：「誰在敲我的門？」  「我們來自王國。可以進去嗎？」歐文問道。  「行啊。門沒鎖，隨你們便。」  他們推門走進一間光線昏暗、陳設簡陋的房間。角落裡隱約可見一個人影，似乎躺在一張睡墊上。  「進來吧，進來吧，歇歇腳吧，」那矮人有氣無力地說道。他閉著雙眼，彷彿正透過眼皮回看當時的景象，向他們說起自己從卡爾達拉一路而來的旅程，以及親眼見到盤旋在艾爾凡達上空的雙足飛龍。  「那些該死的莫瑞德人也到處亂...

## node 3100164  (DIAL_Z31#441)
- speaker=0  style=0
- branches:
    - [flag 0x1f2a in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#442
- speaker=0  style=0  flags=paged-text
- effects:
    - SET flag 0x1f2a=1
- branches:
    - [flag 0x0100 in [1370..2]] -> node 4294901761
    - [flag 0x0101 in [1162..2]] -> node 4294901761
- text: 歐文仔細端詳著這口井。看起來似乎沒什麼危險，不過眾人身處艾爾凡達邊境，什麼事都可能發生。  「看起來沒問題，」他轉向戈拉斯說道。「我要喝一口。」  「不行！」這名莫瑞德人命令道。「這口井該由我來喝。」  歐文望向戈拉斯。

### (sub) DIAL_Z31#444
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - apply status/condition to member#5 idx=3 amt=100
- text: 歐文點頭表示贊同。  戈拉斯舀了些水到手心，湊近鼻子聞了聞，接著仰頭把水倒進嘴裡吞了下去。  「感覺如何？」歐文問道。  「還不賴。也許我該再多喝一點。」  他又舀了些水，幾乎是貪婪地喝了下去。接著又喝了一些。  「我看這口井裡一定是治療之水，」戈拉斯說。「因為它讓我覺得……好極了。不過有點熱。你會熱嗎？」  歐文狐疑地打量著他，注意到戈拉斯的眼神已經開始渙散游移。「你……喝醉了。這口井裡到底裝的是什麼，純麥酒嗎？」  他一把抓住戈拉斯的手，把他拖離井邊。「走吧，我們得離開這...

## node 3100165  (DIAL_Z31#445)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1f2b in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#446
- speaker=0  style=6
- effects:
    - SET flag 0x1f2b=1
- text: 歐文正要敲門，忽然聽見小屋裡傳出響亮的說話聲。  他仔細聽了聽，卻聽不清楚在說什麼。他正要再敲一次，門忽然開了，三個吵吵鬧鬧、看起來醉醺醺的矮人衝了出來。  「……無盡海岸邊那些沙子？那都是我殺過的布拉克努爾留下的殘渣。沒錯！你們別不信——」那名吹噓的矮人一見到歐文跟戈拉斯，話音戛然而止，轉頭望向自己的同伴，滿臉鬍鬚上寫滿驚訝與戒備。  「你們在這裡幹嘛？」他質問道，目光飄向戈拉斯身後的某個東西。  「我們……呃……我們正要去艾爾凡達，」歐文說。  「那你們最好快走。這裡離那...

## node 3100167  (DIAL_Z31#447)
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [3604..2]] -> node 4294901761
    - [flag 0x0101 in [3474..2]] -> node 4294901761
- text: 戈拉斯抓住繩索，雙腳穩穩抵著樹幹，開始往上攀爬。歐文跟在後頭。  他們在一根寬闊的樹枝上停下，樹枝上撐著一間小屋。看起來似乎沒人在。  「我們進去看看嗎，年輕的歐文？」

### (sub) DIAL_Z31#448
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「既然你這麼決定，」戈拉斯說。他抓住繩索滑到地面，歐文跟著下來。

### (sub) DIAL_Z31#449
- speaker=0  style=6
- effects:
    - SET flag 0x1f2c=1
- text: 他們走進這間小小的樹屋。  「看起來屋主走得挺匆忙的，」歐文說。  房間另一頭，一張吊床式的床鋪底下，戈拉斯發現了一只箱子，箱蓋上畫滿了火紅色的古怪符文，鮮豔奪目。  他小心翼翼地掀開箱蓋，往裡頭看去……

## node 3100168  (DIAL_Z31#450)
- speaker=0  style=0
- branches:
    - [flag 0x1f2d in [5118..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#451
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [4713..2]] -> node 4294901761
    - [flag 0x0101 in [4441..2]] -> node 4294901761
- text: 歐文抓住繩索爬上樹。到了頂端，他招呼戈拉斯，對方很快也跟了上來。  「看起來裡頭沒人，」歐文喘著氣說。他挪到屋子側邊，每一步都小心翼翼地試探，接著雙手圈在臉頰兩側，把鼻子貼上一扇小窗往裡頭望去。  「真不敢相信，」他說。「裡頭好像有只裝滿錢的寶箱。我們進去拿吧。」

### (sub) DIAL_Z31#453
- speaker=0  style=6
- effects:
    - play sfx 0
    - DAMAGE Health+Stamina of party by -12800..-6400
    - SET flag 0x1f2d=1
- text: 「不行！」戈拉斯喊道，卻已經來不及阻止這名年輕法師了。  歐文猛地推開門，眼裡依然閃著他篤定會找到的寶藏光芒。然而映入眼簾的並非金銀的閃耀，而是一陣刺眼白光——一場小爆炸將兩人猛然震飛，摔出樹屋，直落將近三十呎下的地面。

## node 3100169  (DIAL_Z31#455)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20537..2]] -> node 4294901761
    - [flag 0x1f2e in [6649..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#456
- speaker=0  style=6
- effects:
    - SET flag 0x1f2e=1
- text: 他們沿繩索爬上將近三十呎高，站到一間小樹屋前。  還沒來得及敲門，一個憤怒的女聲便喝道：「我可是有劍的，莫瑞德人，我不怕用它！給我滾！」  歐文喊道：「我們沒有惡意。我們有件十萬火急的口信要給戰帥托馬斯。您能幫我們找到他嗎？」  門開了一條縫，歐文能看見一隻眼睛跟一只長長的尖耳，一側還垂著幾綹烏黑的鬈髮。  「托馬斯正在抵禦攻擊我們邊境的雙足飛龍。等他回來，你們會在這裡的西北方找到他。」  歐文謝過她的幫忙，轉身去抓繩索。  「要是你們心懷不軌，休想活著見到托馬斯。」

### (sub) DIAL_Z31#457
- speaker=0  style=0
- effects:
    - play sfx 0
- text: 一張熟悉的面孔在門口迎接了他們。  聊了幾分鐘後，門關上了，@4轉身準備離開。  「她沒有新消息可以告訴我們，」他說。

## node 3100170  (DIAL_Z31#458)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20537..2]] -> node 4294901761
    - [flag 0x1f2f in [20148..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#459
- speaker=0  style=6
- effects:
    - SET flag 0x1f2f=1
- text: 粗糙的白色繩索在微風中輕輕搖擺。  「準備好了嗎？」戈拉斯問歐文，看得出來歐文對接下來這番攀爬工程一點都不期待。  「好啦，好啦。走吧，跟我來。」  他吃力地爬上樹頂，氣喘吁吁地轉身，看著戈拉斯毫不費力地跟了上來。  半山腰的這間小小精靈屋已經荒廢。眾人搜索屋內，發現幾只雕工精細的空箱子、一張吊床式的床鋪，還有一堆顯然是從缺了塊玻璃的後窗吹進來的枯葉。  他們正準備離開時，戈拉斯忽然瞥見頭頂樹梢間有些什麼。他爬上去想看個仔細，歐文則小心翼翼地沿著自己所在的樹枝往外挪。  撥開...

## node 3100171  (DIAL_Z31#460)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20537..2]] -> node 4294901761
    - [flag 0x1f30 in [8674..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#461
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - ?wOp12 a1=0 a2=0
    - SET flag 0x1f30=1
- text: 他們爬上樹頂，敲了敲這間小樹屋的門。  門緩緩開啟，露出一名皮膚黝黑、滿臉皺紋的精靈。他神情只帶著淡淡的戒備看著他們，片刻後便讓他們進了屋。  「在下法蘭，」他自我介紹道。接著他轉向戈拉斯：「這些年來，我見過不少『歸返者』，卻從沒見過像你這樣的。」  戈拉斯緩緩點了點頭，卻沒有開口。  法蘭跟他們說起北方來襲的雙足飛龍，以及精靈們如何拚死抵禦莫瑞德人入侵邊境。  告辭時，法蘭指了個方向，告訴他們戰帥托馬斯的下落。「他就在這裡正北方。祝你們好運。」

### (sub) DIAL_Z31#462
- speaker=0  style=0
- effects:
    - play sfx 0
- text: 一張熟悉的面孔在門口迎接了他們。  聊了幾分鐘後，門關上了，@4轉身準備離開。  「他沒有新消息可以告訴我們，」他說。

## node 3100172  (DIAL_Z31#463)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#464
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [9395..2]] -> node 4294901761
    - [flag 0x0101 in [9221..2]] -> node 4294901761
- text: 那條繩索宛如一條編織而成的白蛇，蜿蜒向上，沒入樹梢之中。  歐文雙手抓緊繩索，往上攀爬，戈拉斯緊隨在後。爬到樹頂，他們發現一間小屋，門前掛著一塊古怪的精靈風格招牌。  「一間店舖，年輕的歐文。我們要進去嗎？」戈拉斯問道。

### (sub) DIAL_Z31#465
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「那也許我們該回頭再來看看，」戈拉斯說。「裡頭說不定有什麼對我們有用的東西。」  他們爬下樹，準備離去。

## node 3100173  (DIAL_Z31#467)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f31 in [20154..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#468
- speaker=0  style=6
- effects:
    - SET flag 0x1f31=1
- text: 歐文走近帳篷時，聽見一個粗啞的聲音喝道：「什麼人？」  「歐文．貝勒佛特，還有戈……索爾加斯，一位精靈，」歐文喊道。  帳篷簾布掀開，一名魁梧的男子走出來，在空地上與他們會合。他自我介紹是布雷克．普傑，曾任里蘭儂萊亞姆王麾下的斥候。  「是什麼風把你們吹到這麼遠的地方來？」歐文好奇地問。  「我原本在卡達爾找寶藏，後來聽說莫瑞德人正朝艾爾凡達逼近。精靈們出了不少錢，請我幫忙擋住那些黑心的傢伙。」他狐疑地打量了戈拉斯一眼，接著繼續說：「目前還沒遇上太大的麻煩，倒是那些該死的雙足...

## node 3100174  (DIAL_Z31#469)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f33 in [11732..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#470
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1f33=1
- branches:
    - [flag 0x0100 in [11306..2]] -> node 4294901761
    - [flag 0x0101 in [10800..2]] -> node 4294901761
- text: 這頂軍用風格的小帳篷似乎空無一人。  附近泥地上的痕跡顯示這裡可能發生過一場打鬥，看那痕跡的樣子，歐文相當確定自己不想在這裡多待。  「我們要不要進去看看，年輕的朋友？」戈拉斯問道。

### (sub) DIAL_Z31#471
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 「看看你這決定是不是明智之舉，」戈拉斯說。他退後幾步，示意歐文照做，接著撿起一塊小石頭朝帳篷丟去。石頭發出一聲悶響，緊接著一陣刺目的爆炸將兩人雙雙震倒在地。  歐文從地上爬起來，抖了抖頭髮裡的塵土，轉向戈拉斯說：「下次你再幹這種事，讓我先退遠一點好嗎？退到ñ克朗多去都行。」

### (sub) DIAL_Z31#472
- speaker=0  style=6
- effects:
    - DAMAGE Health+Stamina of party by -19200..-10240
    - (on-exit) play sfx 0
- text: 戈拉斯小心翼翼地靠近這頂小帳篷，在簾布前停下腳步，一動也不動。  「我們就這麼乾站在外頭？進去吧！」歐文不耐煩地說。他推開戈拉斯，伸手拉開帳篷簾布。  千陽般的光芒在他們周圍炸開，一陣魔法風火猛然襲來，把他們踢翻、旋轉，狠狠掀翻在地！

## node 3100175  (DIAL_Z31#474)
- speaker=0  style=0
- branches:
    - [flag 0x1f34 in [13752..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#475
- speaker=0  style=0
- branches:
    - [flag 0xc3c3 in [13078..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#477
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [19985..32815]] -> node 4294901761
    - [flag 0x0101 in [20165..32815]] -> node 4294901761
- text: 這口井乍看之下十分尋常。  歐文俯身望向那砌著岩石的井口，戈拉斯則繞到井後方。他撥開纏繞井身的藤蔓，瞥見一塊金屬牌，上頭精美地刻著精靈文字。  「你發現了什麼？」歐文問道，走到井後跟戈拉斯會合。  「精靈管這口井叫『龍尾井』。當井裡的魔法之水與……」戈拉斯頓了頓，努力辨認上頭的文字，「……法達莫爾秘方……混合之後，便能增強飲用者的力量。」  「我們手上有一瓶。也許該試試這口魔法井，」歐文說。

### (sub) DIAL_Z31#478
- speaker=0  style=0
- effects:
    - SET flag 0x1f34=1
- branches:
    - [flag 0xc3c3 in [14243..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#479
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這就是龍尾井了。你覺得精靈們為什麼要這麼叫它？

### (sub) DIAL_Z31#480
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 據說井水跟法達莫爾秘方混合後能增強力量。當然，我們手上沒有這秘方。

### (sub) DIAL_Z31#481
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可這跟井的名字有什麼關係？

### (sub) DIAL_Z31#483
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [19985..32815]] -> node 4294901761
    - [flag 0x0101 in [20165..32815]] -> node 4294901761
- text: 「這是龍尾井，」歐文說。「我們手上不是有法達莫爾秘方嗎？」  「是啊，我想是有的。你真的想把它倒進井裡嗎，年輕的朋友？」

## node 3100357  (DIAL_Z31#484)
- speaker=0  style=6
- text: 「呃，不用了。也許我們還是別試了。反正我們也有更要緊的事要辦，」歐文緊張地望著那口井說。「我們改天再回來試試……你說是吧？」  戈拉斯沒有回應，逕自拿起行囊離去，歐文連忙跟了上去。

## node 3100177  (DIAL_Z31#485)
- speaker=0  style=0
- effects:
    - RAISE Strength of party by 768
    - (on-exit) play sfx 0
- text: 歐文取出裝著法達莫爾秘方的小瓶，緩緩把裡頭的東西倒進井裡。  「好像沒什麼動靜，」他說。「說不定這又是莫瑞德人的另一個把戲。」  「或許吧。不過這世上並非所有的魔法，都得伴著閃爍的光芒跟盤旋的火焰。」戈拉斯舀起一杯井水，湊到唇邊。瞥了一眼雙眼瞪得比平常大上一倍的歐文，他仰起頭，讓那清涼的液體湧入口中，滑下喉嚨。  一陣熱浪竄過全身，接著又是一陣寒意。他閉上雙眼，感覺無數看不見的細小指尖攫住了他的胸口，接著向外擴散，蔓延到雙臂雙腿，最後直達手腳。  那股感覺來得快，去得也快，轉...

## node 3100178  (DIAL_Z31#486)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20537..2]] -> node 4294901761
    - [flag 0x1f35 in [16993..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#487
- speaker=0  style=6
- effects:
    - ?wOp12 a1=0 a2=0
    - play sfx 0
    - SET flag 0x1f35=1
- text: 歐文沿著繩索爬上樹頂附近一根粗壯的樹枝。  戈拉斯緊跟在後，才剛攀上來，歐文便已敲響了這間小樹屋的門。  屋裡原本傳出的窸窸窣窣聲驟然停止。歐文扶著一根低垂的樹枝穩住身子，又敲了一次。  「請走開，」屋裡傳出一名年輕精靈的聲音。  歐文往門邊靠近了些。「我們不會傷害你。我們是托馬斯的朋友，得找到他。」  門緩緩開啟，一名年輕精靈走了出來。歐文望向他身後的房間，看見一只箱子跟幾只小瓶擺在一張小木桌上。  這名年輕精靈儘管明顯畏懼戈拉斯的存在，仍向歐文說起莫瑞德人跟雙足飛龍攻擊艾...

### (sub) DIAL_Z31#488
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: @4仍因剛才的攀爬而喘著氣，打量著這間樹屋。  「我看我們這趟爬得白費力氣了。這裡好像沒人在。」

## node 3100179  (DIAL_Z31#489)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20151..32815]] -> node 4294901761
    - [flag 0x1f36 in [18223..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#490
- speaker=0  style=6
- effects:
    - play sfx 0
    - play sfx 0
- text: 走近帳篷時，歐文聽見裡頭至少傳出兩個古怪的聲音。這時，戈拉斯已經拔出匕首，如貓一般伏在入口旁蓄勢待發。他示意歐文退後。  他以老練刺客般的身手猛地掀開帳篷簾布，衝了進去。歐文緊隨在後，準備隨時支援。可等他進去時，兩名莫瑞德士兵中已有一人倒在地上，雙手虛弱地掐著自己的喉嚨，鮮血噴濺在泥地上。  另一名士兵儘管猝不及防，仍設法抽出自己的匕首，拔劍面對戈拉斯。他虛晃了幾招，接著猛然撲上，劃傷了戈拉斯的手臂——正是那隻手臂，一把揪住他外套靠近手肘的地方，將他拽向前方，撞上戈拉斯刺出的...

## node 3100369  (DIAL_Z31#492)
- speaker=0  style=0
- branches:
    - [flag 0xc351 in [20128..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#493
- speaker=0  style=6
- effects:
    - SET flag 0x1f87=1
- text: 歐文輕輕推開那扇古怪的門。  他咬緊牙關，戒備著可能的突襲。眼見沒有動靜，他把門再推開了些，走了進去。  他驚訝地發現四面牆上布滿了難以辨識的符文與記號。房間遠處角落一只深色的箱子也吸引了他的注意。走近時，他感到指尖傳來一陣古怪的刺麻感，跟他每次施展特別強大的法術之前那種感覺頗為相似。這股感覺牽引著他，他甚至沒意識到其中可能潛藏的危險，便一把抓起箱子，掀開了蓋子。裡頭赫然是一支深色的水晶法杖！  他左手握著法杖，右手掌心朝上，低聲唸誦了一段簡單的咒語。火焰隨即從他掌心竄出。 ...

## node 3100339  (DIAL_Z31#494)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: @4遲疑了一下。  「我們來過這裡了，」他說。「我看不出再來一趟有什麼意義。」

## node 3100340  (DIAL_Z31#495)
- speaker=0  style=0
- text: @4遲疑了一下。  「考慮到眼下的狀況，我看再回這裡來不是個好主意。我們該離開了。」

## node 3100341  (DIAL_Z31#496)
- speaker=0  style=0
- text: 他們受到熱情款待。  一番閒聊、喝了一壺熱茶之後，他們婉拒了主人進一步的招待。「兩位真是太客氣了，」@4一邊說一邊拿起行囊。「我看我們該重新上路了。」

## node 3100342  (DIAL_Z31#497)
- speaker=0  style=0
- text: 這座穀倉看起來有些眼熟。  「我們來過這裡了，」@4說。眾人在裡頭探查了幾分鐘，沒發現什麼值得留意的東西，便離開了。

## node 3100343  (DIAL_Z31#498)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: @4走近那頂小帳篷。  「從這帳篷封起來的樣子看，」他低聲說，「就算真有人在裡頭，恐怕也不想現在被打擾。」

## node 3100344  (DIAL_Z31#499)
- speaker=0  style=0
- text: @5遲疑了一下。  他轉向@3說：「我看不出再回這裡來有什麼意義。我們該離開了。」

## node 3100346  (DIAL_Z31#500)
- speaker=0  style=0
- text: @4在帳篷前遲疑了一下。  「我們來過這裡了。我看不出再回來有什麼意義。」

### (sub) DIAL_Z31#501
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: @4仍因剛才的攀爬而喘著氣，打量著這間樹屋。  「我看我們這趟爬得白費力氣了。這裡好像沒人在。」

## node 3100181  (DIAL_Z31#502)
- speaker=0  style=0
- text: 這棟建築空無一人。  在@4的堅持下，眾人快速搜索了一番，卻沒發現什麼值得留意的東西，便繼續上路。

## node 3100182  (DIAL_Z31#503)
- speaker=0  style=0
- text: @4仍因剛才的攀爬而喘著氣，打量著這間樹屋。  「我看我們這趟爬得白費力氣了。這裡好像沒人在。」

## node 3100183  (DIAL_Z31#504)
- speaker=0  style=0
- text: 這座小屋已然荒廢。  「這裡與其說是住所，不如說是個擋風的地方，」@4說。他環顧四周，接著說：「看這破敗的樣子，我看已經很久沒人真正ñ住在這裡了。」

## node 3100184  (DIAL_Z31#505)
- speaker=0  style=0
- text: 他們走近這頂小帳篷。  @4掀開簾布，打量了一下裡頭的情況。「這帳篷已經有段時間沒人住了，」他說。

## node 3100185  (DIAL_Z31#506)
- speaker=0  style=0
- text: @4推開了門。  「看起來這裡以前是某種店舖，」他說。「不過現在沒人在這裡做生意了。」

## node 3100189  (DIAL_Z31#507)
- speaker=0  style=0
- text: @4推開了門。  「看起來這裡以前是某種神殿，」他說。「不過看樣子早已荒廢多時了。」

## node 3100190  (DIAL_Z31#508)
- speaker=0  style=0
- text: @4推開了門。  「看起來這裡以前是間客棧，」他說。「不過看樣子早已荒廢多時了。」

## node 3100191  (DIAL_Z31#509)
- speaker=0  style=0
- text: @4推開了木門。  「這裡已經很久沒人住了，」他環顧空蕩的房間，說道。

## node 3100192  (DIAL_Z31#510)
- speaker=0  style=0
- text: 這棟住所此刻空無一人。  @4走進屋裡四下查看，沒發現什麼值得留意的東西，便朝@0打了個手勢，兩人一起離開了這棟小屋。

## node 3100193  (DIAL_Z31#511)
- speaker=0  style=0
- text: 這棟房子此刻空無一人。  @4走進屋裡四下查看，沒發現什麼值得留意的東西，便轉身準備離開。「這裡沒什麼能用的東西。我們該趁其他人回來之前離開。」

## node 3100194  (DIAL_Z31#512)
- speaker=0  style=0
- text: @4掀開了帳篷簾布。  「這裡已經荒廢了，」@5環顧四周說道。「不過說不定原本住這裡的人留下了什麼能用的東西。我們看看吧。」

## node 3100195  (DIAL_Z31#513)
- speaker=0  style=0
- text: @4推開了門。  「這裡已經荒廢了，」@5環顧房間說道。「說不定原本住這裡的人留下了什麼能用的東西。我們看看吧。」

## node 3100347  (DIAL_Z31#514)
- speaker=0  style=0
- text: @4環顧這座小穀倉。  看牲畜種類如此繁雜，他猜想這大概是公用財產，說不定是鎮民共有的。  他四處翻找了幾分鐘，接著說：「這裡沒什麼值得留意的。我們走吧。」

## node 3100197  (DIAL_Z31#515)
- speaker=0  style=0
- text: @4推開了木造穀倉的門。  裡頭的畜欄關著一般常見的牲畜。穀倉地上鋪滿了乾草、塵土跟牲畜糞便混雜出的刺鼻氣味，燻得他直流眼淚。幾分鐘後離開時，他總算鬆了口氣。

## node 3100198  (DIAL_Z31#516)
- speaker=0  style=0
- text: @4走近那頂小帳篷，往裡頭窺了一眼。  「這裡已經很久沒人住了，」他說。「我們該離開了。」

## node 3100199  (DIAL_Z31#517)
- speaker=0  style=0
- text: @4推開了木門。  「這裡已經很久沒人住了，」他環顧空蕩的房間，說道。

## node 3100266  (DIAL_Z31#518)
- speaker=0  style=0
- text: @4推開了門。  「看起來這裡以前是間酒館，」他說。「不過看樣子早已荒廢多時了。」

## node 3100200  (DIAL_Z31#519)
- speaker=0  style=0
- text: 一陣雞鳴聲迎接了他們的到來。  @4拉開穀倉的門，往裡頭看了一眼。「看起來挺正常的，不過還是值得查看一下……」

## node 3100201  (DIAL_Z31#520)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100267  (DIAL_Z31#522)
- speaker=0  style=0
- text: @4走近那扇古怪的門。  他輕輕推開門，朝屋裡窺看，確定沒有其他人後才走了進去。「我們四處看看吧，」他說。「說不定能找到什麼能用的東西。」

## node 3100260  (DIAL_Z31#523)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100261  (DIAL_Z31#524)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100263  (DIAL_Z31#525)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1ef1 in [20144..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#526
- speaker=0  style=6
- effects:
    - SET flag 0x1ef1=1
- text: 這棟小屋原來住著一位身形削瘦、頭頂微禿的歷史學家，名叫凱林，他一邊替他們的行囊補滿清水，一邊說起古老的瓦爾赫魯，以及賽瑟儂附近那場相對晚近的大浩劫。  「我訪問過的人，那些住在賽瑟儂附近的居民，都說當時還以為世界末日到了——彷彿天幕本身被硬生生翻轉過來，天空中露出了另一個宇宙。他們全都提到了那場大爆炸……還有天空中盤旋的可怕飛獸……」他的聲音漸漸低了下去。「我想這多半跟那些曾經自由馳騁在這個世界上的龍族君王有關。總有一天我會把這一切都弄明白的。」  @4笑了。「我相信你會的，...

## node 3100264  (DIAL_Z31#527)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0xe1 mask=0x62 mode=2 chapters=-)] -> node 6160
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#528
- speaker=0  style=0
- effects:
    - SET flag 0x1c86=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#529
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100265  (DIAL_Z31#530)
- speaker=0  style=6
- effects:
    - SET flag 0x1a62=1
- text: @4慶幸自己的鑰匙管用，推開了門。  屋裡放著各式各樣的物品，包括一堆文件與帳冊、一張書桌跟一張小床。@4彎腰仔細查看那些文件，發現是某種稅務記錄。他還找到幾張署名為「ñ史戴倫ð」的字條。  「仔細搜這房間，」@4下令道。「說不定能找到什麼能用的東西。」

## node 3100202  (DIAL_Z31#531)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100203  (DIAL_Z31#532)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100204  (DIAL_Z31#533)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100205  (DIAL_Z31#534)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100271  (DIAL_Z31#535)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100206  (DIAL_Z31#536)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100207  (DIAL_Z31#537)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100208  (DIAL_Z31#538)
- speaker=0  style=6
- text: 穀倉的門上了鎖。  詹姆士悄悄繞到另一側，發現後牆外靠著一塊厚重的石板。在戈拉斯的幫助下，他們合力把石板挪開，露出幾片破損的木板，以及一個剛好夠他鑽過去的洞口。  他悄悄潛入那片幽暗的黑暗中，摸黑一寸寸挪動，直到腳尖碰到一個硬物。他蹲下身，臉上露出笑容，隱約辨認出那是一只木箱的輪廓，慶幸發現它並未上鎖……

## node 3100209  (DIAL_Z31#539)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100210  (DIAL_Z31#540)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100211  (DIAL_Z31#541)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100212  (DIAL_Z31#542)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100213  (DIAL_Z31#543)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100215  (DIAL_Z31#544)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100219  (DIAL_Z31#545)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100220  (DIAL_Z31#546)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100221  (DIAL_Z31#547)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100327  (DIAL_Z31#548)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這塊石板讓@3感到渾身不自在。  儘管如此，他還是走近了些，想仔細瞧瞧這塊古怪的岩石……

### (sub) DIAL_Z31#549
- speaker=243  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [27137..2]] -> node 4294901761
    - [flag 0x0101 in [26992..2]] -> node 4294901761
- text: 這是塊很不尋常的石頭。它似乎散發著一股古怪的能量，但我看不出那是什麼性質。我們該ñ碰它嗎？

### (sub) DIAL_Z31#551
- speaker=0  style=6
- effects:
    - REMOVE item '=' cond=0
    - REMOVE item 'D' cond=0
    - REMOVE item 'C' cond=0
    - REMOVE item 'E' cond=0
    - play sfx 0
    - play sfx 0
- text: @3上前一步，觸碰了那塊古怪的石頭。  雖然沒有真正爆炸，但他手指一碰上岩石表面，眾人都聽見了一聲巨響。  這聲響嚇了大家一跳，對@3的影響尤其嚴重，他一瞬間確信那是死亡女神親自來敲他的門了。  眾人花了好幾分鐘才回過神來，意識到這情況其實挺滑稽的，很快便一邊哈哈大笑，一邊收拾行囊準備離開。  這塊石頭顯然沒有惡意，儘管如此，@5仍不禁擔心，除了理智之外，他們是不是還丟了些什麼別的東西。

## node 3100222  (DIAL_Z31#552)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100223  (DIAL_Z31#553)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [37360..32801]] -> node 393222
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100224  (DIAL_Z31#554)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100328  (DIAL_Z31#555)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[16] (xor=0x25 mask=0x4e mode=47 chapters=8)] -> node 3741384704
    - [event_bitmap_hi[16] (xor=0x9f mask=0x6e mode=2 chapters=-)] -> node 4278256386
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#556
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 一把劍刃橫在他們面前，擋住了去路。  這突如其來的一揮嚇了@4一跳，他退後一步，滿臉輕蔑地打量著這名擋在路中央、神情嚴峻的守衛。「波斯維奇夫人此刻不便打擾，」守衛說。「我奉命誰都不准接近她。除非是克朗多親王親臨，否則誰都不准進去。」

### (sub) DIAL_Z31#557
- speaker=0  style=0
- effects:
    - END conversation, result=65535
    - event_bitmap_hi[16] bitop
- text: 守衛領著他們進了屋。  穿過牧場大門，經過幾間氣味格外刺鼻的馬廄，一名年長的婦人端坐在一張碩大的橡木長椅上，目光嚴厲、不假辭色地打量著圍坐在她四周地上的一群軍官。她抬起頭，顯然對議事被打斷相當不悅。  「什麼事？」她問@4。「你帶來了消息？」  「算是吧，」@4有些尷尬地說。他很快扼要說明了聽來的士兵不滿情緒，以及酒館缺乏補給的問題。  科瓦利斯伯爵怒氣沖沖地轉向@4，搖了搖頭。「真是ñ難以置信，你們竟為了這種芝麻小事打斷這場會議。」  「你沒有發言的權利，ñ伯爵ð，」波斯維...

## node 3100225  (DIAL_Z31#558)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100226  (DIAL_Z31#559)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100228  (DIAL_Z31#560)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100229  (DIAL_Z31#561)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100231  (DIAL_Z31#562)
- speaker=0  style=0
- branches:
    - [flag 0x1f75 in [32448..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是口不太尋常的井。  @4伸手摸了摸木製搖柄，試著轉動，卻發現卡住了。他彎下腰想找個更好的施力點，指尖卻摩擦到一個堅硬光滑的東西——是一把小小的圓鎖。

### (sub) DIAL_Z31#563
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我認得這種鎖。  從前有些男人會要求自己的女眷，在他們外出期間穿戴上ñ上鎖的內衣，以確保貞潔。

### (sub) DIAL_Z31#564
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 據傳說，這些男人只會把鑰匙交給自己最親近、最信任的朋友保管。自然而然，這些女眷會想盡辦法說服對方用鑰匙解開這件令人渾身不自在的東西，據說也因此滋生出不少偷情韻事。丈夫返家前，鎖總會被重新扣上，但解鎖之後，鑰匙往往就留在朋友手上，等下次丈夫再度外出時使用。與此同時，這些偷情的戀人有時會找一口廢棄的井，扣上這種鎖，再用鑰匙藏一張情書進去。

### (sub) DIAL_Z31#565
- speaker=244  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [31774..2]] -> node 4294901761
    - [flag 0x0101 in [31582..2]] -> node 4294901761
- text: 我們要不要試著打開它？

### (sub) DIAL_Z31#567
- speaker=0  style=0
- branches:
    - [flag 0xc38e in [31803..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#568
- speaker=0  style=6
- effects:
    - GIVE item 'a' cond=0 to member#6 (cost 0)
    - SET flag 0x1f75=1
- text: @4檢查了一下他們身上的鑰匙。  找到一把美德鑰匙後，他走到井邊，找到鎖孔，把小鑰匙插了進去，輕輕一轉。鎖有些生鏽，但幾秒鐘後，他還是成功轉動了鑰匙，發出一聲令人滿意的「喀嗒」聲。  把手解鎖後，他順時針搖動搖柄，轉了十來圈，乾涸的水桶便從井裡升了上來。眾人在桶裡翻找，發現一個沾滿泥土跟落葉的小東西——竟是一枚騎士棋子！

### (sub) DIAL_Z31#570
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100270  (DIAL_Z31#571)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100234  (DIAL_Z31#572)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100235  (DIAL_Z31#573)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 3100236  (DIAL_Z31#574)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100237  (DIAL_Z31#575)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100330  (DIAL_Z31#576)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100329  (DIAL_Z31#577)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20142..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100241  (DIAL_Z31#578)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100245  (DIAL_Z31#579)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

## node 3100248  (DIAL_Z31#580)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100249  (DIAL_Z31#581)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#582
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - play sfx 0
- text: 門鈴響了一聲。  @4才剛把門推開，店老闆已經迎上前來領他進屋……

## node 3100320  (DIAL_Z31#583)
- speaker=0  style=0
- text: @4推開了門。  這棟古怪的建築裡，擺放著各式各樣造型奇特的物品，有些是木製的，有些則是用岩石或水晶打造而成。  「我感覺這裡的空氣裡有股怪異的震動，」@0說。「這地方跟我們見過的其他地方都不一樣，也許該四處看看……」

## node 3100353  (DIAL_Z31#584)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100354  (DIAL_Z31#585)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100355  (DIAL_Z31#586)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100360  (DIAL_Z31#587)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[4] (xor=0xb6 mask=0x4e mode=47 chapters=8)] -> node 4278272000
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z31#588
- speaker=0  style=6
- effects:
    - event_bitmap_hi[4] bitop
- branches:
    - [flag 0x1ec9 in [33612..2]] -> node 4294901761
- text: @4在這座大木造穀倉前停下腳步。  戰鬥的記憶仍鮮明地縈繞在他腦海，他輕輕推開門，悄悄溜進靜謐的黑暗之中。終於確認裡頭確實空無一人後，他搖著頭走了出來，示意大家離開。

### (sub) DIAL_Z31#589
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管情況看似如此，這感覺可不像是一場偶然的遭遇。

### (sub) DIAL_Z31#590
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是羅威的穀倉，你覺得這場襲擊跟他有關嗎？

### (sub) DIAL_Z31#591
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看那個混帳農夫是設局害我們的。他這番背叛最好是拿了不少好處，要是讓我再撞見他，我一定要從他身上討回這筆帳。

## node 3100356  (DIAL_Z31#593)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3100358  (DIAL_Z31#594)
- speaker=0  style=0
- text: @3伸手觸碰那根石柱。  手掌拂過冰涼的大理石表面，一陣劈啪作響的能量彷彿有千百根細針，輕輕啄咬著他的指尖。這感覺並不疼痛，卻讓他心裡發毛，趕忙縮回了手。  「這根石柱似乎蘊藏著某種魔法能量，」他說。「不過我完全說不出那究竟是什麼性質……也許我們該去看看其他幾根。」
