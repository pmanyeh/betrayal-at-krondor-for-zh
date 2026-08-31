# DIAL_Z19

483 records, 86 keyed nodes

## node 1900007  (DIAL_Z19#0)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [729..0]] -> node 4294901761
    - [flag 0x7537 in [1155..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#3
- speaker=0  style=6
- branches:
    - [event_bitmap_hi[0] (xor=0x81 mask=0x13 mode=0 chapters=-)] -> node 4278256640
    - [event_bitmap_hi[0] (xor=0x95 mask=0x09 mode=0 chapters=-)] -> node 4278255873
    - [always] -> node 0 (no jump)
- text: 這座駐防要塞令人印象深刻。  這座軍事哨站坐落在俯瞰拉姆特的山丘高處，多年前建造，目的是為了阻擋莫瑞德人可能對王國西境發動的攻勢。  他們沿著一條蜿蜒穿過城鎮、爬上要塞所在岩丘的道路前進。與門口的哨兵交談過後，便被領著穿過要塞那扇巨大的鐵閘門。

### (sub) DIAL_Z19#4
- speaker=0  style=6
- effects:
    - event_bitmap_hi[0] bitop
    - SET flag 0x0016=1
- text: 貝爾福德隊長見他們進屋便站了起來。  「很高興能再見到你，@4，」他說著，伸出了手。  「我也有同感。你有什麼消息？卡蘇米伯爵近況如何？」@4一邊問道，一邊與他握手。  他們在硬邦邦的木椅上坐下，貝爾福德回答道：「他很好，只是正忙著處理一些事務——有幾名新守衛剛從凱勒旺穿過裂界過來。至於我們其他人，正在找一群灰袍武士，他們是從凱勒旺來的，就在裂界關閉前溜了過來。」  @4露出有點困惑的神情。「萊亞姆王與伊金達皇帝已經賜予那些灰袍武士自由，讓他們在王國裡有了新的身分。」  「沒...

### (sub) DIAL_Z19#5
- speaker=0  style=0
- branches:
    - [flag 0xc389 in [3718..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#6
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [4490..0]] -> node 4294901761
    - [flag 0x0101 in [4069..0]] -> node 4294901761
- text: 貝爾福德隊長微笑著迎接他們。  「什麼風把你們吹回來了？」他親切地問道。  @4取出了他們找到的那顆紅寶石。舉起讓貝爾福德查看，寶石正好接住一道陽光，把牆上灑滿了成千上萬個閃爍的紅色光點。  「你們是來歸還馬卡拉的紅寶石的嗎？」貝爾福德問道。

### (sub) DIAL_Z19#8
- speaker=0  style=6
- effects:
    - event_bitmap_hi[0] bitop
    - SET flag 0x1a42=1
    - SET flag 0x1a41=1
    - GIVE gold +1000
    - REMOVE item '9' cond=0
- text: @4把紅寶石交給了貝爾福德隊長。  「真高興你們找到了這個，」他說著，把寶石放進一個襯著絲絨的小盒子裡。「這下總算能擺脫馬卡拉的糾纏了。我派了這麼多人出去找這該死的東西，要塞裡都快沒剩幾個人了！」  他從房間角落一只上了鎖的箱子裡取出一個錢袋。「拿去吧，一百枚金索夫林。謝謝你們，各位。」  @4把錢袋收進背包，隨後他們便離開了。

### (sub) DIAL_Z19#9
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [5543..0]] -> node 131074
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#10
- speaker=0  style=6
- effects:
    - advance in-game time by 1800
- text: @4笑了。  「真高興又見到你了，貝爾福德隊長，」他說著，朝著走近的軍裝男子點了點頭。「你有什麼消息？」  貝爾福德伸出手回答道：「我們持續收到北境局勢不穩的回報，這附近也發現了不少該死的莫瑞德人混蛋——你們有什麼消息要告訴ñ我ð嗎？」  他們談了將近一個鐘頭，交換了各自的見聞與情報。最後，新消息都聊完了，兩人握手道別。

## node 1900008  (DIAL_Z19#12)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20140..32815]] -> node 4294901761
    - [event_bitmap_hi[0] (xor=0xed mask=0x1c mode=0 chapters=-)] -> node 4160750337
    - [flag 0x1f8a in [20147..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#13
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 39
    - SET flag 0x1f8a=1
    - SET flag 0x002b=1
- text: 一個瘦小的男人在門口迎接了他們。  「我是凱佛艾爾庫克。你們是來買賣寶石的嗎？」他用虛弱的聲音問道。  @4靠近了門口。「我們在找一顆紅寶石，可能是被一群灰袍武士偷走的。你有跟這樣的人買過任何寶石嗎？」  「我不知道你在說什麼，」那男人急忙說道。「我不收購ñ贓物。你可以去問問我在鷹谷北邊碰到的一個傢伙，我記得他叫艾薩克。」那男人緊張地四下張望。「我……呃……現在沒開門營業。你們得晚點再來。」  @4話還沒說完，凱佛就已經把門關上了。

## node 1900009  (DIAL_Z19#15)
- speaker=0  style=0
- effects:
    - SET flag 0x1a46=1
    - bind speaker-name slot (kind=0 sub=15)
- branches:
    - [always] -> node 0 (no jump)
- text: @0從已死的布拉克努爾身邊挪開。  他的舌頭感覺又厚又黏，嘴裡和鼻孔裡都殘留著一股苦澀的粉筆味。他沒料到這隻怪物死去時會噴出那朵詭異的小煙霧，但他很慶幸這場戰鬥終於結束了。  @0想透透氣，轉過身，差點被一個咧嘴笑著的矮小矮人絆倒……

### (sub) DIAL_Z19#16
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你們成功啦！我在坑道下頭聽到那陣爆炸聲，都不知道到底發生什麼事哩！恭喜恭喜！」

### (sub) DIAL_Z19#17
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「現在啊，我看我們大家都該歇一歇了……」

### (sub) DIAL_Z19#18
- speaker=15  style=0
- effects:
    - GIVE gold +1500
- branches:
    - [always] -> node 0 (no jump)
- text: 「歇是要歇的，你們也真是該歇歇了！身子骨可得養好，才扛得動那一大堆賞金哪！幹得漂亮！」

## node 1900010  (DIAL_Z19#20)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[1] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 3221226496
    - [event_bitmap_hi[1] (xor=0xb8 mask=0x28 mode=0 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[1] (xor=0x29 mask=0x27 mode=0 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#21
- speaker=0  style=6
- effects:
    - event_bitmap_hi[1] bitop
- text: 門板上覆著一層圖案；一個由油膩黑漬構成的詭異半圓形，在鐵門閂處交會。仔細一看，那些黑漬似乎其實是某種指紋……  「我想我真該把這個清乾淨了。」聽見這粗啞的聲音，@4猛地站直身子。一個微禿的男人從屋角踱步過來，在@0身旁停下，舉起一隻沾滿黑墨的手掌。「當抄寫員總是容易弄得一團糟。職業病嘛。」  「抄寫員？」  「還兼做點別的，」他說。「目前我接下了一位行商的委託，要對這一帶所有的商用箱子做個調查。」他意味深長地看了@5一眼。「或許你們會有興趣幫個忙。」  「那我們能得到什麼好處...

### (sub) DIAL_Z19#22
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- text: 傑瑞米應了他們的敲門聲。  「啊，我的朋友們。看來你們回來了。那個箱子的事，你們有什麼消息？」  @4用靴尖蹭著一塊鬆動的地板。「我們不知道。」  「在你們告訴我箱子裡裝了什麼之前，我不能——我ñ不會——把書給你們。我之前跟你們說過了，就在鷹谷西邊、一座小山丘的南邊。現在走吧。」

### (sub) DIAL_Z19#23
- speaker=0  style=0
- effects:
    - GIVE item '\x84' cond=100 to member#6 (cost 0)
    - event_bitmap_hi[1] bitop
- branches:
    - [flag 0xdacf in [10473..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#24
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 39
- text: @4憤怒地推開了傑瑞米家的門。  「我們得跟你這個抄寫員好好談談，」他啐了一口。「你早就懷疑那個箱子裝了爆炸機關——這就是為什麼你唯獨沒去調查那一個。」  「隨你怎麼想，但事實不是這樣。我根本不知道裡頭有陷阱。」  @4狠狠瞪著這個禿頭男人，對方也帶著輕蔑回瞪過去。「我們本該好好教訓你一頓，但既然你信守了自己的承諾，我想我們就放你一馬吧，畢竟我們還有更重要的事要處理。」  「什麼？還有比威脅抄寫員更重要的事？」傑瑞米厲聲說道，抓起一本書塞進@4手裡。「我不准你們硬給我扣上騙子...

## node 1900011  (DIAL_Z19#26)
- speaker=0  style=0
- effects:
    - event_bitmap_hi[2] bitop
    - SET flag 0x0022=1
- branches:
    - [flag 0xc37f in [13282..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 一隻科博德從坑裡哼哼唧唧地爬了上來。  @5把手按上劍柄，但這隻怪物似乎沒帶武器，過了片刻他便鬆開了握劍的手。  這隻科博德用不太流利的王國語，開始跟他們說起了魯阿爾格——那條曾經棲息在這座礦場裡的巨龍。他們深信是矮人以某種方式害這條龍消失的，於是決定賄賂多爾根王把牠放出來。

### (sub) DIAL_Z19#28
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [13469..0]] -> node 4294901761
    - [flag 0x0101 in [14546..0]] -> node 4294901761
- text: 「我們想要……灰塔鎧甲，」那科博德啞聲說道。「你們……可知道……我們在說什麼？」  @4想了一會兒這個問題，不確定該怎麼回答……

### (sub) DIAL_Z19#29
- speaker=0  style=6
- effects:
    - advance in-game time by 1800
    - RAISE Health+Stamina of party by 11264
    - RAISE Health of party by 1280
    - RAISE Stamina of party by 1280
    - REMOVE item '/' cond=0
    - event_bitmap_hi[2] bitop
    - SET flag 0x1a4e=1
    - SET flag 0x1a4f=1
- text: @4點了點頭。「是的，我們知道，」他緩緩說道。「要是我們把它給你們，我們能得到什麼好處？」  那科博德想了片刻，隨後轉向坑裡，用雙手比劃出一些信號動作，同時用@4聽不懂的語言大聲喊著指示。  將近一個鐘頭後，幾隻年輕的科博德把一個外觀奇特的金屬高腳杯捧上了地面，捧著它的姿態彷彿它擁有無可估量的價值。  @4把灰塔鎧甲放在礦坑地面靠近坑口的地方，退後幾步讓他們檢查。這些科博德似乎對這筆交易感到滿意，示意他們上前，讓他們也能從杯中啜飲一口。  @0第一個上前。他讓那清涼的液體從杯...

## node 1900012  (DIAL_Z19#31)
- speaker=0  style=0
- effects:
    - read Scouting -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [14890..0]] -> node 4294901805
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#32
- speaker=0  style=6
- effects:
    - event_bitmap_hi[2] bitop
    - bind speaker-name slot (kind=1 sub=12)
    - GIVE item '/' cond=20 to member#2 (cost 0)
- text: 一塊發亮的石頭吸引了@1的目光。  仔細一看，他發現那根本不是石頭。他找到了一小塊從夯實的泥土裡冒出來的金屬。他蹲下身仔細查看，試著撥開那覆蓋在上頭、多年來累積的塵土與碎石，然而它們卻緊緊不放。  他用劍緣挖掘，想把它從這座泥土墳墓裡解放出來，這才發現這東西比他原先猜想的還要大，但最終還是把它挖了出來。  他找到了一套古老的矮人鎧甲，人稱灰塔鎧甲！

## node 1900075  (DIAL_Z19#33)
- speaker=0  style=0
- effects:
    - read Haggling -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [16046..0]] -> node 4294901805
    - [always] -> node 0 (no jump)
- text: 士兵們攔下了他們。  一小群人橫在路上排開，全都穿著白色的及膝外衣，上面繡著藍色圓圈裡的灰狼頭紋章，那是拉姆特駐防要塞眾所皆知的軍徽。  「你們違反了宵禁，」其中一名守衛冷冷地說道。「我們接到命令，凡是在夜裡發現遊蕩在這些道路上的人，一律ó處死。」  @4明白對方在等一個解釋，他舔了舔嘴唇。「啊，這個嘛，我們外出是有正當理由的，」他說著，努力想擠出一個聽起來合理的藉口……

### (sub) DIAL_Z19#35
- speaker=0  style=0
- effects:
    - ACTION: request hotspot activation at player
    - SET flag 0xdac4=1 + timer (1800)
- text: @4犯了個ó錯。  雖然他不確定自己到底說錯了什麼，但他注意到守衛們臉上閃過一絲幾乎難以察覺的竊笑。他們耐著性子，等@4把這番信口胡謅的話講完。  「這故事真是ó有意思……」  「……可惜也非常假。」

## node 1900077  (DIAL_Z19#36)
- speaker=0  style=0
- text: 守衛的隊長直視著他們的眼睛，說道：「希望你們三位的武藝過得去。」

## node 1900110  (DIAL_Z19#37)
- speaker=0  style=6
- text: @4停下了腳步。  他望向擋在前方隘口的那隊守衛，喊道：「你們願意放我們安全通過嗎？」  回答來得又快又強硬：「奉亞魯莎親王之命，我們禁止你們再往前一步。」  @4雙手攏在嘴邊喊了回去：「我們是為王國公務出行。你們必須放我們通過。」  「我們接到嚴令，不准任何人再往東走，」對方回應道。  @0走上前站到@4身旁。「我們該怎麼辦？」  「我們人數差太多了，還是走吧。」

## node 1900014  (DIAL_Z19#38)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x4c mask=0x43 mode=0 chapters=-)] -> node 4278256386
    - [always] -> node 0 (no jump)

## node 1900015  (DIAL_Z19#40)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0xd4 mask=0x45 mode=0 chapters=-)] -> node 4278256386
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#41
- speaker=0  style=6
- effects:
    - ACTION: popup-retry-state = max(state, 30)
- branches:
    - [always] -> node 0 (no jump)
- text: 一個眼神閃爍的男人朝他們招了招手。  「小夥子們！」他說。「人稱『蛇眼』史比策。今晚手氣如何啊？看你們ñ挺走運的樣子。要不要來局擲骰子？」

### (sub) DIAL_Z19#42
- speaker=0  style=6
- effects:
    - event_bitmap_hi[3] bitop
- text: 他們湊到了那個眼神閃爍的男人身邊。  「現在不玩了，兄弟們！我欠了後屋一個傢伙一筆錢，我想他大概不會樂意我把錢給ñ你們，拿去賭博。」  注意到這男人似乎有點緊張，@4問道：「你欠的這個人是誰？」  「這一帶的人都管他叫『收帳人』。」他把聲音壓得幾乎只剩耳語，「聽說他在艾格利殺過一個叫『史特倫』的傢伙。」  「好吧，或許改天我們能找你玩一局，」@4說。

## node 1900016  (DIAL_Z19#43)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[3] (xor=0x20 mask=0x48 mode=0 chapters=-)] -> node 4278267904
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#44
- speaker=0  style=6
- effects:
    - event_bitmap_hi[3] bitop
- text: 一個睡眼惺忪的男人把他們推到一旁。  他眨著眼睛，卻怎麼也睜不開一隻眼，跌跌撞撞地走到房間角落的一張鋪蓋上躺下。  「你就是人稱『收帳人』的那個人嗎？」@4問道。  他沒好氣地坐起身，終於把兩隻眼睛都睜開，回道：「就算是又怎樣？」  「看來席爾班神殿有個見習修士欠了你一筆債沒還。我們只是覺得你該知道這事。」  那男人的眼裡閃過一絲……貪婪的光芒。他頓時清醒了不少，用略帶愉快的語氣說：「多謝你們！我明天就去拜訪拜訪他！」

## node 1900017  (DIAL_Z19#46)
- speaker=0  style=0
- effects:
    - event_bitmap_hi[4] bitop
    - SET flag 0x1ce9=1
    - SET flag 0x1a30=1
    - SET flag 0x1a59=1
    - SET flag 0x1a61=1
    - SET flag 0x1a5d=1
    - SET flag 0x1aa8=1
    - SET flag 0x1aa0=1
    - SET flag 0x1a9f=1
    - SET flag 0x1a54=1

## node 1900018  (DIAL_Z19#47)
- speaker=0  style=0
- effects:
    - read Scouting -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [0..0]] -> node 2621440
    - [event_bitmap_hi[4] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4608
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#48
- speaker=0  style=0
- effects:
    - event_bitmap_hi[4] bitop
    - GIVE item '.' cond=11 to member#2 (cost 0)
    - read Scouting -> dlg-result (sel=1)
    - bind speaker-name slot (kind=0 sub=12)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [always] -> node 0 (no jump)
- text: 一件閃亮的東西吸引了@0的目光。  他彎下腰仔細一看，撥開了好幾層泥土與灌木叢，赫然露出一套嚴重損毀的精靈鎧甲！他拉扯著想把它從地裡拔出來，卻驚訝地發現竟然毫不費力就拔了出來。顯然，把它埋起來的並非只是ñ歲月而已。

### (sub) DIAL_Z19#49
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「奇怪。從腳印的形狀判斷，我找到的這副鎧甲附近的足跡，看起來像是精靈的。」

### (sub) DIAL_Z19#50
- speaker=241  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「奇怪在哪？我猜精靈常常走這些路吧。」

## node 1900019  (DIAL_Z19#52)
- speaker=0  style=0
- effects:
    - read Scouting -> dlg-result (sel=1)
    - bind speaker-name slot (kind=0 sub=12)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x753d in [0..0]] -> node 2621440
    - [event_bitmap_hi[4] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 8704
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#53
- speaker=0  style=0
- effects:
    - event_bitmap_hi[4] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: @0不見了。  轉過身，@1發現他單膝跪地，正輕輕擦拭著泥土裡的某樣東西……

## node 1900020  (DIAL_Z19#55)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [23787..32789]] -> node 65537
    - [event_bitmap_hi[5] (xor=0x29 mask=0x51 mode=0 chapters=-)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#57
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [21572..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 那男人看起來不太高興。  「他話不多，」酒館另一頭傳來一個聲音。「他這人挺陰沉的。大夥都叫他葛林姆，因為他從來不笑也不露笑臉。」  另一個聲音說道：「他差不多算是巴本這裡的活招牌了。其實我們常拿陌生人來找點樂子。要是你能讓葛林姆笑出來，我們就給你八十枚索夫林。要不要試試看？」

### (sub) DIAL_Z19#58
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[5] (xor=0x61 mask=0x54 mode=0 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#59
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0111 in [22005..0]] -> node 4294901761
    - [flag 0x0112 in [22314..0]] -> node 4294901761
    - [flag 0x0113 in [22746..0]] -> node 4294901761
    - [flag 0x0114 in [23928..0]] -> node 4294901761
    - [flag 0x010a in [25326..0]] -> node 4294901761
- text: @4點了點頭。  「我們ñ當然願意試試，」他說道，接著轉過身低聲說：「讓我想想……我們要怎麼樣才能逗這傢伙笑呢？」

### (sub) DIAL_Z19#60
- speaker=0  style=3  flags=paged-text
- branches:
    - [flag 0x0111 in [22005..0]] -> node 4294901761
    - [flag 0x0112 in [22314..0]] -> node 4294901761
    - [flag 0x0113 in [22746..0]] -> node 4294901761
    - [flag 0x010a in [25326..0]] -> node 4294901761
- text: @4點了點頭。  「我們ñ當然願意試試，」他說道，接著轉過身低聲說：「讓我想想……我們要怎麼樣才能逗這傢伙笑呢？」

### (sub) DIAL_Z19#61
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 「我有辦法了，」@3說道。「這是我以前用來逗我爸爸開心的小把戲。」  他在葛林姆面前蹲下身，仰起頭，開始唱了起來。隨著這首蠢歌的歌詞從他嘴裡蹦出來，他小心翼翼地把一把湯匙平衡在鼻樑上。  葛林姆皺起了眉頭。

### (sub) DIAL_Z19#62
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 「ñ我來試試，」@5說道。他轉向葛林姆，帶著一絲狡黠的笑容，講起了一個葷段子，內容是一個矮人跟一個精靈少女的風流韻事。  @5帶著促狹的笑容環視全場，講到了笑點：「『這根本行不通嘛，』矮人說，『畢竟我在下面，妳在上面。』」故事講完，室內傳出一片憋著的哼笑與竊笑，但葛林姆只是點了點頭。

### (sub) DIAL_Z19#63
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4站了出來。  「這個小故事肯定能把他笑到從椅子上摔下來。這是一個圖蘭尼士兵告訴我的。說是他們有艘帆船遭遇了一場猛烈的風暴，船身受損嚴重，開始進水。船上是有救生筏的，大部分人都安全脫身了，但船長很快發現，救生筏只剩三個位置，船上卻還有四個人。  『我要問你們每個人一個問題，』他說。『答對了，就能跟你的同伴一起上救生筏。』他轉向第一個人問道：『ñ烈焰ñ風暴ñ號是在哪個半島外海沉沒的？』  『洪修尼半島，長官。』船長點了點頭，把那水手推向救生筏。接著他轉向第二個人。  『那天晚...

### (sub) DIAL_Z19#64
- speaker=0  style=6
- effects:
    - GIVE gold +800
    - event_bitmap_hi[5] bitop
- text: @4露出沉思的神情。  「蘇馬尼跟我們講過一個笑話，有誰還記得嗎？」他這麼一問，換來的只有一片茫然的目光。  「讓我看看能不能想起這個故事，」他對葛林姆說道。「在希迦庫莫在位的時候——」  「是希杜卡瑪，」葛林姆糾正道。  「對……總之，歐瑪……歐瑪爾……三位小家族的領主，被召去聖城覲見……  ……讚頌吧！皇帝陛下一定會喜歡他的新鞋子！」@4講完了，很滿意自己竟然記得ñ大部分的故事。他滿懷期待地轉向葛林姆，卻發現這男人臉上沒有一絲表情。@4厭惡地嘆了口氣，正打算伸手去拿錢袋時...

## node 1900021  (DIAL_Z19#66)
- speaker=0  style=0
- branches:
    - [flag 0x196c in [25735..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#67
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4消失在樓梯上。  一分鐘後他回來了，搖著頭……

### (sub) DIAL_Z19#69
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4消失在樓梯上。  一分鐘後他回來了，臉上帶著一副堅毅的神情……

### (sub) DIAL_Z19#70
- speaker=244  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [26127..0]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: 「這道樓梯一定通往麥克布爾加蘭多克翡翠礦坑。這些坑道非常複雜，但憑著我們在史特倫家找到的說明，應該能順利通過。要不要試著找找看藏書室地下庫？」

### (sub) DIAL_Z19#71
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
    - advance in-game time by 1800
    - load teleport table 26
- text: @0點了點頭。  兩人一起爬上那道長滿青苔的石階，通往礦坑。地上滿是碎石與裂開的木片，讓他們走得很艱難。但他們還是一路披荊斬棘，將近一個鐘頭後，來到一座鑄鐵梯子前，梯子直通天花板上一個漆黑的洞口。  梯級都生了鏽，金屬碎屑割破了他們的手掌，勾破了他們的衣服，彷彿在阻止他們爬出這座礦坑。梯子的頂端連著一條狹小的木造走廊，積滿了塵埃，還掛著絲絲蛛網。走廊盡頭的一扇門，費了好一番力氣才推開，門後是一間堆滿書籍的巨大房間……

## node 1900022  (DIAL_Z19#72)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[6] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#73
- speaker=0  style=6
- effects:
    - event_bitmap_hi[6] bitop
    - SET flag 0x1c85=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們被人發現了。  六名祭司聚集在這條藏書通道裡，全都對兩位陌生人的到來十分關切。一名寬肩的祭司從人群中走了出來。  「ó你們的出現或許能解釋不少事，」那祭司說道，一根手指朝他們指去。「我們從今天早上開始就出不去，才發現門從另一頭被閂上了。既然我不太相信我們伊夏神殿的祭司兄弟們會選擇把我們活活餓死……」  「完全不是那樣，」@4揮著手回答道。「我們上山路時碰到了你們的馬克修士。他說你們有位兄弟染上了奎格熱病，而他的病情不知為何跟這通道被封鎖的事有所關聯……」  「是那道神祕防...

### (sub) DIAL_Z19#74
- speaker=0  style=6
- effects:
    - GIVE item '8' cond=89 to member#2 (cost 0)
    - GIVE item '8' cond=95 to member#2 (cost 0)
    - GIVE item '8' cond=92 to member#2 (cost 0)
    - GIVE item '\x80' cond=90 to member#6 (cost 0)
    - event_bitmap_hi[6] bitop
    - advance in-game time by 7200
- text: 幾個鐘頭過去了。  看著古代抄寫員那幾乎難以辨認的字跡，@4看得雙眼發痠，把頭靠回了那座古老的書架上。「我完全不知道我們在找什麼，戈拉斯。我已經翻到六七處提到這座修道院的記載了，但不是發現跟豌豆實驗有關，就是跟一套新的圖書分類系統有關……」  一陣聲響引起了他們的注意。在他們所坐的書堆通道盡頭，一名祭司神情不悅地打量著這片凌亂。「你們怎麼還在這下面？」  「還在找答案呢，」@4說道。他含糊地朝身邊那半打攤開的書比了比。「還沒找到。」  「哦。」那祭司咬著嘴唇，似乎猶豫著要不要...

## node 1900026  (DIAL_Z19#75)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[7] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 3221230608
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#76
- speaker=0  style=6
- effects:
    - ?wOp12 a1=38 a2=0
    - GIVE gold +600
    - event_bitmap_hi[7] bitop
- text: 門開了。  「日安，兩位先生，」門口的男人說道。「我叫富蘭克林赫利，有什麼能為你們效勞的嗎？」  @4清了清嗓子。「我們在席爾班神殿聽說，你可能想找我們談談。」  「你們跟女祭司們談過了？」他難以置信地問道。「我本想找她們談談明年收成的事，卻有三個大呼小叫的蠢貨不讓我過去。」  「你不會再被那三個人找麻煩了，」@5說。  富蘭克林興奮地退回屋裡，片刻後拿著一袋錢幣出來，硬要他們收下作為酬謝。@4試著婉拒，但那男人堅持不肯。  他們謝過他的好意與慷慨，隨後便離開了。

## node 1900027  (DIAL_Z19#77)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [32974..0]] -> node 4294901762
    - [flag 0x1f91 in [20173..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#78
- speaker=0  style=6
- effects:
    - SET flag 0x1f91=1
    - (on-exit) play sfx 39
- text: 在門口迎接他們的男人身上有股魚腥味。  「大夥都叫我強提，」@4自我介紹後，他這麼回應道。  又閒聊了幾分鐘，他才透露自己是個漁夫，但由於身體不適，已經好幾天沒出海了。他說話時，還不時朝@0肩後某個看不見的東西投去陰沉的眼神。  @4正要再問他一個問題，強提卻突然氣呼呼地嘟噥了一句，砰地一聲把門關上了。任憑怎麼勸說，都沒法讓他再把門打開。

## node 1900028  (DIAL_Z19#79)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [19999..32815]] -> node 65537
    - [flag 0x7537 in [32974..0]] -> node 4294901763
    - [flag 0x1f92 in [20173..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#80
- speaker=0  style=6
- effects:
    - SET flag 0x1f92=1
    - (on-exit) play sfx 39
- text: 「你們看到我的金子了嗎？」門口那男人問道。  「恐怕沒有，」@4說。「你不是漁夫強提嗎？」他問道。  「是啊，可我不是故意的，」他語無倫次地回答。「我只是在找我的金子，我不知道它還……活著。」他不由自主地打了個寒顫。  @4看了看@0，接著繼續順著他的話說下去，儘管他不太明白這男人在說什麼。「但你ñ確實這麼做了。何不跟我們說說詳情？」  強提抖得更厲害了，說道：「那是個黑色的東西……我挖啊挖……然後它抓住了我的手臂，我想抽開，它卻不肯放，接著它就自己爬了出來……而且它ñ跟我說...

## node 1900029  (DIAL_Z19#81)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [19999..32815]] -> node 131073
    - [flag 0x1f93 in [20173..32815]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#82
- speaker=0  style=6
- effects:
    - SET flag 0x1f93=1
    - ?wOp12 a1=34 a2=0
    - (on-exit) play sfx 38
- text: 一個男人應了@4的敲門聲。  他滿臉通紅，額頭上豆大的汗珠似乎隨時要爭先恐後地滑落。他呼吸急促。  「你們是為了ñ那件事來的吧？」他瞪大眼睛問道。「是不是？」  經過好幾分鐘小心翼翼的試探，@4總算弄清楚，這男人相信自己從附近幾座墓地裡放出了什麼邪靈。他越是說起自己跟不死生物打交道的經歷，就越是害怕，直到最後渾身劇烈發抖，關上了門，退回自家相對安全的屋子裡。

## node 1900078  (DIAL_Z19#84)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 警告！ 這塊石頭下的惡靈是被泥土困住的，不是被死亡困住的。離遠一點！

### (sub) DIAL_Z19#85
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [34027..0]] -> node 65537
    - [always] -> node 0 (no jump)

## node 1900079  (DIAL_Z19#86)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 警告！ 這塊石頭下的惡靈是被泥土困住的，不是被死亡困住的。離遠一點！

### (sub) DIAL_Z19#87
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [34027..0]] -> node 131073
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#88
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4看著那堆泥土。  他彎下腰仔細查看，隨後站起身，臉上露出一副厭惡的表情……

### (sub) DIAL_Z19#89
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「有人徒手把這座墳墓挖開了。他們沒用工具，看樣子是赤手空拳挖開的。」

### (sub) DIAL_Z19#90
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「大概是野獸吧。要是氣味夠強烈，餓狼有時候是會去刨淺墳的。」

### (sub) DIAL_Z19#91
- speaker=244  style=0
- effects:
    - END conversation, result=1
- text: 「不，恐怕不是。泥土裡有些乾涸的血跡……而且我還找到了好幾片人類的ñ指甲ð，肯定是有人拼命刨挖堅硬的地面時弄斷的。」

### (sub) DIAL_Z19#92
- speaker=0  style=0  flags=paged-text
- effects:
    - bind speaker-name slot (kind=0 sub=7)
    - bind speaker-name slot (kind=1 sub=13)
- branches:
    - [flag 0x0100 in [34131..0]] -> node 4294901761
    - [flag 0x0101 in [34160..0]] -> node 4294901761
- text: 轉向@0，@1說道：「我們要不要把這座墳挖開？」

### (sub) DIAL_Z19#93
- speaker=0  style=0
- branches:
    - [flag 0xc3a3 in [34410..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#94
- speaker=0  style=0
- effects:
    - END conversation, result=1

### (sub) DIAL_Z19#95
- speaker=0  style=0
- effects:
    - END conversation, result=1
    - bind speaker-name slot (kind=0 sub=7)
    - bind speaker-name slot (kind=1 sub=13)
- text: 跟@1簡短商量過後，@0搖了搖頭。  「一不小心挖到死人，我可不太自在！再說，我們需要一把鏟子。用劍挖只會把劍弄壞。」

### (sub) DIAL_Z19#96
- speaker=0  style=0
- effects:
    - END conversation, result=1
- text: 這片地太硬了。  @4擦了擦額頭上的汗，氣得舉起雙手。「感覺像是有人特意把這裡夯實了，」他說。「大概是這家人怕遭盜墓賊惦記吧。」

## node 1900031  (DIAL_Z19#97)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[8] (xor=0x80 mask=0x87 mode=0 chapters=-)] -> node 100729346
    - [flag 0x7539 in [35723..0]] -> node 4294901761
    - [flag 0x7537 in [34937..0]] -> node 65537
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#98
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 門鎖著。  @4正要離開，卻注意到門上一根生鏽的釘子掛著一塊小牌子。牌子上寫著：妮雅的店——暫時歇業。  「這牌子寫得真怪，」@4一臉困惑地說道。

### (sub) DIAL_Z19#99
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
- text: @4在門口等著。  不到一分鐘，妮雅便從六趾酒館匆匆趕來，手裡的黃銅環上叮叮噹噹掛著一大串鑰匙。  「馬上就幫你們把門打開，」她一邊翻找著正確的鑰匙一邊說道。「啊，在這裡……」  她把鑰匙插進鎖裡，晃了幾下，直到「喀」一聲，隨後便推開了門。

### (sub) DIAL_Z19#100
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
- text: @4在門口等著。  不到一分鐘，妮雅便從六趾酒館匆匆趕來，手裡的黃銅環上叮叮噹噹掛著一大串鑰匙。  「一下子就幫你們把門打開，」她一邊翻找著正確的鑰匙一邊說道。「啊，找到了……」  她把鑰匙插進鎖裡，晃了幾下，直到「喀」一聲，隨後便推開了門。

### (sub) DIAL_Z19#101
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 1900032  (DIAL_Z19#102)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[8] (xor=0x99 mask=0x8d mode=0 chapters=-)] -> node 4278255873
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#103
- speaker=0  style=0
- branches:
    - [flag 0x1f39 in [35829..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#104
- speaker=0  style=0
- effects:
    - SET flag 0x1d22=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#105
- speaker=0  style=6
- effects:
    - ?wOp12 a1=38 a2=0
- text: 門沒上鎖。  @4走進這間小屋，環顧四周。從屋內擺設的簡樸程度判斷，他猜這屋子是麥克斯菲柏的家。「這就怪了，」他說道，注意到有幾樣東西看起來比一般農夫該有的家當要來得昂貴不少。這股不協調感讓他起了戒心，內心有股聲音催促他進一步搜查這位農夫的家當……

### (sub) DIAL_Z19#106
- speaker=0  style=0
- effects:
    - END conversation, result=65535
    - ?wOp12 a1=34 a2=0
- text: @4敲了敲門。  他靠在門框上等了好一會兒，一邊留意屋裡有沒有任何動靜。最後確定沒人回應，他聳了聳肩後退了幾步。  「看來沒人在家，」@4說。

## node 1900033  (DIAL_Z19#107)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x7537 in [20112..32815]] -> node 4294901764
    - [event_bitmap_hi[8] (xor=0x16 mask=0x8f mode=0 chapters=-)] -> node 4278255873
    - [flag 0x1f9d in [37531..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#108
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - apply status/condition to party idx=5 amt=-100
- text: @4敲了敲門。  幾秒鐘後，一個高大的男人迎了出來，自稱「赫歇爾」。  他邀請他們進屋，端出了一些食物與冰涼的麥酒。他們一邊用餐，一邊得知赫歇爾這間屋子原本是座舊驛站，他還興致勃勃地講了不少相關的故事，直到他們吃完準備離開為止。

### (sub) DIAL_Z19#109
- speaker=0  style=6
- effects:
    - SET flag 0x0052=1
    - SET flag 0x1f9d=1
- text: 門口那男人用一種奇怪的眼神打量著詹姆士。  「你一週前左右在我家後面到底在找什麼？」  詹姆士露出驚訝的神情。「我沒做過那種事，」他語帶防備地說。「或許你認錯人了。」  「算了吧，我猜，」那男人咕噥道，眼神裡卻沒什麼說服力。他把他們送到門口，聳了聳肩。「我還有別的事要忙，恕不奉陪了。還有，別再到赫歇爾的地盤上亂晃了，聽見沒……」

## node 1900034  (DIAL_Z19#111)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [event_bitmap_hi[8] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 4177539088
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#112
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [38876..0]] -> node 4294901761
    - [flag 0x0101 in [39871..0]] -> node 4294901761
- text: 門口那男人勃然大怒！  「就是你！」他指著@4喊道。「你賣給我的那隻手根本一文不值！那根本不是什麼榮耀之手！」  @4退後一步。「恐怕你認錯人了，我真的不知道你在說什麼。不過你剛才是說一隻手？我們可以跟你買回來。」  「我把那沒用的東西扔進了萊頓那口乾涸的井裡。一百五十枚索夫林！我當初就花了這麼多錢買它。你是說要是我把它撈回來，你們願意把錢還我？」

### (sub) DIAL_Z19#113
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [38905..0]] -> node 4294901910
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#114
- speaker=0  style=6
- effects:
    - GIVE item 'd' cond=1 to member#6 (cost 1500)
    - event_bitmap_hi[8] bitop
    - advance in-game time by 7200
- text: @4點了點頭。  那男人狐疑地打量著他們，威脅說要是他回來時他們不在場，就把他們吊起來，隨後便離開了。  幾個鐘頭後，他帶著一個小麻布袋回來了。他把袋子往桌上一放，發出「咚」的一聲，轉向@4。「你的手在這，現在把我的金子還來。」  「我沒拿你的金子，就當這是筆『買賣』吧，行嗎？」詹姆士說。  「隨你怎麼稱呼——我那該死的錢呢？」那男人吼道。  @4從錢袋裡取出錢，扔在了桌上。那男人貪婪地一把撈起，要求他們留下來等他數清楚為止。

## node 1900037  (DIAL_Z19#117)
- speaker=0  style=0
- branches:
    - [flag 0x1f6e in [40174..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#118
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 穀倉的門緊閉著。  「你在裡面的，」@4喊道。「我們想跟你談談。是伊凡斯卡德要我們來的！」  穀倉裡傳出一陣騷動，過了片刻，門緩緩開始敞開。

## node 1900038  (DIAL_Z19#120)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[8] (xor=0xeb mask=0x5c mode=21 chapters=8)] -> node 4278259728
    - [always] -> node 0 (no jump)

## node 1900039  (DIAL_Z19#122)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 賈瑞德萊克羅 擁有一間店鋪和一間酒館。此生從未匱乏過。

### (sub) DIAL_Z19#123
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [41347..0]] -> node 4294901761
    - [flag 0x0101 in [43282..0]] -> node 4294901761
- text: 轉向@4，@0說道：「我們要不要把這座墳挖開？」

### (sub) DIAL_Z19#124
- speaker=0  style=0
- branches:
    - [flag 0xc3a3 in [43154..0]] -> node 0 (no jump)
    - [event_bitmap_hi[8] (xor=0xf9 mask=0xa7 mode=0 chapters=-)] -> node 4278256128
    - [flag 0xc3b4 in [42382..0]] -> node 4294901761
    - [event_bitmap_hi[8] (xor=0xfe mask=0xa2 mode=0 chapters=-)] -> node 4278255872
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#125
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
    - END conversation, result=1
- text: 一個鐘頭過去了。  渾身沾滿墓穴污泥的@，帶著嫌惡的表情猛地掀開棺材的沉重蓋子，想看看裡頭裝著什麼。他頓時作嘔，一股濃烈的氨水味從棺材裡腐爛的遺骸中湧了出來。  「就只是具屍體，」@4哽著喉嚨說道。「我們把他重新蓋上吧。」

### (sub) DIAL_Z19#126
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
    - END conversation, result=1
- text: 一個鐘頭過去了。  渾身沾滿墓穴污泥的@，帶著嫌惡的表情猛地掀開棺材的沉重蓋子，想看看裡頭裝著什麼。他頓時作嘔，一股濃烈的氨水味從棺材裡腐爛的遺骸中湧了出來。  「就只是具屍體，」@4哽著喉嚨說道。「我們把他重新蓋上吧。」  「等等，」@3說道，指向洞裡。「你看。有人拿走了他的ó手。盜墓賊為什麼要偷一截屍體的部位？」  @4聳了聳肩。「要不是戈拉斯說過莫瑞德人有時會拿墳墓當祕密藏匿處，我怎麼也想不到自己會親手挖墳……不管怎樣，我們把他蓋好，上路吧。」

### (sub) DIAL_Z19#127
- speaker=0  style=0
- effects:
    - ?wOp12 a1=72 a2=0
    - play sfx 38
    - event_bitmap_hi[8] bitop
    - SET flag 0x1ace=1
    - REMOVE item 'd' cond=0
    - REMOVE item 'W' cond=0
    - END conversation, result=1
- text: @5的鏟尖發出一聲沉悶的木頭撞擊聲。  他用雙手把鬆軟未夯實的泥土推到一旁，用袖子擦去額頭上的汗水，走出了自己剛挖出的坑洞。  他示意有人把那隻手遞給他，小心翼翼地撬開了那口腐朽木箱的松木蓋。接著，他頭也不看一眼，把那隻手丟了進去，迅速蓋上蓋子——蓋子有一部分還在他手指間碎裂開來。  「安息吧，賈瑞德，」@3低聲說道。「來吧，我們把墳填上，離開這裡。」

### (sub) DIAL_Z19#128
- speaker=0  style=0
- effects:
    - END conversation, result=1
- text: @4搖了搖頭。  「我們ñ知道莫瑞德人沒有褻瀆過這座墳，」@4說。「就讓可憐的老賈瑞德安息吧，好嗎？」

### (sub) DIAL_Z19#129
- speaker=0  style=0
- effects:
    - END conversation, result=1
- text: @4搖了搖頭。  「不行，」他說。「沒有鏟子沒法挖。用劍挖只會把劍弄壞。」

### (sub) DIAL_Z19#130
- speaker=0  style=0
- effects:
    - END conversation, result=1

## node 1900041  (DIAL_Z19#131)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[9] (xor=0x42 mask=0xa9 mode=0 chapters=-)] -> node 4278256130
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#132
- speaker=0  style=6
- effects:
    - SET flag 0x753e=72
- text: 客棧老闆微笑著。  「歡迎啊，兩位！天很快就要黑了，你們該考慮在這過夜。外頭可危險得很！」  「危險？」@4問道。「怎麼說？」  客棧老闆傾身向前，低聲說道：「死人最近在這一帶棲身。他們夜裡遊蕩在路上，襲擊旅人。要是我是你們，我會考慮今晚就住這，明天一早再出發。」

## node 1900042  (DIAL_Z19#133)
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4停下了腳步。  他一臉困惑地轉向@0……

## node 1900043  (DIAL_Z19#135)
- speaker=0  style=0
- branches:
    - [flag 0x1d0f in [44083..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#136
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 1900074  (DIAL_Z19#138)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[9] (xor=0xb1 mask=0xaf mode=0 chapters=-)] -> node 4278256640
    - [flag 0x14e9 in [45218..0]] -> node 4294901761
    - [flag 0x1d10 in [44977..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#140
- speaker=0  style=6
- effects:
    - event_bitmap_hi[9] bitop
- branches:
    - [flag 0x1550 in [46541..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 貝拉一言不發地讓他們進了門。  門邊，哈芙拉正坐著，一雙纖細的手指緊揪著自己的頭髮，眼神望向遠方。她看著他們，臉上與其說是痛苦，不如說是如釋重負。「她死了？」  「是的，」@4回答道。「死了。至少我們可以這麼推斷。我們到底目睹了什麼？」  「一個不肯放手讓女兒離開的傻老太婆，」她說道，聲音顫抖著。她抓住貝拉的手尋求支撐，鼓起勇氣繼續說了下去。「我們女兒死後，我試著用我的能力找到她。我想，要是我能抓住她，我們就能把她留在身邊。」  「但你找到的不是她，」@4接話道。  哈芙拉搖...

### (sub) DIAL_Z19#141
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
- text: 深深望進@4的雙眼，哈芙拉緩緩開口道：「你將面對一個生命力與你自身不同的敵人，」她說。「那會發生在一個遙遠的地方，你必須汲取他們的力量，而非他們的生命，才能擊敗他們。而我感覺到，光憑你自己是辦不到的，因為會有另一個人，跟你一樣，是另一位法師。」  「他叫什麼名字？」@4問道，對這個答案很感興趣。  「我不知道，」那婦人羞愧地回答，垂眼望向地面。「說實話，我的能力相當有限。我能真正看見的，都已經告訴你們了。」  「夠了，」貝拉說道。「哈芙拉，你該休息了。」  明白這男人是想讓他...

### (sub) DIAL_Z19#142
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
- text: 深深望進@4的雙眼，哈芙拉緩緩開口道：「有個你正在尋找的人，善於隱藏在各種偽裝之下。他會欺騙你們，引開你們的注意力，避開自己，但他的氣味會出賣他。他將是解開一個重要謎團的關鍵人物。」  「他叫什麼名字？」@4問道，對這個答案很感興趣。  「我不知道，」那婦人羞愧地回答，垂眼望向地面。「說實話，我的能力相當有限。我能真正看見的，都已經告訴你們了。」  「夠了，」貝拉說道。「哈芙拉，你該休息了。」  明白這男人是想讓他們離開，@4向這位算命師與她的丈夫感激地點了點頭。「祝你們攜手...

### (sub) DIAL_Z19#143
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [48787..0]] -> node 4294901761
    - [flag 0x0101 in [48540..0]] -> node 4294901761
- text: 一個男人出現在門口。  他那頭烏黑的頭髮已染上灰白，眼角的皺紋十分深刻，他神情凝重地打量著他們，那目光深沉而銳利。「這裡是哈芙拉夫人的家，」他啞聲說道。「占卜未來、與死者對話、打聽傳聞。我們需要收取五十枚金幣的費用。你們想跟夫人談談嗎？」

### (sub) DIAL_Z19#145
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [49097..0]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#147
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x753f=0
    - TAKE gold -500
    - ACTION: EvtArgValue += 1
    - advance in-game time by 540
- branches:
    - [flag 0x0121 in [50742..0]] -> node 4294901761
    - [flag 0x0120 in [51710..0]] -> node 4294901761
    - [flag 0x0122 in [56302..0]] -> node 4294901761
    - [flag 0x0103 in [56819..0]] -> node 4294901761
- text: @4掏出了要求的金額，交了出去，跟著這位高大的男人往裡走。就在推開一道簾子之前，他停下腳步，低聲對他們說道。  「不管我妻子接下來說了什麼、做了什麼，都不要質疑，」他說。「我們最近痛失愛女，這件事動搖了哈芙拉對自己……ó能力的信心。要是她請求你們的接納，不論她說過什麼，都請善待她。」  他一言不發，掀開簾子，讓他們走進了後屋，哈芙拉夫人正在裡頭等候。她坐在一張桌前，身穿一件織錦背心，罩在一件染色淺淡的農婦罩衫外，手腕與頸間都戴著色澤鮮豔的木珠飾品。  「請坐，」她低聲說道，朝...

### (sub) DIAL_Z19#148
- speaker=0  style=0
- branches:
    - [flag 0x753f in [50240..0]] -> node 262144
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#149
- speaker=0  style=6  flags=paged-text
- effects:
    - ACTION: EvtArgValue += 1
    - advance in-game time by 540
- branches:
    - [flag 0x0121 in [50742..0]] -> node 4294901761
    - [flag 0x0120 in [51710..0]] -> node 4294901761
    - [flag 0x0122 in [56302..0]] -> node 4294901761
    - [flag 0x0103 in [56819..0]] -> node 4294901761
- text: 貝拉以為這場問卜已經結束，正要上前送客，哈芙拉卻示意他留在原地。「我看他們還沒問完，」她說道，帶著一抹淡淡的微笑望著他們。「憑你們付的這個價錢，還可以繼續發問。所以，陌生人們。就像我先前說的，我們可以聊聊當地的傳聞，我可以告訴你們未來，或是我可以與死者對話。你們想要哪一種？」

### (sub) DIAL_Z19#150
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 「傳聞，」她輕聲重複道。她在座位上向前傾身，迎上@4的目光，直視不移，聲音也隨之變得冷硬。「傳聞？我就告訴你們我唯一知道的傳聞吧。不少人來跟我提過，說夜裡有露莎卡在領航員之愚河附近的土地上遊蕩，但這些都是ó謊言……」  被這婦人咬字時透出的凶狠嚇了一跳，@4聳了聳肩。「我倒沒聽說過這事……」  「別去找那些露莎卡！」她的聲音依然帶著幾分狂亂，繼續說道。「她們對誰都沒有傷害！」  哈芙拉開始語無倫次時，貝拉一直靜靜待在一旁，這時他上前輕輕碰了碰她的肩膀，似乎緩解了她心頭湧起的那...

### (sub) DIAL_Z19#151
- speaker=0  style=6  flags=random branch (RND over choices)
- branches:
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
- text: 「好吧，」哈芙拉露出一絲虛弱的微笑說道，靠回她座椅上鬆軟的靠墊，姿態明顯放鬆了下來。「我們來看看你們的未來……」

### (sub) DIAL_Z19#152
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4不禁畏縮了一下，發現這位靈媒正緊盯著他，那目光坦白說比他所希望的還要熟悉幾分。「你將在一處隱密之地發現財富，但為了得到它，你將失去某樣得來不易的東西。得到它時，你會感到莫大的喜悅，但日後你會發現，未來的日子裡它其實藏著莫大的痛苦。」

### (sub) DIAL_Z19#153
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 深深望進@4的雙眼，她遲疑了片刻，隨後搖了搖頭。「我沒什麼能告訴你的，你早已心知肚明，」她說道，接著把目光鎖定在@5身上。「但你，我卻在你的未來裡看見了背叛。你會背棄自己曾發誓效忠的一切，變成自己曾經憎惡的模樣。你將面對自己最痛恨的敵人，而他會改變你。」

### (sub) DIAL_Z19#154
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 有好長一段時間，她靜靜坐著，目光既望向內心，也望向外界，最後她終於開口，聲音出奇地年輕。「一道長長的陰影與一顆星辰籠罩著你的家門，」她對@4說道。「即便你找到了與自己心靈相通的另一半，實現了你所盼望的一切，你也將在異鄉，因一段激情而失去你最親近的朋友。」

### (sub) DIAL_Z19#155
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 望著@3，她臉上的神情漸漸變了，化作一副痛苦與悔恨交織的面容。「你將孤獨一人，在飢餓中緩慢而痛苦地死去，」她語氣沉重地說道。「你曾以為能夠依靠的人，將在你最需要的時刻棄你而去，而在你死後，他們也會認為你玷污了自己的身分。」

### (sub) DIAL_Z19#156
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 哈芙拉臉上閃過一絲困惑，努力集中著精神。  「你的命運，我已經很久沒見過這樣的了。一把死人的鑰匙，將開啟那些看不見的門，它們藏在向七芒星俯首的人之下。」

### (sub) DIAL_Z19#157
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 她半闔著雙眼，恍惚地望著@4，說話時舔了舔嘴唇。「當你被逼上那條最漫長的道路時，你會想摧毀那件矇騙人心的器物，卻發現自己必須欺瞞守路之人。而在最後一刻，你將發現，救贖竟在一個看似孩子的男人身上。」

### (sub) DIAL_Z19#158
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 彷彿突然被一陣寒意攫住，她顫抖著，伸出一根瘦骨嶙峋的手指指向@3。「你將從一場致命的厄運中拯救你所敬重的人，卻也因此喚起了那些最盼望你毀滅之人的注意。從此以後，你將發現自己在世間漂泊，無名亦無伴。」

### (sub) DIAL_Z19#159
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0104 in [54674..0]] -> node 4294901761
    - [flag 0x011d in [54920..0]] -> node 4294901761
- text: 她把手交疊在膝上，平靜地望著他們，臉上漸漸恢復了她這個年紀該有的神情。「這就是我為你們看見的命運，」她說道，聲音裡帶著一絲微微的顫抖，透露出些許緊張。「命運已經藉由我開口了……」

### (sub) DIAL_Z19#160
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 察覺到讓他們相信自己所說的話對這位算命師有多重要，@4傾身向前，輕拍了拍老婦人的手。「我們相信你，哈芙拉，」他說道，臉上還閃過一抹笑容，加強了語氣。

### (sub) DIAL_Z19#161
- speaker=0  style=6
- effects:
    - SET flag 0x1d10=1
- text: @4對這老婦人的預言嗤之以鼻。「這些話我隨便也能說出來。街上那些瘋子講的話我大概都聽過了……」  「哈芙拉！」貝拉喊道，卻像根細枝般被一把推開，那老婦人猛地站起身，雙眼燃著怒火。她用磨尖的指甲抓向@4的臉，發出一聲已不再像人類的咆哮：「ã我ã是ã哈ã芙ã拉ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã你ã會ã相ã信ã的ã！ã…ã…」  貝拉公然哭了出來，繞到他那失魂落魄的妻...

### (sub) DIAL_Z19#162
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 老婦人閉上雙眼，渾身顫抖，彷彿一棵在狂風中彎腰的樹，嘴唇緊繃，臉上血色盡失。過了好一會兒，她搖了搖頭。「我沒辦法……幫你們。林絲克拉格瑪把你們想找的人抓得太緊了。」

### (sub) DIAL_Z19#163
- speaker=0  style=6
- effects:
    - ?wOp12 a1=75 a2=0
- text: 哈芙拉把手按上太陽穴，示意貝拉上前。「這事讓我感到ñ疲憊不堪，」她說道。「貝拉會送你們出去。要是你們想知道更多，改天再回來吧。」

## node 1900044  (DIAL_Z19#165)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [57106..0]] -> node 4294901761
    - [event_bitmap_hi[10] (xor=0xdd mask=0xdf mode=0 chapters=-)] -> node 3238003200
    - [event_bitmap_hi[10] (xor=0x79 mask=0xeb mode=0 chapters=-)] -> node 4278255872
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#166
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- text: 一名僕人應了門。  「我們能跟莊園的主人談談嗎？」@4問道。  那僕人搖了搖頭。「很抱歉，他正在休息。你們得明天早上再來了。」

### (sub) DIAL_Z19#168
- speaker=0  style=0
- branches:
    - [flag 0x9c43 in [57650..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#169
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=34 a2=0
    - event_bitmap_hi[10] bitop
- branches:
    - [flag 0x0100 in [60683..0]] -> node 4294901761
    - [flag 0x0101 in [58778..0]] -> node 4294901761
- text: 一名僕人在門口迎接了他們。  她領著他們進屋，帶到房間一處用簾子隔開的角落。她拉開簾子，露出一個瘦高、留著白鬍子、滿頭灰白頭髮的男人，他自我介紹說自己是萊頓爵爺。  「請原諒我這寒酸的住處，」他嘆了口氣。「我的財務狀況因我主人——羅姆尼的普雷瑟伯爵——過世而陷入了困境。」他忽然眼睛一亮，「或許幾位好心的先生願意幫我個小忙……」  「我們能幫上什麼忙？」@4問道。  這位爵爺又嘆了口氣，「我原本該替我已故的主人裝備六名騎士，送去羅姆尼，但他的產業在他過世後由異母兄弟繼承了，那人...

### (sub) DIAL_Z19#170
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4皺了皺臉。「這種東西ñ通常還真不是我們會隨身帶著的。」  「當然不是，」萊頓一邊送他們到門口一邊回答道。「但拜託，看看你們能幫上什麼忙。」

### (sub) DIAL_Z19#171
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - event_bitmap_hi[10] bitop
- text: 一名僕人在門口迎接了他們。  她領著他們進屋，帶到房間一處用簾子隔開的角落。她拉開簾子，露出一個瘦高、留著白鬍子、滿頭灰白頭髮的男人，他自我介紹說自己是萊頓爵爺。  「請原諒我這寒酸的住處，」他嘆了口氣。「我的財務狀況因我主人——羅姆尼的普雷瑟伯爵——過世而陷入了困境。」他忽然眼睛一亮，「或許幾位好心的先生願意幫我個小忙……」  「我們能幫上什麼忙？」@4問道。  這位爵爺又嘆了口氣，「我原本該替我已故的主人裝備六名騎士，送去羅姆尼，但他的產業在他過世後由異母兄弟繼承了，那人...

### (sub) DIAL_Z19#172
- speaker=0  style=0
- branches:
    - [flag 0x9c43 in [60553..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#174
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [60683..0]] -> node 4294901761
    - [flag 0x0101 in [60310..0]] -> node 4294901761
- text: 萊頓爵爺在門口迎接了他們。  「你們把我要的鎧甲帶來了嗎？」他興奮地問道。

### (sub) DIAL_Z19#175
- speaker=0  style=6
- effects:
    - event_bitmap_hi[10] bitop
    - SET flag 0x1a88=1
    - REMOVE item '0' cond=0
    - REMOVE item '0' cond=0
    - REMOVE item '0' cond=0
    - REMOVE item '0' cond=0
    - REMOVE item '0' cond=0
    - REMOVE item '0' cond=0
    - GIVE item '>' cond=1 to member#6 (cost 0)
    - GIVE item 'x' cond=15 to member#6 (cost 0)
- text: @4點頭回應，但他還沒來得及多說什麼，萊頓爵爺便一躍而起。「太好了！」這位爵爺滿臉笑容地喊道。「我不知道你們是怎麼辦到的，但我只能說謝謝！」  「很高興能幫上忙，」@4得體地說道。  這位爵爺開始在屋角一只雪松木箱裡翻找他的物品。「讓我瞧瞧，有什麼能拿來當作酬謝的。」  「這倒不必——」  「別胡說！」他厲聲說道。「我ñ想幫忙。啊，找到了。這些東西雖不算什麼，但你們或許用得上。」  他把一把美德鑰匙和一張羊皮紙紙條放上桌。他們謝過這位男人，從桌上拿起這些物品，收進了背包。

## node 1900046  (DIAL_Z19#176)
- speaker=0  style=6  flags=paged-text
- effects:
    - ACTION: CONSUME region encounter #151
    - ACTION: CONSUME region encounter #152
- branches:
    - [flag 0x0119 in [62018..0]] -> node 4294901761
    - [flag 0x0103 in [61837..0]] -> node 4294901761
- text: 一群全副武裝的人走近了。  「你們得先繳過路稅才能通過此地，」其中一人喊道。  @4按住劍柄，「你們憑什麼提出這種要求？」他喊了回去。  「萊頓爵爺的命令。現在要嘛掉頭回去，要嘛交出二十五枚金索夫林的稅金。你們選哪個？」

### (sub) DIAL_Z19#178
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [62294..0]] -> node 4294901785
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#180
- speaker=0  style=6
- effects:
    - event_bitmap_hi[10] bitop
    - TAKE gold -250
- text: 這袋子沉甸甸的。  @4咬著牙，強忍怒氣，把那袋金幣搬到眼前這些人面前。他故意把手舉得夠高，讓袋子砸在他們腳邊時發出響亮的聲響。  「萊頓爵爺謝謝你們，」他說道。「ñ我們也謝謝你們，」其他人笑著說道。「好了，你們可以過去了。」

## node 1900047  (DIAL_Z19#181)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[36] (xor=0xe4 mask=0xf4 mode=0 chapters=-)] -> node 4278265864
    - [event_bitmap_hi[36] (xor=0xe2 mask=0xf7 mode=0 chapters=-)] -> node 4278255872
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#182
- speaker=0  style=6
- effects:
    - event_bitmap_hi[36] bitop
    - SET flag 0x1fc9=1
- text: 波德里奇朝他們喊道。  「要是你們拿這一套來耍ó我，我早就把你們的肝挖出來當早餐了，」他說道，指的是他們先前留下那批動過手腳的口糧。「執行官比較寬容。他說，敢玩這種把戲的人，起碼有膽量跟他見上一面。我會解除陷阱，讓你們過去。」  @3畏縮了一下，看著這名守衛從外衣裡掏出一卷卷軸，念起了上頭的咒語，把大部分的字都念得亂七八糟。他曾經親眼見過一個新手法師，就因為念錯了咒語裡的一個關鍵句子而被烈焰吞噬，從此在提伯恩的街上留下了一塊永久的油漬。讓他鬆了口氣的是，那道陷阱平安無事地解除...

### (sub) DIAL_Z19#183
- speaker=0  style=6  flags=paged-text
- effects:
    - SET flag 0x1fbb=1
- branches:
    - [flag 0x0100 in [64176..0]] -> node 4294901761
    - [flag 0x0101 in [64537..0]] -> node 4294901761
- text: 一個男人朝他們喊話。  「你們把首席執行官的晚餐帶來了嗎？」他問道，顯然把他們的到來當成了例行公事的一部分。@4沒能立刻回應，那男人似乎有點不耐煩了。「你們到底是不是雜貨店派來的送貨人？」  「是，」@4立刻扯了個謊，覺得這是矇混過守衛最簡單的辦法。「我們這就進去，把晚餐送給他……」  那男人皺起眉頭。「看來沒人跟你們解釋過這裡的規矩。沒人能繞過波德里奇，」他說著，用力拍了拍自己的胸口。「你們得繞到那片田地旁邊，把貨放進箱子裡，然後就可以走了。現在，你們到底有沒有帶他的食物？...

### (sub) DIAL_Z19#184
- speaker=0  style=0
- branches:
    - [flag 0xc39a in [64396..0]] -> node 4294901761
    - [flag 0xc399 in [64396..0]] -> node 4294901761
    - [flag 0xc398 in [64396..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 1900106  (DIAL_Z19#188)
- speaker=0  style=0
- branches:
    - [flag 0x1fbb in [237..1]] -> node 0 (no jump)
    - [event_bitmap_hi[36] (xor=0x1a mask=0x00 mode=1 chapters=-)] -> node 4278265856
    - [event_bitmap_hi[36] (xor=0xed mask=0x00 mode=1 chapters=-)] -> node 4278263808
    - [flag 0x9c4c in [64777..0]] -> node 4294901761
    - [flag 0x9c4d in [65086..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#189
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4闔上了箱子的蓋子。  「那，我們現在該怎麼辦？」@5問道。  「去酒館等著，」@4回答道。「我們明天再回來，運氣好的話，亞利會願意見我們。填飽肚子往往能讓人願意開口。希望這位首席執行官也不例外。」

### (sub) DIAL_Z19#190
- speaker=0  style=6
- effects:
    - event_bitmap_hi[36] bitop
    - SET flag 0xdc2c=1 + timer (36000)
- branches:
    - [always] -> node 0 (no jump)
- text: @4闔上了箱子的蓋子。  「那，我們現在該怎麼辦？」@5問道。  「等著，」@4回答道。「我們明天再回來，運氣好的話，亞利會願意見我們。當然，他可能不太高興我們留給他的是壞掉的食物，但至少這或許能讓我們見上他一面。」  「那要是他因為我們搞的這齣把戲想殺了我們呢？」@5回道。  @4聳了聳肩。「到時候再說吧。現在先找個地方舒舒服服待著。」

### (sub) DIAL_Z19#191
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝@5揮了揮手示意他退下。  「他們一定在屋裡盯著我們，」@4說。「要是我們對這箱子動作太大，他們會起疑心的。現在先離開這裡，等明天再說。」

### (sub) DIAL_Z19#192
- speaker=0  style=0
- effects:
    - ACTION: clear fixed-obj (3) inventory

## node 1900105  (DIAL_Z19#193)
- speaker=0  style=0
- branches:
    - [flag 0xdc30 in [23787..32789]] -> node 4294901761
    - [flag 0x7537 in [295..1]] -> node 196611
    - [always] -> node 0 (no jump)

## node 1900048  (DIAL_Z19#195)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[36] (xor=0xb4 mask=0x06 mode=1 chapters=-)] -> node 769
    - [event_bitmap_hi[36] (xor=0x7d mask=0x0b mode=1 chapters=-)] -> node 4278288384
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#196
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#197
- speaker=0  style=0
- effects:
    - event_bitmap_hi[36] bitop
- branches:
    - [flag 0x1fc9 in [1774..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#198
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那位執行官在門口迎接了他們。  這人幾乎全禿，只剩耳後幾撮短短的雜毛，像疏於照料的雜草。以他在羅姆尼各公會之間掌握的權勢而言，這位首席執行官身材出奇矮小。他朝他們露出凶狠的笑容，用一隻長滿水泡的手拍了拍@4的肩膀。  「我是亞利鋼魂，」他說。「不管怎麼說，你們膽子倒是不小。還好我沒不經檢查就把你們放進箱子裡的東西給吃了。我很早以前就學到教訓，得提防外人。」

### (sub) DIAL_Z19#199
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 那位執行官在門口迎接了他們。  這人幾乎全禿，只剩耳後幾撮短短的雜毛，像疏於照料的雜草。以他在羅姆尼各公會之間掌握的權勢而言，這位首席執行官身材出奇矮小。他朝他們露出凶狠的笑容，用一隻長滿水泡的手拍了拍@4的肩膀。  「我是亞利鋼魂，」他說。「不管怎麼說，你們膽子倒是不小。沒幾個人看見外頭那個陷阱後還有膽子闖過去。我想至少見見有膽識又有腦子做到這件事的人。」

### (sub) DIAL_Z19#200
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞利朝他們微笑。  他用毛巾擦去臉上的煤灰，看起來是真心對再次見到他們感到高興。

### (sub) DIAL_Z19#201
- speaker=0  style=0
- effects:
    - event_bitmap_hi[36] bitop
- branches:
    - [event_bitmap_hi[36] (xor=0x3f mask=0x0c mode=1 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#202
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 38
    - event_bitmap_hi[36] bitop
    - GIVE item '\x7f' cond=100 to member#2 (cost 0)
- text: 他邀請他們進屋，端出了些食物與水，聊起了羅姆尼附近的公會之爭。「這事的起因，是拉船工會把運價哄抬得太高，沒人負擔得起走水路運貨了，」他解釋道。「這逼得米契爾威蘭德轉而投靠羅姆尼公會——好吧，我跟你說，拉船工會的首席執行官對ñ這事可不太高興——覺得這個新公會是在搶他的生意，但你能怪他嗎？我是說米契爾。」  @4搖了搖頭。「羅姆尼公爵對這件事似乎也不太滿意，」他說。「他希望你能坐上談判桌，好平息羅姆尼這場暴力衝突。」  亞利點了點頭。「是骯髒的政治把這場亂子鬧出來的，看來也只能靠...

## node 1900089  (DIAL_Z19#204)
- speaker=0  style=0
- branches:
    - [flag 0x1fbc in [7921..1]] -> node 4294901761
    - [event_bitmap_hi[36] (xor=0x23 mask=0x16 mode=1 chapters=-)] -> node 4278255873
    - [event_bitmap_hi[36] (xor=0xf2 mask=0x33 mode=1 chapters=-)] -> node 4278256640
    - [event_bitmap_hi[36] (xor=0x5a mask=0x2c mode=1 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[36] (xor=0xc4 mask=0x29 mode=1 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#205
- speaker=0  style=6
- effects:
    - SET flag 0x1fbc=1
- text: 會議廳裡擠滿了人。  室內聚集著十來個滿面風霜的男人，全都圍坐在一張長桌旁，桌首坐著一個留著山羊鬍的年輕人。他們一進門，一名僕人便迅速指引他們坐到旁邊的一張長凳上，示意此刻正在進行一場要事會議。  「……我才不管米契爾威蘭德到底在幹什麼還是沒幹什麼，」那個蓄鬍的男人語氣嚴厲地說道。「ó我是羅姆尼公爵，你們得照我的要求去做，不然我就從巴斯泰拉調人過來。你們真想引起萊亞姆王對這件事的注意嗎？」  被這位年輕公爵語氣中的強硬鎮住，在座的幾位公會首領都不安地在座位上挪動著身子。其中一...

### (sub) DIAL_Z19#207
- speaker=0  style=6
- effects:
    - event_bitmap_hi[36] bitop
- text: 他們被帶進了一間房間。  羅姆尼公爵盤腿坐在一張大木椅上，盯著堆在會議桌上的一具龐大隆起的物體，他那張略顯年輕的臉龐上明顯籠罩著某種深切的憂慮。  「布單底下是什麼？」@4問道。  「波索錢德勒，」公爵沉重地回答道。「他們在巷子裡發現他的屍體，先丟在這裡，等殯葬業者來收。」  「被謀殺的？」  公爵嘆了口氣。「幸好這不是什麼大謎團。他跟磨坊工會的首領起了衝突，被三個傭兵逼到了角落裡。我們已經把他們全都收押了。事情鬧成這樣，我們現在得經常生火燒屍體，就為了平息公會之間這場愚蠢的...

### (sub) DIAL_Z19#209
- speaker=0  style=6
- effects:
    - event_bitmap_hi[36] bitop
    - GIVE gold +3000
    - GIVE item '>' cond=1 to member#6 (cost 0)
    - advance in-game time by 1800
- text: 武裝守衛的軍士攔下了他們。  他伸手按在@4胸前，搖了搖頭。「很抱歉，但公爵正在……」他話說到一半突然停住，因為公爵已經出現在他身後。  「沒關係，」公爵說道。「讓他們進來，軍士。我正等著這幾位先生。我猜他們是來告訴我，已經說服亞利鋼魂願意來幫我了。我猜得沒錯吧？」  @4很快確認了這件事，跟著公爵走進了空無一人的會議廳。他見長凳已經從室內撤走，便毫不客氣地在桌邊坐下，@5與@3則站在門邊。  「趁我還沒忘記，先給你們的酬勞，」公爵說道，打開了房間角落的一只箱子。他翻找著裡頭...

## node 1900098  (DIAL_Z19#211)
- speaker=0  style=3
- text: 前往羅姆尼公爵的會議廳

## node 1900090  (DIAL_Z19#212)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20139..32815]] -> node 4294901761
    - [flag 0x1faa in [20112..32815]] -> node 4294901761
    - [flag 0x7537 in [50906..32813]] -> node 393222
    - [flag 0x1f98 in [20112..32815]] -> node 4294901761
    - [flag 0x7537 in [50906..32813]] -> node 196611
    - [always] -> node 0 (no jump)

## node 1900097  (DIAL_Z19#213)
- speaker=0  style=0
- branches:
    - [flag 0x753c in [20141..32815]] -> node 720897
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#214
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [15206..1]] -> node 196611
    - [flag 0x1fb1 in [14837..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#215
- speaker=0  style=6
- effects:
    - ?wOp12 a1=38 a2=0
    - SET flag 0x1fb1=1
    - END conversation, result=65535
- branches:
    - [always] -> node 0 (no jump)
- text: @4聞到了酒味。  推開店門，一個尖臉男人扛著一只木桶迎面而來。他迅速把桶子跟其他木桶堆在一起，用毛巾擦了擦手，隨後伸出手。  「哈蘭，」他自我介紹道。「不搬東西的時候，我就是這裡的釀酒師傅。」  「那這裡到底ó是什麼地方？」@4回應道。  「這裡是倒扣木桶酒館。我們是羅姆尼這一帶最好的釀酒坊。要不要嚐嚐我們的酒？我們釀的蘋果酒可是一絕，」店主說道。「我可以馬上替你們斟一些來。」  @4盡可能客氣地婉拒了。「我們得保持頭腦清醒，」他說。「前面還有很長一段路要走，聽說最近這一帶...

### (sub) DIAL_Z19#216
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- branches:
    - [always] -> node 0 (no jump)
- text: 哈蘭在門口迎接了他們。  「有事嗎？」這位釀酒師問道，臉上沾滿了看起來髒兮兮的煙灰。  「我們只是想順道進來看看，」@3插話道。「要是你不忙的話。」  「沒空，」那男人說著，搖了搖頭。「我正在釀一批新酒，得隨時盯著才行。抱歉了。改天再來吧。」

### (sub) DIAL_Z19#217
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[11] (xor=0x54 mask=0x43 mode=1 chapters=-)] -> node 4278259712
    - [flag 0x1ec0 in [15245..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#218
- speaker=0  style=6
- effects:
    - ?wOp12 a1=38 a2=0
    - event_bitmap_hi[11] bitop
    - SET flag 0x1ceb=1
- text: @4聞到了酒味。  推開店門，一個尖臉男人扛著一只木桶迎面而來。他迅速把桶子跟其他木桶堆在一起，用毛巾擦了擦手，隨後伸出手。「歡迎光臨倒扣木桶酒館。羅姆尼這一帶最好的釀酒坊。要不要嚐嚐我們的酒？我們釀的蘋果酒可是一絕……」  「我相信一定很棒，但不用了，謝謝，」@4說。「我們是有別的事找你。你最近有沒有送過一批特別的貨到羅姆尼的黑羊酒館？」  那男人點了點頭。「有的。鎮上一個叫米契爾威蘭德的人親自過來下的訂單，用紅寶石付的錢。」  認出這是羅姆尼玻璃匠公會會長的名字，@4挑了...

### (sub) DIAL_Z19#219
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 那位釀酒師在門口迎接了他們。  「有事嗎？」這位釀酒師問道，臉上沾滿了看起來髒兮兮的煙灰。  「我們只是想順道進來嚐嚐你的酒，」@4說。「要是你不忙的話。」  「沒空，」那男人說著，搖了搖頭。「我正在釀一批新酒，得隨時盯著才行。抱歉了。改天再來吧。」

### (sub) DIAL_Z19#220
- speaker=0  style=6
- effects:
    - END conversation, result=65535
- text: 一個男人在門口迎接了他們。  「有事嗎？」這位釀酒師問道，臉上沾滿了看起來髒兮兮的煙灰。  「我們只是想順道進來嚐嚐你的酒，」@4說。「要是你不忙的話。」  「沒空，」那男人說著，搖了搖頭。「我正在釀一批新酒，得隨時盯著才行。抱歉了。改天再來吧。」

## node 1900050  (DIAL_Z19#221)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20112..32815]] -> node 4294901761
    - [event_bitmap_hi[34] (xor=0x66 mask=0x46 mode=1 chapters=-)] -> node 1281
    - [flag 0xc39f in [18488..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#222
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
    - (on-exit) play sfx 39
- text: @4敲了敲門。  過了片刻，一個臉色蒼白的婦人應了門，一隻手臂始終撐在門後，以防來客不懷好意。  「你們想幹嘛？」她顯然是在對@4說話，眼神卻不安地飄向那位莫瑞德人。「我最近跟陌生人打交道的次數已經夠多了。」  「我們只是想要點水……」@4才開口，卻發現這位老婦人已經砰地一聲關上了門。

### (sub) DIAL_Z19#223
- speaker=0  style=6  flags=paged-text
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
- branches:
    - [flag 0x0100 in [19078..1]] -> node 4294901761
    - [flag 0x0101 in [20251..1]] -> node 4294901761
- text: 佩特魯姆開了門。  這位獨自從馬拉克十字鎮徒步跋涉到黑沼鎮的老婦人，精神好得出乎意料，她露出缺了牙的笑容招呼他們，示意請他們進屋。@4搖了搖頭，仍站在門口沒動。  「抱歉，我們其實沒什麼時間進去坐，」他致歉道。「我們只是想順道來看看，確認你一路平安到家了。」  「哦，是啊，」她用濃重的鄉音回答道。「是平安到家了。那你們幾位呢？有沒有順道幫我把我留在王后巷旅店的那只木桶帶回來？」

### (sub) DIAL_Z19#224
- speaker=0  style=6
- effects:
    - event_bitmap_hi[34] bitop
    - SET flag 0x1a89=1
    - REMOVE item 'O' cond=0
    - GIVE item 's' cond=16 to member#6 (cost 0)
    - GIVE item 'P' cond=4 to member#6 (cost 0)
- text: 「帶回來了，」@4說道，一邊把木桶遞了過去，一邊意味深長地看了@5一眼。「就放在你原本放的地方。」  「我可找不到比你更好的小夥子了，」她欣喜地說道，接過木桶。她把桶子放進門邊後，把手指放進嘴裡吹了聲口哨。「ó喂，烏蘭，我叫你放的那些東西你放哪去了？」  從屋子後方傳來另一個女人的回話聲，雖然聽不太清楚她在說什麼。佩特魯姆點了點頭，叫他們再稍等一下，隨後便消失在昏暗的屋內。  「找到了，」她說著，過了片刻又出現在門口。她迅速把幾件小飾品塞進了@4手裡。「其實也沒什麼特別的，但...

### (sub) DIAL_Z19#225
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 39
- text: 「抱歉，我們沒帶你的木桶，」@4連忙撒了個謊。「不過要是我們去了馬拉克十字鎮，一定會幫你帶回來的。」  「唉呀，」她失望地叫了一聲。「那真是不走運了。」她在裙子前擦了擦手，回頭望向屋內。「我正在幫烏蘭弄點吃的，還是先進去忙吧。兩位，日安了。」

### (sub) DIAL_Z19#226
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
- text: 佩特魯姆開了門。  這位獨自從馬拉克十字鎮徒步跋涉到黑沼鎮的老婦人，精神好得出乎意料，她露出缺了牙的笑容招呼他們，示意請他們進屋。@4搖了搖頭，仍站在門口沒動。  「抱歉，我們其實沒什麼時間進去坐，」他致歉道。「我們只是想順道來看看，確認你一路平安到家了。」  「哦，是啊，」她用濃重的鄉音回答道。「是平安到家了。那你們幾位呢？有沒有順道幫我把我留在王后巷旅店的那只木桶帶回來？」  「我們還沒去過馬拉克十字鎮，」@4回答道。「不過要是我們去了，一定會幫你帶回來的。」  「唉呀，...

## node 1900072  (DIAL_Z19#227)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

## node 1900054  (DIAL_Z19#229)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0x3a mask=0x56 mode=1 chapters=-)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#230
- speaker=0  style=0
- effects:
    - ?wOp12 a1=34 a2=0
- text: 奧奇不在家。  @4又敲了敲他家的門，卻沒人回應，他轉向@0說道：「他好像不在。我們走吧。」

### (sub) DIAL_Z19#231
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0xe7 mask=0x59 mode=1 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#232
- speaker=0  style=6
- effects:
    - ?wOp12 a1=38 a2=0
    - play sfx 39
    - event_bitmap_hi[26] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: @4還沒敲門，一個滿臉慍色的男人便出現在門口。  「你們不該來的，」那男人用濃重的哈達提口音拖長了聲音說道。「我院子裡那些死掉的東西也都是來拜訪的。」  他神情擔憂地轉向那男人，說道：「或許你該告訴我們到底發生了什麼事……」  那男人嘆了口氣。「好吧。俺叫奧奇，是個捕獸人。這附近東南方住著個女巫婆——她給俺惹了不少麻煩。把俺陷阱附近的動物都嚇跑了！俺去找她理論的時候，她居然對俺家下了咒！巨大的蠍子每次都會——」那男人忽然倒抽一口氣，砰地一聲把門關上了。  @0喃喃自語道。「蠍...

### (sub) DIAL_Z19#233
- speaker=0  style=0
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
    - (on-exit) play sfx 39
- branches:
    - [always] -> node 0 (no jump)
- text: 奧奇看起來驚慌失措。  「你們得幫俺想想辦法！要是俺出不了家門，俺會死在這裡的！那女巫婆——啊啊！」他尖叫一聲，砰地一聲把門關上了。

### (sub) DIAL_Z19#235
- speaker=0  style=0
- effects:
    - event_bitmap_hi[26] bitop
    - ACTION: CONSUME region encounter #375
    - ACTION: request hotspot activation at player
- text: @4擺出應戰的架勢。  「這些東西大概是用某種小咒法變出來的，但有一件事我ñ很清楚——牠們絕不只是幻象而已！」

## node 1900055  (DIAL_Z19#236)
- speaker=0  style=0
- effects:
    - play sfx 67
    - play sfx 67
    - play sfx 67
    - play sfx 67
    - play sfx 67
- branches:
    - [event_bitmap_hi[26] (xor=0x18 mask=0x5e mode=1 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#237
- speaker=0  style=6
- effects:
    - play sfx 67
    - play sfx 67
    - play sfx 34
- text: 一個女人的聲音突然充斥了@4的腦海。  「我曾受過冤屈，除非這份冤屈得以昭雪，否則我不會開口。」  那聲音來得快，去得也快。他搖了搖頭，想把這個不速之客從腦海裡甩出去——就像抖掉鹽罐裡的鹽粒一樣——接著轉身敲了敲門，想引起屋主的回應。  發現沒人回應，他決定他們該離開了。

### (sub) DIAL_Z19#238
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0x87 mask=0x5f mode=1 chapters=-)] -> node 4278256644
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#240
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - event_bitmap_hi[26] bitop
    - GIVE item 't' cond=14 to member#6 (cost 0)
    - GIVE item 't' cond=14 to member#2 (cost 0)
- text: 一個滿臉皺紋的婦人應了@4的敲門聲。  「我從你的心思裡看出來了，你已經為我平反了那樁冤屈，」她說道。她謝過他們，自我介紹說自己叫薇琳蒂，接著嘆了口氣。  「人們不理解我的魔法天賦，所以我搬到了幽暗林，想在寧靜的獨居生活中度過餘生。我只是想一個人清靜清靜。」  相信了這位老婦人的說詞，@4溫和地說道：「恐怕你那位哈達提鄰居一直以為，是你害他捕獵不順的。」  那婦人神情黯然。「這人也真是簡單。像他這種人，往往害怕自己不理解的事物。我大概該對他多點寬容，但當他殺了我幾隻牲畜、還在...

## node 1900056  (DIAL_Z19#241)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這口井看起來很誘人。  井邊的雜草纏繞叢生，是個不錯的跡象，表示這口井應該還沒乾涸。

### (sub) DIAL_Z19#242
- speaker=240  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [25820..1]] -> node 4294901761
    - [flag 0x0101 in [26882..1]] -> node 4294901761
- text: 「我喉嚨渴得要命，水袋也快空了。要不要打點水來喝？」

### (sub) DIAL_Z19#243
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0xf9 mask=0x64 mode=1 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#244
- speaker=0  style=6
- effects:
    - apply status/condition to party idx=5 amt=-100
    - RAISE Health+Stamina of party by 256
    - play sfx 64
- text: @4把水桶放進了井裡。  水桶「撲通」一聲沉到了井底，他等它完全沉入水中後，才轉動木製的絞盤把它拉上來。  井水清涼可口，他們貪婪地喝了個痛快，才把水袋裝滿，準備繼續趕路。

### (sub) DIAL_Z19#245
- speaker=0  style=6
- effects:
    - event_bitmap_hi[26] bitop
    - apply status/condition to member#0 idx=0 amt=18
    - play sfx 64
- branches:
    - [always] -> node 0 (no jump)
- text: @4把水桶放進了井裡。  水桶「撲通」一聲沉到了井底，他等它完全沉入水中後，才轉動木製的絞盤把它拉上來。  @0從背包裡取出水袋裝滿了水，貪婪地喝了一大口，其他人也跟著準備如法炮製。

### (sub) DIAL_Z19#246
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「等等！有什麼……伊夏神在上，我們早該小心點的。這口井裡除了水，還有別的東西。我想它被下毒了！」

### (sub) DIAL_Z19#247
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你確定嗎？誰會想毒害自己家的井？除非……」

### (sub) DIAL_Z19#248
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「……除非有人想毒害這口井的ñ主人。」

### (sub) DIAL_Z19#249
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[26] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278272064
    - [flag 0xc3c1 in [27442..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#251
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x0100 in [27777..1]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4盯著水桶。  他把桶子一傾，在裡頭摸索了一陣。等他終於抽回手時，拇指與食指間夾著一顆小小的紅色漿果。  「果然沒錯，是銀刺，」他說道。「我們包裡有銀刺解毒劑。要不要拿來替這口井解毒？」

### (sub) DIAL_Z19#252
- speaker=0  style=0
- effects:
    - SET flag 0x1cf8=1
    - event_bitmap_hi[26] bitop
    - REMOVE item 'q' cond=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那瓶銀刺解毒劑閃閃發光。  @4動作迅速，把幾滴珍貴的液體倒進了井裡。片刻猶豫後，他把整瓶藥水倒了個底朝天，將剩餘的內容物全數灑進了那口幽暗的水井之中。

## node 1900107  (DIAL_Z19#254)
- speaker=0  style=0
- branches:
    - [flag 0x1eb9 in [28306..1]] -> node 0 (no jump)
    - [flag 0x1d52 in [20139..32815]] -> node 0 (no jump)
    - [flag 0x1fbd in [28831..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#255
- speaker=0  style=0
- effects:
    - END conversation, result=65535

### (sub) DIAL_Z19#256
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - play sfx 38
    - SET flag 0x1fbd=1
- text: @4倒抽了一口氣。  這座倉庫裡堆滿了急需的補給品。他暗自思忖，這些東西足夠養活一支私人軍隊了。假如他們兩個都能撐過這場劫難，他得好好跟亞魯莎談談皇室的祕密才行。  「菲力普說我們可以隨意拿取所需的東西，」他說。「眼下ñ我滿腦子只想著找點東西吃。我們先補給一下再上路吧。ó誰知道下次還要多久才能再見到這麼多糧食。」

### (sub) DIAL_Z19#257
- speaker=0  style=0  flags=reload-scr-between-pages
- effects:
    - ?wOp12 a1=38 a2=0
- text: @4打開了門。  「來看看這裡還有沒有什麼我們上次沒拿到、用得上的東西，」他說道。

## node 1900057  (DIAL_Z19#258)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[27] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 50397184
    - [event_bitmap_hi[27] (xor=0x90 mask=0x4e mode=47 chapters=8)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#259
- speaker=0  style=0
- effects:
    - SET flag 0x0008=1
- branches:
    - [event_bitmap_hi[27] (xor=0xe7 mask=0x75 mode=1 chapters=-)] -> node 4278259712
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#260
- speaker=0  style=6
- effects:
    - ?wOp12 a1=67 a2=0
    - ?wOp12 a1=67 a2=0
    - ?wOp12 a1=67 a2=0
    - play sfx 38
    - event_bitmap_hi[27] bitop
- branches:
    - [flag 0xc3af in [30661..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 一隻佈滿皺紋的手推開了門。  「有事嗎？」一個矮小的男人啞聲說道，那虛弱的嗓音因年邁而顫抖著。  @4微笑道：「我們不是有意打擾您的，先生。這一帶最近有什麼消息嗎？」  那老人垂下了頭，說話時眼眶泛起了淚水。「別被你們看到的表象給騙了。站在你們面前這個人，實際年齡連看起來的一半都不到。」  「要是你說的是真的，這事是怎麼發生的？」@0問道。  「這是千真萬確的。俺原本在這裡以東的地方設陷阱捕獵——待了大約一個月——後來忽然發現自己一天比一天虛弱。俺決定回家，就在回程路上，看見...

### (sub) DIAL_Z19#261
- speaker=0  style=0
- branches:
    - [flag 0xc3af in [30661..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#262
- speaker=0  style=0
- effects:
    - ?wOp12 a1=67 a2=0
    - ?wOp12 a1=67 a2=0
    - ?wOp12 a1=67 a2=0
    - ?wOp12 a1=67 a2=0
    - play sfx 38
- text: 敲了第四次門後，那老人才應了門。  「你們把俺的鐵顎陷阱帶來了嗎？」他滿懷希望地問道。  @4搖了搖頭，「我們是來跟你聊聊的。」  「俺不想ñ聊天ð，」他嗚咽著說道。「俺累得很，累得很。俺只想睡覺。俺的陷阱在東邊幾維爾格外的一個沒上鎖的箱子裡。找到了再回來，俺們再聊。」他隨即消失進了屋內，關上了門。

### (sub) DIAL_Z19#263
- speaker=0  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 38
- branches:
    - [flag 0x0100 in [30910..1]] -> node 4294901761
    - [flag 0x0101 in [60310..0]] -> node 4294901761
- text: @4敲了敲門，等著回應。  將近一分鐘後，門打開了一條縫，一隻佈滿老繭的手完成了這個動作。「你們把俺的鐵顎陷阱帶來了嗎？」門口那老人問道。

### (sub) DIAL_Z19#264
- speaker=0  style=0
- effects:
    - SET flag 0x1a33=1
    - SET flag 0x1a34=1
    - event_bitmap_hi[27] bitop
    - REMOVE item '_' cond=0
    - GIVE item 'X' cond=10 to member#6 (cost 0)
- text: @4點了點頭。  「帶來了，」他說著，取出了那個陷阱。  「兩位先生，願神保佑你們，」那男人喘著氣說道。「俺自己是沒力氣去把它拿回來的。要是沒了它，俺肯定會活活餓死的。」  拿著陷阱，那男人回到了屋裡。片刻後他又出來了，拳頭裡緊緊攥著什麼東西。「這個給你們。」  他把一枚金戒指丟進了@4攤開的手掌心，隨後便悄悄溜回屋裡，關上了門。

## node 1900058  (DIAL_Z19#265)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[27] (xor=0xd0 mask=0x7a mode=1 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[27] (xor=0xe3 mask=0x7a mode=1 chapters=-)] -> node 50397184
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#266
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#267
- speaker=0  style=0
- effects:
    - END conversation, result=65535
- text: 這間酒館鎖得死死的。  @4把鼻子貼在店面玻璃上，雙手撐在臉的兩側擋住反光，這時@0開口說道：「這塊小招牌上寫著，這地方叫『笛與月桂』。」  @4從窗邊退開。「看起來沒有荒廢，但確實是一個人也沒有。」

### (sub) DIAL_Z19#268
- speaker=0  style=6
- effects:
    - SET flag 0x0007=1
    - END conversation, result=65535
- text: 這間酒館鎖得死死的。  「招牌上寫著，這地方叫『笛與月桂』，」@4說道。  一個身穿深色衣服的男人忽然出現在他們身後。「笛與月桂早就ñ關門了ð，」他嘶聲說道。「自從賽瑟儂被毀之後就一直關著。要是你們是想找點吃的，東南邊有不錯的獵場。」  他們還沒來得及再問什麼，那男人便已悄然離去。

## node 1900059  (DIAL_Z19#269)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[27] (xor=0x0b mask=0x7e mode=1 chapters=-)] -> node 4278288384

### (sub) DIAL_Z19#270
- speaker=0  style=0
- effects:
    - play sfx 12
- branches:
    - [always] -> node 0 (no jump)
- text: @3踉蹌了一下。  一陣噁心感席捲全身，他單膝跪地。頭仍暈眩不已，他緩緩爬起身，轉向其他人……

### (sub) DIAL_Z19#271
- speaker=243  style=0
- branches:
    - [flag 0xdbd3 in [32759..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 「這地方……有種說不出的詭異。有那麼一瞬間，我感覺像是有股……強大的力量從地底竄了上來，正在吸乾我的力氣。」

## node 1900060  (DIAL_Z19#274)
- speaker=0  style=0
- effects:
    - event_bitmap_hi[27] bitop
    - play sfx 12
    - DAMAGE Health+Stamina of party by -2048
    - apply status/condition to party idx=0 amt=4

## node 1900103  (DIAL_Z19#275)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[27] (xor=0x0d mask=0x81 mode=1 chapters=-)] -> node 4278264352
    - [event_bitmap_hi[27] (xor=0xf5 mask=0x85 mode=1 chapters=-)] -> node 4278272000
    - [event_bitmap_hi[27] (xor=0xfa mask=0x80 mode=1 chapters=-)] -> node 4278256130

### (sub) DIAL_Z19#276
- speaker=0  style=0
- effects:
    - event_bitmap_hi[27] bitop

### (sub) DIAL_Z19#277
- speaker=0  style=0
- effects:
    - event_bitmap_hi[27] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#278
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 這個謎團讓他很是煩心。  雖然他們已經活著逃了出來，但潘塔西亞人出現在這一帶這件事，依然讓他耿耿於懷。他向來對這群蛇人一族沒什麼好感，而他們竟然出現在王國境內、離賽瑟儂的戰場如此之近，這讓@5心裡十分不安。

### (sub) DIAL_Z19#279
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你覺得潘塔西亞人到底在打什麼主意，@3？你覺得他們是在到處翻找什麼東西嗎？」

### (sub) DIAL_Z19#280
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「潘塔西亞人的事，誰說得準？王國裡沒人真正清楚他們想要什麼，但幾乎每件不得善終的事，多少都能扯上他們。我猜，他們是想把偷來的力量引導到別的東西上。也許是為了某個法術需要力量。」

### (sub) DIAL_Z19#281
- speaker=245  style=0
- branches:
    - [event_bitmap_hi[27] (xor=0x75 mask=0x85 mode=1 chapters=-)] -> node 4278259728
    - [always] -> node 0 (no jump)
- text: 「一想到這個我就渾身不自在。我們進入這一帶時，我確實感受到了他們的力量，只是當時不知道自己感受到的是什麼。」

### (sub) DIAL_Z19#282
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「至少我們毫髮無傷地離開了那裡。我猜克雷格是沒救了。還好我們沒像他那樣在那裡待上一整個月。」

### (sub) DIAL_Z19#283
- speaker=244  style=0
- effects:
    - apply status/condition to party idx=4 amt=44
- text: 「這個嘛，我不知道你們怎麼樣，但我感覺自己幾乎快恢復正常了。我個人是很高興這整件事終於結束了。」

### (sub) DIAL_Z19#284
- speaker=0  style=0
- effects:
    - SET flag 0xdbd5=0
- branches:
    - [event_bitmap_hi[27] (xor=0x33 mask=0x87 mode=1 chapters=-)] -> node 4278259728
    - [always] -> node 0 (no jump)
- text: @4奮力前行。  這片地面本該很適合趕路，但ñ他覺得，要走出這片海灣，反倒比進來時還要吃力得多。

## node 1900061  (DIAL_Z19#287)
- speaker=0  style=0
- branches:
    - [flag 0xc3b5 in [35266..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#289
- speaker=0  style=0  flags=paged-text
- branches:
    - [flag 0x011e in [35557..1]] -> node 4294901761
    - [flag 0x010a in [0..0]] -> node 4294901761
- text: @4手裡握著那件瓦阿尼。  「我向伊夏神祈禱，這件木製法器能派上用場，」他說。「一想到王國的命運竟繫於這麼一個小小的實驗上，我就不太願意細想，但我怕事實正是如此。」他深吸一口氣，「好吧……我們要不要試試看？」

### (sub) DIAL_Z19#290
- speaker=0  style=0
- effects:
    - REMOVE item 'e' cond=0
    - SET flag 0x1f96=1
    - SET flag 0x7541=1
- text: 那件瓦阿尼在空中劃出一道優美的弧線。  @4用力一吼，差點被投擲的力道帶得摔倒。他抬頭一看，正好瞥見那件奇特的木製物體穿過了那兩根柱頂鑲著水晶的柱子之間。  瓦阿尼始終沒有落地。  強大的閃電般轟擊從兩根水晶柱中猛然噴射而出，把它撕裂成千萬顆微小的光之螢火，緩緩飄落到滿是塵埃的林地上，冷冷地死去。地面震動起來，他們還來不及發出一聲驚呼，一陣不祥的嗡鳴便朝他們滾滾襲來。那嗡鳴隨著每一圈迴旋不斷增強，最終如重錘般擊向他們，一股轟然作響的能量與聲浪把他們掀翻在地。  他們仍暈眩未定...

## node 1900062  (DIAL_Z19#291)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[28] (xor=0xb9 mask=0x95 mode=1 chapters=-)] -> node 4278259712
    - [flag 0x1974 in [37560..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#292
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x011c in [37222..1]] -> node 4294901761
    - [flag 0x0103 in [36958..1]] -> node 4294901761
- text: 這座橋樑戒備森嚴。  幾隻哥布林狐疑地打量著漸漸靠近的他們。  「迪勒肯派我們來協助看守裂界機，」@4扯著嗓子粗聲喊道。  其中一隻哥布林轉向其他同伴，@4似乎聽見了「奎格傭兵」這幾個字，緊接著響起一陣笑聲，但很快就跟起頭時一樣迅速平息下來。「口令是什麼？」一隻哥布林質問道。

### (sub) DIAL_Z19#294
- speaker=0  style=6
- effects:
    - event_bitmap_hi[28] bitop
    - ACTION: request hotspot activation at player
- text: @4神情自信滿滿。  「迪勒肯親自給了我們一個特別的口令，」他說。「希望你們熟悉這個口令。要是不熟，我可不想落到你們的下場。新的口令是『賽瑟儂』。」  那哥布林想了片刻，接著喊道：「說謊的人今天可要倒大楣了！準備受死吧，王國的走狗！」

### (sub) DIAL_Z19#295
- speaker=0  style=6
- effects:
    - event_bitmap_hi[28] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: 這座橋樑戒備森嚴。  幾隻哥布林狐疑地打量著漸漸靠近的他們。  「迪勒肯派我們來協助看守裂界機，」@4扯著嗓子粗聲喊道。  其中一隻哥布林轉向其他同伴，@4似乎聽見了「奎格傭兵」這幾個字，緊接著響起一陣笑聲，但很快就跟起頭時一樣迅速平息下來。「口令是什麼？」一隻哥布林質問道。  @4站了出來。  他胃裡一陣翻攪，拚命回想著他們在精靈寶箱裡找到的那張紙條上寫的內容……

### (sub) DIAL_Z19#296
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「或許用我這把武器的劍刃，狠狠敲你的腦袋一下，能幫你想起來。」

### (sub) DIAL_Z19#297
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「以納拉布之血起誓！」

### (sub) DIAL_Z19#299
- speaker=0  style=6
- effects:
    - event_bitmap_hi[28] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: 這座橋樑戒備森嚴。  幾隻哥布林狐疑地打量著漸漸靠近的他們，注意力在他們與附近另一群心不在焉地互相打鬥的哥布林之間來回切換。  「迪勒肯派我們來看守這台機器，」@4扯著嗓子粗聲喊道，想起自己扮演的是個腦子不太靈光的傭兵角色。其中一隻哥布林轉向其他同伴，啐了一句什麼，@4猜大概是「奎格傭兵」的意思。哥布林隊伍裡頓時爆出一陣笑聲，隨後也跟起頭時一樣迅速平息，這時首領開口要求對口令……

### (sub) DIAL_Z19#300
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「口令跟上次一樣。以納拉布之血起誓。」

## node 1900063  (DIAL_Z19#302)
- speaker=0  style=0
- branches:
    - [flag 0x7539 in [20113..32815]] -> node 4294901761
    - [flag 0x1fb8 in [20139..32815]] -> node 4294901761
    - [flag 0x7537 in [39107..1]] -> node 458759
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#303
- speaker=0  style=6
- effects:
    - SET flag 0x1fb8=1
    - ?wOp12 a1=34 a2=0
    - ?wOp12 a1=34 a2=0
    - ?wOp12 a1=34 a2=0
    - (on-exit) play sfx 39
- text: 一個滿臉驚恐的男人應了門。  越過那男人望向敞開的房間，@4看見他已經打包了好幾個包袱，彷彿正準備離開。  「俺現在沒空聊，」那男人說道。「俺要走了，俺也勸你們趕緊走。哥布林跟莫瑞德人都搬進來了……俺是時候搬出去了！」  「你在哪裡看到他們的？」@0追問道。  那男人正手忙腳亂地想把一件棉衫塞進大袋子裡，回答道：「他們是往西北方去的……朝著那個女巫薇琳蒂的小屋去了。要是那個老巫婆跟這事脫不了關係，俺一點都不意外。現在你們真的得讓俺收拾行李了。日安。」

## node 1900100  (DIAL_Z19#304)
- speaker=0  style=0
- branches:
    - [flag 0x1eae in [0..0]] -> node 0 (no jump)
    - [flag 0x1fb9 in [0..0]] -> node 4294901761
    - [flag 0x196e in [40288..1]] -> node 4294901761
    - [flag 0x1fae in [0..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#305
- speaker=0  style=6
- effects:
    - SET flag 0x1fae=1
- text: 他們搜遍了整個箱子。  「不在這裡，」@4驚呼道。「這確實是莫羅爾夫跟我們提過的那個箱子，但瓦阿尼不在裡面！我們現在該怎麼找到它？」  「多半是被騙了，」派特魯斯啐了一口。「別指望莫瑞德人會說實話，就算他跟你說怎麼親他的屁股，那也是假的！」  「我倒不這麼認為，」@4回答道。「或許這裡還有ó別的東西，能告訴我們瓦阿尼到底發生了什麼事……」

### (sub) DIAL_Z19#306
- speaker=0  style=6
- effects:
    - SET flag 0x1fb9=1
- text: 「我不知道這個叫菲力普的傢伙在打什麼鬼主意，但我打算查個清楚，」@4說道。「聽起來簡直像是他故意想ó引誘發現這張紙條的人往北到他家去。」

## node 1900109  (DIAL_Z19#307)
- speaker=0  style=0
- branches:
    - [flag 0x1fc0 in [40516..1]] -> node 0 (no jump)

### (sub) DIAL_Z19#308
- speaker=0  style=0
- effects:
    - SET flag 0x1fc0=1
- branches:
    - [always] -> node 0 (no jump)
- text: @3的臉色開始發白。  @4對於把這位法術顧問一路拖著參與這趟漫長的任務，心裡多少有點過意不去，但由於他對魔法一竅不通，亞魯莎親王還是認為，至少該讓他來看看這台外星裝置。誰也沒料到的是，他們這趟旅程有很大一部分得ó靠雙腳走完。  一連好幾天，他們騎著從北衛城馬廄借來的三匹上等駿馬，以驚慌失措的速度狂奔。這幾匹馬被逼得太狠、跑得太久，結果一匹接一匹相繼倒斃，甚至還沒抵達幽暗林的外緣就已經斷氣。從那時起，他們只能徒步前行，還得悄悄避開一支正在幽暗林北側出口道路上佈防的哥布林巡邏隊...

### (sub) DIAL_Z19#309
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「所以……也沒什麼ó大不了的事要辦嘛。就是在整片幽暗林裡，找出一個人大小的東西而已。應該不會太難的。」

### (sub) DIAL_Z19#310
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這還不是亞魯莎交代過我們最ó困難的事。還記得裂界之戰後我們去找的那批漿果嗎？要不是我們想起那年雨水比較多，差點就找不到了。真是可惜，這一趟還得拖著可憐的老派特魯斯一起來。」

### (sub) DIAL_Z19#311
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你們兩個小毛頭還是先操心自己的小命吧。俺自認跑得比你們這些小夥子都快，你們可比不上俺。誰敢在俺面前擺架子，俺就敲爛你們兩個的腦袋。」

### (sub) DIAL_Z19#312
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你最好聽他的話，吉米。他可是個殺手。」

### (sub) DIAL_Z19#313
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「嗯哼。我相信你說得對。那，你覺得我們該從哪裡開始找這台裂界機？你猜的跟我猜的差不多準。」

### (sub) DIAL_Z19#314
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「既然我們剛從北邊過來，我敢說它大概不會在那個方向。那就還剩東、西、南邊，還有中間各個方向了。簡直像是在木桶裡叉魚一樣容易。」

### (sub) DIAL_Z19#315
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「既然如此，我看我們就儘量有系統地找吧。我看我們先往東搜一輪，再看看要不要轉往南邊或西邊。」

### (sub) DIAL_Z19#316
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「東邊？為什麼？西邊感覺也一樣有機會啊。」

### (sub) DIAL_Z19#317
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「說不上來。但告訴我該往東走的這股直覺，正是一直讓我活到現在的同一股直覺，我學會了不要輕易忽視它。要是你有更好的主意，我就聽你的……」

## node 1900064  (DIAL_Z19#319)
- speaker=0  style=6
- text: @4停下了腳步。  他望向前方守在關口的那群人，出聲喊道：「你們願意讓我們安全通過嗎？」  對方很快便給出了回應，語氣中透著十足的權威：「奉亞魯薩親王之命，我們禁止你們再往前一步。」  @4用手圈成喇叭狀，湊在嘴邊喊了回去：「我們是奉王國官方之命辦事，你們必須讓我們通過。」  「我們接獲的命令十分嚴格，不得放任何人再往北邊去，」對方如此回應道。  @0走上前來，站到了@4身旁。「我們該怎麼辦？」  「我們人數差太多了，還是該撤退才對。」

## node 1900073  (DIAL_Z19#320)
- speaker=0  style=0
- branches:
    - [flag 0x1fbe in [43547..1]] -> node 0 (no jump)

### (sub) DIAL_Z19#321
- speaker=0  style=0
- effects:
    - SET flag 0x1fbe=1
- branches:
    - [always] -> node 0 (no jump)
- text: @3清了清嗓子。  他引起了@5的注意，接著便打住了……

### (sub) DIAL_Z19#322
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「莫瑞德人怎麼會派斥候到幽暗林來？目的又是什麼？」

## node 1900104  (DIAL_Z19#324)
- speaker=0  style=6  flags=paged-text
- branches:
    - [flag 0x011a in [44944..1]] -> node 4294901761
    - [flag 0x0103 in [45662..1]] -> node 4294901761
- text: @4停下了腳步。  他望向擋在前方隘口的那隊守衛，喊道：「你們願意放我們安全通過嗎？」  一名神情自負的守衛從手邊的事情中抬起頭，帶著十足的輕蔑打量了他們一番，回答道：「我們接到命令，任何人都不准進出幽暗林。」  「誰下的命令？」@4質問道。  「一開始是誰下的令，我確實不清楚，但既然是我的指揮官下的命令，我就得服從，」他回答道，一邊把劍拔出、劍尖插進面前的土裡，一邊帶著威嚇的眼神盯著他們。「當然，要是你們想找碴，質疑這道命令是否明智，我們隨時奉陪。」  @5上前一步，站到@...

### (sub) DIAL_Z19#325
- speaker=0  style=6
- effects:
    - SET flag 0x1fba=1
    - ACTION: request hotspot activation at player
- text: @5走到了首領面前。  「我們會把你們一路踢回北境去，」他吹噓道。  @4立刻上前跟@5商量。「你是不是把你那點僅有的理智也弄丟了？你是想害我們ñ送命ð嗎？」他問道。「再說了，這條路正把我們帶得ñ離我們要摧毀的那台裂界機越來越遠。」  「ñ相信我，」@5向他保證道。「我覺得我們能打贏他們。」  就在他們準備應戰時，那名哥布林守衛朝隘口裡藏著的其他同伴喊了一聲。@5看見一批戰士從樹叢後現身，不禁打了個寒顫，這才意識到這條隘口ñ確實被封鎖了。「ñ轉念一想，或許你ñ不該相信我，」他...

## node 1900101  (DIAL_Z19#327)
- speaker=0  style=0
- branches:
    - [flag 0x1f72 in [45920..1]] -> node 4294901761
    - [flag 0x1fb2 in [46861..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#328
- speaker=3  style=0
- effects:
    - SET flag 0x1f72=0
    - SET flag 0x1fb2=0
    - ?wOp12 a1=12 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我開始覺得……有點ó怪。我真想就地躺下、打個盹……」

### (sub) DIAL_Z19#330
- speaker=0  style=6
- effects:
    - SET flag 0x1fb2=1
    - play sfx 12
    - advance in-game time by 55800
- text: @4忽然覺得睏意襲來。  睡意排山倒海而來，將他徹底吞沒。他轉身想喊出警告，但話還沒出口，眼前便已一片漆黑。  噩夢般的畫面接連折磨著他，像烈焰竄過浸滿煤油的破布般，在他腦海中肆意奔流。  等他隔天醒來時，才意識到自己的生命裡竟憑空消失了一整天。他甩了甩四肢的麻木感，看見@0也正做著同樣的動作。他拾起背包，準備繼續上路。

### (sub) DIAL_Z19#331
- speaker=0  style=0
- effects:
    - advance in-game time by 55800
- branches:
    - [flag 0xcf0c in [46890..1]] -> node 65537

### (sub) DIAL_Z19#332
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=13)
    - play sfx 12
- text: @0再次覺得睏意襲來。  睡意又一次很快地籠罩了他……

## node 1900066  (DIAL_Z19#333)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯示意歐文靠過來。  他先是凝視著遠方，接著又轉頭望向另一邊，這位莫瑞德人終於開口了……

## node 1900067  (DIAL_Z19#335)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[29] (xor=0x0e mask=0xc4 mode=1 chapters=-)] -> node 4278256640
    - [flag 0x1fb3 in [47367..1]] -> node 0 (no jump)
    - [flag 0xc359 in [48735..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#336
- speaker=0  style=0
- effects:
    - SET flag 0x1fb3=1
- branches:
    - [always] -> node 0 (no jump)
- text: 那頭露莎卡正試圖與他們交流。  她用一種奇怪、卻不知怎地能聽懂的語言，向他們開口說話……

### (sub) DIAL_Z19#337
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「不必怕我……我看得出你們的心是真誠的，因此我不會傷害你們。」

### (sub) DIAL_Z19#338
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你怎麼會知道我們的這些事？」

### (sub) DIAL_Z19#339
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我知道的事ñ多著呢。你們是在執行一項使命，是不是？」

### (sub) DIAL_Z19#340
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「是的，沒錯。你能幫我們嗎？」

### (sub) DIAL_Z19#342
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那頭露莎卡正試圖與他們交流。  她用一種奇怪、卻不知怎地能聽懂的語言，向他們開口說話……

### (sub) DIAL_Z19#343
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你們回來了……你們找到我們說過的那件寶物了嗎？」

### (sub) DIAL_Z19#344
- speaker=254  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們還沒找到你派我們去找的那位莫瑞德人法師……」

### (sub) DIAL_Z19#345
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「往西走，在兩水交會之處。你們會在他身邊找到幾個被他意志所束縛的我的族人。務必小心他們，因為他們會像對待天生的敵人一樣，跟你們拚死一戰。」

### (sub) DIAL_Z19#347
- speaker=200  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [48859..1]] -> node 4294901761
    - [flag 0x0101 in [50048..1]] -> node 4294901761
- text: @4站到了露莎卡面前。  「你們把伊萊安之心帶回來了嗎？」那生物問道。

### (sub) DIAL_Z19#348
- speaker=0  style=6
- effects:
    - event_bitmap_hi[29] bitop
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item 'H' cond=14 to party (cost 0)
    - GIVE item '\x10' cond=0 to member#6 (cost 0)
    - REMOVE item '\t' cond=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4點了點頭。  他取出那顆心，忐忑不安地走向露莎卡。他的雙手微微顫抖，把那件物品放在那生物面前，隨即迅速退開了幾步。  「你完成了我的請求，如今也該獲得回報了，」她說著，變出了十幾份口糧。「此外，這條河的岸邊多年前還留下了一樣東西，將來的路上會對你們有所幫助。請收下，這是我全族對你們的謝意。」

### (sub) DIAL_Z19#349
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這只貝殼很珍貴嗎？」

### (sub) DIAL_Z19#350
- speaker=200  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「它的用途，遠比你所能想像的還要多。雖然對你們正在尋找的東西幫助不大，但你們或許還會從中找到另一樣自己渴望的東西。」

### (sub) DIAL_Z19#351
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「艾爾凡達的事呢？去那裡最好走哪條路？」

## node 1900108  (DIAL_Z19#355)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[29] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278259712
    - [flag 0x1fb3 in [50413..1]] -> node 0 (no jump)

### (sub) DIAL_Z19#356
- speaker=0  style=6
- effects:
    - event_bitmap_hi[29] bitop
    - ?wOp12 a1=90 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: @5示意大家安靜。  雖然距離他當年領著族人逃離綠心林、穿越伊列德森林邊緣已經過了好些年頭，但眼前的景象與氣味，對他來說依然熟悉得就像自己指尖的紋路一樣。然而，他們此刻所站的這片區域，卻透著一股ó不自然的氣息……

### (sub) DIAL_Z19#357
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「附近有東西在移動，但那既不是我們的同族，也不是我所熟悉的任何一種林間動物的動靜聲。」

### (sub) DIAL_Z19#358
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我ó好像聽見了什麼——一種尖銳的嗡鳴聲。是從南邊傳來的嗎？」

### (sub) DIAL_Z19#359
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「是同樣的聲音。要是能查清楚它的來源，或許對我們有好處。」

### (sub) DIAL_Z19#360
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「要是那東西把我們當成晚餐怎麼辦？」

### (sub) DIAL_Z19#361
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「要是它真想傷害我們，與其等它自己ñ挑時機出手，把我們吃掉，倒不如我們先摸清楚是什麼東西在跟蹤我們，搶得先機，你說是不是？這事就交給你決定了。」

## node 1900111  (DIAL_Z19#363)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[29] (xor=0x00 mask=0x00 mode=0 chapters=-)] -> node 4278259712
    - [flag 0x1fb3 in [51443..1]] -> node 0 (no jump)

### (sub) DIAL_Z19#364
- speaker=0  style=6
- effects:
    - event_bitmap_hi[29] bitop
    - ?wOp12 a1=90 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: @5示意大家安靜。  雖然距離他當年領著族人逃離綠心林、穿越伊列德森林邊緣已經過了好些年頭，但眼前的景象與氣味，對他來說依然熟悉得就像自己指尖的紋路一樣。然而，他們此刻所站的這片區域，卻透著一股ó不自然的氣息……

### (sub) DIAL_Z19#365
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「附近有東西在移動，但那既不是我們的同族，也不是我所熟悉的任何一種林間動物的動靜聲。」

### (sub) DIAL_Z19#366
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我ó好像聽見了什麼——一種尖銳的嗡鳴聲。是從北邊傳來的嗎？」

### (sub) DIAL_Z19#367
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「是同樣的聲音。要是能查清楚它的來源，或許對我們有好處。」

### (sub) DIAL_Z19#368
- speaker=243  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「要是那東西把我們當成晚餐怎麼辦？

### (sub) DIAL_Z19#369
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 如果它真想傷害我們，與其等它自己ñ挑時機出手，把我們吃掉，倒不如我們先摸清楚是什麼東西在跟蹤我們，搶得先機，你說是不是？這事就交給你決定了。」

## node 1900068  (DIAL_Z19#371)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[30] (xor=0x7b mask=0xd0 mode=1 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#372
- speaker=0  style=0
- effects:
    - DAMAGE Strength of party by -768
    - play sfx 21
- branches:
    - [flag 0xc38f in [52825..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這扇門鎖住了。  「跪下！」一個威嚴的聲音喝道，那聲音彷彿震盪著房間的每一面牆壁、每一個角落。一股強大的力量猛地擊向戈拉斯，像被大鎚重擊一般，把他打倒在地。  「把線之鑰帶來給我，」一個聲音下令道。隨後便陷入了沉默。  他們悄悄地退開了。

### (sub) DIAL_Z19#373
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「看來我們手上沒有需要的那把鑰匙。這片ñ森林裡，我們到底要去哪裡找對的那一把？」

### (sub) DIAL_Z19#374
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「它會由一位掌權者持有，因為這裡是ñ古老力量匯聚之地。我實在難以想像，格拉姆瑞德人這樣的聖地，會任由任何人隨意闖入尋找。就我所知，全天下大概只有三個人有辦法進入這個地方，而亞葛拉蘭娜王后與戰帥托馬斯，都在我們此行的ñ終點才會遇上。所以，我們唯一的希望，就是找到凱林親王。或許他會知道答案。」

### (sub) DIAL_Z19#375
- speaker=0  style=0
- effects:
    - END conversation, result=65535

### (sub) DIAL_Z19#376
- speaker=0  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=5 a2=0
    - play sfx 38
- branches:
    - [flag 0x0100 in [53622..1]] -> node 4294901761
    - [flag 0x0101 in [0..0]] -> node 4294901761
- text: @4用了那把鑰匙。  他們推開了那扇鉸鏈鏽蝕、木板已裂的門，望進了通往這座古老廢墟的幽暗豎坑。轉向@5，@4聳了聳肩。「那，我們要進去嗎？」

### (sub) DIAL_Z19#377
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[30] (xor=0x56 mask=0xd2 mode=1 chapters=-)] -> node 4278256644
- text: 這扇門開著。  他們進入了洞穴，@4注意到臉上感受到的空氣有多麼涼爽。他真希望自己穿得更厚一點，或者皮膚能再厚實一些，一邊搓著手肘，一邊往這座廢墟深處走去。

### (sub) DIAL_Z19#378
- speaker=0  style=0
- effects:
    - event_bitmap_hi[30] bitop
    - RAISE Strength of party by 1536
    - play sfx 63

## node 1900095  (DIAL_Z19#379)
- speaker=0  style=0
- effects:
    - DAMAGE Health+Stamina of party by -256

## node 1900069  (DIAL_Z19#380)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[31] (xor=0xe5 mask=0x05 mode=2 chapters=-)] -> node 1536
    - [flag 0xc358 in [53953..1]] -> node 4294901761
    - [flag 0x1fa3 in [457..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#381
- speaker=0  style=0
- branches:
    - [flag 0x1fa3 in [57170..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#382
- speaker=0  style=6
- effects:
    - event_bitmap_hi[31] bitop
    - SET flag 0x1fa3=1
- text: @4遲疑了一下。  在那地獄般酷熱、閃爍著奇異光芒的空氣中，那顆被烈日曬得溫熱的水晶柱，摸上去恐怕會燙傷人，但他還是很好奇，這根玻璃般的石柱究竟是用什麼材質做成的。他心裡暗自納悶，會不會是他們在沙漠平原上遇見過的那些蛇人一族，跟這些謎樣的巨石陣有關，但不知怎地，這個念頭讓他覺得ñ不對勁……  ã不ã。ã卡ã爾ã贊ã眾ã柱ã，ã從ã來ã就ã並ã非ã由ã潘ã納ã斯ã提ã安ã登ã所ã打ã造ã，ã它ã們ã的ã源ã頭ã另ã有ã所ã自ã，ã遠ã比ã你ã所ã能ã想ã像ã的ã，ã還ã要ã更ã...

### (sub) DIAL_Z19#383
- speaker=0  style=6
- effects:
    - event_bitmap_hi[31] bitop
- text: @4觸碰了達沙梵的石柱。  感受到體內那股熟悉的存在微微騷動，他耐心等候著，靜候那個存在回應他心中的呼喚。  ã你ã們ã終ã於ã帶ã著ã這ã只ã聖ã杯ã回ã來ã了ã，ã那ã聲ã音ã平ã靜ã地ã緩ã緩ã說ã道ã，ã語ã氣ã中ã不ã帶ã一ã絲ã一ã毫ã的ã波ã瀾ã起ã伏ã，ã聽ã不ã出ã絲ã毫ã的ã喜ã怒ã哀ã樂ã。ã這ã很ã好ã，ã這ã正ã是ã我ã們ã所ã期ã望ã、ã所ã盼ã望ã已ã久ã的ã圓ã滿ã結ã果ã。ã如ã今ã，ã那ã些ã早ã已ã被ã自ã己ã的ã族ã人ã所ã徹ã底ã遺ã...

### (sub) DIAL_Z19#384
- speaker=0  style=6
- effects:
    - event_bitmap_hi[31] bitop
- text: @4遲疑了一下。  在那地獄般酷熱、閃爍著奇異光芒的空氣中，那顆被烈日曬得溫熱的石柱表面，摸上去恐怕會燙傷人，但他還是很好奇，這根玻璃般的石柱究竟是用什麼材質做成的。他心裡暗自納悶，會不會是他們在沙漠平原上遇見過的那些蛇人一族，跟這些謎樣的巨石陣有關，但不知怎地，這個念頭讓他覺得ñ不對勁……  ã不ã。ã卡ã爾ã贊ã眾ã柱ã，ã從ã來ã就ã並ã非ã由ã潘ã納ã斯ã提ã安ã登ã所ã打ã造ã，ã它ã們ã的ã源ã頭ã另ã有ã所ã自ã，ã遠ã比ã你ã所ã能ã想ã像ã的ã，ã還ã要ã更...

### (sub) DIAL_Z19#386
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[31] (xor=0xd8 mask=0x16 mode=2 chapters=-)] -> node 4278259712
    - [event_bitmap_hi[31] (xor=0x9c mask=0x09 mode=2 chapters=-)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#387
- speaker=0  style=6
- effects:
    - load teleport table 39
- text: @4觸碰了那根石柱。  指尖傳來一陣輕微的刺麻感，預示著這位神明的心靈即將與他自己的心靈融合為一。ã你ã們ã此ã番ã前ã來ã到ã此ã地ã，ã究ã竟ã有ã什ã麼ã樣ã的ã需ã要ã，ã儘ã管ã直ã說ã便ã是ã，ã不ã必ã拘ã束  「我們至今仍然找不到帕格，」@4說道。「他到底在哪裡？我在這個地方實在分不太清方向。」  ã以ã你ã們ã凡ã人ã衡ã量ã時ã間ã流ã逝ã的ã方ã式ã來ã說ã，ã此ã刻ã時ã日ã已ã然ã無ã多ã，ã然ã而ã要ã執ã行ã這ã麼ã一ã個ã小ã小ã的ã動ã作ã而...

### (sub) DIAL_Z19#388
- speaker=0  style=6
- effects:
    - SET flag 0x1fcd=1
- text: 帕格仔細端詳著這根石柱。  當他先前造訪卡爾贊遺址時，就曾感應到從這些石柱中散發出來的靈性，卻始終不清楚棲居其中的到底是什麼樣的存在，其真實本質為何。他向前踏出一步，微微躬身行了個禮。  「幸會了，阿爾一族的表親們，」他說道。「我很抱歉，第一次造訪時沒能認出你們的身分。萬分抱歉。直到我待在那頂帳篷裡時，神諭曾經提過的某件事，才忽然浮現在我腦海之中。」  ã對ã我ã們ã這ã些ã自ã居ã為ã凡ã人ã之ã神ã的ã存ã在ã而ã言ã，ã其ã實ã根ã本ã就ã不ã需ã要ã什ã麼ã道ã歉ã之...

## node 1900070  (DIAL_Z19#390)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[31] (xor=0xc7 mask=0x17 mode=2 chapters=-)] -> node 4278256640
    - [event_bitmap_hi[31] (xor=0xa8 mask=0x20 mode=2 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#391
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#392
- speaker=0  style=0
- branches:
    - [flag 0x1fb4 in [8221..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#393
- speaker=0  style=0
- effects:
    - SET flag 0x1fb4=1
- branches:
    - [flag 0x1fa3 in [7380..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: @4 尖叫了一聲。  他揉了揉鼻子，滿臉困惑地盯著眼前的景象。似乎有股看不見的力量，正阻擋著他們繼續向前。

### (sub) DIAL_Z19#394
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「看來我們似乎撞上了某種魔法屏障。不管裡頭的是誰，或者ó究竟是什麼東西，顯然都不希望我們進去。」

### (sub) DIAL_Z19#395
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「如果這個地方根本不能施展魔法，這怎麼可能辦得到？」

### (sub) DIAL_Z19#396
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你根本沒在聽我說的話。這不是不可能，只是非常困難而已。建造這道魔法屏障的人，手上握有龐大的魔力。」

### (sub) DIAL_Z19#397
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「或許這一切，是帕格搞出來的也說不定。」

### (sub) DIAL_Z19#398
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「帕格ó牽涉其中，這點似乎八九不離十，但我的直覺告訴我，這屏障不是他建造的。為什麼要在一頂帳篷四周設下力場屏障呢？我猜他現在最優先的事，應該是找到他女兒加米娜失蹤的地方，然後帶她回家。」

### (sub) DIAL_Z19#399
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這麼說，你懷疑這頂帳篷，其實是某種囚禁的手段？」

### (sub) DIAL_Z19#401
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#402
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「看來我們似乎撞上了某種魔法屏障。不管裡頭的是誰，或者ó究竟是什麼東西，顯然都不希望我們進去。」

### (sub) DIAL_Z19#403
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「如果這個地方根本不能施展魔法，這怎麼可能辦得到？」

### (sub) DIAL_Z19#404
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你根本沒在聽我說的話。這不是不可能，只是非常困難而已。建造這道魔法屏障的人，手上握有龐大的魔力。」

### (sub) DIAL_Z19#405
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「或許這一切，是帕格搞出來的也說不定。」

### (sub) DIAL_Z19#406
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「等等……這裡一定就是達沙梵囚禁他的地方！帕格一定就在裡面！」

### (sub) DIAL_Z19#407
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「就是你在那些石柱中聽見的那個聲音？」

### (sub) DIAL_Z19#409
- speaker=0  style=0
- effects:
    - SET flag 0x1fb4=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#411
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[3,2,1]
    - event_bitmap_hi[31] bitop
    - ACTION: SHARE Owyn<->Pug spellbooks
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#412
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帳篷裡有動靜。  一個矮小的男人推開了那扇編織方式古怪的帳篷門簾，走上前來，瞇著眼打量著他們。他的舉止大致上並不起眼，只是隨意地走上前來，彷彿在這片詭異的沙漠世界中遇見人類，根本不是什麼出乎意料的事……

### (sub) DIAL_Z19#413
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「托馬斯在哪裡？我有要事必須跟他談談。」

### (sub) DIAL_Z19#414
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「他沒辦法過來，所以派我們來找你。他把你留給他的那道法術交給了我們……」

### (sub) DIAL_Z19#415
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「沒辦法過來？為什麼？他到底出了什麼事？」

### (sub) DIAL_Z19#416
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「他在摩瑞德爾人攻擊艾爾凡達時受了傷。阿格拉蘭娜女王向我們保證，他會沒事的……」

### (sub) DIAL_Z19#417
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我實在難以相信，派你們來這裡會對馬卡拉的計畫有什麼幫助，所以眼下我只能暫且相信你們的話……看著你，我忽然覺得你這張臉似乎ó有些眼熟。你是不是幾個月前，跟洛克利爾爵士一起來到肯多的那個小法師？」

### (sub) DIAL_Z19#418
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「沒錯，你還記得戈拉斯嗎？」

### (sub) DIAL_Z19#419
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這幾個晚上，我實在很難ó忘記他那張臉。他是馬卡拉這整盤大局裡，第一個被利用的棋子……」

### (sub) DIAL_Z19#420
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你這是在指控我們是騙子和間諜嗎？」

### (sub) DIAL_Z19#421
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「戈拉斯，我並不是指控你是ó心甘情願的參與者。你對自己所扮演的角色一無所知，就跟我猜想戴勒肯對他自己的角色一樣毫不知情。當你說他在薩薩戈斯高舉起穆爾曼達莫斯的戰旗時，我確實有些警覺了起來。」  「我曾親眼目睹穆爾曼達莫斯死去，沒有理由相信他還活著，但打著他名號行事的勢力，卻在塞薩儂引發了那場浩劫，我當時猜想，這或許又是潘納斯提安族在背後搞的鬼。經過一番調查後，我發現他們ó確實插手了王國的事務，但實際上是透過一群搜尋各種魔法物品——那些小玩意兒——的魔法竊賊在行動，這跟北方大陸...

### (sub) DIAL_Z19#422
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「那麼，戈拉斯到底跟你說了什麼那麼重要的事？」

### (sub) DIAL_Z19#423
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「直到馬卡拉騙我來到這裡之後，戈拉斯向亞魯薩親王作的證詞，才顯得意義重大起來。他曾隨口提過，戴勒肯戴著一頂黑色的頭盔，形狀像條龍。穆爾曼達莫斯就曾戴過這樣一頂頭盔，而且在亞魯薩親王將他斬殺時，那頂頭盔就在他身上……不管是誰把穆爾曼達莫斯的頭盔交給戴勒肯，那個人一定曾經ó深入過塞薩儂地底的那些洞穴才行。」  「我能想到的，只有四位法師有這樣的手段，能夠潛入那裡設下的第一層防禦圈。其中一位是馬克羅斯，但既然他當初在那裡對阻止那場浩劫出了不少力，我實在難以相信他會是幕後主使。另一位...

### (sub) DIAL_Z19#424
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這樣一來，你唯一的嫌疑對象就只剩下馬卡拉了。但他為什麼要做這一切呢？他為什麼要把戴勒肯推向跟王國開戰的局面？」

### (sub) DIAL_Z19#425
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「就算他ó真有那個本事潛入那些洞穴，要達成他最終的目標——那間藏有一件威力驚人到令人難以置信的毀滅性神器的密室——他仍然需要相當程度的幫助才行，他對那件神器的執著，可是從未有一刻鬆懈過。我留下了一條龍在那裡守護著它，就連ó我自己的力量，光是跟一條那個年紀的龍正面交手一次，都得吃盡苦頭了，更別說是那條沉睡在塞薩儂地底、擁有特殊能力的龍了。一旦她察覺到異狀，她必定會召喚萊姆國王下令留守在塞薩儂周邊地區的那支祕密駐軍前來相助，而馬卡拉在第一次造訪時，肯定早就察覺到這支駐軍的存在，並...

### (sub) DIAL_Z19#426
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「但這正是亞魯薩親王派我們來找你的原因啊！他擔心戴勒肯會讓法師在北衛堡的圍城戰中出手！也許只要我們能在那裡阻止他們……」

### (sub) DIAL_Z19#427
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「很遺憾，我現在對任何人都幫不上什麼忙，更別說是亞魯薩親王了。為了盡快找到加米娜，我在盲目匆忙之下，動用了一件本該置之不理的魔法神器……」

### (sub) DIAL_Z19#428
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這件事，我們多少已經知道一些了。你之前說過，你不得不相信我們，所以現在換我告訴你，我想我能幫得上忙，你也得相信我才行。看在我們大家的份上，我真心希望自己這次沒有想錯……」

### (sub) DIAL_Z19#429
- speaker=0  style=6
- effects:
    - advance in-game time by 21600
    - (on-exit) play sfx 63
- branches:
    - [always] -> node 0 (no jump)
- text: 帕格顫抖著舉起那只鑲滿寶石的倫恩斯克爾之杯，感覺到一股力量在這件鑲滿寶石的神器之中迸發流竄。他的意識如漣漪般不斷向外擴散，觸及了同行夥伴們的心靈，感受到了敬畏、困惑、恐懼、痛楚，以及ñ知識ð……  毫無預警之間，歐文的心靈與帕格的心靈猛然相連，兩人都被這股親密無間的接觸震懾得暈頭轉向。á把á你á所á知á道á的á那á一á切á法á術á與á各á種á奧á術á方á面á的á所á有á知á識á，á統á統á都á要á好á好á地á集á中á精á神á，á仔á細á專á注á起á來á。 帕格在心中想著。á我...

## node 1900083  (DIAL_Z19#432)
- speaker=0  style=0
- branches:
    - [flag 0x1fa4 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#433
- speaker=0  style=6
- effects:
    - SET flag 0x1fa4=1
    - RAISE Assessment of party by 3840
- text: 石柱觸摸起來十分光滑。  這根石柱聳立在@3面前，看起來似乎是由某種極為精緻的水晶所打造而成，只是這種水晶，跟他在米德凱米亞見過的任何東西都截然不同。透過它，他能看見遠處沙漠折射出來的種種景象，但當他微微轉動頭部、變換視角時，卻似乎能看見另一些ó並不在石柱另一側的地方。相反地，他看見的，彷彿是其他色彩的海洋與天空的景象……  ã凡ã人ã啊ã，ã你ã方ã才ã所ã說ã的ã這ã些ã觀ã察ã與ã見ã解ã，ã倒ã是ã引ã起ã了ã我ã幾ã分ã興ã致ã與ã好ã奇ã之ã心ã呢ã。ã你ã，ã應...

## node 1900084  (DIAL_Z19#434)
- speaker=0  style=0
- branches:
    - [flag 0x1fa5 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#435
- speaker=0  style=6
- effects:
    - SET flag 0x1fa5=1
    - RAISE Strength of party by 2560
- text: 一股能量從石柱中爆發而出。  @3頭暈目眩，從他跌倒的沙地上爬了起來，伸手讓戈拉斯把他拉了起來。「剛才，裡頭好像有種……ó存在感ð……在石柱裡面。當我碰到它的時候，我感覺自己好像想要把這世界上每一個潘納斯提安登都殺光……甚至覺得自己ó光憑赤手空拳，就能把他們統統掐死，接著，那種感覺就消失了。」  「你會這麼說還真是奇怪，因為我自己也忽然覺得渾身是勁。不過，這些潘納斯提安登到底是什麼？」@5回應道。「這個詞我完全沒聽過。」  「就是我們遇到的那些蛇人。我也不知道自己為什麼會知道...

## node 1900085  (DIAL_Z19#436)
- speaker=0  style=0
- branches:
    - [flag 0x1fa6 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#437
- speaker=0  style=6
- effects:
    - SET flag 0x1fa6=1
- text: 這根石柱有些不太對勁。  @4收回了手，努力想要找出恰當的字眼，來形容自己的感受。「你知道那種感覺嗎？就是有人站在你背後，你明明沒聽見他們靠近的聲音，卻還是能感覺到他們就站在那裡的那種感覺？」  戈拉斯微微一笑，聳了聳肩。「這種感覺我倒是聽說過，不過恐怕在我們族人之中，這幾乎是聞所未聞的體驗。」他伸手扯了扯自己的一隻耳朵。「幾乎沒什麼事，能逃得過我們的聽覺。」  「喔。」歐文低頭看著地面，忽然臉紅了起來，這才意識到自己對戈拉斯和他的族人，其實了解得少之又少。總有一天，他一定要...

## node 1900086  (DIAL_Z19#438)
- speaker=0  style=0
- branches:
    - [flag 0x1fa7 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#439
- speaker=0  style=6
- effects:
    - SET flag 0x1fa7=1
    - RAISE Defense of party by 2560
- text: 石柱散發著溫暖的熱度。  @4起初以為，這是水晶反射了那顆異界太陽的光線，才會散發出熱度，但即使是在背光的那一側，這根石柱似乎依然同樣溫暖。  ã「ã我ã或ã許ã還ã能ã夠ã為ã你ã稍ã微ã做ã點ã什ã麼ã，ã就ã只ã這ã麼ã一ã點ã點ã小ã事ã罷ã了ã，ã」ã一ã個ã溫ã柔ã輕ã柔ã的ã女ã性ã聲ã音ã，ã在ã他ã的ã心ã中ã悄ã悄ã地ã、ã輕ã聲ã細ã語ã地ã開ã口ã問ã道ã。ã「ã也ã就ã僅ã僅ã只ã是ã止ã於ã此ã而ã已ã，ã實ã在ã不ã能ã再ã多ã了ã，ã一ã丁ã點...

## node 1900087  (DIAL_Z19#440)
- speaker=0  style=0
- branches:
    - [flag 0x1fa8 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#441
- speaker=0  style=6
- effects:
    - SET flag 0x1fa8=1
- text: 這根石柱是由水晶打造而成的。  相較於這圈石柱裡的其他幾根，它的狀況要好上許多，反射光滑的表面，也不像其他石柱那樣，被風沙侵蝕得坑坑洞洞的。@4輕輕撫摸著它的表面，不禁對工匠們所投注的心血與工夫，感到嘖嘖稱奇。  「不知道這個地方，原本究竟是做什麼用的，」@4隨口問道，並沒有料到，一陣心靈上的回應，竟會如潮水般湧入他的感官之中。  ã凡ã人ã啊ã，ã你ã如ã今ã，ã正ã身ã處ã卡ã爾ã贊ã莫ã克ã的ã殘ã垣ã廢ã墟ã之ã中ã，ã此ã地ã，ã曾ã經ã是ã提ã米ã里ã安ã雅ã七ã...

## node 1900088  (DIAL_Z19#442)
- speaker=0  style=0
- branches:
    - [flag 0x1fa9 in [14253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#443
- speaker=0  style=6
- effects:
    - play sfx 12
    - DAMAGE Health+Stamina of party by -3840..-2048
- text: 這塊水晶冰冷刺骨。  在酷熱難耐的沙漠之中，這件物品竟然透著這股違反常理的寒意，讓@4深感不安，於是他退開了幾步，同時察覺自己忽然感到十分不舒服，也注意到@5看起來同樣一臉困擾。  「我們別再碰那件神器了，」@5訓斥道。「我對那根石柱有種非常不好的預感。」

## node 1900091  (DIAL_Z19#444)
- speaker=0  style=0  flags=reload-scr-between-pages
- text: 門猛然被撞開了。  從裡頭湧出的那些生物，排成了一種奇特的陣形，彷彿正拚命想要保護這座古怪小屋裡的某樣東西。@3一時不確定該如何應對這種局面，於是朝@5瞥了一眼。就在心跳之間，戰鬥旋即爆發。

## node 1900096  (DIAL_Z19#445)
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[31] (xor=0xfc mask=0x5c mode=2 chapters=-)] -> node 4278260736
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#446
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [23308..2]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#449
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [23833..2]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 1900092  (DIAL_Z19#452)
- speaker=0  style=0
- effects:
    - DAMAGE Health+Stamina of party by -1280
    - ?wOp12 a1=26 a2=0
    - SET flag 0x1fce=1
- branches:
    - [flag 0x1fb4 in [24551..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: @4倒抽了一口氣。  他緊緊揪著自己腹部糾結成一團的肌肉，絕望地看向@5，只見對方看起來也是同樣的狀況……

### (sub) DIAL_Z19#453
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們一定又撞上了某種魔法邊界，就跟我們之前在那頂帳篷周圍遇到的那種一樣。我有種感覺，他們並不希望我們穿越這個區域。」

### (sub) DIAL_Z19#454
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我覺得自己就像被牧人牽著走的一頭牛。這邊轉轉，那邊繞繞……」

### (sub) DIAL_Z19#455
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們永遠都還有硬闖向前的選擇。除了那股痛楚之外，似乎沒有什麼真正能阻止我們朝這個方向前進。不過話說回來，這也可能只是接下來還會有更糟情況的一種警告罷了。」

### (sub) DIAL_Z19#457
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#458
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這是某種ó魔法邊界。有人不希望我們繼續朝這個方向前進……」

### (sub) DIAL_Z19#459
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我覺得自己就像被牧人牽著走的一頭牛。這邊轉轉，那邊繞繞……」

### (sub) DIAL_Z19#460
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們永遠都還有硬闖向前的選擇。除了那股痛楚之外，似乎沒有什麼真正能阻止我們朝這個方向前進。不過話說回來，這也可能只是接下來還會有更糟情況的一種警告罷了。」

## node 1900093  (DIAL_Z19#462)
- speaker=0  style=0
- effects:
    - DAMAGE Health+Stamina of party by -5120
    - ?wOp12 a1=26 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文放聲尖叫了起來。  一陣劇痛猛然襲來，痛得他整個人跪倒在地。在他身旁，戈拉斯似乎也同樣受到了這股魔法力量的波及。

### (sub) DIAL_Z19#463
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「這比我們前往艾爾凡達那趟旅途中所感受到的，還要更加……ó劇烈ð……得多。這股力量，簡直……ó龐大到難以想像。」

## node 1900094  (DIAL_Z19#465)
- speaker=0  style=0
- effects:
    - apply status/condition to party idx=6 amt=100
    - ?wOp12 a1=26 a2=0
    - play sfx 26
    - SET flag 0x7540=2
- text: 一道光芒在@4的腦海中猛然炸開。  ã你ã竟ã敢ã公ã然ã違ã逆ã提ã米ã里ã安ã雅ã眾ã神ã所ã共ã同ã頒ã布ã的ã律ã令ã、ã律ã法ã與ã誡ã命ã，ã危ã及ã了ã普ã天ã之ã下ã、ã眾ã生ã共ã同ã的ã福ã祉ã安ã危ã，ã此ã舉ã實ã在ã罪ã不ã可ã赦ã、ã萬ã死ã難ã辭ã其ã咎ã。ã你ã們ã兩ã人ã，ã如ã今ã都ã必ã須ã為ã自ã己ã所ã犯ã下ã的ã這ã樁ã異ã端ã邪ã說ã之ã罪ã，ã付ã出ã應ã有ã的ã慘ã痛ã代ã價ã，ã來ã自ã異ã界ã的ã薩ã瓦ã尼ã啊ã，ã你ã們...

## node 1900112  (DIAL_Z19#466)
- speaker=0  style=0
- branches:
    - [flag 0x1fcf in [0..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#467
- speaker=2  style=0
- effects:
    - SET flag 0x1fcf=1
- branches:
    - [always] -> node 0 (no jump)
- text: 「我無意冒犯，但我們ñ究竟要去哪裡呢？」

### (sub) DIAL_Z19#468
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們必須找到我的女兒，加米娜！以我目前的狀態，實在沒辦法觸及她的心靈。我不清楚ñ你們一路上的經歷，但我自己的搜尋，始終沒能完成。」

### (sub) DIAL_Z19#469
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「那我們豈不是還要繼續這樣漫無目的地亂逛下去？！」

### (sub) DIAL_Z19#470
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我實在不想讓我們的搜尋，就這樣毫無章法地漫無目的下去。往北邊，也就是眾門之主達沙梵的那根石柱那裡，或許能找到一些幫助。在受困期間，我發現自己的心思，總是不自覺地聚焦在那個方向……」

### (sub) DIAL_Z19#471
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「你所說的那根石柱，我們知道在哪裡。」

## node 1900113  (DIAL_Z19#473)
- speaker=0  style=0
- branches:
    - [flag 0x1fd0 in [0..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z19#474
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「ã「ã去ã尋ã覓ã找ã出ã瓦ã爾ã赫ã魯ã一ã族ã當ã年ã所ã遺ã留ã下ã來ã的ã那ã一ã整ã批ã古ã老ã部ã眾ã們ã吧ã，ã好ã不ã好ã呢ã？ã」 我實在不明白這是什麼意思……」

### (sub) DIAL_Z19#475
- speaker=4  style=0
- branches:
    - [flag 0x1fce in [27971..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 「我猜想你ñ確實明白，這個地方並不ñ一直都是現在這副模樣的。等到加米娜安全無虞之後，找個時間，再進一步詢問我吧。」  「眼下，你們只需要知道，瓦爾赫魯離開這片土地時，還留下了ñ另外一樣東西。不管那東西究竟是什麼，想必也跟他們的那些遺跡一樣，被埋藏了起來。既然它能夠歷經這麼多年依然完好無損，想必一定受到了某種魔法防禦的保護……或許正是由這些石柱所產生的防禦。」

### (sub) DIAL_Z19#476
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「歐文和我，就ñ很不走運地，在這座島嶼的西南角，撞上了某種古怪的防禦機制。」

### (sub) DIAL_Z19#477
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「先別急著下定論，說不定你們其實是ñ走運了呢。這下我們知道了必須儘快趕往的地點在哪裡。這一次，我們不會再受到那些防禦機制的傷害了。」

### (sub) DIAL_Z19#478
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「戈拉斯和我，在這裡從來沒遇過那樣的防禦機制。」

### (sub) DIAL_Z19#479
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「在我的搜尋範圍裡，除了這座島嶼的南端之外，其餘地方我都已經探查過了。我們應該從那裡開始才對……」

### (sub) DIAL_Z19#480
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「我們已經搜索過這座島嶼的東南端了，那就只剩下……」

### (sub) DIAL_Z19#481
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 「大家做好準備。我們要前往西南方了。」
