# DIAL_Z21

88 records, 10 keyed nodes

## node 2100016  (DIAL_Z21#0)
- speaker=0  style=0
- effects:
    - play sfx 75
    - bind speaker-name slot (kind=1 sub=29)
    - frame/rect style override x=70 y=40 w=180 h=35
- text: 隊伍的@1能力提升了。

## node 2100017  (DIAL_Z21#1)
- speaker=0  style=0
- effects:
    - play sfx 75
    - frame/rect style override x=70 y=40 w=180 h=35
- text: 隊伍的各項能力都提升了。

## node 2100018  (DIAL_Z21#2)
- speaker=0  style=0
- effects:
    - play sfx 75
    - frame/rect style override x=70 y=40 w=180 h=35
    - bind speaker-name slot (kind=1 sub=29)
- text: @的@1能力提升了。

## node 2100019  (DIAL_Z21#3)
- speaker=0  style=0
- effects:
    - play sfx 75
    - frame/rect style override x=70 y=40 w=180 h=35
- text: @的各項能力都提升了。

## node 2100007  (DIAL_Z21#4)
- speaker=3  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們最好盡快穿過這座城鎮。我不久前才在這裡放了一場婚禮的鴿子，要是又被人認出來，恐怕會惹來不少尷尬的追問。

### (sub) DIAL_Z21#5
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們可能需要補給……

### (sub) DIAL_Z21#7
- speaker=0  style=0
- effects:
    - SET flag 0x753e=0

### (sub) DIAL_Z21#8
- speaker=0  style=0
- effects:
    - SET flag 0x753e=10

### (sub) DIAL_Z21#9
- speaker=0  style=0
- effects:
    - SET flag 0x753e=20

### (sub) DIAL_Z21#10
- speaker=0  style=0
- effects:
    - SET flag 0x753e=30

### (sub) DIAL_Z21#11
- speaker=0  style=0
- effects:
    - SET flag 0x753e=40

### (sub) DIAL_Z21#12
- speaker=0  style=0
- effects:
    - SET flag 0x753e=50

### (sub) DIAL_Z21#13
- speaker=0  style=0
- effects:
    - SET flag 0x753e=100

### (sub) DIAL_Z21#14
- speaker=0  style=0
- effects:
    - SET flag 0x753e=150

### (sub) DIAL_Z21#15
- speaker=0  style=0
- effects:
    - SET flag 0x753e=200

### (sub) DIAL_Z21#16
- speaker=0  style=0
- effects:
    - SET flag 0x753e=250

### (sub) DIAL_Z21#17
- speaker=0  style=0
- effects:
    - SET flag 0x753e=300

### (sub) DIAL_Z21#18
- speaker=0  style=0
- effects:
    - SET flag 0x753e=400

### (sub) DIAL_Z21#19
- speaker=0  style=0
- effects:
    - SET flag 0x753e=500

### (sub) DIAL_Z21#20
- speaker=0  style=0
- effects:
    - SET flag 0x753e=750

### (sub) DIAL_Z21#21
- speaker=0  style=0
- effects:
    - SET flag 0x753e=1000

### (sub) DIAL_Z21#22
- speaker=0  style=0
- effects:
    - SET flag 0x753e=2000

## node 2100011  (DIAL_Z21#23)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#24
- speaker=0  style=0
- branches:
    - [flag 0x754d in [1714..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#25
- speaker=0  style=6  flags=paged-text
- effects:
    - push return-address key 1438 (GoodBye target)
- branches:
    - [flag 0x00f5 in [827..0]] -> node 4294901761
    - [flag 0x00f6 in [846..0]] -> node 4294901761
    - [flag 0x00f9 in [903..0]] -> node 4294901761
    - [flag 0x00fc in [960..0]] -> node 4294901761
    - [flag 0x010a in [732..0]] -> node 4294901761
- text: 賭徒抬起頭來。  他握緊拳頭，在@4鼻子底下晃了晃，接著壞笑一聲攤開手掌，露出一對骰子。「這局玩骰子，朋友，」賭徒重新坐了下來說道。「贏家可以拿到賭注的一半。你要下多少金幣？」

### (sub) DIAL_Z21#26
- speaker=0  style=0
- branches:
    - [flag 0x753e in [1526..0]] -> node 0 (no jump)
    - [flag 0x7533 in [1941..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#27
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 6/6 payout 50%)
- branches:
    - [flag 0x7530 in [2204..0]] -> node 0 (no jump)
    - [flag 0x7530 in [2454..0]] -> node 65537
    - [flag 0x7530 in [2636..0]] -> node 131074

### (sub) DIAL_Z21#31
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 露西亞女神對他們微笑。  @4儘量不動聲色地收起那堆閃亮的贏來的錢，把贏得的金幣收進口袋。「希望你以後運氣能好一點，」@4點頭說道。

### (sub) DIAL_Z21#32
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4擲出了爛骰子。  他皺著眉，不情願地交出下注的金幣。「這局是你的了，先生，」他說。

### (sub) DIAL_Z21#33
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 兩邊擲出的點數不相上下。  「平手。看來露西亞女神待我們同樣公平，」@4收回自己的賭注說道。「或許我們可以再玩一局。」

### (sub) DIAL_Z21#34
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [1526..0]] -> node 262144
    - [always] -> node 0 (no jump)

## node 2100012  (DIAL_Z21#35)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#36
- speaker=0  style=0
- branches:
    - [flag 0x754d in [3390..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#37
- speaker=0  style=6  flags=paged-text
- effects:
    - push return-address key 3114 (GoodBye target)
- branches:
    - [flag 0x00f1 in [751..0]] -> node 4294901761
    - [flag 0x00f5 in [827..0]] -> node 4294901761
    - [flag 0x00f6 in [846..0]] -> node 4294901761
    - [flag 0x00f9 in [903..0]] -> node 4294901761
    - [flag 0x010a in [732..0]] -> node 4294901761
- text: 賭徒拍了拍手中的一疊牌。  「小賭一把如何，陪我玩一局林嵐牌，」他說。「贏家可以拿走跟賭注一樣多的錢。你要下多少注？」

### (sub) DIAL_Z21#38
- speaker=0  style=0
- branches:
    - [flag 0x753e in [3202..0]] -> node 0 (no jump)
    - [flag 0x7533 in [3617..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#39
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 70/30 payout 100%)
- branches:
    - [flag 0x7530 in [3885..0]] -> node 0 (no jump)
    - [flag 0x7530 in [4135..0]] -> node 65537
    - [flag 0x7530 in [4358..0]] -> node 131074

### (sub) DIAL_Z21#43
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 露西亞女神對他們微笑。  @4儘量不動聲色地收起那堆閃亮的贏來的錢，把贏得的金幣收進口袋。「希望你以後運氣能好一點，」@4點頭說道。

### (sub) DIAL_Z21#44
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4盯著手中的牌。  這大概是他在林嵐牌裡拿過最爛的一手牌，他皺著眉，不情願地交出下注的金幣。「這局是你的了，先生，」他說。

### (sub) DIAL_Z21#45
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 牌都攤在桌上了。  「平手。看來露西亞女神待我們同樣公平，」@4收回自己的賭注說道。「或許我們可以再玩一局。」

### (sub) DIAL_Z21#46
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [3202..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

## node 2100013  (DIAL_Z21#47)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#48
- speaker=0  style=0
- branches:
    - [flag 0x754d in [5228..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#49
- speaker=0  style=6  flags=paged-text
- effects:
    - push return-address key 4952 (GoodBye target)
- branches:
    - [flag 0x00f6 in [846..0]] -> node 4294901761
    - [flag 0x00f9 in [903..0]] -> node 4294901761
    - [flag 0x00fc in [960..0]] -> node 4294901761
    - [flag 0x00fe in [998..0]] -> node 4294901761
    - [flag 0x010a in [732..0]] -> node 4294901761
- text: 賭徒拍了拍手中的一疊牌。  「帕夏瓦牌，」他說著，把色彩鮮豔的一疊牌推向@4。見對方對這提議似乎興趣缺缺，他便加碼利誘。「如果你贏了，我會付你賭注的一倍半。你想下多少注？」

### (sub) DIAL_Z21#50
- speaker=0  style=0
- branches:
    - [flag 0x753e in [5040..0]] -> node 0 (no jump)
    - [flag 0x7533 in [5455..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#51
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 40/60 payout 150%)
- branches:
    - [flag 0x7530 in [5723..0]] -> node 0 (no jump)
    - [flag 0x7530 in [5973..0]] -> node 65537
    - [flag 0x7530 in [6196..0]] -> node 131074

### (sub) DIAL_Z21#55
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 露西亞女神對他們微笑。  @4儘量不動聲色地收起那堆閃亮的贏來的錢，把贏得的金幣收進口袋。「希望你以後運氣能好一點，」@4點頭說道。

### (sub) DIAL_Z21#56
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4盯著手中的牌。  這大概是他在帕夏瓦牌裡拿過最爛的一手牌，他皺著眉，不情願地交出下注的金幣。「這局是你的了，先生，」他說。

### (sub) DIAL_Z21#57
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 牌都攤在桌上了。  「平手。看來露西亞女神待我們同樣公平，」@4收回自己的賭注說道。「或許我們可以再玩一局。」

### (sub) DIAL_Z21#58
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [5040..0]] -> node 589824
    - [always] -> node 0 (no jump)

## node 2100014  (DIAL_Z21#59)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#60
- speaker=0  style=0
- branches:
    - [flag 0x754d in [7452..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#61
- speaker=0  style=6  flags=paged-text
- effects:
    - push return-address key 7176 (GoodBye target)
- branches:
    - [flag 0x00fc in [960..0]] -> node 4294901761
    - [flag 0x00fd in [979..0]] -> node 4294901761
    - [flag 0x00fe in [998..0]] -> node 4294901761
    - [flag 0x00ff in [1017..0]] -> node 4294901761
    - [flag 0x010a in [732..0]] -> node 4294901761
- text: 這男人是個賭徒。  他抽出一疊比林嵐牌或帕夏瓦牌都厚的牌，啪地拍在桌上，抽出一張造型古怪的牌翻了過來。牌面上畫著一名女子。  「這叫『藍衣夫人』，」男人拖長了語調說道。「這遊戲叫做ó波基爾，是凱許狗兵最近才在玩的新花樣。你聽過嗎？」  @4點了點頭。「我還曾經跟路過本地酒館的傭兵玩過幾局。」  賭徒似乎有些失望，但仍接著說：「那就不對等下注吧。既然你已經會玩了，我就付你賭注的一半。你要下多少注？」

### (sub) DIAL_Z21#62
- speaker=0  style=0
- branches:
    - [flag 0x753e in [7264..0]] -> node 0 (no jump)
    - [flag 0x7533 in [7679..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#63
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 20/80 payout 200%)
- branches:
    - [flag 0x7530 in [7947..0]] -> node 0 (no jump)
    - [flag 0x7530 in [8197..0]] -> node 65537
    - [flag 0x7530 in [8420..0]] -> node 131074

### (sub) DIAL_Z21#67
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 露西亞女神對他們微笑。  @4儘量不動聲色地收起那堆閃亮的贏來的錢，把贏得的金幣收進口袋。「希望你以後運氣能好一點，」@4點頭說道。

### (sub) DIAL_Z21#68
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4盯著手中的牌。  這大概是他在ó波基爾裡拿過最爛的一手牌，他皺著眉，不情願地交出下注的金幣。「這局是你的了，先生，」他說。

### (sub) DIAL_Z21#69
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 牌都攤在桌上了。  「平手。看來露西亞女神待我們同樣公平，」@4收回自己的賭注說道。「或許我們可以再玩一局。」

### (sub) DIAL_Z21#70
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [7264..0]] -> node 3211264
    - [always] -> node 0 (no jump)

## node 2100015  (DIAL_Z21#71)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#72
- speaker=0  style=0
- branches:
    - [flag 0x754d in [9670..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#73
- speaker=0  style=6  flags=paged-text
- effects:
    - push return-address key 9249 (GoodBye target)
- branches:
    - [flag 0x00f1 in [751..0]] -> node 4294901761
    - [flag 0x00f3 in [789..0]] -> node 4294901761
    - [flag 0x00f5 in [827..0]] -> node 4294901761
    - [flag 0x00f6 in [846..0]] -> node 4294901761
    - [flag 0x010a in [732..0]] -> node 4294901761
- text: 那男人皺起眉頭。  他面前的桌上擺著一副小巧的西洋棋盤，木雕棋子的擺法看起來執白的一方情勢相當不妙。他頭也不抬地挪動了一枚棋子。「你會下棋嗎？」  @4聳了聳肩，坐了下來。「還算過得去。」  「很好。那你應該不介意我們這局下點小注吧，」男人微笑著說，這次換從對面挪動了一枚棋子。「對等下注。贏家拿走賭注。你要下多少？」

### (sub) DIAL_Z21#74
- speaker=0  style=0
- branches:
    - [flag 0x753e in [9482..0]] -> node 0 (no jump)
    - [flag 0x7533 in [9897..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#75
- speaker=0  style=0
- branches:
    - [flag 0x1f6f in [9356..0]] -> node 4294901761
    - [flag 0x1f70 in [9385..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#76
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 40/60 payout 100%)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#77
- speaker=0  style=0
- branches:
    - [flag 0x1f70 in [9414..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#78
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 60/40 payout 100%)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#79
- speaker=0  style=0
- effects:
    - ACTION: gambling resolve (max 80/20 payout 100%)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z21#80
- speaker=0  style=0
- branches:
    - [flag 0x7530 in [10165..0]] -> node 0 (no jump)
    - [flag 0x7530 in [10394..0]] -> node 65537
    - [flag 0x7530 in [10699..0]] -> node 131074

### (sub) DIAL_Z21#84
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他的棄兵策略奏效了。  他微笑著看自己如何成功攻破了賭徒的防守陣式，優雅地收起贏來的錢。「希望你以後運氣能好一點，」@4點頭說道。

### (sub) DIAL_Z21#85
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 將死。  @4皺眉苦思，沒想到自己竟這麼輕易就被賭徒將死了，他一邊努力回想這局棋是怎麼下輸的，一邊把賭注交給賭徒。「這局你贏了，」他咕噥道。  「是啊，」賭徒回答。「不過我猜我可比你享受多了。」

### (sub) DIAL_Z21#86
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 和局。  雖然這結果跟他原本盼望的相去甚遠，但至少慶幸賭注沒有落入對手的錢袋，他也還算滿意。  「平手。看來露西亞女神待我們同樣公平，」@4收回自己的賭注說道。「或許我們可以再玩一局。」

### (sub) DIAL_Z21#87
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [9482..0]] -> node 0 (no jump)
    - [always] -> node 0 (no jump)
