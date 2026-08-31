# DIAL_Z22

136 records, 35 keyed nodes

## node 2200027  (DIAL_Z22#0)
- speaker=0  style=0
- effects:
    - SET flag 0x1f79=0
    - SET flag 0x1f7a=0
- branches:
    - [always] -> node 0 (no jump)

## node 2200028  (DIAL_Z22#1)
- speaker=0  style=0
- effects:
    - SET flag 0x1f79=1
    - SET flag 0x1f7a=0
- branches:
    - [always] -> node 0 (no jump)

## node 2200029  (DIAL_Z22#2)
- speaker=0  style=0
- effects:
    - SET flag 0x1f79=0
    - SET flag 0x1f7a=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#3
- speaker=0  style=0
- effects:
    - SET flag 0x1f77=0
    - SET flag 0x1f78=0
    - SET flag 0x753f=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#4
- speaker=0  style=6  flags=paged-text
- effects:
    - bind speaker-name slot (kind=1 sub=19)
    - bind speaker-name slot (kind=2 sub=20)
    - bind speaker-name slot (kind=3 sub=22)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 「你們哪位有興趣買呢?」店主問道。「一包只要@1。」  @4發現他們身上有@2可以花……

### (sub) DIAL_Z22#5
- speaker=0  style=0
- branches:
    - [flag 0x7533 in [686..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#6
- speaker=0  style=0
- effects:
    - SET flag 0x1f78=1
    - ACTION: deduct gold (EvtArgGoldCost)
    - ACTION: EvtArgValue += 1
- branches:
    - [flag 0x1f79 in [784..0]] -> node 4294901761
    - [flag 0x1f7a in [813..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#7
- speaker=0  style=0
- effects:
    - GIVE item 'H' cond=1 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#8
- speaker=0  style=0
- effects:
    - GIVE item 'I' cond=1 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#9
- speaker=0  style=0
- effects:
    - GIVE item 'J' cond=1 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#10
- speaker=0  style=0
- branches:
    - [flag 0x753f in [890..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#11
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#12
- speaker=0  style=0
- effects:
    - SET flag 0x1f77=1
- branches:
    - [always] -> node 0 (no jump)

## node 2200034  (DIAL_Z22#14)
- speaker=0  style=0
- effects:
    - SET flag 0xdc54=1 + timer (1800)
- text: 兩名男子攔住了他們。  「不准再往前了,」其中一人下令道。「任何人進入巴納斯神殿前,都必須卸下身上一切金屬物品。」  @4皺起眉頭。「你們憑什麼提出這種要求?我們是亞魯莎王子的代表,命令你們放行。」  這番話似乎讓兩人有些吃驚,但他們一邊離開,一邊仍繼續談論著這條規矩。  「金屬是卑賤之物,冒犯我們的神。任何攜帶金屬進入這座神殿的人都會被當場擊斃……」從神殿的另一頭,聲音幾乎已經聽不清了,@4隱約聽見:「……這是巴納斯的旨意!」

## node 2200032  (DIAL_Z22#15)
- speaker=0  style=0
- effects:
    - SET flag 0x1fb0=0
- branches:
    - [flag 0x1f81 in [0..0]] -> node 4294901761
    - [flag 0x1f80 in [1624..0]] -> node 4294901761
    - [flag 0x1f76 in [2772..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#16
- speaker=0  style=0
- effects:
    - SET flag 0x1f81=1
- text: 一支箭咻地從@4頭邊掠過。  他嚇了一跳,但還算冷靜,立刻停下腳步,舉起雙手,並示意同伴照做。他們碰上了科瓦利斯伯爵的守衛。  一名四肢修長的士兵,以近乎貓科動物般的靈巧身手,穿過長長的草叢,停在幾步外,狐疑地打量著他們。「你們在這裡有什麼事?」男人問道。  「其實,我們就是來找你的,」@4說道,慶幸那支弩箭沒射中自己。「你是科瓦利斯伯爵的守衛之一,對吧?」  「就算是,那又怎樣?」男人回答道。  @4朝他們來時的方向比了比大拇指,轉述了那位自耕農跟他們說過、關於這一帶蜘蛛的...

## node 2200033  (DIAL_Z22#18)
- speaker=0  style=0
- effects:
    - read Scouting -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [3848..0]] -> node 4294901810

### (sub) DIAL_Z22#19
- speaker=200  style=0
- effects:
    - SET flag 0x1fac=1
    - GIVE item 'p' cond=1 to member#6 (cost 0)
- text: @4注意到泥地裡有東西。  他彎下腰撿了起來,拂去半掩著那東西的塵土。他小心翼翼地拿起來,朝同伴們露出驚訝的笑容。「有人在搞鬼。這是銀刺!」

## node 2200035  (DIAL_Z22#20)
- speaker=0  style=0
- effects:
    - read Scouting -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [4168..0]] -> node 4294901805
    - [always] -> node 0 (no jump)

## node 2200036  (DIAL_Z22#22)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [4343..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#23
- speaker=200  style=0
- branches:
    - [flag 0xc74b in [4781..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: @4拍了拍那人的肩膀。  男人抹去唇邊的啤酒泡沫,上下打量了來客一番,放下手中的酒杯。「你們是想找人把東西送去北衛城的集結地嗎?」他問道。  「你是信使嗎?」歐文回答道。  「不算是,不過要是有人想把訊息送到北衛城,那個人就是我,」男人說道。「算是被硬塞了這份差事吧。」

### (sub) DIAL_Z22#24
- speaker=0  style=0
- effects:
    - REMOVE item 'x' cond=19
- text: 歐文取出他們找到的那張字條,遞給了他。「這則訊息務必要送到北衛城的當權者手上。我已經看過內容,我認為裡頭寫的東西可能會影響這場戰役的局勢。」  「是嗎?」男人站起身說道。「好吧。我保證會親自送到馬丁公爵手上,絕不假手他人。不過我警告你,要是這是什麼惡作劇,我會追到天涯海角,狠狠揍你一頓。」

## node 2200037  (DIAL_Z22#26)
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 傭兵朝他們走了過來。  他上下打量著他們,手指在劍柄上敲打著,在他們面前來回踱步。最後,顯然對自己頗有信心,他開口挑釁起來……

### (sub) DIAL_Z22#30
- speaker=200  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 你在ó瞪什麼瞪,小子?回答我!

## node 2200039  (DIAL_Z22#37)
- speaker=0  style=0
- effects:
    - SET flag 0x1d19=0
    - SET flag 0x1f85=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4皺起了臉。  眼前這群列隊而立的男人,個個看起來心情都不太好,即使他們跟這夥人沒什麼過節,他們出現在這條路上,也很可能意味著前方有麻煩。@4並不想真的動起武來,只好盡力設法化解局面。

### (sub) DIAL_Z22#38
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們能幫上什麼忙嗎,各位?你們看起來心事重重。

### (sub) DIAL_Z22#39
- speaker=200  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [8201..0]] -> node 4294901761
    - [flag 0x0101 in [7969..0]] -> node 4294901761
- text: 心事重重?喔,沒錯,我們ó確實心事重重。羅姆尼那邊亂成一團,我們這夥人正要南下幫縴夫公會一把。你們呢?你們是站在米契爾跟那個該死的玻璃匠公會那邊嗎?

### (sub) DIAL_Z22#40
- speaker=200  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [8201..0]] -> node 4294901761
    - [flag 0x0101 in [8026..0]] -> node 4294901761
- text: 那你們一定是支持伊恩的囉?

### (sub) DIAL_Z22#41
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 不站邊的人啊,嗯?那也好,總比羅姆尼現在那幫烏合之眾裡的騙子強。不過我警告你們,最好離那攤子事遠一點!

### (sub) DIAL_Z22#42
- speaker=200  style=0
- effects:
    - ACTION: request hotspot activation at player
    - SET flag 0x1f85=1
- text: 米契爾．韋蘭德是條ó毒蛇,伊恩也一樣不是東西!縴夫工會是王室親自授予的獨家貿易特許,結果他們兩個都各自召集人手。現在他們這一鬧,把其他公會也捲了進來,那些公會壓低價錢搶我們的生意!你們居然還敢站在他們那邊!

## node 2200030  (DIAL_Z22#43)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[16] (xor=0x83 mask=0x21 mode=0 chapters=-)] -> node 4278259712
    - [event_bitmap_hi[16] (xor=0x36 mask=0x24 mode=0 chapters=-)] -> node 4278255872
    - [event_bitmap_hi[16] (xor=0x49 mask=0x2f mode=0 chapters=-)] -> node 536936448
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#45
- speaker=0  style=0
- branches:
    - [flag 0xc39f in [9299..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#46
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [10728..0]] -> node 4294901761
    - [flag 0x0101 in [11782..0]] -> node 4294901761
- text: 酒館老闆搖了搖頭。  他側身避開一名相貌兇悍的傭兵,壓低了聲音說話,深怕被人偷聽到。「儘管外頭鬧著莫瑞德人的事,但我不覺得自己這幾週的處境能比現在更糟了,」陸洛嘟囔道。「昨晚換崗過後,來了一群士兵。他們威脅說要是我不給他們弄點喝的,就要放火燒了ó匕ó首ó與星。幸好達布尼設法勸住了他們。」  歐文環顧酒館四周,看得出自那場衝突以來,氣氛沒什麼改善。「我們一直在幫你找……」  「找到了嗎?」陸洛突然來了興致,問道。「你們有什麼發現嗎?」

### (sub) DIAL_Z22#48
- speaker=0  style=6
- effects:
    - ACTION: spawn fixed objs 0x14/0x1e, clone inv
    - SET flag 0x1abb=1
    - event_bitmap_hi[16] bitop
    - GIVE item '\x1c' cond=83 to member#6 (cost 0)
    - REMOVE item 'O' cond=0
- text: @4咧嘴一笑。  他覺得自己彷彿是仲冬節上發禮物的慈善老爹,解開行囊的束口,讓酒館老闆瞥見他們的戰利品,同時四下張望,確認沒有人注意到他們。  酒館老闆眼裡閃過一絲喜色,強忍著興奮領著他們走進酒館的後房。「這裡東西不多,但至少能防著這裡不鬧出暴動!」他壓低嗓子尖聲說道,一離開客人的視線,便忍不住手舞足蹈起來。「讓我好好報答你們!」  他在後房的雜物裡翻找了一陣,找出一件用麻布包著的長條物,遞給了他們。  「是把劍,」@5端詳著這把做工精良的武器,說道。「依我看,還挺致命的。」...

### (sub) DIAL_Z22#50
- speaker=0  style=6
- effects:
    - SET flag 0x008f=1
    - event_bitmap_hi[16] bitop
- text: @4朝男人示意。  酒館老闆陸洛身穿一件沾滿食物污漬、彷彿壓得他肩膀發沉的圍裙,猶疑地走近他們,綠色的雙眼裡透著幾分懼色。「要是你們是來找酒喝的,恐怕得空手而回了。我們的酒桶都見底了。」  @4驚訝地朝這位紅髮男子挑起眉毛,又看了看酒館裡那些抱怨連連的客人。「沒酒可喝,酒館裡卻擠滿了士兵。我很意外居然還沒鬧起來,」他說道。  「喔,他們ó確實鬧過,」酒館老闆回答道。「目前為止,他們還不算太凶,我們勉強還能約束得住。但要是這情況再持續下去,這些士兵遲早會變得跟野狗一樣,誰也攔不...

## node 2200048  (DIAL_Z22#51)
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 這間酒館ó已經打烊了。 門上釘著一張看似匆匆寫就的字條:ã因ã近ã日ã酒ã水ã存ã量ã嚴ã重ã短ã缺ã，ã實ã在ã無ã法ã繼ã續ã供ã應ã各ã位ã顧ã客ã所ã需ã，ã燭ã匠ã的ã笑ã臉ã小ã店ã自ã即ã日ã起ã暫ã停ã營ã業ã，ã直ã至ã酒ã水ã補ã貨ã完ã成ã、ã恢ã復ã供ã應ã之ã時ã，ã方ã才ã重ã新ã開ã張ã迎ã客ã。ã造ã成ã諸ã位ã貴ã客ã諸ã多ã不ã便ã之ã處ã，ã還ã請ã多ã多ã見ã諒ã為ã盼ã。ã ã ã塔ã巴ã爾ã謹ã啟ã ã燭ã匠ã的ã笑ã臉ã酒ã館ã店...

## node 2200009  (DIAL_Z22#52)
- speaker=0  style=0
- branches:
    - [flag 0x1ddb in [13919..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#53
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[16] (xor=0xdf mask=0x42 mode=0 chapters=-)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#55
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [16364..0]] -> node 4294901761
    - [flag 0x0101 in [16198..0]] -> node 4294901761
- text: 一名男子攔住了他們。  眼前這個人身上有股嗆人的體味,長相粗野,烏黑的頭髮貼著濃眉修剪得整整齊齊,一雙眼睛擠在腫脹的鼻樑兩側。  「抱歉,除了她的顧問,誰也不能見波斯維奇夫人。快走吧,」守衛說道,朝他們揮了揮那隻碩大的手。「集結隊長在別處。他大概ó需要幾個打雜的小廝……」  歐文選擇不理會這番輕蔑之詞,深吸了一口氣。「我必須進去跟波斯維奇夫人談談。我們是想確保你們這裡的集結不會鬧成暴動。」  「我不能放任何人進去,」他說道,語氣像是在自言自語重複一遍這件事,而不是在回答他們。...

### (sub) DIAL_Z22#57
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [16791..0]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#59
- speaker=0  style=0
- effects:
    - event_bitmap_hi[16] bitop
    - event_bitmap_hi[16] bitop
    - TAKE gold -500
- text: 歐文交出了金子。  守衛堅持要先數過錢才肯放行,惹得他有些不耐煩,腳在泥濘的地面上輕輕跺著。  「那就進去吧,」守衛清點完畢,滿意地搖了搖錢袋,說道。「替我向夫人問好。」

### (sub) DIAL_Z22#60
- speaker=0  style=0
- effects:
    - event_bitmap_hi[16] bitop
- text: 守衛瞇眼打量著他們。  「喔,是你們兩個啊,」他說道。「你們已經付過錢了,快進去吧。」

## node 2200004  (DIAL_Z22#61)
- speaker=0  style=6
- text: 這男人正好聊興大發。  他一邊講著自己傭兵生涯的故事,一邊從一只碩大的酒杯裡啜飲著麥酒,最後不知怎地聊到了他有多討厭卡胡利的信徒。  「你為什麼這麼討厭他們?」@4問道。  聽到這問題,男人挑起一邊眉毛,搖了搖頭。「肯廷拉什那座神殿裡那些該死的卡胡利祭司,我告訴你,一點都不ó正常ð。凡是男人享受的東西,他們都要人放棄。全都被那套該死的虔誠戒律綁得死死的。提斯在上,什麼苦行贖身,說穿了不就是叫某個倒楣鬼餓得只剩皮包骨,還得戒掉花天酒地嗎?依我看,一點都不正常……」

## node 2200040  (DIAL_Z22#62)
- speaker=0  style=6
- text: 房子前面站著武裝守衛。  「我們是奉公務前來,」@4喊道。  一名守衛手按著武器,反問道:「憑誰的授權?」  「憑克朗多親王的授權,」@4語氣平淡地說道。「而且我們是卡胡利神殿的祭司派來的。」  守衛顯然對這個答案感到滿意,讓開了一旁,放他們通過。

## node 2200005  (DIAL_Z22#63)
- speaker=0  style=0
- branches:
    - [flag 0x1cf7 in [19342..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#64
- speaker=0  style=0
- effects:
    - ACTION: mark region encounter #645 defended (roster killed)
- branches:
    - [always] -> node 0 (no jump)
- text: 一名夜鷹會的人正等著他們。  他伸手探進黑色長衫的衣褶裡,取出一件在昏暗中閃著微光的東西。但他沒有撲上前來,而是迅速將手伸向嘴邊,咬了下去,動作快得詹姆士都還沒反應過來他要做什麼。  「他剛吞下毒藥了,」詹姆士說道,一把攔住戈拉斯。「也好。省得我們動手殺他了。」他蹲下身,端詳著這名夜鷹會成員抽搐的臉,臉上帶著一絲厭惡的神情,繼續說道:「我敢打賭他不是首領,而且前面那扇門一定上了鎖。只要找出主導這個組織的人,我們就能找到需要的鑰匙。」  「你怎麼能猜出這麼多?」歐文困惑地問道。...

### (sub) DIAL_Z22#65
- speaker=0  style=0
- effects:
    - ACTION: mark region encounter #645 defended (roster killed)
- branches:
    - [always] -> node 0 (no jump)
- text: 一名夜鷹會的人正等著他們。  他伸手探進黑色長衫的衣褶裡,取出一件在昏暗中閃著微光的東西。但他沒有撲上前來,而是迅速將手伸向嘴邊,咬了下去,動作快得詹姆士都還沒反應過來他要做什麼。  「他剛吞下毒藥了,」詹姆士說道,一把攔住戈拉斯。「也好。省得我們動手殺他了。」他蹲下身,端詳著這名夜鷹會成員抽搐的臉,臉上帶著一絲厭惡的神情。「幸好我們已經找到納馮和他的鑰匙了。我猜這把鑰匙就能打開那邊那扇門。」

## node 2200006  (DIAL_Z22#67)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x197d in [21261..0]] -> node 0 (no jump)
    - [flag 0xc751 in [21261..0]] -> node 0 (no jump)
    - [event_bitmap_hi[14] (xor=0x0d mask=0x53 mode=0 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#68
- speaker=0  style=6
- effects:
    - event_bitmap_hi[14] bitop
    - SET flag 0x0097=1
- text: 門虛掩著。  他們走進屋裡,一名男子從小櫃檯後方向他們打招呼:「我是這裡的首席放款人。敝姓伊蘇納圖斯。有什麼能為您效勞的嗎?」他問道。  @4取出他們在阿布克的魔法箱裡找到的那份帳冊,放在櫃檯上。「我們想知道,您能不能告訴我們這張借據的一些細節。底下這個印記是您的。」  「是的,我ó明白ð了,」男人回答道。他把眼鏡往鼻樑上推了推,開始仔細審視起來,先看了看借據頂端,又皺著眉頭瞄了瞄底部,接著又看回頂端,就像個小孩盯著彈跳的球一樣。最後他終於開口了。「恐怕要跟我們的紀錄核對,我...

## node 2200007  (DIAL_Z22#70)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [21726..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#71
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 一團塵霧在門口迎接他們。  「抱歉,兩位先生,」一名年輕女子說道。「我只是想抖抖手上的除塵拖把……不知道外頭有人。」  @4甩了甩頭,抖掉頭髮上的灰塵,回答道:「沒關係。這裡是科瓦利斯家,對嗎?」  「這你說對了,不過科瓦利斯伯爵和他女兒烏格妮眼下都不在家,」她說道。  @4微微一笑,和氣地問道:「喔,那你知道他們去哪裡了嗎?」  侍女左右張望了一下,才壓低聲音說道:「他們去肯廷拉什的集結地,替波斯維奇夫人主持事務去了。不過這話可不是我說的。」  他們謝過她提供的消息,便離開...

### (sub) DIAL_Z22#72
- speaker=0  style=0
- branches:
    - [flag 0x753a in [22483..0]] -> node 4294901761
    - [flag 0x1f76 in [23366..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#74
- speaker=0  style=0  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#75
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
    - (on-exit) play sfx 39
    - SET flag 0x1f76=1
    - END conversation, result=65535
- text: 一名僕人應了敲門聲。  「什麼事?」從她凌亂的頭髮和身上穿的睡衣看來,這名僕人顯然是被吵醒了,原本正睡得香甜。  「抱歉吵醒你了,」@4道歉道。  「科瓦利斯伯爵眼下不在家,他女兒烏格妮也已經就寢了,」女孩說道,顯然是想擋掉進一步的追問。「恐怕兩位得等ó正常的時候再來拜訪了。再見。」  「等等!」@4連忙把腳伸進門縫,不讓門關上,腳被夾在門框裡疼得他倒抽一口氣。「伯爵去哪裡了?」  「出門了,」女孩沒好氣地說道。「他有時候會在領地原本的莊園上夜間狩獵。」  「那我們或許能在那...

### (sub) DIAL_Z22#76
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - (on-exit) play sfx 39
    - END conversation, result=65535
- text: 科瓦利斯家的一名僕人應了敲門聲。  「走開!」她厲聲說道。「要是你們想找科瓦利斯伯爵或他女兒說話,得改天再來。最好,」她冷冰冰地補了一句,「是白天的時候!」  @4還沒來得及說第二句話,便發現自己已經站在一扇緊閉的門前了。

## node 2200011  (DIAL_Z22#77)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [24906..0]] -> node 4294901761
    - [event_bitmap_hi[18] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 4278256640
    - [event_bitmap_hi[18] (xor=0x84 mask=0x6a mode=0 chapters=-)] -> node 4278255872
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#79
- speaker=0  style=6
- effects:
    - advance in-game time by 3600
    - event_bitmap_hi[18] bitop
- text: 一名士兵領著他們進去。  跟隨著那人白色戰袍飄動的下擺,他們被領進一間布置雅致的書房,幾扇大窗俯瞰著城堡的校閱場。窗台下方坐著一名體格魁梧的男子,正全神貫注地看著下方的動靜,不時在身旁的一張羊皮紙上潦草記下幾筆。  「凱文男爵,這幾位求見,」士兵通報道。「我可以先退下嗎?」  紅髮男子點了點頭,示意他們坐到比他自己現在所坐的位置正式一些的椅子上。「兩位有什麼事要我效勞的?恐怕特羅維爾男爵不在家。」  「沒關係。我們是想打聽一些高堡可能遭到攻擊的消息,」@4開口道。「您最近有沒...

### (sub) DIAL_Z22#80
- speaker=0  style=0
- effects:
    - advance in-game time by 3600
- branches:
    - [flag 0xc750 in [27307..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#81
- speaker=0  style=6
- effects:
    - event_bitmap_hi[18] bitop
    - REMOVE item 'x' cond=24
    - GIVE gold +2000
    - GIVE item 'H' cond=1 to party (cost 0)
- text: 凱文在門口迎接他們。  寒暄過後,他們跟著他走向廚房——他原本正要去那裡。轉過一個寬闊的轉角後,他們走進了一間小廚房。  「怎麼樣?」他一邊問,一邊拿了些點心,也遞了些給眾人。「你們一路上有什麼發現?」  @4一言不發,取出他們從那具哥布林屍體上搜出的字條,遞了過去,仔細觀察著男爵讀信的神情。最後,他把羊皮紙揉成一團,說道:「迪勒肯要騙我們,得比在橋上留這麼明顯的假消息高明點才行。他是想讓我們相信,既然我們的兵力ñ明顯多過ñ對岸那點薄弱的守軍,就該派兵渡河。我們才不會上這個當...

## node 2200023  (DIAL_Z22#83)
- speaker=0  style=0
- effects:
    - event_bitmap_hi[37] bitop
- branches:
    - [event_bitmap_hi[37] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278255873
    - [event_bitmap_hi[37] (xor=0xe0 mask=0x72 mode=0 chapters=-)] -> node 4278263808
    - [event_bitmap_hi[37] (xor=0x92 mask=0x82 mode=0 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#84
- speaker=0  style=0
- effects:
    - event_bitmap_hi[37] bitop
- text: 哥布林攔住了他們。  「你們記得我們吧?」@4朝著等候的一夥人喊道。「我們之間有新的契約了對吧?」  「我們記得,」哥布林首領回答道。「我們很快就會依約前往北衛城。過來吧。你們不會受到傷害。」

### (sub) DIAL_Z22#85
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [29723..0]] -> node 4294903760
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#86
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [32514..0]] -> node 4294901761
    - [flag 0x0101 in [33159..0]] -> node 4294901761
- text: 一群哥布林在路上聚集著。  詹姆士緊盯著眼前這夥哥布林的首領。洛克利爾在他身旁默默數著人頭,盤算著這支傭兵隊伍的身價。  「你怎麼看,洛奇?」詹姆士低聲問道。  「不管迪勒肯在打什麼算盤,他都是ó花了錢的,」洛克利爾語氣沉重地回答道。「哥布林傭兵收費不便宜,依我估計,這裡至少有……一千枚金幣的身價。除非牠們覺得我們靠得太近,不然應該不會出手攻擊我們。我們ó或許能談出一個通行費……」  「呸,」派特魯斯啐了一口。「黑暗兄弟就是黑暗兄弟。牠們就是心術不正,沒別的。」  敵方隊伍裡...

### (sub) DIAL_Z22#88
- speaker=0  style=0
- effects:
    - event_bitmap_hi[37] bitop
    - TAKE gold -20000
- text: 詹姆士湊出了所需的數目。  他把錢扔在哥布林腳邊,等著蜂擁而上的傭兵們把錢收好。「你答應讓我們通行,」詹姆士說道。  「是,」哥布林回答道。「我們不打你們,遇到我們同伴也不會打。告訴他們你們付錢通行是古拉下的命令。我們會替你們的男爵打仗。」  哥布林首領轉身離去時,洛克利爾湊在詹姆士耳邊,忍著笑低聲說道:「想像一下,等這夥人浩浩蕩蕩開進北衛城,宣布他們是替ó他打仗,加博特男爵那張臉會是什麼表情。他一定會氣炸的!」  詹姆士微微一笑。「可惜我們沒辦法在場親眼看到。」

## node 2200041  (DIAL_Z22#91)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[20] (xor=0xeb mask=0x5c mode=21 chapters=8)] -> node 769
    - [event_bitmap_hi[20] (xor=0xf4 mask=0x83 mode=0 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#93
- speaker=0  style=0
- effects:
    - event_bitmap_hi[20] bitop
- text: 男人邀他們坐下聊聊。  這是個沉靜隨和的傢伙,左手少了三根手指,詹姆士和洛克利爾講起他們兒時在克朗多一起長大的故事時,他微笑聽著。等他們講到吟遊詩人勞瑞後來成了薩拉多公爵的故事時,男人點了點頭,但當他們聲稱勞瑞是史上最厲害的吟遊詩人時,他卻打斷了他們。  「我想你們說的這位公爵想必才華洋溢,」男人說道。「不過不久前,這裡來過一位ó行吟藝人,技藝之高,我還沒聽過能與他相比的。」  洛克利爾和詹姆士立刻交換了一個意味深長的眼神,才回頭望向男人。「這位吟遊詩人長什麼樣子?」詹姆士問...

## node 2200014  (DIAL_Z22#94)
- speaker=0  style=0
- effects:
    - event_bitmap_hi[21] bitop
- branches:
    - [event_bitmap_hi[21] (xor=0x8c mask=0x90 mode=0 chapters=-)] -> node 4278259712
    - [event_bitmap_hi[21] (xor=0x59 mask=0x8d mode=0 chapters=-)] -> node 4278263808
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#95
- speaker=0  style=0
- effects:
    - ACTION: request hotspot activation at player
    - event_bitmap_hi[21] bitop
- text: 派特魯斯停下了腳步。  @4又往前走了幾步,才發現這名法師沒跟上來,轉身一看,只見他一臉滑稽的疑惑,盯著灌木叢瞧。  「這地方有點不對勁……」派特魯斯緩緩轉了一圈,說道。「事情根本ó不ó是表面看起來那樣。要是一樣東西看起來不像它本來的樣子,那就表示它戴著某種面具。」  「你在胡扯些什麼?」洛克利爾問道。  「隱形法師啊,你這蠢驢!」派特魯斯反脣相譏。他的嘴唇幾乎難以察覺地動了起來。他無聲地唸著早已遺忘的字句,雙唇越動越快,配合著只有他自己知道的、逐漸加快的秘密節奏。接著他終於...

### (sub) DIAL_Z22#97
- speaker=0  style=0
- effects:
    - DAMAGE Health+Stamina of party by -1280
- text: @5感到一陣刺痛。  「哎唷!」他叫出聲來,四處尋找是哪隻蟲子害他這麼難受。卻什麼也沒找到,只好轉向一臉困惑的@3,想解釋自己這聲驚呼。但他話還沒說出口,@3也感到被咬了一口。  「這是什麼地方?」法師喊道,又感到另一陣刺痛。  「我不知道,」@5說道。「不過我建議我們——哼——立刻離開這裡。」

## node 2200024  (DIAL_Z22#98)
- speaker=0  style=0
- text: @4停下了腳步。  他搖了搖頭,轉向其他人。「這條路走不通。要是繼續往這個方向走,我們只會白白浪費寶貴的時間。我們得掉頭了。」

## node 2200050  (DIAL_Z22#99)
- speaker=0  style=0
- effects:
    - ACTION: mark region encounter #0 defended (roster killed)

## node 2200017  (DIAL_Z22#100)
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x004a=1
    - event_bitmap_hi[24] bitop
- branches:
    - [flag 0x0100 in [38671..0]] -> node 4294901761
    - [flag 0x0101 in [38057..0]] -> node 4294901761
- text: @3使勁嚥了口口水。  守橋的莫瑞德苔蘚兵團,以冷冽的眼神迎接他們的靠近。「沒有莫萊伍夫的口令,誰都不准過此地,」一名守衛威脅道。「你們知道口令嗎?」

### (sub) DIAL_Z22#102
- speaker=0  style=0
- branches:
    - [flag 0x1f6d in [39064..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#104
- speaker=0  style=0
- effects:
    - event_bitmap_hi[24] bitop
- text: 戈拉斯點了點頭。  「屠蛇者,」他直視著這名莫瑞德守衛的雙眼,說道。「這口令是莫萊伍夫親口告訴我的。難道要我回去告訴他,你不放我們過橋嗎?」  守衛狠狠地盯著他們看。「很好。你們可以過去了。」

## node 2200018  (DIAL_Z22#105)
- speaker=0  style=0
- effects:
    - ACTION: request hotspot activation at player
    - ACTION: mark region encounter #343 defended (roster killed)

## node 2200019  (DIAL_Z22#106)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[24] (xor=0x21 mask=0x9b mode=0 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#108
- speaker=0  style=0
- branches:
    - [flag 0x9c4b in [39742..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#109
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0103 in [39989..0]] -> node 4294901761
    - [flag 0x0123 in [0..0]] -> node 4294901761
- text: @3感到一陣暈眩。  洞穴裡濃烈的氣味讓他頭暈目眩,他盯著那被那夫沙油染污的水面。  「你準備好要游了嗎?」戈拉斯問道。「還是需要再準備一會兒?」

### (sub) DIAL_Z22#110
- speaker=0  style=6
- effects:
    - event_bitmap_hi[24] bitop
    - ACTION: request hotspot activation at player
    - load teleport table 29
- text: 他把防毒面罩戴上口鼻,望著眼前的水流,看它源源不絕地灌入岩洞——他知道,這水終究會流回開闊的空氣中……以及自由。  他透過面罩深深吸了口氣,終於感到頭腦清醒了些,便縱身跳入河中,@5也在他身旁濺起水花。冰冷的河水刺得他皮膚生疼,他不禁覺得有些諷刺——防毒面罩總算讓他呼吸順暢了一些,如今卻被這股寒意奪走了這份輕鬆。  他忍著疼痛,任由水流帶著他前進,直到抵達那個黑漆漆的洞口——只要他一鬆開扒著洞壁的手,就會被吞沒進去。  他盡力深吸了一口氣,鬆開了手。那頭黑暗的巨獸將他吸入喉嚨...

## node 2200025  (DIAL_Z22#112)
- speaker=0  style=6
- text: @3看見一絲微弱的光。  那光模糊而沒有形狀,卻迅速變得越來越清晰、強烈,伴隨而來的還有——疼痛。頭部和四肢傳來一陣陣鈍痛,每跳動一下心臟就更痛一分。  他的眼皮顫動著睜開,隱約看見戈拉斯的身影站在他上方,那身影朦朧得不太真實,彷彿一場夢。但他知道這不是夢,他知道自己撐過了那段水下洞穴的旅程,意識到自己還活著,他勉強擠出沙啞的低語:「你要是再敢讓我們幹這種事,我就發明一道法術,唯一的目的,」他說得越來越快、越來越清楚,「就是讓你死心塌地愛上一頭疣豬——祝你們倆白頭偕老!」  ...

## node 2200021  (DIAL_Z22#113)
- speaker=0  style=6
- text: @4朝那間莫瑞德酒館走去。  「你真的覺得我們能大搖大擺走進去,不引來注意嗎?」@3問道。  「這是我多年前學到的一招,遇到難題時,大家都會傾向相信最簡單的解釋,」他低聲說道,伸手去推門。  @3並不信服。「這實在太不尋常了。」  「換個角度想,」@4接著說道。「我們要不是有正當理由在這裡,就是完全瘋了,大搖大擺闖進敵人的地盤。後者根本說不通,所以裡頭的人都會假定前者才是真的。現在就試著表現得像是這裡的常客吧……」

## node 2200042  (DIAL_Z22#114)
- speaker=0  style=6
- text: @4走近一名莫瑞德人。  他狐疑地打量了他們一眼,聳了聳肩。雖然他用王國語跟他們交談,但口齒含糊,說得斷斷續續。  「你們是納拉布的兄弟雇來的?他叫什麼名字來著……納戈?」莫瑞德人問道。  @4點了點頭。「是,我們是……傭兵……剛從奎格過來。你知道南下攻勢的消息嗎?」  莫瑞德人低下頭,低聲說道:「聽說克洛戴克隊長已經接到進攻北衛城的最終命令了。除此之外,我什麼也不清楚。」  @4意識到這莫瑞德人再也問不出什麼有價值的情報,便又留了片刻聽了聽,免得引起不必要的注意。最後,他找...

## node 2200043  (DIAL_Z22#115)
- speaker=0  style=6
- text: 這名莫瑞德人走近了他們。  他顯然對他們自稱是奎格傭兵的說法感到滿意,並解釋道自己是個商人,經常往返王國與北境邊界附近的幾座城鎮,這也是他為何能講一口流利王國語的原因。  「你知道多少關於南下攻勢的消息?」@4問道。  「聽說克洛戴克隊長已經接到進攻北衛城的最終命令了。不過根本沒用。憑我們的兵力,別說攻破城牆,連走到那裡都撐不住。要是那位工程師沒想出什麼辦法,王國的這位男爵會把我們徹底輾碎。」  @4刻意不表現出太大的興趣,又試探著追問下去。「賽格森?」  莫瑞德人古怪地盯著...

## node 2200026  (DIAL_Z22#116)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[25] (xor=0x4d mask=0xb1 mode=0 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[25] (xor=0x08 mask=0xbc mode=0 chapters=-)] -> node 4278263808
    - [flag 0xc3ab in [47792..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z22#118
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @5望著這座沉重的木造投石機,驚訝地張大了嘴。  他們繞著這件武器走了一圈,從各個角度仔細打量,花了不少時間研究發射與扳機機構。整體看來狀況良好,只是有一根扭力齒輪斷了……

### (sub) DIAL_Z22#119
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這台丟蟾蜍的玩具,肯定是莫瑞德人造來惹惱男爵的。他們根本沒辦法把它弄上山口,老臭臉那幫人早就把他們射下來了!」

### (sub) DIAL_Z22#120
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「也許吧,不過除非有人把它修好,拿來對拉格蘭姆ó扔石頭,不然對他們也沒什麼用。」

### (sub) DIAL_Z22#121
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這麼一說,ó這點還真奇怪。告訴我,洛奇,要是你打算把這種東西就這樣扔在野地裡,就算它壞了不能用,你會讓它ó對著自己的家鄉嗎?」

### (sub) DIAL_Z22#122
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你想說什麼?」

### (sub) DIAL_Z22#123
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這東西不能用,唯一的原因就是有一根扭力齒輪斷了,修起來也不算太複雜。現在假設這根齒輪不是自己壞的。戈拉斯告訴過我,不少莫瑞德氏族對於要不要繼續打著穆爾曼達穆斯的舊戰旗作戰,心裡其實有所保留。要是你是這些氏族之一,又想留一手,萬一哪天想退出這場攻勢,那只需要裝上一根替換的齒輪就行了……」

### (sub) DIAL_Z22#124
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「……再拉下釋放拉桿就行了!籃子裡甚至還裝著發射物!當然,假設我們自己能找到那個零件,我們就能製造點麻煩。說不定還能趁著混亂,想辦法拿到馬丁公爵需要的作戰計畫。」

### (sub) DIAL_Z22#125
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「也許吧,不過我們得先找到替換的投石機零件。我不覺得這附近會剛好躺著一個,但我們四處找找看吧……」

### (sub) DIAL_Z22#127
- speaker=0  style=0
- effects:
    - REMOVE item '[' cond=0
    - event_bitmap_hi[25] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: @5深吸了一口氣。  他拿著他們在箱子裡找到的投石機零件,用幾樣臨時湊合的工具,跪在機器前動起手來。  裝上這個零件花了將近兩個鐘頭,雖然@5並不確定這台機器到底能不能運作,他還是退後幾步,端詳起自己的傑作。

### (sub) DIAL_Z22#128
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [48609..0]] -> node 4294901761
    - [flag 0x0101 in [48478..0]] -> node 4294901761
- text: 「我不是工程師,不過我想這樣應該行得通,」他說道,招手示意其他人過來。  眾人一同站在這隻奇特的木造怪物面前,它那隻機械臂已經蓄勢待發,準備把特製的貨物拋向那座昏昏欲睡的莫瑞德小鎮拉格蘭姆。  @5深吸了一口氣。「我們要不要試試看?」他問道。

### (sub) DIAL_Z22#130
- speaker=0  style=0
- effects:
    - SET flag 0x1aad=1
    - event_bitmap_hi[25] bitop
- text: @3從投石機旁退開了幾步。  @5用手背抹了抹額頭,彎下腰去抓住那根能讓這頭巨獸活過來的木製把手……

## node 2200038  (DIAL_Z22#131)
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「別這麼心急,我的年輕朋友。」

### (sub) DIAL_Z22#132
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「怎麼了?」

## node 2200052  (DIAL_Z22#134)
- speaker=5  style=0
- text: 好吧,看來我們只能走到這裡了。橋的另一頭守衛太多,我們溜不過去。反正走那條路也不是太重要。我們的目標是拿到公爵要的作戰計畫。走吧,我們往拉格蘭姆折回去。

## node 2200049  (DIAL_Z22#135)
- speaker=0  style=0
- text: @4拉了拉那扇柵欄。  「不行,推不動,」@4說道。「看來我們只能走正門出去了。不過我的鼻子倒是鬆了口氣。」
