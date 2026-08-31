# DIAL_Z20

1550 records, 24 keyed nodes

## node 2000023  (DIAL_Z20#0)
- speaker=0  style=0
- effects:
    - push return-address key 223 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [671..0]] -> node 65537
    - [flag 0x7537 in [960..0]] -> node 131074
    - [flag 0x7537 in [1365..0]] -> node 196611
    - [flag 0x7537 in [1603..0]] -> node 262148
    - [flag 0x7537 in [1742..0]] -> node 327685
    - [flag 0x7537 in [2265..0]] -> node 393222
    - [flag 0x7537 in [2691..0]] -> node 458759
    - [flag 0x7537 in [2966..0]] -> node 524296
    - [flag 0x7537 in [3092..0]] -> node 589833

## node 2000026  (DIAL_Z20#2)
- speaker=0  style=0
- effects:
    - SET flag 0x1ea9=0
    - SET flag 0x1eaa=0
    - SET flag 0x1eab=0
    - SET flag 0x1eac=0
    - SET flag 0x1ead=0
    - SET flag 0x1eae=0
    - SET flag 0x1eaf=0
    - SET flag 0x1eb0=0
    - SET flag 0x1eb1=0
    - SET flag 0x1eb2=0
    - SET flag 0x1eb3=0
    - SET flag 0x1eb4=0
    - SET flag 0x1eb6=0
    - SET flag 0x1eb7=0
    - SET flag 0x1eb8=0
    - SET flag 0x1eb9=0
    - SET flag 0x1e84=0
    - SET flag 0x1eba=0
    - SET flag 0x1ebb=0
    - SET flag 0x1ebd=0
    - SET flag 0x1ebe=0
    - SET flag 0x1ebf=0
    - SET flag 0x1ec0=0
    - SET flag 0x1ec1=0
    - SET flag 0x1ec2=0
    - SET flag 0x1ec3=0
    - SET flag 0x1ec4=0
    - SET flag 0x1e87=0
    - SET flag 0x1ec6=0
    - SET flag 0x1ec7=0
    - SET flag 0x1ec8=0
    - SET flag 0x1ec9=0
    - SET flag 0x1eca=0
    - SET flag 0x1ecc=0

### (sub) DIAL_Z20#3
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[0,2,1]
    - GIVE gold +143
    - HEAL party amt=100
    - event_bitmap_hi[26] bitop
    - SET flag 0x1ecb=0
    - SET flag 0x1ecd=0
    - SET flag 0x0072=1
    - SET flag 0x007c=1
    - SET flag 0x0073=1
    - SET flag 0x007b=1
    - SET flag 0x0096=1
    - SET flag 0x0039=1
    - SET flag 0x0035=1
    - SET flag 0x0030=1
    - SET flag 0x0029=1
    - SET flag 0x0055=1
    - SET flag 0x0058=1
    - SET flag 0x005a=1
    - SET flag 0x0053=1
    - SET flag 0x001a=1
    - SET flag 0x009d=1
    - SET flag 0x009c=1
    - SET flag 0x0063=1
    - SET flag 0x0064=1
    - SET flag 0x0002=1
    - SET flag 0x0001=1
    - SET flag 0x000e=1
    - SET flag 0x003e=1

### (sub) DIAL_Z20#4
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[4,2,1]
    - HEAL party amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#5
- speaker=0  style=0
- effects:
    - SET PARTY size=2 members=[4,1,0]
    - HEAL party amt=100
    - load teleport table 30
    - SET flag 0x1ecb=0
    - SET flag 0x1e88=0
    - SET flag 0x1ecd=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#6
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [1146..0]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#7
- speaker=0  style=0
- effects:
    - TAKE gold -1000
    - GIVE gold +1000
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#8
- speaker=0  style=0
- effects:
    - SET flag 0x1a84=1
    - SET flag 0x1a2f=1
    - SET flag 0x1a2e=1
    - SET flag 0x1a2d=1
    - SET flag 0x00a4=1
    - SET flag 0x009b=1
    - SET flag 0x0070=1
    - SET flag 0x0076=1
    - SET flag 0x0077=1
    - SET flag 0x0057=1
    - SET flag 0x005b=1
    - SET flag 0x005c=1
    - SET flag 0x0059=1
    - SET flag 0x0093=1
    - SET flag 0x0095=1
    - SET flag 0x0042=1
    - SET flag 0x005e=1
    - SET flag 0x000c=1
    - SET flag 0x0017=1
    - SET flag 0x0012=1
    - SET flag 0x0088=1

### (sub) DIAL_Z20#9
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[4,2,1]
    - HEAL party amt=100
    - load teleport table 31
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#10
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=5)
    - GIVE item '\x07' cond=200 to member#2 (cost 0)
    - GIVE item 'o' cond=200 to member#2 (cost 0)
    - event_bitmap_hi[36] bitop
    - SET flag 0x1aa4=1
    - SET flag 0x1aa2=1
    - SET flag 0x1abf=1
    - SET flag 0x1a38=1
    - SET flag 0x1a43=1
    - SET flag 0x0040=1
    - SET flag 0x003c=1
    - SET flag 0x006e=1
    - SET flag 0x0037=1
    - SET flag 0x0091=1
    - SET flag 0x0092=1
    - SET flag 0x0041=1
    - SET flag 0x009e=1
    - SET flag 0x008c=1

### (sub) DIAL_Z20#11
- speaker=0  style=0
- effects:
    - SET PARTY size=2 members=[1,2,0]
    - HEAL party amt=100
    - HEAL party amt=50
    - SET flag 0x1a85=1
    - SET flag 0x1abd=1
    - SET flag 0x1ace=1
    - SET flag 0x1aca=1
    - SET flag 0x0048=1
    - SET flag 0x0043=1
    - SET flag 0x004d=1
    - SET flag 0x004f=1
    - SET flag 0x0050=1
    - SET flag 0x004c=1

### (sub) DIAL_Z20#12
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[4,5,0]
    - HEAL party amt=100
    - SET flag 0x1ecb=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#13
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=1)
    - HEAL speaker amt=100
    - RAISE Strength of member#0 by 1280
    - RAISE Crossbow Acc of member#0 by 2560
    - RAISE Melee Acc of member#0 by 2560
    - RAISE Casting Acc of member#0 by 2560
    - RAISE Assessment of member#0 by 2560
    - RAISE Armorcraft of member#0 by 2560
    - RAISE Weaponcraft of member#0 by 2560
    - RAISE Barding of member#0 by 2560
    - RAISE Haggling of member#0 by 2560
    - RAISE Lockpick of member#0 by 2560
    - RAISE Scouting of member#0 by 2560
    - RAISE Stealth of member#0 by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#14
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=5)
    - HEAL speaker amt=100
    - RAISE Strength of member#0 by 512
    - RAISE Crossbow Acc of member#0 by 512
    - RAISE Melee Acc of member#0 by 512
    - RAISE Casting Acc of member#0 by 512
    - RAISE Assessment of member#0 by 512
    - RAISE Armorcraft of member#0 by 512
    - RAISE Weaponcraft of member#0 by 512
    - RAISE Barding of member#0 by 512
    - RAISE Haggling of member#0 by 512
    - RAISE Lockpick of member#0 by 512
    - RAISE Scouting of member#0 by 512
    - RAISE Stealth of member#0 by 512
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#15
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=6)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#16
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [2216..0]] -> node 4294902060
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#17
- speaker=0  style=0
- effects:
    - TAKE gold -3000
    - GIVE gold +3000
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#18
- speaker=0  style=0
- effects:
    - SET flag 0x1a9a=1
    - SET flag 0x006f=1
    - SET flag 0x007d=1
    - SET flag 0x0084=1

### (sub) DIAL_Z20#19
- speaker=0  style=0
- effects:
    - SET PARTY size=2 members=[2,1,0]
    - HEAL party amt=100
    - SET flag 0x1c85=1
    - SET flag 0x1ecd=0
    - event_bitmap_hi[36] bitop
    - event_bitmap_hi[13] bitop
    - event_bitmap_hi[8] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#20
- speaker=0  style=0
- effects:
    - load teleport table 37
    - bind speaker-name slot (kind=0 sub=3)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#21
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=2)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#22
- speaker=0  style=0
- effects:
    - SET flag 0x1aa9=1
    - SET flag 0x1aa3=1
    - SET flag 0x1ac3=1
    - SET flag 0x1ac4=1
    - SET flag 0x1a6c=1
    - SET flag 0x1a68=1
    - SET flag 0x1a6d=1
    - SET flag 0x1a8b=1
    - SET flag 0x1ab9=1
    - SET flag 0x1aba=1
    - SET flag 0x1ab6=1
    - SET flag 0x1ab4=1
    - SET flag 0x1ab8=1
    - SET flag 0x1ab7=1
    - SET flag 0x1a7e=1
    - SET flag 0x0075=1
    - SET flag 0x007a=1
    - SET flag 0x0068=1
    - SET flag 0x006a=1
    - SET flag 0x0066=1
    - SET flag 0x0065=1
    - SET flag 0x0025=1
    - SET flag 0x009f=1
    - SET flag 0x00a1=1

### (sub) DIAL_Z20#23
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[4,5,0]
    - HEAL party amt=100
    - SET flag 0x1c85=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#24
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=5)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#25
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=6)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#26
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=1)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#27
- speaker=0  style=0
- effects:
    - SET flag 0x1a76=1
    - SET flag 0x1a77=1
    - SET flag 0x1a36=1
    - SET flag 0x1a37=1
    - SET flag 0x1a33=1
    - SET flag 0x007e=1
    - SET flag 0x0080=1
    - SET flag 0x0049=1
    - SET flag 0x0006=1
    - event_bitmap_hi[26] bitop

### (sub) DIAL_Z20#28
- speaker=0  style=0
- effects:
    - SET PARTY size=2 members=[2,1,0]
    - HEAL party amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#29
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=3)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#30
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=2)
    - HEAL speaker amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#32
- speaker=0  style=0
- effects:
    - SET PARTY size=3 members=[3,2,1]
    - HEAL party amt=100
- branches:
    - [flag 0x7531 in [3170..0]] -> node 4294901770
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#33
- speaker=0  style=0
- effects:
    - GIVE gold +100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#34
- speaker=0  style=0
- effects:
    - SET flag 0x1ac8=1
    - SET flag 0x1acb=1
    - SET flag 0x1acd=1

## node 2000027  (DIAL_Z20#35)
- speaker=255  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=30)
    - bind speaker-name slot (kind=1 sub=32)
- branches:
    - [always] -> node 0 (no jump)
- text: 其實，ó我……這個……不對。剛見到你的時候，我腦子裡閃過一個想問你的問題，可這會兒卻怎麼也想不起來了。要是我晚點再來問你，會不會太打擾？我們還有些別的事得先去處理……

### (sub) DIAL_Z20#36
- speaker=253  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你去忙吧。我自己也還有些事要辦。

## node 2000001  (DIAL_Z20#38)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb9=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483649 (GoodBye target)
- branches:
    - [flag 0x0001 in [3799..0]] -> node 4294901761
    - [flag 0x0002 in [4359..0]] -> node 4294901761
    - [flag 0x0003 in [5009..0]] -> node 4294901761
    - [flag 0x0004 in [5496..0]] -> node 4294901761
    - [flag 0x0005 in [6038..0]] -> node 4294901761
    - [flag 0x0006 in [6317..0]] -> node 4294901761
    - [flag 0x0007 in [7273..0]] -> node 4294901761
    - [flag 0x0008 in [8401..0]] -> node 4294901761
    - [flag 0x0009 in [9526..0]] -> node 4294901761
    - [flag 0x000a in [10271..0]] -> node 4294901761
    - [flag 0x000b in [10895..0]] -> node 4294901761
    - [flag 0x000c in [11646..0]] -> node 4294901761

### (sub) DIAL_Z20#39
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#40
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我現在方向感跟距離感都有點不太準。我們昨晚喝了點酒，現在還沒完全醒過來。最近的地方能讓我們梳洗一下，是哪個方向？

### (sub) DIAL_Z20#41
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看你這麼糊塗，昨晚肯定喝得不輕吧！沿著大路一直往南走，就能進拉姆特了。要找好吃的，「藍輪」客棧是個穩妥的選擇，不過先提醒你，他們的圖蘭尼菜可有點辣。

### (sub) DIAL_Z20#42
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#44
- speaker=0  style=0
- effects:
    - SET flag 0x0003=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#45
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我個人是有點受夠了睡地上。有沒有推薦的好客棧？

### (sub) DIAL_Z20#46
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拉姆特有「藍輪」客棧，鷹谷那邊也可以試試「塵封矮人」。真要是走投無路了，我猜你也可以闖進那一帶的某間廢棄屋子將就一晚，不過要我說，睡在一間隨時可能塌下來砸到自己的屋子裡，我可睡不安穩。當然，居民搬走說不定也有正當理由。我聽說洛瑞爾南邊有幾戶人家，是因為那附近開始鬧瘟疫才搬走的。

### (sub) DIAL_Z20#47
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#49
- speaker=0  style=0
- effects:
    - SET flag 0x0005=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#50
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你見過的那些廢棄屋子裡，有留下什麼東西嗎？

### (sub) DIAL_Z20#51
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒什麼值錢的東西。幾個櫥櫃裡剩點食物，偶爾有一兩枚金幣被踢到屋子地基底下，多半是些遺失的雜物。我去過的大部分地方都裝了那種撬不開的鎖——叫什麼來著——對，韋伯鎖。裝了韋伯鎖，我根本進不去。

### (sub) DIAL_Z20#52
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#54
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#55
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這話聽起來可能有點瘋，不過您介不介意讓我看看您的手？

### (sub) DIAL_Z20#56
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的手？好吧……為什麼？

### (sub) DIAL_Z20#57
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就當是遷就我一下吧。我們在鷹谷遇到一個人，他說我們該找一個手上有記號的人，說那人的行囊裡有非常重要的卷軸，要我們務必聽他的話。  不過您的手看起來沒什麼異狀。

### (sub) DIAL_Z20#58
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 卷軸？聽起來你們遇到的那個人，腦子恐怕有點不清楚。

### (sub) DIAL_Z20#59
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#61
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#62
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不太確定，不過我想我可能弄丟了一件非常珍貴的東西……

### (sub) DIAL_Z20#63
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒不會太擔心。看你是在哪弄丟的，多半ñ還在原地沒被人動過。

### (sub) DIAL_Z20#64
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#66
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#67
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道我這位朋友洛克利爾怎麼想，不過要是您能指點我們去哪吃頓像樣的飯，我會很感激。我們最近一直找不到吃的。

### (sub) DIAL_Z20#68
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不奇怪。我們已經有證據顯示，莫瑞德人這幾個月一直在賽瑟儂附近刺探情報，合理推測他們是想先掠光當地的資源，替這次進攻鋪路。上次他們進軍賽瑟儂時也玩過同一套把戲。我們料到會有這麼一手，便自己備了些糧食。薇琳蒂很慷慨地把她的房子暫時借給我們存放物資。需要什麼儘管拿，但拜託別拿太多，我們的必需品已經相當吃緊了。要是你們留意路上那些老樹幹，會找到一些為防萬一儲存起來的口糧，不過我勸你們小心點，有些恐怕已經放壞了。

### (sub) DIAL_Z20#69
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#71
- speaker=0  style=0
- effects:
    - SET flag 0x000a=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#72
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你有沒有去過一間叫『橫笛與月桂』的酒館？要是我沒記錯方向，就在這裡北邊一點。他們的肉派做得很棒。

### (sub) DIAL_Z20#73
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 橫笛？我特地去過那裡好幾次呢。要不是有老凱利的那杯拉格啤酒，我好幾次恐怕都要渴死了。真可惜老人家一過世，店就這麼關了。

### (sub) DIAL_Z20#74
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們路過的時候可沒關門。事實上，那個經營酒館的老人家看起來還挺硬朗的。你確定我們說的是同一間？

### (sub) DIAL_Z20#75
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 橫笛可是整個幽暗林裡唯一一間酒館。這事透著古怪。老凱利差不多一年前就過世了，他過世後根本沒有親戚接手經營。

### (sub) DIAL_Z20#76
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽你這口氣，倒像是自家人似的。你肯定常去光顧吧。

### (sub) DIAL_Z20#77
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，幽暗林算是我的必經之路。我趕路的時候，總喜歡找些熟面孔聊聊。

### (sub) DIAL_Z20#78
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#80
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#81
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道一個叫克雷格的人嗎？

### (sub) DIAL_Z20#82
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他住在南邊……我是說，如果我沒記錯的話，有個這名字的人住在賽瑟儂附近。

### (sub) DIAL_Z20#83
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那也許你能幫我們解開個疑惑。我們碰見他的時候，他自稱二十三歲，但一看就知道他少說也有七八十歲了。他說自己在幽暗林東南角設陷阱捕獵時出了什麼事，人就突然開始迅速衰老。這聽起來簡直瘋狂，不過我們想知道你是不是知道，是什麼把他逼瘋的。

### (sub) DIAL_Z20#84
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我認識的克雷格只有二十三個仲夏節那麼大，而且據我所知，他父親也不叫克雷格。他看起來健康嗎？

### (sub) DIAL_Z20#85
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 以一個八十歲的老人來說，強壯得跟馬一樣。

### (sub) DIAL_Z20#86
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道這事背後到底是怎麼回事，不過給你們個建議：在我們之中有誰查清楚是怎麼回事之前，最好別靠近他去的那片幽暗林。

### (sub) DIAL_Z20#87
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#89
- speaker=0  style=0
- effects:
    - SET flag 0x1a35=1
    - GIVE item 'e' cond=1 to member#6 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#90
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在莫瑞德人的箱子裡發現了你的字條。裡頭那個瓦尼還在你那裡嗎？

### (sub) DIAL_Z20#91
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 如果你說的是那個魔法裝置，是的，還在我這，不過不管是我還是薇琳蒂，都還沒弄清楚它是做什麼用的。我們原本希望它能用來對付莫瑞德人。

### (sub) DIAL_Z20#92
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呸！哪個殺蟾蜍的女巫弄得懂這玩意兒！這是圖蘭尼的東西，八成是那種可惡的『大道』法術造出來的物件。那群自以為是的傢伙搞出一整套新魔法，就是存心來氣我的！

### (sub) DIAL_Z20#93
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 雖然薇琳蒂大概不會這麼說，但我相信她也是這個意思。她目前還在仔細研究這東西。你們走之前我去幫你們拿來。

### (sub) DIAL_Z20#94
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#96
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#97
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我對幽暗林還不太熟悉，您知道的事……不管什麼都好……

### (sub) DIAL_Z20#98
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也沒什麼好說的，至少幽暗林本身沒什麼特別。它其實不怎麼『幽暗』，說是『林』嘛……我覺得也有點勉強稱得上森林，不過當地人喜歡這麼叫，就隨他們去吧。地方是挺大的。除了蠍子跟幾個想在那裡種點什麼的自耕農，沒什麼人願意住那兒。商人也都對那地方避之唯恐不及。據我所知，橫笛以前是……現在也是幽暗林裡唯一在營業的店家。

### (sub) DIAL_Z20#99
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#101
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#102
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不知道您知不知道，我們能上哪弄到一袋生穀物？

### (sub) DIAL_Z20#103
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們要那玩意兒做什麼？那東西又不能吃，至少不做點噁心的加工是吃不了的。別告訴我你們開始迷上什麼濃粥了……

### (sub) DIAL_Z20#104
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，沒那麼糟。達拉神殿這一季照顧的窮困信眾多到快忙不過來了，需要一些穀物送去磨坊。我們想著能幫上一點忙。

### (sub) DIAL_Z20#105
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來是件善事。你們可以去找住在高堡岔路南邊的海利．貝騰科特。我以前替家父跟他做過生意，他說不定願意跟你們交換點什麼。

### (sub) DIAL_Z20#106
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#108
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#109
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是叔叔跟我往東邊走，說不定會順道去高堡逛逛，看看風景。

### (sub) DIAL_Z20#110
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒什麼好看的。就是個典型的邊境小鎮，唯一值得一提的就是那座城堡本身。我聽說裂界之戰後，亞魯莎親王還出資修了些新的防禦工事，不過整體來說我沒什麼特別印象。不過我得承認，他們那間軍械庫倒是不錯，庫存了幾把我這輩子見過最漂亮的劍。

### (sub) DIAL_Z20#111
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000002  (DIAL_Z20#113)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1e84=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483650 (GoodBye target)
- branches:
    - [flag 0x000d in [12345..0]] -> node 4294901761
    - [flag 0x000e in [12892..0]] -> node 4294901761
    - [flag 0x000f in [13805..0]] -> node 4294901761
    - [flag 0x0011 in [16567..0]] -> node 4294901761
    - [flag 0x0012 in [17086..0]] -> node 4294901761
    - [flag 0x0014 in [17676..0]] -> node 4294901761
    - [flag 0x0015 in [19412..0]] -> node 4294901761
    - [flag 0x0016 in [19981..0]] -> node 4294901761
    - [flag 0x0017 in [21124..0]] -> node 4294901761
    - [flag 0x0018 in [21750..0]] -> node 4294901761

### (sub) DIAL_Z20#114
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#115
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽說通往凱勒旺的永久裂界之門就在這附近。我原本希望能一睹它的風采……

### (sub) DIAL_Z20#116
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在去也看不到什麼。帝國內部，阿科瑪家跟阿納薩堤家之間起了衝突，法師議會已下令暫停帝國與王國之間的往來運輸，直到這場紛爭平息為止。我聽說這只是暫時的措施。

### (sub) DIAL_Z20#117
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#119
- speaker=0  style=0
- effects:
    - SET flag 0x000d=1
    - SET flag 0x000f=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#120
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 話說回來，你當初怎麼會想來米德凱米亞開一間客棧？在凱勒旺生意肯定更好做吧。

### (sub) DIAL_Z20#121
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我並非一直都是個酒館老闆。我原本是效忠信澤瓦伊家、隸屬卡蘇米伯爵麾下的一名士兵，裂界之戰末期，裂界之門崩塌，我就這麼被困在了這裡。我們當時都以為，此生再也見不到圖蘭努安尼的家人，也見不到凱勒旺那片翠綠的天空了。

### (sub) DIAL_Z20#122
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可是按照傳統，圖蘭尼戰士要是有淪為敵人俘虜的危險，都會自我了斷……

### (sub) DIAL_Z20#123
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大人，此言不假，不過伯爵曾告訴我們，在得到一位至尊法師——我想在米德凱米亞你們會稱之為法師——的許可之前，我們不得自我了斷。在那之前，我就安於經營這間藍輪客棧了。

### (sub) DIAL_Z20#124
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#126
- speaker=0  style=0
- effects:
    - SET flag 0x0011=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#127
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說你曾是圖蘭尼軍隊的士兵。你有沒有興趣教我們一些你們的戰鬥技巧？

### (sub) DIAL_Z20#128
- speaker=25  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [14258..0]] -> node 4294901761
    - [flag 0x0101 in [16266..0]] -> node 4294901761
- text: 這是我的榮幸，大人，不過恕我得收取一點酬勞。萬一我的盔甲受損，我可付不起修理的費用。    七十五枚金幣應該足夠彌補任何可能的損傷。這個價錢您能接受嗎？

### (sub) DIAL_Z20#129
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [14287..0]] -> node 4294901835
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#130
- speaker=0  style=0
- effects:
    - TAKE gold -750
    - RAISE Melee Acc of party by 1280
    - RAISE Defense of party by 1280
    - SET flag 0x1a3b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#131
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來還算合理。就這麼說定了。

### (sub) DIAL_Z20#132
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我五分鐘後在河邊跟你們碰面。不過我得先提醒一聲，我一旦披甲備戰，有時看起來會判若兩人。若因此對你們造成任何傷害，先在此致歉了。

### (sub) DIAL_Z20#133
- speaker=0  style=0
- effects:
    - ?wOp12 a1=50 a2=0
    - play sfx 50
    - play sfx 56
- branches:
    - [always] -> node 0 (no jump)
- text: @0張大了嘴。  從藍輪酒館狹窄的門口大步走出來的身影，已經完全看不出半點尋常酒館老闆的模樣。蘇馬尼顯然花了不少工夫重新武裝自己，穿上一套坑坑窪窪的藍色疊層盔甲，護脛、胸甲跟護腿都是用輕質木材打造，隨著他沉重的步伐咯吱作響。  「圖蘭尼盔甲？」@0問道。  蘇馬尼調整了一下遮住雙眼的藍羽頭盔。「我以前是名巡邏隊長。卡蘇米伯爵堅持要我留著信澤瓦伊家賜給我的這套盔甲。雖然我已不再於駐軍中效力，但我對伯爵的效忠誓言依然有效。準備好上課了嗎？」  「是，我想是的。」  這名圖蘭尼人的...

### (sub) DIAL_Z20#134
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: @0第三次從冰冷的拉姆特河裡爬出來，示意暫停這堂課。「好了好了，饒了我吧，叔叔，隨便你們這些該死的圖蘭尼人怎麼說『我投降』都行。」  「遵命，大人，」蘇馬尼呵呵一笑，已經開始恢復他那副謙遜酒館老闆的模樣。「等你們擦乾身子，我在藍輪裡等你們。」

### (sub) DIAL_Z20#135
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#136
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#137
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒是很想，不過看來我們手頭有點緊。

### (sub) DIAL_Z20#138
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是可惜。要是你們願意去駐軍那邊跟卡蘇米伯爵談談，我相信一定能替你們安排一份薪餉，到時候再回來上我的課。我想你們會覺得值得的。

### (sub) DIAL_Z20#139
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#140
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#141
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你開的價比我原本想的高了些。修盔甲能貴到哪去？

### (sub) DIAL_Z20#142
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的盔甲是圖蘭尼製的，說得更明確點，得由信澤瓦伊家的人來修才行。這是我們那個世界的規矩。

### (sub) DIAL_Z20#143
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#145
- speaker=0  style=0
- effects:
    - SET flag 0x001d=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#146
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道我們的盔甲還能撐多久。你知道哪裡能修嗎？

### (sub) DIAL_Z20#147
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們的盔甲跟我的一樣，我會建議去駐軍那邊試試，可惜王國的盔甲做法不一樣。我看麥克莫丹卡達爾裡的矮人應該幫得上忙。聽杜巴爾說，那些矮個子在打造武器盔甲這方面天賦異稟。

### (sub) DIAL_Z20#148
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#150
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#151
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在克朗多遇見一名叫馬卡拉的圖蘭尼人。你知道他的事嗎？

### (sub) DIAL_Z20#152
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他是法師議會的一名至尊法師。除此之外我所知不多，因為至尊法師不與凡夫俗子打交道。

### (sub) DIAL_Z20#153
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 凡夫俗子？

### (sub) DIAL_Z20#154
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是不屬於議會、也不是圖蘭尼帝國貴族的人。像我這樣的人，除非對方主動問話，否則跟他這種身分的人交談是不合禮數的。這是我原本那個族群的規矩。

### (sub) DIAL_Z20#155
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#157
- speaker=0  style=0
- effects:
    - event_bitmap_hi[5] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#158
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴爾跟我說您可是個活寶。有沒有機會哪天聽您講個圖蘭尼笑話？

### (sub) DIAL_Z20#159
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴爾跟很多人說過很多事。有些是真的，有些……就沒那麼真了。我只是把從駐軍那邊聽來的話重複一遍罷了。

### (sub) DIAL_Z20#160
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係，我不挑。

### (sub) DIAL_Z20#161
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 遵命，大人，不過容我先提醒一句，圖蘭尼的幽默……該怎麼說呢……審美跟你們不太一樣。你可能會覺得……有點費解。既然您有此雅興，我就盡力博您一笑吧。

### (sub) DIAL_Z20#162
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在第四十四任希朱卡瑪皇帝在位期間，歐瑪圖家、敘杜馬卡爾家跟赫巴托奇家這幾個小家族的家主，都被召往聖城覲見戰爭之王。歐瑪圖家知道戰爭之王與『黑拳黨』結盟，便決定獻上一名蘆葦階層的女子。敘杜馬卡爾家比較有錢，決定買下一把來自凱努家領地上秋加蜂巢的精美木劍獻上。但赫巴托奇家出的代價最大，騎著一頭凶猛的哈魯斯獸來到戰爭之王的宅邸。哈魯斯獸一到，立刻吞了那名蘆葦階層的女子，開始大肆破壞戰爭之王的宅邸。他用敘杜馬卡爾家獻上的那把劍砍下了那頭野獸的頭，卻也在過程中把劍給折斷了。眼見自己收到...

### (sub) DIAL_Z20#163
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊……那個……這個嘛……老實說，我從『在位』兩個字之後就完全聽不懂了，不過我相信您講得肯定很精彩。

### (sub) DIAL_Z20#164
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#166
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#167
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我有種預感，這樁紅寶石竊案恐怕不是單一事件。

### (sub) DIAL_Z20#168
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你倒是聽出弦外之音了。這是過去一年裡第六起同類竊案。有兩次，寶石就是在法師議會附近，從至尊法師馬卡拉的隨行人員身上被偷走的。就算是身手最頂尖的盜賊，要辦到這點也絕非易事。不管此人是誰，他敢不畏懼至尊法師的怒火，膽子肯定不小。  朋友，你要是打算追查這名盜賊，可得多加小心。我感覺得出他非常危險。

### (sub) DIAL_Z20#169
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#171
- speaker=0  style=0
- effects:
    - SET flag 0x0015=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#172
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們先前去了駐軍那邊，他們說有一群『灰衣戰士』偷走了一對紅寶石。灰衣戰士是凱勒旺上某種特殊武裝部隊嗎？

### (sub) DIAL_Z20#173
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 特殊是特殊，但不是你想的那種。灰衣戰士是失去榮譽的人，是家族被敵對家族摧毀的人。這種人只能自力更生、四處流浪直到死去，不過我聽說阿科瑪家的瑪拉收留了不少這樣的人到她的領地。還有些人聽說只要能抵達王國，就有機會獲得自由。很多人為此送了命。

### (sub) DIAL_Z20#174
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這種人到了這裡之後會去哪？

### (sub) DIAL_Z20#175
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 反正是離開拉姆特就是了，去哪都行。雖然這裡駐軍的成員得遵守王國的法律，可不少士兵骨子裡還是照著圖蘭尼的習俗過日子，我自己也一樣。要我們對這些灰衣人改觀，可不是件容易的事。  要是真是這些灰衣戰士偷了紅寶石，我建議你們去找一個名譽有污點的人……洛瑞爾鎮的凱佛．艾勒斯庫克。他在自己家裡做寶石生意。

### (sub) DIAL_Z20#176
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#178
- speaker=0  style=0
- effects:
    - SET flag 0x0018=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#179
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看啊，要是這些路再這麼危險下去，拉姆特城外的墳場恐怕會塞得比挖墳人挖得還快。

### (sub) DIAL_Z20#180
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這話比您想的還要真。拉姆特衛隊現在夜裡都會巡邏道路，天黑後被逮到的人，格殺勿論。

### (sub) DIAL_Z20#181
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有例外嗎？

### (sub) DIAL_Z20#182
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴爾跟我說他曾經……討價還價，這詞對嗎？……跟一名衛兵混過去了，不過他那張嘴皮子確實特別靈光。要是我，可不敢指望靠這種本事。

### (sub) DIAL_Z20#183
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#185
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#186
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 每次我試著討價還價，總是吃虧的那個。要我哄得農家姑娘寬衣解帶，那沒問題。可要說服商人虧本賣我東西，我可就沒那本事了。

### (sub) DIAL_Z20#187
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您生下來也不會走路，如今卻能一步接一步走得毫不費力。只要真心想學，什麼都學得會。

### (sub) DIAL_Z20#188
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我該找誰學討價還價？杜巴爾嗎？

### (sub) DIAL_Z20#189
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴爾就是杜巴爾。這本事是他天生的一部分，我懷疑他自己都搞不清楚自己是怎麼辦到的。不過住在羅姆尼有一位，我想能幫上忙。他叫米契爾．韋蘭德，是玻璃匠公會這個大公會的會長。他當年想買我們幾只圖蘭尼陶罐時，跟我談了好長一段時間。我想他能教您討價還價的訣竅。

### (sub) DIAL_Z20#190
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000024  (DIAL_Z20#192)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb0=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483672 (GoodBye target)
- branches:
    - [flag 0x001a in [22905..0]] -> node 4294901761
    - [flag 0x001b in [23702..0]] -> node 4294901761
    - [flag 0x001c in [24187..0]] -> node 4294901761
    - [flag 0x001d in [24818..0]] -> node 4294901761
    - [flag 0x001f in [25357..0]] -> node 4294901761
    - [flag 0x0020 in [26188..0]] -> node 4294901761
    - [flag 0x0021 in [28646..0]] -> node 4294901761
    - [flag 0x0022 in [29845..0]] -> node 4294901761
    - [flag 0x0023 in [31129..0]] -> node 4294901761
    - [flag 0x0024 in [31853..0]] -> node 4294901761
    - [flag 0x0025 in [32277..0]] -> node 4294901761

### (sub) DIAL_Z20#193
- speaker=0  style=0
- effects:
    - SET flag 0x001b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#194
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不是說我們有意獵殺你們說的那頭布拉克努爾，不過假如我們要找，牠長什麼樣子？

### (sub) DIAL_Z20#195
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 比你高上半個頭，渾身像是活生生的石頭做的。牠們鼻孔會噴出一股綠霧，不過我勸你別靠太近瞧，牠們可是說砸石頭就砸石頭，準保砸中你的腦門。已經有幾個自認勇猛的傢伙來試過身手了，除了把自己弄得傷痕累累、非得神殿救治不可，也沒見他們幹出什麼名堂來。這些人我勸你也一樣得防著點，跟防那頭怪物一樣——他們一個個都只惦記著我們懸賞給屠獸者的那筆金子。

### (sub) DIAL_Z20#196
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#198
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#199
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 照我們最近的運氣看，去神殿求點幫助大概也不是壞主意。最近的神殿在哪？

### (sub) DIAL_Z20#200
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 咱們矮人平時很少在灰塔或石山之外閒晃，不過就我所知，尊恩跟鷹谷之間有座基利安神的神殿。這附近好像也有座伊夏神殿，不過確切在哪，我可記不清了。

### (sub) DIAL_Z20#201
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#203
- speaker=0  style=0
- effects:
    - SET flag 0x1f6c=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#204
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人字鎖是什麼東西？

### (sub) DIAL_Z20#205
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管矮人還是人類，都打不出比這更缺德的鎖了。上頭有幾個小轉輪，一輪代表一個字母，得轉出鎖匠設計時心裡想的那個單字，箱子才會開。大部分鎖上還附了塊提示牌，用莫瑞德文寫的——免得連鎖匠自己都忘了答案。當然啦，這提示牌對絕大多數王國人來說根本沒用。誰叫它是用該死的莫瑞德文寫的！

### (sub) DIAL_Z20#206
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#208
- speaker=0  style=0
- effects:
    - SET flag 0x0020=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#209
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拉姆特藍輪客棧的老闆說，你們或許能幫我們修修盔甲……

### (sub) DIAL_Z20#210
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要不是咱們正忙著從這爛攤子裡把自己挖出來，是能幫你們弄弄。可眼下每個人都脫不了身。恕我直說，咱們手頭的麻煩事，可比幾件凹了的盔甲要緊多了。你們可以去試試住在鷹谷附近的一個隱士，這幾年他也算是小有名氣。

### (sub) DIAL_Z20#211
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#213
- speaker=0  style=0
- effects:
    - SET flag 0x001c=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#214
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 魯亞格是誰，或者說是什麼東西？他的洞穴又是怎麼回事？我無意中聽人提起他……牠？

### (sub) DIAL_Z20#215
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無意中聽到，我腳趾頭才信！你們自己四處打聽的吧？不過也沒什麼壞處。魯亞格是頭了不起的巨獸，一條龍！牠在麥克莫丹住了好幾百年，大概十年前才過世。我聽咱們的多爾根王說，牠嚥氣的時候精靈王配托馬斯也在場，不過我是不太信這說法。牠的洞穴倒真是個奇景，就埋在咱們目前開挖的地方再過去一點。當年那裡藏了不少寶藏——可惜大半都鎖在裝著莫瑞德人字鎖的箱子裡——說不定現在還在。改天再回來，也許咱們可以一起去瞧瞧！

### (sub) DIAL_Z20#216
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#218
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#219
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是盔甲修不了，那能不能至少幫我們的劍想想辦法？我不是有意刁難，只是我們現在情況真的很緊急。

### (sub) DIAL_Z20#220
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是耳聾了嗎，小子？我剛才不是說了，咱們現在沒空修東修西的。要是你沒注意到，咱們自己也正是情況緊急！

### (sub) DIAL_Z20#221
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們願意付錢……

### (sub) DIAL_Z20#222
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我信你願意，就跟我知道下頭那些矮人肯花錢求個活路出來一樣沒錯！問題是時間，時間啊！  唉！這樣吧，我教你們個磨劍的訣竅，你們保證不再去煩礦坑裡其他人，成不成？我看這幾枚金幣拿去拉姆特，正好能雇幾個壯丁來幫忙。

### (sub) DIAL_Z20#223
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我以我的名譽保證。

### (sub) DIAL_Z20#224
- speaker=15  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [27232..0]] -> node 4294901761
    - [flag 0x0101 in [28391..0]] -> node 4294901761
- text: 那也只好這樣了。我教你們一點磨兵器的手藝，不過這番工夫，我要收五十枚金幣的酬勞。成交嗎？

### (sub) DIAL_Z20#225
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [27261..0]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#226
- speaker=0  style=0
- effects:
    - TAKE gold -500
    - RAISE Weaponcraft of party by 2560
    - SET flag 0x1a4c=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#227
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 走之前一定把金子給你。現在讓我們瞧瞧你的訣竅吧。

### (sub) DIAL_Z20#228
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 仔細看好我怎麼做。我可不想多說第二遍。首先，手邊得備一塊磨刀石，沒這個，我這套訣竅就跟魚長膝蓋一樣沒用。  最要緊的是劍刃劃過磨石時的角度……就像這樣……

### (sub) DIAL_Z20#229
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這倒有意思……  你把刀刃磨成兩面紋理相反的斜面。一邊一個方向，正好相對。這樣劈砍出來的傷口肯定不簡單。

### (sub) DIAL_Z20#230
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 保管你砍出的傷口，敵人一輩子忘不了。磨兵器這堂課就上到這兒，小子。咱們倆都還有更要緊的事要辦。

### (sub) DIAL_Z20#231
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#232
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#233
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你有沒有過一種感覺，好像諸神在耍弄你……

### (sub) DIAL_Z20#234
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們沒錢付我。掏不出錢，我就抽不出時間。就這麼簡單。

### (sub) DIAL_Z20#235
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#236
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#237
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我現在也沒特別想上課。我們再看看能不能找別人幫忙磨劍吧。

### (sub) DIAL_Z20#238
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。咱們倆都還有事要忙。

### (sub) DIAL_Z20#239
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#241
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#242
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真沒想到這一帶居然沒什麼奎格熱的病例。薩斯的伊夏修道院那邊可鬧得挺兇的。

### (sub) DIAL_Z20#243
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哼！你要說布爾加蘭，就用它正經的名字叫，別用那個凱許人的鬼叫聲來稱呼。

### (sub) DIAL_Z20#244
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩斯以前是矮人的地方？

### (sub) DIAL_Z20#245
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 修道院本身不是，不過底下的洞窟是！那是矮人有史以來挖過最大的綠寶石礦，叫麥克布爾加蘭多克。礦坑四通八達，綿延數哩，有一部分洞穴就正好在如今修道院底下，不過我聽說那些傻里傻氣的神父已經把隧道堆得滿滿的都是書。咱們本來還擁有那些洞窟，後來梅賈卡爾．黑補丁搬進了蓋在其中一個入口上方的城堡，咱們才跟他談了個協議。

### (sub) DIAL_Z20#246
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那梅賈卡爾現在還擁有那座礦？

### (sub) DIAL_Z20#247
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊，前提是屍體也算擁有東西的話。他早就死了，就算按咱們矮人的算法也是好久以前的事了。那礦坑現在歸伊夏修士會所有，不過我看他們大概也不知道怎麼從他們的地窖走到礦坑的主通道去。

### (sub) DIAL_Z20#248
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#250
- speaker=0  style=0
- effects:
    - SET flag 0x0023=1
    - SET flag 0x0024=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#251
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道我們上哪能弄到一套灰塔的鈑金甲嗎？

### (sub) DIAL_Z20#252
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，該死！那些傢伙再這麼搞下去，我非把牠們燉了吃不可……你們是跟那些該死的狗頭人打過交道吧？牠們跟你們說要那套鈑金甲做什麼？獻給魯亞格的寶藏？贖回一位失蹤的狗頭人公主？牠們是在耍你們，還拿咱們墊背。灰塔的鈑金甲，這卡達爾這一頭你們是弄不到的！

### (sub) DIAL_Z20#253
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是我糊塗了。難道矮人都發誓不穿盔甲了？

### (sub) DIAL_Z20#254
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們王國人啊，一個個蠢得跟趕牲口的一樣。咱們矮人才不是住在這些礦坑裡呢，就跟你們的萊亞姆王也不是住在海裡一樣——雖然他確實是從一座島上統治王國！咱們大部分族人都住在跟你們差不多的村子裡，唯一不同的是，咱們大多數村子都在灰塔西側。拉姆特這一頭，用不著什麼矮人盔甲。

### (sub) DIAL_Z20#255
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼我們是絕對找不到矮人盔甲的了。

### (sub) DIAL_Z20#256
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可沒這麼說吧？你們可以去舊戰場找找看。老戰爭留下來的東西，有時候還會在那些地方出現。

### (sub) DIAL_Z20#257
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#259
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#260
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文，你想不想去看看矮人的古戰場？我是很想，而且我看納杜爾要是不趕快告訴我們上哪找，都快憋不住了。是吧，納杜爾？

### (sub) DIAL_Z20#261
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要說矮人絕不會忘記的一件事，那就是同胞灑過熱血的土地。是啊，我能告訴你們上哪找古戰場。該死的泰索格。你們那族跟咱們這族最後一次刀兵相見就是在那兒，那場惡戰凶猛得能讓賽瑟儂之戰看起來跟趕集一樣輕鬆。  你們要是真有這個心思，去泰索格渡口前的河西岸試試。那裡運氣最好。

### (sub) DIAL_Z20#262
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#264
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#265
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們想找路往下走，卻碰上一個深不見底的坑。有沒有辦法繞過去？

### (sub) DIAL_Z20#266
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要繞過去，就只能從上頭過。你們得備條繩子才能越過那些天坑。我倒是想借你們一條咱們的，不過恕我開個玩笑，咱們的繩子現在全都『綁死』了，脫不了身啊。

### (sub) DIAL_Z20#267
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#269
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#270
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 離開麥克莫丹卡達爾之後，我們要往哪個方向去艾爾凡達？我從沒去過那裡。

### (sub) DIAL_Z20#271
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小子，你該不會真以為這事有這麼容易吧？精靈可不會請外頭的人去喝什麼茶會，我看他們對你這位莫瑞德朋友，恐怕還要格外反感。

### (sub) DIAL_Z20#272
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，他不是莫瑞德人，他是……

### (sub) DIAL_Z20#273
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一個連艾爾凡達的路都不知道的精靈？我可不是傻子，你要是敢拿這套去唬戰帥托馬斯手下的邊境遊騎兵，你這小可憐蛋準保吃不了兜著走。他們會把你們倆倒吊在樹上，晃得跟麻雀落地一樣快。要是我兄弟麥卡努爾說的沒錯，他們搞不好見到你這位朋友，二話不說就一箭射了。

### (sub) DIAL_Z20#274
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼？他們對戈拉斯有什麼過節？

### (sub) DIAL_Z20#275
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是針對他本人，是針對莫瑞德人這個族。細節我也不太清楚，不過我聽說莫瑞德人正在莫拉埃林附近侵逼邊境。我兄弟麥卡努爾應該比我更清楚。要是他不在卡達爾，說不定人在去卡爾達拉的路上。

### (sub) DIAL_Z20#276
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000004  (DIAL_Z20#278)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1e88=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483652 (GoodBye target)
- branches:
    - [flag 0x0026 in [33602..0]] -> node 4294901761
    - [flag 0x0027 in [33981..0]] -> node 4294901761
    - [flag 0x0028 in [34627..0]] -> node 4294901761
    - [flag 0x0029 in [35235..0]] -> node 4294901761
    - [flag 0x002a in [36048..0]] -> node 4294901761
    - [flag 0x002b in [37580..0]] -> node 4294901761
    - [flag 0x002c in [40614..0]] -> node 4294901761
    - [flag 0x002d in [42233..0]] -> node 4294901761
    - [flag 0x002e in [42851..0]] -> node 4294901761
    - [flag 0x002f in [43181..0]] -> node 4294901761

### (sub) DIAL_Z20#279
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#280
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鷹谷這名字，我好像聽過。

### (sub) DIAL_Z20#281
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你最近聽到的，我猜多半是提醒你別在那裡過夜的警告吧。那原本是個不錯的小村子，直到一個外號叫『煙指』的宵小搬了進去。整個鎮上，沒有一把鎖是他開不了的。

### (sub) DIAL_Z20#282
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#284
- speaker=0  style=0
- effects:
    - SET flag 0x0026=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#285
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不知道是什麼緣故，有人費了好大工夫，就是要確保我們別靠近奧賽因斯的東側。我們在通往東邊的路上發現了陷阱。

### (sub) DIAL_Z20#286
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們認定那些陷阱是衝著你們設的。也許那是為了防止東邊有人溜到西邊來。我看不出擋著人不讓進鷹谷或洛瑞爾有什麼好處，但擋著人不讓進拉姆特，倒是有明顯的好處。我看你們最好往西南方向走，遠離設下這些陷阱的人。

### (sub) DIAL_Z20#287
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#289
- speaker=0  style=0
- effects:
    - SET flag 0x0031=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#290
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這一路上似乎到處都是急著預判我們行動的人。你知道這一帶有沒有誰擁有什麼不尋常的本事？那種好像能看穿人心思的人？

### (sub) DIAL_Z20#291
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不……說實話我還真想不出誰。不過我倒想起一個在艾格利跟我玩波基爾、贏走我一大筆錢的傢伙。我記得他叫ñ戴文ð。跟他玩那一晚輸掉的錢，我花了好一陣子才補回來。他幾乎把我一整個月賺的金幣都給贏光了。

### (sub) DIAL_Z20#292
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#294
- speaker=0  style=0
- effects:
    - SET flag 0x0028=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#295
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我剛執行完一項軍務歸來，得盡快又不引人注目地南下才行。你覺得有哪些地方我們該避開？

### (sub) DIAL_Z20#296
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無論如何，你們得避開艾格利到坦紐爾這條路。艾格利那邊要辦慶典，你這位精靈同伴八成一下子就會被人認出來。

### (sub) DIAL_Z20#297
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你怎麼會覺得我們是要去克朗多？

### (sub) DIAL_Z20#298
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 精靈很少走出艾爾凡達，就算真的出遠門，也不太可能跟一個小夥子跟一位紳爵結伴同行。不管你們三位在忙什麼，我猜想必是攸關王國福祉的事。合乎邏輯的話，克朗多是你們唯一該去的地方。

### (sub) DIAL_Z20#299
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#301
- speaker=0  style=0
- effects:
    - SET flag 0x1a53=1
    - SET flag 0x1a54=1
    - SET flag 0x1a55=1
    - SET flag 0x002c=1
    - SET flag 0x002d=1
    - SET flag 0x002f=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#302
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在艾格利遇到你那位玩波基爾的朋友，他跟我們說了些你跟他對局的事。他還提到跟你同行的精靈朋友，可正如你先前自己說的，精靈很少走出艾爾凡達，更不可能挨個城鎮跑去玩波基爾。說吧，艾薩克。你為什麼跟莫瑞德人勾結，艾薩克？他們在王國境內到底在幹什麼？

### (sub) DIAL_Z20#303
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來跟他們打交道的可不只我一個，紳爵大人。

### (sub) DIAL_Z20#304
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我現在沒心情跟你耍嘴皮子，艾薩克。說！

### (sub) DIAL_Z20#305
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然他們已經一腳把我踢開了，我看說出來也無傷大雅。他們是在黃騾附近一座穀倉裡活動。我找到一個老農夫，他租地不太挑人，對自己的領主跟親王都沒什麼忠誠可言。一個叫納戈的莫瑞德人搬了進去，把那裡當成雇用凱許傭兵的據點。

### (sub) DIAL_Z20#306
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這就說得通了。傭兵在王國境內活動不會引人注目。他們在籌劃什麼？

### (sub) DIAL_Z20#307
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我一向奉行不打聽的原則。知道太多會折壽的，尤其是跟一群瘋子打交道的時候。你們愛怎麼想都行，反正對我來說就是純粹的生意往來。他們付我錢，我負責去莫瑞德人的鎖箱那邊取貨送貨，我幫他們做的就只有這些。

### (sub) DIAL_Z20#308
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#310
- speaker=0  style=0
- effects:
    - SET flag 0x002e=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#311
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是不是從洛瑞爾的凱佛．艾勒斯庫克那買過一顆紅寶石？他跟我們說他賣給了一個叫艾薩克的人，形容起來聽著就像你。

### (sub) DIAL_Z20#312
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 怎麼，你想跟我買？這世上又不是只有這麼一顆紅寶石。

### (sub) DIAL_Z20#313
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他賣給你的那顆紅寶石，是從一名路過拉姆特的圖蘭尼法師那裡偷來的。駐軍希望能拿回這顆寶石。我們原本希望能說服你，至少先還給凱佛，把你的錢拿回來……

### (sub) DIAL_Z20#314
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽到你們的難處我很遺憾，不過我付錢跟凱佛買的時候，根本不知道這寶石是偷來的，而且我自己也有點小麻煩。我需要這顆寶石去付錢給一位鑄劍匠，把我的劍修好。

### (sub) DIAL_Z20#315
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你不能付他金幣嗎？

### (sub) DIAL_Z20#316
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他只收寶石當交易。這顆紅寶石不只夠付修理費，還能剩下一些，應該夠我吃上一個月，甚至更久。

### (sub) DIAL_Z20#317
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們能幫你修好這把劍呢？

### (sub) DIAL_Z20#318
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼，在這？就在大路中間？

### (sub) DIAL_Z20#319
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我又沒有工坊，也沒別的地方能修了。

### (sub) DIAL_Z20#320
- speaker=42  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [39073..0]] -> node 4294901761
    - [flag 0x0101 in [40311..0]] -> node 4294901761
- text: 這個嘛……我想也行。我這把劍相當昂貴，我可不想看它被弄得更糟。你們搞不好會愈修愈糟，除非你們真有磨兵器的本事……這個……你們真覺得自己有這麼厲害？

### (sub) DIAL_Z20#321
- speaker=0  style=0
- effects:
    - SET flag 0x1a57=1
    - read Weaponcraft -> dlg-result (sel=1)
- branches:
    - [flag 0x753d in [39122..0]] -> node 4294901805
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#322
- speaker=0  style=0
- effects:
    - GIVE item '9' cond=1 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#323
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夠好了。你的劍呢？

### (sub) DIAL_Z20#324
- speaker=42  style=0
- effects:
    - (on-exit) play sfx 19
    - (on-exit) play sfx 19
    - (on-exit) play sfx 19
    - (on-exit) play sfx 19
- branches:
    - [always] -> node 0 (no jump)
- text: 請小心點，這把劍我可花了不少錢。

### (sub) DIAL_Z20#325
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗯，我得說，你看起來確實有兩把刷子。這劍比之前好看多了。刃能撐得住吧？

### (sub) DIAL_Z20#326
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就算你把迪勒肯的荒野游兵全砍上一輪，這劍一個月之內都還鋒利得很。

### (sub) DIAL_Z20#327
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛……看來你這頭確實做到了約定的事。提醒我在你們離開前把紅寶石給你們。

### (sub) DIAL_Z20#328
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#329
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#330
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我手藝還算不差。

### (sub) DIAL_Z20#331
- speaker=42  style=0
- effects:
    - (on-exit) play sfx 20
    - (on-exit) play sfx 19
- branches:
    - [always] -> node 0 (no jump)
- text: 請……小心點，這把劍我可花了不少錢。

### (sub) DIAL_Z20#332
- speaker=42  style=0
- effects:
    - play sfx 20
    - play sfx 19
    - play sfx 65
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定你知道自己在做什麼嗎？這刃看起來……我覺得……那看起來……能不能把劍還給我？

### (sub) DIAL_Z20#333
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我覺得我剛才才抓到訣竅。要是你讓我再試一次……

### (sub) DIAL_Z20#334
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你做得已經夠多了，謝謝。幸好紅寶石還在我手上。希望鑄劍匠能一併修好你這番『改良』。

### (sub) DIAL_Z20#335
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#336
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#337
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 仔細想想，我大概是太衝動了。我可不想毀了你的兵器。

### (sub) DIAL_Z20#338
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 智者懂得量力而為，是吧？我記得司儀德拉西以前也常這麼跟我們說。

### (sub) DIAL_Z20#339
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#341
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#342
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然你能從莫瑞德人的鎖箱裡取東西，你肯定知道怎麼打開它們。我要那些密碼，艾薩克。

### (sub) DIAL_Z20#343
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那跟親手把自己的棺材蓋釘死沒兩樣。他們已經在找機會滅口了。山裡到處都是他們派來的刺客……

### (sub) DIAL_Z20#344
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 把密碼給我們，我們設法幫你清出一條南下的路。

### (sub) DIAL_Z20#345
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼要幫我？你們不怕我轉頭就把你們的下落告訴莫瑞德人？

### (sub) DIAL_Z20#346
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這問題你自己早就解決了。他們搞不好會請你去跟首領『友好』聊聊，說既往不咎，重重拍你一下肩膀，然後一刀砍下你的腦袋。殺光線人，向來是入侵行動的第一步。

### (sub) DIAL_Z20#347
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 入侵？別荒唐了！北境現在正打內戰呢，根本不可能發動什麼有組織的進攻。

### (sub) DIAL_Z20#348
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那為什麼要費工夫雇用凱許人？為什麼要在王國境內安插這麼多莫瑞德刺客？你沒那麼笨，艾薩克。把密碼給我們，我保證這件事絕不會傳到親王耳裡。

### (sub) DIAL_Z20#349
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。密碼有……五個？不對，六個。我記不清哪個對應哪個了，好像是陰影、蠟燭、陌生人……不對……骰子、蜘蛛、鑰匙，還有……什麼來著？  陰影……蠟燭……陌生人……蜘蛛……鑰匙……  抱歉，第六個我實在想不起來了。我知道有個莫瑞德人也老是記不住那一個，還把它刻在拉姆特附近的一塊墓碑上。

### (sub) DIAL_Z20#350
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#352
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#353
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說這個叫納戈的傢伙拿穀倉當據點。要是我們碰上他，該有什麼心理準備？

### (sub) DIAL_Z20#354
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 麻煩，就這麼簡單。他是個法師，武裝齊全，身上帶的金幣足夠雇上好幾十個凱許傭兵好幾個月。納戈遞出一袋四百枚金幣的時候，羅威差點沒當場暈過去……

### (sub) DIAL_Z20#355
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 羅威？

### (sub) DIAL_Z20#356
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是那穀倉的主人，一個老頭。要是納戈真有我猜的一半那麼狠，他很可能雇了那老頭替自己做事，不過我也說不準。

### (sub) DIAL_Z20#357
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#359
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#360
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你說的那個手藝通神的鑄劍匠在哪？我們或許也該把自己的兵器拿去修修。

### (sub) DIAL_Z20#361
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 高堡有間店叫「ñ戰ñ械坊ð」。路是遠了點，不過他們的手藝真的很不錯。

### (sub) DIAL_Z20#362
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#364
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#365
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 納戈放你走之前，最後一道命令是什麼？

### (sub) DIAL_Z20#366
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是我自己放自己走的。我當時覺得自己對莫瑞德人已經沒剩多少利用價值了，便照這個想法做了打算。他們要我從凱佛．艾勒斯庫克那裡取一顆紅寶石，送到某個指定的莫瑞德人鎖箱去，我這才意識到，他們是想一石二鳥。那名負責接應的莫瑞德人肯定是個刺客。他們打算殺了我，同時也順便抹去紅寶石送到誰手上的證據。

### (sub) DIAL_Z20#367
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000006  (DIAL_Z20#369)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb2=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483654 (GoodBye target)
- branches:
    - [flag 0x0030 in [43928..0]] -> node 4294901761
    - [flag 0x0031 in [44577..0]] -> node 4294901761
    - [flag 0x0032 in [45797..0]] -> node 4294901761
    - [flag 0x0033 in [47643..0]] -> node 4294901761
    - [flag 0x0034 in [49583..0]] -> node 4294901761
    - [flag 0x0035 in [50967..0]] -> node 4294901761
    - [flag 0x0036 in [52044..0]] -> node 4294901761
    - [flag 0x0037 in [52602..0]] -> node 4294901761
    - [flag 0x0038 in [53348..0]] -> node 4294901761
    - [flag 0x0039 in [53888..0]] -> node 4294901761
    - [flag 0x003a in [54941..0]] -> node 4294901761

### (sub) DIAL_Z20#370
- speaker=0  style=0
- effects:
    - event_bitmap_hi[3] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#371
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你剛才說『陌生人慶典』是慶祝哪位神明的？

### (sub) DIAL_Z20#372
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 豐饒女神——豐收的賜予者、大地之母、席爾班神。隨你叫哪個名字，反正都是同一回事。就是那個讓一堆醜老頭醜老太婆求她賜個醜娃、外加撐過冬天的小麥的娘們。要我說，我對她沒什麼用處。

### (sub) DIAL_Z20#373
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 附近有沒有她的神殿，還是……

### (sub) DIAL_Z20#374
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從艾格利一直往西走，到十字路口再往北。一棟有柱子的大白樓，聞起來跟妓院的房間差不多，很難錯過。

### (sub) DIAL_Z20#375
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#377
- speaker=0  style=0
- effects:
    - SET flag 0x0032=1
    - SET flag 0x002a=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#378
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼一說我倒想起來了，我們認識一個人說他在艾格利這兒輸給一個叫戴文的人玩ñ波基爾。您就是那位吧？

### (sub) DIAL_Z20#379
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那得看你為什麼問了，不是嗎？要是你想跟我玩上一兩把，那我就是這個人沒錯。可要是你朋友是想找幾個打手來，討回他堂堂正正輸給我的東西……

### (sub) DIAL_Z20#380
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在我看來，你贏的就是你的。我只是好奇您牌技怎麼樣。艾薩克說您這方面有種不尋常的天賦。

### (sub) DIAL_Z20#381
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 艾薩克？艾薩克說我有不尋常的天賦？這要不是五十步笑百步，我還真沒聽過比這更可笑的了。我們對局的時候，那小子簡直就像能看穿我腦子裡每一個念頭。他每次棄牌，都會朝他那幾個精靈朋友咧嘴一笑……

### (sub) DIAL_Z20#382
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 精靈朋友？像這位索爾加斯嗎？

### (sub) DIAL_Z20#383
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看那模樣，簡直能當親兄弟了。是啊，長得跟您這位朋友有點像，可他絕對不是精靈。他穿的是迪勒肯手下荒野游兵的衣服。莫瑞德人，錯不了。

### (sub) DIAL_Z20#384
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#386
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#387
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我對帕夏瓦牌比較熟，不過也跟沙瑪塔駐軍的人玩過幾次波基爾。您這邊有什麼特殊規則嗎？

### (sub) DIAL_Z20#388
- speaker=17  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [46153..0]] -> node 4294901761
    - [flag 0x0101 in [46619..0]] -> node 4294901761
- text: 規規矩矩來。全套牌，不用花色鬼牌，照默西規矩打。我唯一的特殊規則就是：你敢出老千，我就給你肝上開個窟窿透透氣。就這麼簡單。有興趣玩一局嗎？

### (sub) DIAL_Z20#389
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [46182..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#390
- speaker=0  style=0
- effects:
    - push return-address key 46221 (GoodBye target)
    - ACTION: popup-retry-state = max(state, 200)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#391
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#392
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#393
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，等等……我可不想被您說成騙子。我剛想起來，我身上一枚金幣都沒有。

### (sub) DIAL_Z20#394
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您腰間掛的那把劍看起來挺結實。我可以拿自己的劍下注，咱們就以劍賭劍。

### (sub) DIAL_Z20#395
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在風險太大了。我寧可等手頭有幾枚銀幣可以下注再說。

### (sub) DIAL_Z20#396
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#397
- speaker=0  style=0
- effects:
    - SET flag 0x0033=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#398
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 今天不行。您別多想，我只是覺得今天巴納斯神不太眷顧我。

### (sub) DIAL_Z20#399
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也經歷過那種手氣。有一次我替帕蘭克的儲妃辦事，正春風得意，在一間酒館裡跟一個倒楣的老海狗連贏了十五把ñ林嵐牌，他卻死不認輸。打到第十六把中途，他掏出一顆有我半個拳頭大的鑽石，說要拿它下注。我說我的錢不夠跟這麼大的注碼，他卻建議我把替儲妃保管的錢袋押上去。

### (sub) DIAL_Z20#400
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他怎麼知道那個錢袋的事？

### (sub) DIAL_Z20#401
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，是酒告訴他的……總之，我把錢袋押上去了。他亮出一張藍夫人、一張紅騎士、兩張黃侍從跟一張國王的弄臣，把我輸得一乾二淨。儲妃當然不太高興。我後來替那個母老虎當了兩年保鑣，才把錢袋裡輸掉的那筆錢還清。

### (sub) DIAL_Z20#402
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#404
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#405
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然當過儲妃的保鑣，劍術想必相當高超。或許您能教教我們兩招。

### (sub) DIAL_Z20#406
- speaker=17  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [48034..0]] -> node 4294901761
    - [flag 0x0101 in [49424..0]] -> node 4294901761
- text: 我自有幾手訣竅。人要不多學點本事，可活不了我這麼久。要是你們願意付錢，我可以指點你們幾招。一堂課八十枚金幣。有興趣嗎？

### (sub) DIAL_Z20#407
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [48063..0]] -> node 4294901840
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#408
- speaker=0  style=0
- effects:
    - advance in-game time by 9000
    - SET flag 0x1a5f=1
    - TAKE gold -800
    - RAISE Defense of party by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#409
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戴文朝門口揮了揮手。  他從吧台下抓起一把坑坑疤疤的薩拉曼卡劍，領著他們走進『陌生人』酒館前的空地，接著超前領路，穿過一片草地。地勢緩緩爬升，漸漸化為一片岩石坡面，散落著一堆年久失修、爬滿苔蘚的古老墓碑。  「艾格利的墓園？」@0在這名結實的傭兵身後停下腳步。「我不懂。」  「懂得怎麼自保，不只是懂得怎麼握劍，還得懂得腳往哪擺！」戴文半轉身子，一劍朝@0的臉揮去，逼得毫無防備的學生一個踉蹌，仰面摔在一塊半埋在土裡的石碑上。戴文猛地欺身向前，劍尖抵住@0的脖子。  「恭喜，」戴...

### (sub) DIAL_Z20#410
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#411
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#412
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我把腦子裡的叮噹聲誤當成錢袋裡的金幣聲了。恐怕我還是得婉拒您的提議。

### (sub) DIAL_Z20#413
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係。我想在咱們下次見面之前，我這招架的本事也不會忘。

### (sub) DIAL_Z20#414
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#415
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#416
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前我們負擔不起。或許改天吧。

### (sub) DIAL_Z20#417
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨時歡迎。

### (sub) DIAL_Z20#418
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#420
- speaker=0  style=0
- effects:
    - SET flag 0x003a=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#421
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩斯修道院有位修士，最近看見有幾批傭兵正穿越這片轄地，說他們看起來像是奎格人。您這名字『戴文尼烏斯』聽起來就是道地的奎格名字，我想您說不定知道些他們的事。

### (sub) DIAL_Z20#422
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我已經三年多沒跟奎格的儲妃或她那個混帳公公打交道了。就在史畢澤跟我一起登上儲妃的那艘戰艦——「ñ風暴ñ主宰」號——把勒比烏斯王的旗艦連人帶船一起擊沉的那天，我就把自己的通行證燒了。從那天起，我就只替自己一個人做事。就我自己。

### (sub) DIAL_Z20#423
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那您也不清楚為什麼會有這麼多傭兵在王國境內四處遊蕩？

### (sub) DIAL_Z20#424
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奎格傭兵要是超過三個聚在同一個地方，除非是有人花錢讓他們湊在一塊兒。那麼個小島，他們大半都曾殺過另一個傭兵的家人。錢給夠了，他們會暫時把私人恩怨擱一邊，先把差事辦完，再回頭自相殘殺。不管是誰在資助他們，手上肯定藏著一大筆紅寶石財富。

### (sub) DIAL_Z20#425
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紅寶石？

### (sub) DIAL_Z20#426
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 王國的金幣在奎格什麼都買不到，頂多換你在勒比烏斯王的地牢裡蹲一個月。紅寶石。他們只認這個。

### (sub) DIAL_Z20#427
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#429
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#430
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在路上遇到的一個人說，他在這附近看見一名莫瑞德人。不知道您有沒有見過他？

### (sub) DIAL_Z20#431
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他？我見過的莫瑞德人多得都能湊出一整支滾球聯賽了。幾週前一大票人才從這裡經過，三五成群地往南、往坦紐爾那個方向去。

### (sub) DIAL_Z20#432
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們有帶武器嗎？

### (sub) DIAL_Z20#433
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 武裝得跟戰神提斯的軍團一樣。看起來像是要去應徵商隊護衛的，可誰會雇他們啊？

### (sub) DIAL_Z20#434
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您有沒有看清楚他們哪個人的長相？

### (sub) DIAL_Z20#435
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們沒一個靠『陌生人』酒館夠近，讓我看清楚。這麼一想倒是挺古怪的。莫瑞德人偶爾闖進城鎮，通常都會跟當地人鬧出點動靜，證明自己才是這一帶的狠角色。可這批人就這麼大搖大擺地穿過鎮子，跟閱兵似的，好像是特意要讓誰看見他們走過去一樣。

### (sub) DIAL_Z20#436
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#438
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#439
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在找一位名叫史戴倫的稅務官。您知道慶典之後他去了哪嗎？

### (sub) DIAL_Z20#440
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 右邊數來第三塊墓碑，往下六呎，那就是史戴倫的下落。那位先生是被『收集者』殺害的。你們找他做什麼？

### (sub) DIAL_Z20#441
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他有一份舊文件，我想看看。

### (sub) DIAL_Z20#442
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那份文件說不定還鎖在他鎮上的辦公室裡。當然，前提是你們得先找到他的鑰匙。

### (sub) DIAL_Z20#443
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#445
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#446
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這附近有什麼值得留意的事嗎？

### (sub) DIAL_Z20#447
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡的ñ生意好像漸漸有起色了。我們已經有了第一個新的長住居民，瘋得跟老羅德里克王有得比。

### (sub) DIAL_Z20#448
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的？怎麼說？

### (sub) DIAL_Z20#449
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我發現他在墳場裡用手挖墳。他已經撬開了一副棺材，不過屍體大概早就腐化了，箱子裡什麼都沒有。我幫他清理乾淨之後，把他帶到一間屋子裡讓他躺下休息。我等會兒還得去看看他。你們要是想去探望他，他就在鎮子北邊出口前，右手邊最後一間屋子裡。

### (sub) DIAL_Z20#450
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#452
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#453
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩斯的修士跟我們說，奎格熱正在沿海一帶肆虐。您是奎格人，關於這種熱病，我們能做點什麼嗎？

### (sub) DIAL_Z20#454
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 對染病的人，什麼也做不了。為了你們自己著想，別走大路。一大群人染上熱病後，會不管身在何處都盲目奪路而逃，把身邊每個人都當成威脅。別靠近大路，應該就能避免撞上他們。

### (sub) DIAL_Z20#455
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#457
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#458
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 整座鎮子都歸您一個人，我倒挺意外您沒把其他店舖或屋子也開起來。

### (sub) DIAL_Z20#459
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我先按兵不動，等搞清楚這裡最後會怎麼樣再說。誰知道哪天會有人突然冒出來，要討回自己的產業。我可不想當那個扛黑鍋的傻瓜。要是大部分人夠精明，八成早就把屋子鎖上了，而我開鎖的本事也不怎麼樣。

### (sub) DIAL_Z20#460
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您知道誰開鎖比較在行嗎？

### (sub) DIAL_Z20#461
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有個怪人叫阿布克。我替奎格的儲妃卡珊卓辦事時遇見過他。我們登上一艘凱許船隻時發現了他。他幫忙撬開了幾只挑過的商貨箱子後，我們把他鎖進船艙底，打算獻給卡珊卓當禮物。可船一停靠帕蘭克，我們在船艙裡卻只找到一張字條，說要是以後還需要他效勞，可以去錫爾登找他。從那之後，開鎖的活兒我再沒找過別人。

### (sub) DIAL_Z20#462
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#464
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#465
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您提到一個叫史畢澤的人，跟您一起登上了那艘「ñ風暴ñ主宰」號。他是您的朋友嗎？他現在還在附近嗎？

### (sub) DIAL_Z20#466
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道嗎，明明只是路過，你問的問題可真不少……

### (sub) DIAL_Z20#467
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只是好奇。我在想他說不定知道些關於奎格人的事。

### (sub) DIAL_Z20#468
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他比我更有理由怕勒比烏斯王，見到奎格人肯定避之唯恐不及。不過你要是想找他玩骰子，我想他倒是很樂意跟你聊聊。我上次聽說，他人在坦紐爾。

### (sub) DIAL_Z20#469
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000007  (DIAL_Z20#471)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb1=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483655 (GoodBye target)
- branches:
    - [flag 0x003b in [55668..0]] -> node 4294901761
    - [flag 0x003c in [57639..0]] -> node 4294901761
    - [flag 0x003d in [58277..0]] -> node 4294901761
    - [flag 0x003e in [58907..0]] -> node 4294901761
    - [flag 0x003f in [60600..0]] -> node 4294901761
    - [flag 0x0040 in [61250..0]] -> node 4294901761
    - [flag 0x0041 in [62653..0]] -> node 4294901761
    - [flag 0x0042 in [64072..0]] -> node 4294901761

### (sub) DIAL_Z20#472
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#473
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說你是克朗多最安靜的小偷。證明給我看。

### (sub) DIAL_Z20#474
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 憑什麼？

### (sub) DIAL_Z20#475
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們接下來有件事可能需要極度的隱密行動，我們有些人正需要指點。你願意教我們一點你會的東西嗎？

### (sub) DIAL_Z20#476
- speaker=16  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [56214..0]] -> node 4294901761
    - [flag 0x0101 in [57379..0]] -> node 4294901761
- text: 價錢對了，我連親王頭上的王冠都能偷走，讓他半天都發現不了。聽起來挺有意思。一百二十枚金幣如何？你覺得這價錢合理嗎？

### (sub) DIAL_Z20#477
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [56243..0]] -> node 4294901880
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#478
- speaker=0  style=0
- effects:
    - SET flag 0x1a67=1
    - TAKE gold -1200
    - RAISE Stealth of party by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#479
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名小偷點了點頭。  他蹲下身，朝隧道深處指了指，要@3走過去再走回來。  「常見的毛病。你腳跟著地太重了，」林姆看著徒弟從黑暗中重新現身，說道。他抓住@3的腳，讓它左右擺動而不是前後踏地。「想像你的腳像波浪一樣，得讓它滾動——先從外側落地，再滾向中心。現在再走一趟過去再回來。咱們就這樣練，練到你抓到訣竅為止。」  又試了幾次後，@3漸漸抓到了竅門。「差別居然這麼大，真是不可思議。我自己幾乎都聽不見腳步聲了。」  「就是這樣，」林姆微笑著收下酬勞。「我得回去站崗了。你要是願意...

### (sub) DIAL_Z20#480
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#481
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#482
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這價錢聽起來合理，不過目前我也付不起。或許我改天再回來上這堂課？

### (sub) DIAL_Z20#483
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只要你找得到我，隨時歡迎。

### (sub) DIAL_Z20#484
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#485
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#486
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這數目倒也不算過分，不過我看現在還是先算了。

### (sub) DIAL_Z20#487
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是可惜。你其實挺需要上這堂課的。你走過來老遠，我就聽見腳步聲了。

### (sub) DIAL_Z20#488
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#490
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#491
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽說這下面有道閘門，連嘲弄幫的人都打不開。撬不開，也砸不壞鎖。是真的嗎？

### (sub) DIAL_Z20#492
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧。也許豬也會飛，誰說得準呢？你打聽這個做什麼？你可不是這下水道長大的人。話說回來，你是怎麼聽說的？

### (sub) DIAL_Z20#493
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，我算是自家人的朋友。我只是想知道有沒有人找到過它的鑰匙。

### (sub) DIAL_Z20#494
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就我所知沒有鑰匙，至少沒人講過有。要我說，那道『永恆之門』根本沒人打得開。不可能的事。

### (sub) DIAL_Z20#495
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#497
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#498
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道一件叫『拉蘇爾偶像』的東西嗎？

### (sub) DIAL_Z20#499
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那不就是唬小孩的故事嘛？說什麼一個小玩意能讓你凌駕死亡女神之上，之類的鬼扯。

### (sub) DIAL_Z20#500
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼會有人在克朗多找這東西？

### (sub) DIAL_Z20#501
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記得那故事裡有這麼一段，說是被某個凱許人藏在下水道深處某個秘密角落，還是什麼的，差不多這意思。不過那玩意兒不是真的，我敢保證。要是真有，嘲弄幫早找到了。

### (sub) DIAL_Z20#502
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#504
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#505
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你身上該不會剛好有多餘的開鎖工具吧？

### (sub) DIAL_Z20#506
- speaker=16  style=0
- branches:
    - [flag 0x7537 in [59547..0]] -> node 393222
    - [always] -> node 0 (no jump)
- text: 也許有。那就得看你能拿什麼來換了，不是嗎？

### (sub) DIAL_Z20#507
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 下次你落到城衛手裡的時候，來份王室赦免狀怎麼樣？

### (sub) DIAL_Z20#508
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哦，那可真好啊。順便再把親王的王宮也給我怎麼樣！你剛才那套鬼話，我得腦子進水又缺根筋才會信。你前腳一走上大道，這事後腳就忘得一乾二淨了。你得拿點更實在的東西來。

### (sub) DIAL_Z20#509
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那金子呢？

### (sub) DIAL_Z20#510
- speaker=16  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [59684..0]] -> node 4294901761
    - [flag 0x0101 in [60269..0]] -> node 4294901761
- text: 這才像話。二十五枚金幣。要不要？

### (sub) DIAL_Z20#511
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [59713..0]] -> node 4294901785
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#512
- speaker=0  style=0
- effects:
    - GIVE item 'P' cond=12 to member#2 (cost 250)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#513
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 成交。我們走之前就把錢給你。

### (sub) DIAL_Z20#514
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你也不介意我拿到錢之前先不交開鎖工具吧？公平交易嘛，不是嗎？

### (sub) DIAL_Z20#515
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#516
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#517
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 交易取消。看來我身上少了幾枚金幣。這事你該不會知道點什麼吧？

### (sub) DIAL_Z20#518
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可不是扒手，大爺。這活兒超出我的本事範圍，雖然要是能在夜主面前多長點臉面，我倒也不介意。我專攻的是順手牽羊的大件貨。

### (sub) DIAL_Z20#519
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#520
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#521
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我還是算了。這價錢我都能買一整套開鎖工具外加一週的口糧了。你這行情，當商人是絕對成不了氣候的。

### (sub) DIAL_Z20#522
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也沒那個志向。要是你不介意，我還是比較喜歡待在這下面。

### (sub) DIAL_Z20#523
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#525
- speaker=0  style=0
- effects:
    - GIVE item ']' cond=1 to member#2 (cost 0)
    - SET flag 0x1a6b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#526
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們跟萊斯爾．瑞格談過了，他要我轉告你，正直人的猜測已經證實，不過他說爬行者並不是喬科．瑞德本……

### (sub) DIAL_Z20#527
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這下總算鬆了口氣。至少現在能確定他們是打哪冒出來的了。他還說了別的嗎？

### (sub) DIAL_Z20#528
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他提到了什麼獎賞？

### (sub) DIAL_Z20#529
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他要的那枚印璽我會給你，不過要我說，這價碼未免也太寒酸了。要是我，起碼也得要顆亮晶晶的寶石，還得是上等貨色。

### (sub) DIAL_Z20#530
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#532
- speaker=0  style=0
- effects:
    - GIVE item '>' cond=1 to member#2 (cost 0)
    - SET flag 0x003b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#533
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你鑰匙圈上有幾把鑰匙？

### (sub) DIAL_Z20#534
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好小偷才不需要那玩意兒。誰家的窗板卡了彈簧、誰家的門沒閂好，我一眼就看得出來。眼力好得很。依我看，不靠這些東西反倒更厲害。我大概是正直人這輩子見過最厲害的小偷，而且我早就知道自己是最安靜的那個。

### (sub) DIAL_Z20#535
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是ñ這樣嗎？真有意思。那，你知不知道怎麼找到『黃比爾』？也許他能賣我們幾把鑰匙。

### (sub) DIAL_Z20#536
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 比爾？你說的是『老比爾』？他一個月前左右，就被爬行者派來的一群流氓給做掉了。

### (sub) DIAL_Z20#537
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真可惜，他算是個有自己一套的好人……那還有誰能弄到鑰匙？

### (sub) DIAL_Z20#538
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我ñ倒是有一把鑰匙……

### (sub) DIAL_Z20#539
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記得你剛才不是說好小偷不需要這玩意兒嗎。

### (sub) DIAL_Z20#540
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是ñ不需要，只是碰巧手邊有一把。是在一具屍體旁邊撿到的，那人穿得像死亡公會的人。長相挺醜的，不過話說回來，半邊腦袋都被砸爛了……

### (sub) DIAL_Z20#541
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 細節就免了吧。這把夜鷹會的鑰匙你要多少錢？

### (sub) DIAL_Z20#542
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不用錢，直接給你。我可不想帶著這東西到處走，也不想因此招來厄運。拿去吧。以後可別說林姆什麼都沒替你做過。

### (sub) DIAL_Z20#543
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#545
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#546
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定正直人已經死了？

### (sub) DIAL_Z20#547
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夜主是這麼說的。

### (sub) DIAL_Z20#548
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他以前有一枚護身符，據說……他一直帶著求好運。有人知道那東西後來怎麼樣了嗎？

### (sub) DIAL_Z20#549
- speaker=16  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [63238..0]] -> node 4294901761
    - [flag 0x0101 in [63778..0]] -> node 4294901761
- text: 需要點額外的好運氣，嗯？誰不需要呢？碰巧那護身符就在我手上。夜主在我從爬行者的兩個打手手裡救了他一命之後，順手塞給我的。他覺得這東西不值幾個錢，不過我倒覺得不然。三百枚金幣，它就是你的了？你覺得如何？

### (sub) DIAL_Z20#550
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [63267..0]] -> node 4294902060
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#551
- speaker=0  style=0
- effects:
    - SET flag 0x1a6d=1
    - bind speaker-name slot (kind=1 sub=5)
    - GIVE item '\x05' cond=8 to member#3 (cost 3000)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#552
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這數目簡直打得我肉痛。好吧，這護身符我要了。

### (sub) DIAL_Z20#553
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 成交！相信我，絕不會讓你失望。

### (sub) DIAL_Z20#554
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#555
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#556
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我還是算了吧。

### (sub) DIAL_Z20#557
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這是想反悔已經談成的交易？想耍什麼花招？

### (sub) DIAL_Z20#558
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是耍花招。我只是身上的錢沒我想的那麼多。

### (sub) DIAL_Z20#559
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#560
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#561
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這價碼太傷人了。不成交。

### (sub) DIAL_Z20#562
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是您的損失了，大人。這可是我這輩子見過數一數二的好東西，不過人總有說不的權利，是吧？這不就是『大自由』的真諦嗎？

### (sub) DIAL_Z20#563
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#565
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#566
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你有沒有從那些冒充嘲弄幫的人身上搜到什麼東西？

### (sub) DIAL_Z20#567
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們身上沒帶什麼值錢玩意兒，不過確實找到過幾件不錯的東西。今早我才剛翻過一具在海門附近發現的屍體。

### (sub) DIAL_Z20#568
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是價錢合適，我或許有興趣跟你買下那批贓物。

### (sub) DIAL_Z20#569
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？那我的價錢是一百枚金幣。

### (sub) DIAL_Z20#570
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一百枚金幣？你剛才不是說他們身上沒帶什麼值錢的？

### (sub) DIAL_Z20#571
- speaker=16  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [64710..0]] -> node 4294901761
    - [flag 0x0101 in [65259..0]] -> node 4294901761
- text: 看來對你來說倒挺值錢的，我說它值一百枚金幣，一個子兒都不能少。成交嗎？

### (sub) DIAL_Z20#572
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [64739..0]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#573
- speaker=0  style=0
- effects:
    - SET flag 0x1a6e=1
    - GIVE item 'x' cond=27 to member#2 (cost 1000)
    - GIVE item 'T' cond=3 to member#2 (cost 0)
    - GIVE item 'w' cond=8 to member#2 (cost 0)
    - GIVE item 'w' cond=8 to member#2 (cost 0)
    - GIVE item 'w' cond=8 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#574
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 簡直是搶劫，不過我們買了。

### (sub) DIAL_Z20#575
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那好。我去把包袱拿給你。

### (sub) DIAL_Z20#576
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#577
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#578
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 交易取消。看來我身上少了幾枚金幣。這事你該不會知道點什麼吧？

### (sub) DIAL_Z20#579
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可不是扒手，大爺。這活兒超出我的本事範圍，雖然要是能在夜主面前多長點臉面，我倒也不介意。我專攻的是順手牽羊的大件貨。

### (sub) DIAL_Z20#580
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#581
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#582
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我都不確定你有什麼東西，這價錢未免開得太高了。抱歉。

### (sub) DIAL_Z20#583
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說是打算穩妥行事了？可惜。摸起來分量還挺不錯的。

### (sub) DIAL_Z20#584
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000008  (DIAL_Z20#586)
- speaker=2  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1ead=1
    - bind speaker-name slot (kind=0 sub=2)
    - push return-address key 2149483656 (GoodBye target)
- branches:
    - [flag 0x0043 in [34..1]] -> node 4294901761
    - [flag 0x0044 in [1323..1]] -> node 4294901761
    - [flag 0x0045 in [1843..1]] -> node 4294901761
    - [flag 0x0046 in [3508..1]] -> node 4294901761
    - [flag 0x0047 in [5529..1]] -> node 4294901761
    - [flag 0x0048 in [7008..1]] -> node 4294901761

### (sub) DIAL_Z20#587
- speaker=0  style=0
- effects:
    - SET flag 0x0044=1
    - SET flag 0x0045=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#588
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們需要你為我們占卜一番。哪條路能引我們走向安全？

### (sub) DIAL_Z20#589
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你的答案我無需再問星辰，自你離去以來，我已凝望它連日不輟。迪勒肯的大軍正雲集於王國邊境，克里艾達、達爾格拉斯與歐爾杜三個氏族的旌旗，正在拉格蘭姆附近的原野上飄揚。我不會建議你們穿越世界之齒、取道北衛城或高堡這兩座王國要塞的南向路徑；納拉布必定親自坐鎮那裡。

### (sub) DIAL_Z20#590
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 納拉布已經背棄了那頭老狼。薩薩戈斯如今被他的氏族團團圍住。他不會來煩我們了。

### (sub) DIAL_Z20#591
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管如此，各方軍隊正在集結，你在其中找不到任何盟友。你也不能穿越大北山脈、取道莫拉埃林。莫萊伍夫正與六賢者聯手，確保綠心氏族的舊部無一能從艾爾凡達邊緣逃脫。

### (sub) DIAL_Z20#592
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓林絲克拉格瑪吞噬他的靈魂吧！他以為我們逃不了，就會加入他那該死的行軍？！

### (sub) DIAL_Z20#593
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再說一次，你唯一的逃生之路就在因克林德爾山口。不知是何緣故，六賢者放任那裡的積雪消融。也許他們正忙著把法力集中在別處。

### (sub) DIAL_Z20#594
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#596
- speaker=0  style=0
- effects:
    - SET flag 0x004b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#597
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這幾位如今效忠迪勒肯的六賢者，出身哪個氏族？也許能設法讓他們倒戈。

### (sub) DIAL_Z20#598
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們的法術強大，夫君，遠超乎我的力量所及。他們自稱承襲『織法者』這個古老的頭銜，卻與我們在艾爾凡達的法術同源截然不同。有人懷疑他們出身自蛇族，但我已許久未曾觸及北境那些族類的心念了。

### (sub) DIAL_Z20#599
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#601
- speaker=0  style=0
- effects:
    - SET flag 0x0046=1
    - SET flag 0x1a71=1
    - RAISE Casting Acc of member#3 by 3840
    - advance in-game time by 7200
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#602
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們得神不知鬼不覺地穿越因克林德爾山口，恐怕得借助妳的幻術。就跟我當初初次逃脫迪勒肯手下時，妳施展的那種幻術一樣。

### (sub) DIAL_Z20#603
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你不知道自己在要求什麼……那個法術耗費心力極大，施完之後我整整一個月都虛弱得使不出半點力氣！我不能跟你走這條路，因為我認為這是條懦夫之路！

### (sub) DIAL_Z20#604
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文侷促不安地動了動身子。  雖然聽不懂那刺耳的莫瑞德語在說些什麼，他還是感覺得出戈拉斯跟這名陌生莫瑞德女子交談的語氣——不管他們在說什麼，顯然意見不合。  「她會跟你談，」戈拉斯厲聲說道，滿臉怒色地大步走向窗邊。「仔細聽她說的話。」  「可我要怎麼聽懂她說什麼？」歐文說。「我不會莫瑞德語。」  「Weyoda aldeweynn，」庫利奇低聲說道。她輕盈地滑步到他身邊，溫柔地握起他的手，輕輕撫摸著。「Weyoda aldeweynn，Owynna……你會聽懂的。」

### (sub) DIAL_Z20#605
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 彷彿過了好幾天。  「發生了什麼事？」歐文搖了搖頭，驚訝地發現自己竟躺在地上。戈拉斯跟庫利奇正興致盎然地盯著他，看著他漸漸恢復意識。「妳對我施了什麼法術？」  「妳教給你的東西非同尋常，」庫利奇答道，扶著歐文站起身。「從此以後你會聽懂我對你說的一切話，你也會發現自己施法的本領比以前強上許多。到附近走走吧。我跟我丈夫還有些事要商量。」

### (sub) DIAL_Z20#606
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#608
- speaker=0  style=0
- effects:
    - SET flag 0x0047=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#609
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們碰上莫萊伍夫跟六賢者，我希望能有更充分的準備去面對他。

### (sub) DIAL_Z20#610
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我曾煉製過一道法術，或許能教給這孩子。那是一種幻術，能扭曲周遭人的感知，讓他們看不出你的真面目，反而把你當成他們想進入的那個地區的居民。這道法術是特地為哈勒克鎮量身打造的，說不定在你們對付莫萊伍夫時派得上用場。你若有八百枚銀幣，我便可以教給歐文，或是等值的金幣也行，好讓我去買所需的銀子。

### (sub) DIAL_Z20#611
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳要為此收我們的錢？

### (sub) DIAL_Z20#612
- speaker=12  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [4363..1]] -> node 4294901761
    - [flag 0x0101 in [5295..1]] -> node 4294901761
- text: 就算我這麼做也理所應當，不過我要銀子，是因為煉製這道法術本身就需要它。你們身上有這筆錢嗎？

### (sub) DIAL_Z20#613
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [4392..1]] -> node 4294901840
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#614
- speaker=0  style=0
- effects:
    - SET flag 0x1a72=1
    - TAKE gold -800
    - bind speaker-name slot (kind=3 sub=3)
    - set combatant bitmap bit (sel=5 bit=35)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#615
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這筆錢給你。該做的就去做吧。

### (sub) DIAL_Z20#616
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很好。    歐文，過來一下。

### (sub) DIAL_Z20#617
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不會又昏倒在地上吧？

### (sub) DIAL_Z20#618
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這堂課你會一直站著，不會倒下。  我們開始吧……

### (sub) DIAL_Z20#619
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
- branches:
    - [always] -> node 0 (no jump)
- text: 時間流逝。  歐文腦子裡塞滿了法術的種種細節，一句接一句地把咒語複誦給庫利奇聽。她見他已經掌握了所有細節，滿意地點了點頭。  「你學得很好，」她說。「去休息一會兒吧。」

### (sub) DIAL_Z20#620
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#621
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#622
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這超出我們付得起的範圍了。我們得另外想辦法弄到銀子才行。

### (sub) DIAL_Z20#623
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那也是無可奈何。我相信等你們回來時，我還不會忘了這法術。

### (sub) DIAL_Z20#624
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#625
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#626
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這筆錢都夠我們買通莫萊伍夫的守衛了。我們不能把錢財當糠秕一樣揮霍。

### (sub) DIAL_Z20#627
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就這樣吧。你自己拿主意吧。

### (sub) DIAL_Z20#628
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#630
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#631
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳還有沒有別的法術能教我？要是準備得更充分一些，我這趟出行也能安心一點。妳有沒有能讓我們自保的法術？

### (sub) DIAL_Z20#632
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有一道法術我或許能教你。不過同樣的，我需要你的銀子。

### (sub) DIAL_Z20#633
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我早猜到了。妳需要多少？

### (sub) DIAL_Z20#634
- speaker=12  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [6038..1]] -> node 4294901761
    - [flag 0x0101 in [6767..1]] -> node 4294901761
- text: 三千枚銀幣應該就夠我用了。你願意付這個價錢嗎？

### (sub) DIAL_Z20#635
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [6067..1]] -> node 4294902060
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#636
- speaker=0  style=0
- effects:
    - TAKE gold -3000
    - bind speaker-name slot (kind=3 sub=3)
    - set combatant bitmap bit (sel=5 bit=20)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#637
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就依妳。這回的方式會跟之前一樣嗎？

### (sub) DIAL_Z20#638
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大致相同，不過這次我要你閉上眼睛。現在，專心……

### (sub) DIAL_Z20#639
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
- branches:
    - [always] -> node 0 (no jump)
- text: 時間流逝。  歐文腦子裡塞滿了法術的種種細節，一句接一句地把咒語複誦給庫利奇聽。她見他已經掌握了所有細節，滿意地點了點頭。  「你學得很好，」她說。「去休息一會兒吧。」

### (sub) DIAL_Z20#640
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#641
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#642
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們身上沒帶這麼多錢。

### (sub) DIAL_Z20#643
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等你們回來，我還是可以教你們這法術。

### (sub) DIAL_Z20#644
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#645
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#646
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 太貴了。這筆錢拿去買盔甲，說不定更能讓我們有備無患。

### (sub) DIAL_Z20#647
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看你遲早會改變主意的，年輕的人類，不過就依你的意思吧。

### (sub) DIAL_Z20#648
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#650
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#651
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 感謝妳救了我們的命。要不是妳出手相助，我跟我這位同伴恐怕早已死在迪勒肯手中了。

### (sub) DIAL_Z20#652
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我確實不願見你們喪命，不過你們最近那次脫身，可不是我的功勞。你為什麼會覺得那跟我有關？

### (sub) DIAL_Z20#653
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當時涉及了法術。我們被囚禁時，有人解開了我們的束縛。我還以為是妳做的。

### (sub) DIAL_Z20#654
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有別人在暗中幫你，戈拉斯。不是我。換作是我，也會想弄清楚那人是誰，動機又是什麼。

### (sub) DIAL_Z20#655
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000009  (DIAL_Z20#657)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eae=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483657 (GoodBye target)
- branches:
    - [flag 0x0049 in [7690..1]] -> node 4294901761
    - [flag 0x004a in [8305..1]] -> node 4294901761
    - [flag 0x004b in [9194..1]] -> node 4294901761
    - [flag 0x004c in [10216..1]] -> node 4294901761

### (sub) DIAL_Z20#658
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#659
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 裂界機那邊的法師跟我說，那道門好像出了故障。他們需要一個原本存放起來的零件。

### (sub) DIAL_Z20#660
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那道門還能運作嗎？

### (sub) DIAL_Z20#661
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不行。就在法師派我們來之前故障的，靠他們手上現有的東西修不好。他們說需要那些存放在你這裡的裝置。

### (sub) DIAL_Z20#662
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那東西藏在一只箱子裡，用咱們……特製的……鎖鎖著。密碼是『勝利』。你會在這片林子西南角附近的一座峽谷裡找到，箱子就在那兒。

### (sub) DIAL_Z20#663
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#665
- speaker=0  style=0
- effects:
    - SET flag 0x1f6d=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#666
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 因克林德爾橋的守衛把從王國搶來的貨物給擋了回去。我們需要今日的通行密碼，才能授權貨物過橋。

### (sub) DIAL_Z20#667
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們要把貨運去哪？

### (sub) DIAL_Z20#668
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟我們一起，運回薩薩戈斯的集結地。那邊急需這些補給，好多飢餓的士兵等著吃飯呢。

### (sub) DIAL_Z20#669
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的士兵比他們還餓。你們有新的命令：先把貨運到哈勒克停下，再繼續北上。我們會取走需要的部分。

### (sub) DIAL_Z20#670
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看迪勒肯不會太高興。

### (sub) DIAL_Z20#671
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯去死吧！他要是不服氣，大可親自來這裡取貨，但這批東西我要定了！  告訴橋上的人，你是屠蛇者。我要立刻拿到這批補給。

### (sub) DIAL_Z20#672
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#674
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#675
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 令尊表達了憂慮，說他對六賢者的動向了解得不夠充分。他要求立即呈報。

### (sub) DIAL_Z20#676
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 父親跟我一樣清楚六賢者是怎麼辦事的！他們對我彙報的，頂多是抱怨住處太冷、伙食不合口味！我不信任他們的動機。他們只跟他們的首領交談，而那位首領也只在自己願意的時候才會出現。要是由我決定，我會把他們全趕到雪地裡，讓他們自己凍死算了。

### (sub) DIAL_Z20#677
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可是進攻北衛城，他們不是至關重要嗎？

### (sub) DIAL_Z20#678
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 北衛城本身沒什麼要緊的。真正讓我在意的，是那背後的目標。要是穆爾曼達穆斯真回到我們陣中，那會發生什麼事？

### (sub) DIAL_Z20#679
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那怎麼可能？穆爾曼達穆斯已經死了。

### (sub) DIAL_Z20#680
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 信使，我父親的問題我自會回答，但我可不是來滿足你的好奇心的。

### (sub) DIAL_Z20#681
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#683
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#684
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們一直找不到糧食。我們這支隊伍裡其他人也快餓壞了。要維繫這幾十個飢餓傭兵的忠誠，恐怕會愈來愈難……

### (sub) DIAL_Z20#685
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們一定得找到糧食！王國的士兵找到了我們藏在這裡的補給。他們一定是……察覺到……我們正在逼近了。

### (sub) DIAL_Z20#686
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000010  (DIAL_Z20#688)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb8=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483658 (GoodBye target)
- branches:
    - [flag 0x004d in [10666..1]] -> node 4294901761
    - [flag 0x004e in [11759..1]] -> node 4294901761
    - [flag 0x004f in [12064..1]] -> node 4294901761
    - [flag 0x0050 in [13007..1]] -> node 4294901761
    - [flag 0x0051 in [14001..1]] -> node 4294901761

### (sub) DIAL_Z20#689
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#690
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳跟一頭怪物同床共枕，莉艾蘭。告訴我們一條路，我們便趁他熟睡時取他性命。指給我們一條密道，我們便飲他之血，替莫瑞德人贖回這份血誓之約。

### (sub) DIAL_Z20#691
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們又會落得什麼下場？莫萊伍夫會立刻接替他父親的位置，拿我們的背叛當柴火，燒起追兵的怒火。迪勒肯必須打完這一仗，讓我們的同胞跟他一起在異鄉的土地上為了徒勞的理由送命。唯有如此，那些還在觀望、等著加入他的其他氏族，才會明白我們無法在一面死亡的旗幟下團結一致。

### (sub) DIAL_Z20#692
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 穆爾曼達穆斯當年在戰場上背叛了我們，他們的失敗根本沒讓他們學到教訓，這次也不會有什麼不同的結局！

### (sub) DIAL_Z20#693
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們想要的其實是同一件事，戈拉斯，只不過我打算奪取你所畏懼的那個位子。等迪勒肯倒在王國的劍下之後，我要登上北境諸國的王座。由我來領導。

### (sub) DIAL_Z20#694
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽妳這麼說，我還真不知道該笑還是該哭，莉艾蘭，不過比起他那個雜種兒子莫萊伍夫，我還是更屬意妳。

### (sub) DIAL_Z20#695
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#697
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#698
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很少有機會去納拉爾之肋。我都忘了它的位置在哪。

### (sub) DIAL_Z20#699
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就在這裡以南，直線距離離薩薩戈斯正門只有幾分鐘路程。我也已經好一陣子沒去過了。

### (sub) DIAL_Z20#700
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#702
- speaker=0  style=0
- effects:
    - SET flag 0x0051=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#703
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還是得到王國去尋求援助。亞魯莎親王的軍隊必須在那裡迎擊迪勒肯才行。

### (sub) DIAL_Z20#704
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這恐怕比你想的還要棘手。迪勒肯已經下令要納拉布的人頭。

### (sub) DIAL_Z20#705
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼會這樣？要不是納拉布，我根本還在王國境內逍遙自在。

### (sub) DIAL_Z20#706
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道他心裡燃著什麼樣的火，但那火冒出的煙，在我看來跟瘋狂沒兩樣。納拉布已經召集他的氏族包圍我們，儘管他們在這裡對我們構不成什麼威脅。六賢者能輕易碾碎他們，不過他們暫時還是能困住我們一陣子。

### (sub) DIAL_Z20#707
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 納拉布越是耍蠢，我們就越能爭取到時間，不過我倒寧願他挑別的地方耍。真沒有辦法繞過他的氏族嗎？

### (sub) DIAL_Z20#708
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 除非你懂得怎麼從納拉爾之肋召來黑暗之神的怒火，否則在六賢者抵達之前，我實在想不出別的辦法。

### (sub) DIAL_Z20#709
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#711
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#712
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯這麼做究竟是為了什麼目的？光是攻打王國邊境的一座城堡，根本得不到什麼好處。

### (sub) DIAL_Z20#713
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他告訴那些歸附他的人，穆爾曼達穆斯還活著，被囚禁在王國境內，他打算把他救出來。當年在賽瑟儂，沒有人親眼見到他死去。

### (sub) DIAL_Z20#714
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這對迪勒肯又有什麼好處？退位讓穆爾曼達穆斯重新登上王座？要我相信迪勒肯是那種懷念舊主的人，還不如相信妳是死亡女神本人來得容易。

### (sub) DIAL_Z20#715
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來莫瑞德人裡頭，總算還有一個懂得動腦筋的。我自己也一直在納悶他到底想圖什麼，唯一想得出的結論是——他打算以救出穆爾曼達穆斯為條件，從他那裡換取些什麼。穆爾曼達穆斯法力高強，甚至勝過如今為迪勒肯效力的六賢者。也許他相信自己能學到我們這位前領袖力量的秘密。

### (sub) DIAL_Z20#716
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#718
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#719
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯的法師是從哪來的？我第一次離開北境之前，就在哈勒克聽人提起過他們。他們會參與謀劃嗎？

### (sub) DIAL_Z20#720
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不只如此。他們常跟他徹夜密謀，開的會連我都不再有資格出席。當初正是他們建議要滅絕你們部族的。他們談起出身低微的人，彷彿那些人的性命一文不值。他們似乎活著就是為了那些盤根錯節的陰謀詭計，除此之外，什麼都無關緊要。

### (sub) DIAL_Z20#721
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們買酒的時候，用的是什麼樣的錢幣？

### (sub) DIAL_Z20#722
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不用錢幣。他們身上只帶寶石，品質低劣的紅寶石。丟起來就像撒種子一樣隨意。

### (sub) DIAL_Z20#723
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們住在薩薩戈斯嗎？

### (sub) DIAL_Z20#724
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟迪勒肯在一起的時候是。眼下他們正跟莫萊伍夫南下前往哈勒克。我想他們是打算把那些不願加入迪勒肯陣營的你們族人一併圍捕。

### (sub) DIAL_Z20#725
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000011  (DIAL_Z20#727)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb4=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483659 (GoodBye target)
- branches:
    - [flag 0x0052 in [15154..1]] -> node 4294901761
    - [flag 0x0053 in [16408..1]] -> node 4294901761
    - [flag 0x0055 in [17672..1]] -> node 4294901761
    - [flag 0x0056 in [18325..1]] -> node 4294901761
    - [flag 0x0057 in [19512..1]] -> node 4294901761
    - [flag 0x0058 in [21067..1]] -> node 4294901761
    - [flag 0x0059 in [22846..1]] -> node 4294901761
    - [flag 0x005a in [25241..1]] -> node 4294901761
    - [flag 0x005b in [26458..1]] -> node 4294901761
    - [flag 0x005c in [27074..1]] -> node 4294901761
    - [flag 0x005d in [27930..1]] -> node 4294901761

### (sub) DIAL_Z20#728
- speaker=0  style=0
- effects:
    - SET flag 0x1f6e=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#729
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看起來眼熟嗎？

### (sub) DIAL_Z20#730
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不能說眼熟。我該認識你嗎？

### (sub) DIAL_Z20#731
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是問我這個人，是問我這張臉。仔細看看我。你確定不認識哪個長得跟我一樣的人？

### (sub) DIAL_Z20#732
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒說沒見過長得像你的人，我只是說沒見過你本人。  你要找的那個人叫萊斯爾．瑞格。他跟你有親戚關係嗎？

### (sub) DIAL_Z20#733
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不確定。我對父親一無所知，母親也在我年幼時就過世了。他們倆任何一方都有可能還有別的孩子。我只是想跟他談談，看看我們是不是有什麼共同的過去。

### (sub) DIAL_Z20#734
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那也罷。  他最近在跑一趟差事，不過沒告訴我是什麼事，也沒說是誰雇他的。他說要是有一陣子人間蒸發了，多半是躲在黑沼鎮，大概就在那邊的公用儲物倉裡。你要是到了那附近，就喊一聲『伊凡叫我來的』。他就會現身。不過我先警告你，麻煩事常常跟著他一起出現。你最好做好打架的心理準備。

### (sub) DIAL_Z20#735
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來挺耳熟的。就算不是我親兄弟，至少也是個近親堂表兄弟。

### (sub) DIAL_Z20#736
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#738
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#739
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這附近有沒有機會弄點吃的？

### (sub) DIAL_Z20#740
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是連這個都辦不到，這酒館也算不上什麼酒館了。是要在這吃，還是想帶點乾糧上路？

### (sub) DIAL_Z20#741
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要帶上路的。要是你們的廚子能備一批乾糧，那就再好不過了。

### (sub) DIAL_Z20#742
- speaker=19  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [16830..1]] -> node 4294901761
    - [flag 0x0101 in [17416..1]] -> node 4294901761
- text: 那就這麼說定了，一份七枚金幣。還要嗎？

### (sub) DIAL_Z20#743
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [17073..1]] -> node 393216
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#744
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒理由不要啊。這價錢挺合理的。

### (sub) DIAL_Z20#745
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那好。我這就去催達芙妮動手。她一會兒就能給你們備好。

### (sub) DIAL_Z20#746
- speaker=0  style=0
- effects:
    - SET flag 0x1eb4=1
    - END conversation, result=65534

### (sub) DIAL_Z20#747
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想要的跟我能拿出來的，現在恐怕是兩碼子事了。我的錢弄丟了。

### (sub) DIAL_Z20#748
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是這是哪個學生的惡作劇，我可不會上當。你們別想白吃這頓飯。

### (sub) DIAL_Z20#749
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的不是惡作劇。我們改天再來拿吧。

### (sub) DIAL_Z20#750
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#751
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 仔細想想，我大概還是把錢省下來比較好。我有不少開銷得考慮。

### (sub) DIAL_Z20#752
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我倒希望你的金子能當飯吃。不然路上餓肚子的時候，它可頂不了用。

### (sub) DIAL_Z20#753
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#755
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#756
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這所修道院的名聲越來越響了吧？我聽過不少關於它的傳聞。

### (sub) DIAL_Z20#757
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽過的傳聞，你恐怕沒聽過。這地方確實培養出幾個優秀的頭腦，沒錯，可它同時也是貴族們打發礙眼兒子的垃圾場。裡頭大半都是些沒出息的紈褲子弟。

### (sub) DIAL_Z20#758
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那少數幾個不是的呢？

### (sub) DIAL_Z20#759
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那幾個特別的，都是些出色的人才。要是伊夏神保佑，將來都能成為出色的公爵、男爵之類的人物。他們個個都成了了不起的戰術家。這正是這所修道院的專長。

### (sub) DIAL_Z20#760
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#762
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#763
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們稍早發現一件挺古怪的東西。是一座龍的雕像，孤零零地立在荒郊野外，就杵在一條小涵洞裡，周圍什麼都沒有。

### (sub) DIAL_Z20#764
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們找到老馬拉克的『戰利品』了？牠可不是一直都在那荒郊野外的。以前牠就在馬拉克十字鎮大街不遠處，可鎮子後來搬走了，就把可憐的老馬拉克丟在那自生自滅了。

### (sub) DIAL_Z20#765
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們為什麼把牠留在那？

### (sub) DIAL_Z20#766
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唯一覺得馬拉克是個英雄的，大概就只有馬拉克自己了。出身低微的百姓對他可是恨之入骨。不管怎樣，後來鎮子開始遭到從夢海一帶北上的凱許劫掠者襲擊，大夥便決定把鎮中心搬到伊夏修道院的轄地裡去。搬過去之後，劫掠者就再也不敢動這座鎮子了，畢竟伊夏修士會最初就是從凱許來的。後來情勢稍微穩定下來，大家便決定把那座雕像留在原地，任由它被大自然收回去。奇怪的是，最近去看過它的人都說了些古怪的事……說那雕像會跟他們說話。

### (sub) DIAL_Z20#767
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#769
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#770
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡有沒有存放旅客遺失物品的地方？

### (sub) DIAL_Z20#771
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有時候會，要是我覺得有意思，或是看起來失主會回來找。怎麼，你以前在這弄丟過什麼東西嗎？

### (sub) DIAL_Z20#772
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是，我只是好奇你有沒有撿到什麼有意思的東西，而且你覺得原主大概不會再回來認領了。要是有，我或許有興趣跟你收購。

### (sub) DIAL_Z20#773
- speaker=19  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [20209..1]] -> node 4294901761
    - [flag 0x0101 in [20816..1]] -> node 4294901761
- text: 把吧台底下清一清，對我倒也沒什麼壞處。那裡確實有幾樣東西。這樣吧，我連看都不看，一整批賣你……就說……五十枚金幣。成交嗎？

### (sub) DIAL_Z20#774
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [20238..1]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#775
- speaker=0  style=0
- effects:
    - SET flag 0x1a83=1
    - GIVE item '\x82' cond=100 to member#2 (cost 500)
    - GIVE item 'M' cond=1 to member#2 (cost 0)
    - GIVE item 'V' cond=4 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#776
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 成交，老闆。我全要了。

### (sub) DIAL_Z20#777
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我得先把東西收集起來。你們離開前我會給你們，順便把這筆帳算進你們的消費裡。

### (sub) DIAL_Z20#778
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#779
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#780
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你那吧台底下該不會也剛好有幾枚多餘的金幣吧？

### (sub) DIAL_Z20#781
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 錢弄丟了？這樣啊。反正我看明天之前也不會有人回來認領這批東西。你晚點再來找我吧。

### (sub) DIAL_Z20#782
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#783
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#784
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這賭注對我來說太大了。不了，謝謝。

### (sub) DIAL_Z20#785
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，這才是明智之言。不學會怎麼算計著輸，你永遠成不了真正的棋手。

### (sub) DIAL_Z20#786
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#788
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#789
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有沒有興趣跟我下盤棋？

### (sub) DIAL_Z20#790
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不下注我可不下棋。有賭注才有意思。

### (sub) DIAL_Z20#791
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼樣的賭注？三十、四十枚金幣？

### (sub) DIAL_Z20#792
- speaker=19  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [21465..1]] -> node 4294901761
    - [flag 0x0101 in [22604..1]] -> node 4294901761
- text: 賭注不夠大，我可不下。至少得是綠寶石。你覺得自己的棋藝配得上這種賭注嗎？

### (sub) DIAL_Z20#793
- speaker=0  style=0
- branches:
    - [flag 0xc388 in [21494..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#794
- speaker=0  style=0
- branches:
    - [flag 0x1f6f in [21846..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#795
- speaker=0  style=0
- effects:
    - REMOVE item '8' cond=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#796
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這局棋很快就結束了。  伊凡自信滿滿地舉起手移動了他的祭司棋子，接著撂倒了@0的黑皇后。「將死。我記得是第五步吧。」他摸了摸下巴，忍住了一抹得意的笑容。「我警告過你我很厲害了。我那顆綠寶石，該是你交出來了吧？」

### (sub) DIAL_Z20#797
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#798
- speaker=0  style=0
- effects:
    - SET flag 0x1a84=1
    - GIVE item '8' cond=100 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#799
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊凡驚恐地張大了嘴。  棋盤上，他原本部署精密的攻勢已經亂成一團，而@0不知怎地竟把一步戰術性撤退，硬是轉成了正面攻勢。將死已不可避免。  「要投降嗎？」@0手指按在一枚獵人棋子上，問道。「還是要繼續下？」  伊凡搖了搖頭。「不用了，不用了。我看沒這個必要。這局是你的了。」  「你那顆綠寶石也是，」@0答道。「當然，前提是你願意信守賭約。」

### (sub) DIAL_Z20#800
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#801
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#802
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等等，我……我ñ本以為身上有顆綠寶石的……

### (sub) DIAL_Z20#803
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊。我還以為我擁有整個凱許帝國呢。不過看你不像是那種不誠實的人，這次我就放你一馬。

### (sub) DIAL_Z20#804
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#805
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#806
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 直覺告訴我，這賭注下得不明智，尤其我對你的棋路一無所知。不賭了。

### (sub) DIAL_Z20#807
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你會回來討打的。我的直覺告訴我準沒錯。

### (sub) DIAL_Z20#808
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#810
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#811
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有沒有興趣跟我下盤棋？

### (sub) DIAL_Z20#812
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你恐怕不會想跟我下棋的。我才剛從修道院借的一本書裡學到幾招新棋路。

### (sub) DIAL_Z20#813
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 先說賭注是什麼，我再告訴你有沒有興趣。

### (sub) DIAL_Z20#814
- speaker=19  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [23230..1]] -> node 4294901761
    - [flag 0x0101 in [24999..1]] -> node 4294901761
- text: 綠寶石。你覺得自己有這本事嗎？

### (sub) DIAL_Z20#815
- speaker=0  style=0
- branches:
    - [flag 0xc388 in [23259..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#816
- speaker=0  style=0
- branches:
    - [flag 0x1f70 in [23912..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#817
- speaker=0  style=0
- effects:
    - REMOVE item '8' cond=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#818
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊凡這局下得很好。  @0緊張地在吧台上敲著手指，試圖從眼前的陷阱裡找出一條生路，但機會看起來並不樂觀。除非酒館老闆犯下致命失誤，否則接下來他頂多只能一路防守，而這種失誤看起來根本不可能發生。  「黑皇后吃白獵人，」伊凡說。「兩步之內將死。」  彷彿魔法顯靈一般，@0忽然看穿了對手的意圖，明白自己絕無可能阻止對方逼出將死。  「這顆綠寶石歸你了，」@0說著，撂倒了自己的國王。「你贏了。」

### (sub) DIAL_Z20#819
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#820
- speaker=0  style=0
- effects:
    - SET flag 0x1a85=1
    - GIVE item '8' cond=100 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#821
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 酒館老闆渾然不覺。  伊凡忙著猛攻@0左翼的防線，卻沒注意到這位紳爵悄悄調整了自己右翼由一枚步兵、一名祭司跟皇后組成的陣形。  伊凡咧嘴一笑，把一枚步兵從棋盤上撥掉。「看來我已經打進你的防線了。準備好投降了嗎？」  「還沒呢，」@0答道，把獵人棋子滑向棋盤另一側。「你聽過『阿巴爾迴旋』嗎？」  酒館老闆盯著棋子，臉色瞬間發白。「你不可能……你居然真的……」接下來三步，他有氣無力地試圖挽回頹勢，最後終於死心放棄。「我投降。」

### (sub) DIAL_Z20#822
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#823
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#824
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，可我身上好像ó沒有綠寶石……我原本很確定自己帶著一顆的……

### (sub) DIAL_Z20#825
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó這種錯我自己也常犯……這次就放你一馬。幸好你不是等下完棋才耍這招，不然我肯定要懷疑你不是個講信用的人了。

### (sub) DIAL_Z20#826
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#827
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#828
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 直覺告訴我，這賭注下得不明智，尤其我對你的棋路一無所知。不賭了。

### (sub) DIAL_Z20#829
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你會回來討打的。我的直覺告訴我準沒錯。

### (sub) DIAL_Z20#830
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#832
- speaker=0  style=0
- effects:
    - SET flag 0x00ab=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#833
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，你倒是勾起了我的好奇心，什麼叫『ñ昂ñ帕薩』？我見過不少象棋的變體，倒是從沒聽過這一招。

### (sub) DIAL_Z20#834
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是凱許話。有天晚上我跟一個杜爾賓來的傢伙下棋。局勢全靠我一枚步兵撐著，勝券在握。結果你猜他幹了什麼？他把自己的步兵移到我那枚棋子正後方一格，居然聲稱吃掉了我的棋子！

### (sub) DIAL_Z20#835
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那根本是違規的一步棋。

### (sub) DIAL_Z20#836
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我當時也是這麼說的。可他接著跟我說，這是這局棋最基本的一招。我們為此爭了整整三個鐘頭，直到一個學生從王后街跑去修道院翻出一本古書。書裡確實有記載——書末用凱許文寫著這局棋最原始的規則。那一招『ñ昂ñ帕薩』害我輸了兩顆鑽石，差點連王后街都要一起賠進去。不用說，從那以後我這裡就不准再用這一招了。上一個試圖對我用這招的傢伙，叫納馮．杜桑多，我讓他好好見識了一下規矩，不過他也讓我見識了一招他自創的絕活，叫『桑多迴避』。只是那招具體怎麼下的，我現在倒是記不清了。

### (sub) DIAL_Z20#837
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#839
- speaker=0  style=0
- effects:
    - SET flag 0x0079=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#840
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是不是還有一招跟『阿巴爾棄兵』有點像、但又不太一樣的招式？

### (sub) DIAL_Z20#841
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊，有『阿巴爾迴旋』。那是勇者才敢用的一招棄局。用對地方，那大概是人能擺出最強的陣形了，可用錯地方，可要付出慘痛的代價。

### (sub) DIAL_Z20#842
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那招怎麼下？

### (sub) DIAL_Z20#843
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這招我可不會教你。你要是真學會怎麼用，我以後就沒法再跟你下棋了。光是你知道有這一招，就足以說明你這局棋懂得太深了。

### (sub) DIAL_Z20#844
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#846
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#847
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡商隊來來往往，我想你肯定跟不少商人打過交道吧。

### (sub) DIAL_Z20#848
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我打交道的也不少，不過王后街主要還是修道院學生的天堂。

### (sub) DIAL_Z20#849
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有沒有什麼不尋常的事，是長途旅人該知道的？哪座橋斷了？有沒有盜匪出沒？

### (sub) DIAL_Z20#850
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 最近唯一聽說的怪事，就是萊頓勳爵派了一批稅務官，在萊頓鎮進出的路口攔人收稅，數目高得離譜。要是拿不出來，稅務官不是把人趕回頭，就是直接一刀捅穿人家的脾臟。這一帶的商人要是老實照規矩來，肯定一個子兒都賺不到。看樣子他們是找到了什麼辦法，能偷偷繞過守衛。

### (sub) DIAL_Z20#851
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#853
- speaker=0  style=0
- effects:
    - SET flag 0x1a89=1
    - GIVE item 'O' cond=8 to member#6 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#854
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你認識一位名叫佩特魯姆的老婦人嗎？

### (sub) DIAL_Z20#855
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 她偶爾會來喝上一杯。你們在找她？

### (sub) DIAL_Z20#856
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實不是。我們碰巧遇見她，她說上次來這裡的時候忘了拿東西，請我們幫忙帶回去。

### (sub) DIAL_Z20#857
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 她可不只是忘了拿東西呢。一整桶凱許麥酒。還好我沒自己把它喝乾。你們離開前我拿給你們。

### (sub) DIAL_Z20#858
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000012  (DIAL_Z20#860)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eac=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483660 (GoodBye target)
- branches:
    - [flag 0x005e in [28556..1]] -> node 4294901761
    - [flag 0x005f in [29282..1]] -> node 4294901761
    - [flag 0x0060 in [29949..1]] -> node 4294901761
    - [flag 0x0061 in [30992..1]] -> node 4294901761
    - [flag 0x0063 in [31644..1]] -> node 4294901761
    - [flag 0x0064 in [33117..1]] -> node 4294901761

### (sub) DIAL_Z20#861
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#862
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你在這一帶見過夜鷹會的人嗎？

### (sub) DIAL_Z20#863
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊夏神保佑，別讓這種事發生！死亡公會嗎？我可不會讓他們踏進我這店裡。客人走進我這客棧的時候是活著的，我也希望他們離開的時候還是同樣的狀態——活著。拜託告訴我，你們不是想雇一個。

### (sub) DIAL_Z20#864
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 雇一個？我……也許是吧。有個人一直讓我很頭疼。

### (sub) DIAL_Z20#865
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別再說了，一個字都別再說了！不管你跟那人有什麼過節，我都不想知道。要找門路，這裡沒有。要找罪犯，去普蘭克石鎮的酒館試試吧。

### (sub) DIAL_Z20#866
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#868
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#869
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就住在伯爵家對街，你肯定常見到他吧。

### (sub) DIAL_Z20#870
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實不常。伯爵性子安靜，大多時候都喜歡獨處。他不太愛跟平民百姓一起喝酒。他們家上上下下都差不多，除了他女兒。

### (sub) DIAL_Z20#871
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他家裡有沒有什麼不尋常的訪客？

### (sub) DIAL_Z20#872
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 上他家的人不多。別誤會，他人不壞，只是有時候脾氣不太好相處。會進出他家的，大概就只有烏格妮的追求者，跟替伯爵做事的人。

### (sub) DIAL_Z20#873
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#875
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#876
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 烏格妮有沒有跟你說過內維爾是怎麼死的？那件事發生的時候我才七個仲夏節那麼大。

### (sub) DIAL_Z20#877
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那真是可怕、可怕的一天。我當時還以為烏格妮會就此崩潰，不過她身上流著她母親的血，骨子裡挺硬朗的。那些可憐的人挖了整整四天，卻始終沒能從瓦礫堆裡找回那孩子的遺體。我到現在都想不通伯爵當時心裡是怎麼想的。

### (sub) DIAL_Z20#878
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 叔叔？他做了什麼？

### (sub) DIAL_Z20#879
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是說，他當初為什麼要雇桑多那個人來替他們蓋酒窖？那人本來就有點嗜酒如命的名聲，蓋酒窖的時候，伯爵還撞見他喝得爛醉、醉到連挨罵都站不直，前前後後就有三次。伯爵當時就該想到那酒窖會蓋得不牢靠……  抱歉，這麼說對他不太公平。當然了，我們誰也沒辦法事先知道。他總不會故意把酒窖蓋得偷工減料吧？那不是白白浪費自己的錢嗎？

### (sub) DIAL_Z20#880
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#882
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#883
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽說伯爵不太喜歡烏格妮的一位追求者，叫納馮．杜桑多的。你知道他的事嗎？

### (sub) DIAL_Z20#884
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真可惜伯爵不喜歡他。那人可迷人了，一表人才，只要你沒得罪他，禮貌得很，不過要是他覺得你在欺負別人，那可就會較真到底。他配烏格妮，簡直是天造地設的一對。

### (sub) DIAL_Z20#885
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道我們上哪能找到他嗎？

### (sub) DIAL_Z20#886
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他是個商人，恐怕不太好找。我記得他住在肯廷拉什。你們可以去那邊的酒館問問看。

### (sub) DIAL_Z20#887
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#889
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#890
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 老闆，話說回來，『鴨頭』這裡都供應些什麼樣的吃食？

### (sub) DIAL_Z20#891
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 整個王國最好的手藝，別無分號！彼得今天能為您推薦點什麼呢？來份烤雞配一大塊乳酪？還是叉燒烤肉配蒸馬鈴薯芽？要不然，來份本店招牌——檸檬烤鴨，餡料是玫瑰花瓣碎屑！您覺得如何？

### (sub) DIAL_Z20#892
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜這些菜色應該沒有能帶上路的份量吧？

### (sub) DIAL_Z20#893
- speaker=11  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [32281..1]] -> node 4294901761
    - [flag 0x0101 in [32799..1]] -> node 4294901761
- text: 哎呀，那可沒有。不過我們可以幫兩位準備乾糧，一份只要十四枚金幣，價錢相當公道。要我這就去準備嗎？

### (sub) DIAL_Z20#894
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [32445..1]] -> node 851968
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#895
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 麻煩您了。會等很久嗎？

### (sub) DIAL_Z20#896
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一會兒就好。

### (sub) DIAL_Z20#897
- speaker=0  style=0
- effects:
    - SET flag 0x1eac=1
    - END conversation, result=65534

### (sub) DIAL_Z20#898
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒是想答應，可是仔細算過我身上的錢，現在恐怕辦不到。

### (sub) DIAL_Z20#899
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不太樂意讓兩位餓著肚子離開『鴨頭』，不過我這裡的存貨也已經捉襟見肘了。也許兩位可以去鎮上的錢莊那邊想想辦法湊點錢。

### (sub) DIAL_Z20#900
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#901
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來是挺誘人，不過我看還是先算了。我剛想起還有幾筆別的開銷得先處理。

### (sub) DIAL_Z20#902
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這次就放你們一馬，不過可別忘了以後回『鴨頭』來喝一杯、吃點東西。

### (sub) DIAL_Z20#903
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#905
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#906
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們有沒有空房間能讓我們躺一下？我想小睡片刻。

### (sub) DIAL_Z20#907
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 需要歇歇腳？真希望我能幫上忙，可惜『鴨頭』現在唯一空著的房間，就只有洗碗間了。

### (sub) DIAL_Z20#908
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們不介意跟人合住。

### (sub) DIAL_Z20#909
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是真心想幫兩位，可惜能出租的房間都住滿了，我看我那洗碗小廝也不會想跟人合住。那房間本來就只夠他一個人擠進去，已經夠緊了。要是再塞進你們三個，簡直得像疊柴火一樣把你們疊起來。真抱歉。

### (sub) DIAL_Z20#910
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000025  (DIAL_Z20#912)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eba=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483673 (GoodBye target)
- branches:
    - [flag 0x0065 in [33849..1]] -> node 4294901761
    - [flag 0x0066 in [34921..1]] -> node 4294901761
    - [flag 0x0067 in [36193..1]] -> node 4294901761

### (sub) DIAL_Z20#913
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#914
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 卡林王子在統領？那戰帥托馬斯呢？

### (sub) DIAL_Z20#915
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 確實是壞消息。三天前，托馬斯率領一隊精靈，去抵禦一批從莫拉埃林附近渡河而來的劫掠者。他們順利擊退了那些劫掠者，可混戰中，這位戰帥被一把淬了毒的劍刺中了側腹。他們得把他抬回艾爾凡達，我聽說過程也不輕鬆。托馬斯原本堅持要留下，可消息一傳回亞葛拉蘭娜王后那裡，這事就沒得商量了。  卡林王子那時便接掌了巡邏隊，據我所知，他這會兒還在森林東北邊緣一帶跟莫瑞德人拚殺呢。

### (sub) DIAL_Z20#916
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戰帥還活著嗎？

### (sub) DIAL_Z20#917
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那小子向來是個硬漢，而且韌性十足。他寧可讓人砍掉一條腿，也不會向這毒藥低頭。我看不用擔心。不過看見托馬斯倒下，倒是把你們族人嚇了一大跳。他跟你們族人在一起十五年了，我還從沒聽說過這種事發生過。

### (sub) DIAL_Z20#918
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#920
- speaker=0  style=0
- effects:
    - SET flag 0x0067=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#921
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們得盡快趕到艾爾凡達去。你剛才提到大火？

### (sub) DIAL_Z20#922
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 已經撲滅了，不過也是費了一番功夫又是踩火又是提水桶的！我一度還以為整片森林要燒成一片火海了，幸好塔薩爾跟亞葛拉蘭娜王后的其他織法者及時把火勢給止住了。

### (sub) DIAL_Z20#923
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們回艾爾凡達應該就沒什麼阻礙了。

### (sub) DIAL_Z20#924
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒不敢這麼說。森林裡還是有不少雙足飛龍到處亂飛，儘管塔薩爾日夜不停地想辦法解決那些討厭鬼。他甚至還教了卡林王子一點法術，能左右那些暴躁蜥蜴的心智，不過我聽說這還是沒能止住牠們的襲擊。

### (sub) DIAL_Z20#925
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那矮人那邊呢？

### (sub) DIAL_Z20#926
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哦，我們是派了幾個人自願幫忙，不過你們精靈不太喜歡外人踏進自己的地盤，我們也一向尊重你們的邊界。多爾根王確實派了幾名志願者去幫精靈女王的忙，可他們一進森林就犯起了要命的睡意，再也走不動了。八成是撞上你們那傳說中的『沉眠林地』了。

### (sub) DIAL_Z20#927
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#929
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#930
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們可能得面對雙足飛龍，先把盔甲修好或許是明智之舉。卡爾達拉有沒有修盔甲的匠人？

### (sub) DIAL_Z20#931
- speaker=26  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [36668..1]] -> node 4294901761
    - [flag 0x0101 in [38057..1]] -> node 4294901761
- text: 艾爾凡達有沒有樹葉？你是不是傻了！卡爾達拉當然有修盔甲的匠人！不過你們用不著跑那麼遠。我幾個金幣就能替你們修，你們要是看仔細點，說不定還能學到點修盔甲的門道。一百枚金幣，你們覺得如何？

### (sub) DIAL_Z20#932
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [36697..1]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#933
- speaker=0  style=0
- effects:
    - TAKE gold -1000
    - ACTION: repair party armour
- branches:
    - [flag 0x1f71 in [36785..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#934
- speaker=0  style=0
- effects:
    - SET flag 0x1f71=1
    - RAISE Armorcraft of party by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#935
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這價錢我沒問題。我們該做什麼？

### (sub) DIAL_Z20#936
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，小夥子，麻煩你把外衣底下的盔甲脫下來，你那位精靈朋友也一樣，我們就開工了。仔細看好我怎麼做……

### (sub) DIAL_Z20#937
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 以前有人跟我說過，盔甲上有幾個凹痕其實反倒有好處。說是能擋住原本會沿著表面滑進縫隙的攻擊？仔細想想，好像還真有點道理。  說不定該一開始就把盔甲打造成帶有凸起、稜面的樣子！要是本來就有這些設計，那盔甲就……  你已經修完了？

### (sub) DIAL_Z20#938
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊，修好了。你會發現這盔甲已經修到能力所及的最好狀態了，小夥子，不過我敢說，你要是少說點話、多聽一點，肯定能學到更多東西。

### (sub) DIAL_Z20#939
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#940
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#941
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，我們身上的錢不夠付這筆費用。

### (sub) DIAL_Z20#942
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你們可找不到第二個像我這麼會使錘子的甲匠了。等你們有空又有錢的時候，我還在這一帶到處走動。卡達爾重新開通之後，我還有不少差事要跑呢。

### (sub) DIAL_Z20#943
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#944
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#945
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們先去問問別人的價錢，你不介意吧？

### (sub) DIAL_Z20#946
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是你們的權利，我也不攔著，不過灰塔這一頭，我可是最好的。要是哪天一個莫瑞德人一劍捅穿你的五臟六腑，捅到劍柄都沒入為止，那可是你們自己活該。

### (sub) DIAL_Z20#947
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000014  (DIAL_Z20#949)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb7=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483662 (GoodBye target)
- branches:
    - [flag 0x0068 in [38469..1]] -> node 4294901761
    - [flag 0x0069 in [41284..1]] -> node 4294901761
    - [flag 0x006a in [42943..1]] -> node 4294901761
    - [flag 0x006b in [43798..1]] -> node 4294901761
    - [flag 0x006c in [44538..1]] -> node 4294901761

### (sub) DIAL_Z20#950
- speaker=0  style=0
- effects:
    - SET flag 0x006b=1
    - SET flag 0x1a94=1
    - bind speaker-name slot (kind=1 sub=3)
    - bind speaker-name slot (kind=2 sub=2)
    - RAISE Stealth of member#1 by 2560
    - RAISE Crossbow Acc of member#2 by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#951
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人不斷侵擾你們的邊境，你們居然還能獨自撐下來，真是令人意外。你們是怎麼躲過去的？

### (sub) DIAL_Z20#952
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人在艾爾凡達境內對伊列德人幾乎造不成什麼傷害，他們要是想試，也未免太傻了。一個莫瑞德人要懷著惡意踏入這片森林，得有非凡的意志力才辦得到，而要在這種嘗試中活下來，所需的意志力就更加驚人了。這正是守護我們家園的法術的一部分。

### (sub) DIAL_Z20#953
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那戈拉斯呢？他進森林可沒遇上什麼麻煩。

### (sub) DIAL_Z20#954
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你還沒告訴這孩子？

### (sub) DIAL_Z20#955
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的歸來與他無關。他有自己要完成的使命。

### (sub) DIAL_Z20#956
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歸來？你的意思是你以前來過這裡？

### (sub) DIAL_Z20#957
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是事情如我所料發展，你之後自然會明白一些事情。不過眼下還有你自身安危的問題得處理。儘管我們這位戈拉斯表親行動優雅自如，你的腳步卻不太穩健。為了你在救援我這件事上出的力，我想教你精靈的行動之道。

### (sub) DIAL_Z20#958
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那戈拉斯呢？

### (sub) DIAL_Z20#959
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這在我們族人之間並非慣例，不過既然你這麼希望……我便把我所知的十字弓用法教給他。  來吧。這事我們耽擱不了太久。

### (sub) DIAL_Z20#960
- speaker=0  style=0
- effects:
    - advance in-game time by 7200
- branches:
    - [always] -> node 0 (no jump)
- text: 卡林等候著。  他盤腿坐在地上，半闔著眼，看著歐文從一片濃密的樹叢間走來。雖然他的動作依然稱不上優雅，短短時間內卻已經有了長足的進步。  「我現在走路像個精靈了嗎？」歐文問道，臉上寫滿了期待。  「要偷襲戰帥恐怕還早得很，不過沒錯，你確實學到了一點東西，」這名精靈答道。「你何不繞回去再試一次？你剛才走近時，還在窸窸窣窣踩著落葉呢。」  歐文一走遠，卡林便把目光轉向戈拉斯練習十字弓的情況。雖然一眼就看得出這名莫瑞德人使起這把武器來威力驚人，他的心思卻明顯不在這上頭。  「聽說要...

### (sub) DIAL_Z20#961
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#963
- speaker=0  style=0
- effects:
    - event_bitmap_hi[30] bitop
    - SET flag 0x1a95=1
    - GIVE item '?' cond=1 to member#7 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#964
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 走地下路線倒有個好處，至少不太可能有東西從天而降砸到我們頭上。這一帶雙足飛龍滿天飛，我幾乎每次一轉頭，都覺得會冒出一隻朝我撲來。

### (sub) DIAL_Z20#965
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等你真的穿過那座古老遺跡，恐怕就沒這麼興致勃勃了。我們平時也很少用那條路。

### (sub) DIAL_Z20#966
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託告訴我那裡沒有布拉克努爾之類同樣噁心的東西出沒……

### (sub) DIAL_Z20#967
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 『出沒』？這說法倒有意思，不過不是你想的那種意思。任何流著精靈血統的人，走進那些迴廊都難免會心生畏懼。

### (sub) DIAL_Z20#968
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，那地方跟瓦爾赫魯有關。

### (sub) DIAL_Z20#969
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戰帥向我們保證，牠們那古老的本質已無法在此觸及我們，不過那地方瀰漫的邪惡氣息，卻也不容輕易忽視。話雖如此，我們也沒愚蠢到讓任何人隨意進出那裡。萬一裡頭還有什麼尚未被發現、超出我們掌控的東西，那風險太大了。只有少數幾名精靈持有能打開那扇門的鑰匙。

### (sub) DIAL_Z20#970
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們要怎麼進去？

### (sub) DIAL_Z20#971
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會把我隨身帶著的鑰匙交給戈拉斯。這樣就夠了。

### (sub) DIAL_Z20#972
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就這麼簡單？

### (sub) DIAL_Z20#973
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這一點也不簡單。戈拉斯光是能靠近艾爾凡達到這種程度，就已經需要非凡的意志力了。要不是他來此的理由極其重要，他早就逃離這片森林了。  我信任他。

### (sub) DIAL_Z20#974
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#976
- speaker=0  style=0
- effects:
    - SET flag 0x1a96=1
    - GIVE item '\x85' cond=41 to member#5 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#977
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們是怎麼擋住這些雙足飛龍的？我還以為這麼多隻，早該把艾爾凡達燒成平地了。

### (sub) DIAL_Z20#978
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 幸好莫瑞德人用來控制牠們的法術既不強大也不複雜。就連我這點微薄的法術知識，塔薩爾都能教會我一個能把牠們趕走的小咒語。

### (sub) DIAL_Z20#979
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來挺有用的。要是你有空，能不能教教我？

### (sub) DIAL_Z20#980
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我學過的那卷卷軸可以給你。我想我以後也用不上了，不過先提醒你，每次施展這法術，你都得先找到一顆那種生物的蛋才行。塔薩爾曾試著跟我解釋箇中原理，可我實在跟不上那些複雜的道理。

### (sub) DIAL_Z20#981
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#983
- speaker=0  style=0
- effects:
    - SET flag 0x0069=1
    - SET flag 0x006c=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#984
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哪條路能最快帶我們到艾爾凡達？

### (sub) DIAL_Z20#985
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是單論距離，我會建議你們走北橋，不過我從斥候那裡得知，那附近最近有大批雙足飛龍棲息。走遠一點的西橋要安全得多，可以從那裡穿越沉眠林地，儘管你們可能得費點工夫應付那些林地。過了那裡，一直往正北走，直到抵達灰角山。你們會在那裡找到一座地下古老遺跡的入口。一旦從裡頭出來，就已經非常接近艾爾凡達的核心地帶了。

### (sub) DIAL_Z20#986
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#988
- speaker=0  style=0
- effects:
    - SET flag 0x1f72=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#989
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你剛才說我們可能會在沉眠林地遇上一些麻煩？

### (sub) DIAL_Z20#990
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是艾爾凡達天然防禦的一部分。誰要是走進去，會突然感到一陣強烈睡意，接連沉睡好幾天。不少人就這麼在睡夢中因缺乏飲食而喪命。

### (sub) DIAL_Z20#991
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這防禦手段確實有效，只是不分敵我。我猜總有辦法能穿越過去吧……

### (sub) DIAL_Z20#992
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 住在一間沒有門的房子裡是不切實際的。這些林地大小不一，你們靠近時，會感覺到一陣輕微的暈眩。  不過，ñ確實ð有一條鮮為人知的小路，能安全帶你們穿過去。這些林地與此地西南方一座山脈平行延伸，位於河流分岔口以北。要橫越很困難，但你們可以繞過去。只要你們前往河流的分岔口，接著沿著北邊的山脈靠近走，ñ應該就不會被這些林地所困擾了。

### (sub) DIAL_Z20#993
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000022  (DIAL_Z20#995)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb3=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483670 (GoodBye target)
- branches:
    - [flag 0x006e in [45629..1]] -> node 4294901761
    - [flag 0x006f in [48017..1]] -> node 4294901761
    - [flag 0x0070 in [48864..1]] -> node 4294901761

### (sub) DIAL_Z20#996
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#997
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這一帶敵軍的活動情況如何？有沒有增兵的跡象？

### (sub) DIAL_Z20#998
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 至少我們能證實亞魯莎親王的擔憂——莫瑞德人確實正在籌劃進攻。我有幾名斥候潛入拉格蘭姆，發現那裡正在打造一台投石機跟幾具攻城器械。已經有一大批凱許傭兵抵達鎮上，只是還沒人知道他們會被派往何處。看樣子當地的莫瑞德人，倒是採取了觀望的態度，想先看看戰局如何，再決定要不要加入迪勒肯的攻擊部隊。

### (sub) DIAL_Z20#999
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯也是這麼跟我們說的。上次進攻賽瑟儂顯然讓各莫瑞德氏族心裡都留下了陰影，這個迪勒肯又沒有穆爾曼達穆斯那副能言善道的口才。他只能靠威逼手段強迫幾個氏族加入自己，不過有幾個較大的氏族已經發誓，除非迪勒肯先證明自己的實力，否則絕不出手相助。

### (sub) DIAL_Z20#1000
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 比起戰場上的凱許人，我更擔心莫瑞德人可能會搞出什麼出乎意料的花招。聽說迪勒肯身邊有個叫『六賢者』的顧問團，是某種法師組織。想到當年穆爾曼達穆斯在阿曼加一役搞出的那些手段，我可一點也不想再領教一次。馬丁公爵一直跟我說起那場戰役，不過我聽說最後總攻發起前，他人並不在場……

### (sub) DIAL_Z20#1001
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬丁公爵在這裡？

### (sub) DIAL_Z20#1002
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他是在您這位朋友抵達前不久，以私人拜訪的名義來的。他還在克萊迪公爵麾下做事的時候，我曾是卡斯的獵場總管，巴倫．羅索死後，是他推薦我來接下這個職位的。您這位朋友從克朗多帶來另一波可能進攻的消息之後，他便決定留下來，盡自己所能幫忙，直到亞魯莎親王另有指示為止。眼下他跟洛克利爾紳爵正帶著一支小型偵察隊，前往高地那邊。

### (sub) DIAL_Z20#1003
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那法術這方面的問題呢？您打算雇些法師嗎？

### (sub) DIAL_Z20#1004
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很久以前，我就見識過博里克公爵當年把庫爾根跟帕格留在自己領地裡的那份遠見。我一接掌這裡的指揮權，這就是我最先辦的幾件事之一。不知為何，派特魯斯在這裡待著不太自在，此刻正忙著研究幾招自己的手段，好對付莫瑞德人的法術。

### (sub) DIAL_Z20#1005
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1007
- speaker=0  style=0
- effects:
    - event_bitmap_hi[22] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1008
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在哪能找到馬丁公爵？他在城堡裡的什麼地方嗎？

### (sub) DIAL_Z20#1009
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我要求他待在離城堡不遠的地方，好讓我的守衛萬一有緊急情況能找到他。你們得自己去找他。順便的話，也許你們也能查查我們那位吟遊詩人塔姆尼，如今究竟怎麼樣了。

### (sub) DIAL_Z20#1010
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他說不定已經離開城堡了。吟遊詩人向來不以在大戰中堅守崗位聞名。

### (sub) DIAL_Z20#1011
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是他一直不見蹤影，會打擊士氣。我要你們找到他，不管用什麼手段都行，把他帶回來——就算是用鐵鍊拴著、麻袋套頭拖回來也行。眼看大戰將至，我不希望有任何事讓士兵們人心渙散。

### (sub) DIAL_Z20#1012
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1014
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1015
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡的守衛是誰在統領？我想跟他談談。

### (sub) DIAL_Z20#1016
- speaker=18  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [49241..1]] -> node 4294901761
    - [flag 0x0101 in [51915..1]] -> node 4294901761
- text: 我的守衛都在忙著執勤。紳爵大人，您若想跟守衛談談，我可以安排您去站一班崗。除此之外，我可不希望他們的排班被打亂。要不要我叫亞倫中尉把您排進夜間巡邏？

### (sub) DIAL_Z20#1017
- speaker=0  style=0
- effects:
    - SET flag 0x1a9c=1
    - bind speaker-name slot (kind=0 sub=5)
    - GIVE item '-' cond=100 to member#2 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1018
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來太好了。我什麼時候開始？

### (sub) DIAL_Z20#1019
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞倫中尉！我這裡有個新兵要交給你安排……

### (sub) DIAL_Z20#1020
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 夜已深了。  詹姆士對著攏起的雙手呵著暖氣，在後門與外堡大門之間結霜的石板路上來回踱步，望向城堡外那片黑暗。霧氣中什麼動靜都沒有。跟大門之內的世界一樣，這裡的一切都顯得極度井然有序——太過井然有序了。就連在克朗多，親王的掌控都遠稱不上滴水不漏，下水道裡有正直人在管事，貧民區裡也有形形色色的惡棍各自呼風喚雨。可在這裡，彷彿北衛城以外的世界，除了加博特男爵向手下下達的命令之外，根本不存在別的可能。這種嚴苛到近乎僵化的治軍方式，反倒太容易被外力所趁了。  「是時候讓『神偷吉米』做點...

### (sub) DIAL_Z20#1021
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很想知道，你覺得有什麼必要，非得三更半夜把我叫醒不可。

### (sub) DIAL_Z20#1022
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您要是一叫就來，那就更好了。男爵大人，您這裡的守衛輪班安排根本形同虛設。昨晚我站崗的時候，決定稍微調動一下排班，看看會發生什麼事。我本該待在城堡另一側，卻跑去盯著外堡大門，結果看見一名士兵偷偷把一張紙條遞給等在城堡外的另一個人。幾分鐘後，我換到對面那一側，又親眼撞見有人企圖從城堡軍械庫偷走一把『悲愴使者』。我自然是把他攔下了。類似的情況還不只這幾樁。

### (sub) DIAL_Z20#1023
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那張紙條，是從外堡大門遞出去的？

### (sub) DIAL_Z20#1024
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無傷大雅。是一名駐紮在這裡、名叫科比的士兵，寫給一個叫蒂雅的姑娘的情書。  您這裡的排班已經僵化到危險的地步了。您的作息時間表城外的人都摸得一清二楚，十有八九是這高牆之內有內鬼洩露出去的。我強烈建議您加強戒備，重新審視您的人手。這可能會是這座城堡覆滅的原因。

### (sub) DIAL_Z20#1025
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會……考慮的。  這段期間，還請您收下一點小小的謝意。我這裡有一套尤利利科盔甲，已經用不上了。您若願意，就拿去吧。對我來說也沒什麼差別。

### (sub) DIAL_Z20#1026
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1027
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1028
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然您似乎不太需要我的幫助，那我就收回這番好意。

### (sub) DIAL_Z20#1029
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 知道了，紳爵大人。

### (sub) DIAL_Z20#1030
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000015  (DIAL_Z20#1032)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eaf=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483663 (GoodBye target)
- branches:
    - [flag 0x0072 in [52230..1]] -> node 4294901761
    - [flag 0x0073 in [54898..1]] -> node 4294901761
    - [flag 0x0074 in [55915..1]] -> node 4294901761
    - [flag 0x0075 in [56647..1]] -> node 4294901761
    - [flag 0x0076 in [57705..1]] -> node 4294901761
    - [flag 0x0077 in [59379..1]] -> node 4294901761
    - [flag 0x0078 in [61640..1]] -> node 4294901761
    - [flag 0x0079 in [63207..1]] -> node 4294901761
    - [flag 0x007a in [839..2]] -> node 4294901761
    - [flag 0x007b in [1227..2]] -> node 4294901761
    - [flag 0x007c in [1986..2]] -> node 4294901761

### (sub) DIAL_Z20#1033
- speaker=0  style=0
- effects:
    - bind speaker-name slot (kind=0 sub=15)
    - SET flag 0x0078=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1034
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您懂得一些施法的知識嗎？

### (sub) DIAL_Z20#1035
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我懂一點皮毛，不過多明尼克修士比我懂得多。等他研究完奎格民法典，我相信他一定很樂意坐下來跟您聊聊這方面的事。我看他大概還要再花兩三個月的功夫……

### (sub) DIAL_Z20#1036
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我們等不了兩三個月。姪兒，我們還是別打擾這位修士了吧？

### (sub) DIAL_Z20#1037
- speaker=14  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [53035..1]] -> node 4294901761
    - [flag 0x0101 in [54685..1]] -> node 4294901761
- text: 哎呀呀！別打消這孩子發問的興致，不然他以後什麼都不敢問了。要是你們能撥出幾枚金幣，比如說五十枚，我倒是能抽空教教他一點集中心神的門道。大家都同意嗎？

### (sub) DIAL_Z20#1038
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [53064..1]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1039
- speaker=0  style=0
- effects:
    - SET flag 0x1a9e=1
    - TAKE gold -500
    - bind speaker-name slot (kind=1 sub=3)
    - RAISE Casting Acc of member#1 by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1040
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 同意，再樂意不過了。我們從哪開始？

### (sub) DIAL_Z20#1041
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，一個熱情的學生！真令人高興。教你會是件樂事……

### (sub) DIAL_Z20#1042
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文臉色發白。  他分到的任務其實很簡單：施展一道念力法術，把自己的背包移近一點。結果背包紋絲不動，卻把馬克修士整個人震得往後飛，一頭栽進他悉心照料的作物裡。  「您沒事吧？」歐文倒抽一口氣。「我不是故意的。」  「你還是太依賴眼睛了，」馬克修士嘆了口氣，一邊掙扎著爬起來，一邊撥開臉上的一根玉米梗。「集中精神。要是哪天你碰上看不見自己想影響的目標的情況，那世上所有的法術對你來說都毫無用處。別試著用眼睛去看目標，試著去感覺它。來，我們再試一次。我相信你遲早會學會的……」  「我...

### (sub) DIAL_Z20#1043
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1044
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1045
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這提議太慷慨了，馬克修士，不過我這姪兒常常搶著說話。我們現在真的付不起這筆錢。

### (sub) DIAL_Z20#1046
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧。那就改天吧。

### (sub) DIAL_Z20#1047
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1048
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1049
- speaker=240  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的，我們還有別的事要辦。不過還是很感謝您的好意。

### (sub) DIAL_Z20#1050
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們改變主意，這提議還是有效的。

### (sub) DIAL_Z20#1051
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1053
- speaker=0  style=0
- effects:
    - SET flag 0x0034=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1054
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從這裡往南到克朗多的路上有沒有什麼危險？我們有點趕時間，不想碰上什麼意外的耽擱。

### (sub) DIAL_Z20#1055
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這幾週路過這裡的旅人，我倒沒聽過什麼抱怨。之前來找多明尼克修士的那批傭兵，好像也沒提過這方面的事。

### (sub) DIAL_Z20#1056
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 傭兵？他們該不會是奎格的強徵兵吧？

### (sub) DIAL_Z20#1057
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就我所知不是。這批人是從一艘叫「浪沫紡者」號的船上下來的，就在尋道崖以南靠岸。看他們在這條路上跑上跑下的，我猜是在放假上岸。

### (sub) DIAL_Z20#1058
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們人多嗎？

### (sub) DIAL_Z20#1059
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 人多嗎？要是把他們一個接一個頭尾相連排開，我看都能踩著他們的身體橫渡黑暗海峽而不濕腳了。看樣子一艘奎格戰艦，都能一次載走一整座小村子似的！

### (sub) DIAL_Z20#1060
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1062
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1063
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那這場暴風雨什麼時候會來？我們有點擔心找不到地方躲，會被淋成落湯雞。

### (sub) DIAL_Z20#1064
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 暴風雨？這我還是頭一次聽說有這種氣象異狀。我今早離開修道院時，吉羅姆修士可沒跟我提過這事。

### (sub) DIAL_Z20#1065
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真奇怪。我們遇見一位叫羅威的先生，他說修道院的修士們預言會有暴風雨。

### (sub) DIAL_Z20#1066
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真不知道他為什麼會跟你們說這種話。不過話說回來，自從他妻子過世後，他的行為就一直有點古怪。真是場可怕的悲劇，偏偏又碰上他不得不放棄農場的時候。我真為這可憐的老人家感到心疼。

### (sub) DIAL_Z20#1067
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1069
- speaker=0  style=0
- effects:
    - SET flag 0x0036=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1070
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我祖父以前常跟我說薩斯地底下那些洞窟的故事，他說那裡以前是座富饒的矮人礦坑的一部分。他管它叫麥克布加蘭……博爾古……

### (sub) DIAL_Z20#1071
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記得叫麥克布爾加蘭多克，沒錯。曾經是座相當壯觀的綠寶石礦。

### (sub) DIAL_Z20#1072
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他說那裡可能還有隧道，直通修道院正下方。要是你們手上有任何舊的矮人地圖或地契，我們或許能從那座舊礦坑進去。

### (sub) DIAL_Z20#1073
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可惜那些地圖目前不在薩斯修士會手上。我們把它們交給了住在艾格利的助理稅務官，一個叫史戴倫的人。我聽說是因為修道院跟那些舊礦坑的關聯，在課稅額度上起了些爭議。  你們要是找他談談，我相信他能把那些文件拿給你們看。至少聽起來，這是我們能重新進入修道院的一條路！

### (sub) DIAL_Z20#1074
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1076
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1077
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實，我是希望您能幫忙翻找點跟法術有關的東西，也許是一卷卷軸……

### (sub) DIAL_Z20#1078
- speaker=14  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [58092..1]] -> node 4294901761
    - [flag 0x0101 in [58995..1]] -> node 4294901761
- text: 前幾天我在整理目錄時，有一卷卷軸說不定您會感興趣。我記得標題是ñ『天火術』。我可以去幫您找出來，酌收一百枚金幣的搜尋費。要我這就去找嗎？

### (sub) DIAL_Z20#1079
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [58121..1]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1080
- speaker=0  style=0
- effects:
    - SET flag 0x1aa2=1
    - GIVE item '\x85' cond=5 to member#5 (cost 1000)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1081
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 同意。我們要在這裡等，還是……

### (sub) DIAL_Z20#1082
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 安東尼修士不喜歡地窖裡同時有太多人。這會打擾正在整理目錄跟抄寫的人。我很快就回來……

### (sub) DIAL_Z20#1083
- speaker=0  style=0
- effects:
    - advance in-game time by 5400
- branches:
    - [always] -> node 0 (no jump)
- text: 他們等著。  就在眾人幾乎要以為這位神父再也不會回來時，他終於搖搖擺擺地從山坡上走了下來，腋下夾著一卷繫著緞帶的羊皮紙卷軸。他從歐文那收下欠款，開心地把卷軸交了出去。

### (sub) DIAL_Z20#1084
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1085
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1086
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，我差了一截。看來我終究買不了這卷卷軸了。

### (sub) DIAL_Z20#1087
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒看不出你的『身高』跟你差的那一截購買力有什麼關係！  咳……原諒我，這雙關語實在讓人受不了。有時候我就是管不住自己。

### (sub) DIAL_Z20#1088
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1089
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1090
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，我其實沒打算真的付錢。我想說既然你們是獻身於知識的人，那麼，呃……

### (sub) DIAL_Z20#1091
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就算是伊夏修士會的人，也得養活自己。雖然我們都認同知識本該對所有人免費這個理念。等你們手頭寬裕一點，我們再談吧。

### (sub) DIAL_Z20#1092
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1094
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1095
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們修道院裡有沒有關於死亡公會的資料？我記得多年前造訪貴修道院時，你們的藏書相當豐富。我想查查他們當中有些人，是怎麼變成黑衣殺手的。

### (sub) DIAL_Z20#1096
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不需要翻找地窖。他們當中不少人信奉卡胡利神，這位復仇之神偶爾會賜予他們近乎不死之身，交換條件是徹底獻身於祂。我們花了好長時間，才學會能阻止夜鷹會成員死而復生的法術。

### (sub) DIAL_Z20#1097
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還有這種法術？我們還以為得把屍體剁碎燒成灰才行……

### (sub) DIAL_Z20#1098
- speaker=14  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [60469..1]] -> node 4294901761
    - [flag 0x0101 in [61284..1]] -> node 4294901761
- text: 那是個令人不快又費時的辦法。大崛起之戰結束、莫瑞德人退兵之後，我們才得以跟林絲克拉格瑪的祭司們合作，研發出一道法術，既能阻止夜鷹會成員變成黑衣殺手，也能讓黑衣殺手一旦被殺就徹底倒下不再復生。您若有興趣，我或許能到地窖裡把這道法術翻找出來。有興趣嗎？費用是一百枚金幣。

### (sub) DIAL_Z20#1099
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [60498..1]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1100
- speaker=0  style=0
- effects:
    - SET flag 0x1aa3=1
    - bind speaker-name slot (kind=1 sub=5)
    - GIVE item '\x85' cond=32 to member#3 (cost 1000)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1101
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 想到我不久後可能會撞上死亡公會的人，我看這筆投資挺明智的。

### (sub) DIAL_Z20#1102
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我盡量快去快回。請在這裡稍候。

### (sub) DIAL_Z20#1103
- speaker=0  style=0
- effects:
    - advance in-game time by 5400
- branches:
    - [always] -> node 0 (no jump)
- text: 他們等著。  就在眾人幾乎要以為這位神父再也不會回來時，他終於搖搖擺擺地從山坡上走了下來，腋下夾著一卷繫著緞帶的羊皮紙卷軸。他從詹姆士那收下欠款，開心地把卷軸交了出去。

### (sub) DIAL_Z20#1104
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1105
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1106
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我原本想買這卷卷軸，可看來我身上的錢比我想的還少。

### (sub) DIAL_Z20#1107
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係。我很確定修道院不會把它燒了，要是您以後還想要，隨時都在。

### (sub) DIAL_Z20#1108
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1109
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1110
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩斯的伊夏修士會，不是應該獻身於知識之神的嗎？

### (sub) DIAL_Z20#1111
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就算是伊夏修士會的人，也得養活自己。雖然我們都認同知識本該對所有人免費這個理念。等你們手頭寬裕一點，我們再談吧。

### (sub) DIAL_Z20#1112
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1114
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1115
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在我對施法多懂了一點，也許您能教我一道簡單的法術？

### (sub) DIAL_Z20#1116
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文……

### (sub) DIAL_Z20#1117
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就簡單的就好，好讓我們萬一路上遇上心懷不軌的人，也有辦法自保。

### (sub) DIAL_Z20#1118
- speaker=14  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [62288..1]] -> node 4294901761
    - [flag 0x0101 in [62999..1]] -> node 4294901761
- text: 我不知道你以為外頭等著你的是什麼，不過我想我正好有樣東西適合。我得跑一趟地窖去找，是個叫『擲焰術』的小法術。當然，還有費用的問題，就說三十枚金幣吧。我很清楚它放在哪，要我這就去拿嗎？

### (sub) DIAL_Z20#1119
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [62317..1]] -> node 4294901790
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1120
- speaker=0  style=0
- effects:
    - advance in-game time by 5400
    - SET flag 0x1aa4=1
    - GIVE item '\x85' cond=4 to member#5 (cost 300)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1121
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您能快一點嗎？

### (sub) DIAL_Z20#1122
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不會耽擱太久。我會盡我這雙小短腿最快的速度趕回來。

### (sub) DIAL_Z20#1123
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們等著。  就在眾人幾乎要以為這位神父再也不會回來時，他終於搖搖擺擺地從山坡上走了下來，腋下夾著一卷繫著緞帶的羊皮紙卷軸。他從@5那收下欠款，開心地把卷軸交了出去。

### (sub) DIAL_Z20#1124
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1125
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1126
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來這次只好算了。我身上的錢比我想的還少。

### (sub) DIAL_Z20#1127
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧。那就當是衝動購物告吹了。

### (sub) DIAL_Z20#1128
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1129
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1130
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 仔細想想，我今天大概已經花得超出自己能負擔的範圍了。

### (sub) DIAL_Z20#1131
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。要是改變主意，再來找我。

### (sub) DIAL_Z20#1132
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1134
- speaker=0  style=0
- effects:
    - SET flag 0x1a87=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1135
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜你們修道院那一大堆藏書裡，該不會剛好有一本講棋藝的吧？我在找一種叫『阿巴爾迴旋』的棋路資料。

### (sub) DIAL_Z20#1136
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 任何一間有點自尊的凱許藏書閣都不會少了這種書，而這座修道院正是由凱許遊方僧所創建的……

### (sub) DIAL_Z20#1137
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……所以你們理當有這方面的資料。太好了。要是您能幫我們翻找出來，只要是關於棋路的東西，我都很樂意支付搜尋費。

### (sub) DIAL_Z20#1138
- speaker=14  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [63961..1]] -> node 4294901761
    - [flag 0x0101 in [525..2]] -> node 4294901761
- text: 這個要求相當特殊，我恐怕得花上一番工夫翻找，而且今晚我還有另一件事要處理。您願意付一百枚金幣嗎？

### (sub) DIAL_Z20#1139
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [63990..1]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1140
- speaker=0  style=0
- effects:
    - SET flag 0x1aa5=1
    - SET flag 0x1f70=1
    - advance in-game time by 7200
    - TAKE gold -1000
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1141
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗯，這個嘛。我想這次這筆錢應該花得值得。

### (sub) DIAL_Z20#1142
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會確保您這筆錢花得物有所值。請在這裡稍候，我一找到有用的東西就馬上回來……

### (sub) DIAL_Z20#1143
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 文士修士過了好幾個鐘頭才回來。  「怎麼樣，你查到了什麼？」@0見馬克修士終於現身，心情也跟著好轉，問道。「有什麼能用的東西嗎？」  馬克皺著眉頭，在袍子的皺褶裡翻找。「我發現就我們的分類系統來說，ñ林嵐牌、ñ帕夏瓦牌、ñ鬥雞、ñ達爾茲、ñ波基爾、ñ國王ñ之山、ñ骰子、ñ修松、ñ四手ñ落地，跟ñ棋，其實根本沒什麼分別。到目前為止，它們全都只被歸類成『遊戲』。」  @0聳了聳肩。「唉，白費心思了。真希望我們沒浪費這趟時間。」  馬克修士從左邊袖子裡抽出一卷卷軸，放在@0膝上。「...

### (sub) DIAL_Z20#1144
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1145
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1146
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看巴納斯神是不希望我做這件事了。我的金子用光了。

### (sub) DIAL_Z20#1147
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這番道理，我可不會跟您爭辯。

### (sub) DIAL_Z20#1148
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1149
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1150
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這比我預期的貴了一些。您確定不能把價錢再降一點嗎？

### (sub) DIAL_Z20#1151
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我先前說過了，這是個特殊要求，得耽誤我處理其他職務的時間。要是這價錢讓您感到不便，我很抱歉。

### (sub) DIAL_Z20#1152
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1154
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1155
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您知道『馬克羅斯之書』這東西嗎？

### (sub) DIAL_Z20#1156
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克羅斯『的』書，沒有。關於馬克羅斯『的』書，我知道地窖裡倒是有幾本，大多是他住在法師之島上的貝亞塔別墅時流傳下來的傳說。裡頭說不定也收藏了幾本他親筆所著的書，不過不查一查我也不能確定。

### (sub) DIAL_Z20#1157
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1159
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1160
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 外人可以進地窖翻閱書籍嗎？我很想親自看看。

### (sub) DIAL_Z20#1161
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒是沒意見，不過您恐怕得說服安東尼修士才行。他不喜歡陌生人在沒人監督的情況下在下頭到處亂逛。我們收藏了不少珍貴罕見的書籍，要是因為一個隨意翻閱的訪客而遺失，那可就太悲劇了。不過我得先提醒您，您想找的東西可能不太好找。許多書都還沒編目，除非您非常清楚自己要找的是哪位抄寫者或哪個書名，否則恐怕找不到什麼對您有用的東西。

### (sub) DIAL_Z20#1162
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1164
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1165
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您知道這一帶有什麼不錯的客棧嗎？今晚要是能睡在冰冷地面以外的地方，我想我會睡得好一點。

### (sub) DIAL_Z20#1166
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有幾間。您可以去尋道崖的巴本旅舍試試，或者那間老臨水客棧。要不是我這裡還有職務在身，我倒有點想跟您們一起去住呢。不知道哪來的一個見習修士，最近老愛拿『託夢術』練手，害我好幾週都沒睡過一個好覺了。

### (sub) DIAL_Z20#1167
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 託夢術？

### (sub) DIAL_Z20#1168
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是一種能傳遞長距離訊息的法術。只有特定的法師才有這方面的天賦。不管是誰在施法，距離都不會太遠，因為那些影像相當清晰強烈。

### (sub) DIAL_Z20#1169
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們似乎想傳達什麼訊息？

### (sub) DIAL_Z20#1170
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也說不準。那些影像太零散了，不過這麼一想，我一直覺得你這位精靈朋友的臉有點眼熟。現在我知道為什麼了。他的臉就出現在那些託夢影像裡。

### (sub) DIAL_Z20#1171
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000018  (DIAL_Z20#1173)
- speaker=0  style=0
- effects:
    - SET flag 0x1eb6=1
- branches:
    - [event_bitmap_hi[22] (xor=0xf7 mask=0x0b mode=2 chapters=-)] -> node 4278256128
    - [flag 0x9c45 in [3024..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1174
- speaker=0  style=0
- effects:
    - event_bitmap_hi[22] bitop
    - SET flag 0x0082=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1175
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 134135 (GoodBye target)
- branches:
    - [flag 0x007d in [3182..2]] -> node 4294901761
    - [flag 0x007e in [4860..2]] -> node 4294901761
    - [flag 0x007f in [6230..2]] -> node 4294901761
    - [flag 0x0080 in [7696..2]] -> node 4294901761
    - [flag 0x0081 in [8505..2]] -> node 4294901761
    - [flag 0x0082 in [10771..2]] -> node 4294901761
    - [flag 0x0083 in [12257..2]] -> node 4294901761
    - [flag 0x0084 in [13530..2]] -> node 4294901761
    - [flag 0x0085 in [14690..2]] -> node 4294901761

### (sub) DIAL_Z20#1176
- speaker=0  style=0
- effects:
    - SET flag 0x1aa9=1
    - bind speaker-name slot (kind=1 sub=5)
    - bind speaker-name slot (kind=2 sub=1)
    - RAISE Crossbow Acc of member#1 by 2560
    - RAISE Crossbow Acc of member#2 by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1177
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞魯莎親王好幾次跟我提過，您是他認識的人裡頭箭術最精湛的一位。

### (sub) DIAL_Z20#1178
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞魯莎以前也常跟他妹妹卡琳說，他們父親打算把她綁在『克朗多榮耀』號的主桅上，好讓奎格人經過港口時拿她當靶子練習。這可不代表那是真的。

### (sub) DIAL_Z20#1179
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我也不是神偷吉米了。公爵大人，您太謙虛了。

### (sub) DIAL_Z20#1180
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就算我弓箭用得還算順手，你們感興趣的理由是什麼？

### (sub) DIAL_Z20#1181
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我原本希望您能給洛奇跟我一點指點。我們倆都該學學怎麼更有效地使用十字弓。

### (sub) DIAL_Z20#1182
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，既然莫瑞德人這會兒還沒直接殺到我們頭上，我想我大概能教你們一點東西……

### (sub) DIAL_Z20#1183
- speaker=0  style=0
- effects:
    - advance in-game time by 1800
- branches:
    - [always] -> node 0 (no jump)
- text: 馬丁瞄準十字弓，扣下扳機。  羽毛從高處飄落，一隻沒了氣息的麻雀撞穿樹枝墜地，一支弩箭俐落地貫穿了牠的頭。牠碰到地面之前，其實早已斷了氣。  「這太厲害了，」詹姆士說。「這個距離，我還以為根本不可能射中呢。」  「不，」馬丁說，神情有些高深莫測地蹲下身，摸了摸腳邊的鳥。「我曾在兩倍遠的距離擊中過牠們，所以這頂多只能算困難而已。」  他先把十字弓遞給詹姆士，接著遞給洛克利爾，一邊指導他們嘗試同樣的射擊。  「你們倆都有些進步了，」馬丁說。「照今天這樣繼續練下去，你們倆都能成為出...

### (sub) DIAL_Z20#1184
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1186
- speaker=0  style=0
- effects:
    - SET flag 0x007f=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1187
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 以我們現在的位置來說，裂界機在哪個方向？離這裡近嗎？

### (sub) DIAL_Z20#1188
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也不確定。為了逃離莫瑞德人的營地，我鑽進他們一輛補給車後頭一堆帆布袋底下藏了起來。走了幾個鐘頭後，他們停下車方便，我才趁機逃了出來。不過我記得出發時，好像聽見過水流的聲音。

### (sub) DIAL_Z20#1189
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，你們當時在瀑布或河流附近……至少這給了我們一個搜索的方向。還有沒有什麼我們該知道的？

### (sub) DIAL_Z20#1190
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽那些趕車人的對話，我感覺自己並不是唯一一個意外闖過那台機器的人。看樣子有個反叛的莫瑞德氏族領袖也經過那裡，給他們添了不少麻煩，接著往南前往他們某位軍閥正在集結、準備攻打賽瑟儂的地方。他們對這人依然逍遙在外相當不滿。我倒希望自己能親自找到他，問他幾個問題。

### (sub) DIAL_Z20#1191
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 知道南邊這位軍閥是誰嗎？

### (sub) DIAL_Z20#1192
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想是迪勒肯的兒子莫萊伍夫，不過不太確定。他們把名字丟來丟去的速度太快，我聽得有點吃力。我的莫瑞德語已經不像從前那麼靈光了。

### (sub) DIAL_Z20#1193
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1195
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1196
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 賽瑟儂跟莫瑞德人到底有什麼過節？這已經是他們第二次進攻那裡了，我一直搞不懂十年前他們為什麼要打那裡。賽瑟儂除了一堆廢墟，什麼都沒有。

### (sub) DIAL_Z20#1197
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 至少上次我們還有軍隊擋在他們前頭。就算強行軍，亞魯莎親王的部隊也還要好幾天才能趕到，等他們到了肯定也已經筋疲力盡……

### (sub) DIAL_Z20#1198
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……這麼一想，迪勒肯何必興師動眾帶一支大軍？要是他預期能繞到我方防線後方抵達賽瑟儂，大可直接走進去、拿走他想要的東西，再轉身毫髮無傷地穿過那道裂界之門——除非他料到那裡會有別人在！他以為賽瑟儂那裡會有誰？這到底是什麼意思？

### (sub) DIAL_Z20#1199
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這代表他們上次進犯並沒有拿到想要的東西。這也代表迪勒肯已經監視賽瑟儂好一段時間了，說不定從上一場戰役結束以來就沒間斷過。他知道菲力普扈從麾下的人會擋在路上……

### (sub) DIAL_Z20#1200
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 菲力普扈從麾下的人？一個ñ扈從怎麼會領軍發動反攻？

### (sub) DIAL_Z20#1201
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在跟你解釋這個要花太多時間了。只能說，我看迪勒肯跟他手下一到賽瑟儂，日子恐怕不會好過。要是我們運氣好，他們會被拖住足夠久的時間，讓亞魯莎有機會開始蠶食他們的側翼。

### (sub) DIAL_Z20#1202
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1204
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1205
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看得出唯一對我們有利的一點，就是我們跟莫瑞德人其實處境相當——半斤八兩。雙方都沒有穩定的補給來源，而他們還得預留一部分，好在時機來臨時撤回北境。

### (sub) DIAL_Z20#1206
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 前提是他們真打算撤退。他們上次來的時候，可沒表現出多少撤退的意願。給你們一點建議：要是遇上任何糧食，我建議你們留著別放手。我們已經找到他們好幾處糧食儲藏點，跟在北衛城一樣下了毒，而眼下兩支大軍同時行經此地，我看糧食很快就會變得緊缺。這選項聽起來不太愉快，但你們恐怕得考慮從陣亡的莫瑞德人身上搜刮糧食。

### (sub) DIAL_Z20#1207
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1209
- speaker=0  style=0
- effects:
    - event_bitmap_hi[37] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1210
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我開始有點懷念以前在克朗多幫德拉西大人跑腿當差的日子了。我已經好久沒運動得這麼激烈了。  話說回來，你跟我們提過的那些哥布林在哪？

### (sub) DIAL_Z20#1211
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 塔姆尼怎麼樣了？找到他了嗎？

### (sub) DIAL_Z20#1212
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 找到了，不過費了點額外的工夫，才說服他願意回北衛城。他鄭重承諾會回去，我也相信他會。我們談了很久。

### (sub) DIAL_Z20#1213
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在我懂為什麼亞魯莎這麼看重你們了。要是我自己，恐怕不會相信這是辦得到的事。不過話說回來，就像俗話說的，我們前頭還有一大段苦活要幹。已經有一支哥布林弓箭隊移防到山口，試圖在那裡站穩腳跟。要是讓他們紮下根，等莫瑞德人一擁而入，恐怕就再也拔不掉了。我們得查清楚，等戰事一開，他們會怎麼佈署。

### (sub) DIAL_Z20#1214
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，那我們去抓他們的頭頭，帶回北衛城地牢用燒紅的鐵棍好好『招待』一番。告訴我們去哪找他，他就歸您了。

### (sub) DIAL_Z20#1215
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不行。他們一發現頭頭失蹤，就會改變戰術。不，我需要的是整體作戰計畫，我敢打賭那計畫還放在拉格蘭姆。

### (sub) DIAL_Z20#1216
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵借給您多少名斥候？

### (sub) DIAL_Z20#1217
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 眼下大約有二十人在外頭執行任務。怎麼問這個？

### (sub) DIAL_Z20#1218
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那您應該不會太想念我們三個吧。我們這就去拉格蘭姆，設法幫您把那份計畫弄到手。

### (sub) DIAL_Z20#1219
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們打算大搖大擺穿過一整支哥布林弓箭隊，走進莫瑞德人集結的城裡，直接走到敵軍首領面前說：「ñ勞ñ駕ñ可ñ否ñ借ñ看ñ您ñ的ñ計畫？」

### (sub) DIAL_Z20#1220
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記得我曾經在喬科．瑞德本跟居伊．杜．巴斯泰拉圍城期間，把未來的克萊迪公爵、王子跟公主，還有西方艦隊的海軍上將，一個個偷偷送出克朗多。我想弄到一張破紙應該不成問題。

### (sub) DIAL_Z20#1221
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看要是亞魯莎親王不打算哪天封你做克朗多公爵，大概早就把你當瘋子處決了。好吧，去把那份文件弄到手，小心點。我在這裡等你們。

### (sub) DIAL_Z20#1222
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1224
- speaker=0  style=0
- effects:
    - event_bitmap_hi[20] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1225
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們找到的莫瑞德人鎖箱，裡頭的糧食都下了毒。外頭找到的箱子其實也不多。

### (sub) DIAL_Z20#1226
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們大概已經找到大部分了，這方面倒不用太擔心。我還有件別的事要你們去辦。  男爵在北衛城雇了一位吟遊詩人，叫塔姆尼。我們一得知莫瑞德人開始從拉格蘭姆往北衛城山口移動，他就收拾好所有東西，半夜不告而別了。男爵堅持要把他找回來。

### (sub) DIAL_Z20#1227
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵也跟我們提過這個塔姆尼，不過為什麼非得把他找回來不可？士兵們或許會覺得有點被背叛，不過要是他們的士氣真這麼脆弱……

### (sub) DIAL_Z20#1228
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵不久前傳話說，今早在城堡範圍內發現了一名夜鷹會成員，而且有跡象顯示可能還有其他人。這消息自然傳開了，士兵們對整件事都很緊張。塔姆尼從沒宣誓效忠過，這一點也讓事情更加雪上加霜。

### (sub) DIAL_Z20#1229
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 而且他有可能跟夜鷹會有牽連。我明白了。

### (sub) DIAL_Z20#1230
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 找到他，盡可能把他帶回北衛城，不過別讓他察覺你們起了疑心，不然他可能會逃跑。  加博特的一名斥候跟我說，北邊可能有哥布林在活動，你們辦完事就趕快回來，我可能需要你們幫忙。

### (sub) DIAL_Z20#1231
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1233
- speaker=0  style=0
- effects:
    - SET flag 0x1aaf=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1234
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說……加博特男爵要我們在圍城開始前向您報到聽候差遣。您要我們去哪？

### (sub) DIAL_Z20#1235
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我正打算來點小樂子……派特魯斯，你的莫瑞德語怎麼樣了？

### (sub) DIAL_Z20#1236
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 公爵大人，您說的是哪個莫瑞德語？我床底下那個，還是每天早上幫我做早飯那個？

### (sub) DIAL_Z20#1237
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是不可思議。吉米，是我多心了，還是你也覺得派特魯斯讓你想起我們倆都認識的某位海軍上將？

### (sub) DIAL_Z20#1238
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看他跟阿莫斯．特拉斯克要不就是一見如故，要不就是恨不得把對方吊死在絞架上……  我想公爵的意思是，派特魯斯，你莫瑞德語說得怎麼樣了？

### (sub) DIAL_Z20#1239
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我明明清楚得很，別跟我裝蒜，你這隻宮廷耗子……我看得懂，可別要我把那些狗嚎似的鬼話唸出來。

### (sub) DIAL_Z20#1240
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我打的主意，用不著你唸出來。這附近有幾只箱子上刻著莫瑞德文字牌。我要你把上頭的密碼破解出來。我猜那些箱子裡裝的是莫瑞德人圍城時要用的口糧補給，不過我看他們大概想不到我們會動手腳。要是裡頭有口糧，就想辦法下毒，再放回箱子裡。辦完了就回來找我。

### (sub) DIAL_Z20#1241
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1243
- speaker=0  style=0
- effects:
    - SET flag 0x1ab0=1
    - event_bitmap_hi[21] bitop
    - REMOVE item 'x' cond=21
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1244
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬丁，計畫我們幫您弄到手了。可惜您沒跟我們一起去，我們玩得可開心了。

### (sub) DIAL_Z20#1245
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕沒多少時間再玩樂了。我的直覺告訴我，他們這幾天之內就會發動攻勢。  在我們回城堡之前，我想請你們三個幫我查一件事。我收到一張來歷不明的字條，說有一隊莫瑞德幻術師已經潛入北衛城後方。我想派特魯斯應該最清楚該怎麼對付他們。

### (sub) DIAL_Z20#1246
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那群尖耳朵的百合花啃食族，就愛偷我的點子！加博特男爵之前就叫我研究類似的東西，可我一直搞不定裡頭的毛病……難怪我這幾天老覺得嘴皮子癢……不過要是讓咱們撞上他們，我這有點東西，保證一眨眼工夫就能讓他們屁股開花。

### (sub) DIAL_Z20#1247
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 寫字條的人沒說明他們具體在哪，所以麻煩你們三個往西南方向繞一圈，看看能找到什麼。辦完之後回來，我們就一起前往城堡。

### (sub) DIAL_Z20#1248
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1250
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1251
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德法師一夥，解決了。我們找到他們了，公爵大人。

### (sub) DIAL_Z20#1252
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很好。我要你們三個趕快先去城堡。今天他們已經擊退了一波試探性的攻擊，我看男爵這會兒正需要你們幫忙。我得先查清楚我們一名失蹤斥候的下落。我盡快趕過去跟你們會合。

### (sub) DIAL_Z20#1253
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000019  (DIAL_Z20#1255)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eaa=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483667 (GoodBye target)
- branches:
    - [flag 0x0088 in [15229..2]] -> node 4294901761
    - [flag 0x0089 in [16056..2]] -> node 4294901761
    - [flag 0x008a in [17423..2]] -> node 4294901761
    - [flag 0x008b in [18659..2]] -> node 4294901761
    - [flag 0x008c in [19737..2]] -> node 4294901761
    - [flag 0x008d in [21129..2]] -> node 4294901761
    - [flag 0x008e in [21513..2]] -> node 4294901761
    - [flag 0x008f in [23184..2]] -> node 4294901761

### (sub) DIAL_Z20#1256
- speaker=0  style=0
- effects:
    - SET flag 0x0061=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1257
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 話說回來，什麼時候會有追求者把妳娶走啊？有沒有哪個名聲還算不錯的？

### (sub) DIAL_Z20#1258
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有兩個，父親一個都不喜歡，不過話說回來，我喜歡誰他從來就沒喜歡過。一個是麥倫，父親的訟務代理人，跟他女兒艾米就住在卡瓦爾堡外頭不遠。他多少沾點貴族邊，因為他哥哥在某個地方當伯爵，不過父親覺得這層關係太薄弱，不值得考慮。

### (sub) DIAL_Z20#1259
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那第二個追求者呢？

### (sub) DIAL_Z20#1260
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他是個從肯廷拉什來的商人，叫納馮．杜桑多。我挺喜歡他的，雖然他有時候有點過於認真。我們很喜歡聊天，他老愛問我一些神話方面的問題。他也不介意女孩子愛讀書。

### (sub) DIAL_Z20#1261
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1263
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1264
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳父親人呢？我還挺意外他沒親自來指揮這次集結。

### (sub) DIAL_Z20#1265
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道……我們鬧翻了。我不知道什麼時候還能再見到他。我想他大概跟波斯維奇夫人一起待在集結區那邊，不過我也不確定。我現在對什麼事好像都不太確定了。

### (sub) DIAL_Z20#1266
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼？出了什麼事？

### (sub) DIAL_Z20#1267
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道現在還能相信誰了。我分不清誰在說真話，誰在騙我。  你還記得多年前我哥哥在酒窖意外中喪生的事嗎？

### (sub) DIAL_Z20#1268
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 記得……烏格妮，我……

### (sub) DIAL_Z20#1269
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他沒有死，歐文。父親發現內維爾其實是私生子，於是安排了那場意外，可內維爾並沒有因此喪命。後來一群壞人找到了他，本想拿他去勒索贖金，可內維爾知道父親不會付這筆錢。於是他想辦法用他的望遠鏡對付了那些人，然後……歐文，他回來了，成了我的一名追求者！自從我還是個小女孩，我就再沒見過他，他變了好多。我怎麼可能認得出來？他自稱納馮，我還以為……我還以為……我也不知道了……

### (sub) DIAL_Z20#1270
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噓……噓。妳語無倫次了，表妹。等妳冷靜下來一點，也許可以再跟我好好解釋這一切。我看妳需要休息一下。

### (sub) DIAL_Z20#1271
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1273
- speaker=0  style=0
- effects:
    - SET flag 0x0060=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1274
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 內維爾是怎麼死的，我記得不太清楚了。畢竟是很久以前的事了。

### (sub) DIAL_Z20#1275
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你人遠在提伯恩，本來也不可能知道太多細節。母親跟父親當時都悲痛欲絕，不想把他的死弄得沸沸揚揚。  內維爾當時在卡瓦爾坑道下面，父親派他去酒窖取一桶奎格酸酒。那天我們家裡正好有客人……

### (sub) DIAL_Z20#1276
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 卡瓦爾坑道？

### (sub) DIAL_Z20#1277
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你記得的……堡壘底下那個？那些彷彿綿延數哩的隧道？我們一直都不確定那到底有多長。我以前很喜歡一個人在裡頭的黑暗中散步，就只是想想事情，享受獨處的時光。那也是我如今最想念堡壘的地方之一——再也沒有那些隧道可以讓我去玩了。  內維爾去取酒桶卻遲遲沒回來，父親便下坑道去找他。酒先上了，接著是開胃菜，然後是第一道主菜，父親還是沒回來。第二道主菜上了，第三道，父親這才終於出現。他告訴我們隧道塌了，內維爾被困在裡頭。我們始終沒能把瓦礫挖開夠深，找回他的遺體。

### (sub) DIAL_Z20#1278
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1280
- speaker=0  style=0
- effects:
    - SET flag 0x008d=1
    - SET flag 0x008a=1
    - SET flag 0x00a9=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1281
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳父親說他不喜歡妳這位追求者納馮，是因為他打聽家族傳說的時候，老是勾起堡壘那些痛苦的回憶——妳母親的死，還有那場燒毀堡壘的大火……

### (sub) DIAL_Z20#1282
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼怪罪納馮並不公平。他關心我們家族，也關心我，自然會好奇堡壘的事。你要是打算娶一個人，難道不會對她的家族歷史感興趣嗎？難道不會想像了解自己家人一樣了解她嗎？  不過真正困擾父親的，與其說是母親的死，倒不如說是多年前內維爾的死。可父親偏偏死咬著一個荒唐的巧合不放……

### (sub) DIAL_Z20#1283
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 巧合？什麼巧合？

### (sub) DIAL_Z20#1284
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 納馮姓杜桑多。跟當初替父親蓋那座後來坍塌的酒窖的人，姓氏一模一樣。父親就因為他碰巧同姓，就對他心懷芥蒂！這實在……太荒唐了。

### (sub) DIAL_Z20#1285
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1287
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1288
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們看起來有點狼狽，還請見諒，我們正在追查一樁發生在羅姆尼的謀殺案。已經查了好一陣子了。

### (sub) DIAL_Z20#1289
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們覺得凶手逃到卡瓦爾堡來了嗎？

### (sub) DIAL_Z20#1290
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還不確定。目前我們只知道，這案子可能跟我們在屍體附近發現的一副黃銅望遠鏡，或是一隻銀蜘蛛有關。

### (sub) DIAL_Z20#1291
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那副望遠鏡上該不會刻著一顆星星吧？

### (sub) DIAL_Z20#1292
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記不清楚了。怎麼問這個？這很重要嗎？

### (sub) DIAL_Z20#1293
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 身為家族的一份子，你對家族的傳說知道得可真不多啊……我們以前有一副望遠鏡，擺在堡壘門廳的玻璃櫃裡。傳說只要一個人心裡想著對的東西，就能用這副望遠鏡窺探別人的心思。這東西在我們家傳了好幾代，卻在多年前內維爾死於酒窖意外前後消失了。父親指控是工匠偷走的。

### (sub) DIAL_Z20#1294
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那要心裡想著什麼，望遠鏡才會起作用？

### (sub) DIAL_Z20#1295
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道。內維爾以前老愛逗我，說他知道該想什麼、還說他能用它，可他從沒真的用過。畢竟這終究只是個傳說。

### (sub) DIAL_Z20#1296
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1298
- speaker=0  style=0
- effects:
    - SET flag 0x008e=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1299
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳父親說納馮老纏著妳問家族傳說的事……

### (sub) DIAL_Z20#1300
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他對科瓦利斯家族的一切都很著迷。他會問望遠鏡是打哪來的、堡壘立了多久，還有加爾達復仇劍後來去了哪裡。我們什麼都聊。

### (sub) DIAL_Z20#1301
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1303
- speaker=0  style=0
- effects:
    - SET flag 0x00a0=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1304
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 加爾達復仇劍跟我們的家族歷史有什麼關係？我還以為那是這裡還只有精靈居住那個年代的某種傳說。

### (sub) DIAL_Z20#1305
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大家都知道的那部分傳說，確實跟精靈有關，不過據我們家族的傳說，加爾達復仇劍曾有一段時間，是落在我們家族手裡的。  卡瓦爾堡的夫人在她十四歲生日那天，收到精靈侍女送的一份特殊禮物——一把能讓她丈夫科瓦利斯領主在世人中揚名立萬的劍。她興沖沖地跑去他的寢室，想把這份大禮獻給他，可一推開門，一股巨大的邪惡氣息便攫住了她。劍身在她手中開始發出幽光，她尖叫著把劍高舉過頭，一劍砍下了丈夫的頭顱。接著，她一間又一間地闖進孩子們的房間，直到把她跟科瓦利斯領主所生的孩子全部殺光，做完這一切之後，...

### (sub) DIAL_Z20#1306
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是……迷人的故事。妳該不會剛好把它擱在家裡什麼地方吧？

### (sub) DIAL_Z20#1307
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 對我好一點，不然我可能會把這把劍送給你！不，傳說接下來說，後來家族其他分支又重演了同樣的悲劇，這把劍最終才被移出家族。我手上有一本書記載了它後來去了哪，不過那本書我借給納馮看了。

### (sub) DIAL_Z20#1308
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這就奇怪了。我還以為加爾達復仇劍應該只對莫瑞德人起作用。

### (sub) DIAL_Z20#1309
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這只是個傳說。誰說傳說就得前後一致了！

### (sub) DIAL_Z20#1310
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1312
- speaker=0  style=0
- effects:
    - SET flag 0x0089=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1313
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡有些酒館老闆擔心，要是士兵們再不快點喝上點酒，恐怕會鬧出暴動。我記得妳父親以前存了不少舶來的美酒……

### (sub) DIAL_Z20#1314
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是很久以前的事了，在……我們能不能先別談這個？我頭痛得厲害，正竭盡所能幫蘿娜照顧孩子們。

### (sub) DIAL_Z20#1315
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 平時我不會逼問這種事，可眼下情況實在是燃眉之急。要是不趕快把這幾個人灌醉，這裡恐怕要出的亂子，說不定比北衛城那邊的戰事還要嚴重。

### (sub) DIAL_Z20#1316
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你得去找父親問問。他或許能替你去跟波斯維奇夫人談談。我知道她以前常從她的私藏酒窖送酒給我們……

### (sub) DIAL_Z20#1317
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000017  (DIAL_Z20#1319)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1ebe=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483665 (GoodBye target)
- branches:
    - [flag 0x0090 in [24135..2]] -> node 4294901761
    - [flag 0x0091 in [24591..2]] -> node 4294901761
    - [flag 0x0092 in [25359..2]] -> node 4294901761
    - [flag 0x0093 in [26036..2]] -> node 4294901761
    - [flag 0x0094 in [26564..2]] -> node 4294901761
    - [flag 0x0095 in [27986..2]] -> node 4294901761

### (sub) DIAL_Z20#1320
- speaker=0  style=0
- effects:
    - SET flag 0x1abc=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1321
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你能不能幫我帶個口信給亞魯莎親王？

### (sub) DIAL_Z20#1322
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可以試試。是什麼口信？

### (sub) DIAL_Z20#1323
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就跟他說，我們還沒抵達羅姆尼的黑羊酒館，不過我會盡快傳話給他。

### (sub) DIAL_Z20#1324
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這應該不是什麼難事。他一回來，我就轉告他。

### (sub) DIAL_Z20#1325
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1327
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1328
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是亞魯莎親王不在這裡，那他肯定已經開始了……

### (sub) DIAL_Z20#1329
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 開始什麼？

### (sub) DIAL_Z20#1330
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，我只是自言自語。方便的話，你能幫我轉告他一件事嗎？這件事他非聽到不可。

### (sub) DIAL_Z20#1331
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是什麼口信？

### (sub) DIAL_Z20#1332
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟他說，羅姆尼那場宴會因為主人病倒取消了，現在我們正在找他那隻飛走的寵物長尾鸚鵡。等我們找到棲架，就會去母親家跟他喝茶碰面。

### (sub) DIAL_Z20#1333
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不太確定我聽懂了……

### (sub) DIAL_Z20#1334
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 但親王會懂的。我不是有意故弄玄虛，只是眼下這件事，最好只有我們兩人知道就好。

### (sub) DIAL_Z20#1335
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1337
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1338
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我離開之後克朗多有發生什麼事嗎？還是說整座城都閒得發慌，就等著我回來？

### (sub) DIAL_Z20#1339
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實沒什麼不尋常的。我聽過最刺激的事，就是有幾個港口似乎爆發了奎格熱，不過大家都不覺得情況會太嚴重。頌恩神殿的祭司已經派人到碼頭那邊處理任何出現的病例，宮廷守衛也被告知要留意任何看起來出現幻覺的人。大家都認為疫情應該會被控制在克朗多以北的區域。

### (sub) DIAL_Z20#1340
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1342
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1343
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 話說回來，我什麼時候才能見見您這位傾城的女兒啊？我聽過不少關於蓋米娜的事，可一直忙得抽不出空見她一面。

### (sub) DIAL_Z20#1344
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看你見到她的時間，大概跟我差不多。她十有八九正跟著帕格跟馬卡拉在宮裡到處轉。只要有機會聽她父親談論法術，她就會立刻黏到他身邊。再不然，也可能是在躲亞魯莎家那對雙胞胎。她現在對男孩子還沒什麼興趣。

### (sub) DIAL_Z20#1345
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1347
- speaker=0  style=0
- effects:
    - GIVE item 'H' cond=3 to party (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1348
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們得弄點吃的。卡杜今天爐子上燉的是什麼，還是我不該問？

### (sub) DIAL_Z20#1349
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實王宮的廚房現在沒開伙。亞魯莎親王一直是私下用餐，其他人手也被告知有需要可以自己去廚房拿食材，所以卡杜這陣子基本上沒事做。我大概可以幫你們弄幾份乾糧，前提是他已經備好了一些。

### (sub) DIAL_Z20#1350
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的不必了。您跟帕格難得來克朗多度假，該是反過來才對。

### (sub) DIAL_Z20#1351
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，我堅持。一下子就好。

### (sub) DIAL_Z20#1352
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 她真是讓我讚嘆不已。我聽帕格說，她把星塢島上所有學生都當成自己的孩子一樣照顧。換作是我，光是兩個孩子加上世上法力最高強的法師要照料，就該忙得團團轉了。

### (sub) DIAL_Z20#1353
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文低頭看著自己的鞋子。  他抬頭瞥了詹姆士一眼，說道：「她聽起來是位好夫人。」這位紳爵正要回話，卻聽見卡塔拉漸漸走近的輕微腳步聲。他用手背掩著嘴，低聲說：「確實是。」

### (sub) DIAL_Z20#1354
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 卡塔拉，妳又回來了？真快。

### (sub) DIAL_Z20#1355
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正好有些已經備好的，我就順手拿給你們了。當然，我先確認過是新鮮的。

### (sub) DIAL_Z20#1356
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1358
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1359
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我知道星塢島有不少工匠已經開始把學院的產品外銷出去了。這附近有沒有什麼買魔法物品的好去處？

### (sub) DIAL_Z20#1360
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 附近最有名的一間，是薩斯伊夏修道院裡一個叫『星塢分部』的小地方。正式來說他們跟學院沒有任何關係，不過我們也拿他們用這個名號沒什麼辦法。另外還有個叫達貝的人跟我們進貨，不過他住得挺遠的，我記得是在羅姆尼以北的地方。

### (sub) DIAL_Z20#1361
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000020  (DIAL_Z20#1363)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eab=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483668 (GoodBye target)
- branches:
    - [flag 0x0096 in [28685..2]] -> node 4294901761
    - [flag 0x0097 in [29996..2]] -> node 4294901761
    - [flag 0x0098 in [30890..2]] -> node 4294901761
    - [flag 0x0099 in [31899..2]] -> node 4294901761
    - [flag 0x009a in [33395..2]] -> node 4294901761
    - [flag 0x009b in [33998..2]] -> node 4294901761

### (sub) DIAL_Z20#1364
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1365
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是我不喜歡您現在這棟新房子，不過堡壘後來怎麼了？

### (sub) DIAL_Z20#1366
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這棟宅子只是暫時的落腳處，姪兒。我們可沒打算像尋常百姓一樣，就這麼一直住在卡瓦爾。至於堡壘嘛，三年前的一個晚上，一個粗心的侍女把一盞燈丟在西牆掛毯旁邊沒人看管。你記得那些掛毯吧，歐文？有好幾百年歷史，是全王國最好的織工織出來的。轉眼間就燒了起來，連帶把堡壘剩下的部分也一起燒了。

### (sub) DIAL_Z20#1367
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我記得聽說過火災的事，可不知道堡壘居然整座燒成了平地。你們大家都能活下來，真是奇蹟。有搶救出什麼東西嗎？

### (sub) DIAL_Z20#1368
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們救出了我們自己，歐文，那才是那座城堡裡唯一真正有價值的東西。可惜引發那場大火的那個姑娘沒能逃出來，不過烏格妮跟我都平安無事地逃了出來。我下令只留下地基的石頭，並封死了坑道入口。我們得繼續向前過日子。

### (sub) DIAL_Z20#1369
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼要大費周章做這些事……

### (sub) DIAL_Z20#1370
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我真的不想再談這件事了。這讓我非常悲痛，我寧可聊點別的。

### (sub) DIAL_Z20#1371
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1373
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1374
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鎮上住著一位錢莊放款人……

### (sub) DIAL_Z20#1375
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊蘇納圖斯，是啊，我跟他很熟。是個古怪的奎格人。

### (sub) DIAL_Z20#1376
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說您最近跟他有生意往來？

### (sub) DIAL_Z20#1377
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這關你什麼事？我該繳給國王的稅一分不少。

### (sub) DIAL_Z20#1378
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們想借點錢，想先確認打交道的是家信譽良好的商號。我想您要是跟他有過生意往來，存過什麼款，或許就能知道他為人誠不誠實。

### (sub) DIAL_Z20#1379
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊。做生意保持點戒心是個健康的做法。要回答你的話，我最近倒是沒借過錢，反而存了幾筆相當可觀的款項。多虧巴納斯神保佑，我幾筆眼光不錯的投資讓我賺得挺舒服的。伊蘇納圖斯會好好對待你們的。

### (sub) DIAL_Z20#1380
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1382
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1383
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伯爵大人，我要您給我一個直截了當的答案。您跟死亡公會有沒有任何關聯，是或不是？

### (sub) DIAL_Z20#1384
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是什麼胡說八道？！你憑什麼相信這種事有可能？

### (sub) DIAL_Z20#1385
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 納馮．杜桑多告訴我們，您多次雇用過刺客……

### (sub) DIAL_Z20#1386
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是當保鑣！要找人保護我，還有誰比那些以跟蹤盯梢為業的人更合適？可我從沒為了別的目的雇用過刺客公會的人。我雇的那些人，只負責看守我的莊園，保護我跟我女兒的人身安全。僅此而已。

### (sub) DIAL_Z20#1387
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您是怎麼聯絡到這些人的？

### (sub) DIAL_Z20#1388
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是請卡胡利神殿的祭司幫我引薦這些人來，所以我從來不知道該怎麼直接聯絡他們。堡壘燒毀後，我又請求增派人手，可祭司們跟我說，夜鷹會已經失去了神殿的信任，他們再也無法召喚夜鷹會的人來效力了。

### (sub) DIAL_Z20#1389
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1391
- speaker=0  style=0
- effects:
    - SET flag 0x008b=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1392
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您素來以厭惡納馮．杜桑多聞名。有什麼想跟我們分享的嗎？

### (sub) DIAL_Z20#1393
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你憑什麼認為我對烏格妮的追求者心懷敵意？

### (sub) DIAL_Z20#1394
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您向卡胡利神的祈願書上寫的。您要求讓納馮——您是怎麼寫的來著——瘋癲終老，直到白髮蒼蒼？

### (sub) DIAL_Z20#1395
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你花錢買通誰弄到那張字條的？你在神殿裡安插了眼線？

### (sub) DIAL_Z20#1396
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒那麼陰險，伯爵大人。看樣子卡胡利神殿今年收祈願書的人手腳有點慢。我們找到了您的字條，還有您的什一稅。您要是願意告訴我們，為什麼希望他發瘋，我就把這件小事拋到腦後。不然，我看我可以把這件事拿去跟杜桑多先生聊聊。

### (sub) DIAL_Z20#1397
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵大人，隨您的便吧。他早就知道我對他的看法了。我只是希望他離開我的家族，別再插手我們家的事。  他日夜纏著烏格妮，不停問她堡壘跟卡瓦爾坑道的事。大廳底下的隧道究竟延伸多遠？有沒有人詳細繪製過地圖？我的金庫裡有多少錢？我的行程安排如何？我都跟誰見面？他的問題沒完沒了。  我在那座該死的堡壘裡失去了一位妻子，我希望這件事就此了結。我再也不想聽到任何相關的問題！紳爵大人，您能理解嗎？他不斷勾起我寧願塵封的回憶跟情緒。

### (sub) DIAL_Z20#1398
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1400
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1401
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您了解卡胡利神殿嗎？我們先前跟他們談過，他們似乎有一套要求信徒嚴格遵守的行為準則。

### (sub) DIAL_Z20#1402
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們說自己是卡胡利神殿的信徒。這座神殿其實沒有表面上看起來那麼嚴格，只要他們能收到信徒的什一稅就行。希望今年他們派來的收稅人，能比往年那幾位機靈一點。去年我藏起來的什一稅，他們差點就沒找到。

### (sub) DIAL_Z20#1403
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1405
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1406
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您年輕時不是當過納塔爾遊騎兵的斥候嗎？我記得以前去堡壘拜訪時，聽您講過這方面的故事。

### (sub) DIAL_Z20#1407
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那確實是很久以前的事了，早在你、烏格妮，甚至內維爾出生之前。我這雙眼睛可還沒退化。我光看一個人走路的樣子，就能準確判斷他身上帶了多少東西；光看他拔劍出鞘的動作，就能看出他劍術有多高明。

### (sub) DIAL_Z20#1408
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來是門很有用的本事。有沒有機會請您教教我們一點？

### (sub) DIAL_Z20#1409
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別胡鬧了。我花了五年才練成一名斥候。你指望我一個下午就把這一身本事全教給你們？

### (sub) DIAL_Z20#1410
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想您說得對。不過我自己也算是個不錯的觀察家了。這樣吧，我跟您打個賭。您要是能教我什麼我不知道的東西，我就付您金幣。

### (sub) DIAL_Z20#1411
- speaker=9  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [35044..2]] -> node 4294901761
    - [flag 0x0101 in [36284..2]] -> node 4294901761
- text: 這賭我接了，不過我可不喜歡浪費時間。兩百枚金幣，不然免談。您接受這個賭注嗎？

### (sub) DIAL_Z20#1412
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [35073..2]] -> node 4294901960
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1413
- speaker=0  style=0
- effects:
    - SET flag 0x1ac7=1
    - TAKE gold -2000
    - RAISE Assessment of party by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1414
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您準備好了，我隨時奉陪。

### (sub) DIAL_Z20#1415
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們到外頭去，空間比較大……

### (sub) DIAL_Z20#1416
- speaker=0  style=6
- effects:
    - advance in-game time by 9000
- branches:
    - [always] -> node 0 (no jump)
- text: 伯爵伸開雙臂。  「我用哪隻手打鬥？」伯爵問道。  @0瞇起眼睛，距離讓他難以準確判斷。這幾個鐘頭裡，伯爵毫不客氣地一再訓斥他評估敵人實力的能力太差。  「我猜是您的右手。」  「很好，」伯爵說。「為什麼？」  「您的劍掛在左邊腰上，」@0平淡地答道。雖然這是顯而易見的答案，伯爵卻對這種直白的推論不甚滿意。他察覺伯爵又要開始長篇大論地說教，忙不迭補上一句：「還有您右手拇指指腹跟指根的老繭。」  伯爵點了點頭，垂下雙手。「我浪費夠多時間了。你輸了這個賭，小子。我們回屋裡去吧。」

### (sub) DIAL_Z20#1417
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1418
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1419
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這賭我倒想接，可惜我拿不出這筆錢。

### (sub) DIAL_Z20#1420
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你要是拿不出賭注，就別來跟我打什麼賭。

### (sub) DIAL_Z20#1421
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1422
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1423
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我有時候賭性挺大的，不過這次我可沒那麼大的膽子。

### (sub) DIAL_Z20#1424
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這樣也好，反正這個賭你本來也是要輸的。

### (sub) DIAL_Z20#1425
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000016  (DIAL_Z20#1427)
- speaker=3  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1eb5=1
    - bind speaker-name slot (kind=0 sub=3)
    - push return-address key 2149483664 (GoodBye target)
- branches:
    - [flag 0x009c in [36620..2]] -> node 4294901761
    - [flag 0x009d in [37066..2]] -> node 4294901761
    - [flag 0x009e in [37765..2]] -> node 4294901761
    - [flag 0x009f in [38367..2]] -> node 4294901761
    - [flag 0x00a0 in [38850..2]] -> node 4294901761
    - [flag 0x00a1 in [39197..2]] -> node 4294901761
    - [flag 0x00a2 in [39904..2]] -> node 4294901761

### (sub) DIAL_Z20#1428
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1429
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟我們同行的有一名叫戈拉斯的莫瑞德人。他真如自己所說的那樣嗎？我們信得過他嗎？

### (sub) DIAL_Z20#1430
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他並非自稱的那個身分，儘管就連他自己，恐怕也不知道自己心中的那個謊言。他會是你們堅實的盟友，我甚至相信，他終將成為如今咒罵他名字的同胞的守護者。只要他有勇氣放下心中的痛苦，一段偉大的命運正等待著他。

### (sub) DIAL_Z20#1431
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1433
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1434
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯跟我們提過一位莫瑞德人首領，迪勒肯。他會不會越過世界之齒，進攻王國？

### (sub) DIAL_Z20#1435
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯永遠不會親自跨越王國與北境之間的疆界，但他會透過背叛的手段，同時對王國跟他自己的北境諸國造成重創。

### (sub) DIAL_Z20#1436
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你能不能說得更具體一點？他會在哪裡動手？這份背叛的本質又是什麼？

### (sub) DIAL_Z20#1437
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看見的並非你們想像中的那種未來，而是『可能』成為的未來。我只知道，迪勒肯正跟六名法師策劃一場騙局，而這件事關乎王國的命運。

### (sub) DIAL_Z20#1438
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1440
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1441
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 羅姆尼發生了一樁謀殺案，我們正在追查凶手。我們需要他的名字。

### (sub) DIAL_Z20#1442
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們以為自己在尋找一個名字，但那並非你們真正想知道的。正如你們所猜想的，你們找到的那兩件物品，都是謀殺案的線索，只是其中一件指向的，是一樁你們可能根本沒察覺已經發生過的謀殺。

### (sub) DIAL_Z20#1443
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哪一件物品能帶我們找到我們要找的東西？

### (sub) DIAL_Z20#1444
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那副黃銅望遠鏡會為你們指路。追查它的下落，通往目的地的路便會自然浮現。

### (sub) DIAL_Z20#1445
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1447
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1448
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們需要找一本書，叫『馬克羅斯之書』。要怎麼找到它？

### (sub) DIAL_Z20#1449
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們追逐的是幻影，因為你們口中那本書並不存在，儘管它的精神依然熾烈燃燒著。

### (sub) DIAL_Z20#1450
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不明白。妳的意思是，我們在找的東西是活的？

### (sub) DIAL_Z20#1451
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 去薩斯的伊夏修道院，找出地窖裡收藏的知識。你們的答案就在那裡。

### (sub) DIAL_Z20#1452
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1454
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1455
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們得知有一件武器，或許能助我們一臂之力。它在哪裡能找到？

### (sub) DIAL_Z20#1456
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 加爾達復仇劍，藏在一處連精靈跟莫瑞德人都畏懼踏足的地方——一處古老之地，曾是人稱瓦爾赫魯者的家園。

### (sub) DIAL_Z20#1457
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1459
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1460
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帕格去了哪裡？這跟『馬克羅斯之書』有什麼關係？

### (sub) DIAL_Z20#1461
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帕格被一個他以為是朋友的人背叛了。此刻，他正遊蕩在一個遙遠的世界，尋找他的女兒蓋米娜，但他找不到她。在他尋找的過程中，他將喚醒自瓦爾赫魯縱橫宇宙征戰以來便沉睡至今的力量。『馬克羅斯之書』，將會是你們拯救他的憑藉。

### (sub) DIAL_Z20#1462
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可我要怎麼幫得上忙？要是連他都保護不了自己，我跟戈拉斯能做的恐怕不多。

### (sub) DIAL_Z20#1463
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他跌倒之處，正是你成長茁壯之地。這條路早已為你鋪就。

### (sub) DIAL_Z20#1464
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1466
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1467
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們要怎麼樣才能讓一個鬼魂安息？附近有個女孩正被一個鬼魂纏得心驚膽戰，我希望我們或許能幫上她的忙。

### (sub) DIAL_Z20#1468
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那被驚擾的亡魂，必須重新安葬回賈瑞德的墓中。到萊頓尋回他的手，將它交還給賽瑟儂英烈長眠的土地。如此，她的恐懼便會終結。

### (sub) DIAL_Z20#1469
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

## node 2000021  (DIAL_Z20#1471)
- speaker=255  style=0  flags=ASK-ABOUT keyword menu
- effects:
    - SET flag 0x1ea9=1
    - bind speaker-name slot (kind=0 sub=30)
    - push return-address key 2149483669 (GoodBye target)
- branches:
    - [flag 0x00a3 in [40432..2]] -> node 4294901761
    - [flag 0x00a4 in [44593..2]] -> node 4294901761
    - [flag 0x00a5 in [45573..2]] -> node 4294901761
    - [flag 0x00a7 in [46495..2]] -> node 4294901761
    - [flag 0x00a9 in [47992..2]] -> node 4294901761
    - [flag 0x00aa in [48460..2]] -> node 4294901761
    - [flag 0x00ab in [49420..2]] -> node 4294901761

### (sub) DIAL_Z20#1472
- speaker=0  style=0
- effects:
    - SET flag 0x1cf7=1
    - event_bitmap_hi[13] bitop
    - SET flag 0x1a8a=1
    - SET flag 0x1a8d=1
    - ACTION: request hotspot activation at player
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1473
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 烏格妮．科瓦利斯告訴我們，她把一本關於加爾達復仇劍的書借給了你。我能不能跟你借回來看看？

### (sub) DIAL_Z20#1474
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可惜這書不在我身上。我把它放在家裡了。

### (sub) DIAL_Z20#1475
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在家裡。你確定沒有把它隨手放到別的地方去？

### (sub) DIAL_Z20#1476
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然是借來的書，我把它收在一個非常安全的地方，確保它不會受損。

### (sub) DIAL_Z20#1477
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是不是像卡瓦爾坑道那種地方？我一直很好奇夜鷹會的頭目是什麼模樣，看來現在我們是面對面了。

### (sub) DIAL_Z20#1478
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有意思的結論。你是怎麼得出這個推論的？

### (sub) DIAL_Z20#1479
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們在卡瓦爾坑道裡找到了修道院院長的日記……在跟你幾個手下小小交過手之後。你先前提過，你認為科瓦利斯伯爵可能殺了自己的兒子，可我記得那具屍體根本沒被找到，而你對科瓦利斯家族又展現出一種百發百中的興趣。那種興趣，倒挺像一個被迫與家族分離的兒子才會有的？是你自己安排了那場『死亡』，還是你父親的手筆？

### (sub) DIAL_Z20#1480
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看該恭喜你才對。你辦到了我父親、他的手下，還有巴斯泰拉的王室分遣隊都辦不到的事。你確實是個聰明人。

### (sub) DIAL_Z20#1481
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼要加入夜鷹會，納馮？還是我該叫你內維爾？

### (sub) DIAL_Z20#1482
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 假設有那麼一位妻子，替她丈夫生下一個強壯、俊美又聰穎的兒子。這孩子長大的過程中，處處顯露出將來會是個優秀男子的跡象，只是總有些說不上來的不同。再假設，這孩子大約十一歲時，他的父親發現這孩子其實不是自己的親骨肉，而是另一個男人的兒子——一個私生子。在平民百姓之間，這算不上什麼大罪，但要是這位被蒙在鼓裡的父親，恰好是位貴族呢？那事情可就不一樣了，不是嗎？要是那位真正的生父，正是為了謀取權力，才刻意讓那位輕率的貴婦懷上這個孩子呢？

### (sub) DIAL_Z20#1483
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你成了繼承權的威脅，所以伯爵決定除掉你。他把你鎖進酒窖，你卻設法落入了夜鷹會的手中。

### (sub) DIAL_Z20#1484
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯。他們被亞魯莎親王擊潰後跑到卡瓦爾整頓，一開始還想拿我勒索贖金。等他們發現伯爵不肯付錢贖回我，便打算殺了我，可我說服了他們，說我擁有心靈方面的力量……

### (sub) DIAL_Z20#1485
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那副望遠鏡？

### (sub) DIAL_Z20#1486
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 它派上用場的次數可不只一兩次。它讓我掌控了夜鷹會，也讓我能預判我父親的動向。他當然以為我死了，可多年後納馮．杜桑多的出現，讓他變得神經兮兮。他認為我可能知道那樁醜聞，還怕我會把知道的事說出去。那樣就沒意思了。折磨自己的殺手，總比乾脆殺了他要有趣得多，你說是不是？我一把火燒了咱們家的堡壘之後，他更是坐立難安。失去那座堡壘是挺可惜，不過那是必要的犧牲……

### (sub) DIAL_Z20#1487
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這樣你就能掌控堡壘底下的洞窟了。既是你跟你手下絕佳的藏身之處，也是你跟你打交道的莫瑞德人絕佳的會面地點。

### (sub) DIAL_Z20#1488
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那些坑道範圍廣大，族人以外的人幾乎沒人知曉。再說，作為烏格妮的丈夫，我遲早會名正言順地成為它的主人。倒不是說我真打算圓房，伊夏神ó保佑，可別。她大概會在新婚之夜死於某種不太愉快的方式。悲劇似乎總愛纏上科瓦利斯家族。有了家族的財富，加上迪勒肯存放在伊蘇納圖斯那裡、又轉存進卡瓦爾堡的款項，我大可讓夜鷹會無限期地經營下去。

### (sub) DIAL_Z20#1489
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我要那把ó鑰匙，納馮。交出來。

### (sub) DIAL_Z20#1490
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許你想親自從我手裡搶過去。詹姆士紳爵，自從你剛到羅姆尼打聽夜鷹會的下落開始，我就一直在觀察你。這些年來，我從那些在你克朗多的夜鷹會肅清行動中倖存下來的人口中，聽過不少關於神偷吉米的傳聞。他們把你說得神乎其技。現在，該看看你能不能在戰鬥中，勝過一名ó真正的夜鷹會刺客了……

### (sub) DIAL_Z20#1491
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1492
- speaker=0  style=0
- effects:
    - END conversation, result=65535

### (sub) DIAL_Z20#1493
- speaker=0  style=0
- effects:
    - SET flag 0x0098=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1494
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵有什麼理由不喜歡你，納馮？

### (sub) DIAL_Z20#1495
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許他就是個過度保護的父親，誰知道呢？老實說，我還挺意外他沒雇一票夜鷹會的人來殺我。我問的問題，對他的胃口來說實在太多了。

### (sub) DIAL_Z20#1496
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你覺得他跟刺客公會有關係？

### (sub) DIAL_Z20#1497
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是眾所皆知的事，他身邊圍繞著夜鷹會的人。他們守著他的宅子、他的地產、卡瓦爾堡。每次我跟他女兒烏格妮相處，身後總跟著幾名刺客，只不過替伯爵辦事的時候，他們從不穿公會的服飾。

### (sub) DIAL_Z20#1498
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這一帶的居民怎麼都不管管這事？他們肯定不樂見夜鷹會的人在這一帶橫行吧。

### (sub) DIAL_Z20#1499
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們選擇睜一隻眼閉一隻眼。只要沒人殺到自己頭上，這事就跟他們不相干。我敢說，就連在克朗多也是這樣。

### (sub) DIAL_Z20#1500
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1502
- speaker=0  style=0
- effects:
    - SET flag 0x1a8a=1
    - SET flag 0x1a8d=1
    - SET flag 0x1cf7=1
    - ACTION: request hotspot activation at player
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1503
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我代表卡胡利神殿通知你，你已被逐出教門。神殿已正式與刺客公會斷絕一切關係，並將公布所有公會成員的身分。夜鷹會完了，納馮。儘管他們要求我取你性命，但只要你告訴我，哪裡能找到跟這次進攻有關的莫瑞德人通訊，我就饒你一命。

### (sub) DIAL_Z20#1504
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 撒謊，紳爵大人，你自己心裡清楚。不管我說不說，你都會為了我在羅姆尼殺的那些人取我性命。自從你一開始來打聽夜鷹會下落，我就一直在觀察你。這些年來，我從那些在你克朗多的夜鷹會肅清行動中倖存下來的人口中，聽過不少關於神偷吉米的傳聞。他們把你說得神乎其技。現在，該看看你能不能在戰鬥中，勝過一名真正的夜鷹會刺客了……

### (sub) DIAL_Z20#1505
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1506
- speaker=0  style=0
- effects:
    - END conversation, result=65535

### (sub) DIAL_Z20#1507
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1508
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我對卡胡利神的信徒不太熟悉。一般來說，克朗多這邊的人比較常信奉巴納斯神跟阿斯塔隆神。

### (sub) DIAL_Z20#1509
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 公開信奉一位以復仇為職志的神明並不容易，我猜大概就跟公開信奉死亡女神一樣難。人們自然而然地會認為，你要是開始定期朝聖，肯定是心裡憋著一筆帳要算，而這猜測往往也八九不離十。他們卻對另一件事視而不見——卡胡利雖然有時被稱作『追獵者』，但祂同時也是『真相的裁決者』。當你在別處求不到公道時，人們自然會轉向卡胡利。

### (sub) DIAL_Z20#1510
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你當初想替誰報仇？

### (sub) DIAL_Z20#1511
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哈，這個嘛，當然是替我自己。不過我已經有段時間沒去過神殿了。我的問題後來差不多自己解決了，也就用不著神明插手了，於是……

### (sub) DIAL_Z20#1512
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，不去比繳什一稅省事多了。你還記得他們的虔信律則嗎？那位祭司提過，我倒挺好奇具體內容是什麼。

### (sub) DIAL_Z20#1513
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還特意想忘掉那些呢……嗯……我只記得第一條，好像跟『意志之服從』有關。加入神殿，就得斷絕與國王和王國的一切羈絆。這就是為什麼你不會在神殿裡見到任何貴族。當然啦，都能指揮一支私人軍隊了，誰還在乎那個。

### (sub) DIAL_Z20#1514
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1516
- speaker=0  style=0
- effects:
    - SET flag 0x00aa=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1517
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你該不會剛好跟當初替科瓦利斯伯爵蓋酒窖的那個桑多有親戚關係吧？

### (sub) DIAL_Z20#1518
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有，不過可惜伯爵就是不肯相信我。每次見面，我都能從他眼裡看出懷疑，可我實在不知道該怎麼讓他對那場意外釋懷。要是他別老糾結在這樁不幸的巧合上，對我們倆的身心都好。

### (sub) DIAL_Z20#1519
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1521
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1522
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知道殺死內維爾．科瓦利斯的那場意外嗎？

### (sub) DIAL_Z20#1523
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 照卡瓦爾堡『鴨頭』酒館老闆的說法，那是場相當古怪的意外。聽說這個桑多是個酒鬼，蓋出來的東西向來品質低劣。我很難相信伯爵會把工程交給這種人，不過他總不可能是故意讓酒窖塌下來的吧。

### (sub) DIAL_Z20#1524
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你覺得伯爵是故意讓酒窖塌下來的？為了什麼目的？

### (sub) DIAL_Z20#1525
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽說伯爵懷疑自己的兒子做了什麼可怕的事，不過……我跟伯爵之間已經夠多過節了。我不想再多說什麼，免得影響我對烏格妮的追求。我跟你說的這些都只是傳聞，還請你別告訴伯爵我們聊過這個話題。

### (sub) DIAL_Z20#1526
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1528
- speaker=0  style=0
- effects:
    - SET flag 0x1a86=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1529
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬拉克十字鎮的伊凡．史卡德跟我們說，你棋藝相當高明。

### (sub) DIAL_Z20#1530
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 過獎了。他自己棋下得也不算差。

### (sub) DIAL_Z20#1531
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他跟我們說你有一招叫『桑多迴避』。我很想跟你學學這一招。

### (sub) DIAL_Z20#1532
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這種招式我可不能隨便教人。靠著它，我已經連勝好幾年不敗了……

### (sub) DIAL_Z20#1533
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我願意付錢跟你學。

### (sub) DIAL_Z20#1534
- speaker=7  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [50125..2]] -> node 4294901761
    - [flag 0x0101 in [51218..2]] -> node 4294901761
- text: 你是想去對付伊凡吧？他到時候肯定被殺得莫名其妙。我記得他下注一向拿綠寶石，這樣吧，好歹讓你贏了以後有點賺頭……就說一百枚金幣。成交嗎？

### (sub) DIAL_Z20#1535
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [50154..2]] -> node 4294901860
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1536
- speaker=0  style=0
- effects:
    - SET flag 0x1ad7=1
    - SET flag 0x1f6f=1
    - TAKE gold -1000
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1537
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 光是看他到時候的表情就值回票價了。開始吧。

### (sub) DIAL_Z20#1538
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓我先找幾顆合適的石頭。你在地上畫個棋盤出來，我這就讓你見識見識這場羞辱大戲的完整架構……

### (sub) DIAL_Z20#1539
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士咧嘴一笑。  納馮用一堆五花八門的石頭擺出他的招式，一看就知道，這一招要是用在一個好攻的對手身上，威力會相當驚人。  「你記得住這一整套嗎？」納馮拍了拍手上的塵土，問道。  「沒問題，」詹姆士答道，把欠納馮的酬勞倒在這張匆匆畫出來的棋盤上。「我看伊凡有得驚訝了。」

### (sub) DIAL_Z20#1540
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1541
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1542
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，看來我現在只好先算了。我身上的錢不夠付這堂課的學費。

### (sub) DIAL_Z20#1543
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那『桑多迴避』又能多保密一天了。改天再來找我試試吧。我倒挺想看看，這招落在別人手裡效果如何。

### (sub) DIAL_Z20#1544
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1545
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z20#1546
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哎呀，不了……我是很想學你這招，可這代價未免太高了。

### (sub) DIAL_Z20#1547
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 反正這招還是我自己留著比較好。這種秘技不該隨便丟給毫無防備的大眾，尤其是伊凡．史卡德。我看他大概會不知所措。

### (sub) DIAL_Z20#1548
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
