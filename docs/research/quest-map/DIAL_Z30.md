# DIAL_Z30

3181 records, 44 keyed nodes

## node 3000001  (DIAL_Z30#0)
- speaker=0  style=0
- branches:
    - [flag 0x1ea7 in [383..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1
- speaker=0  style=0
- effects:
    - SET flag 0x1ea7=0
    - SET flag 0x1ea8=0
- branches:
    - [always] -> node 0 (no jump)
- text: 翻頁功能（PAGE_THRU）已關閉

### (sub) DIAL_Z30#2
- speaker=0  style=0
- effects:
    - SET flag 0x1ea7=1
- branches:
    - [always] -> node 0 (no jump)
- text: 翻頁功能（PAGE_THRU）已被呼叫……  ……現在對話應該會連續播放  而且，

## node 3000002  (DIAL_Z30#3)
- speaker=0  style=0  flags=paged-text
- effects:
    - SET flag 0x1ea8=1
- branches:
    - [flag 0x0100 in [746..0]] -> node 4294901761
    - [flag 0x0101 in [775..0]] -> node 4294901761
- text: 對話路徑測試模式即將啟用  你要不要聽取角色的提示語音，並在畫面上顯示出來？

### (sub) DIAL_Z30#4
- speaker=0  style=0
- effects:
    - push return-address key 775 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#5
- speaker=0  style=0
- branches:
    - [flag 0x1ea7 in [50883..32813]] -> node 4294901761
    - [always] -> node 0 (no jump)

## node 3000003  (DIAL_Z30#6)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [6035..0]] -> node 65537
    - [flag 0x7537 in [9507..0]] -> node 196611
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#7
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#8
- speaker=0  style=0
- effects:
    - SET flag 0x1ea9=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000004  (DIAL_Z30#9)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [12525..0]] -> node 131074
    - [flag 0x7537 in [15856..0]] -> node 196611
    - [flag 0x7537 in [19695..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#10
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#11
- speaker=0  style=0
- effects:
    - SET flag 0x1eaa=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000005  (DIAL_Z30#12)
- speaker=0  style=0
- effects:
    - SET flag 0x005f=1
- branches:
    - [flag 0x7537 in [22365..0]] -> node 65537
    - [flag 0x7537 in [25266..0]] -> node 131074
    - [flag 0x7537 in [27713..0]] -> node 196611
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#13
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#14
- speaker=0  style=0
- effects:
    - SET flag 0x1eab=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000006  (DIAL_Z30#15)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [30014..0]] -> node 65537
    - [flag 0x7537 in [31674..0]] -> node 131074
    - [flag 0x7537 in [34104..0]] -> node 196611
    - [flag 0x7537 in [36479..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#16
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#17
- speaker=0  style=0
- effects:
    - SET flag 0x1eac=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000007  (DIAL_Z30#18)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [38441..0]] -> node 262148
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#19
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#20
- speaker=0  style=0
- effects:
    - SET flag 0x1ead=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000008  (DIAL_Z30#21)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [41049..0]] -> node 262148
    - [flag 0x7537 in [43510..0]] -> node 458759
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#22
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#23
- speaker=0  style=0
- effects:
    - SET flag 0x1eae=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000009  (DIAL_Z30#24)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [46031..0]] -> node 65537
    - [flag 0x7537 in [48431..0]] -> node 131074
    - [flag 0x7537 in [50284..0]] -> node 196611
    - [flag 0x7537 in [53317..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#25
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#26
- speaker=0  style=0
- effects:
    - SET flag 0x1eaf=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000010  (DIAL_Z30#27)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [56462..0]] -> node 65537
    - [flag 0x7537 in [60144..0]] -> node 131074
    - [flag 0x7537 in [62923..0]] -> node 196611
    - [flag 0x7537 in [65398..0]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#28
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#29
- speaker=0  style=0
- effects:
    - SET flag 0x1eb0=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000011  (DIAL_Z30#30)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [3266..1]] -> node 65537
    - [flag 0x7537 in [5390..1]] -> node 131074
    - [flag 0x7537 in [8014..1]] -> node 196611
    - [flag 0x7537 in [10706..1]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#31
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#32
- speaker=0  style=0
- effects:
    - SET flag 0x1eb1=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000012  (DIAL_Z30#33)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [14411..1]] -> node 196609
    - [flag 0x7537 in [14411..1]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#34
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#35
- speaker=0  style=0
- effects:
    - SET flag 0x1eb2=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000013  (DIAL_Z30#36)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [21797..1]] -> node 131074
    - [flag 0x7537 in [24886..1]] -> node 196611
    - [flag 0x7537 in [27609..1]] -> node 327685
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#37
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#38
- speaker=0  style=0
- effects:
    - SET flag 0x1eb3=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000014  (DIAL_Z30#39)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [30361..1]] -> node 65537
    - [flag 0x7537 in [32759..1]] -> node 131074
    - [flag 0x7537 in [35335..1]] -> node 196611
    - [flag 0x7537 in [38004..1]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#40
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#41
- speaker=0  style=0
- effects:
    - SET flag 0x1eb4=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000015  (DIAL_Z30#42)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [40385..1]] -> node 524289
    - [flag 0x7537 in [42663..1]] -> node 589833
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#43
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#44
- speaker=0  style=0
- effects:
    - SET flag 0x1eb5=1
- branches:
    - [flag 0x7537 in [50923..32813]] -> node 589833
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#45
- speaker=0  style=0
- effects:
    - END conversation, result=65532

## node 3000016  (DIAL_Z30#46)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [44819..1]] -> node 327685
    - [flag 0x7537 in [48220..1]] -> node 458759
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#47
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#48
- speaker=0  style=0
- effects:
    - SET flag 0x1eb6=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000017  (DIAL_Z30#49)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [50665..1]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#50
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#51
- speaker=0  style=0
- effects:
    - SET flag 0x1eb7=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000018  (DIAL_Z30#52)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [52960..1]] -> node 262148
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#53
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#54
- speaker=0  style=0
- effects:
    - SET flag 0x1eb8=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000019  (DIAL_Z30#55)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [55394..1]] -> node 65537
    - [flag 0x7537 in [58262..1]] -> node 131074
    - [flag 0x7537 in [60064..1]] -> node 393219
    - [flag 0x7537 in [62412..1]] -> node 458759
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#56
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#57
- speaker=0  style=0
- effects:
    - SET flag 0x1eb9=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000020  (DIAL_Z30#58)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [609..2]] -> node 65537
    - [flag 0x7537 in [2665..2]] -> node 131074
    - [flag 0x7537 in [4300..2]] -> node 196611
    - [flag 0x7537 in [6019..2]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#59
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#60
- speaker=0  style=0
- effects:
    - SET flag 0x1e84=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000021  (DIAL_Z30#61)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [8019..2]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#62
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#63
- speaker=0  style=0
- effects:
    - SET flag 0x1eba=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000022  (DIAL_Z30#64)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [10410..2]] -> node 65537
    - [flag 0x7537 in [11019..2]] -> node 196610
    - [flag 0x7537 in [19873..2]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#65
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#66
- speaker=0  style=0
- effects:
    - SET flag 0x1ebb=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000023  (DIAL_Z30#67)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [24887..2]] -> node 196610
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#68
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#69
- speaker=0  style=0
- effects:
    - SET flag 0x1ebc=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000024  (DIAL_Z30#70)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [30287..2]] -> node 262148
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#71
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#72
- speaker=0  style=0
- effects:
    - SET flag 0x1ebd=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000025  (DIAL_Z30#73)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [35303..2]] -> node 131074
    - [flag 0x7537 in [36626..2]] -> node 196611
    - [flag 0x7537 in [38483..2]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#74
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#75
- speaker=0  style=0
- effects:
    - SET flag 0x1ebe=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000026  (DIAL_Z30#76)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [40583..2]] -> node 65537
    - [flag 0x7537 in [48484..2]] -> node 131074
    - [flag 0x7537 in [53648..2]] -> node 196611
    - [flag 0x7537 in [64868..2]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#77
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#78
- speaker=0  style=0
- effects:
    - SET flag 0x1ebf=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000027  (DIAL_Z30#79)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [1491..3]] -> node 65537
    - [flag 0x7537 in [3421..3]] -> node 196611
    - [flag 0x7537 in [7551..3]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#80
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#81
- speaker=0  style=0
- effects:
    - SET flag 0x1ec0=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000028  (DIAL_Z30#82)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [9827..3]] -> node 65537
    - [flag 0x7537 in [12625..3]] -> node 131074
    - [flag 0x7537 in [17923..3]] -> node 196611
    - [flag 0x7537 in [23739..3]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#83
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#84
- speaker=0  style=0
- effects:
    - SET flag 0x1ec1=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000029  (DIAL_Z30#85)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [27847..3]] -> node 196609
    - [flag 0x7537 in [27847..3]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#86
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#87
- speaker=0  style=0
- effects:
    - SET flag 0x1ec2=1
    - END conversation, result=0
- branches:
    - [always] -> node 0 (no jump)

## node 3000030  (DIAL_Z30#88)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [35226..3]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#89
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#90
- speaker=0  style=0
- effects:
    - SET flag 0x1ec3=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000031  (DIAL_Z30#91)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [40537..3]] -> node 262148
    - [flag 0x7537 in [45978..3]] -> node 458759
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#92
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#93
- speaker=0  style=0
- effects:
    - SET flag 0x1ec4=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000032  (DIAL_Z30#94)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [49690..3]] -> node 65537
    - [flag 0x7537 in [52443..3]] -> node 131074
    - [flag 0x7537 in [53680..3]] -> node 196611
    - [flag 0x7537 in [56302..3]] -> node 262148
    - [flag 0x7537 in [58319..3]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#95
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#96
- speaker=0  style=0
- effects:
    - SET flag 0x1e87=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000033  (DIAL_Z30#97)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [60497..3]] -> node 196610
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#98
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#99
- speaker=0  style=0
- effects:
    - SET flag 0x1ec5=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000034  (DIAL_Z30#100)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [832..4]] -> node 65537
    - [flag 0x7537 in [3166..4]] -> node 131074
    - [flag 0x7537 in [8367..4]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#101
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#102
- speaker=0  style=0
- effects:
    - SET flag 0x1ec6=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000035  (DIAL_Z30#103)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [10621..4]] -> node 65537
    - [flag 0x7537 in [12858..4]] -> node 131074
    - [flag 0x7537 in [15445..4]] -> node 196611
    - [flag 0x7537 in [18117..4]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#104
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#105
- speaker=0  style=0
- effects:
    - SET flag 0x1ec7=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000036  (DIAL_Z30#106)
- speaker=0  style=0
- effects:
    - SET flag 0x1a81=1
- branches:
    - [flag 0x7537 in [22299..4]] -> node 131074
    - [flag 0x7537 in [27826..4]] -> node 196611
    - [flag 0x7537 in [34770..4]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#107
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#108
- speaker=0  style=0
- effects:
    - SET flag 0x1ec8=1
    - END conversation, result=0
- branches:
    - [always] -> node 0 (no jump)

## node 3000037  (DIAL_Z30#109)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [41000..4]] -> node 65537
    - [flag 0x7537 in [43960..4]] -> node 196610
    - [flag 0x7537 in [46862..4]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#110
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#111
- speaker=0  style=0
- effects:
    - SET flag 0x1e88=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000038  (DIAL_Z30#112)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [47703..4]] -> node 196609
    - [flag 0x7537 in [47703..4]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#113
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#114
- speaker=0  style=0
- effects:
    - SET flag 0x1ec9=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000039  (DIAL_Z30#115)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [50881..4]] -> node 262148
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#116
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#117
- speaker=0  style=0
- effects:
    - SET flag 0x1eca=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000040  (DIAL_Z30#118)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [55172..4]] -> node 65537
    - [flag 0x7537 in [61046..4]] -> node 196610
    - [flag 0x7537 in [5965..5]] -> node 327685
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#119
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#120
- speaker=0  style=0
- effects:
    - SET flag 0x1ecb=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000041  (DIAL_Z30#121)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [13738..5]] -> node 65537
    - [flag 0x7537 in [16750..5]] -> node 131074
    - [flag 0x7537 in [19230..5]] -> node 196611
    - [flag 0x7537 in [27725..5]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#122
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#123
- speaker=0  style=0
- effects:
    - SET flag 0x1ecc=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000042  (DIAL_Z30#124)
- speaker=0  style=0
- branches:
    - [flag 0x7537 in [29761..5]] -> node 65537
    - [flag 0x7537 in [30982..5]] -> node 196610
    - [flag 0x7537 in [36806..5]] -> node 393222
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#125
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#126
- speaker=0  style=0
- effects:
    - SET flag 0x1ecd=1
- branches:
    - [always] -> node 0 (no jump)

## node 3000043  (DIAL_Z30#127)
- speaker=0  style=0

## node 3000045  (DIAL_Z30#128)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#129
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾憂心忡忡。  他們此刻離該追尋的目標還有好幾哩遠，好在他能靠一個事實稍稍安撫自己揮之不去的不安——自從他們繞道遠離克朗多之後，擋在路上的刺客明顯ó少了許多。他們終究還是得去見親王，這點無可避免，但他直覺告訴他，沒有一個刺客會料到他們竟朝高堡以南的丘陵地帶而去……

### (sub) DIAL_Z30#130
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們往東走的距離，應該已經足以甩開其他刺客的追蹤了。戈拉斯，你比我們更清楚迪勒肯會派什麼手段來對付我們。你怎麼看？

### (sub) DIAL_Z30#131
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想，換作是我，會像獵狐一樣獵殺我們——緊追不捨、咬著腳跟不放，一路把獵物嚇得逃回自己的洞穴……

### (sub) DIAL_Z30#132
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，那個洞穴就是克朗多了。就算他現在還沒猜到我們的目的地，也不會蒙在鼓裡太久。可他沒辦法在ó克朗多本地布下陷阱等我們。光是一大群精靈出現在那裡，就足以引起軒然大波了。

### (sub) DIAL_Z30#133
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我懷疑陷阱就設在我們目的地正北方。ó這樣安排最為謹慎。

### (sub) DIAL_Z30#135
- speaker=0  style=0
- branches:
    - [flag 0x1ea9 in [8739..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#136
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1032 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#137
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾疲憊不堪。  當初他離開克朗多，去莫耶特隊長麾下受訓一段時日時，還以為不過是當幾個月兵、再回陸地盡頭老家或亞魯莎宮廷裡去，是件簡單的事。可如今，他已經在王國跟北境之間漫無目的地遊蕩了數不清多少個月，卻感覺不出自己完成了什麼對亞魯莎親王有價值的事。更何況，如今他身邊還多了戈拉斯跟這位提伯恩來的扈從，他得負責把他們三個活著帶回克朗多。  感覺到袖子被拉了一下，他這才從恍神中回過神來。歐文正指著身邊一個逐漸靠近的身影……

### (sub) DIAL_Z30#138
- speaker=7  style=0
- effects:
    - ?wOp12 a1=119 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 離親王宮廷這麼遠，我還挺意外你們那個地方居然有人知道肯廷拉什的存在。你們是為了生意還是純粹來遊玩的？

### (sub) DIAL_Z30#139
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 老實說，會來到這裡，說是機緣巧合更貼切。其實我們只是路過，正從拉姆特一路趕來。我們在羅姆尼有筆生意約好了……

### (sub) DIAL_Z30#140
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó「啊ð」，公會之城。我聽說那邊出了些麻煩事，好像是縴夫公會跟玻璃匠公會之間有糾紛。我甚至聽過謠言說刺客公會也牽涉其中，不過我實在不太相信。希望這件事能盡快和平解決。  恕我盯著看，只是我已經有段時間沒在這一帶見過ó精靈了。而且遇上一位全副武裝的精靈，就更是難得一見了。

### (sub) DIAL_Z30#141
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈……索爾加斯正跟我們合作，商談一筆精靈貨品在東部王國的新交易。他做的是盔甲生意，這樣運送起來，總比裝在袋子裡背著方便。

### (sub) DIAL_Z30#142
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這主意確實巧妙。索爾加斯，你說。這名字聽起來……有點ó耳熟。也許我們以前見過……

### (sub) DIAL_Z30#143
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們從未見過面。您弄錯了。

### (sub) DIAL_Z30#144
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然，這件事我就相信您的話了。想必我只是見過某個ó跟您長得相似的人……  換個話題。既然幾位都是來肯廷拉什的訪客，而訪客也是門好ó生意ð，有什麼我能幫得上忙的嗎？

### (sub) DIAL_Z30#145
- speaker=0  style=0
- effects:
    - push return-address key 8381 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#146
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還有別的約要赴，大概該上路了。

### (sub) DIAL_Z30#147
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那祝各位一路順風。要是以後有任何需要，人又在肯廷拉什，務必來找我。

### (sub) DIAL_Z30#148
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [8643..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#149
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [8739..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Navon_Du_Sandau

### (sub) DIAL_Z30#150
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1032 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#151
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 有人喊了他們一聲。  雖然陽光刺得@4睜不開眼，他還是相當確定朝他們走來的人，是納馮．杜桑多——他們先前在肯廷拉什見過的一名商人……

### (sub) DIAL_Z30#152
- speaker=7  style=0
- effects:
    - ?wOp12 a1=119 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒想到這麼快又見到你們三位了。納馮．杜桑多能幫上什麼忙嗎？

### (sub) DIAL_Z30#153
- speaker=0  style=0
- effects:
    - push return-address key 9150 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#154
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還有別的約要赴，大概該上路了。

### (sub) DIAL_Z30#155
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那祝各位一路順風。要是以後有任何需要，人又在肯廷拉什，務必來找我。

### (sub) DIAL_Z30#156
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9412..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#157
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9507..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Navon_Du_Sandau

### (sub) DIAL_Z30#158
- speaker=0  style=0
- branches:
    - [flag 0x1ea9 in [11540..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#159
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
    - advance in-game time by 1800
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#160
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士嗅了嗅空氣。  過去將近一個鐘頭，他一直在試圖拼湊黑羊酒館那樁謀殺案的細節，這時卻有另一件事開始揮之不去地纏著他，就跟他曾經認識的那些嘲弄幫成員的名字一樣，怎麼想都想不真切。過了幾分鐘他才意識到，是什麼在分散他的注意力。  「你有沒有聞到什麼奇怪的味道？」他問戈拉斯。在露天環境裡聞到茉莉花香，實在透著古怪，他四下張望，卻找不到任何能解釋這股氣味的天然植物。可就在他搜尋的同時，他似乎瞥見有人正沿著大路朝他們走來……

### (sub) DIAL_Z30#161
- speaker=7  style=0
- effects:
    - ?wOp12 a1=119 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡實在沒什麼大事，值得招來苦海那邊的訪客，而要是這樣還不夠稀奇，看來我們還有從ó艾爾凡達ð來的貴客呢。歡迎來到肯廷拉什。

### (sub) DIAL_Z30#162
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這問題聽起來可能有點奇怪，不過剛才我好像聞到一股香料味……確切地說是茉莉花香。這附近有種這種植物嗎？

### (sub) DIAL_Z30#163
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您鼻子真靈。可惜這不是本地的東西。我做的是香料生意，也經營一些其他的進口貨。我才剛從凱許跑完一趟長途行程回來，恐怕這氣味還沾在衣服上沒散去。

### (sub) DIAL_Z30#164
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可您才剛從路那頭走過來。這味道我已經聞了好一陣子了……

### (sub) DIAL_Z30#165
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽人說這味道傳得挺遠的。今天ó確實有點風。這麼說……幾位既是這一帶的旅人，跟本地人打交道有時候也不容易，有什麼我能幫得上忙的嗎？

### (sub) DIAL_Z30#166
- speaker=0  style=0
- effects:
    - push return-address key 11182 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#167
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還有別的約要赴，大概該上路了。

### (sub) DIAL_Z30#168
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那祝各位一路順風。要是以後有任何需要，人又在肯廷拉什，務必來找我。

### (sub) DIAL_Z30#169
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [11444..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#170
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [11540..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Navon_Du_Sandau

### (sub) DIAL_Z30#171
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [flag 0x753a in [11579..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#172
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 有人喊了他們一聲。  雖然陽光刺得@4睜不開眼，他還是相當確定朝他們走來的人，是納馮．杜桑多——他們先前在肯廷拉什見過的一名商人……

### (sub) DIAL_Z30#173
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 有人喊了他們一聲。  雖然光線昏暗，@4還是相當確定朝他們走來的人，是納馮．杜桑多——他們先前在肯廷拉什見過的一名商人……

### (sub) DIAL_Z30#174
- speaker=7  style=0
- effects:
    - ?wOp12 a1=119 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒想到這麼快又見到你們三位了。納馮．杜桑多能幫上什麼忙嗎？

### (sub) DIAL_Z30#175
- speaker=0  style=0
- effects:
    - push return-address key 12168 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#176
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還有別的約要赴，大概該上路了。

### (sub) DIAL_Z30#177
- speaker=7  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那祝各位一路順風。要是以後有任何需要，人又在肯廷拉什，務必來找我。

### (sub) DIAL_Z30#178
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [12430..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#179
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [12525..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Navon_Du_Sandau

### (sub) DIAL_Z30#180
- speaker=0  style=0
- branches:
    - [flag 0x1eaa in [14500..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#181
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#182
- speaker=0  style=6
- effects:
    - ?wOp12 a1=131 a2=0
    - preload portraits 0x3,0x8,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 一名女孩穿過田野走來。  她沒有父親那種傲慢的氣派，行動起來就像一縷輕煙，腳步輕盈得彷彿是飄過那片沙沙作響的雜草，而不是走過去的。她翩然來到歐文身邊，在他臉頰上輕輕一吻。

### (sub) DIAL_Z30#183
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你比我記憶中高多了！你這是趁我不注意就長大了，是吧？

### (sub) DIAL_Z30#184
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我總不能一輩子當個小女孩吧，表哥。要是照父親的意思，他早把我嫁給哪個子爵，成天在家織掛毯了，可我這人太固執，大多數追求者都受不了我。你知道我一直希望有一天你會出現，把我帶去某個新奇的地方。

### (sub) DIAL_Z30#185
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一個微不足道的伯爵家排行老三的兒子？我看妳父親不會同意的。再說，我還是沒法接受一個喜歡看滾球錦標賽的女孩子。

### (sub) DIAL_Z30#186
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 豬頭。你要不要把你這幾位相貌堂堂的朋友介紹給我，還是要讓我活活好奇死？

### (sub) DIAL_Z30#187
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許等一下吧，如果我有這個心情的話。

### (sub) DIAL_Z30#188
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我勸你最好有這個心情，不然就算是親戚，我也會叫父親把你上鐐銬。話說回來，是什麼風把你一路吹到卡瓦爾堡來的？

### (sub) DIAL_Z30#189
- speaker=0  style=0
- effects:
    - push return-address key 13885 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#190
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，表妹，能再見到妳真好，不過我們得走了。還有事要辦，還得去打幾條龍呢。

### (sub) DIAL_Z30#191
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好啊。你就這麼走了，把我一個人丟在這個牧羊人的天堂裡，讓我活活無聊死好了！我這幾個月見過最刺激的事，就是看著幾頭豬從圈裡逃出來，在卡瓦爾堡的街上到處亂竄！

### (sub) DIAL_Z30#192
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳死不了的。烏格妮，照顧好自己。要是妳比我先見到妳父親，替我問候他一聲。

### (sub) DIAL_Z30#193
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [14405..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#194
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [14500..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Ugyne_Corvalis

### (sub) DIAL_Z30#195
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#196
- speaker=0  style=6
- effects:
    - preload portraits 0x8,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 烏格妮朝他們喊了一聲。  她站到表哥面前，用那雙淡琥珀色的眼睛直直盯著他。

### (sub) DIAL_Z30#197
- speaker=8  style=0
- effects:
    - ?wOp12 a1=131 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文！要是我不了解你，還真會以為你打算長住不走了。

### (sub) DIAL_Z30#198
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這也不算什麼壞主意。我一直挺喜歡這一帶的……

### (sub) DIAL_Z30#199
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜也是。只要能離你那個暴君父親遠遠的，什麼都好。他從來不讓我們玩得開心，什麼事都嚴肅得要命……

### (sub) DIAL_Z30#200
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我猜妳覺得妳父親帶孩子的功夫就好到哪去了？

### (sub) DIAL_Z30#201
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗯，這麼說，咱們倆的父親都是無趣得要命的老頑固。我看這就是我們倆這麼合得來的原因——好了，你幹嘛跑來打擾一個正享受下午時光的年輕姑娘？

### (sub) DIAL_Z30#202
- speaker=0  style=0
- effects:
    - push return-address key 15374 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#203
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，表妹，能再見到妳真好，不過我們得走了。還有事要辦，還得去打幾條龍呢。

### (sub) DIAL_Z30#204
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好啊。你就這麼走了，把我一個人丟在這裡活活無聊死吧。我完全沒意見。

### (sub) DIAL_Z30#205
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳死不了的。烏格妮，照顧好自己。要是妳比我先見到妳父親，替我問候他一聲。

### (sub) DIAL_Z30#206
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [15762..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#207
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [15856..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Ugyne_Corvalis

### (sub) DIAL_Z30#208
- speaker=0  style=0
- branches:
    - [flag 0x1eaa in [18282..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#209
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#210
- speaker=0  style=6
- effects:
    - preload portraits 0x3,0x8,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 一名女孩穿過田野走來。  她沒有父親那種傲慢的氣派，行動起來就像一縷輕煙，腳步輕盈得彷彿是飄過那片沙沙作響的雜草，而不是走過去的。她翩然來到歐文身邊，在他臉頰上輕輕一吻。

### (sub) DIAL_Z30#211
- speaker=8  style=0
- effects:
    - ?wOp12 a1=131 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我有沒有跟你說過，你每次出現的時機都怪得很？不過見到你真好！

### (sub) DIAL_Z30#212
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳一個人在外頭閒晃是怎麼回事？老實說，妳真讓我吃驚。到了妳這個年紀，大部分女孩子都該懂得外頭四處遊蕩著危險人物的常識了……

### (sub) DIAL_Z30#213
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這開場白可真夠嗆的！歐文，你才比我大四歲，我看不出我的年紀跟這有什麼關係。我只是喜歡在遇到怎麼想都想不通的問題時，跑來這裡靜靜思考。這裡也是我父親發脾氣時，能讓我逃開他的一個安全避風港。

### (sub) DIAL_Z30#214
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他現在正在發脾氣嗎？

### (sub) DIAL_Z30#215
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我見過最嚴重的一次。他把整個廚房的人都開除了，解散了守衛，還把我五個侍女統統趕走。從昨晚晚餐時分開始，他就是這副樣子。我試著問他到底是什麼事讓他這麼心煩，他卻只告訴我，他收到一名信使帶來的壞消息，跟他安排的某項財務事宜有關。

### (sub) DIAL_Z30#216
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 知道那張字條上寫了什麼嗎？

### (sub) DIAL_Z30#217
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰知道呢？他老是把陰謀掛在嘴邊，說東說西的。就好像他總是擔心有人會發現家族什麼見不得人的秘密，可明明就沒什麼好藏的。這種戲碼實在演得有點膩了。  話說回來……你臉上這副驚恐的表情，好像有什麼事不敢跟我說似的。是什麼事？

### (sub) DIAL_Z30#218
- speaker=0  style=0
- effects:
    - push return-address key 17746 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#219
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能再跟妳聊聊真好，不過我們得上路了。答應我，妳會盡快找個人來照顧妳。

### (sub) DIAL_Z30#220
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你別再把我當小孩子一樣操心，我會很感激。不過這個承諾我可以答應，前提是ó你也得做出同樣的承諾。

### (sub) DIAL_Z30#221
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。我以提伯恩伯爵之子的身分向妳保證。再見了，烏格妮……

### (sub) DIAL_Z30#222
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18187..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#223
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [18282..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Ugyne_Corvalis

### (sub) DIAL_Z30#224
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#225
- speaker=0  style=6
- effects:
    - ?wOp12 a1=131 a2=0
    - preload portraits 0x8,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 烏格妮朝他們喊了一聲。  她站到表哥面前，用那雙淡琥珀色的眼睛直直盯著他。

### (sub) DIAL_Z30#226
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼快又回來了？看來我得查查是卡瓦爾堡哪位年輕姑娘勾走了你的心！

### (sub) DIAL_Z30#227
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實我們是回來問妳幾個問題的。妳有空嗎？

### (sub) DIAL_Z30#228
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，我看我可以在長槍騎兵比武大會跟舞會之後，勉強擠出點時間給你們，畢竟你們ó也知道卡瓦爾堡一向這麼忙……

### (sub) DIAL_Z30#229
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳簡直沒救了！有沒有人跟妳說過這句話？

### (sub) DIAL_Z30#230
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許有吧。好了，你們三個到底想幹嘛？想聽點關於我那些ó前任侍女的八卦？還是想聽聽老「灰袍」彼得的故事？

### (sub) DIAL_Z30#231
- speaker=0  style=0
- effects:
    - push return-address key 19085 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#232
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能再跟妳聊聊真好，不過我們得上路了，還有事要辦。

### (sub) DIAL_Z30#233
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，剛好我也有些事要忙。我得把花全都撢一撢灰，免得蜜蜂打噴嚏。沒有什麼比蜜蜂打噴嚏更糟糕的事了。然後我還得用樹枝把堡壘重新蓋起來……

### (sub) DIAL_Z30#234
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再ó見了，你這個傻鵝。照顧好自己。天黑之前一定要回去。我不喜歡妳一個人在外頭閒晃……

### (sub) DIAL_Z30#235
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [19601..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#236
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [19695..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Ugyne_Corvalis

### (sub) DIAL_Z30#237
- speaker=0  style=0
- branches:
    - [flag 0x1eaa in [21649..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#238
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#239
- speaker=0  style=6
- effects:
    - preload portraits 0x8,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 一個身影從屋子轉角處出現。  歐文開心地放下法杖，張開雙臂迎向走來的女孩，給了她一個擁抱……

### (sub) DIAL_Z30#240
- speaker=8  style=0
- effects:
    - ?wOp12 a1=131 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道你為什麼會在這裡，歐文，不過我真的好高興。我現在真的很需要見到一張友善的面孔……

### (sub) DIAL_Z30#241
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳怎麼跑出卡瓦爾堡了？

### (sub) DIAL_Z30#242
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞魯莎親王手下的一些人路過卡瓦爾堡的時候，我們就跟著來了。他們說有場戰事即將爆發，會有軍隊在這裡跟波斯維奇夫人一起集結。這是真的嗎？我們真的要再次跟莫瑞德人開戰了？

### (sub) DIAL_Z30#243
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道能透露多少，不過這種可能性相當高。其實戈拉斯跟我ó應該是要去找一位星塢島來的法師，叫帕格，不過眼看這裡就要開戰了……我想先確認妳跟妳父親都平安無事。

### (sub) DIAL_Z30#244
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們怎麼會不平安？戰火總不會一路打到這麼南邊來吧……會嗎？

### (sub) DIAL_Z30#245
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不會……只是……有幾件事，等局勢平靜下來之後我們得好好談談。我只是很高興妳平安無事。我一直擔心妳會出什麼事。

### (sub) DIAL_Z30#246
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你越來越傻里傻氣，跟我有得比了。話說回來……你都吃些什麼？瘦得跟骨頭似的。我能為你們倆做點什麼嗎？

### (sub) DIAL_Z30#247
- speaker=0  style=0
- effects:
    - push return-address key 21193 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#248
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好了，既然知道妳平安無事，我看我們該走了。我也不確定我們還會在這一帶待多久。妳需要什麼嗎？

### (sub) DIAL_Z30#249
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不用，我想我會沒事的。表哥，你也照顧好自己。

### (sub) DIAL_Z30#250
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳也是，烏格妮。我保證，一有空就會來看妳。

### (sub) DIAL_Z30#251
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [21554..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#252
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [21649..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Ugyne_Corvalis

### (sub) DIAL_Z30#253
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#254
- speaker=0  style=6
- effects:
    - preload portraits 0x8,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 烏格妮朝他們喊了一聲。  她站到表哥面前，用那雙淡琥珀色的眼睛直直盯著他。

### (sub) DIAL_Z30#255
- speaker=8  style=0
- effects:
    - ?wOp12 a1=131 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你又回來了！怎麼了？

### (sub) DIAL_Z30#256
- speaker=0  style=0
- effects:
    - push return-address key 21910 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#257
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好了，既然知道妳平安無事，我看我們該走了。我也不確定我們還會在這一帶待多久。妳需要什麼嗎？

### (sub) DIAL_Z30#258
- speaker=8  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不用，我想我會沒事的。表哥，你也照顧好自己。

### (sub) DIAL_Z30#259
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳也是，烏格妮。我保證，一有空就會來看妳。

### (sub) DIAL_Z30#260
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [22271..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#261
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [22365..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Ugyne_Corvalis

### (sub) DIAL_Z30#262
- speaker=0  style=0
- branches:
    - [flag 0x1eab in [24672..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#263
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#264
- speaker=9  style=0
- effects:
    - ?wOp12 a1=98 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我今天特地交代過不許有人打擾我，不過蜜莉似乎覺得你們來訪可能有些要緊事。

### (sub) DIAL_Z30#265
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道算不算得上ó要緊ð，不過我想您對自己的親人，多少該ó客氣ð一點吧，叔叔。

### (sub) DIAL_Z30#266
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別以為你有資格教訓我的禮數，歐文。你要是真如你父親多年前冊封的那樣，是個規規矩矩的扈從，此刻早該在提伯恩你哥哈羅德身邊了。可你倒好，愛去哪就去哪，對誰都不用負半點責任。我ó女兒烏格妮的責任感，可比你強得多了……

### (sub) DIAL_Z30#267
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 三年沒見我了，您的意見倒是不少。您一直都這麼討厭我嗎？

### (sub) DIAL_Z30#268
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不是ó討厭ð不討厭的問題，歐文。可你這樣像個江湖藝人或傭兵一樣到處遊蕩，簡直是家族的恥辱。你再這麼下去，要怎麼指望娶到哪位公爵或伯爵的女兒？你又要怎麼學會治理領地？

### (sub) DIAL_Z30#269
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？整天坐在那裡，聽兩個吵架的自耕農爭論這塊地是誰的、那塊地又是誰的？我可不ó想過那種日子。我想成為法師，像星塢島的帕格那樣。

### (sub) DIAL_Z30#270
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你打算靠著替萊亞姆王表演客廳戲法混口飯吃？靠著讓耳朵冒煙來換一頓晚餐嗎……

### (sub) DIAL_Z30#271
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伯爵大人，很抱歉打斷您這場爭論，不過眼下他正是ó我的扈從，為我效力。在下克朗多的洛克利爾紳爵，亞魯莎親王麾下的顧問……

### (sub) DIAL_Z30#272
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從克朗多來的？請恕我失禮，我沒注意到您的紋章。我居然就這麼站在這裡，跟家人吵起架來了！有什麼我能為您效勞的嗎？

### (sub) DIAL_Z30#273
- speaker=0  style=0
- effects:
    - push return-address key 24257 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#274
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#275
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#276
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#277
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24577..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#278
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24672..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Count_Corvalis

### (sub) DIAL_Z30#279
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#280
- speaker=9  style=0
- effects:
    - play sfx 98
- branches:
    - [always] -> node 0 (no jump)
- text: 我今天還有不少事要忙，麻煩你們快點說明來意……

### (sub) DIAL_Z30#281
- speaker=0  style=0
- effects:
    - push return-address key 24852 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#282
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#283
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#284
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#285
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [25172..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#286
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [25266..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Count_Corvalis

### (sub) DIAL_Z30#287
- speaker=0  style=0
- branches:
    - [flag 0x1eab in [27129..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#288
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#289
- speaker=9  style=0
- effects:
    - ?wOp12 a1=98 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我現在沒空聊天。也許你父親在提伯恩那邊治家比較隨性，可在卡瓦爾——我們一切都得照規矩來。要是我打算把女兒栽培成未來的王妃，就得確保她從小熟悉宮廷生活的禮數。

### (sub) DIAL_Z30#290
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó王妃烏格妮？您打算怎麼安排這件事？我還以為她已經跟費隆準男爵訂婚了……

### (sub) DIAL_Z30#291
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 關鍵字是ñ『曾經』ð，姪兒。我已經決定，該替她找個更高的門第。克朗多親王有兩個兒子，都還未婚，配我這位嬌女綽綽有餘。我看無論哪一個，都是個好夫婿。

### (sub) DIAL_Z30#292
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我同意，不過恕我直言，博里克跟厄蘭不過是兩個活蹦亂跳、看見女生就跑的ó十一歲小男孩罷了。我看這時候跟他們提求婚的事，他們兩個大概都要嚇壞了，不過我倒是能想像亞魯莎親王會覺得這主意挺不錯。

### (sub) DIAL_Z30#293
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我當然不是建議他們現在就成婚。他們還需要點時間自然長大，就說兩年吧。十三歲正是適婚的好年紀。

### (sub) DIAL_Z30#294
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃……等我回到克朗多，我會跟亞魯莎親王提一提這件事。

### (sub) DIAL_Z30#295
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵大人，我將永遠感激不盡。有什麼我能回報您的嗎？

### (sub) DIAL_Z30#296
- speaker=0  style=0
- effects:
    - push return-address key 26714 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#297
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#298
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#299
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#300
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27034..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#301
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27129..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Count_Corvalis

### (sub) DIAL_Z30#302
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#303
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我今天還有不少事要忙，麻煩你們快點說明來意……

### (sub) DIAL_Z30#304
- speaker=0  style=0
- effects:
    - push return-address key 27299 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#305
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#306
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#307
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#308
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27619..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#309
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27713..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Count_Corvalis

### (sub) DIAL_Z30#310
- speaker=0  style=0
- branches:
    - [flag 0x1eab in [29444..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#311
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#312
- speaker=9  style=0
- effects:
    - ?wOp12 a1=98 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 勞煩您告訴我，先生，我到底做了什麼，才會對這世上這些微不足道的傢伙有這麼大的吸引力？從我今早踏出寢室那一刻起，僕人就像蝨子一樣圍著我團團轉，煩人的親戚也纏著我的腳踝不放。您能不能行行好，讓我清靜一下？！

### (sub) DIAL_Z30#313
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們有件非常重要的事要處理，必須跟您談談……

### (sub) DIAL_Z30#314
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管你們要辦什麼事，我十分確定都跟我無關！紳爵大人，我才不管你們的事是什麼性質，我還有別的事要煩……

### (sub) DIAL_Z30#315
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？您的煩心事，難道比克朗多親王的事還要緊嗎？要是真是這樣，我回去之後一定樂意向他詳細稟報。您說吧，我這就記下來。我相信亞魯莎一定會很感興趣。

### (sub) DIAL_Z30#316
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您說親王？請理解，眼下有些——事情——我不便完全公開討論。只能說，我跟肯廷拉什卡胡利神殿的祭司們，因為一件私事起了些ó爭執。所以，若您能原諒我方才的失態，我很樂意為親王效勞。您到底需要我做什麼？

### (sub) DIAL_Z30#317
- speaker=0  style=0
- effects:
    - push return-address key 29029 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#318
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#319
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#320
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#321
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29349..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#322
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [29444..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Count_Corvalis

### (sub) DIAL_Z30#323
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#324
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 姪兒，紳爵大人，啊……這位精靈先生。還有什麼我能幫上忙的嗎？

### (sub) DIAL_Z30#325
- speaker=0  style=0
- effects:
    - push return-address key 29600 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#326
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科瓦利斯伯爵，您幫了大忙，不過我們也該回去忙正事了。請代我向令嬡烏格妮問好。

### (sub) DIAL_Z30#327
- speaker=9  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的，紳爵大人。祝您一路順風，也請ó多看顧一下我這姪兒。

### (sub) DIAL_Z30#328
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，我一定會的，相信我。再會。

### (sub) DIAL_Z30#329
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29920..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#330
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [30014..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Count_Corvalis

### (sub) DIAL_Z30#331
- speaker=0  style=0
- branches:
    - [flag 0x1eac in [30888..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#332
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#333
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾的肚子咕嚕作響。  他等另一名客人點完硬麵包捲跟一瓶波特酒之後，才招呼這名酒館老闆暫時放下其他事務，希望既能打聽點消息，又能順便討點吃的……

### (sub) DIAL_Z30#334
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是彼得，有時候人稱ó「灰ó袍ó彼得」。今天想來點什麼？

### (sub) DIAL_Z30#335
- speaker=0  style=0
- effects:
    - push return-address key 30481 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#336
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我唐突，我們還有些別的事要辦，時間也不多了。也許改天再見。

### (sub) DIAL_Z30#337
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很期待！祝您愉快！

### (sub) DIAL_Z30#338
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是。祝您生意興隆！

### (sub) DIAL_Z30#339
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [30793..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#340
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [30888..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Peter_the_Grey

### (sub) DIAL_Z30#341
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#342
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾朝酒館老闆招了招手。  「灰袍」彼得只停下來把一張打翻了麥酒杯的桌子擦乾淨，隨即匆匆趕了過來。

### (sub) DIAL_Z30#343
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 又回來光顧啦！啊，我最近手氣真是旺。老彼得能為你們做點什麼？

### (sub) DIAL_Z30#344
- speaker=0  style=0
- effects:
    - push return-address key 31268 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#345
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我唐突，我們還有些別的事要辦，時間也不多了。也許改天再見。

### (sub) DIAL_Z30#346
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很期待！祝您愉快！

### (sub) DIAL_Z30#347
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是。祝您生意興隆！

### (sub) DIAL_Z30#348
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [31580..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#349
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [31674..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Peter_the_Grey

### (sub) DIAL_Z30#350
- speaker=0  style=0
- branches:
    - [flag 0x1eac in [33363..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#351
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#352
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士的肚子咕嚕作響。  他等另一名客人點完烤雞跟一杯麥酒之後，才招呼這名酒館老闆暫時放下其他事務，希望既能打聽點消息，又能順便討點吃的……

### (sub) DIAL_Z30#353
- speaker=11  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望兩位今晚不是來找熱鬧的。『鴨頭』今晚有點冷清。安靜得就像晚餐時段有人在我地板正中央擺了具屍體似的。

### (sub) DIAL_Z30#354
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 該不會真有吧？

### (sub) DIAL_Z30#355
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哈，沒有啦！除了幾個月前有人企圖對伯爵一家下毒那件事，卡瓦爾堡這一帶大致上算是相當平靜。這裡的農家人大多各過各的，只操心自己的莊稼，不太管別人的閒事。

### (sub) DIAL_Z30#356
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你覺得是誰想毒害他們？

### (sub) DIAL_Z30#357
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你聽堡壘那邊的說法，還真會以為根本沒這回事。他們都是些硬骨頭，一個個表現得跟什麼都沒發生過一樣。要不是我最好的廚房小廝在試喝那瓶波特酒時中毒喪命，這事對我來說也不打緊。我現在雇了個新的，可我還是懷念我那個老幫手。他是個好孩子……好了……我都嘮叨這麼久了，兩位想來點什麼？

### (sub) DIAL_Z30#358
- speaker=0  style=0
- effects:
    - push return-address key 32989 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#359
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#360
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#361
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#362
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [33268..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#363
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33363..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Peter_the_Grey

### (sub) DIAL_Z30#364
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#365
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士朝酒館老闆招了招手。  「灰袍」彼得只停下來把一張打翻了麥酒杯的桌子擦乾淨，隨即匆匆趕了過來。

### (sub) DIAL_Z30#366
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼快又回來啦？我倒是不介意，我喜歡有人陪。彼得能為兩位做點什麼？

### (sub) DIAL_Z30#367
- speaker=0  style=0
- effects:
    - push return-address key 33731 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#368
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#369
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#370
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#371
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34010..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#372
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34104..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Peter_the_Grey

### (sub) DIAL_Z30#373
- speaker=0  style=0
- branches:
    - [flag 0x1eac in [35748..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#374
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#375
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文的肚子咕嚕作響。  他等另一名客人點完烤雞跟一杯麥酒之後，才招呼這名酒館老闆暫時放下其他事務，希望既能打聽點消息，又能順便討點吃的……

### (sub) DIAL_Z30#376
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 晚安，各位。需要什麼儘管吩咐。

### (sub) DIAL_Z30#377
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們三個都挺好，不過聽你這語氣，日子過得不太順啊。朋友，有什麼煩心事嗎？

### (sub) DIAL_Z30#378
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小夥子，你該不會有興趣來當個洗碗小廝吧？

### (sub) DIAL_Z30#379
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 老實說，這目前還真不在我的志向清單上。跟幫手處得不太順？

### (sub) DIAL_Z30#380
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 與其說是麻煩，不如說是失望吧。我都不知道該怎麼跟那孩子說了。他人是挺好的，善良、老實、又肯吃苦。可整體來說，他連鍋柄在哪頭都搞不清楚。我花了好幾週想教他做飯，好讓我跟老婆能偶爾歇口氣，可一說到做飯，他就跟雷獄草原一樣一片荒蕪。我實在不知道還能怎麼辦了。不過別光聽我發牢騷了。彼得能為你們做點什麼？

### (sub) DIAL_Z30#381
- speaker=0  style=0
- effects:
    - push return-address key 35374 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#382
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#383
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#384
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#385
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [35653..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#386
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [35748..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Peter_the_Grey

### (sub) DIAL_Z30#387
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#388
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士朝酒館老闆招了招手。  「灰袍」彼得只停下來把一張打翻了麥酒杯的桌子擦乾淨，隨即匆匆趕了過來。

### (sub) DIAL_Z30#389
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼快又回來啦？我倒是不介意，我喜歡有人陪。彼得能為兩位做點什麼？

### (sub) DIAL_Z30#390
- speaker=0  style=0
- effects:
    - push return-address key 36106 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#391
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#392
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#393
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#394
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [36385..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#395
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36479..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Peter_the_Grey

### (sub) DIAL_Z30#396
- speaker=0  style=0
- branches:
    - [flag 0x1eac in [37627..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#397
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#398
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文的肚子咕嚕作響。  他等另一名客人點完烤雞跟一杯麥酒之後，才招呼這名酒館老闆暫時放下其他事務，希望既能打聽點消息，又能順便討點吃的……

### (sub) DIAL_Z30#399
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 進來吧，進來吧。我猜你們聽說我們『鴨頭』新來的廚子了吧？哦，他做的烤肉簡直是一絕，雞肉更是了不得。

### (sub) DIAL_Z30#400
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來太棒了。也許我們待會兒可以嚐嚐看。

### (sub) DIAL_Z30#401
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 相信我，你們絕對不會後悔的，一點都不會！價錢當然也很公道。那，今晚想來點什麼？

### (sub) DIAL_Z30#402
- speaker=0  style=0
- effects:
    - push return-address key 37253 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#403
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#404
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#405
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#406
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [37532..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#407
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [37627..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Peter_the_Grey

### (sub) DIAL_Z30#408
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#409
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文朝酒館老闆招了招手。  「灰袍」彼得只停下來把一張打翻了麥酒杯的桌子擦乾淨，隨即匆匆趕了過來。

### (sub) DIAL_Z30#410
- speaker=11  style=0
- effects:
    - ?wOp12 a1=124 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是抵擋不住『鴨頭』的香味吧，嗯？我們這會兒正烤著十來隻雞呢！那，今晚想來點什麼？

### (sub) DIAL_Z30#411
- speaker=0  style=0
- effects:
    - push return-address key 38068 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#412
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我們失陪，還有些別的事要辦，時間也不多了。

### (sub) DIAL_Z30#413
- speaker=11  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，好吧，看來我還是得自己消磨時間了。祝兩位愉快！

### (sub) DIAL_Z30#414
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#415
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [38347..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#416
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [38441..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Peter_the_Grey

### (sub) DIAL_Z30#417
- speaker=0  style=0
- branches:
    - [flag 0x1ead in [40548..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#418
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
    - play sfx 99
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#419
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳的丈夫終於回來了。

### (sub) DIAL_Z30#420
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 丈夫？這話怎麼說？氏族領袖？憑什麼資格？曾幾何時，你光榮而有尊嚴地擔起這些頭銜。阿爾達尼恩氏族曾像一頭金龍般盤踞在你身邊，只待你一聲令下便會騰空而起，粉碎擋在你面前的一切。如今那頭龍在哪？牠為何沉睡不醒？

### (sub) DIAL_Z30#421
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 庫利奇……妳在那片奇異的星空下，夢見的就只有這些嗎？一段已死的過去？穆爾曼達穆斯那些演說，除了讓我們明白自己有多軟弱，我們還從中得到過什麼？我們在那場敗仗中領悟到的精神，除了發現自己正從內部腐爛之外，還有什麼？是時候放下屠刀、正視自己了，親手了結我們已經淪為的那頭怪物。

### (sub) DIAL_Z30#422
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯，你希望莫瑞德人擁有什麼樣的命運？我們該再一次低頭伏地，把自己的意志交給住在艾爾凡達的伊列德人奴役嗎？就像我們在那段黑暗世紀裡，曾在瓦爾赫魯腳下瑟瑟發抖那樣？他們的亞葛拉蘭娜王后，不會把我們當作家人接納回去，只會把我們當成奴隸。你也見過我們那些回歸他們的同胞。他們如今除了在精靈麾下當一頭頭閹過的公牛，還算得上是什麼？

### (sub) DIAL_Z30#423
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道他們在那片深夜星空下，究竟是歡欣還是哀泣，可他們的孩子能活到高齡，能在王國的陽光下自由交易。而我們卻得為了區區一條麵包大打出手，得殺害自己的同族兄弟，只因深怕他們趁我們熟睡時偷走我們的幼崽。是時候讓我們超越野蠻人這個身分了。

### (sub) DIAL_Z30#424
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你來這裡做什麼，戈拉斯？該不會是為了爭論一段我們之間早已死去的愛情吧。

### (sub) DIAL_Z30#425
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不……我還需要妳的幫忙，就一小段時間，之後我便會離去，讓妳過妳自己的日子。這是我對我這位前妻僅剩的請求。到那之後，妳便可以隨心所欲了。

### (sub) DIAL_Z30#426
- speaker=12  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看在我曾深愛之人的份上，我聽你說，也會盡力而為。說吧，戈拉斯。

### (sub) DIAL_Z30#427
- speaker=0  style=0
- effects:
    - push return-address key 40431 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#428
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40460..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#429
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [40548..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C4_Cullich

### (sub) DIAL_Z30#430
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#431
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#432
- speaker=12  style=0
- effects:
    - ?wOp12 a1=99 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯的六賢者正在搜尋你們，我沒辦法保證還能拖住他們派來的搜索隊多久。有話快說。

### (sub) DIAL_Z30#433
- speaker=0  style=0
- effects:
    - push return-address key 40933 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#434
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40962..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#435
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [41049..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Cullich

### (sub) DIAL_Z30#436
- speaker=0  style=0
- branches:
    - [flag 0x1eae in [42603..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#437
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#438
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯敲了敲木門。  一名穿著制服的莫瑞德人前來應門，盯著歐文看了片刻，才領他們進屋。守衛把他們帶進一間內室，將他們引見給莫萊伍夫。

### (sub) DIAL_Z30#439
- speaker=13  style=0
- effects:
    - ?wOp12 a1=117 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們有什麼事？長話短說。

### (sub) DIAL_Z30#440
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩薩戈斯已遭圍困。納拉布大人與數目不明的心腹，放出了被囚在地牢裡的反叛分子，一同逃往北方。迪勒肯要求您跟六賢者剩下的成員立即支援。

### (sub) DIAL_Z30#441
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 瘋了！我的部隊已經就位，隨時準備出擊，我們的目標離這裡只有一週的行軍路程。要是現在離開，等最後總攻的時刻來臨，我們就沒法就位了！迪勒肯該不會真打算讓我們繞去雪原，追一小撮懦夫吧？！

### (sub) DIAL_Z30#442
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 令尊的用意我不得而知。我只是奉命傳話。此外，他還要求了解您這邊行動的進展。

### (sub) DIAL_Z30#443
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要不是他是我父親，我早就割了他這副無禮的喉嚨了！他想知道什麼？

### (sub) DIAL_Z30#444
- speaker=0  style=0
- effects:
    - push return-address key 42271 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#445
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您已經回答了我們奉命打探的一切。

### (sub) DIAL_Z30#446
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是引人入勝。現在退下吧，替我向父親轉達ñ我的ñ問候。

### (sub) DIAL_Z30#447
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 遵命，莫萊伍夫大人。

### (sub) DIAL_Z30#448
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [42514..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#449
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [42603..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C4_Moraeulf

### (sub) DIAL_Z30#450
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#451
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯敲了敲木門。  一名穿著制服的莫瑞德人前來應門，盯著歐文看了片刻，才領他們進屋。守衛把他們帶進一間內室，將他們引見給莫萊伍夫。

### (sub) DIAL_Z30#452
- speaker=13  style=0
- effects:
    - ?wOp12 a1=117 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我父親又派你們來確認我有沒有能力ñ自己餵飽自己，還是你們忘了帶什麼東西？

### (sub) DIAL_Z30#453
- speaker=0  style=0
- effects:
    - push return-address key 43065 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#454
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 若您允許，我們這就告退……

### (sub) DIAL_Z30#455
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管你們是誰，我勸你們最好別這樣嘲弄我。等這場戰事結束之後……

### (sub) DIAL_Z30#456
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……我們終究還是令尊的僕從，您也知道他對自己ñ所擁有的ð東西向來護得緊。莫萊伍夫大人，告辭了……

### (sub) DIAL_Z30#457
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [43422..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#458
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [43510..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Moraeulf

### (sub) DIAL_Z30#459
- speaker=0  style=0
- branches:
    - [flag 0x1eae in [45232..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#460
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#461
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#462
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ñCrualla ñsholbah ñmoredhelan ñnordrannas ñbaktu?

### (sub) DIAL_Z30#463
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃，我們是……ñ奎格ð人，大人。要是您能繼續用王國語交談，我們或許能更好地理解彼此？

### (sub) DIAL_Z30#464
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ñSebah！圖蘭尼裂界之門那邊的移轉進度如何了？

### (sub) DIAL_Z30#465
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們遭到伏擊了，莫萊伍夫大人！有好幾個全副武裝的人正穿越幽暗林。我們算是僥倖逃了出來！

### (sub) DIAL_Z30#466
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 王國的士兵？

### (sub) DIAL_Z30#467
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許……我知道他們不是打著我們的旗號，所以應該不是傭兵。我們聽到他們來的方向，更遠處還有其他動靜。搞不好是整支軍隊。

### (sub) DIAL_Z30#468
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡可能已經聯繫上什麼人，拉響了警報。該死！這下賽瑟儂的行軍計畫要複雜了。他們離六賢者的裂界機有多近？

### (sub) DIAL_Z30#469
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不清楚。我們在遭遇攻擊時被打散了……我們的傳令兵都死了，正需要戰報。希望您能幫我們一把。

### (sub) DIAL_Z30#470
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們想知道什麼？

### (sub) DIAL_Z30#471
- speaker=0  style=0
- effects:
    - push return-address key 44877 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#472
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管有沒有我們的小隊，我們都還有命令要執行。

### (sub) DIAL_Z30#473
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就速速前去執行。若再有任何變故，立刻向我回報。

### (sub) DIAL_Z30#474
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 遵命，大人……

### (sub) DIAL_Z30#475
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45143..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#476
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [45232..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C7_Moraeulf

### (sub) DIAL_Z30#477
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1044 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#478
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#479
- speaker=13  style=0
- effects:
    - ?wOp12 a1=117 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 又是你們。看你們又出現了，想必是發生了什麼值得打斷我的事吧？

### (sub) DIAL_Z30#480
- speaker=0  style=0
- effects:
    - push return-address key 45677 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#481
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管有沒有我們的小隊，我們都還有命令要執行。

### (sub) DIAL_Z30#482
- speaker=13  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就速速前去執行。若再有任何變故，立刻向我回報。

### (sub) DIAL_Z30#483
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 遵命，大人……

### (sub) DIAL_Z30#484
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45943..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#485
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [46031..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C7_Moraeulf

### (sub) DIAL_Z30#486
- speaker=0  style=0
- branches:
    - [flag 0x1eaf in [47776..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#487
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#488
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 附近有座花園。  歐文皺著鼻子聞著新鮮肥料的氣味，指了指路邊揚起的一小片塵霧。塵霧中，一個蘑菇般矮胖的男人正忙著幹活，鋤頭在一畦冒著粉紅嫩芽的馬鈴薯上起起落落。洛克利爾臉上掛著那抹難以壓抑的笑容，悄悄摸到了這名修士身後……

### (sub) DIAL_Z30#489
- speaker=14  style=0
- effects:
    - ?wOp12 a1=96 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我差點嚇得跳出袍子外！你們好啊，陌生人。

### (sub) DIAL_Z30#490
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望我們沒打擾到您。

### (sub) DIAL_Z30#491
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，不會。反正我也正要離開花園了。雙手忙碌，腦子才會轉得快嘛。你們是要去薩斯嗎？

### (sub) DIAL_Z30#492
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧，修士……？

### (sub) DIAL_Z30#493
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 薩斯的馬克修士。很高興認識你們。這裡不常有ñ識字之人上門。比起黃金或風流韻事，平民似乎對書本沒什麼興趣。不過我們的學者倒是不少，一個個都讀蟲蛀的舊書讀到眼睛快瞎了，還有十來個男孩把青春都耗在抄寫我們的典藏室裡。這裡真是個特別的地方。

### (sub) DIAL_Z30#494
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我有個朋友曾經來過這裡。他告訴我，你們信奉的是知識之神。

### (sub) DIAL_Z30#495
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是有人這麼說沒錯，我想某種程度上也算是真的。要是有什麼問題在別處都找不到答案，你們最好的希望就是來我們的典藏室看看。

### (sub) DIAL_Z30#496
- speaker=0  style=0
- effects:
    - push return-address key 47434 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#497
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。

### (sub) DIAL_Z30#498
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能幫上忙總是樂意之至。歡迎再來找我。

### (sub) DIAL_Z30#499
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。再見！

### (sub) DIAL_Z30#500
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [47683..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#501
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [47776..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Brother_Marc

### (sub) DIAL_Z30#502
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#503
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x0,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝洛克利爾比劃了一下。

### (sub) DIAL_Z30#504
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來上次還沒把你的耳朵灌滿呢！是什麼風把你吹回薩斯兄弟會來的？

### (sub) DIAL_Z30#505
- speaker=0  style=0
- effects:
    - push return-address key 48090 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#506
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。

### (sub) DIAL_Z30#507
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能幫上忙總是樂意之至。歡迎再來找我。

### (sub) DIAL_Z30#508
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。再見！

### (sub) DIAL_Z30#509
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [48339..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#510
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [48431..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Brother_Marc

### (sub) DIAL_Z30#511
- speaker=0  style=0
- branches:
    - [flag 0x1eaf in [49577..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#512
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#513
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x5,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝詹姆士比劃了一下。

### (sub) DIAL_Z30#514
- speaker=14  style=0
- effects:
    - ?wOp12 a1=96 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 被逮個正著！恐怕你們會覺得我是個假扮修士的農夫，而不是相反。你們好嗎？

### (sub) DIAL_Z30#515
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等我這位年輕的扈從歐文忘了自己還有腳這回事，我想我們就會過得不錯了……

### (sub) DIAL_Z30#516
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他這年紀就開始喊疼，真不敢想像到了我這把年紀他會抱怨成什麼樣！到時候大概走到哪都得讓人抬著了！

### (sub) DIAL_Z30#517
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他這是在練習當凱許皇帝吧，肯定沒錯。

### (sub) DIAL_Z30#518
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼，旅途中的朋友們，這次想向薩斯請教什麼問題？

### (sub) DIAL_Z30#519
- speaker=0  style=0
- effects:
    - push return-address key 49235 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#520
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。

### (sub) DIAL_Z30#521
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能幫上忙總是樂意之至。歡迎再來找我。

### (sub) DIAL_Z30#522
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。再見！

### (sub) DIAL_Z30#523
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [49484..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#524
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [49577..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Brother_Marc

### (sub) DIAL_Z30#525
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#526
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x5,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝詹姆士比劃了一下。

### (sub) DIAL_Z30#527
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這次我能替你們查些什麼？王國歷史？凱許律法？精靈傳統？儘管問吧，我會盡力找出你們需要的一切。

### (sub) DIAL_Z30#528
- speaker=0  style=0
- effects:
    - push return-address key 49943 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#529
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。

### (sub) DIAL_Z30#530
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能幫上忙總是樂意之至。歡迎再來找我。

### (sub) DIAL_Z30#531
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。再見！

### (sub) DIAL_Z30#532
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50192..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#533
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50284..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Brother_Marc

### (sub) DIAL_Z30#534
- speaker=0  style=0
- branches:
    - [flag 0x1eaf in [52538..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#535
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#536
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x5,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭握著鋤頭，朝詹姆士比劃了一下。

### (sub) DIAL_Z30#537
- speaker=14  style=0
- effects:
    - ?wOp12 a1=96 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興見到你們，不過我建議你們現在還是保持點距離。薩斯這邊爆發了奎格熱，我也不確定自己身上有沒有帶著病。

### (sub) DIAL_Z30#538
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您怎麼會不知道？提伯恩隨便一個五歲小男孩都認得出警訊。

### (sub) DIAL_Z30#539
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在提伯恩或許是這樣，但容我指出，這裡並不是提伯恩。

### (sub) DIAL_Z30#540
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還以為薩斯的伊夏兄弟會應該無所不知呢。

### (sub) DIAL_Z30#541
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 或許有朝一日會的，只要伊夏神保佑，不過讓我跟你說件事。我像你這麼大的時候，曾在種植上發現了一件不可思議的事。多年來，我把自己在田裡耕作時學到的東西都記在日記裡。有一天——就在我剛加入伊夏兄弟會不久之後——我翻閱著自己的一些筆記，竟有了個驚人的發現！這將永遠改變農夫種植作物的方式！我興奮極了，決定要把這個大祕密公諸於世，便把日記得意洋洋地夾在腋下，一路小跑到了最近的城鎮。

### (sub) DIAL_Z30#542
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那些農夫用了您的技術嗎？

### (sub) DIAL_Z30#543
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，用了……而且他們早就用了三百多年了！比起這些農夫早就知道的東西，我那點粗淺的小把戲不過是孩子氣的空想罷了。我想說的是：要是我們在馬拉克十字鎮的弟兄，把某些事當成理所當然的常識，對我們其他人來說，那可能會因為他們以為我們早就該知道，而多年來一直是不為人知的知識。知識就跟其他可攜帶的財貨一樣，必須被收集、被傳播出去。朋友們，這正是薩斯之所以存在的主要原因。

### (sub) DIAL_Z30#544
- speaker=0  style=0
- effects:
    - push return-address key 52196 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#545
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。

### (sub) DIAL_Z30#546
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能幫上忙總是樂意之至。歡迎再來找我。

### (sub) DIAL_Z30#547
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。再見！

### (sub) DIAL_Z30#548
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52445..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#549
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52538..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Brother_Marc

### (sub) DIAL_Z30#550
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#551
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x5,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝詹姆士比劃了一下。

### (sub) DIAL_Z30#552
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別靠太近。就像我先前說的，我可能帶著熱病，不想害你們任何人生病。也許你們想請我到薩斯的圖書館替你們查點東西？

### (sub) DIAL_Z30#553
- speaker=0  style=0
- effects:
    - push return-address key 52934 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#554
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們至少有些東西可以好好想想了。謝謝您，馬克修士。也許我們下次來訪時，還能跟您討顆蕪菁。

### (sub) DIAL_Z30#555
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會留意的！祝您愉快！

### (sub) DIAL_Z30#556
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是……

### (sub) DIAL_Z30#557
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [53225..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#558
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [53317..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Brother_Marc

### (sub) DIAL_Z30#559
- speaker=0  style=0
- branches:
    - [flag 0x1eaf in [55742..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#560
- speaker=0  style=0
- effects:
    - SET flag 0x0021=1
    - SET flag 0x0038=1
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#561
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝歐文比劃了一下。

### (sub) DIAL_Z30#562
- speaker=14  style=0
- effects:
    - ?wOp12 a1=96 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我勸你們最好離薩斯遠一點。我們的多明尼克修士染上了奎格熱。

### (sub) DIAL_Z30#563
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 怎麼沒人在病情惡化之前就治療呢？

### (sub) DIAL_Z30#564
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們誰也不知道他染病了，直到今天早上才發現。他今早醒來後，向兄弟會的藥草師報告說自己感到暈眩。

### (sub) DIAL_Z30#565
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是熱病的早期徵兆之一，不過我倒不會太過擔心。奎格熱對成年人來說很少致命。

### (sub) DIAL_Z30#566
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓我擔心的並不是熱病本身的主要影響。身為『守門者』，多明尼克修士是我們之中法術造詣最深的人。要是他開始出現幻覺，恐怕就會失去分辨真實威脅與想像威脅的能力。他可能會把兄弟會的其他成員當成敵人，又或者會在外界看見根本不存在的威脅。我們從星塢島的帕格那裡得知，法師生病時確實可能發生這類事情。

### (sub) DIAL_Z30#567
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有人能替他退燒嗎？

### (sub) DIAL_Z30#568
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我相信藥草師會盡他所能，不過我們最大的希望，還是寄託在多明尼克修士自己那股鋼鐵般的意志上。在他退燒之前，薩斯的伊夏神修道院會是個極其危險的地方，我勸你們最好別再靠近。你們是有什麼事需要修道院幫忙嗎？

### (sub) DIAL_Z30#569
- speaker=0  style=0
- effects:
    - push return-address key 54927 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#570
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會盡力想辦法解決，不過我們還有另一件要事要處理，時間也不多了。要是多明尼克修士真的開始產生幻覺，會發生什麼事？

### (sub) DIAL_Z30#571
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不敢十分肯定。我猜測他會啟動修道院的神祕防禦。要是真發生那種事，恐怕整座修道院都無法進入了……

### (sub) DIAL_Z30#572
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 至少聽起來他不會對性命構成威脅……要是我們遇上什麼我覺得可能有幫助的東西，我保證會盡快回來。作為交換，請幫我們個忙，在這件事解決之前別擋到多明尼克的路。再見了，修士……

### (sub) DIAL_Z30#573
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [55649..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#574
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [55742..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Brother_Marc

### (sub) DIAL_Z30#575
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#576
- speaker=0  style=6
- effects:
    - preload portraits 0xe,0x3,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克修士的身影映入眼簾。他那雙厚實的拳頭仍緊握著鋤頭，朝歐文比劃了一下。

### (sub) DIAL_Z30#577
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就像飛蛾撲火一樣？薩斯有什麼魔力，讓你們這麼快又回來了？

### (sub) DIAL_Z30#578
- speaker=0  style=0
- effects:
    - push return-address key 56038 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#579
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 索爾加斯跟我還有些事要處理，我想該向您道別了。

### (sub) DIAL_Z30#580
- speaker=14  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 願伊夏神保佑你們一路平安，年輕人。

### (sub) DIAL_Z30#581
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會盡力的。謝謝您。再見了，馬克修士。

### (sub) DIAL_Z30#582
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [56310..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#583
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [56462..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Brother_Marc ///////////////////////////////////////////////////////////

### (sub) DIAL_Z30#584
- speaker=0  style=0
- branches:
    - [flag 0x1eb0 in [58745..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#585
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#586
- speaker=0  style=6
- effects:
    - ?wOp12 a1=57 a2=0
    - ?wOp12 a1=29 a2=0
    - preload portraits 0xf,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 火花在走廊中竄射而過。  洛克利爾將歐文猛地按在礦坑坑壁上，自己也險險躍身閃避，某樣東西正沿著石地滑掠而過。那團發光的火焰錐忽然撞上一道看不見的牆，瞬間消失無蹤。過了好幾個漫長的心跳，這位紳爵才緩緩從牆邊移開身子，正好與一個矮壯如樹樁的男人四目相對。

### (sub) DIAL_Z30#587
- speaker=15  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
    - ?wOp12 a1=118 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這該死的破鎚子！……你這身子骨裡最好是藏了個惡魔。你們是來幫忙宰了那怪物的吧，是不是？

### (sub) DIAL_Z30#588
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 怪物？

### (sub) DIAL_Z30#589
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 怪物，沒錯！半個禮拜前，我們聽見礦坑裡傳來一陣兇猛的咆哮聲，冷得嚇人。矮人一聽就知道，不管以前聽沒聽過——那是布拉克努爾。打從矮人第一次拿起鎚子挖洞開始，牠就是每個礦工的詛咒。

### (sub) DIAL_Z30#590
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我從沒聽說過牠們……

### (sub) DIAL_Z30#591
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好一段時間沒人聽過了，小子。自從戴隆大帝奪下群島王國以來，上層礦坑就再也沒出現過布拉克努爾。我們原以為早就把牠們全都解決了，可科博德在他們的聖戰中把牠們給攪動起來了。

### (sub) DIAL_Z30#592
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 科博德？

### (sub) DIAL_Z30#593
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們那邊的人管牠們叫地精。牠們以前信奉一頭住在這下面的龍，可那條龍消失以後，牠們就認定是矮人把牠給藏起來了。牠們的首領菲德希爾三不五時就會興起一股聖戰的念頭，想去把牠找出來。這回牠們肯定是驚動了一窩布拉克努爾。如今那些努爾把主通道給塌了，還害死了我們三十個同胞。誰要能宰了牠，我們有賞——當然，前提是你們有那個膽量跟本事。

### (sub) DIAL_Z30#594
- speaker=0  style=0
- effects:
    - push return-address key 58320 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#595
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你撥空，納杜爾。希望你們能把這裡的事情處理好。

### (sub) DIAL_Z30#596
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會沒事的，等我們鑿穿這些岩石、把布拉克努爾解決掉就好了。你們可壓不垮我們矮人。

### (sub) DIAL_Z30#597
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也這麼想。也許我們還會再見。

### (sub) DIAL_Z30#598
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [58650..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#599
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [58745..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Naddur_Ban_Dok

### (sub) DIAL_Z30#600
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#601
- speaker=0  style=6
- effects:
    - ?wOp12 a1=57 a2=0
    - ?wOp12 a1=29 a2=0
    - preload portraits 0xf,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 火花在走廊中竄射而過。  洛克利爾將歐文猛地按在礦坑坑壁上，自己也險險躍身閃避，某樣東西正沿著石地滑掠而過。那團發光的火焰錐忽然撞上一道看不見的牆，瞬間消失無蹤。過了好幾個漫長的心跳，這位紳爵才緩緩從牆邊移開身子，正好與一個矮壯如樹樁的男人四目相對。

### (sub) DIAL_Z30#602
- speaker=15  style=0
- effects:
    - ?wOp12 a1=118 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我搞不清楚你們是要來還是要走，小子們，不過要是你們想找條路穿過麥克莫丹卡達爾通往艾爾凡達，那可就沒指望了。你們儘管說我沒種，或罵我是頭醉牛都成，可我這雙鎚子手，在這些山底下可沒人比得上快。布拉克努爾挖出來的爛攤子，可不是我一眨眼就能清乾淨的！要是你們非去艾爾凡達不可，那就過一個月左右再回來看看，說不定那時候我們已經打通了！還是說，你們是有別的事想問？

### (sub) DIAL_Z30#603
- speaker=0  style=0
- effects:
    - push return-address key 59776 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#604
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們該讓你回去做事了。再次謝謝你願意跟我們聊聊。

### (sub) DIAL_Z30#605
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊，我也很樂意，不過容我先失陪了……

### (sub) DIAL_Z30#606
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。我們這就上路了……

### (sub) DIAL_Z30#607
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [60050..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#608
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [60144..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Naddur_Ban_Dok

### (sub) DIAL_Z30#609
- speaker=0  style=0
- branches:
    - [flag 0x1eb0 in [61848..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#610
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#611
- speaker=0  style=6
- effects:
    - ?wOp12 a1=57 a2=0
    - ?wOp12 a1=29 a2=0
    - preload portraits 0xf,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 火花在走廊中竄射而過。  詹姆士將歐文猛地按在礦坑坑壁上，自己也險險躍身閃避，某樣東西正沿著石地滑掠而過。那團發光的火焰錐忽然撞上一道看不見的牆，瞬間消失無蹤。過了好幾個漫長的心跳，這位紳爵才緩緩從牆邊移開身子，正好與一個矮壯如樹樁的男人四目相對。

### (sub) DIAL_Z30#612
- speaker=15  style=0
- effects:
    - ?wOp12 a1=118 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 但願你們不是為了找路去艾爾凡達來的。我們是有點進展，新清出了大概三哩左右的坑道，不過還有很長的路要走。自從布拉克努爾把通道弄塌以後，我們可是忙得不可開交。

### (sub) DIAL_Z30#613
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們估計還要拖多久？

### (sub) DIAL_Z30#614
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就算派上一百個矮人拚了命地鑿石頭，也還是得花上一段時間。這岩層鬆得跟乳酪皮似的，我們得慢慢來，不然整片都會塌在我們頭上，全部白費工夫。不過我們或許能得到些幫助。我們一直隔著岩石敲敲打打互通消息，對面的同族說，精靈那邊的亞葛拉蘭娜或許能幫上一把。

### (sub) DIAL_Z30#615
- speaker=0  style=0
- effects:
    - push return-address key 61479 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#616
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們該讓你回去做事了。再次謝謝你願意跟我們聊聊。

### (sub) DIAL_Z30#617
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是啊，我也很樂意，不過容我先失陪了……

### (sub) DIAL_Z30#618
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。我們這就上路了……

### (sub) DIAL_Z30#619
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [61753..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#620
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [61848..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Naddur_Ban_Dok

### (sub) DIAL_Z30#621
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#622
- speaker=0  style=6
- effects:
    - ?wOp12 a1=57 a2=0
    - ?wOp12 a1=29 a2=0
    - preload portraits 0xf,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 火花在走廊中竄射而過。  詹姆士將歐文猛地按在礦坑坑壁上，自己也險險躍身閃避，某樣東西正沿著石地滑掠而過。那團發光的火焰錐忽然撞上一道看不見的牆，瞬間消失無蹤。過了好幾個漫長的心跳，這位紳爵才緩緩從牆邊移開身子，正好與一個矮壯如樹樁的男人四目相對。

### (sub) DIAL_Z30#623
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我今天天黑前得清出一段坑道，可沒空一直被打擾。有什麼能為你們效勞的？

### (sub) DIAL_Z30#624
- speaker=0  style=0
- effects:
    - push return-address key 62499 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#625
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你撥空，納杜爾。希望你們能把這裡的事情處理好。

### (sub) DIAL_Z30#626
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會沒事的，等我們鑿穿這些岩石、把布拉克努爾解決掉就好了。你們可壓不垮我們矮人。

### (sub) DIAL_Z30#627
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也這麼想。也許我們還會再見。

### (sub) DIAL_Z30#628
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [62829..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#629
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [62923..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Naddur_Ban_Dok

### (sub) DIAL_Z30#630
- speaker=0  style=0
- branches:
    - [flag 0x1eb0 in [64118..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#631
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#632
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 一道陰影靠近。  那身影從礦坑通道陰暗的角落中，朝他們走了過來。@0的脈搏頓時加快，但看出對方並無攻擊之意後，便稍稍放鬆下來。

### (sub) DIAL_Z30#633
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們現在算是徹底停工了。原本都快把整段坑道打通到艾爾凡達了，結果又發現一個該死的布拉克努爾巢穴！雖然只是隻小的，我們也把牠給宰了，可這事就讓我們忙上了好幾個禮拜。牠一隻就塌了好幾百碼的岩石。我們得先確保這段坑道禁得起再度開鑿。再過幾個月，我們應該就能打通到艾爾凡達了。

### (sub) DIAL_Z30#634
- speaker=0  style=0
- effects:
    - push return-address key 63693 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#635
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你撥空，納杜爾。希望你們能把這裡的事情處理好。

### (sub) DIAL_Z30#636
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會沒事的，等我們鑿穿這些岩石、把布拉克努爾解決掉就好了。你們可壓不垮我們矮人。

### (sub) DIAL_Z30#637
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也這麼想。也許我們還會再見。

### (sub) DIAL_Z30#638
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [64023..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#639
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [64118..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Naddur_Ban_Dok

### (sub) DIAL_Z30#640
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#641
- speaker=0  style=6
- effects:
    - ?wOp12 a1=57 a2=0
    - ?wOp12 a1=29 a2=0
    - preload portraits 0xf,0x1,0x0,0x0
- branches:
    - [always] -> node 0 (no jump)
- text: 火花在走廊中竄射而過。  詹姆士將歐文猛地按在礦坑坑壁上，自己也險險躍身閃避，某樣東西正沿著石地滑掠而過。那團發光的火焰錐忽然撞上一道看不見的牆，瞬間消失無蹤。過了好幾個漫長的心跳，這位紳爵才緩緩從牆邊移開身子，正好與一個矮壯如樹樁的男人四目相對。

### (sub) DIAL_Z30#642
- speaker=15  style=0
- effects:
    - ?wOp12 a1=118 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們儘管說我沒種，或罵我是頭醉牛都成，可我這雙鎚子手，在這些山底下可沒人比得上快。布拉克努爾挖出來的爛攤子，可不是我一眨眼就能清乾淨的！要是你們非去艾爾凡達不可，那就過一個月左右再回來看看，說不定那時候我們已經打通了！

### (sub) DIAL_Z30#643
- speaker=0  style=0
- effects:
    - push return-address key 64974 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#644
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你撥空，納杜爾。希望你們能把這裡的事情處理好。

### (sub) DIAL_Z30#645
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會沒事的，等我們鑿穿這些岩石、把布拉克努爾解決掉就好了。你們可壓不垮我們矮人。

### (sub) DIAL_Z30#646
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也這麼想。也許我們還會再見。

### (sub) DIAL_Z30#647
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [65304..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#648
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [65398..0]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Naddur_Ban_Dok

### (sub) DIAL_Z30#649
- speaker=0  style=0
- branches:
    - [flag 0x1eb0 in [2218..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#650
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#651
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#652
- speaker=15  style=0
- effects:
    - ?wOp12 a1=118 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽見你們沿著通道走過來，一時還以為又是哪隻怪物，想來嚇嚇我這把老骨頭。我看我們這裡的人現在都還有點神經兮兮的。

### (sub) DIAL_Z30#653
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望我們沒把您嚇得太厲害。我們只是在找一條通往艾爾凡達的路。我記得曾聽說，那是在灰塔的另一頭……

### (sub) DIAL_Z30#654
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們可真是ó找對了路！這片礦坑一路從灰塔的一頭延伸到另一頭。我們這裡本來塌了，不過大概半小時前才剛打通。我這輩子頭一次好幾個月沒見著我兄弟麥卡努爾了！噢，不過也是有些慘痛的損失。洞穴裡出了場崩落，通往那裡的坑道被毀得很嚴重。我看我們大概是再也見不著那地方了。那些布拉克努爾搞出來的，真是一團糟……

### (sub) DIAL_Z30#655
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們可以通到艾爾凡達了嗎？

### (sub) DIAL_Z30#656
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯！不過我勸你們最好走主要坑道，有些彎彎繞繞的地方，人類走了容易受不了。照規矩我們是不會讓你們自己走的，免得迷路，不過現在也只清出了主要通道。你們這樣走應該夠安全了。

### (sub) DIAL_Z30#657
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在我們離開之前，能向您請教幾個問題嗎？

### (sub) DIAL_Z30#658
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒理由不行啊。你想知道什麼，小子？

### (sub) DIAL_Z30#659
- speaker=0  style=0
- effects:
    - push return-address key 67056 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#660
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們也該上路了。戈拉斯跟我都還有不少事要處理。

### (sub) DIAL_Z30#661
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰不是呢！不過我可有好一陣子沒這麼開心過了。你們要是想繼續往艾爾凡達走，就一路朝西走，直到看見天光為止。

### (sub) DIAL_Z30#662
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 用你們的母語，「謝謝」該怎麼說？

### (sub) DIAL_Z30#663
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看你們的舌頭大概轉不過來，不然我早就告訴你們了，不過還是謝謝你們的心意。祝你們一路順風。

### (sub) DIAL_Z30#664
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就謝謝了。戈拉斯，不如你來帶路吧？

### (sub) DIAL_Z30#665
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [2123..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#666
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [2218..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Naddur_Ban_Dok

### (sub) DIAL_Z30#667
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#668
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#669
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒想到這麼快又見到你們了。是在麥克莫丹卡達爾裡迷路了嗎？

### (sub) DIAL_Z30#670
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是，我只是突然想到，或許您能替我解答幾個問題。

### (sub) DIAL_Z30#671
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不敢保證能告訴你們想知道的事，不過我會盡力而為。問吧。

### (sub) DIAL_Z30#672
- speaker=0  style=0
- effects:
    - push return-address key 68362 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#673
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次謝謝您的耐心。您幫了我們大忙。

### (sub) DIAL_Z30#674
- speaker=15  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為了你們好，希望如此。要是你們不介意，我看我該回去做事了。還有很多事要忙呢。

### (sub) DIAL_Z30#675
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。再次謝謝您的耐心。戈拉斯跟我自己也還有些事要辦……

### (sub) DIAL_Z30#676
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [3172..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#677
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [3266..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Naddur_Ban_Dok

### (sub) DIAL_Z30#678
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#679
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#680
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們是什麼人？來盜賊大道做什麼？

### (sub) DIAL_Z30#681
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我乃紳爵洛克利爾，在親王的下水道裡，我想做什麼就做什麼！要是你有你看起來一半聰明，我勸你還是讓開的好。

### (sub) DIAL_Z30#682
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這把刀可不是擺著好看的。你再往前一步，我就宰了你，我說到做到！

### (sub) DIAL_Z30#683
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這位年輕的朋友，你唯一能做的事，就是死在我劍下，死得挺不值。我以前可是跟神偷吉米對練過的，我的劍比他還快。你還想跟我過招嗎？

### (sub) DIAL_Z30#684
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 神偷吉米？他可是個ó傳說ð人物，大人。接下來你該不會要說你跟凱許的拉凱莎女皇睡過吧……不過我勸您還是客氣點好，因為我還有五個弟兄在不遠處候著，確保我不會有事，懂吧。您該不會是奉詹姆士紳爵之命來的吧？

### (sub) DIAL_Z30#685
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士紳爵？那你不是……嗯，或許我們是奉他之命來的。

### (sub) DIAL_Z30#686
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，那就打開天窗說亮話。要是他沒派你們來，ó你們就得去跟正直人交代，不干我的事，我可就撒手不管了。你們在這下面走路小心點，這兒最近不太平。告辭。

### (sub) DIAL_Z30#687
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等等……我們對這下面的路不熟。

### (sub) DIAL_Z30#688
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看起來像哪家的跑腿小廝嗎？我自己也是有正事要辦的……

### (sub) DIAL_Z30#689
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就回答幾個問題？

### (sub) DIAL_Z30#690
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧，只要你們別問些會讓我在守夜頭領那邊惹麻煩的事就成。你們想知道什麼？

### (sub) DIAL_Z30#691
- speaker=0  style=0
- effects:
    - push return-address key 70599 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#692
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這就得走了，我跟正直人還有事要辦。你們哪天再來，多說點神偷吉米的傳說故事給我聽聽。

### (sub) DIAL_Z30#693
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們會的。謝謝你的幫忙。

### (sub) DIAL_Z30#694
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [5309..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#695
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [5390..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C1_Limm

### (sub) DIAL_Z30#696
- speaker=0  style=0
- branches:
    - [flag 0x1eb1 in [7183..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#697
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#698
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#699
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別再往前了，你們三個。這裡是盜賊大道，你們哪個看起來都不像嘲弄幫的人。滾開。

### (sub) DIAL_Z30#700
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那什麼能攔著我把克朗多的長槍騎兵團帶下來，踹爛你們的門？

### (sub) DIAL_Z30#701
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 攔著歷代克朗多親王的東西也一樣攔著你。我們早一週零一天就會得到消息，中間還有空睡個午覺。等他們在這下面咚咚踏踏的時候，我們早就把他們的房子跟軍營給洗劫一空，靠這趟遠征發了筆橫財。

### (sub) DIAL_Z30#702
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 離開十四年了，嘲弄幫還是老樣子……我要你去給正直人捎個信，說詹姆士紳爵需要進出下水道，只要幾個鐘頭就好。

### (sub) DIAL_Z30#703
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士紳爵？噢，那可就不一樣了。這兩個月來，『嘲弄幫棲身處』上下都在談論您！守夜頭領已經明確交代，我們得盡一切可能協助您。

### (sub) DIAL_Z30#704
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼？

### (sub) DIAL_Z30#705
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可不清楚。我只是照守夜頭領的話去做。他還說，我們得回答您可能提出的任何問題。

### (sub) DIAL_Z30#706
- speaker=0  style=0
- effects:
    - push return-address key 72333 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#707
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還得去通道另一頭查點事情，先走一步了。你們可別在我地盤上順手牽羊。

### (sub) DIAL_Z30#708
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 放心，你的地盤在我們手上很安全。替我向正直人問聲好。

### (sub) DIAL_Z30#709
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7098..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#710
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7183..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Limm

### (sub) DIAL_Z30#711
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#712
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#713
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您好，紳爵。這條大道暫時是您的了。不過還是留意一下爬行者的手下。

### (sub) DIAL_Z30#714
- speaker=0  style=0
- effects:
    - push return-address key 73094 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#715
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該繼續上路了，林姆。再次謝謝你的幫忙。

### (sub) DIAL_Z30#716
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你要是真心感激，就該告訴我怎麼溜進亞魯莎那座王宮，好讓我撈點閃亮的小東西……

### (sub) DIAL_Z30#717
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我就當沒聽見，咱們就算ó扯平了。保重，林姆。

### (sub) DIAL_Z30#718
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7930..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#719
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [8014..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Limm

### (sub) DIAL_Z30#720
- speaker=0  style=0
- branches:
    - [flag 0x1eb1 in [9661..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#721
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#722
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#723
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們得去別處辦事了，夥計們。今晚，還有接下來好一陣子，不管給多少錢我都不能放一隻蚊子過去。盜賊大道封了。

### (sub) DIAL_Z30#724
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼，連買路錢都不收？看來這下面出了什麼相當嚴重的事……

### (sub) DIAL_Z30#725
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你要是嘲弄幫的朋友，就該明白我說這是『家務事』是什麼意思。嘲弄幫棲身處在開會呢。

### (sub) DIAL_Z30#726
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正直人的事？

### (sub) DIAL_Z30#727
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這話不是從我嘴裡說出去的。我只是個守夜的，還是個蠢守夜的。

### (sub) DIAL_Z30#728
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我明白了。你覺得是誰幹的？

### (sub) DIAL_Z30#729
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟幾個月前對你們下手的是同一夥人。不管是誰幹的，一定有內鬼幫忙。正直人是被下毒害死的。在棲身處那邊，他們都管他叫『爬行者』——到現在也還搞不清楚他到底想圖什麼。我們絕不會向他俯首稱臣，不管他過去對我們做過什麼好事。與其讓他當家作主，我們寧可看他死。

### (sub) DIAL_Z30#730
- speaker=0  style=0
- effects:
    - push return-address key 74839 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#731
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該繼續上路了，林姆。謝謝你的幫忙。

### (sub) DIAL_Z30#732
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也算不上什麼幫忙，不過不客氣。告辭了，大人們。

### (sub) DIAL_Z30#733
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你也是。小心別讓爬行者的手下也把你給做了。

### (sub) DIAL_Z30#734
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9576..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#735
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9661..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Limm

### (sub) DIAL_Z30#736
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#737
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#738
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在我接到消息說這道門可以重新開放之前，您沒法進下水道。抱歉了，紳爵。還請您先離開吧。

### (sub) DIAL_Z30#739
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 眼下我對下水道沒什麼興趣，倒是對您那對ó耳朵之間的東西比較感興趣。方便的話，我想問您幾個問題……，掏掏您的腦子。

### (sub) DIAL_Z30#740
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那倒也無妨，只要您不是想耍花招矇混過去就行。您想知道什麼？

### (sub) DIAL_Z30#741
- speaker=0  style=0
- effects:
    - push return-address key 75874 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#742
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該繼續上路了，林姆。再次謝謝你的幫忙。

### (sub) DIAL_Z30#743
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也算不上什麼幫忙，不過不客氣。告辭了，大人們。

### (sub) DIAL_Z30#744
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你也是。小心別讓爬行者的手下也把你給做了。

### (sub) DIAL_Z30#745
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [10622..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#746
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [10706..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Limm

### (sub) DIAL_Z30#747
- speaker=0  style=0
- branches:
    - [flag 0x1eb1 in [13338..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#748
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1034 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#749
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#750
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們闖進嘲弄幫的地盤了。我勸你們趁我還沒被逼得對你們下重手之前，趕緊掉頭離開。

### (sub) DIAL_Z30#751
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託，只要你回答我們幾個問題，我們馬上就走。

### (sub) DIAL_Z30#752
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 問題？！我現在唯一在乎的，就是收拾這場暴風雨留下的爛攤子，讓我們大家重新站穩腳跟。平常我們對偶爾來場暴風雨倒也不介意——順便把臭味沖乾淨，您懂我的意思吧。可這場暴風雨，可真是把我們害慘了。海水灌了進來，沖走了我們二十來個弟兄，毀了我們的總部，還搞砸了我們原本要處理一個小小地頭問題的計畫。我們差一點就抓到他了……

### (sub) DIAL_Z30#753
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他？你們差點抓到誰？

### (sub) DIAL_Z30#754
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 爬行者，就是他，不過這跟你們也沒什麼關係。他一除掉正直人這個絆腳石，我猜他就打算回來領取他的獎賞了。我們可另有打算。我們給他布下了一個現成的小陷阱，誘餌他絕對拒絕不了。本來能讓他夾著尾巴逃回落日群島，或是他打哪個地獄爬出來的地方去的。可惜天公不作美，搞砸了我們的小計畫。

### (sub) DIAL_Z30#755
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們嘲弄幫裡有法師嗎？

### (sub) DIAL_Z30#756
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有，至少沒人願意大方承認。我們寧可割了法師的喉嚨，也不會讓他混進來，不過說實話，這幾個月我們倒是巴不得有一個。爬行者的手下裡，有幾個是玩法術的。

### (sub) DIAL_Z30#757
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？他們還有留在這下面的嗎？

### (sub) DIAL_Z30#758
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰說得準？我們還在清點自己的死者，哪還顧得上他們有誰留在這下面。下水道有大片都塌了。甚至還有傳言說，海堤有一段崩塌時，打通了一道通往下水道更深層的新樓梯。

### (sub) DIAL_Z30#759
- speaker=0  style=0
- effects:
    - push return-address key 78392 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#760
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們該走了，歐文。

### (sub) DIAL_Z30#761
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你想幹嘛隨你，尖耳朵，只要趁還沒人把你剁成肉派之前滾出下水道就行。

### (sub) DIAL_Z30#762
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 相信我，我一點都不想留在這下面。要是這輩子再也不用見到克朗多的地下世界，我會很高興的。再見了，林姆，祝你好運。

### (sub) DIAL_Z30#763
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [13253..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#764
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [13338..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Limm

### (sub) DIAL_Z30#765
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#766
- speaker=0  style=6
- effects:
    - ?wOp12 a1=112 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通道裡有個身影在移動。  一個少年彷彿憑空冒出，擋在他們面前，不讓他們再往前走。

### (sub) DIAL_Z30#767
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽著，除非你們願意幫忙收拾這下面的爛攤子，不然我勸你們最好趕緊滾。我不是那種一言不合就殺陌生人的人，可我們嘲弄幫的弟兄們可沒幾個這麼隨和。懂我意思嗎？趁還沒被劈成兩半之前，自己閃人。

### (sub) DIAL_Z30#768
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們至少能問你幾個問題嗎？

### (sub) DIAL_Z30#769
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來你剛剛已經問了……你想知道什麼？

### (sub) DIAL_Z30#770
- speaker=0  style=0
- effects:
    - push return-address key 79553 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#771
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們現在打聽得也夠多了。

### (sub) DIAL_Z30#772
- speaker=16  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真奇怪你腦袋裡裝了這麼多東西居然沒炸開。肯定是個十足的天才……

### (sub) DIAL_Z30#773
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再ó見了，林姆。別偷些你扛不動的東西。

### (sub) DIAL_Z30#774
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [14327..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#775
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [14411..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Limm

### (sub) DIAL_Z30#776
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[3] (xor=0x45 mask=0x51 mode=1 chapters=-)] -> node 4278272000
    - [event_bitmap_hi[3] (xor=0xa9 mask=0x4b mode=1 chapters=-)] -> node 4278261768
    - [flag 0x1eb2 in [18590..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#777
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1011 a2=0
    - event_bitmap_hi[3] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#778
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#779
- speaker=17  style=0
- effects:
    - play sfx 100
- branches:
    - [always] -> node 0 (no jump)
- text: 今天有什麼能為你們效勞的？

### (sub) DIAL_Z30#780
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我真心覺得這是我去過最冷清的酒館了。大家都ñ跑哪去了？

### (sub) DIAL_Z30#781
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大家都不在鎮上。除了雷克、我自己，還有幾個從路上晃進來投宿的旅客之外，自從那場慶典之後，鎮上就再沒別的人影了。

### (sub) DIAL_Z30#782
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 所有人？為什麼？這裡發生了什麼事？

### (sub) DIAL_Z30#783
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 昨晚第八個鐘頭，一位披著斗篷的先生從那扇門走了進來，找了個位子坐下。他點了一塊牛肉、一條麵包跟一杯麥酒。我會記得這些，是因為我點的也是一樣的東西。他一吃完，就走到酒館老闆那兒，扔下五十枚金幣，轉身就從門口出去了。那些錢幣還沒在櫃檯上轉停，酒館裡剩下的人就全都衝出去追他了。老闆連門都沒鎖上。

### (sub) DIAL_Z30#784
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是什麼交易嗎？

### (sub) DIAL_Z30#785
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是。是什麼該死的地方習俗。看樣子我來的時候，正好碰上一場叫『陌生人慶典』的儀式。按傳統，鎮上的長老們會聚在酒館裡抽籤，抽到最長那支籤的人就成了『陌生人』。慶典的第一晚，『陌生人』會挨家挨戶，發給鎮民假的金幣——他們管那叫『尼普托』——然後鎮民就都跑去田裡睡覺。當然，我當時完全不知道發生了什麼事……

### (sub) DIAL_Z30#786
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們該一直待在田裡嗎？

### (sub) DIAL_Z30#787
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，不，不，不是。隔天早上，被選中的『陌生人』得繞著村子走三圈，同時把一段麻繩甩在頭頂上轉。完事之後，他會把繩子剪斷，放在路上，讓鎮民知道他們可以回來了。這樣一來，大家就知道基利安對這座小鎮心懷善意，不會讓他們的田地枯死。可要是繩子沒放，那就表示她不高興了，任何試圖回鎮上的居民都會被擊斃。

### (sub) DIAL_Z30#788
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 『陌生人』是被基利安殺死的嗎？

### (sub) DIAL_Z30#789
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，不是基利安殺的，而是一個叫『收帳人』的傢伙下的手，他不知道這座小鎮的傳統，只是來討他欠的債。不過對艾格利的鎮民來說，這無關緊要。他們仍然選擇把這件事當成基利安的示警，從此再也沒回來過，認定這地方遭了詛咒，除非詛咒解除，否則不會回去。他們搬去了坦紐爾、鷹谷，還有幾個搬去了馬拉克十字鎮。他們都相信自己做了對的事，還准我在這裡愛怎麼做就怎麼做。出於對他們的尊重，我決定沿用艾格利這個舊鎮名。

### (sub) DIAL_Z30#790
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我說不準。感覺要相信這一整套，人得挺蠢才行。

### (sub) DIAL_Z30#791
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？那你敢對著伊夏神的神殿吐口水嗎？

### (sub) DIAL_Z30#792
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不敢……不過……我想我明白你的意思了。

### (sub) DIAL_Z30#793
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 人人都有自己的信仰。這些村子裡許多人曾經是農夫，要他們就這麼背棄那位ñ自然女神，並不是件容易的事。他們需要她的祝福，才能展開新的生活。你在評斷什麼事愚昧無知之前，最好先記得這一點。好了——既然我現在的新差事是這間酒館的酒保，我想我有責任問問你們需要點什麼？我能替你們張羅點什麼嗎？

### (sub) DIAL_Z30#794
- speaker=0  style=0
- effects:
    - push return-address key 83723 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#795
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的款待，戴文。這對長途跋涉來說，是一段令人愉快的歇息。

### (sub) DIAL_Z30#796
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 下次你跟人提起艾格利的時候，記得這件事。是時候該散布些ñ新的謠言了。

### (sub) DIAL_Z30#797
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。再見了，戴文。

### (sub) DIAL_Z30#798
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18487..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#799
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [18590..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_HNM_Devon_Town_UNpopulated

### (sub) DIAL_Z30#800
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1011 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#801
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 戴文啐了一口。  顯然對自己發的這手單人ñ波基爾牌不太滿意，他用手指敲著大腿。

### (sub) DIAL_Z30#802
- speaker=17  style=0
- effects:
    - play sfx 100
- branches:
    - [always] -> node 0 (no jump)
- text: 又回來享受戴文的款待啦？進來吧。我正需要個人來陪我在ñ波基爾ð牌上作弊！有什麼我能為你們做的？

### (sub) DIAL_Z30#803
- speaker=0  style=0
- effects:
    - push return-address key 84503 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#804
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的款待，戴文。這對長途跋涉來說，是一段令人愉快的歇息。

### (sub) DIAL_Z30#805
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 下次你跟人提起艾格利的時候，記得這件事。是時候該散布些ñ新的謠言了。

### (sub) DIAL_Z30#806
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。再見了，戴文。

### (sub) DIAL_Z30#807
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [19267..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#808
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [19369..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_HM_Devon_Town_UNpopulated

### (sub) DIAL_Z30#809
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1014 a2=0
    - event_bitmap_hi[3] bitop
    - SET flag 0x1a65=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#810
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#811
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 快進來一起慶祝！歡迎光臨陌生人酒館！

### (sub) DIAL_Z30#812
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們在慶祝什麼？

### (sub) DIAL_Z30#813
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 慶祝在艾格利展開新生活！你們還記得吧，我跟你們說過，我抵達的那晚發生了件很奇怪的事？全鎮的人都消失了，無影無蹤。他們一直沒回來，我就決定留下來看看會發生什麼事，說不定還能接手這間酒館……結果沒想到他們居然全都決定回來了！

### (sub) DIAL_Z30#814
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是好消息吧？

### (sub) DIAL_Z30#815
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 整體來說，我想是的，雖然我還不知道自己經營這間酒館最後會是什麼結果。到現在還沒聽說原本的老闆怎麼樣了，不過既然我還在這裡，我想我也該做出老闆的樣子。想來點什麼？

### (sub) DIAL_Z30#816
- speaker=0  style=0
- effects:
    - push return-address key 85919 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#817
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恭喜艾格利重生，戴文。希望這裡一切順利，讓你能保住這間酒館。

### (sub) DIAL_Z30#818
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不管結果如何，這段日子都挺有意思的，所以不管怎樣我都不後悔。

### (sub) DIAL_Z30#819
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興聽你這麼說。再會了，酒保！

### (sub) DIAL_Z30#820
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [20702..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#821
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [20805..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_HNM_Devon_Town_Repopulated

### (sub) DIAL_Z30#822
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1014 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#823
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 戴文啐了一口。  顯然對自己發的這手單人ñ波基爾牌不太滿意，他抬眼瞥了瞥正擠在門口的新客人。看見@4，他勉強擠出一個笑容。

### (sub) DIAL_Z30#824
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在鎮民都回來了，我還真不確定自己是不是更喜歡這座小鎮。如今我連片刻靜下心思考的時間都難找。我想這就是追夢要付出的代價吧。想來點什麼？

### (sub) DIAL_Z30#825
- speaker=0  style=0
- effects:
    - push return-address key 86851 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#826
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們該走了。還有事要辦。要我們繼續替艾格利散播消息嗎？

### (sub) DIAL_Z30#827
- speaker=17  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想現在人已經夠多了。等我們終於達到一個介於鬼鎮跟城市之間的規模，我會很高興的。

### (sub) DIAL_Z30#828
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我相信你總有一天會如願的，戴文。再次感謝。

### (sub) DIAL_Z30#829
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [21695..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#830
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [21797..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_HM_Devon_Town_Repopulated

### (sub) DIAL_Z30#831
- speaker=0  style=0
- branches:
    - [flag 0x1eb3 in [24126..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#832
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1044 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#833
- speaker=18  style=0
- effects:
    - ?wOp12 a1=94 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們該知道，能激怒我的事情不多。可就我現在的感受而言，我這輩子從沒像此刻這麼憤怒過！

### (sub) DIAL_Z30#834
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我冒犯了您……

### (sub) DIAL_Z30#835
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 冒犯？！我的部下每天都得騎馬前往北疆邊界，阻擋迪勒肯那群畜生；他們每天都得把性命豁出去，只為了替王國多爭取一天的自由！這些山頭上到處散落著為此犧牲性命的士兵屍骨，而你竟把一個莫瑞德人帶進我的城堡，簡直是在他們的墳頭上吐口水！我真該把你吊死在外堡牆上！

### (sub) DIAL_Z30#836
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他來這裡是有正當理由的。亞魯莎親王認為這個莫瑞德人可能握有能帶我們找到夜鷹會的情報。

### (sub) DIAL_Z30#837
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 該死的亞魯莎親王！他根本不了解莫瑞德人是什麼樣子，他居然採信這個莫瑞德人的話，正好證明了這一點。洛克利爾紳爵跟我說過這個莫瑞德人的來歷，可我對他的德行，就跟對迪勒肯的實力一樣毫無信心！

### (sub) DIAL_Z30#838
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵，我身負職責在身，要是為了盡這份職責必須冒犯一位男爵，那也是不得已！既然我有正當理由來到此地，我需要一些答案，而我真心相信，彼此配合對我們雙方都有好處。要是您選擇阻撓我，那我相信亞魯莎親王一定會樂於向萊亞姆王稟報，說他的一位臣民自認可以凌駕於王室禮節之上！

### (sub) DIAL_Z30#839
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，身為邊境男爵，我只效忠萊亞姆王一人！亞魯莎親王要做什麼、不做什麼，是他自己的事。不過要是回答您的問題能讓我早點打發您走，那我聽候差遣！您想問什麼？

### (sub) DIAL_Z30#840
- speaker=0  style=0
- effects:
    - push return-address key 89168 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#841
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們已經打聽到來這裡想知道的事了。要是我知道下次再見面時，您能以更周到的禮節接待您的王室貴賓，我會很欣慰的。

### (sub) DIAL_Z30#842
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會列入考慮。請自行離開。

### (sub) DIAL_Z30#843
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。感謝您這番不同凡響的ñ盛情款待ð。我們這就告辭了……

### (sub) DIAL_Z30#844
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24034..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#845
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24126..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Baron_Gabot

### (sub) DIAL_Z30#846
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#847
- speaker=18  style=0
- effects:
    - ?wOp12 a1=94 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興再次見到你們。我為先前的態度感到抱歉。就在你們抵達之前，我剛得知有幾名部下陣亡，這件事一直讓我心煩意亂。請儘管告訴我，我能幫上什麼忙……

### (sub) DIAL_Z30#848
- speaker=0  style=0
- effects:
    - push return-address key 89988 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#849
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝您的幫助，男爵。您的回答至少幫我們釐清了一些事……

### (sub) DIAL_Z30#850
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興能幫上忙。恕我沒空送你們出去了。

### (sub) DIAL_Z30#851
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。我想我們自己找路出去應該不難……

### (sub) DIAL_Z30#852
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24795..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#853
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24886..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Baron_Gabot

### (sub) DIAL_Z30#854
- speaker=0  style=0
- branches:
    - [flag 0x1eb3 in [27067..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#855
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#856
- speaker=18  style=0
- effects:
    - ?wOp12 a1=94 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，我是想跟您談談，不過這個莫瑞德人在場讓我不太自在。能否請他先離開房間？

### (sub) DIAL_Z30#857
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會在前廳等候。

### (sub) DIAL_Z30#858
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不會花太久時間。  詹姆士，你對我們在北衛城進行的這些實驗計畫了解多少？

### (sub) DIAL_Z30#859
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不太清楚。我記得親王提過，您發現了一種類似那夫沙油的爆炸性粉末，不過除此之外我就不清楚了。

### (sub) DIAL_Z30#860
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們這種粉末確實類似那夫沙油，沒錯，不過威力要強上許多倍。只要一小撮還不夠塞滿我手掌的分量，就能把兩百磅重的鐵球如雨點般砸向敵軍。凡是被擊中的東西，都會被摧毀殆盡。可惜這武器得靠十個人花上半小時才能重新裝填，而且準確度目前也還不足以讓我在戰場上倚重它。再過個幾年，它或許會成為一種威力驚人的武器，但我們得先學會如何駕馭它才行。

### (sub) DIAL_Z30#861
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這將會是王國軍械庫的一大貢獻。

### (sub) DIAL_Z30#862
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯，而要是落到迪勒肯手裡，那貢獻可就更大了。有件事我還沒告訴你們：過去六個月裡，北衛城已經有三十頭豬被偷走了。

### (sub) DIAL_Z30#863
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 豬？……我不明白，失蹤的豬跟這件事有什麼關係？

### (sub) DIAL_Z30#864
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 豬尿是這種粉末配方裡的主要成分之一，而我們的豬又撐不過北疆的寒冬。要是城堡裡有人把配方洩漏給他們，他們很可能正試圖囤積存量，好進行自己的實驗。

### (sub) DIAL_Z30#865
- speaker=0  style=0
- effects:
    - push return-address key 92168 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#866
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝您的幫助，男爵。您的回答至少幫我們釐清了一些事……

### (sub) DIAL_Z30#867
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興能幫上忙。恕我沒空送你們出去了。

### (sub) DIAL_Z30#868
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。我想我們自己找路出去應該不難……

### (sub) DIAL_Z30#869
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [26975..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#870
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27067..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Baron_Gabot

### (sub) DIAL_Z30#871
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#872
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士，我能為你做什麼？

### (sub) DIAL_Z30#873
- speaker=0  style=0
- effects:
    - push return-address key 92711 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#874
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝您的幫助，男爵。您的回答至少幫我們釐清了一些事……

### (sub) DIAL_Z30#875
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興能幫上忙。恕我沒空送你們出去了。

### (sub) DIAL_Z30#876
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。我想我們自己找路出去應該不難……

### (sub) DIAL_Z30#877
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27518..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#878
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27609..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Baron_Gabot

### (sub) DIAL_Z30#879
- speaker=0  style=0
- branches:
    - [flag 0x1eb3 in [29434..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#880
- speaker=0  style=0
- effects:
    - SET flag 0x0083=1
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#881
- speaker=18  style=0
- effects:
    - ?wOp12 a1=94 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我們備戰的時間已經到頭了。我有兩名野戰隊長，陳屍在莫瑞德突擊部隊很可能會經過的地區。這下我只剩一個駐防連，還有兩個由生手指揮官帶領的野戰連。這對守城可沒什麼優勢。

### (sub) DIAL_Z30#882
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那馬丁公爵呢？我知道他當時正在這裡作客……

### (sub) DIAL_Z30#883
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他已經跟我的遊騎兵一起在外野戰了。我要你們兩個跟他配合，想辦法拖延或阻擋敵軍逼近的部隊。我方斥候估計，莫瑞德人已經出動了大約一千五百名兵力。

### (sub) DIAL_Z30#884
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您這裡有三百名士兵，還有一座城堡！要擋下那麼多敵軍，這已經綽綽有餘了……

### (sub) DIAL_Z30#885
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有夜鷹會的人滲透進我的部隊，等這一切結束時，我們損失的恐怕不只是幾名野戰隊長。眼下我們得假設，莫瑞德人知道些我們不知道的事。要是我們能擋下他們哪怕一半的兵力，我想就足以瓦解他們不管籌劃了什麼計畫。那麼，開始行動之前還有什麼問題嗎？

### (sub) DIAL_Z30#886
- speaker=0  style=0
- effects:
    - push return-address key 94369 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#887
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，考慮到這一切，我想我們應該能勝任這次的任務。

### (sub) DIAL_Z30#888
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很好。我很期待看到你跟洛克利爾大顯身手。派特魯斯，你留下來跟他們一起，盡你所能地協助他們。你對這一帶的地形比我手下任何人都熟，指路也講得比誰都清楚。

### (sub) DIAL_Z30#889
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們這就出發了。要是發現什麼重要的事，或是馬丁公爵派我們回來，我們會再向您回報……

### (sub) DIAL_Z30#890
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29342..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#891
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [29434..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C5_Baron_Gabot

### (sub) DIAL_Z30#892
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [event_bitmap_hi[20] (xor=0x21 mask=0x73 mode=1 chapters=-)] -> node 4278264352
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#893
- speaker=5  style=0
- effects:
    - event_bitmap_hi[20] bitop
- branches:
    - [always] -> node 0 (no jump)
- text: 我們按您的要求找到了坦尼。他說他會盡快趕回這裡。

### (sub) DIAL_Z30#894
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 感謝你們的努力，不過我眼下還有別的事要操心。我還是不喜歡這場戰事的走向。你們還需要我幫什麼忙嗎？

### (sub) DIAL_Z30#895
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士紳爵，我還是不喜歡這場戰事的走向。你需要什麼？

### (sub) DIAL_Z30#896
- speaker=0  style=0
- effects:
    - push return-address key 95451 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#897
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們大概該回去找馬丁公爵了。他大概正納悶我們跑哪去了。

### (sub) DIAL_Z30#898
- speaker=18  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就帶著我的祝福去吧，不過要留意自己身在何處、正在做什麼。我現在可承擔不起再損失一個人。

### (sub) DIAL_Z30#899
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們心領了。祝您健康，加博特男爵。

### (sub) DIAL_Z30#900
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [30270..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#901
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [30361..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C5_Baron_Gabot

### (sub) DIAL_Z30#902
- speaker=0  style=0
- branches:
    - [flag 0x1eb4 in [32100..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#903
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#904
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#905
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽著，你們這幾個小流氓……你們該不會是學生吧——我是說，修道院的學生？我可沒少被他們惹麻煩。

### (sub) DIAL_Z30#906
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，不是。我們只是路過的旅人。

### (sub) DIAL_Z30#907
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗯哼。這種話我聽多了，不過你們看起來還算老實。我們這裡有幾條規矩。守規矩，咱們保證能成為好朋友。壞規矩，我就把你們三個串起來烤了。

### (sub) DIAL_Z30#908
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們洗耳恭聽……

### (sub) DIAL_Z30#909
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 劍啦、匕首啦，這些傢伙都給我收好在鞘裡。除非情非得已，不然我這店裡可不興什麼殺生。第二，不准帶動物進來，尤其是袋狸、獾，還是什麼火蜥蜴之類的。牠們會掉進湯裡，還會惹毛我家的狗，晚餐時間我可不想聽見一陣狂吠亂叫。最後，不管在什麼情況下，你們都絕對、絕對不准在我這店裡用什麼ó恩 ó帕薩。

### (sub) DIAL_Z30#910
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 用什麼？ó恩 ó帕薩？

### (sub) DIAL_Z30#911
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然你們連那是什麼都不知道，那我也不用擔心了，是吧？那，有什麼我能為你們做的？

### (sub) DIAL_Z30#912
- speaker=0  style=0
- effects:
    - push return-address key 97260 (GoodBye target)
    - SET flag 0x1eb4=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#913
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#914
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#915
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#916
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [32008..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#917
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [32100..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Ivan_Skaald

### (sub) DIAL_Z30#918
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#919
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#920
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 兩位想來點什麼？有什麼我能為你們做的？

### (sub) DIAL_Z30#921
- speaker=0  style=0
- effects:
    - push return-address key 97920 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#922
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#923
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#924
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#925
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [32668..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#926
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [32759..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Ivan_Skaald

### (sub) DIAL_Z30#927
- speaker=0  style=0
- branches:
    - [flag 0x1eb4 in [34586..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#928
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#929
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#930
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望你們不是為了那場比賽來的。已經結束了！

### (sub) DIAL_Z30#931
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 比賽？什麼比賽？

### (sub) DIAL_Z30#932
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你人在王后街還問這種問題？當然是西洋棋賽啊。精彩極了。傑米．提勒正在衛冕頭銜，對手是修道院那個自以為是的黃毛小子，凱爾．費雪。傑米開局把后翼兵推到第四排。費雪則用阿巴爾棄兵局應戰——傲慢的臭小子——結果傑米居然用騎士順勢切入了那個棄兵局。我當時還以為他是衝著皇后去的……

### (sub) DIAL_Z30#933
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可是他犧牲了王翼城堡，吃掉了那個祭司……這步棋確實高明，可這樣不就讓他自己的皇后陷入險境了嗎？

### (sub) DIAL_Z30#934
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，您對這棋藝真有兩下子。

### (sub) DIAL_Z30#935
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 親王喜歡下棋，可我們並不總是有棋盤在手邊。一旦學會在腦子裡下棋，棋盤幾乎就變得多餘了。不過我得承認，開局階段比較吃力。要盯著的棋子比較多。

### (sub) DIAL_Z30#936
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不過看棋還是挺有意思的。這就是王后街存在的原因。也許我可以邊喝麥酒邊跟你們講完剩下的棋局，前提是兩位請客。今天想來點什麼？

### (sub) DIAL_Z30#937
- speaker=0  style=0
- effects:
    - push return-address key 99746 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#938
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#939
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#940
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#941
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34494..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#942
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34586..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Ivan_Skaald

### (sub) DIAL_Z30#943
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#944
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#945
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們想聽剩下的棋局，隨時捅捅我的肋骨提醒一聲。那場面真是振奮人心。那，有什麼我能給你們的？

### (sub) DIAL_Z30#946
- speaker=0  style=0
- effects:
    - set party-speaker = 5
    - push return-address key 100496 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#947
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#948
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#949
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#950
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [35244..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#951
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [35335..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Ivan_Skaald

### (sub) DIAL_Z30#952
- speaker=0  style=0
- branches:
    - [flag 0x1eb4 in [37283..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#953
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#954
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#955
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟我說說看。馬拉克十字鎮到底做了什麼孽，才會攤上伊夏神修道院？我們是對國王犯了什麼滔天大罪，才害他把一車不知天高地厚、煩人又自我中心的小屎蛋全都倒進我們鎮上？這回又怎麼了？

### (sub) DIAL_Z30#956
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜伊夏神修道院的學生又給你惹麻煩了。

### (sub) DIAL_Z30#957
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不。鄰居家的狗把你的秋海棠挖出來、還在你家門口撒尿，那才叫麻煩。不，修道院跟她那些寶貝學生給我的，是一個隱隱作痛的潰瘍，還有滿頭的白髮！

### (sub) DIAL_Z30#958
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真奇怪。我還以為學生應該是很不錯的顧客。

### (sub) DIAL_Z30#959
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，說到顧客，那倒是沒錯。我囤麥酒的速度都快趕不上他們灌到眼珠子發花的速度，可要我伺候他們那些高貴的屁股……那可就是另一回事了。我看不如把這群可憐的臭小子鎖進地窖，關到二十歲左右再放出來算了。

### (sub) DIAL_Z30#960
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定沒跟親王聊過天嗎？這話聽起來就像他會說的，說他那對雙胞胎似的。博里克跟厄蘭雖然是王室血脈的親王，可在亞魯莎眼裡，他們不過是兩個道地的皇家屁股痛。

### (sub) DIAL_Z30#961
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小孩都一個樣，不管血統高不高貴。今天想來點什麼？

### (sub) DIAL_Z30#962
- speaker=0  style=0
- effects:
    - push return-address key 102443 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#963
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#964
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#965
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#966
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [37191..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#967
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [37283..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Ivan_Skaald

### (sub) DIAL_Z30#968
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#969
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#970
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我得去後面洗幾個鍋子，不過應該還能抽個一兩分鐘聊聊。有什麼我能為你們做的？

### (sub) DIAL_Z30#971
- speaker=0  style=0
- effects:
    - push return-address key 103165 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#972
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#973
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#974
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#975
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [37913..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#976
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [38004..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Ivan_Skaald

### (sub) DIAL_Z30#977
- speaker=0  style=0
- branches:
    - [flag 0x1eb4 in [39627..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#978
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#979
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#980
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 今晚來的可是勇敢的客人啊！我還以為今晚只能陪著這幾個小毛頭顧顧爐火呢。

### (sub) DIAL_Z30#981
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 酒保，我們是怎麼配得上『勇敢』這個稱號的？

### (sub) DIAL_Z30#982
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們沒聽說那些傳聞嗎？外頭到處都是ó蛇ó人，在街上到處遊蕩，從母親懷裡偷走嬰兒，還害綿羊得了藍喘病。牠們把老保姆芬奇家的小羊羔都給偷走了，還把伊夏神修道院的排水溝給堵死了。

### (sub) DIAL_Z30#983
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您看起來倒是沒遇上什麼麻煩。

### (sub) DIAL_Z30#984
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，是沒有！我住在這兒，不用上路趕道。總不能因為哪個討人厭的學生決定去騷擾鎮民，我就關門大吉吧。

### (sub) DIAL_Z30#985
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 所以您覺得這一切都是惡作劇？

### (sub) DIAL_Z30#986
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 少來了，小子！長得像人的蛇到處跑來偷雞？這要不是玩笑，我就是格瓦利獸的叔叔了！當然是惡作劇！你們把我當成什麼了，一個老糊塗的傻老頭嗎？好了，我能為你們兩位做點什麼？

### (sub) DIAL_Z30#987
- speaker=0  style=0
- effects:
    - push return-address key 104787 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#988
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#989
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#990
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#991
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [39535..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#992
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [39627..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Ivan_Skaald

### (sub) DIAL_Z30#993
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#994
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#995
- speaker=19  style=0
- effects:
    - ?wOp12 a1=106 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 進來的路上宰了幾個蛇人嗎？要是有，把屍體堆在門口，我好剝皮做雙新靴子！想來點什麼？

### (sub) DIAL_Z30#996
- speaker=0  style=0
- effects:
    - push return-address key 105546 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#997
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你聊天。我想我們可能會在這兒待一會兒，跟幾個學生聊聊。

### (sub) DIAL_Z30#998
- speaker=19  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。我還有一堆碗盤要洗呢。

### (sub) DIAL_Z30#999
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次感謝。也許我們待會兒再聊……

### (sub) DIAL_Z30#1000
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40294..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1001
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [40385..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Ivan_Skaald

### (sub) DIAL_Z30#1002
- speaker=0  style=0
- branches:
    - [flag 0x1eb5 in [42400..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1003
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1042 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1004
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文，你好。

### (sub) DIAL_Z30#1005
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什……？！……我到底ñ在哪裡？

### (sub) DIAL_Z30#1006
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你的身體正安然無恙、靜止無聲地躺在馬拉克十字鎮附近的一處洞穴裡，而你的心靈卻已神遊他方……ñ來到這裡ð……  你的到來，我早已預料到了。能招待提伯恩的歐文．貝勒佛特這位貴賓，我深感榮幸。

### (sub) DIAL_Z30#1007
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我？

### (sub) DIAL_Z30#1008
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 待這段旅程走到盡頭，你將不再是如今的你，也再無法沿著來時的路走回去。前方等著你的日子將充滿艱辛，你也將多次認為自己遠不如實際那般重要。在未來的日子裡，你或許會站在萊薩與麥薩之間的關鍵交會點上，倘若那一刻真的到來，你該知道這件事：萬物終有一死之時。

### (sub) DIAL_Z30#1009
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是什麼意思？萊薩跟麥薩是誰？

### (sub) DIAL_Z30#1010
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 憑你目前對這個世界的理解，我無法再多做解釋。等你年歲漸長、智慧漸增，你會再度前來見我，屆時一項偉大的命運將降臨在你身上。到了那遙遠的一天，你將準備好接受完整的真相。在那之前，你可以就其他事情向我請教。

### (sub) DIAL_Z30#1011
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 傳說中龍能知曉自己的命運，但我倒沒聽說過牠們也能知曉他人的命運。

### (sub) DIAL_Z30#1012
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我並非真龍，儘管我披著龍皮。我是阿爾一族的神諭者，是我族最後的倖存者。我極為古老，比矮人、比精靈都要古老，比龍族還古老，甚至比曾是牠們主人的瓦爾赫魯都還要古老。在我誕生之時猛烈燃燒的星辰，如今早已冷卻、熄滅。這一切我都親眼見過，而我所能窺見的，還遠遠不止於此，更能看見那些可能發生的事。

### (sub) DIAL_Z30#1013
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你能看見未來？

### (sub) DIAL_Z30#1014
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我能窺見一些可能發生的事。這是賦予我族所有成員的天賦。

### (sub) DIAL_Z30#1015
- speaker=0  style=0
- effects:
    - push return-address key 107813 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1016
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [42306..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1017
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [42400..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_CX_Oracle_of_Aal

### (sub) DIAL_Z30#1018
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1042 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1019
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 神諭者正等候著你。你想提出什麼問題？

### (sub) DIAL_Z30#1020
- speaker=0  style=0
- effects:
    - push return-address key 108077 (GoodBye target)
    - set party-speaker = 3
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1021
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [42570..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1022
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [42663..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_CX_Oracle_of_Aal

### (sub) DIAL_Z30#1023
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1024
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我呼喚了你，卻無法觸及你的心靈。那名法師手持一件護符，能使這副身軀變得虛弱無力，而他正在解除環繞生命石的最後幾道防禦。

### (sub) DIAL_Z30#1025
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬卡拉行事魯莽，不過我不認為他會對你造成永久性的損害。他一定是挖出了某件瓦爾赫魯的遺物，很可能是「群龍之主」里隆-巴克托斯的作品。他雖然無法掌控你的心智，卻仍能號令你這副龍軀的血肉之驅。

### (sub) DIAL_Z30#1026
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我無法預知自己的未來，這讓我們對這種可能性視而不見。

### (sub) DIAL_Z30#1027
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這件事我們得留到之後再處理。  戈拉斯，我要你留在這裡，守護神諭者。

### (sub) DIAL_Z30#1028
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你。需要有人保護，這讓我感到痛心。

### (sub) DIAL_Z30#1029
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帕格，等你面對那個圖蘭尼法師時，或許會需要我的力量……

### (sub) DIAL_Z30#1030
- speaker=20  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你ñ在生命石密室裡會遇上一番苦戰。

### (sub) DIAL_Z30#1031
- speaker=4  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，戈拉斯。你為這趟任務已經付出得夠多了，也看見了原本除了我以外不該有人看見的事物。你連馬卡拉的皮都還沒抓破，他就會先把你燒成灰燼。有法師在場，他會更有所顧忌，也比較不會輕舉妄動。眼下，你的職責是守護神諭者。

### (sub) DIAL_Z30#1032
- speaker=0  style=6
- effects:
    - SET PARTY size=2 members=[3,2,0]
    - load teleport table 38
    - SET flag 0x7541=2
    - END conversation, result=65532
- branches:
    - [always] -> node 0 (no jump)
- text: 帕格催促著歐文穿過一道拱門。  通道陡然向下傾斜，粗糙的泥土地面上散落著滑溜的陶瓷碎片，每踩一步都會發出碎裂聲。有些地方，少年瞥見了古老的壁畫，畫中是一支貌似莫瑞德人的種族，那些畫像的眼睛裡充滿了難解的恨意，而引發那份恨意的緣由，早在數百萬年前就已消逝。  沿著一道緩緩的彎道，他們終於來到一堵看似石牆的地方，但帕格很快低聲唸了幾個字，那道門便化為虛無、消失不見。門後是一間廣闊的密室，馬卡拉正在那裡等著他們……

### (sub) DIAL_Z30#1033
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [44729..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1034
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [44819..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C9_Oracle_of_Aal

### (sub) DIAL_Z30#1035
- speaker=0  style=0
- branches:
    - [flag 0x1eb6 in [47129..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1036
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1037
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1038
- speaker=21  style=0
- effects:
    - ?wOp12 a1=102 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我一看見洛克利爾紳爵跟加博特男爵鬼鬼祟祟地到處走動，就知道你不會離得太遠。我那親王哥哥亞魯莎還好嗎？

### (sub) DIAL_Z30#1039
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我上次見到他時他還好。他帶著一小支部隊駐紮在幽暗林外，正等著我的信使送信過去。話說回來，你怎麼跑到離克萊迪這麼遠的地方來了？是布莉安娜叫你來獵兔子給公爵府燉湯的嗎？

### (sub) DIAL_Z30#1040
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是，不過我們四個很快就要去獵更大的獵物了。要是洛克利爾跟我說的沒錯，北疆這場小小的風波看來很快就要變成整個王國的難題了。有你們兩個在這裡幫忙，我很高興。

### (sub) DIAL_Z30#1041
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 萊亞姆王會加入這場戰事嗎？

### (sub) DIAL_Z30#1042
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕不會。這場交戰的規模還不足以驚動國王，況且他光是應付凱許帝國那邊，手頭已經夠忙的了。似乎是我們王國的一艘船，誤把她們皇帝麾下的一艘御用護衛艦當成海盜船，連人帶船一起擊沉了。哈茲拉-可汗大人自然是氣得暴跳如雷。北衛城這場仗，我們得靠自己打了。

### (sub) DIAL_Z30#1043
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾跟我能做些什麼？

### (sub) DIAL_Z30#1044
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我已經把加博特男爵手下大部分的遊騎兵都派去查探敵軍動向了，所以我需要你們三個幫我處理各項任務。希望你們三個有心情到處跑跑腿。

### (sub) DIAL_Z30#1045
- speaker=0  style=0
- effects:
    - push return-address key 112102 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1046
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，這至少解答了一些疑問。我們最好回去把這場戰事的部署安排好。您眼下還需要什麼嗎？

### (sub) DIAL_Z30#1047
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只希望你們三個ó小心行事。我們可承擔不起再損失人手了。

### (sub) DIAL_Z30#1048
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們能遵守這道命令。公爵，您也要遠離危險。要是您不知怎麼被哪個哥布林弓箭手一箭射中，亞魯莎絕不會原諒我的！再會！

### (sub) DIAL_Z30#1049
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [47037..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1050
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [47129..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C5_Duke_Martin

### (sub) DIAL_Z30#1051
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1052
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1053
- speaker=21  style=0
- effects:
    - ?wOp12 a1=102 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 情況一點也不樂觀。我已經開始收到我方斥候的回報，從他們的說法聽來，這場圍城戰不會輕鬆……那，你們是為什麼事來找我的？

### (sub) DIAL_Z30#1054
- speaker=0  style=0
- effects:
    - push return-address key 113194 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1055
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，這至少解答了一些疑問。我們最好回去把這場戰事的部署安排好。您眼下還需要什麼嗎？

### (sub) DIAL_Z30#1056
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只希望你們三個ó小心行事。我們可承擔不起再損失人手了。

### (sub) DIAL_Z30#1057
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們能遵守這道命令。公爵，您也要遠離危險。要是您不知怎麼被哪個哥布林弓箭手一箭射中，亞魯莎絕不會原諒我的！再會！

### (sub) DIAL_Z30#1058
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [48129..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1059
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [48220..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C5_Duke_Martin

### (sub) DIAL_Z30#1060
- speaker=0  style=0
- branches:
    - [flag 0x1eb6 in [50095..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1061
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1062
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1063
- speaker=21  style=0
- effects:
    - ?wOp12 a1=102 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士！洛克利爾！你們怎麼會在這裡？

### (sub) DIAL_Z30#1064
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞魯莎親王跟我們說，有個圖蘭尼法師把一台裂界機交給了莫瑞德人，供他們在這場戰事中使用。我們是來這裡找出並摧毀它的，趁迪勒肯還沒能徹底運用它之前。您怎麼會在這裡？我們在城堡裡完全沒見到您。

### (sub) DIAL_Z30#1065
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當『南箭連』有一部分兵力開始從北衛城撤退時，我決定跟蹤他們，確保他們沒在搞什麼鬼。你們大概也猜到了，他們把那台該死的機器架設在北邊幾哩外，不過他們發現了我，還把我當成一個掉隊偷懶的人類傭兵……

### (sub) DIAL_Z30#1066
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……於是您就將計就計，穿過了裂界門，結果就到了這裡。您怎麼知道自己不會落到薩薩戈斯去？

### (sub) DIAL_Z30#1067
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道，可我當時被莫瑞德人團團圍住。我猜想，不管那扇門通向哪裡，我最大的生機都在門的另一頭。等我們從這裡出來以後，我就跟那名隊長說我得回歸自己的部隊，然後便脫身離開了。路上有幾次差點露餡，不過我最終還是成功逃了出來。

### (sub) DIAL_Z30#1068
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您當時為什麼不試著摧毀它？

### (sub) DIAL_Z30#1069
- speaker=21  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我考慮過，可那台裝置當時被莫瑞德人團團圍住，所以我決定設法找些人手幫忙。你們三個是我這一週以來見到的第一批人類。

### (sub) DIAL_Z30#1070
- speaker=0  style=0
- effects:
    - push return-address key 115510 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1071
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50003..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1072
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50095..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C7_Duke_Martin

### (sub) DIAL_Z30#1073
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1074
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1075
- speaker=21  style=0
- effects:
    - play sfx 102
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興看到迪勒肯還沒把你們三個給生吞活剝了。我上次見到你們時，還真開始有點擔心了。

### (sub) DIAL_Z30#1076
- speaker=0  style=0
- effects:
    - push return-address key 116081 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1077
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50574..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1078
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50665..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C7_Duke_Martin

### (sub) DIAL_Z30#1079
- speaker=0  style=0
- branches:
    - [flag 0x1eb7 in [52331..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1080
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1081
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1082
- speaker=22  style=0
- effects:
    - ?wOp12 a1=97 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要不是你殺了那頭雙足飛龍……我很感激，但我懇求你離開這個地方，同族兄弟，把你帶來的邪惡也一併帶走。你不能奪走不願被你奪走的東西，也傷不了不願被你傷害的事物。你跟你的族人，理應歸屬於自己的同胞之中。

### (sub) DIAL_Z30#1083
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不與我的族人一同劫掠。放我通行吧，伊列德人。我是為了瞻仰『明月』的容顏而來的。

### (sub) DIAL_Z30#1084
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 古語……我想，那麼你的到來會在艾爾凡達受到歡迎。告訴我母親跟托馬斯統帥，我一切安好，我會繼續前往莫拉埃林，跟那裡的莫瑞德人會面。或許我們還能設法阻止他們的劫掠。

### (sub) DIAL_Z30#1085
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 『明月』是什麼？是在艾爾凡達嗎？

### (sub) DIAL_Z30#1086
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是ñ她ð，不是ñ它ð，年輕的人類朋友。你的同伴指的是我們的亞葛拉蘭娜王后。用你們的語言來說，大概就是『明月』的意思。

### (sub) DIAL_Z30#1087
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 通往艾爾凡達的路能通行嗎？

### (sub) DIAL_Z30#1088
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人發動的攻擊讓通行變得困難。艾爾凡達各處都燃著大火，織法者們忙得應接不暇。大部分道路都無法通行，不過就我最後得到的消息，西邊那條小路還是暢通的。

### (sub) DIAL_Z30#1089
- speaker=0  style=0
- effects:
    - push return-address key 117752 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1090
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52245..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1091
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52331..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Calin

### (sub) DIAL_Z30#1092
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1093
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1094
- speaker=22  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯今日給我們帶來了極大的傷痛，他多少得為此付出代價。希望你們今天的旅途，比我今天的遭遇要順利得多。

### (sub) DIAL_Z30#1095
- speaker=0  style=0
- effects:
    - push return-address key 118382 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1096
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52875..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1097
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52960..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Calin

### (sub) DIAL_Z30#1098
- speaker=0  style=0
- branches:
    - [flag 0x1eb8 in [54824..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1099
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1100
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1101
- speaker=23  style=0
- effects:
    - ?wOp12 a1=111 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還一度以為迪勒肯已經把你殺了。他知道你逃脫了，肯定會勃然大怒。

### (sub) DIAL_Z30#1102
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽你這語氣，對這個前景可是相當得意啊。莉艾蘭，妳這場戲究竟是為了什麼？妳心裡不會比我更相信迪勒肯的所作所為，可妳卻支持他的大業。妳統領著一個舉足輕重的部族，幾乎跟他一樣有權有勢……

### (sub) DIAL_Z30#1103
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 幾乎？你忘了幾個月前是誰一手策劃了你從薩薩戈斯逃脫嗎？你以為當初是誰把迪勒肯那群鼠輩引去雪原，好讓奧布卡一家人趁機逃到安全的地方？那都是我的手筆。要不是我出手相助，六賢者早就把你們從綠心林逃出來的部族給徹底剿滅了。

### (sub) DIAL_Z30#1104
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 難道是妳一手促成了……

### (sub) DIAL_Z30#1105
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，這次我跟你的逃脫毫無關係。不管你做了什麼，都是你自己的本事。你第一次逃脫符合我的目的，可你之後能不能繼續活下去，對我來說根本無關緊要。這既不會威脅、也不會推進我的大業。

### (sub) DIAL_Z30#1106
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那妳願意再幫我一次嗎？

### (sub) DIAL_Z30#1107
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯，我會把我的付出當成是對北疆未來的一項投資。眼下這對我沒什麼好處，可將來某天，你的幫助或許會派上用場。我會通知我的眼線，配合你的任何需求。老實說，我不認為你除了保住自己一條命之外還能成就什麼，不過就算只是如此，對我來說或許也已經是種收穫了。

### (sub) DIAL_Z30#1108
- speaker=0  style=0
- effects:
    - push return-address key 120243 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1109
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [54736..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1110
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [54824..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C4_Liallan

### (sub) DIAL_Z30#1111
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1036 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1112
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1113
- speaker=23  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你在這兒磨蹭什麼？你唯一的自由之路，就是穿過因克林德爾山口。你還需要什麼嗎？

### (sub) DIAL_Z30#1114
- speaker=0  style=0
- effects:
    - push return-address key 120814 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1115
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [55307..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1116
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [55394..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Liallan

### (sub) DIAL_Z30#1117
- speaker=0  style=0
- branches:
    - [flag 0x1eb9 in [57681..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1118
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1119
- speaker=0  style=6
- effects:
    - play sfx 128
- branches:
    - [always] -> node 0 (no jump)
- text: 有人在呼喚。  歐文認出了那年輕的聲音的抑揚頓挫，轉頭望向身後的道路。一名他曾在亞邦的一場宴會上見過的年輕扈從，正拖著腳步跟在他們後頭，肩上扛著一整袋卷軸。那名扈從友善地揮了揮手，歐文也照樣揮手回應。  「你這是在做什麼？！我們正想避人耳目呢！該死，」洛克利爾低聲咕噥道。「盡量表現得正常一點。你認識他，歐文，你來應付他。還有，記得戈拉斯的名字是……」  「索爾加斯，」歐文有點不耐煩地接了話。「我又不是小孩子。」  洛克利爾低聲說道。「這可有待商榷。」

### (sub) DIAL_Z30#1120
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒想到這麼快又見到你了。我還以為你這時候應該已經到拉姆特了呢。

### (sub) DIAL_Z30#1121
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要不是公爵夫人堅持要把她所有的女兒都介紹給我認識，我早就到了。我覺得艾蜜莉亞是最漂亮的一個，不過我看凱瑟琳好像挺喜歡你的……

### (sub) DIAL_Z30#1122
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 凱瑟琳對宴會上每個人都挺有好感的。她跟她母親一樣善變。要是能找到一個還沒被婚姻套牢的康多因家族成員，她大概會嫁給那個人。

### (sub) DIAL_Z30#1123
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這倒是真的。話說，我記得你說過你是提伯恩人。你怎麼會走這條路回家？這樣繞路是不是有點遠？

### (sub) DIAL_Z30#1124
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃，是沒錯，不過我得先來見我的……這位洛克利爾叔叔。還有我這位朋友是精靈，叫索爾加斯。他們覺得帶我一起去克朗……

### (sub) DIAL_Z30#1125
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……鷹谷……

### (sub) DIAL_Z30#1126
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……去鷹谷玩玩挺不錯的。我聽說這個季節那裡很漂亮。你在忙什麼？

### (sub) DIAL_Z30#1127
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實我是想來領一筆獎賞的。上個月我前往亞邦的路上，在這一帶發現了一個箱子，可我怎麼也撬不開那把鎖。我當時想大概是沒這個緣分，就作罷了。問題是，整場公爵夫人的宴會上，我腦子裡老是想著那個箱子，滿腦子都是它。我根本不在乎裡頭裝了什麼，但我非把那把鎖撬開不可。

### (sub) DIAL_Z30#1128
- speaker=0  style=0
- effects:
    - push return-address key 123093 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1129
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [57586..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1130
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [57681..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Squire_Phillip

### (sub) DIAL_Z30#1131
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1004 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1132
- speaker=0  style=6
- effects:
    - (on-exit) play music 1041
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文豎起一根手指抵在唇邊。  察覺到附近有人或有什麼東西，他做出了先前說好、代表得小心行事的手勢。他們繃緊神經，做好戰鬥準備，一個個像上緊的發條。  突然間，一道身影出現在他們面前的空地上。

### (sub) DIAL_Z30#1133
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 菲力普扈從！

### (sub) DIAL_Z30#1134
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文？……真是……呃，真意外……

### (sub) DIAL_Z30#1135
- speaker=0  style=0
- effects:
    - push return-address key 123675 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1136
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [58168..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1137
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [58262..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Squire_Phillip

### (sub) DIAL_Z30#1138
- speaker=0  style=0
- branches:
    - [flag 0x1eb9 in [59567..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1139
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1140
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 這道裂隙已經有人在使用了。  菲力普扈從站在一叢灌木旁，一邊繫緊褲子的束帶，一邊漲紅著臉狠狠瞪了他們一眼。他斷定自己的尊嚴還沒有徹底無可挽回，便一邊禮貌地把襯衫下擺塞好，一邊對歐文開口說話。

### (sub) DIAL_Z30#1141
- speaker=24  style=0
- effects:
    - ?wOp12 a1=128 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 倒不是我不高興見到你，歐文，只是你出現的時機還真有點微妙。

### (sub) DIAL_Z30#1142
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是抱歉。我們從背後認不出是你，看你鑽進這個小洞裡，我們就起了疑心。這一帶的路上，我們遇過幾次強盜的麻煩。

### (sub) DIAL_Z30#1143
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我自己也差點撞上。幸好他們沒太注意我。要是我最後淪落到被綁票勒贖，我看父親不會太高興的……

### (sub) DIAL_Z30#1144
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你後來找到你在找的那個箱子了嗎？

### (sub) DIAL_Z30#1145
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有點令人失望。我一打開蓋子，就發現裡頭空空如也。我早該料到會有人搶先我一步。大概是被我們那些強盜朋友給洗劫一空了吧。

### (sub) DIAL_Z30#1146
- speaker=0  style=0
- effects:
    - push return-address key 124979 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1147
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [59472..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1148
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [59567..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Squire_Phillip

### (sub) DIAL_Z30#1149
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1150
- speaker=0  style=6
- effects:
    - play sfx 128
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1151
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 又見面了。你在想什麼？

### (sub) DIAL_Z30#1152
- speaker=0  style=0
- effects:
    - push return-address key 125477 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1153
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [59970..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1154
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [60064..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Squire_Phillip

### (sub) DIAL_Z30#1155
- speaker=0  style=0
- branches:
    - [flag 0x1eb9 in [61845..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1156
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1157
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1158
- speaker=24  style=0
- effects:
    - ?wOp12 a1=128 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文，你確定沒在跟蹤我嗎？我們碰面的次數也未免太頻繁了。

### (sub) DIAL_Z30#1159
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是一年碰面不只一次就能算頻繁的話。我看亞邦那場婚禮宴會，把我們倆都變成遊牧民族了。

### (sub) DIAL_Z30#1160
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可受夠了。要是說旅行能增廣見聞，那我敢說我的腦袋現在大概已經有一輛乾草車那麼大了。我真希望能早點回家，好好在自己的床上躺一陣子。

### (sub) DIAL_Z30#1161
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你怎麼會在王國東部？我還以為你住在拉姆特。

### (sub) DIAL_Z30#1162
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 偶爾，要是我父親允許，我會在拉姆特過夜，不過我大部分時間似乎都在王國的道路上，為了家族生意四處奔波。依我估計，他插手的買賣，大概比全米德凱米亞的麵包師傅加起來還多！當商人的事情多如牛毛，能幫忙的兒子卻沒幾個。

### (sub) DIAL_Z30#1163
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他怎麼不乾脆雇個跑腿的替他辦事？

### (sub) DIAL_Z30#1164
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這建議提過，尤其是我們這些不幸生為他兒子的人強烈建議過，可他老愛引用一句關於婚姻的奎格諺語：能免費得到的東西，何必花錢買？不過我倒不是要把他說得多小氣——他只是對自己的錢非常務實而已。

### (sub) DIAL_Z30#1165
- speaker=0  style=0
- effects:
    - push return-address key 127257 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1166
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [61750..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1167
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [61845..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Squire_Phillip

### (sub) DIAL_Z30#1168
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1169
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1170
- speaker=24  style=0
- effects:
    - ?wOp12 a1=128 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文，要不要跟我來場賽跑？就憑我練出來的這雙腿，四分之一哩內我肯定能贏過你！

### (sub) DIAL_Z30#1171
- speaker=0  style=0
- effects:
    - push return-address key 127825 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1172
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [62318..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1173
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [62412..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Squire_Phillip

### (sub) DIAL_Z30#1174
- speaker=0  style=0
- branches:
    - [flag 0x1eb9 in [65162..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1175
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1176
- speaker=0  style=6
- effects:
    - play sfx 128
- branches:
    - [always] -> node 0 (no jump)
- text: 一個男孩從屋裡匆匆跑了出來。  他身穿扈從的服色，一邊拉近彼此的距離，一邊加快腳步，神情看得出他見到他們相當高興。他喘著粗氣，朝他們揮了揮手……

### (sub) DIAL_Z30#1177
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託，請先別走。紳爵們，換作平常，我沒有權力請求兩位相助，可我們眼下兵力實在吃緊。不管兩位是否曾向賽瑟儂那支祕密駐軍宣誓效忠，我們都需要每一分能用得上的人手來幫忙。

### (sub) DIAL_Z30#1178
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 賽瑟儂駐軍？我從沒聽亞魯莎提過賽瑟儂附近駐紮著什麼部隊，而且你年紀輕輕，也太嫩了些，擔不起資深職務……

### (sub) DIAL_Z30#1179
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您猜我幾歲？

### (sub) DIAL_Z30#1180
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 十八，也許十九歲。跟我們認識的一位來自提伯恩的扈從差不多年紀……

### (sub) DIAL_Z30#1181
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 貝勒佛特伯爵的兒子歐文還在學走路的時候，我跟我妻子已經有個三歲的兒子了。我今年三十七歲，在王國陸軍裡官拜上尉。我的指揮官注意到，即便身為一名資深軍官，我看起來卻依然十分年輕，便靈機一動，想到我很適合替那支祕密駐軍當信使。

### (sub) DIAL_Z30#1182
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的老天！是王國的間諜！

### (sub) DIAL_Z30#1183
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就算你說的關於自己的事都是真的，你這故事其他部分也不可能。要是真有一支祕密駐軍，亞魯莎應該會告訴我……

### (sub) DIAL_Z30#1184
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他有沒有跟您解釋過，為什麼賽瑟儂被完全禁止進入？您能想起還有哪一次，亞魯莎親王或萊亞姆王曾禁止人民造訪戰場遺址嗎？

### (sub) DIAL_Z30#1185
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有，不過我一直以為他是想把那裡當作那場戰役的紀念地保留下來。

### (sub) DIAL_Z30#1186
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一座連老兵都不能造訪的紀念地？紳爵，您這是在強詞奪理。就連駐軍成員本身，除非有武裝部隊逼近，否則也不准靠近賽瑟儂。他們奉命殲滅任何來犯之敵。現在我得想辦法把莫瑞德人正在逼近的消息傳給他們。您對這件事有什麼想法嗎？

### (sub) DIAL_Z30#1187
- speaker=0  style=0
- effects:
    - push return-address key 130223 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1188
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們得回去繼續我們的任務了。你在這裡撐得住嗎？

### (sub) DIAL_Z30#1189
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 除非又有一群哥布林過來，不然我應該沒問題。我得留在這裡看守補給，不過要是兩位需要回來，隨時歡迎。

### (sub) DIAL_Z30#1190
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 感激不盡。再會了，ó扈從……

### (sub) DIAL_Z30#1191
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [65067..1]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1192
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [65162..1]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C7_Squire_Phillip

### (sub) DIAL_Z30#1193
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1194
- speaker=0  style=6
- effects:
    - ?wOp12 a1=128 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 菲力普朝他們打了招呼。  他一臉憂心忡忡的神情，從那間改建成補給屋的房子裡走出來迎接他們……

### (sub) DIAL_Z30#1195
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我覺得莫瑞德人可能已經察覺我在監視他們了。我看見一小隊他們的人在這附近偵查，不過不知為何，他們並沒有靠近這棟屋子。不過這不代表他們不會回來。你們需要什麼？

### (sub) DIAL_Z30#1196
- speaker=0  style=0
- effects:
    - push return-address key 131166 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1197
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 外頭還有那台該死的機器，我看迪勒肯是不會ó親自把它毀掉的，所以我想我們該回去處理它了。

### (sub) DIAL_Z30#1198
- speaker=24  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就祝你們好運了。我可不羨慕你們得直接走進他們的據點。

### (sub) DIAL_Z30#1199
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我自己也說不上有多興奮，不過該做的事還是得做。菲力普，後會有期……

### (sub) DIAL_Z30#1200
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [515..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1201
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [609..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C7_Squire_Phillip

### (sub) DIAL_Z30#1202
- speaker=0  style=0
- branches:
    - [flag 0x1e84 in [1951..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1203
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1204
- speaker=0  style=6
- effects:
    - ?wOp12 a1=16 a2=0
    - ?wOp12 a1=16 a2=0
    - (on-exit) play music 1002
- branches:
    - [always] -> node 0 (no jump)
- text: 蘇馬尼拍了兩下手。  室內原本歡樂的氣氛頓時沉靜下來，酒杯的碰撞聲與盤子的刮擦聲一時止息，這名酒館老闆穿梭在長凳之間，來到洛克利爾腳邊躬身行禮。他用一隻布滿老繭的拳頭先觸額、再觸胸，神情肅穆地開口說道。

### (sub) DIAL_Z30#1205
- speaker=25  style=0
- effects:
    - preload portraits 0x19,0x1,0x0,0x0
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎光臨藍輪客棧。願您喜歡我們的酒水，也享受與我們這些客人相伴的時光。若有任何需要我或敝店僕從效勞之處，只需吩咐蘇馬尼一聲即可。

### (sub) DIAL_Z30#1206
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊……也向貴店致上敬意……蘇馬尼……我沒理解錯的話，這裡是間酒館吧？

### (sub) DIAL_Z30#1207
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此。我們供應許多位米德凱米亞的酒水，也有幾款來自圖蘭努安尼帝國的飲品。也許您會有興趣來一杯巧恰。

### (sub) DIAL_Z30#1208
- speaker=0  style=0
- effects:
    - push return-address key 132627 (GoodBye target)
    - SET flag 0x1e84=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1209
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的招待，蘇馬尼。你這店開得真好。很有圖蘭尼風味。

### (sub) DIAL_Z30#1210
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 承蒙您光顧，是敝店的榮幸。

### (sub) DIAL_Z30#1211
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了。我保證，要是我還會再來拉姆特，一定會進來吃點東西。

### (sub) DIAL_Z30#1212
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [1864..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1213
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [1951..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Sumani

### (sub) DIAL_Z30#1214
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1215
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 蘇馬尼立刻回應。  他挪步靠近，壓低了聲音，以免打擾到酒館裡其他正在飲酒的客人。

### (sub) DIAL_Z30#1216
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大人有何吩咐？

### (sub) DIAL_Z30#1217
- speaker=0  style=0
- effects:
    - push return-address key 133277 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1218
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我們該去做點正事了，不能光坐在這兒享受氣氛。還有事要辦。

### (sub) DIAL_Z30#1219
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興您選擇光臨藍輪客棧。希望您能再度蒞臨。

### (sub) DIAL_Z30#1220
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們還會再來拉姆特，我想這絕對有可能。再見了，蘇馬尼。

### (sub) DIAL_Z30#1221
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [2579..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1222
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [2665..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Sumani

### (sub) DIAL_Z30#1223
- speaker=0  style=0
- branches:
    - [flag 0x1e84 in [3595..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1224
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1225
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 蘇馬尼立刻回應。  他挪步靠近詹姆士，壓低了聲音，以免打擾到酒館裡其他正在飲酒的客人。

### (sub) DIAL_Z30#1226
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大人有何吩咐？

### (sub) DIAL_Z30#1227
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 老闆，要是您抽得出時間，能耽誤您一分鐘嗎？

### (sub) DIAL_Z30#1228
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有需要，一整天的時間我都奉陪，尊貴的大人。有什麼能為您效勞的？

### (sub) DIAL_Z30#1229
- speaker=0  style=0
- effects:
    - push return-address key 134206 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1230
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我們該去做點正事了，不能光坐在這兒享受氣氛。還有事要辦。

### (sub) DIAL_Z30#1231
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興您選擇光臨藍輪客棧。希望您能再度蒞臨。

### (sub) DIAL_Z30#1232
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們還會再來拉姆特，我想這絕對有可能。再見了，蘇馬尼。

### (sub) DIAL_Z30#1233
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [3508..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1234
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [3595..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Sumani

### (sub) DIAL_Z30#1235
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1236
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1237
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無論藍輪客棧能為您效勞什麼，請儘管告訴蘇馬尼，不必客氣。

### (sub) DIAL_Z30#1238
- speaker=0  style=0
- effects:
    - push return-address key 134996 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1239
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的招待，蘇馬尼。你這店開得真好。

### (sub) DIAL_Z30#1240
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 承蒙您光顧，是敝店的榮幸。

### (sub) DIAL_Z30#1241
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了。我保證，要是我還會再來拉姆特，一定會進來吃點東西。

### (sub) DIAL_Z30#1242
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [4214..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1243
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [4300..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Sumani

### (sub) DIAL_Z30#1244
- speaker=0  style=0
- branches:
    - [flag 0x1e84 in [5269..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1245
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1246
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1247
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能招待兩位如此尊貴的客人，我們一向深感榮幸。藍輪客棧能為您效勞什麼？

### (sub) DIAL_Z30#1248
- speaker=0  style=0
- effects:
    - push return-address key 135745 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1249
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管我很想多留一會兒，可還有幾具屍體，我們得找出殺害他們的凶手。感謝你的款待。

### (sub) DIAL_Z30#1250
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望您能找到您要找的人。我可不希望看到『議會之局』在您這個世界也變得司空見慣。

### (sub) DIAL_Z30#1251
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不太清楚這個『議會之局』究竟是什麼，不過就我從其他圖蘭尼人那裡聽來的一點皮毛，我想我也不得不同意這一點。再次感謝。

### (sub) DIAL_Z30#1252
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [5182..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1253
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [5269..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Sumani

### (sub) DIAL_Z30#1254
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1255
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1256
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 藍輪客棧能招待如此尊貴的客人，深感榮幸。蘇馬尼能為您效勞什麼？

### (sub) DIAL_Z30#1257
- speaker=0  style=0
- effects:
    - push return-address key 136661 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1258
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該走了。還有人要找。

### (sub) DIAL_Z30#1259
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 願丘丘安神看顧您。

### (sub) DIAL_Z30#1260
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜那大概是位圖蘭尼神明。我不確定他們在米德凱米亞這裡有沒有什麼影響力，不過事到如今，能求到什麼好運我都不介意。謝謝你，蘇馬尼。

### (sub) DIAL_Z30#1261
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [5933..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1262
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [6019..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Sumani

### (sub) DIAL_Z30#1263
- speaker=0  style=0
- branches:
    - [flag 0x1e84 in [7248..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1264
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1265
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1266
- speaker=25  style=0
- effects:
    - ?wOp12 a1=129 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望您在藍輪客棧的這段時光，能是一段愉快的體驗。

### (sub) DIAL_Z30#1267
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您是圖蘭尼人吧？您以前是拉姆特這裡駐軍的一員嗎？我聽說卡蘇米伯爵麾下有不少士兵，以前都來自圖蘭努安尼。

### (sub) DIAL_Z30#1268
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此……

### (sub) DIAL_Z30#1269
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您怎麼會離開駐軍，跑來開酒館呢？留在駐軍裡，您想必會有更多晉升的機會。說不定哪天還能替自己掙得一塊土地，甚至一個頭銜。

### (sub) DIAL_Z30#1270
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 卡蘇米伯爵寬宏大量，將我革職，免得我的不名譽玷污了拉姆特駐軍的名聲。

### (sub) DIAL_Z30#1271
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您做了什麼？

### (sub) DIAL_Z30#1272
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我失陪，我想我聽見廚子在廚房裡喊我了。我稍後再來招呼您。

### (sub) DIAL_Z30#1273
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧……希望我沒有……我們回頭再聊。

### (sub) DIAL_Z30#1274
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7161..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1275
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7248..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Sumani

### (sub) DIAL_Z30#1276
- speaker=0  style=0
- effects:
    - SET flag 0x1fd1=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1277
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1278
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 能招待兩位如此尊貴的客人，我們一向深感榮幸。藍輪客棧能為您效勞什麼？

### (sub) DIAL_Z30#1279
- speaker=0  style=0
- effects:
    - push return-address key 138664 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1280
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的招待，蘇馬尼。你這店開得真好。

### (sub) DIAL_Z30#1281
- speaker=25  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 承蒙您光顧，是敝店的榮幸。

### (sub) DIAL_Z30#1282
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了。我保證，要是我還會再來拉姆特，一定會進來吃點東西。

### (sub) DIAL_Z30#1283
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7882..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1284
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [8019..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Sumani //////////////////////////////////////////////////

### (sub) DIAL_Z30#1285
- speaker=0  style=0
- branches:
    - [flag 0x1eba in [9485..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1286
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1287
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1288
- speaker=26  style=0
- effects:
    - ?wOp12 a1=115 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從這裡再往前，情況糟糕透頂。雙足飛龍從山那頭飛了過來，把這一帶燒得亂七八糟。要不是這幾週我們一直在撲滅火勢，我們早一個月就能打通了！眼下我也搞不清楚還有多少路能通行。你們那位親戚，先前來幫我們清理礦坑裡的爛攤子，一聽到火勢逼近艾爾凡達的消息，就立刻離開了。

### (sub) DIAL_Z30#1289
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那些雙足飛龍是打哪來的？

### (sub) DIAL_Z30#1290
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還能打哪來，小子？北疆啊！聽說是哪個新冒出來的莫瑞德混帳頭領在騷擾你們的族人。希望你們沒有哪個小崽子正身陷險境。

### (sub) DIAL_Z30#1291
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有……那莫瑞德人那邊呢？

### (sub) DIAL_Z30#1292
- speaker=26  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有幾個大膽從莫拉埃林越境過來的，已經被戳成串了，不過我知道卡林王子還在邊境上搜索其他人。眼下最要緊的，還是撲滅火勢，救援那些被困在火場後頭的人。

### (sub) DIAL_Z30#1293
- speaker=0  style=0
- effects:
    - push return-address key 140431 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1294
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9388..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1295
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9485..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_McCannur_Ban_Dok

### (sub) DIAL_Z30#1296
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1297
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1298
- speaker=26  style=0
- effects:
    - ?wOp12 a1=115 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 又多兩雙眼睛跟手，但願中間還帶著顆腦子！很高興看到你們倆沒被大火燒成焦炭！我們北邊的人可能需要點幫忙。剛剛沒過多久，有個精靈快跑信使經過這裡，說卡林王子跟他的護衛遭到雙足飛龍襲擊。目前那位年輕王子似乎還活著，可統帥麾下有三名部下當場喪命，統帥托馬斯本人也中了莫瑞德人的毒箭！

### (sub) DIAL_Z30#1299
- speaker=0  style=0
- effects:
    - push return-address key 141357 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1300
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [10314..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1301
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [10410..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_McCannur_Ban_Dok

### (sub) DIAL_Z30#1302
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1303
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1304
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾紳爵！見到您真高興。有意思的消息。有意思的消息。

### (sub) DIAL_Z30#1305
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 尼維克，你這老滑頭。又豎起耳朵到處打聽小道消息了，是吧？這回又是什麼？

### (sub) DIAL_Z30#1306
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我最近去了趟賽瑟儂附近，見了六趾客棧的妮雅。啊……這事我現在還真不方便說。你何不待會兒再回來找我？

### (sub) DIAL_Z30#1307
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的，好朋友！保重。

### (sub) DIAL_Z30#1308
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1309
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[8] (xor=0xeb mask=0x5c mode=21 chapters=8)] -> node 4278256128
    - [flag 0x1ece in [18892..2]] -> node 4294901761
    - [flag 0x1ed8 in [12091..2]] -> node 4294901761
    - [flag 0x1ebb in [12654..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1310
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1311
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士咧嘴一笑。  坐在一張長凳後方的，是一位老相識——尼維克，西境財政大臣。他是亞魯莎忠心耿耿的臣子，當年他跟洛克利爾紳爵倆人還在克朗多街頭闖蕩時，尼維克便與他們結為好友，並教了他們不少王國財政運作的門道。  他順著那長長的鼻梁向下打量，愉快地向他們打了招呼……

### (sub) DIAL_Z30#1312
- speaker=27  style=0
- effects:
    - ?wOp12 a1=121 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士紳爵！見到您真是太高興了！

### (sub) DIAL_Z30#1313
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 彼此彼此。尼維克，王國的帳本情況如何？你覺得我們今年的錢夠讓王國維持運轉嗎？

### (sub) DIAL_Z30#1314
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帳本倒是收支平衡，不過我敢說，我這口渴的赤字可就嚴重到災難等級了。雖然我每天經手成千上萬枚金幣，但眼下我自己能動用的，恐怕連一把都湊不齊。不知道您是否方便……

### (sub) DIAL_Z30#1315
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 尼維克瞇眼打量著他們。  他撐著桌子站起身，走過來向詹姆士打招呼……

### (sub) DIAL_Z30#1316
- speaker=27  style=0
- effects:
    - ?wOp12 a1=121 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 見到您真高興。是什麼風把您吹進彩虹鸚鵡酒館來的？

### (sub) DIAL_Z30#1317
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，看來你還站得挺直的嘛……

### (sub) DIAL_Z30#1318
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士，別仗著自己是亞魯莎面前的紅人就這麼放肆。我只是ó偶爾喝得多了點，而且我也好一陣子沒放縱過這種享受了。您是否願意請我喝一杯？

### (sub) DIAL_Z30#1319
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1320
- speaker=5  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [12826..2]] -> node 4294901761
    - [flag 0x0101 in [18588..2]] -> node 4294901761
- text: 歐文，你說呢？我們是該請這位尊貴的稅務官喝一杯，還是就讓他渴死算了？

### (sub) DIAL_Z30#1321
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x7531 in [13378..2]] -> node 4294901765
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1322
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1323
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唉，我們的錢已經花光了。眼下我能給您的，大概就只有一把口袋裡的棉絮了。除非這裡的老闆改用棉絮當貨幣，不然我看咱們倆都沒指望了。

### (sub) DIAL_Z30#1324
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哼！

### (sub) DIAL_Z30#1325
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許下次我們再請您喝一杯。祝您愉快。

### (sub) DIAL_Z30#1326
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [13265..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1327
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [13378..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_Cx_Nivek_YES_DRINK1_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#1328
- speaker=0  style=0
- effects:
    - SET flag 0x1ed8=1
    - TAKE gold -10
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1329
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 酒保，給這位稅務官來一杯！  喝吧，朋友，告訴我你知道些什麼。你對王國內外的大小事，一向消息靈通。

### (sub) DIAL_Z30#1330
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謠言？我的天啊，我可不是那種跟長舌婦廝混的人。不，大人，您該知道這一點的。當然，我偶爾也會聽到一些讓大家感興趣的事實。會計這行業啊……嗝……可有意思了，各種數字啦什麼的……

### (sub) DIAL_Z30#1331
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託說點更有意思的。偷牛的、偷情的老婆、不老實的商人——那種事。

### (sub) DIAL_Z30#1332
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 香豔跟腌臢的那種，嗯？唔。好，讓我想想。我記得上禮拜聽說了什麼事——至少我覺得是上禮拜。也可能是前一禮拜。不可能是馬拉克十字鎮那次併入之前——

### (sub) DIAL_Z30#1333
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託了，尼維克。我們可希望在天亮之前離開這裡。

### (sub) DIAL_Z30#1334
- speaker=27  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [14555..2]] -> node 4294901761
    - [flag 0x0101 in [18588..2]] -> node 4294901761
- text: 我……呃……很樂意配合您，不過看來我這張嘴又有點乾了。您看再請我喝一杯如何？

### (sub) DIAL_Z30#1335
- speaker=0  style=0
- effects:
    - TAKE gold -10
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1336
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，這下好多了。我剛才說到哪了？對了，說到這個故事。有——嗝——個住在賽瑟儂附近的傢伙，這一年裡申請了三塊新的土地。三——塊，聽懂了嗎？

### (sub) DIAL_Z30#1337
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他買地這件事有什麼可疑之處嗎？

### (sub) DIAL_Z30#1338
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，他挑的地段都挺不錯的。事實上都是上好的地皮，可他偏偏沒有……呃……爵位！一個出身卑微的人，怎麼買得起三塊上等地產？你倒是說說看！

### (sub) DIAL_Z30#1339
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這傢伙叫什麼名字？也許我們該查一查。

### (sub) DIAL_Z30#1340
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這算什麼問——嗝——問題啊？你以為我把帳本都背在腦子裡嗎？你這問題，還不如問我亞魯——亞魯莎親王的老婆叫什麼名字算了。

### (sub) DIAL_Z30#1341
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你的意思是，你連安妮塔公主的名字都記不得了？

### (sub) DIAL_Z30#1342
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不——她叫什麼名字？

### (sub) DIAL_Z30#1343
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你剛才在跟我說賽瑟儂附近那個人的事。你還知道他什麼事？跟我說說那個人。

### (sub) DIAL_Z30#1344
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊……我記得他叫費博……不，不對，完全不對……費利伯……修士的手指……地圖的鰭……發燒……費伯！麥克斯．費伯！就是他！你知道嗎，我現在真的真的累了，也許該回家了……

### (sub) DIAL_Z30#1345
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還有幾件事想知道。你覺得你還能再撐個幾分鐘嗎？

### (sub) DIAL_Z30#1346
- speaker=27  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [16132..2]] -> node 4294901761
    - [flag 0x0101 in [18588..2]] -> node 4294901761
- text: 當然……嗝……我撐得住。不過還得再喝點什麼才行。你請——嗝——客嗎？

### (sub) DIAL_Z30#1347
- speaker=0  style=0
- effects:
    - TAKE gold -10
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1348
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這下真是——那個啊——什麼？

### (sub) DIAL_Z30#1349
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜你是想說這杯酒正合你意吧。不如再多跟我們說說這個麥克斯．費伯的事？

### (sub) DIAL_Z30#1350
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不不不不……那個很無——嗝——聊……來聊聊過去這一年吧。你知道嗎，米德凱米亞每頭牛，光是牠的糞便，我們一年就能收一枚金幣……你知道嗎？我打賭你不知道！還有每隻鴨子……

### (sub) DIAL_Z30#1351
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 麥克斯．費伯。我想知道麥克斯．費伯的事。

### (sub) DIAL_Z30#1352
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好——好吧。莫西．費利伯。呃，我知道他幾年前想跟賈瑞德．萊克羅買下賽瑟儂那邊留下來的一些地產，可賈瑞德誰都不肯賣，所以莫西就——嗝——想出了個點子……你們真的不想聽聽鴨子的事嗎？

### (sub) DIAL_Z30#1353
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不用。快跟我們說麥克斯的事就好。他做了什麼？

### (sub) DIAL_Z30#1354
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他弄了把鏟子，挖啊——啊嗝——想嚇唬賈瑞德。當然賈瑞德什麼都不怕，不過倒是把——嗝——妮雅給嚇得不輕。

### (sub) DIAL_Z30#1355
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他在挖什麼東西？

### (sub) DIAL_Z30#1356
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我要睡了……晚安……

### (sub) DIAL_Z30#1357
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我再請你喝一杯？

### (sub) DIAL_Z30#1358
- speaker=27  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [17463..2]] -> node 4294901761
    - [flag 0x0101 in [18588..2]] -> node 4294901761
- text: 什麼，你的錢——錢——還沒花完啊？噢，那樣的話我再來一杯……既然你請客？

### (sub) DIAL_Z30#1359
- speaker=0  style=0
- effects:
    - TAKE gold -10
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1360
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 賽——賽瑟儂附近的墓——墓地。那就是他挖——挖的地方。怕——嗝——怕鬼跟賈——賈瑞德什麼的。才不是呢。就只是妮雅。妮雅一個人怕。

### (sub) DIAL_Z30#1361
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你覺得他買地的錢是從哪來的？

### (sub) DIAL_Z30#1362
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他說他在洞——洞裡找到的！所有的猴——嗝——銀子都在洞裡！只要去……拿就行了……才不怕什麼鵝呢。

### (sub) DIAL_Z30#1363
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說的是什麼洞？他要去哪裡？

### (sub) DIAL_Z30#1364
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我現在該回家了……

### (sub) DIAL_Z30#1365
- speaker=5  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [18055..2]] -> node 4294901761
    - [flag 0x0101 in [18588..2]] -> node 4294901761
- text: 再來一杯麥酒讓他繼續撐下去？

### (sub) DIAL_Z30#1366
- speaker=0  style=0
- effects:
    - TAKE gold -10
    - SET flag 0x1ece=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1367
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知——知道……那個地——地下的鑰匙跟串——串子……想跟我說什麼來——嗝——著，可我不是罪——罪犯……噢天啊……啊嗄。噢老天！我要吐——吐了！哈——嘔！

### (sub) DIAL_Z30#1368
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼東西？我聽不懂。

### (sub) DIAL_Z30#1369
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我說，我要吐了！

### (sub) DIAL_Z30#1370
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好啦，好啦。我看我這樣折騰你也夠了。睡個好覺吧，尼維克。我想我們該知道的都知道了。

### (sub) DIAL_Z30#1371
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18510..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1372
- speaker=0  style=0
- branches:
    - [flag 0x1ea7 in [18588..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：GET_NIVEK_DRUNK

### (sub) DIAL_Z30#1373
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1374
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我晚點再請你喝點什麼。眼下，我跟同伴恐怕得去別處辦點正事了。謝謝你的幫忙，尼維克！

### (sub) DIAL_Z30#1375
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18812..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1376
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：GET_NIVEK_DRUNK_STOP_BUYING

### (sub) DIAL_Z30#1377
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這位稅務官看起來ó病懨懨的。  他癱坐在長凳上，呆滯地望著虛空，單片眼鏡蒙上了一層霧氣，面容也鬆垮無力。看見詹姆士，他似乎又白了幾分臉色……

### (sub) DIAL_Z30#1378
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗚嗯……讓我死了吧，諸神啊！

### (sub) DIAL_Z30#1379
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 尼維克，還在宿醉啊？

### (sub) DIAL_Z30#1380
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……別這麼大聲……噢……拜託，就讓我這可憐的老頭子安靜等死吧……

### (sub) DIAL_Z30#1381
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定不想喝一杯嗎？

### (sub) DIAL_Z30#1382
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……我要你知道，我現在打從心底恨你……苦海都沒我對你的厭惡來得深……

### (sub) DIAL_Z30#1383
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我猜你現在沒心情聊天了。

### (sub) DIAL_Z30#1384
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……去跳下世界的邊緣吧……悄悄地……只要別發出任何聲音就好。再見了，詹姆士。

### (sub) DIAL_Z30#1385
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 保重，老朋友。

### (sub) DIAL_Z30#1386
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [19778..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1387
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [19873..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_Cx_Nivek_COMPLETED

### (sub) DIAL_Z30#1388
- speaker=0  style=0
- branches:
    - [flag 0x1ebb in [21637..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1389
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這位稅務官看起來ó病懨懨的。  他癱坐在長凳上，呆滯地望著虛空，單片眼鏡蒙上了一層霧氣，面容也鬆垮無力。看見歐文，他似乎又白了幾分臉色……

### (sub) DIAL_Z30#1390
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 請快點小聲說明來意。我現在……行動不便……

### (sub) DIAL_Z30#1391
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很抱歉打擾您宿醉，大人，不過我們有非常重要的事得跟您談談。您這幾天有見過或跟星塢島的帕格說過話嗎？他從王宮裡失蹤了，我們正試著查出他離開前去了哪裡、做了什麼。

### (sub) DIAL_Z30#1392
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許他跟我穿上安妮塔公主最華麗的禮服，在碼頭上跟骷髏跳了支舞，可我對昨晚的事一個細節都想不起來。我想我是喝多了……而且此刻我正深切地後悔著這件事。

### (sub) DIAL_Z30#1393
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您總該記得自己進酒館時的情形吧？

### (sub) DIAL_Z30#1394
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼都不記得。一刻都想不起來……腦子裡一片空白……我甚至不記得自己把鑰匙掉在哪了……

### (sub) DIAL_Z30#1395
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許找到您的鑰匙，您就會想起昨晚的事了。

### (sub) DIAL_Z30#1396
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是個值得敬重的理論，年輕的朋友，可我現在根本沒法動彈，沒辦法替您驗證這個假說。

### (sub) DIAL_Z30#1397
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 告訴我鑰匙長什麼樣子。要是我們碰巧找到，會幫您帶回來，說不定那時候您就會想起來了。

### (sub) DIAL_Z30#1398
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟其他鑰匙比起來也沒什麼特別的……上頭刻著我的名字……就這樣而已。  祝你們好運。

### (sub) DIAL_Z30#1399
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 保重，老朋友。

### (sub) DIAL_Z30#1400
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [21551..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1401
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [21637..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Nivek

### (sub) DIAL_Z30#1402
- speaker=0  style=0
- branches:
    - [flag 0x1fa0 in [24575..2]] -> node 4294901761
    - [flag 0xc391 in [22516..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1403
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這位稅務官看起來ó病懨懨的。  他癱坐在長凳上，呆滯地望著虛空，單片眼鏡蒙上了一層霧氣，面容也鬆垮無力。看見歐文，他似乎又白了幾分臉色……

### (sub) DIAL_Z30#1404
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜你們沒找到我的鑰匙吧？幸好鎖匠來過，給了我一把新的，讓我能重新進屋。不過我還是想知道，我那次縱酒狂歡到底跑到哪去了。

### (sub) DIAL_Z30#1405
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您還是想不起來嗎？

### (sub) DIAL_Z30#1406
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼都想不起來。我只知道我鞋子裡發現了一根小樹枝，口袋裡還有片葉子。也許我曾在林子裡遊蕩過。

### (sub) DIAL_Z30#1407
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 至少這給了戈……索爾加斯跟我一點線索。謝謝你，尼維克。

### (sub) DIAL_Z30#1408
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [22424..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1409
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [22516..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Nivek_NO_KEY

### (sub) DIAL_Z30#1410
- speaker=0  style=6
- effects:
    - SET flag 0x1fa0=1
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這位稅務官看起來ó病懨懨的。  他癱坐在長凳上，呆滯地望著虛空，單片眼鏡蒙上了一層霧氣，面容也鬆垮無力。看見歐文，他似乎又白了幾分臉色……

### (sub) DIAL_Z30#1411
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼，你們找到能解開我過去那把鑰匙了嗎？

### (sub) DIAL_Z30#1412
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 如果您是問我們有沒有找到您的鑰匙，答案是有。就在我包裡，不過……我建議您最好去找位律師諮詢一下。

### (sub) DIAL_Z30#1413
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 律師？為什麼？我的鑰匙在哪找到的？

### (sub) DIAL_Z30#1414
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們是在一具屍體身上找到的。就在克朗多城外不遠處。看起來他的頭側被某種大型鈍器狠狠砸過。他是您的仇家嗎？

### (sub) DIAL_Z30#1415
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是您是在暗示我醉醺醺的時候殺了人，那您可真是失心瘋了。我喝醉了並不會動粗，事實上，我通常喝個幾杯麥酒就會不省人事……我開始想起一些關於我那次……姑且稱之為『插曲』吧……的片段了。我記得有個男人走進彩虹鸚鵡酒館，請我喝了一杯，然後我似乎就跟著他去了某個地方……也許是城外？

### (sub) DIAL_Z30#1416
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是您殺了他的地方。

### (sub) DIAL_Z30#1417
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，是他……他又請我喝了幾杯……然後他帶我去了別的地方，還是他朋友帶我去的？然後……在那之後，一切又是一片空白了。

### (sub) DIAL_Z30#1418
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，是這些陌生人把您灌醉，偷走了您的鑰匙。您這把家門鑰匙，除了您家之外，還能開別的鎖嗎？

### (sub) DIAL_Z30#1419
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是的，它還能打開我在艾格利那間通訊處的鎖。親王特地為我打造了這把鑰匙，好讓我能出入王國財政部的任何一間辦事處。

### (sub) DIAL_Z30#1420
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 介意我們暫時借用一下這把鑰匙嗎？我想驗證一個推論。

### (sub) DIAL_Z30#1421
- speaker=27  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 請便。只要能幫上自己的忙，什麼都行。我真的很想把這件事查清楚。

### (sub) DIAL_Z30#1422
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會盡力而為的。謝謝。

### (sub) DIAL_Z30#1423
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24482..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1424
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24575..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Nivek_YES_KEY

### (sub) DIAL_Z30#1425
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1427
- speaker=0  style=0
- effects:
    - SET flag 0x1a7e=1
- branches:
    - [flag 0x1ebc in [29585..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1428
- speaker=0  style=0
- effects:
    - SET flag 0x003f=1
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1429
- speaker=28  style=0
- effects:
    - ?wOp12 a1=113 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們……我們可能是……

### (sub) DIAL_Z30#1430
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……雙胞胎，對，看起來是這樣沒錯。見到你，突然間有好多事在我心裡都清楚了起來。你跟克朗多的嘲弄幫是什麼關係？

### (sub) DIAL_Z30#1431
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這話什麼意思？我沒有……

### (sub) DIAL_Z30#1432
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 萊斯爾，別再裝傻了。我知道你跟克朗多的嘲弄幫脫不了關係。幾個月前，我在下水道調查一則傳聞時，被一夥打扮成夜鷹會的殺手綁架了。當時我以為他們綁架我，是因為我跟亞魯莎關係親近，可事實根本不是那樣，對吧？

### (sub) DIAL_Z30#1433
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那想必表示情況已經比正直人預想的還要糟了。他當初派人到凱許找我的時候……

### (sub) DIAL_Z30#1434
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉……你剛才是說凱許，就是大凱許帝國那個凱許嗎？

### (sub) DIAL_Z30#1435
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你比誰都該清楚，正直人的眼線無所不在，就連皇帝的眼皮子底下也不例外。要不然他也沒法在沒有這些眼線的情況下，經營米德凱米亞最強大的公會。不過我剛才說到——他派人到凱許找我，要我搭船去錫爾登，查探當地活動的一群竊賊。詳情我不方便多說，但我證實了正直人的懷疑。要是你比我先到克朗多，告訴其中一個竊賊——一個叫林姆的男孩——就說我認為正直人是對的，不過我現在相當確定，爬行者ñ絕不是喬科．瑞德本。他應該會拿點好處酬謝你這個消息……

### (sub) DIAL_Z30#1436
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有什麼陰謀正威脅著親王……

### (sub) DIAL_Z30#1437
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別費心了。克朗多的夜鷹會多半是在我在錫爾登搞砸調查之後，被派去殺正直人的，不是衝著亞魯莎去的。這個掌管新竊賊公會的爬行者，一心想擴張他的地盤，一直忙著滲透其他公會。他是至少半打公會背後的影子親王，其中最引人注目的，就是那個新成立的羅姆尼公會。他還在訓練他的手下學習法術……

### (sub) DIAL_Z30#1438
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一整幫竊賊都被訓練成法師？這聽起來一點都不妙。

### (sub) DIAL_Z30#1439
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也不喜歡，不過原因跟你不太一樣。我還在設法查出是誰在訓練他們。我追查的最後一條線索，聽說萊頓有人想買『榮光之手』——我聽過一些關於這種魔法器物的傳聞。我在賽瑟儂附近找到了這隻骸骨手，便賣給了萊頓一個叫格洛佛的傢伙。我猜想，要是他們真是法師，應該會看穿這是贗品，說不定就能讓我摸出點線索……

### (sub) DIAL_Z30#1440
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可他們跟你買了，卻毀了你的線索。你是怎麼找到那隻骸骨手的？

### (sub) DIAL_Z30#1441
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你大概會覺得這事有點噁心，不過……我原本打算去賽瑟儂的墓地挖個人出來，借用一隻手。既然那一帶已經荒廢好一陣子了，我想這是我不被發現、找到所需之物的最佳機會。幸好，有個老怪物幫我省了這番功夫。我不知道這傢伙拖著那具屍體想做什麼，不過他當時正把屍體拖過一片田野，像是要往墓地去。中途他似乎是累了或渴了，便把屍體暫時擱下，我就過去想ñ順手把這死人的手取走，可還沒完成，那老人就回來了。因為我當時差不多快把手弄下來了，隔天我又回去看看，那隻手在搬運過程中會不會已經鬆脫……

### (sub) DIAL_Z30#1442
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 於是你找到了它，賣給了萊頓的格洛佛。

### (sub) DIAL_Z30#1443
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此，不過我的麻煩並沒有就此結束。萊頓有幾個人認出了我，顯然是爬行者手下的人。看樣子我在錫爾登被發現之後，他就對我發出了追殺令。所以從那以後，我就一直在低調行事。

### (sub) DIAL_Z30#1444
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可以理解……要是哪天我們還能再見面，我想再跟你多聊聊。多了解一下你的出身背景。

### (sub) DIAL_Z30#1445
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是說，想查出我們是不是兄弟？這不太可能。我出生在圖藍，大概三年前才因為正直人召見而來到克朗多。我一直不確定他ñ為什麼要召見我，只知道他顯然聽說過我。不過他這人就是有點古怪。我看我這輩子大概都搞不懂他腦子裡在想什麼。

### (sub) DIAL_Z30#1446
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也是。至少謝謝你跟我聊了這麼多，萊斯爾。你幫了我們大忙，而且看看別人怎麼看待我，也挺有意思的。希望我們還能再見面。

### (sub) DIAL_Z30#1447
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29492..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1448
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [29585..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_CX_Lysle_Rigger

### (sub) DIAL_Z30#1449
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1450
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 113
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1451
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您好，詹姆士紳爵。是什麼風把您又吹回來了？

### (sub) DIAL_Z30#1452
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們回來是想確認一下，你把在賽瑟儂附近找到的那隻骸骨手賣去了哪。你說你賣給了萊頓一個叫格洛佛的人？

### (sub) DIAL_Z30#1453
- speaker=28  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是的，沒錯。

### (sub) DIAL_Z30#1454
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我只是想在自己出糗之前再確認一次。再次謝謝你，萊斯爾……

### (sub) DIAL_Z30#1455
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [30195..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1456
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [30287..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_CX_Lysle_Rigger

### (sub) DIAL_Z30#1457
- speaker=0  style=0
- branches:
    - [flag 0x1fa1 in [34909..2]] -> node 4294901761
    - [event_bitmap_hi[24] (xor=0xca mask=0x83 mode=2 chapters=-)] -> node 4278256128
    - [flag 0x1eca in [31359..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1458
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1459
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 一道身影從礦坑裡踉蹌走出。  歐文嚇得倒抽一口氣，但一旁的戈拉斯卻不為所動，面對這名傭兵的突然現身，他眼中滿是銳利的挑釁之色，彷彿早已料到他會出現。  這名男子留著一頭黑色短髮，緊貼在他寬闊的額頭上，露出一塊從髮際線一路蜿蜒到左眼下方的深色胎記。他打量了他們一番，朝戈拉斯點了點頭……

### (sub) DIAL_Z30#1460
- speaker=29  style=0
- effects:
    - play sfx 132
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人，你來這裡做什麼？這是我的私人礦區……

### (sub) DIAL_Z30#1461
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們不知道這是你的地盤。我們看見這個洞穴，以為可能是個過夜的好地方。

### (sub) DIAL_Z30#1462
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你現在ó知道了，我勸你別忘了，這裡是蘭恩的維努特里爾說了算。現在，滾吧……

### (sub) DIAL_Z30#1463
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。祝你愉快。

### (sub) DIAL_Z30#1464
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [31254..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1465
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [31359..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C4_Venutrier_of_Lan_BeforeQuest

### (sub) DIAL_Z30#1466
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1467
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 一道身影從礦坑裡踉蹌走出。  這名男子留著一頭黑色短髮，緊貼在他寬闊的額頭上，露出一塊從髮際線一路蜿蜒到左眼下方的深色胎記。他打量了他們一番，朝戈拉斯點了點頭……

### (sub) DIAL_Z30#1468
- speaker=29  style=0
- effects:
    - ?wOp12 a1=132 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人，你這是擅闖私人領地。這一帶是商業管制區，不是給人閒晃的地方……

### (sub) DIAL_Z30#1469
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可我對你的生意可感興趣得很，先生，這正是我找你的原因。我想把這男孩賣給你……

### (sub) DIAL_Z30#1470
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？！

### (sub) DIAL_Z30#1471
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哼，真可憐！他哭得跟頭小牛似的！得餵他一整群牲畜的量，才能讓他長點肉。他這麼虛弱，搞不好還帶著病。看起來好幾週沒吃過東西了……

### (sub) DIAL_Z30#1472
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他的外表會騙人。他單槍匹馬用一把廚刀殺了我的夥伴，還打斷了我另一個同伴的手臂。他會長成一個更強壯的男人。

### (sub) DIAL_Z30#1473
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 令人佩服，不過聽起來是個麻煩。我們得天天跟他搏鬥，才能防止他逃跑。

### (sub) DIAL_Z30#1474
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我才不會被賣給任何人！

### (sub) DIAL_Z30#1475
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一個輕易就能被制伏的傭兵沒什麼用處，你說是吧？磨掉他的意志，他就會成為你手裡的無價之寶。

### (sub) DIAL_Z30#1476
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他看起來出身高貴，我可不想招惹王國那邊派來的賞金獵人來煩我的生意……

### (sub) DIAL_Z30#1477
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他不過是個無足輕重的侍寢小廝。你不會惹上什麼麻煩的。

### (sub) DIAL_Z30#1478
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無足輕重？！

### (sub) DIAL_Z30#1479
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一百五十枚金幣，要就要，不要拉倒。不過在我們成交之前，你要不要先來看看我們這裡的營運情況？

### (sub) DIAL_Z30#1480
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這主意倒挺有意思的……要是不麻煩你的話？

### (sub) DIAL_Z30#1481
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一點也不麻煩。我的守衛會護送你……

### (sub) DIAL_Z30#1482
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人將他們團團圍住。  維努特里爾自顧自地笑了起來，像打量市場上買來的牛似的把兩人上下端詳了一番，先是歐文，接著又饒富興味地打量起戈拉斯。「太容易了，」他嘆了口氣說道。「你當我是什麼傻瓜？這男孩沒什麼用，戈拉斯，可ó你倒真是個上等的奴隸。你會喜歡你在下面的新生活的。」  無數雙手抓住了他們，將他們拖到洞口丟了進去。他們彷彿踉踉蹌蹌走了一段沒有盡頭的階梯……

### (sub) DIAL_Z30#1483
- speaker=0  style=0
- effects:
    - ACTION: reset kind-1/sub-0 timers, tick
    - load teleport table 28
- branches:
    - [flag 0x1ea8 in [33738..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1484
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
    - SET flag 0x1fa1=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1485
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 維努特里爾從礦坑裡走了出來。  他臉上帶著震驚的神情，望向戈拉斯跟歐文，搖了搖頭……

### (sub) DIAL_Z30#1486
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 維努特里爾，我巡視過你的洞穴了，對這裡經營得如此不善感到震驚。迪勒肯要是知道你把自己的地盤搞成這樣，肯定會大失所望。

### (sub) DIAL_Z30#1487
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這事跟ó他有什麼關係？我只看見一個叛徒莫瑞德人跟一個乳臭未乾的小子！你們的頭領怎麼會扯上這件事？

### (sub) DIAL_Z30#1488
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他的兒子莫萊伍夫已經傳話給他，說你窩藏叛徒，並打算派他的手下前來ó好好『照顧』你。我來這裡查過，並沒有發現什麼叛徒，不過你要是敢扣留我，我保證他一定會找上你……

### (sub) DIAL_Z30#1489
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我憑什麼相信你？他已經下令要取你的ó人頭了。

### (sub) DIAL_Z30#1490
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那不過是謠言。我還聽說穆爾曼達穆斯依然沉睡在薩薩戈斯呢，不過隨你怎麼想吧——要是你喜歡冒險的話。

### (sub) DIAL_Z30#1491
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呸！那就滾吧。你們兩個對我都沒用！離這些洞穴遠一點。

### (sub) DIAL_Z30#1492
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會讓你不受打擾地做生意。

### (sub) DIAL_Z30#1493
- speaker=0  style=0
- branches:
    - [flag 0x1ea7 in [34909..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1494
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1495
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 維努特里爾從礦坑裡走了出來。  他臉上帶著震驚的神情，望向戈拉斯跟歐文，搖了搖頭……

### (sub) DIAL_Z30#1496
- speaker=29  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我早跟你說過，莫瑞德人，我不想再在這附近看見你。

### (sub) DIAL_Z30#1497
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的錯，維努特里爾。我們會讓你不受打擾地做生意。

### (sub) DIAL_Z30#1498
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1499
- speaker=0  style=0
- branches:
    - [flag 0x1ebe in [36253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1500
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1018 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1501
- speaker=30  style=0
- effects:
    - play sfx 110
- branches:
    - [always] -> node 0 (no jump)
- text: 又見到你了，詹姆士，真高興。

### (sub) DIAL_Z30#1502
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我才更是榮幸，夫人。帕格在嗎？

### (sub) DIAL_Z30#1503
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你剛好錯過他了。他跟馬卡拉跑去某個地方討論法術了，要是我了解自己的丈夫，那就表示我這幾天都見不到他了。就算是在放假，他似乎也沒法讓心思長時間離開法術這門技藝。

### (sub) DIAL_Z30#1504
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在很多方面，他跟親王還真像。話說回來，亞魯莎人在哪？

### (sub) DIAL_Z30#1505
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 帶著他那對雙胞胎跟安妮塔公主出去了。看來你那出了名的好運，今天似乎有點薄弱啊。

### (sub) DIAL_Z30#1506
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恰恰相反，因為我還有夫人您相伴。方便耽誤您一點時間嗎……

### (sub) DIAL_Z30#1507
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您需要多少時間都行。我能為您做什麼？

### (sub) DIAL_Z30#1508
- speaker=0  style=0
- effects:
    - push return-address key 167209 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1509
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [36166..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1510
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36253..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Katala

### (sub) DIAL_Z30#1511
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1018 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1512
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許帕格的能力，多少也感染了我一些。上次我們見面之後，我有種——你大概會稱之為『預感』的東西吧——覺得你很快就會回來。我能為你做什麼？

### (sub) DIAL_Z30#1513
- speaker=0  style=0
- effects:
    - push return-address key 167583 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1514
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [36540..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1515
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36626..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Katala

### (sub) DIAL_Z30#1516
- speaker=0  style=0
- branches:
    - [flag 0x1ebe in [38189..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1517
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1518
- speaker=30  style=0
- effects:
    - play sfx 110
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士！

### (sub) DIAL_Z30#1519
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士紳爵聽候差遣，夫人。抱歉打擾您了……

### (sub) DIAL_Z30#1520
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，不會。其實我很高興你能來，詹姆士。王宮裡最近變得非常古怪。亞魯莎親王已經好幾週沒有臨朝了，帕格則把自己跟馬卡拉、還有我們的女兒蓋米娜關在一起，天曉得在討論些什麼。

### (sub) DIAL_Z30#1521
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，您覺得自己被排除在外了，是嗎？

### (sub) DIAL_Z30#1522
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想過去我一直很榮幸——甚至可以說是被寵壞了——因為他總會把心裡的想法都告訴我。他讓我見識過我從未能想像的事物，可如今他卻對我有所隱瞞。某種程度上，我幾乎忍不住覺得，有什麼事讓他感到害怕了。

### (sub) DIAL_Z30#1523
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓帕格感到害怕？老天，這聽起來可不妙！我能跟他談談嗎？

### (sub) DIAL_Z30#1524
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也希望你能，可他已經去了我們星塢島的學院。我不知道他打算什麼時候回來。更糟的是，我去見亞魯莎親王的時候，他傳話說自己忙於國事，沒空見我。這一點都不像他的作風。

### (sub) DIAL_Z30#1525
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是不像，不過我對這一切可能代表什麼，有一些懷疑。首先，我有幾件事需要了解……

### (sub) DIAL_Z30#1526
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽候你差遣。

### (sub) DIAL_Z30#1527
- speaker=0  style=0
- effects:
    - push return-address key 169145 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1528
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [38102..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1529
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [38189..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Katala

### (sub) DIAL_Z30#1530
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1531
- speaker=30  style=0
- effects:
    - ?wOp12 a1=110 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡的情況沒有任何好轉，不過謝天謝地，也沒有惡化。紳爵，很高興再見到你。

### (sub) DIAL_Z30#1532
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [38397..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1533
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [38483..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Katala

### (sub) DIAL_Z30#1534
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1535
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……冥想塔是我最先想到要去找的地方之一。我一發現他跟女兒那天早上都沒來吃早餐，就立刻趕了過去。我在那裡找到了他用火燒在牆上的訊息。

### (sub) DIAL_Z30#1536
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克羅斯之書……您覺得這則訊息是什麼意思？

### (sub) DIAL_Z30#1537
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我一度以為他是想要我們去聯繫一位名叫馬克羅斯的法師，不過就算是帕格，也不可能辦到這種事。馬克羅斯早在很久以前就已經離開了米德凱米亞，只留下了他的著作。

### (sub) DIAL_Z30#1538
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼，這本『馬克羅斯之書』想必就在他留下的著作之中了。

### (sub) DIAL_Z30#1539
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧，不過我不能肯定。馬克羅斯留在法師之島上的藏書浩如煙海，我們花了將近一年的時間，才把大部分搬到星塢島的學院。從那之後，有些卷冊也被外借給各地的抄寫員，以便編目跟謄抄。

### (sub) DIAL_Z30#1540
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那這本書可能在任何地方——得換個方向找了。他失蹤之前，您有沒有注意到他說過或做過什麼不尋常的事？

### (sub) DIAL_Z30#1541
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就像我先前說的，他已經焦躁不安好一段時間了，不過，對，是有件事。大概一個月前，我們倆在王宮外的花園裡散步，就我們兩個人享受著那天的陽光，他卻突然在一道下水道柵欄旁停下腳步。我問他怎麼了，他說：『不是所有的羊都在我們的羊圈裡。』

### (sub) DIAL_Z30#1542
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 羊？恕我直言，夫人，令夫似乎特別偏好讓人抓狂的隱晦說法。

### (sub) DIAL_Z30#1543
- speaker=30  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 平常倒不會，只有心事重重的時候才這樣。好了，我得動身前往星塢島，去那裡找找這本馬克羅斯之書的線索了。你們兩個要去哪？

### (sub) DIAL_Z30#1544
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夫人，我們要下到克朗多下方的下水道去，歐文。我想，我們這些牧羊人，有一群走失的羊要找。

### (sub) DIAL_Z30#1545
- speaker=0  style=0
- effects:
    - END conversation, result=65532

### (sub) DIAL_Z30#1546
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40500..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1547
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [40583..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Katala

### (sub) DIAL_Z30#1548
- speaker=0  style=0
- branches:
    - [flag 0x1ebf in [44955..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1549
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1550
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方的路被擋住了。  看守橋樑的人群之中，一名男子上前攔住了他們……

### (sub) DIAL_Z30#1551
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我勸你們別再靠近羅姆尼了。那座城正遭到圍困。

### (sub) DIAL_Z30#1552
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡發生了什麼事？

### (sub) DIAL_Z30#1553
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 公會戰爭、暴動、一片混亂，整個羅姆尼都失去理智了。我很意外你們居然沒聽說過，不過話說回來，在這一帶，羅姆尼一個小孩擦破膝蓋，大概都比里蘭儂的加冕典禮還重要。這一切，是從縴夫公會被一個分裂出去的公會——羅姆尼公會——擠出錫爾登開始的。縴夫公會想靠在羅姆尼提高運費來彌補損失，玻璃匠公會跟染工公會不肯承受這個負擔，便轉而跟那個分裂公會簽約運貨。不料縴夫公會宣稱他們握有王室授予的河運獨佔權，燒了兩艘羅姆尼公會的木筏。玻璃匠公會有三名成員葬身火場，染工公會的總管事也不幸罹難。從那之後，...

### (sub) DIAL_Z30#1554
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前看來哪一方占上風？

### (sub) DIAL_Z30#1555
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哪一方都沒有。這是場僵局，勞工公會占據著烏爾辛渡口的北岸，工匠公會則占著南岸。縴夫公會下令封鎖之前，我剛好被困在這一邊。噢，對了，我叫米契爾．韋蘭德，是玻璃匠公會的地方總管事。

### (sub) DIAL_Z30#1556
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 幸會。你覺得要怎樣才能結束這場紛爭？

### (sub) DIAL_Z30#1557
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們是坐下來跟他們談過，可縴夫公會的頭頭是個老頑固，坦白說，我不認為他真想結束這件事。他們宣稱，凡是違約沒能運送出去的貨物，全都歸他們所有，算是違約金。當地的律師告訴他，這已經超出王國慣例了，可縴夫公會卻堅稱，這也是他們王室特許狀裡的內容。我們到現在都還不知道這份文件到底存不存在。

### (sub) DIAL_Z30#1558
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還有別的路能進羅姆尼嗎？

### (sub) DIAL_Z30#1559
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 曾經有段時間，你還能雇條船載你進去，可現在河上沒人傻到敢去闖那道封鎖線。因為這樣，河上幾乎沒什麼人了。還留在這一帶的人，都是些能說會道、討價還價一流的人。

### (sub) DIAL_Z30#1560
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的嗎？為什麼會這樣？

### (sub) DIAL_Z30#1561
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 除非你討價還價的本事跟他們一樣厲害，不然這河上什麼貨你都買不到公道的價錢。在這一帶想買一包口糧，大概跟想買萊亞姆王的王冠一樣難。

### (sub) DIAL_Z30#1562
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然你也是幹這行的，也許能教我們幾招討價還價的訣竅……

### (sub) DIAL_Z30#1563
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許可以，不過……我真的得去斯魯普找我的一些同僚。我拖得越久，損失的錢就越多。

### (sub) DIAL_Z30#1564
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你能幫忙，我們或許願意補償你耽誤的時間。

### (sub) DIAL_Z30#1565
- speaker=31  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [46097..2]] -> node 4294901761
    - [flag 0x0101 in [43807..2]] -> node 4294901761
- text: 真的嗎？這樣的話，我想……五十枚金幣，或許能說服我幫你們一把。這是我的條件。你們覺得如何？

### (sub) DIAL_Z30#1566
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1567
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們暫時算了。我一向對划算的交易感興趣，可不是你開的這個價。

### (sub) DIAL_Z30#1568
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便，不過小心點。這一帶大部分的公會，把這件事看得就跟大凱許的走狗部隊撐船殺上羅姆尼一樣嚴重。對我們大多數人來說，這就是ó戰爭。

### (sub) DIAL_Z30#1569
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們這話八九不離十。羅姆尼是王國的一個村鎮，因此也是座自由城鎮。任何硬要把這座城市違反其意願封鎖起來的派系，都活該被開戰對付，不管有沒有王國詔令都一樣。我相信你們的公爵對這件事一定有話要說。

### (sub) DIAL_Z30#1570
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他當然不太高興，這是肯定的，不過在他能請動五金匠公會的會長出面談判之前，他也做不了什麼。這些都不重要了。我還得看守這座橋，之後還得去斯魯普處理點事情。兩位，先告辭了。

### (sub) DIAL_Z30#1571
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 祝你愉快。我們回頭再聊。

### (sub) DIAL_Z30#1572
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [44843..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1573
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [44955..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Mitchel_Waylander_PAY_FOR_IT_NO

### (sub) DIAL_Z30#1574
- speaker=0  style=0
- branches:
    - [flag 0x1ed9 in [50923..32813]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1575
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 前方的路被擋住了。  看守橋樑的人群之中，一名男子上前攔住了他們……

### (sub) DIAL_Z30#1576
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我有點吃驚，我還一度以為你們已經死了呢。很高興看到縴夫公會沒把你們送進墳墓。

### (sub) DIAL_Z30#1577
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們挺過來了。你在斯魯普的事情辦好了嗎？

### (sub) DIAL_Z30#1578
- speaker=31  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [46097..2]] -> node 4294901761
    - [flag 0x0101 in [45706..2]] -> node 4294901761
- text: 那邊的玻璃匠說他們會派幾個人來支援，不過不確定會派多少人、什麼時候到。我只能相信他們的話，希望到頭來用不上這些援手。那，討價還價那堂課怎麼樣？我還是需要那筆資金。有興趣嗎？

### (sub) DIAL_Z30#1579
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1580
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，就像我們之前說的，這個價錢對我們來說太高了。

### (sub) DIAL_Z30#1581
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 到頭來你們還是得付出更多代價，不過那是你們的選擇。祝你們愉快。

### (sub) DIAL_Z30#1582
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你也是。

### (sub) DIAL_Z30#1583
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45986..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1584
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [46097..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Mitchel_Waylander_PAY_FOR_IT_NO

### (sub) DIAL_Z30#1585
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [46126..2]] -> node 4294901810
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1586
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1003 a2=0
    - TAKE gold -500
    - SET flag 0x1ed9=1
    - RAISE Haggling of party by 2560
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1587
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我說你們瘋得跟老羅德里克王有得比，不過我也不能怪你們想正正當當賺點錢。成交。

### (sub) DIAL_Z30#1588
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 第一件事，說話的時候別抱著胳膊。我知道身為貴族，你們從小被教導要盡量擺出威嚴的架勢，可那一套買一匹布的時候可行不通。要表現得脆弱一點，至少也別擺出一副高高在上的樣子。一旦你顯得跟凡人沒兩樣，對方就更容易相信你是真的需要通融。

### (sub) DIAL_Z30#1589
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽起來挺有道理。還有呢？

### (sub) DIAL_Z30#1590
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟你說話的時候，要直視他的眼睛。這會讓他相信你跟他有共同的利益，通常也會讓他心軟、慷慨起來。要是他覺得自己在這件事上握有話語權，他就會更好說話……

### (sub) DIAL_Z30#1591
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那要是他其實沒有話語權呢？

### (sub) DIAL_Z30#1592
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……第三課，絕不要打斷你想跟他買東西的那個人說話。第四課，在討價還價的氣氛裡，對錯是沒有意義的。店家拿給你看的劍，是不是全國最好的一把劍，其實根本不重要。你要嘛對他開的價錢感興趣，要嘛不感興趣。質疑他的誠信，只會換來他的輕蔑。表現出不感興趣，往往更能讓你談到更好的價錢。

### (sub) DIAL_Z30#1593
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唔。有些東西值得好好想想，我敢說我們以後在別處也用得上你這番智慧。

### (sub) DIAL_Z30#1594
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是我的榮幸。我很想多留下來聊聊，不過我還有財務上的事要處理。告辭了。

### (sub) DIAL_Z30#1595
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你，米契爾。告辭。

### (sub) DIAL_Z30#1596
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [47786..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1597
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [47906..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：WANT_LESSON_FROM_Mitchel_Waylander_ENOUGH_MONEY

### (sub) DIAL_Z30#1598
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1599
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 老毛病又犯了，我這張嘴又答應了我這荷包負擔不起的交易。我沒有錢能付給你。

### (sub) DIAL_Z30#1600
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我很抱歉，我沒空在這裡耗著。抱歉了，紳爵，不過也許等我在別處把事情辦完，我們可以再見一面。告辭。

### (sub) DIAL_Z30#1601
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了，米契爾。

### (sub) DIAL_Z30#1602
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [48327..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1603
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：WANT_LESSON_FROM_Mitchel_Waylander_NOT_ENOUGH_MONEY // END: WANT_LESSON_FROM_Mitchel_Waylander

### (sub) DIAL_Z30#1604
- speaker=0  style=0
- branches:
    - [flag 0x1ebf in [51350..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1605
- speaker=0  style=0
- branches:
    - [flag 0xc3ad in [51186..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1606
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1607
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方的路被擋住了。  看守橋樑的人群之中，一名男子上前攔住了他們……

### (sub) DIAL_Z30#1608
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們有玻璃匠公會的印信嗎？我得先看過才能讓你們過橋。我們正試著阻止這裡爆發全面的公會戰爭，得確保不會有不受歡迎的人物出現。這只是個手續，等我們這裡的情況再度穩定下來就好。

### (sub) DIAL_Z30#1609
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 公會戰爭？你這話什麼意思？

### (sub) DIAL_Z30#1610
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡發生過一場暴動，持續了好幾個月。縴夫公會掌控了其他勞工公會，把羅姆尼團團圍住。工匠公會試圖突圍，眼看就要打輸了，幸好國王的人馬從巴斯泰拉趕來支援，才總算安撫住了縴夫公會的頭頭。羅姆尼公爵一直設法防止情勢惡化，不過我沒法保證他還能撐多久。恐怕還得再過一陣子，我們才能對一般民眾重新開放道路。

### (sub) DIAL_Z30#1611
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鎮民能自由進出嗎？

### (sub) DIAL_Z30#1612
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們限制的是外來的訪客，不是把居民關起來。任何鎮民都能隨意進出。

### (sub) DIAL_Z30#1613
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜這對你們的客人也一樣適用吧？國王部隊的人能出來走動嗎？我們跟他們有事要談。

### (sub) DIAL_Z30#1614
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很樂意幫忙，不過我不太確定該怎麼聯絡上他們。他們很難聚在一起，而且我也不確定自己見過他們的頭領。他們是一群相當不輕易信任人的傢伙。

### (sub) DIAL_Z30#1615
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們也只能如此。要追蹤刺客，你得比獵物更狡猾、道德底線也要低上一些才行。  那，我該去哪弄一枚這種印信？

### (sub) DIAL_Z30#1616
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒那麼簡單。錫爾登附近有一群人，已經申請入會好一陣子了，可他們是群不服管教的傢伙，一直找不到人願意替他們擔保。

### (sub) DIAL_Z30#1617
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那要是我出示印信，你就會二話不說讓路？

### (sub) DIAL_Z30#1618
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，倒也不是二話不說，不過那至少能證明公會裡有人替你擔保。

### (sub) DIAL_Z30#1619
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夠了，總管事。我們會再回來的。這段期間，請替我們帶個口信給巴斯泰拉來的國王部隊，就說很快會有三個人來拜訪他們，是為了一隻在夜裡獵殺的夜行猛禽的事。他們會明白這則訊息的意思。

### (sub) DIAL_Z30#1620
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [51076..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1621
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [51186..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Mitchel_Waylander_HAS_NO_SEAL

### (sub) DIAL_Z30#1622
- speaker=0  style=0
- effects:
    - push return-address key 182287 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1623
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [51244..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1624
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [51350..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Mitchel_Waylander_HAS_SEAL

### (sub) DIAL_Z30#1625
- speaker=0  style=0
- branches:
    - [flag 0xc3ad in [52213..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1626
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1627
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方的路被擋住了。  看守橋樑的人群之中，一名男子上前攔住了他們……

### (sub) DIAL_Z30#1628
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 站住。沒有玻璃匠公會的……我不能讓你們過去。

### (sub) DIAL_Z30#1629
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……印信，是的，你之前說過了。我跟國王部隊有非常重要的事，不能再容忍被一群自以為是的蠢牛耽擱下去！讓我們過去！

### (sub) DIAL_Z30#1630
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拿出印信，這座城就是你的了。在那之前，紳爵，你就睡泥地裡吧。這正配得上你的禮數。

### (sub) DIAL_Z30#1631
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 眼下，我這份『禮數』，是唯一能讓你的腦袋跟我的靴子保持距離的東西。我們會再回來的。

### (sub) DIAL_Z30#1632
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52104..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1633
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52213..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Mitchel_Waylander_HAS_NO_SEAL

### (sub) DIAL_Z30#1634
- speaker=0  style=0
- effects:
    - push return-address key 183314 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1635
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52271..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1636
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52377..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Mitchel_Waylander_HAS_SEAL

### (sub) DIAL_Z30#1637
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
    - SET flag 0x1cea=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1638
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方的路被擋住了。  看守橋樑的人群之中，一名男子上前攔住了他們……

### (sub) DIAL_Z30#1639
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前羅姆尼城是封閉的，只有居民跟玻璃匠公會的成員能進出。你們有我們公會的印信嗎？

### (sub) DIAL_Z30#1640
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有。為什麼是一個公會在掌管這座城市？

### (sub) DIAL_Z30#1641
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 治安隊在縴夫公會發動的暴動中全數喪命，沒有其他任何有權責的人存活下來主持大局。當有人請我出面接管的時候，我決定動用公會裡的人手維持秩序，直到公爵能從他的領地趕來為止。

### (sub) DIAL_Z30#1642
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這倒也說得過去。我們能在哪找到巴斯泰拉來的國王部隊？

### (sub) DIAL_Z30#1643
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們正待在黑羊酒館，好像在慶祝什麼。我記得聽見他們其中一人說，他們找到了一直在找的東西。詳細情況我就不清楚了。

### (sub) DIAL_Z30#1644
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想這對我們來說，或許也是個好消息。晚安，總管事。我們這就進羅姆尼去。

### (sub) DIAL_Z30#1645
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [53564..2]] -> node 4294901761

### (sub) DIAL_Z30#1646
- speaker=0  style=0
- effects:
    - free paged image table
- text: 這是對話路徑的結尾：SHOW_Mitchel_Waylander_THE_SEAL

### (sub) DIAL_Z30#1647
- speaker=0  style=0
- branches:
    - [flag 0x1ebf in [60983..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1648
- speaker=0  style=0
- branches:
    - [flag 0x1ceb in [56206..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1649
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1650
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 39
    - ?wOp12 a1=1017 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4小心翼翼地敲了敲門。  幾個緊繃的片刻過後，木門開始嘎吱作響，隨即敞開。一道身影從黑暗的房間裡走了出來，@4握緊了劍柄，準備應付任何突發狀況。儘管米契爾．韋蘭德並不是他特別中意的人物，看見這張熟悉的面孔，他還是稍稍鬆了口氣……而米契爾看見ó他們ð，似乎也鬆了一口氣。

### (sub) DIAL_Z30#1651
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道是誰派你們來的，但我真的非常感激你們的幫忙！

### (sub) DIAL_Z30#1652
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，最近凡是被夜鷹會的劍指著的人，我都很感興趣。除非目標被視為對公會構成威脅，不然他們一般不會派出這麼多刺客。

### (sub) DIAL_Z30#1653
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可我只是個商人！我對刺客公會一無所知！

### (sub) DIAL_Z30#1654
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你未必需要對他們有所了解。也許你目睹了什麼他們不想被人看見的事，又或者他們認為你在某方面得罪了他們。巴斯泰拉那支國王部隊遇刺的那晚，你人在哪裡？

### (sub) DIAL_Z30#1655
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？！我都還沒聽說……老天，他們都是好人啊！要不是有他們，我們根本沒法打破縴夫公會對羅姆尼的圍困。他們是怎麼死的？

### (sub) DIAL_Z30#1656
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夜鷹會的人在黑羊酒館襲擊了他們，把每個人都殺光了。唯一讓我覺得奇怪的是，幾乎沒有任何反抗的跡象。看店的男孩告訴我，前一晚有人送來了幾桶凱許麥酒，可巴斯泰拉的人紀律極為嚴明。我很懷疑他們在追蹤夜鷹會的時候，還會喝到爛醉。我懷疑那批麥酒被人動了手腳，好確保刺客們能盡量輕鬆得手。我們還在屍體上找到了一隻銀蜘蛛跟一支黃銅望遠鏡。

### (sub) DIAL_Z30#1657
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 黃銅望遠鏡？我同意，這確實很奇怪，非常奇怪。我很好奇他們拿那東西做什麼？不過那隻銀蜘蛛，那絕對是個徵兆。那是刺客的工具……

### (sub) DIAL_Z30#1658
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的嗎？那東西怎麼用？

### (sub) DIAL_Z30#1659
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也不清楚。我只聽說夜鷹會的人有時候會帶著這東西。也許是他們打鬥的時候掉在屍體上的。

### (sub) DIAL_Z30#1660
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這至少算是條線索。謝謝你，米契爾。要是我們還需要你，能去哪找你？

### (sub) DIAL_Z30#1662
- speaker=0  style=0
- effects:
    - SET flag 0x1f98=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1663
- speaker=0  style=6
- effects:
    - ?wOp12 a1=34 a2=0
    - play sfx 39
    - ?wOp12 a1=1017 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4小心翼翼地敲了敲門。  幾個緊繃的片刻過後，木門開始嘎吱作響，隨即敞開。一道身影從黑暗的房間裡走了出來，@4握緊了劍柄，準備應付任何突發狀況。儘管米契爾．韋蘭德並不是他特別中意的人物，看見這張熟悉的面孔，他還是稍稍鬆了口氣……而米契爾看見ó他們ð，似乎也鬆了一口氣。

### (sub) DIAL_Z30#1664
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道是誰派你們來的，但我真的非常感激你們的幫忙。

### (sub) DIAL_Z30#1665
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，最近凡是被夜鷹會的劍指著的人，我都很感興趣。除非目標被視為對公會構成威脅，不然他們一般不會派出這麼多刺客。

### (sub) DIAL_Z30#1666
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可我只是個商人！我對刺客公會一無所知！

### (sub) DIAL_Z30#1667
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你未必需要對他們有所了解。也許你目睹了什麼他們不想被人看見的事，又或者他們認為你在某方面得罪了他們。巴斯泰拉那支國王部隊遇刺的那晚，你人在哪裡？

### (sub) DIAL_Z30#1668
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？！我都還沒聽說……老天，他們都是好人啊！要不是有他們，我們根本沒法打破縴夫公會對羅姆尼的圍困。他們是怎麼死的？

### (sub) DIAL_Z30#1669
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夜鷹會的人在黑羊酒館襲擊了他們，把每個人都殺光了。唯一讓我覺得奇怪的是，幾乎沒有任何反抗的跡象。看店的男孩告訴我，前一晚有人送來了幾桶凱許麥酒，可巴斯泰拉的人紀律極為嚴明。你覺得合理嗎？一支正在追蹤夜鷹會的分隊，會在他們懷疑刺客公會設有總部的城鎮裡喝得爛醉？

### (sub) DIAL_Z30#1670
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這聽起來是有點奇怪……

### (sub) DIAL_Z30#1671
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也覺得奇怪，所以我判斷那批麥酒一定被動了手腳。我想，要是能找到送酒的人，或許就能循線找到夜鷹會。於是我造訪了鎮上這間酒館，發現了一件非常令人不安的事。這批送酒的安排就是在這裡談成的，酒館老闆被交代要在酒裡加入大量的焦渴草，這種東西雖然沒有毒，卻會讓喝的人變得異常口渴，確保他會不停地喝下去，直到爛醉如泥。不過真正令人震驚的消息還在後頭。原來，安排這批麥酒送貨的，正是本地一個聲望顯赫的公會的總管事……米契爾．韋蘭德。

### (sub) DIAL_Z30#1672
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我從沒下過那筆訂單！那筆交易談成的時候，我人應該在羅姆尼。我不可能下那個訂單的！

### (sub) DIAL_Z30#1673
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這我也知道。夜鷹會費了這麼大的功夫想嫁禍給你，這說明他們是想為了什麼事報仇。派來殺你的人，無疑會在你的屍體上留下最後的『證據』。那麼，你到底對他們做了什麼？

### (sub) DIAL_Z30#1674
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我真的不知道……

### (sub) DIAL_Z30#1675
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你對銀蜘蛛或黃銅望遠鏡有任何了解嗎？

### (sub) DIAL_Z30#1676
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 黃銅望遠鏡？噢，天啊！可那個人不可能是夜鷹會的人啊……他看起來那麼、那麼氣派……

### (sub) DIAL_Z30#1677
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你對這個人做了什麼？跟那支望遠鏡有關嗎？

### (sub) DIAL_Z30#1678
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 羅姆尼北邊有個地方叫『惡作劇石』。人一靠近那裡，身上的物品就常常會不翼而飛。我跟一個生意夥伴發現了這些消失的物品都跑去了哪裡，便把找到的東西拿去變賣。總之，有天晚上，我在同名的那座小鎮喝酒，看見一個男人帶著一支非常精美的黃銅望遠鏡。我當時公會的處境很艱難，手頭又缺錢，便起了心思想把那支望遠鏡弄到手。我注意到他一直在留意一個相當標緻的酒館女侍，便安排人送了張字條到他桌上，說要他到惡作劇石附近跟她碰面。那支望遠鏡就這樣到了我們手上。

### (sub) DIAL_Z30#1679
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是被你偷走望遠鏡的那個人查出真相，我能理解他為什麼會想報仇。你把它賣去哪了？

### (sub) DIAL_Z30#1680
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不負責賣東西。是我的夥伴在賣，我們平分利潤。除了他是錫爾登本地人這件事以外，我對他一無所知。我們一開始就講好只分贓不通消息，這樣一個人要是被抓，另一個還能安然無恙。

### (sub) DIAL_Z30#1681
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那看來我們在錫爾登還有事要辦了。低調行事吧。這或許是唯一能保住你性命的辦法了，米契爾。夜鷹會可不是能隨便招惹的人。

### (sub) DIAL_Z30#1682
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [60885..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1683
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [60983..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Mitchel_Waylander

### (sub) DIAL_Z30#1684
- speaker=0  style=0
- branches:
    - [flag 0x1ceb in [61762..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1685
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1686
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1687
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你查出這樁謀殺案的新線索了嗎？

### (sub) DIAL_Z30#1688
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還沒有。我們原本希望你可能對這件事有些額外的見解。

### (sub) DIAL_Z30#1689
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們找錯人了。自從那些夜鷹會的人來找過我之後，我到現在都還在發抖……

### (sub) DIAL_Z30#1690
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是連這點都不能體諒，那我未免太不通情理了。那我們就先讓你好好定定神吧。祝你愉快，米契爾。

### (sub) DIAL_Z30#1691
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [61665..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1692
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [61762..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Mitchel_Waylander

### (sub) DIAL_Z30#1693
- speaker=0  style=0
- effects:
    - SET flag 0x1f98=1
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1694
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1695
- speaker=31  style=0
- effects:
    - ?wOp12 a1=116 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你查出是誰殺了國王部隊的人了嗎？

### (sub) DIAL_Z30#1696
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也覺得奇怪，所以我判斷那批麥酒一定被動了手腳。我想，要是能找到送酒的人，或許就能循線找到夜鷹會。於是我造訪了鎮上這間酒館，發現了一件非常令人不安的事。這批送酒的安排就是在這裡談成的，酒館老闆被交代要在酒裡加入大量的焦渴草，這種東西雖然沒有毒，卻會讓喝的人變得異常口渴，確保他會不停地喝下去，直到爛醉如泥。不過真正令人震驚的消息還在後頭。原來，安排這批麥酒送貨的，正是本地一個聲望顯赫的公會的總管事……米契爾．韋蘭德。

### (sub) DIAL_Z30#1697
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我從沒下過那筆訂單！那筆交易談成的時候，我人應該在羅姆尼。我不可能下那個訂單的！

### (sub) DIAL_Z30#1698
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這我也知道。夜鷹會費了這麼大的功夫想嫁禍給你，這說明他們是想為了什麼事報仇。派來殺你的人，無疑會在你的屍體上留下最後的『證據』。那麼，你到底對他們做了什麼？

### (sub) DIAL_Z30#1699
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我真的不知道……

### (sub) DIAL_Z30#1700
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你對銀蜘蛛或黃銅望遠鏡有任何了解嗎？

### (sub) DIAL_Z30#1701
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 黃銅望遠鏡？噢，天啊！可那個人不可能是夜鷹會的人啊……他看起來那麼、那麼氣派……

### (sub) DIAL_Z30#1702
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你對這個人做了什麼？跟那支望遠鏡有關嗎？

### (sub) DIAL_Z30#1703
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 羅姆尼北邊有個地方叫『惡作劇石』。人一靠近那裡，身上的物品就常常會不翼而飛。我跟一個生意夥伴發現了這些消失的物品都跑去了哪裡，便把找到的東西拿去變賣。總之，有天晚上，我在同名的那座小鎮喝酒，看見一個男人帶著一支非常精美的黃銅望遠鏡。我當時公會的處境很艱難，手頭又缺錢，便起了心思想把那支望遠鏡弄到手。我注意到他一直在留意一個相當標緻的酒館女侍，便安排人送了張字條到他桌上，說要他到惡作劇石附近跟她碰面。那支望遠鏡就這樣到了我們手上。

### (sub) DIAL_Z30#1704
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是被你偷走望遠鏡的那個人查出真相，我能理解他為什麼會想報仇。你把它賣去哪了？

### (sub) DIAL_Z30#1705
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不負責賣東西。是我的夥伴在賣，我們平分利潤。除了他是錫爾登本地人這件事以外，我對他一無所知。我們一開始就講好只分贓不通消息，這樣一個人要是被抓，另一個還能安然無恙。

### (sub) DIAL_Z30#1706
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那看來我們在錫爾登還有事要辦了。低調行事吧。這或許是唯一能保住你性命的辦法了，米契爾。夜鷹會可不是能隨便招惹的人。

### (sub) DIAL_Z30#1707
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [64771..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1708
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [64868..2]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Mitchel_Waylander

### (sub) DIAL_Z30#1709
- speaker=0  style=0
- branches:
    - [flag 0x1ec8 in [64897..2]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1710
- speaker=0  style=0
- effects:
    - SET flag 0x1faa=1
    - ?wOp12 a1=1002 a2=0
    - GIVE item 'z' cond=1 to member#5 (cost 0)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1711
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1712
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我現在沒空聊天。我還有玻璃匠公會的事要處理，今晚天黑之前還有一大堆罐子要上釉……

### (sub) DIAL_Z30#1713
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們是從馬拉克十字鎮來的。是葛雷夫斯院長派我們來的。

### (sub) DIAL_Z30#1714
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為了什麼事？

### (sub) DIAL_Z30#1715
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬拉克十字鎮的鎮民正在要求處死他。他說我們該來找你幫忙。

### (sub) DIAL_Z30#1716
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他這是在賭一把，賭偏偏是我會出手幫他。要不是我當初接受了他跟爬行者、還有羅姆尼公會的關係，這場公會戰爭說不定根本就不會爆發……真該死。我心底知道他當初是想幫我們，可他惹出來的這些麻煩……你們覺得他們真的會想殺他嗎？

### (sub) DIAL_Z30#1717
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒法確定，不過院長本人看起來相當確信。

### (sub) DIAL_Z30#1718
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他也不是不懂事理的人……好吧。我會寫張字條讓你們帶給院長。馬拉克十字鎮有間玻璃匠公會的辦事處，他們應該能幫上他的忙，不過我這是在動用我最後的人情了。我大概會因此丟了公會，不過這是為了一個朋友。

### (sub) DIAL_Z30#1719
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我相信他會心存感激的。謝謝你，米契爾。

### (sub) DIAL_Z30#1720
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [798..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1721
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [912..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Mitchel_Waylander_HASMET_Abbot_Graves

### (sub) DIAL_Z30#1722
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1723
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#1724
- speaker=31  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我現在真的沒空說話。我還有玻璃匠公會的事要處理，今晚天黑之前還有一大堆罐子要上釉。再見。

### (sub) DIAL_Z30#1725
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那祝你愉快。

### (sub) DIAL_Z30#1726
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [1374..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1727
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [1491..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Mitchel_Waylander_HASNOTMET_Abbot_Graves

### (sub) DIAL_Z30#1728
- speaker=0  style=0
- effects:
    - SET flag 0x7530=10
- branches:
    - [flag 0x1ec0 in [23770..32789]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1729
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1011 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那個男孩走了過來，加入他們。他站在他們面前，垂著眼低下頭。

### (sub) DIAL_Z30#1730
- speaker=32  style=0
- effects:
    - ?wOp12 a1=107 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們是……收容人嗎？

### (sub) DIAL_Z30#1731
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 收容人？你對他們了解多少？

### (sub) DIAL_Z30#1732
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我只知道卡羅魯斯師傅說過的話。他離開之前跟我說，總有一天收容人會來，把我帶去一個漂亮的地方，那裡的每個男孩都會跟我一樣，我就不用再擔心了，還說他得離開這件事我不該難過，因為他是要去一個很美好的地方，那裡的人也都跟他一樣。我試著不要害怕，可真的好難，師傅走了以後，我哭了好幾天，哭到頭都痛了。後來有一天，黑羊酒館那個人找到了我，說我可以幫他刷鍋子，直到收容人來帶我走為止。

### (sub) DIAL_Z30#1733
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你現在這位師傅，付你多少工錢？

### (sub) DIAL_Z30#1734
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 付我工錢？

### (sub) DIAL_Z30#1735
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 對，你的薪水——黑羊酒館那個人，給了你什麼作為報酬，讓你幫忙打掃、掃地、刷鍋子？

### (sub) DIAL_Z30#1736
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，他對我很好的，大人。他讓我跟雞一起睡在雞舍裡，這樣我就不會發抖著涼，還會給我還沒發霉的麵包吃。

### (sub) DIAL_Z30#1737
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這……真是太仁慈了。他在這裡嗎？

### (sub) DIAL_Z30#1738
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不在。他一週前出門去錫爾登辦事了。他說他很快就會回來，還說我可以睡在這間店裡。我忘了鎖門。

### (sub) DIAL_Z30#1739
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，那我們這就離開了。我要你在我們走後把店門鎖好，一直待在這裡，直到你師傅回來為止。等他回來，我要你告訴他，收容人很快就要來找ó他了，這是亞魯莎親王宮廷的洛克利爾紳爵說的。

### (sub) DIAL_Z30#1740
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [3339..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1741
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [3421..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C1_Jason

### (sub) DIAL_Z30#1742
- speaker=0  style=0
- branches:
    - [flag 0x1ec0 in [5940..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1743
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1011 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1744
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那個男孩走了過來，加入他們。他站在他們面前，垂著眼低下頭。

### (sub) DIAL_Z30#1745
- speaker=32  style=0
- effects:
    - ?wOp12 a1=107 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們……你們是要帶我走嗎？

### (sub) DIAL_Z30#1746
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們為什麼要那麼做？

### (sub) DIAL_Z30#1747
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 因為每次我打破東西，師傅都會說，會有人來把我帶去一個又壞又暗的地方，他們永遠不會給我東西吃，我也永遠見不到天日。我知道這裡所有人都被殺了以後，一定會有人來找我，把我帶去那個壞地方。

### (sub) DIAL_Z30#1748
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 傑森，你沒什麼好害怕的。不是你殺了那些人。這不是你的錯。

### (sub) DIAL_Z30#1749
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 師傅說，住在咱們屋簷下的人，都是咱們的責——責——責任，他們被殺的時候我就在這裡！這就表示是我的錯。

### (sub) DIAL_Z30#1750
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那麼，你看見兇殺過程了嗎？

### (sub) DIAL_Z30#1751
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有，可他們進來叫我離開，不然就要狠狠傷害我。他們沒告訴我他們要做什麼。

### (sub) DIAL_Z30#1752
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那些叫你離開的人長什麼樣子？

### (sub) DIAL_Z30#1753
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們個子很大，胸口上有鳥的圖案，像老鷹那樣。而且他們身上的味道很奇怪，有點像凱許來的水手身上有時候會有的那種味道。像花的味道……

### (sub) DIAL_Z30#1754
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 胸口上有鷹的圖案。這至少證實了夜鷹會牽涉其中……你知不知道一隻銀做的蜘蛛，或是被殺的其中一人可能帶著的黃銅望遠鏡？這非常重要。仔細想想。

### (sub) DIAL_Z30#1755
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我……我對那隻蜘蛛一無所知，不過我記得國王部隊裡有一個人有一根黃銅管子，兩端都嵌著小玻璃片，透過它我能看見很遠的東西。他說他跟另一個人是從錫爾登把它帶回來的。

### (sub) DIAL_Z30#1756
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他有說是在錫爾登哪裡弄到的嗎？

### (sub) DIAL_Z30#1757
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有……只說是在錫爾登。

### (sub) DIAL_Z30#1758
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你還能想起別的事嗎？在兇手出現之前，有沒有別人進來過黑羊酒館？

### (sub) DIAL_Z30#1759
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有個搬運工從『倒扣酒桶』給那些士兵送了些酒來。他跟我說這是特別送來的，除此之外，我想不起別的了……

### (sub) DIAL_Z30#1760
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你，傑森。我們晚點可能還會回來問你更多問題，所以別跑遠了。

### (sub) DIAL_Z30#1761
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [5854..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1762
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [5940..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Jason

### (sub) DIAL_Z30#1763
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1764
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那個男孩走了過來，加入他們。他站在他們面前，垂著眼低下頭。

### (sub) DIAL_Z30#1765
- speaker=32  style=0
- effects:
    - ?wOp12 a1=107 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你好。你們現在是要再問我更多問題嗎？

### (sub) DIAL_Z30#1766
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你有沒有聽說更多關於這樁謀殺案的事？

### (sub) DIAL_Z30#1767
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我只知道我師傅說這對生意不好，我們得『撞兔子』才能把客人找回來。

### (sub) DIAL_Z30#1768
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 撞兔子？這可是個新鮮的說法。好了，既然我們人都在這兒了，我想也該幫幫當地人。這裡有什麼吃的嗎？

### (sub) DIAL_Z30#1769
- speaker=32  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [6676..3]] -> node 4294901761
    - [flag 0x0101 in [6705..3]] -> node 4294901761
- text: 沒有新鮮的東西，不過要是你們有錢，我們有一般的口糧。

### (sub) DIAL_Z30#1770
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [7206..3]] -> node 65536
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1771
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們口糧就不用了。也許下次吧。

### (sub) DIAL_Z30#1772
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [6809..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1773
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [6903..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Jason_DONT_BUY

### (sub) DIAL_Z30#1774
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1775
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們要買一些。我們還有不少路要趕。

### (sub) DIAL_Z30#1776
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我去後面拿。

### (sub) DIAL_Z30#1777
- speaker=0  style=0
- effects:
    - SET flag 0x1ec0=1
    - END conversation, result=65534

### (sub) DIAL_Z30#1778
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7109..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1779
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7206..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Jason_ENOUGH_GOLD

### (sub) DIAL_Z30#1780
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1781
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來我話說得太早了。我手頭有點緊。也許下次吧。

### (sub) DIAL_Z30#1782
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 下次吧。好。再見。

### (sub) DIAL_Z30#1783
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了，傑森。保重。

### (sub) DIAL_Z30#1784
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7450..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1785
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7551..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Jason_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#1786
- speaker=0  style=0
- branches:
    - [flag 0x1ec0 in [8545..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1787
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1788
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那個男孩走了過來，加入他們。他站在他們面前，垂著眼低下頭。

### (sub) DIAL_Z30#1789
- speaker=32  style=0
- effects:
    - ?wOp12 a1=107 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有什麼我能幫你們拿的嗎？

### (sub) DIAL_Z30#1790
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你好，傑森。生意最近怎麼樣？我記得上次見面時，你還在擔心客人回不回得來。

### (sub) DIAL_Z30#1791
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 師傅很生氣，說他得把店關了，還要把我攆走，因為羅姆尼的人都嚇壞了。沒生意了。

### (sub) DIAL_Z30#1792
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們在怕什麼？

### (sub) DIAL_Z30#1793
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道，不過師傅說他們在害怕，而且他還不起債的時候，養不起一個蠢男孩。不過我猜他是對的，因為我確實很蠢，還一直花他的錢……

### (sub) DIAL_Z30#1794
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 傑森，聽到這件事我……真的很遺憾。真希望我們能幫上點忙。

### (sub) DIAL_Z30#1795
- speaker=32  style=0
- branches:
    - [flag 0x0100 in [8820..3]] -> node 4294901761
    - [flag 0x0101 in [8849..3]] -> node 4294901761
- text: 也許你們要是買點吃的，會有幫助。

### (sub) DIAL_Z30#1796
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1797
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那個男孩走了過來，加入他們……

### (sub) DIAL_Z30#1798
- speaker=32  style=0
- branches:
    - [flag 0x0100 in [8820..3]] -> node 4294901761
    - [flag 0x0101 in [8849..3]] -> node 4294901761
- text: 儲藏室裡還剩幾包口糧，你們要的話還有。要我去幫你們拿嗎？

### (sub) DIAL_Z30#1799
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [9481..3]] -> node 65536
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1800
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1801
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真希望我們能幫上忙，不過我看我們口糧就不用了。抱歉了，傑森。

### (sub) DIAL_Z30#1802
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係。也許你們下次可以買一些。

### (sub) DIAL_Z30#1803
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再見了，傑森。保重。

### (sub) DIAL_Z30#1804
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9107..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1805
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9198..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Jason_DONT_BUY

### (sub) DIAL_Z30#1806
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1807
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只要我們幫得上忙。我們要買一些。

### (sub) DIAL_Z30#1808
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我去儲藏室拿。

### (sub) DIAL_Z30#1809
- speaker=0  style=0
- effects:
    - SET flag 0x1ec0=1
    - END conversation, result=65534

### (sub) DIAL_Z30#1810
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9387..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1811
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9481..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Jason_ENOUGH_GOLD

### (sub) DIAL_Z30#1812
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1813
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真希望我們能幫上忙，不過我們手頭有點緊。抱歉了，傑森。

### (sub) DIAL_Z30#1814
- speaker=32  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係。也許你們下次可以買一些。

### (sub) DIAL_Z30#1815
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 保重，傑森。

### (sub) DIAL_Z30#1816
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [9729..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1817
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [9827..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Jason_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#1818
- speaker=0  style=0
- branches:
    - [flag 0x1ec1 in [11736..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1819
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1820
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾目光沒有離開路上那名陌生人，低聲喃喃道。「他穿著凱許人的服飾——這可能有點麻煩。要是我一聲令下，做好隨時行動的準備。」

### (sub) DIAL_Z30#1821
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼熱的天，站在太陽底下無遮無蔽地閒晃。我能猜你是在等人嗎？

### (sub) DIAL_Z30#1822
- speaker=33  style=0
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此。一位從馬拉克十字鎮來、要前往錫爾登的香料商人。我猜他的旅程想必是耽擱了。我們該在女皇客棧裡痛飲個一兩週才是。

### (sub) DIAL_Z30#1823
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是擔心這位商人會在錫爾登遇害嗎？

### (sub) DIAL_Z30#1824
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊！你這雙眼睛敏銳如鷹，一眼便看穿了問題所在——在那裡等著他的危險，並非專為他一人而設，也非針對任何單獨一人。每當爬行者召開他那些手下的祕密會議時，踏入錫爾登的陌生人，壽命都不長久。

### (sub) DIAL_Z30#1825
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那這個爬行者已經召開了這樣的會議？

### (sub) DIAL_Z30#1826
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此。兩晚前的黃昏，有人把一隻渡鴉釘在了錨首酒館的門柱上，這是個信號，告訴任何在錫爾登沒有正事要辦的人，該盡快離開這座城鎮。這樣的規矩，已經行之有年了。

### (sub) DIAL_Z30#1827
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那鎮上的治安官呢？他對這個罪犯就什麼都不做嗎？

### (sub) DIAL_Z30#1828
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在凱許有句話是這麼說的：眼中裝滿黃金的人看不見真相，心中藏著罪孽的人不願正視真相。

### (sub) DIAL_Z30#1829
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我明白了。  那我們這就繼續上路了，謝謝你告訴我們錫爾登的消息。

### (sub) DIAL_Z30#1830
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 記住，留意路上的標誌。除非必要，別再靠近錫爾登了，因為爬行者的手下擁有強大的『卡尊洛』——強大的力量。

### (sub) DIAL_Z30#1831
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你，阿布克。我們會記住你的警告。

### (sub) DIAL_Z30#1832
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [11651..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1833
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [11736..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Abuk

### (sub) DIAL_Z30#1834
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1835
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1836
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你還在等你的朋友嗎？

### (sub) DIAL_Z30#1837
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 正是如此。儘管我舌頭上起了水泡，腳上也長了膿瘡，我仍會等下去，直到太陽把我的血肉都曬乾，蛆蟲啃食我的腦子，即使到了那時，我也要等到有他的消息為止。

### (sub) DIAL_Z30#1838
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許他出了什麼事。

### (sub) DIAL_Z30#1839
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會等下去！謝謝你的關心，不過我不能就此放棄我對朋友的責任。一路順風，先生。

### (sub) DIAL_Z30#1840
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的。祝你好運。

### (sub) DIAL_Z30#1841
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [12541..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1842
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [12625..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Abuk

### (sub) DIAL_Z30#1843
- speaker=0  style=0
- branches:
    - [flag 0x1ec1 in [15192..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1844
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1845
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1846
- speaker=33  style=0
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 打擾了，兩位先生。我只耽誤你們一點時間。能指引我去萊頓的路嗎？我聽說那裡有人需要我的服務，去開一把韋伯鎖。我收到的那封信，聽起來十萬火急……

### (sub) DIAL_Z30#1847
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不可能。韋伯鎖是撬不開的。

### (sub) DIAL_Z30#1848
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 或許你辦不到，不過精通這門精細技藝的人，或許知道該如何攻破再困難的鎖。這只是耐心的問題。

### (sub) DIAL_Z30#1849
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我才不管你有多少耐心，韋伯鎖是撬不開的。你這是在說大話。

### (sub) DIAL_Z30#1850
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那阿布克跟陌生人說謊話，又能得到什麼好處呢，嗯？我說這些，只是想替自己打個廣告，好讓你們有朝一日能用得上我的服務。我陳述的不過是簡單的事實。在你們這個王國裡，沒有一把鎖是阿布克開不了的。一把都沒有。

### (sub) DIAL_Z30#1851
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？也許你能教我們怎麼撬開韋伯鎖。

### (sub) DIAL_Z30#1852
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這得花上比你們願意花的時間更多。我花了整整五年，在阿舜塔山的山蔭下，跟隨我的師傅卡里法德學習這門技藝。不過或許我能改善你們已經具備的技巧。區區七十枚金幣，應該就足以支付我的時間。

### (sub) DIAL_Z30#1853
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 七十枚金幣上一堂開鎖課？這根本跟搶劫沒兩樣。

### (sub) DIAL_Z30#1854
- speaker=33  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [16142..3]] -> node 4294901761
    - [flag 0x0101 in [14559..3]] -> node 4294901761
- text: 你真是精明。我不該這樣虧待自己。八十枚金幣，不過儘管你們對我如此敬重，我也不能再往上加價了。這樁交易，要成交嗎？

### (sub) DIAL_Z30#1855
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1856
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 人生中我喜歡的事情有很多，可浪費辛苦賺來的錢不在其中。任何自稱能撬開韋伯鎖的人，肯定都是騙子。

### (sub) DIAL_Z30#1857
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許你說得對。我會一邊在萊頓開一把鎖，一邊好好想想這些事。不過要是你改變主意，我們又剛好再相遇，我會樂意教你們一些我不可能知道的事。一路順風。

### (sub) DIAL_Z30#1858
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。祝你愉快。

### (sub) DIAL_Z30#1859
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [15097..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1860
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [15192..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Abuk_LESSON_NO

### (sub) DIAL_Z30#1861
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1862
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1863
- speaker=33  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [flag 0x0100 in [16142..3]] -> node 4294901761
    - [flag 0x0101 in [15672..3]] -> node 4294901761
- text: 親愛的朋友們！來吧，阿布克會教你們怎麼開鎖。我記得我們上次談定的價錢是八十枚金幣。現在要我教你們一課嗎？

### (sub) DIAL_Z30#1864
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1865
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就像我上次跟你說的，任何自稱能撬開韋伯鎖的人都是騙子。我才不會把錢白白扔掉。

### (sub) DIAL_Z30#1866
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你改變主意，我們又再相遇，我會再試著證明你是錯的。一路順風。

### (sub) DIAL_Z30#1867
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。祝你愉快。

### (sub) DIAL_Z30#1868
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [16048..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1869
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [16142..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Abuk_LESSON_NO

### (sub) DIAL_Z30#1870
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [16171..3]] -> node 4294901840
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1871
- speaker=0  style=0
- effects:
    - SET flag 0x1cf0=1
    - TAKE gold -800
    - RAISE Lockpick of party by 1536
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1872
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧，凱許人。八十枚金幣，不過我警告你……我很懷疑你有什麼東西能教我。

### (sub) DIAL_Z30#1873
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你必須向新事物敞開自己。這是第一課。不敞開自己，你就不完整。敞開自己，就像打開一把鎖。要是你打不開自己，那把鎖也可能打不開。你該明白，你自己跟你要開的那把鎖之間，並沒有差別。這一切，我會用隨身攜帶的一把試驗用鎖來示範給你看。現在，我要你仔細觀察……

### (sub) DIAL_Z30#1874
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 凱許人的……模稜兩可的鬼話。等等……你剛才是怎麼辦到的？我沒看清楚……再做一次。

### (sub) DIAL_Z30#1875
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是這樣。你已經上完了你的第一課，黑眼睛的孩子。

### (sub) DIAL_Z30#1876
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 太快了。我沒能看清楚你在做什麼。

### (sub) DIAL_Z30#1877
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 時候到了，你自然會明白發生了什麼事。在你心中，這段經歷終將解鎖，而你的雙手也會隨之解鎖。我該走了。再見。

### (sub) DIAL_Z30#1878
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等等……

### (sub) DIAL_Z30#1879
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [17256..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1880
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [17358..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：LESSON1_FROM_Abuk_ENOUGH_GOLD

### (sub) DIAL_Z30#1881
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1882
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我有錢，我肯定會讓你這個凱許人出出糗，可不巧的是，看來我手頭的金幣沒有我想得那麼多。

### (sub) DIAL_Z30#1883
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這確實很可惜，因為我倒是很希望有朝一日能被人比下去。也許等你手頭寬裕些，你可以再來，咱們互相較量一下。在那之前，祝你一路順風。

### (sub) DIAL_Z30#1884
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很期待我們再見面的那一天。再見。

### (sub) DIAL_Z30#1885
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [17827..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1886
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：LESSON1_FROM_Abuk_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#1887
- speaker=0  style=0
- branches:
    - [flag 0x1ecc in [17952..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1888
- speaker=0  style=0
- effects:
    - SET flag 0x1f38=1
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1889
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1890
- speaker=33  style=0
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 阿布克，開鎖大師，聽候差遣。有什麼我能幫上忙的？

### (sub) DIAL_Z30#1891
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來你不只精通開鎖而已。你對羅姆尼北邊的惡作劇石了解多少？

### (sub) DIAL_Z30#1892
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 錫爾登有張嘴巴不夠嚴實啊。看來我的生意恐怕保不住了。

### (sub) DIAL_Z30#1893
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我只對你賣給錫爾登喬夫塔茲的那支黃銅望遠鏡感興趣。跟我說說吧，我會選擇忘掉你可能參與過的其他偷竊勾當。你是怎麼弄到那支望遠鏡的？

### (sub) DIAL_Z30#1894
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 二十年前，我在錫爾登跟一個商人買了個箱子。他告訴我這箱子會帶給我大好運，可我只是想要個堅固的箱子來放我的東西，還跟他說，他要是賣掉這種箱子那才叫傻。我們討價還價了一番，最後我用十枚金幣買下了它，賣家對這個價錢似乎相當滿意。這筆交易我自己也很滿意，不過後來我開始納悶，自己到底買了個什麼樣的東西。這箱子帶著ó卡尊洛。

### (sub) DIAL_Z30#1895
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó卡尊洛？那是什麼意思？

### (sub) DIAL_Z30#1896
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是個充滿詭計、充滿魔法的箱子。箱子裡會出現一些東西，是我根本沒放進去的東西。後來有一天，我遇見一個羅姆尼來的人，他告訴了我這個箱子的真正本質。某個特定地點遺失的東西，會出現在我的箱子裡，我們便能把這些物品賣掉。我們當然也講好，絕不透露更多彼此的底細，這樣一來，要是我們其中一人出了事，這門生意還能安然無恙。

### (sub) DIAL_Z30#1897
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們倆會平分箱子裡出現的東西賣得的利潤。我猜這支黃銅望遠鏡，就是他安排讓你找到的其中一樣東西吧？

### (sub) DIAL_Z30#1898
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是眾多東西之一。

### (sub) DIAL_Z30#1899
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你拿到那支望遠鏡的那天，箱子裡還出現了別的東西嗎？

### (sub) DIAL_Z30#1900
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有幾樣東西。我不知道價值的東西都會留著，所以跟望遠鏡一起出現的那些物品，現在應該也還在。我記得好像有張字條，不過內容我不記得了。

### (sub) DIAL_Z30#1901
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個箱子在哪？離這裡近嗎？

### (sub) DIAL_Z30#1902
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 它就放在錫爾登附近一座山後面，跟另外兩個箱子放在一起，鎖著一把特殊的鎖。你得拼出Thorn這個字，才能把它打開。要是你聽不懂我在說什麼，等你找到箱子就會明白了。

### (sub) DIAL_Z30#1903
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: Thorn？我們會記住你的好意的。謝謝你。

### (sub) DIAL_Z30#1904
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [20679..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1905
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [20774..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C3_Abuk_HASMET_JOFTAZ

### (sub) DIAL_Z30#1906
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1907
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1908
- speaker=33  style=0
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 旅人，願陽光眷顧著你。我是錫爾登的阿布克，開鎖大師，卡爾德吉之子，卡里法德的學生，鎖匠中的鎖匠大師……

### (sub) DIAL_Z30#1909
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 省省吧。我目前不需要鎖匠。我需要打聽一支最近可能造訪過錫爾登的王國士兵部隊的消息。

### (sub) DIAL_Z30#1910
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 造訪錫爾登的士兵可多了。有些是從停靠的船上下來的，有些是從萊頓或更遠的地方來的。你要找的這些人，有什麼特徵能跟其他人區分開來？

### (sub) DIAL_Z30#1911
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你注意到他們，他們應該會顯得『刻意不起眼』。他們喝酒喝得不多，不管店家開價多離譜都會照付。他們會避免打鬥，除非被逼上梁山，而一旦動起手來，就會很明顯看出他們是身手不凡的戰士……

### (sub) DIAL_Z30#1912
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我認識這些人。他們來錫爾登是想雇刺客，不過阿布克告訴他們，他們用不著刺客。

### (sub) DIAL_Z30#1913
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 雇夜鷹會的人？不對。這些人應該是在找夜鷹會，可他們並不是想雇用他們。要說有什麼目的，他們反而是想把他們引出來……

### (sub) DIAL_Z30#1914
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們要阿布克幫忙雇刺客，可我跟他們說了我那隻蜘蛛的事，他們就不想雇刺客了。他們買下了那隻蜘蛛，然後就去羅姆尼了。

### (sub) DIAL_Z30#1915
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你把那隻銀蜘蛛賣給他們了？他們為什麼想買？

### (sub) DIAL_Z30#1916
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們沒告訴阿布克，我也沒問。我只是個開鎖大師，國王部隊的事是他們自己的事。

### (sub) DIAL_Z30#1917
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒人在指控你什麼。你這隻銀蜘蛛是打哪弄來的？是跟誰買的嗎？

### (sub) DIAL_Z30#1918
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有個刺客公會的人打聽到我收藏小小珍寶的地方，想打開它。他手藝相當高明，打開了那把奇特的鎖，卻被他不小心觸發的機關給當場擊斃。我在他身上找到那隻銀蜘蛛，便留了下來，直到後來賣給國王的士兵為止。

### (sub) DIAL_Z30#1919
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他們可能以為能用這東西追蹤夜鷹會。那個死掉的夜鷹會成員身上，還有沒有別的東西能透露他的身分？

### (sub) DIAL_Z30#1920
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他身上有一張搭乘『夜爬行者號』前往克朗多的船票，那是艘偶爾會在錫爾登靠港的船。我用不著，就把它扔了。

### (sub) DIAL_Z30#1921
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們目前該問的都問完了，阿布克，不過請你留在這裡。我們可能還需要再找你談談。

### (sub) DIAL_Z30#1922
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [23641..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1923
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [23739..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C3_Abuk_HASNOTMET_JOFTAZ

### (sub) DIAL_Z30#1924
- speaker=0  style=0
- branches:
    - [flag 0x1ec1 in [24658..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1925
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1926
- speaker=0  style=6
- effects:
    - (on-exit) play music 1024
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1927
- speaker=33  style=0
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 旅人，你好。我是阿布克，開鎖之人，靈魂的導師。我能為你效勞什麼？

### (sub) DIAL_Z30#1928
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說你是位老師。你有興趣教我們怎麼開鎖嗎？

### (sub) DIAL_Z30#1929
- speaker=33  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [25546..3]] -> node 4294901761
    - [flag 0x0101 in [24427..3]] -> node 4294901761
- text: 阿布克永遠對賺錢感興趣。我開價七十枚金幣。這個價錢你能接受嗎？

### (sub) DIAL_Z30#1930
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1931
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我得考慮一下你的提議。讓我想想。

### (sub) DIAL_Z30#1932
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24563..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1933
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24658..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Abuk_LESSON_NO

### (sub) DIAL_Z30#1934
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1935
- speaker=0  style=6
- effects:
    - (on-exit) play music 1024
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#1936
- speaker=33  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=93 a2=0
- branches:
    - [flag 0x0100 in [25546..3]] -> node 4294901761
    - [flag 0x0101 in [25124..3]] -> node 4294901761
- text: 年輕人，我仍然能增進你對鎖的了解。要是你還有興趣，我的價錢依然是七十枚金幣。要我教你嗎？

### (sub) DIAL_Z30#1937
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1938
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉，我的金子還有更值得花的地方。也許你能找到別人來教。

### (sub) DIAL_Z30#1939
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這對你來說是個可惜的選擇，不過我會尊重你的決定。一路順風。

### (sub) DIAL_Z30#1940
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 阿布克，我們的道路或許有朝一日還會再交會。在那之前……

### (sub) DIAL_Z30#1941
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [25452..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1942
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [25546..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Abuk_LESSON_NO

### (sub) DIAL_Z30#1943
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [25575..3]] -> node 4294901830
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1944
- speaker=0  style=0
- effects:
    - SET flag 0x1cf2=1
    - TAKE gold -700
    - RAISE Lockpick of party by 1280
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1945
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我曾把七十枚金幣花在更無趣的事情上。教我們吧。

### (sub) DIAL_Z30#1946
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你必須向新事物敞開自己。這是第一課。不敞開自己，你就不完整。敞開自己，就像打開一把鎖。要是你打不開自己，那把鎖也可能打不開。你該明白，你自己跟你要開的那把鎖之間，並沒有差別。這一切，我會用隨身攜帶的一把試驗用鎖來示範給你看。現在，我要你仔細觀察……

### (sub) DIAL_Z30#1947
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這法術遮掩得不太好。雖然我差點就沒發現。

### (sub) DIAL_Z30#1948
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 法……法術？這個詞阿布克不懂。也許你能教教我……

### (sub) DIAL_Z30#1949
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 剛才你用那把鎖示範的時候，我注意到你右手做了個很細微的動作——那是個施法手勢。你剛才施展了什麼樣的法術？

### (sub) DIAL_Z30#1950
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你觀察得真敏銳，不過我並非法師一族。我對卡尊洛一無所知，可我卻有這種……能力……我能把一粒知識的種子，種進另一個人肥沃的心田裡。不管怎樣，我已經照約定教了你們一些開鎖的技藝，咱們這筆交易依然算數。

### (sub) DIAL_Z30#1951
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 同意，不過要是你想保守這個祕密，給你個小建議。務必讓你的學生把目光都盯在那把鎖上。也許你該想個辦法，讓鎖冒出火花，或是把它漆成閃亮的顏色。我知道很多假冒法師的騙子，都是靠這一招，不讓人看清他們在做什麼。

### (sub) DIAL_Z30#1952
- speaker=33  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這次交流讓我們雙方都有所收穫。年輕的法師，謝謝你的建議。感激不盡。願你踏著清涼的沙，一路走向太陽。

### (sub) DIAL_Z30#1953
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 阿布克，我們的道路或許有朝一日還會再交會。在那之前……

### (sub) DIAL_Z30#1954
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27463..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1955
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27565..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：LESSON2_FROM_Abuk_ENOUGH_GOLD

### (sub) DIAL_Z30#1956
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1957
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這價錢很公道，可我話說得太早了。我沒有足夠的金子付你的服務費。也許改天吧。

### (sub) DIAL_Z30#1958
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27751..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1959
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：LESSON2_FROM_Abuk_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#1960
- speaker=0  style=0
- branches:
    - [flag 0x1ecf in [34145..3]] -> node 4294901761
    - [event_bitmap_hi[9] (xor=0x58 mask=0x7e mode=3 chapters=-)] -> node 4278256384
    - [event_bitmap_hi[9] (xor=0x06 mask=0x7a mode=3 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1961
- speaker=0  style=0
- effects:
    - event_bitmap_hi[9] bitop
    - apply status/condition to party idx=1 amt=-100
    - ?wOp12 a1=1019 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1962
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#1963
- speaker=34  style=0
- effects:
    - ?wOp12 a1=95 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們之中有人受了傷，需要照料。船應該很快就會回到這裡。我建議你們盡快尋求幫助……

### (sub) DIAL_Z30#1964
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這正是我們來的原因。錫爾登的船長說，這座島上能找到一位治療者幫助我們。

### (sub) DIAL_Z30#1965
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們得到的消息有誤。我不是頌神的祭司，而埃奧提斯只關心他海洋王國裡的子民。他只能代表他們行事。這正是至高無上的伊夏神所賦予他的使命。

### (sub) DIAL_Z30#1966
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我年輕的時候，有幸學過一些神殿運作的道理。我記得，一位神有時候能被說動，超出祂原本的職責範圍行事，只要換來相應的敬奉義務。

### (sub) DIAL_Z30#1967
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是真的，不過埃奧提斯如今已是昔日的影子。曾幾何時，在瓦爾赫魯與米德凱米亞諸神開戰之前，祂的影響力如海洋般深廣，涵蓋一切航行其上的事物。祂終於消失之後，基利安接掌了祂的領域，不過這裡仍殘留著祂本質的一絲餘韻。我們沒法跟一位已經消逝的神明溝通……

### (sub) DIAL_Z30#1968
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可要是我們代祂行事，你覺得祂會賜予我們恩惠嗎？

### (sub) DIAL_Z30#1969
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我無法得知。要是這裡殘留的不只是祂的一絲餘韻，或許我們還能與祂溝通，得知祂的心意，可我們埃奧提斯教團的人，不過是侍奉一位已然消逝的神明。我們只能從極其細微之處窺見祂的意志。

### (sub) DIAL_Z30#1970
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許我們來到這裡，正是為了服侍那份意志。我們能幫上你什麼忙？

### (sub) DIAL_Z30#1971
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看不出你們的請求有什麼壞處，不過我沒法保證你們的努力會成功還是失敗。我只能仰賴徵兆告訴我的事。或許埃奧提斯ñ會從沉睡中甦醒，賜下祂的恩惠。在那之前，ó迷霧ó惡魔號不會再帶你們來這座島了。

### (sub) DIAL_Z30#1972
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你至少能給我們個頭緒，告訴我們該從哪裡著手嗎？你或許能從一隻麻雀的墜落中讀出神的旨意，可我們有些人可沒那麼ó聰明……

### (sub) DIAL_Z30#1973
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 最近，有許多人告訴我們，有時徘徊在河邊的ó露莎卡水靈變得躁動不安。要是你們能找到牠們全部，並讓牠們得以安息，或許就能達成你們的目的。不過我得警告你們，這些伊萊亞姆的姊妹們大多狡猾，會想方設法隱藏自己的蹤跡。許多水靈都不願意被送進林斯克拉格瑪的殿堂。你們得夠機靈才能找到牠們……這是我的建議。

### (sub) DIAL_Z30#1974
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們魚貫走出內殿時，貝拉突然在他們身後雙膝跪地。他們連忙衝上前去，可等他們趕到她身邊時，她已經自己站了起來。  「抱歉，」她喘著氣說道。「埃奧提斯的觸動，有時候讓人難以承受。雖然我不明白這其中的含義，但你們身上有什麼東西引起了祂的興趣，今日祂對你們展露了笑顏。祝你們好運。」

### (sub) DIAL_Z30#1975
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [31142..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1976
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [31238..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：X_Beyla_NO_EORTIS_FAVOR

### (sub) DIAL_Z30#1977
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1018 a2=0
    - event_bitmap_hi[9] bitop
    - SET flag 0x1ecf=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1978
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#1979
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我已經期盼你們多日了。我的占卜顯示，蒙受埃奧提斯眷顧的陌生人，將會來到我們這裡，如今我便見到你們站在我面前。你們讓這位神明相當滿意。

### (sub) DIAL_Z30#1980
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們讓祂滿意了？我們到底ó做了什麼？

### (sub) DIAL_Z30#1981
- speaker=34  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [33300..3]] -> node 4294901761
    - [flag 0x0101 in [33721..3]] -> node 4294901761
- text: 這一點你們該比ó我更清楚。我沒辦法確知，只能猜想，你們的所作所為，在某種程度上，改善了那些住在海裡、或住在滋養海洋的河流裡的生靈的處境，那些正是我們的主宰曾經統治的領域。不過現在，我做了一個夢，受到指示要好好接待你們。深海泳者已經允許我賜予你們一項恩惠。只要你們活著的一天，你們之中任何人前來向我請求，都能治好任何困擾你們的病痛傷勢。這正是埃奧提斯恩惠的本質。你們之中有誰需要治療嗎？

### (sub) DIAL_Z30#1982
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1018 a2=0
    - SET flag 0x1ecf=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1983
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#1984
- speaker=34  style=0
- effects:
    - ?wOp12 a1=95 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我已經期盼你們多日了。我的占卜顯示，有蒙受埃奧提斯眷顧的陌生人存在。我猜想，你們想必已經完成了你們的儀式。

### (sub) DIAL_Z30#1985
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大祭司，這跟儀式沒什麼關係，反倒跟消滅亡靈脫不了關係……

### (sub) DIAL_Z30#1986
- speaker=34  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [33300..3]] -> node 4294901761
    - [flag 0x0101 in [33721..3]] -> node 4294901761
- text: 聽起來你們似乎有些苦惱。請放心，你們並沒有殺害任何人，而是解放了那些被不自然地束縛在這個世界上的靈魂……深海泳者對此深感欣慰，已允許我賜予你們一項恩惠。只要你們活著的一天，你們之中任何人前來向我請求，都能治好任何困擾你們的病痛傷勢。這正是埃奧提斯恩惠的本質。你們之中有誰需要治療嗎？

### (sub) DIAL_Z30#1987
- speaker=0  style=0
- effects:
    - HEAL party amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1988
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們有些傷勢，恐怕超出了我的治療能力。我們該怎麼做？

### (sub) DIAL_Z30#1989
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你會發現，我們說話的同時，你的病痛已經開始痊癒了。等ó迷霧ó惡魔號把你們送回錫爾登時，你會感到自己已經完全康復。

### (sub) DIAL_Z30#1990
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [33621..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1991
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33721..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：X_Beyla_FIRST_TIME_HEAL_YES

### (sub) DIAL_Z30#1992
- speaker=0  style=0
- effects:
    - GIVE gold +200
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1993
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們目前狀況還算不錯。謝謝你，貝拉。

### (sub) DIAL_Z30#1994
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不客氣，年輕的法師。我現在得回去處理神殿裡的事務了。我相信，即便沒有埃奧提斯的治療，你們也會發現幸運女神已經對你們展露了笑顏。

### (sub) DIAL_Z30#1995
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34046..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1996
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34145..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：X_Beyla_FIRST_TIME_HEAL_NO

### (sub) DIAL_Z30#1997
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1018 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#1998
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#1999
- speaker=34  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=95 a2=0
- branches:
    - [flag 0x0100 in [34474..3]] -> node 4294901761
    - [flag 0x0101 in [34900..3]] -> node 4294901761
- text: 當ó迷霧ó惡魔號靠近時，神殿裡的風鈴便響了起來。你們之中有誰受傷了嗎？

### (sub) DIAL_Z30#2000
- speaker=0  style=0
- effects:
    - HEAL party amt=100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2001
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們有些傷勢，恐怕超出了我的治療能力。我們該怎麼做？

### (sub) DIAL_Z30#2002
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你會發現，我們說話的同時，你的病痛已經開始痊癒了。等ó迷霧ó惡魔號把你們送回錫爾登時，你會感到自己已經完全康復。

### (sub) DIAL_Z30#2003
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34795..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2004
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34900..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：X_Beyla_SUBSEQUENTLY_INJURED_YES

### (sub) DIAL_Z30#2005
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2006
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們目前狀況還算不錯。謝謝你，貝拉。

### (sub) DIAL_Z30#2007
- speaker=34  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不客氣，年輕的法師。我現在得回去處理神殿裡的事務了。

### (sub) DIAL_Z30#2008
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [35122..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2009
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [35226..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：X_Beyla_SUBSEQUENTLY_INJURED_NO

### (sub) DIAL_Z30#2010
- speaker=0  style=0
- branches:
    - [flag 0x1ec3 in [37620..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2011
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1042 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2012
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2013
- speaker=35  style=0
- effects:
    - ?wOp12 a1=109 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們不是嘲弄幫的人！你們是……你們是從哪來的？！

### (sub) DIAL_Z30#2014
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從上面，從王宮來的。從克朗多。

### (sub) DIAL_Z30#2015
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 從上面來的？那你們是帕格的學生？他派你們下來幫我們的？

### (sub) DIAL_Z30#2016
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不是……

### (sub) DIAL_Z30#2017
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不明白。你們來這裡做什麼？

### (sub) DIAL_Z30#2018
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們認為帕格公爵知道有些法師住在克朗多的下水道裡，我們有事需要跟他們談談。你知道關於他們的事嗎？

### (sub) DIAL_Z30#2019
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒空管這個。我有東西非找到不可，而嘲弄幫正在徹底搜查這片下水道。要是被他們找到我，天亮的時候我就會浮在港灣裡了……

### (sub) DIAL_Z30#2020
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嘲弄幫或許在找你，可他們不會找我們。要是我們能找到你在找的東西，或許就能救你一命。作為交換，你回答我們幾個問題，半個鐘頭之內，你就能踏上前往薩斯、馬拉克十字鎮，或是任何你想去的地方的路了。

### (sub) DIAL_Z30#2021
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我怎麼知道你們不會讓盜賊公會的人埋伏等著抓我？

### (sub) DIAL_Z30#2022
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你沒法確定，不過就像你自己說的，沒有我們幫忙，你已經是個死人了。依我看，至少我們能給你一個不會落得埋進墳墓的選擇。咱們互相幫忙吧——告訴我你在找什麼。

### (sub) DIAL_Z30#2023
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一尊青銅雕像，我想它叫『拉蘇爾神像』。爬行者多年前從一個凱許人那裡聽說了一則關於這件東西的傳說——這正是他最初開始尋找法師輔佐自己的原因——據說它能賜予擁有者掌控健康的力量。傳說中，這尊神像原本在一艘於克朗多附近沉沒的船上，可爬行者相信它其實成功上了岸，最終在這座城市還屬於凱許的時候被埋在了這裡。

### (sub) DIAL_Z30#2024
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們把這尊雕像帶給你，你就會告訴我們需要知道的事？

### (sub) DIAL_Z30#2025
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我保證。你們需要知道的任何事。

### (sub) DIAL_Z30#2026
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [37536..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2027
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [37620..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Kat

### (sub) DIAL_Z30#2028
- speaker=0  style=0
- branches:
    - [flag 0xc35c in [38311..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2029
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1042 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2030
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝密室另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2031
- speaker=35  style=0
- effects:
    - ?wOp12 a1=109 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 過去這一個鐘頭裡，我已經三次聽見嘲弄幫的腳步聲了。神像在哪？

### (sub) DIAL_Z30#2032
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還沒找到。你得給我們點時間……

### (sub) DIAL_Z30#2033
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒時間給你們！我還活著，全靠爬行者教我的那點機靈。找到神像，不然咱們這筆交易就算了。

### (sub) DIAL_Z30#2034
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [38216..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2035
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [38311..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Kat_HAS_NO_IDOL

### (sub) DIAL_Z30#2036
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1042 a2=0
    - REMOVE item '\x0c' cond=0
    - SET flag 0x1ed1=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2037
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來。那名女子穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2038
- speaker=35  style=0
- effects:
    - ?wOp12 a1=109 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我能聽見嘲弄幫的人越來越近了。你們替我找到拉蘇爾神像了嗎？

### (sub) DIAL_Z30#2039
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你不擔心爬行者會濫用這尊神像嗎？靠著它，他可能會殺死成百上千的人，親王，甚至可能是國王。你確定你想把它交給他？

### (sub) DIAL_Z30#2040
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我就是指望他去用它。你知道，他並沒有把關於這尊神像的一切都打聽清楚。拉蘇爾神像確實會賜予擁有者掌控生命的力量，可米德凱米亞上沒有任何人能成為它真正的主人——拉蘇爾才是它的主人，而那不過是伊薩拉尼人對死亡女神林斯克拉格瑪的另一個稱呼。任何其他妄稱擁有它的人，都會在一個月內死去。

### (sub) DIAL_Z30#2041
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還以為你是替爬行者做事的！

### (sub) DIAL_Z30#2042
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有人真的是替爬行者做事的。圍繞在他身邊的那些人，不是出於恐懼就是欠了債，沒有一個是出於忠誠！我打算讓他的計畫徹底泡湯，不過我們沒時間談這個了。說回我們的交易。你們想知道什麼？

### (sub) DIAL_Z30#2043
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰是爬行者手下法師的頭領？

### (sub) DIAL_Z30#2044
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不確定，不過我認為是馬拉克十字鎮的葛雷夫斯院長。他曾以出色的抄寫員聞名，也曾受託處理來自星塢島的書籍，直到帕格發現了事情的真相為止。

### (sub) DIAL_Z30#2045
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，院長曾受託謄抄關於法術的書籍？

### (sub) DIAL_Z30#2046
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 各式各樣的書都有。正是他發現了拉蘇爾神像的真正本質，並把這個消息轉告給我的。

### (sub) DIAL_Z30#2047
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想你已經告訴我需要知道的事了。謝謝你，希望你……祝你一切順利。

### (sub) DIAL_Z30#2048
- speaker=35  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 到頭來，總是得在兩害之中取其輕，不是嗎。也許有朝一日，我們的選擇不會這麼艱難。再見了，孩子，也祝你好運。

### (sub) DIAL_Z30#2049
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40445..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2050
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [40537..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Kat_HAS_IDOL

### (sub) DIAL_Z30#2051
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[24] (xor=0x13 mask=0xb1 mode=3 chapters=-)] -> node 4278256128
    - [flag 0x1ec4 in [43355..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2052
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2053
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯停下了腳步。  他緊盯著歐文，等著這男孩解釋。「你拍了拍我的肩膀。你是想跟我說話？」戈拉斯低沉地問道。  「不，」一個聲音在他們身後應道。「ñ是我……」

### (sub) DIAL_Z30#2054
- speaker=36  style=0
- effects:
    - (on-exit) play sfx 122
- branches:
    - [always] -> node 0 (no jump)
- text: 我起初還以為自己看錯了，可現在我知道不是。你怎麼會在這裡？我聽說你的頭已經被插在薩薩戈斯城外的木樁上了。

### (sub) DIAL_Z30#2055
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 並非所有住在北疆的人都屈服於迪勒肯的意志。天意讓他派了一名守衛看守我的牢房，恰好是我的一位近親堂表兄弟，同情我的處境。他替我爭取到了逃脫的時間。

### (sub) DIAL_Z30#2056
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，如今是你堂表兄弟的頭顱代替你懸掛在那裡了……你肩上扛著一份沉重的責任啊。

### (sub) DIAL_Z30#2057
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡，這正是我更該終結迪勒肯統治的理由！他要用他的血來償還我的血；他每一次冒犯我的族人，我都要雙倍加諸在他的血肉之上。我不會給他任何喘息的機會，不會對他心慈手軟，也不會因為他對我們族人所做的一切而收手。我想你應該也會同意這一點吧，奧布卡！

### (sub) DIAL_Z30#2058
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戈拉斯，我對著他所殺害的一切亡魂之墓起誓，你的事業就是我的事業！不管我能怎麼幫你，你儘管開口就是。不過這些話說了也是白說。我們得先逃出這個地方，不然就沒有什麼可以復仇的了。

### (sub) DIAL_Z30#2059
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 先前被囚禁在這裡的一些人告訴過我，有一條地下河流，會匯入伊斯班迪河。

### (sub) DIAL_Z30#2060
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我親眼見過那條河，不過從那裡冒出來的煙氣，會奪走一個人的力氣。我偶爾會看見維努特里爾的一些手下戴著用骨頭跟布料做成的面罩……要是我們三個能弄到那種面罩，我相信我們就能成功逃脫。

### (sub) DIAL_Z30#2061
- speaker=0  style=0
- branches:
    - [flag 0xc3a9 in [42575..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2062
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 待在這裡。你要是離開這地方，恐怕會引來不必要的注意。我跟這男孩去找面罩，然後回來找你。

### (sub) DIAL_Z30#2063
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [42575..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2064
- speaker=0  style=0
- effects:
    - REMOVE item 'Y' cond=0
    - event_bitmap_hi[24] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2065
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那真是天意，我們已經弄到手了。拿去這個，順利逃出去吧。

### (sub) DIAL_Z30#2066
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來等迪勒肯這場戰事平息之後，北疆會有許多人得做出補償。

### (sub) DIAL_Z30#2067
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡，我對補償沒有興趣。薩薩戈斯的王座，我早已不做此想了。我夢想的，只是這場噩夢的終結。

### (sub) DIAL_Z30#2068
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可悲的是，最該領導眾人的人，往往最不想要這份責任。不過我不會強迫你接受你不想要的東西。戈拉斯，你是個高尚的人。

### (sub) DIAL_Z30#2069
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在這個瘋狂的世界裡，這只是小小的安慰。去吧，奧布卡，保重身體。我們分頭行動吧。

### (sub) DIAL_Z30#2070
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [43355..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2071
- speaker=0  style=0
- branches:
    - [flag 0xc3a9 in [44105..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2072
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2073
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡再度出現。  他看起來比上次見面時精神好上不少，@4猜想，逃脫的可能性，想必讓他重新找回了那份被困在洞穴裡好幾週所奪走的勇氣。就像他跟歐文一樣，他或許也開始看見了希望……

### (sub) DIAL_Z30#2074
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你把面罩帶回來了嗎？

### (sub) DIAL_Z30#2075
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不。我們在這片黑暗裡摸索，是有點困難。

### (sub) DIAL_Z30#2076
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們會習慣的。只需要一點時間……

### (sub) DIAL_Z30#2077
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我可沒打算ñ習慣ñ任何形式的囚禁。奧布卡，我們會找到那些面罩，把它們帶回來。我以性命擔保。在那之前，你可得活著……

### (sub) DIAL_Z30#2078
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
    - REMOVE item 'Y' cond=0
    - event_bitmap_hi[24] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2079
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡再度出現。  他看起來比上次見面時精神好上不少，@4猜想，逃脫的可能性，想必讓他重新找回了那份被困在洞穴裡好幾週所奪走的勇氣。就像他跟歐文一樣，他或許也開始看見了希望……

### (sub) DIAL_Z30#2080
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還沒能弄到面罩。你們那邊有比較順利嗎？

### (sub) DIAL_Z30#2081
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有。拿去這個，順利逃出去吧。我們也會這麼做的。

### (sub) DIAL_Z30#2082
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來等迪勒肯這場戰事平息之後，北疆會有許多人得做出補償。

### (sub) DIAL_Z30#2083
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡，我對補償沒有興趣。薩薩戈斯的王座，我早已不做此想了。我夢想的，只是這場噩夢的終結。

### (sub) DIAL_Z30#2084
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可悲的是，最該領導眾人的人，往往最不想要這份責任。不過我不會強迫你接受你不想要的東西。戈拉斯，你是個高尚的人。

### (sub) DIAL_Z30#2085
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在這個瘋狂的世界裡，這只是小小的安慰。去吧，奧布卡，保重身體。我們分頭行動吧。

### (sub) DIAL_Z30#2086
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45244..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2087
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [45331..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C4_Obkhar

### (sub) DIAL_Z30#2088
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2089
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4發現了奧布卡。  這名頭頂微禿的莫瑞德人抬眼瞥了他們一眼，神情茫然，隨即又低頭盯著自己腳邊的地面。

### (sub) DIAL_Z30#2090
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還以為你們已經走了……

### (sub) DIAL_Z30#2091
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在這片幽暗之中，我弄丟了自己的一件東西。只是個小玩意兒，不過我想在離開之前找到它。這用不著你們操心。請，走吧……

### (sub) DIAL_Z30#2092
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。朋友，我們有朝一日還會再見的。

### (sub) DIAL_Z30#2093
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45871..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2094
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [45978..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Obkhar_HAVEGIVEN_VAPOR_MASK

### (sub) DIAL_Z30#2095
- speaker=0  style=0
- branches:
    - [flag 0x1ec4 in [50923..32813]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2096
- speaker=0  style=0
- effects:
    - preload portraits 0x24,0x5,0x0,0x0
    - ?wOp12 a1=1025 a2=0
    - (on-exit) play sfx 122
- branches:
    - [always] -> node 0 (no jump)
- text: @4發出一聲驚呼。  他揉著頭上被重重一擊的地方，轉頭一看，發現@3跟@5也在做著同樣的動作。三人面面相覷，一臉困惑，誰都沒料到會突然冒出一個高大的莫瑞德人……

### (sub) DIAL_Z30#2097
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也遇上了麻煩。我是奧布卡。或許我們能互相幫忙。

### (sub) DIAL_Z30#2098
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這假設可不小啊。莫瑞德人，我看我們誰都沒有理由信任你。

### (sub) DIAL_Z30#2099
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 剛才你們都感受到我扔石頭的手法了，每一顆都輕輕鬆鬆打中了你們的頭，換成莫瑞德的飛刀也一樣容易。要是我存心要傷害你們，你們現在早就死了。

### (sub) DIAL_Z30#2100
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你王國語說得相當流利。當間諜挺方便的技能。

### (sub) DIAL_Z30#2101
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們只說自己的母語，就沒法跟從王國或更遠的地方來的商人做買賣了。看來學我們的語言，對他們來說似乎是件有失身分的事……

### (sub) DIAL_Z30#2102
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有道理。我還在聽……

### (sub) DIAL_Z30#2103
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯正利用一種裝置入侵這片森林。要是任由它繼續運作，對你們來說就意味著徹底的潰敗。要是迪勒肯達成了他的目標，他就會利用藏在賽瑟儂的那件東西，取得穆爾曼達穆斯當初沒能到手的力量。這對你們的王國、也對我的族人來說，都將意味著一場新的暴政。

### (sub) DIAL_Z30#2104
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這件裝置的事我們已經知道了。從一個攻打北衛城的野戰隊長口中逼問出來的。要是你真心想幫我們，就告訴我們去哪能找到那件裝置……

### (sub) DIAL_Z30#2105
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在一座河流交匯處的半島上。得穿過六賢者製造的一座假山幻象才能進去，不過從這裡出發，我也不確定確切位置在哪。自從我偷偷溜出營地以後，我一直在找一件魔法器物。

### (sub) DIAL_Z30#2106
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 器物？做什麼用的？

### (sub) DIAL_Z30#2107
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就在他們開始讓士兵通過裂界之門不久後，我發現這道門能被一種他們稱為『瓦尼』的東西給破壞掉，那是個我很陌生的詞。我在一個看守裂界之門的法師身上找到過這樣一件東西。在我殺了他之前，我發現要是把它扔進裂界之門的漩渦裡，就會讓那道門崩潰瓦解。我原本以為它已經被永久摧毀了。

### (sub) DIAL_Z30#2108
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迪勒肯的手裡花招還真不少。那，你覺得我們有可能再找到一件這種裝置嗎？

### (sub) DIAL_Z30#2109
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我殺那名法師之前打聽到的一點消息，製造裂界之門少不了這東西。要是有人打算搭一座橋，通常明智的做法，是多帶幾塊木板，以防其中一塊斷裂。

### (sub) DIAL_Z30#2110
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個假設聽起來挺合理。現在就只剩找到這個……瓦尼的問題了？誰會有這種東西？

### (sub) DIAL_Z30#2111
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有誰會知道，那就是後衛部隊的首領莫萊伍夫了。他正率領部隊，在這片森林南端一帶，為最後的總攻做準備。

### (sub) DIAL_Z30#2112
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我看是時候去找他談談了。

### (sub) DIAL_Z30#2113
- speaker=245  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 吉米，找他談談？你該不會是打算大搖大擺走上前去，直接跟他要那件能毀掉他整場戰役的裝置吧？

### (sub) DIAL_Z30#2114
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 至少也得先打聲招呼再說。我們就假扮成奎格人，希望他看不穿我們。這麼一片混亂之中，他不可能認得他麾下所有連隊裡的每一個人。

### (sub) DIAL_Z30#2115
- speaker=36  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好一場值得敬佩的賭局。我贊成。

### (sub) DIAL_Z30#2116
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽見沒，洛基？莫瑞德人都贊成了。這ñ肯定是個好主意。趁我還沒恢復理智之前，咱們快行動吧。再見了，奧布卡……

### (sub) DIAL_Z30#2117
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [49607..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2118
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [49690..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C7_Obkhar

### (sub) DIAL_Z30#2119
- speaker=0  style=0
- branches:
    - [flag 0x1e87 in [51517..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2120
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2121
- speaker=0  style=0
- effects:
    - ?wOp12 a1=76 a2=0
    - ?wOp12 a1=76 a2=0
    - play music 1006
- branches:
    - [always] -> node 0 (no jump)
- text: 因克林德爾山口響起了號角聲。  緊接著又是幾聲號角回應第一聲，沿著峽谷的彎道一路傳了開去，狹道兩側也開始浮現出人影。十來個散落各處的士兵，從岩石後方跟溝渠裡起身，響應著召集的號令。一名看起來約莫四十歲的男子，從一處先前未曾被注意到的洞口現身，笨重地從他的藏身處走了下來，見用不著這些守衛，便吹了聲口哨解散他們。

### (sub) DIAL_Z30#2122
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唉，紳爵，沒想到您這麼快又回到這一帶來了。說實話，我當時還在納悶，您那副被砍得傷痕累累的樣子，到底能不能撐到任何地方……

### (sub) DIAL_Z30#2123
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 芬恩中尉，您的部隊呢？他們怎麼沒在這個山口按規矩站崗？

### (sub) DIAL_Z30#2124
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恕我直言，紳爵，我們目前正忙著把自己從一團爛攤子裡挖出來。您跟那個莫瑞德人闖過這裡沒多久，一場白色尖嘯風暴不知從哪冒了出來，是我這十六年來見過最猛的暴風雪。往下十哩的谷地裡，山口埋在五呎深的積雪底下。我派了守衛去支援我們的前哨，可我不確定他們能起什麼作用。就跟想在苦海底下點菸斗差不多。

### (sub) DIAL_Z30#2125
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 完全沒辦法穿過因克林德爾山口了嗎？

### (sub) DIAL_Z30#2126
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 除非您是隻會鑽雪的鼴鼠，或是條火蜥龍，不然沒辦法，大人。不管是北疆那邊還是王國這邊的人，要是非得走這條路不可，那都得等上好一陣子了。

### (sub) DIAL_Z30#2127
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧，那就這樣了。我們得回頭了。保重，中尉。

### (sub) DIAL_Z30#2128
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [51432..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2129
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [51517..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Finn

### (sub) DIAL_Z30#2130
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2131
- speaker=0  style=0
- effects:
    - ?wOp12 a1=76 a2=0
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 號角聲宣告了這位中尉的到來。  芬恩從他那設在洞穴裡的指揮所走下來，一邊搖著頭，一邊把毛皮頭盔往下拉緊，蓋住耳朵。

### (sub) DIAL_Z30#2132
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，您想必是相信奇蹟的人，不過恐怕這天氣可沒那麼配合。因克林德爾山口依然凍得結結實實。我手下有一半的人凍傷得厲害，恐怕得花上三年才能把體內的寒氣驅乾淨。

### (sub) DIAL_Z30#2133
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說是過不去了？

### (sub) DIAL_Z30#2134
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是的，大人。很抱歉。您可以試試高堡的割岩隘口，或者北衛山口。

### (sub) DIAL_Z30#2135
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 該死的北疆寒冬。我看我們大概找不到任何通往北方的暢通路線了，不過還是謝謝你的建議。保重，中尉。

### (sub) DIAL_Z30#2136
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52359..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2137
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52443..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Finn

### (sub) DIAL_Z30#2138
- speaker=0  style=0
- branches:
    - [flag 0x1e87 in [53050..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2139
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2140
- speaker=0  style=0
- effects:
    - ?wOp12 a1=76 a2=0
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 號角聲宣告了這位中尉的到來。  芬恩從他那設在洞穴裡的指揮所走下來，一邊搖著頭，一邊把毛皮頭盔往下拉緊，蓋住耳朵。

### (sub) DIAL_Z30#2141
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 外頭那些積雪根本過不去。因克林德爾山口被堵死了，大概得等到春天，我們才能再次通行。

### (sub) DIAL_Z30#2142
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的消息，中尉。

### (sub) DIAL_Z30#2143
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52965..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2144
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [53050..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Finn

### (sub) DIAL_Z30#2145
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2146
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2147
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 外頭那些積雪根本過不去。因克林德爾山口被堵死了，大概得等到春天，我們才能通行。

### (sub) DIAL_Z30#2148
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 再次謝謝你的消息，中尉。

### (sub) DIAL_Z30#2149
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [53596..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2150
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [53680..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Finn

### (sub) DIAL_Z30#2151
- speaker=0  style=0
- branches:
    - [flag 0x1e87 in [55701..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2152
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2153
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2154
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，我不知道您來這裡做什麼，不過我看因克林德爾山口可不是什麼文明人會想待的地方。就連哈達提山民都裹緊衣物，朝亞邦南下避難了，我跟您說句實話。連哈達提人都想著要進城避難，那可真是冷到家了。

### (sub) DIAL_Z30#2155
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您想必就是芬恩中尉了。洛克利爾紳爵回克朗多之後，對您這支駐軍讚不絕口。聽聞您指揮官的死訊，我們深感遺憾。

### (sub) DIAL_Z30#2156
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這種事難免。我們在這兒屁股都對著莫瑞德人晾著，可沒空太多愁善感。太容易眼睜睜看著最好的朋友送命了，所以乾脆不交最好的朋友。當然，我們還是得互相依靠、彼此照應，不過……也就僅止於此了。我看您大老遠跑來，應該不是為了跟我說您對我們指揮官的死感到遺憾吧。紳爵，您需要什麼？

### (sub) DIAL_Z30#2157
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們原本在想往北走……

### (sub) DIAL_Z30#2158
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那可過不去。就算積雪開始融化了，那些該死的莫瑞德人還是引爆了什麼東西。炸塌了半座山的岩石，我們得花上一段時間才能清出一條路來。

### (sub) DIAL_Z30#2159
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你說『引爆』。他們是用那夫沙油嗎？

### (sub) DIAL_Z30#2160
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很有可能。他們一定是在岩石裡埋了一包包那種東西，就等著我們一從山口下來就給我們狠狠一擊。我猜他們那邊有人是在我們四處查探的時候給嚇著了。不管怎樣，短時間內誰都別想從這條路過去了。

### (sub) DIAL_Z30#2161
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的消息，中尉。

### (sub) DIAL_Z30#2162
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [55616..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2163
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [55701..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Finn

### (sub) DIAL_Z30#2164
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2165
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2166
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，希望您不是打算從這裡過去，因為因克林德爾山口現在還堵得跟酒罐子似的，密不透風。

### (sub) DIAL_Z30#2167
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我就怕是這樣。謝了，中尉。

### (sub) DIAL_Z30#2168
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [56218..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2169
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [56302..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Finn

### (sub) DIAL_Z30#2170
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
    - SET flag 0x7541=1
- branches:
    - [always] -> node 0 (no jump)
- text: 一名男子朝他們走了過來。  @3仍因剛才的戰鬥而喘著粗氣，勉強朝那名笨重地走近他們的王國士兵揮了揮手打招呼……

### (sub) DIAL_Z30#2171
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小子，你可真是我這輩子見過最走運的私生子了。要不是我們在山口下聽見了打鬥的聲響，我看那些哥布林現在早就在燉貴族肉湯了。差點就把你這位朋友給收拾了，幸好我看出他好像是站在你這邊打的。我實在搞不懂你跟這些莫瑞德人在北疆搞什麼名堂……

### (sub) DIAL_Z30#2172
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 麻煩您帶我們去見亞魯莎親王，這非常重要。

### (sub) DIAL_Z30#2173
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？！小子，你腦子讓寒氣給凍壞了吧。你憑什麼覺得我會放下職責，大老遠帶你去克朗多？

### (sub) DIAL_Z30#2174
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 亞魯莎親王不ó在克朗多。他很可能還跟他的克朗多長槍騎兵團，駐紮在賽瑟儂附近的幽暗林外。我們需要您護送我們前往他的營地。

### (sub) DIAL_Z30#2175
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他為什麼會在那？他又為什麼會想見一個男孩跟一個ó莫瑞德人？

### (sub) DIAL_Z30#2176
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 親王就是派我們去刺探他們的，行嗎？他們絕不會懷疑一個瘦巴巴的十九歲小子跟一個莫瑞德人，所以……這就是他派我們去的原因。我們握有一項針對王國的攻擊計畫情報，必須盡快送到他手上，這至關重要。

### (sub) DIAL_Z30#2177
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我怎麼知道你說的是實話？

### (sub) DIAL_Z30#2178
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你沒法確定，不過要是您不帶我們去，結果莫瑞德人攻陷了北衛城，您覺得自己以後還睡得安穩嗎？

### (sub) DIAL_Z30#2179
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不得不承認你這一點。你要是個賭徒，下注可真不手軟……好了，咱們走吧。幽暗林離這兒可有得走了，親王也不會想乾等。我們走。

### (sub) DIAL_Z30#2180
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 中尉，趕緊帶我們離開這鬼地方吧。越快越好。

### (sub) DIAL_Z30#2181
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [58238..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2182
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [58319..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C4_Finn

### (sub) DIAL_Z30#2183
- speaker=0  style=0
- branches:
    - [flag 0x1e87 in [59814..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2184
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2185
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2186
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們兩個怎麼又跑回這兒來了？亞魯莎親王又派你們執行什麼祕密任務？

### (sub) DIAL_Z30#2187
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 算是吧……我們在找一本遺失的書。

### (sub) DIAL_Z30#2188
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，就咱們私下聊聊，你不覺得在這種地方找書，未免也太奇怪了嗎？我們這些人可沒機會安安穩穩坐下來看本書，至於莫瑞德人嘛……我看偷書大概也排不上他們優先事項的前幾名。

### (sub) DIAL_Z30#2189
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 因克林德爾山口能通行了嗎？

### (sub) DIAL_Z30#2190
- speaker=37  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們兩個要嘛是自討苦吃，要嘛就是真的不太靈光……不，因克林德爾山口沒開通。幾週前，他們又把它給炸封了。我個人是覺得，乾脆讓那該死的地方就這麼封著算了，不過軍令就是軍令，所以我的人又開始清理起來了。我不知道萊亞姆王為什麼這麼堅持要保持通往阿曼加的道路暢通，不過話說回來，追究原因也輪不到我。

### (sub) DIAL_Z30#2191
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你的消息，芬恩中尉。

### (sub) DIAL_Z30#2192
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [59729..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2193
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [59814..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Finn

### (sub) DIAL_Z30#2194
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1006 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2195
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2196
- speaker=37  style=0
- effects:
    - ?wOp12 a1=103 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 因克林德爾山口封閉了……聽清楚了……封閉了。這表示你跟你這位莫瑞德朋友，要是鐵了心非去北邊不可，就得另尋他路了。

### (sub) DIAL_Z30#2197
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該再次上路了。謝謝你撥空，芬恩。

### (sub) DIAL_Z30#2198
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [60413..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2199
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [60497..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Finn

### (sub) DIAL_Z30#2200
- speaker=0  style=0
- branches:
    - [flag 0x1f39 in [63733..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2201
- speaker=0  style=0
- branches:
    - [flag 0x1ec5 in [63109..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2202
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2203
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4發現田裡有個男人。  他彎著腰，看起來像是某種農夫，不過隨著他們越走越近，他的動作似乎變得更加勤快。無疑地，他也看見了他們……

### (sub) DIAL_Z30#2204
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這塊小田地經營得挺不錯的嘛。

### (sub) DIAL_Z30#2205
- speaker=38  style=0
- effects:
    - play sfx 114
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你喜歡翻土犁地，我想是吧。我好幾次都動過要賣掉的念頭。最近這裡發生的事，我是越看越不順眼。搞不好我真會像我一直跟大家說的那樣，把這一切全賣了。當然，我也不指望你這種養尊處優的小子能懂。

### (sub) DIAL_Z30#2206
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大概是不懂，不過這片地看起來這麼好，放棄未免可惜。你為什麼會想賣掉呢？

### (sub) DIAL_Z30#2207
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰都知道賽瑟儂戰役發生了什麼邪惡的事，絕對不是什麼自然的東西。我自己，以前就住在鎮中心，後來萊亞姆王出錢要我搬走。我當時對搬家沒想太多，只以為那股邪氣會留在那邊不出來。

### (sub) DIAL_Z30#2208
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 難道不是嗎？它正沿著那條路從賽瑟儂爬過來？

### (sub) DIAL_Z30#2209
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 聽著，小子，我可不喜歡你這種態度。你也許讀過不少書，可那不代表你就懂這個世界。你要是識相，就離賽瑟儂遠一點，能拉多少人跟你一起走就拉多少人。這一帶有什麼邪惡的東西，等它終於到來的時候，我可不想還待在這兒。

### (sub) DIAL_Z30#2210
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那，你這塊地想賣多少錢？

### (sub) DIAL_Z30#2211
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我……呃……什麼？

### (sub) DIAL_Z30#2212
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是這股邪氣真的迫在眉睫，你又急著想遠離它，那我倒是有興趣買下你這塊小地。我可不怕鬼。你打算賣我多少錢？

### (sub) DIAL_Z30#2213
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，我其實還沒真正決定要搬……你知道，不能本末倒置嘛……我大概還得過一陣子才會賣，你知道的……不想急著做決定。

### (sub) DIAL_Z30#2214
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你對緊鄰你這塊地的那片地了解嗎？有在賣嗎？

### (sub) DIAL_Z30#2215
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃，沒有，現在沒在賣了。老寡婦佩特魯姆搬走的時候，我把它買下來了……

### (sub) DIAL_Z30#2216
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 買下來了？我還以為你說你想搬家？

### (sub) DIAL_Z30#2217
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是想搬……聽著，我沒空整天站在這兒聊天。你要是對那塊地有興趣，自己去看看吧——只是別靠近我這塊地就行了。好了，我還有事要忙。祝你愉快。

### (sub) DIAL_Z30#2218
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 祝您愉快，先生。

### (sub) DIAL_Z30#2219
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [63018..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2220
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [63109..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_CX_Max_Feeber

### (sub) DIAL_Z30#2221
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2222
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 這名農夫仍在田裡。  他滿臉狐疑地抬頭望向他們，用手背抹開沾滿汗水、擋住眼睛的頭髮，等在原地。隨著他們越走越近，他瞇起了眼。他看起來不太歡迎訪客。

### (sub) DIAL_Z30#2223
- speaker=38  style=0
- effects:
    - ?wOp12 a1=114 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我一直在考慮你買我這塊地的提議，不過還沒決定……改天再來，我們再談吧。

### (sub) DIAL_Z30#2224
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會再來的。

### (sub) DIAL_Z30#2225
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [63627..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2226
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [63733..3]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_CX_Max_Feeber_CLOTH_NOT_FOUND

### (sub) DIAL_Z30#2227
- speaker=0  style=0
- branches:
    - [flag 0x1ec5 in [64314..3]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2228
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
    - event_bitmap_hi[8] bitop
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2229
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4發現田裡有個男人。  他彎著腰，看起來像是某種農夫，不過隨著他們越走越近，他的動作似乎變得更加勤快。無疑地，他也看見了他們……

### (sub) DIAL_Z30#2230
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你知不知道附近那間房子住著誰？

### (sub) DIAL_Z30#2231
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我當然知道。我大半輩子都住在那裡。我叫麥克斯．費伯。

### (sub) DIAL_Z30#2232
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你確定嗎？

### (sub) DIAL_Z30#2233
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小子，你腦子有毛病嗎？我當然確定。我怎麼可能不確定？

### (sub) DIAL_Z30#2234
- speaker=0  style=0
- effects:
    - event_bitmap_hi[8] bitop
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2235
- speaker=0  style=6
- effects:
    - (on-exit) play sfx 114
- branches:
    - [always] -> node 0 (no jump)
- text: 這名農夫仍在田裡。  他滿臉狐疑地抬頭望向他們，用手背抹開沾滿汗水、擋住眼睛的頭髮，等在原地。隨著他們越走越近，他瞇起了眼。他看起來不太歡迎訪客。

### (sub) DIAL_Z30#2236
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是不是常有去墓地挖掘的習慣？

### (sub) DIAL_Z30#2237
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這話什麼意思？

### (sub) DIAL_Z30#2238
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我是說，我們三個找到了一塊裹屍布，我們認為這一帶所有的邪祟之事都跟你脫不了關係。你一直在褻瀆墳墓，對吧？

### (sub) DIAL_Z30#2239
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們闖進了我家！我要為這件事去告訴治安官！

### (sub) DIAL_Z30#2240
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是他還住在鎮上，我或許還會覺得有點威脅，不過我猜你大概早就把他嚇跑了。快說，不然我就要去找我一個朋友，好好聊聊了——他叫尼維克，亞魯莎親王的稅務官——人很不錯。我看你們倆一定能處得非常融洽。

### (sub) DIAL_Z30#2241
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一座墳！我就只挖了一座墳而已！那傢伙的名字我現在也不記得了，不過他以前是六趾客棧的老闆，後來妮雅才接手那間店的。我想說也許能把她嚇跑，好讓她把店賣給我，可她這人固執得要命。

### (sub) DIAL_Z30#2242
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你把屍體怎麼處理了？

### (sub) DIAL_Z30#2243
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哪來的屍體！他早就只剩一副骨架了。我試著把他重新埋回去，可他有隻手一直找不著。那隻手肯定就在墓地附近。我想我大概是在老赫歇爾家附近的時候把它弄丟的……

### (sub) DIAL_Z30#2244
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還有別的嗎？

### (sub) DIAL_Z30#2245
- speaker=38  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就這樣。我知道的就這些了！我發誓。挖出來，然後又埋回去。

### (sub) DIAL_Z30#2246
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們得去找到那隻手，把它埋了。這可不是託你的福。再見了，先生，我勸你以後離六趾客棧遠一點。我看你在那兒大概不會受到什麼熱烈歡迎。

### (sub) DIAL_Z30#2247
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [730..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2248
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [832..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_CX_Max_Feeber_CLOTH_FOUND

### (sub) DIAL_Z30#2249
- speaker=0  style=0
- branches:
    - [flag 0x1ec6 in [2526..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2250
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2251
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2252
- speaker=39  style=0
- effects:
    - ?wOp12 a1=125 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的老天，我們的請願終於有人聽見了！親王的人總算來了一個！你們是為了……啊！你們帶了個精靈！

### (sub) DIAL_Z30#2253
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 索爾加斯看起來雖然嚇人，不過我向您保證，他對您不會有任何危險。好心的夫人，您說的這個請願是怎麼回事？

### (sub) DIAL_Z30#2254
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只要他還在這兒，我這輩子就一個字也不會再多說，這是真話。一個字也不多說！

### (sub) DIAL_Z30#2255
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾，我先讓你去辦你的事。要是需要我，我就在附近……

### (sub) DIAL_Z30#2256
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝您。  他已經走了，現在……您有什麼理由要請求亞魯莎親王的援助？

### (sub) DIAL_Z30#2257
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我派人去找親王，是因為賽瑟儂那邊得有人出面處理才行！要是他願意聽我們說話，他就會聽見林子裡到底發生了什麼事。那裡有光，可怕的、駭人的精靈之光，在林子裡出沒，而且每次出現，總是預示著某種災禍……

### (sub) DIAL_Z30#2258
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這些想必只是傳說罷了……

### (sub) DIAL_Z30#2259
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是這是傳說，那也是明事理的人親口說的傳說！我親眼看見過這些光，看著它們在夜裡跳著惡魔般的舞，就在那時，我丈夫昏死過去，嚥下了最後一口氣。那裡有某種可怕的邪惡存在。

### (sub) DIAL_Z30#2260
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不會做出任何承諾，不過我們會盡力而為。

### (sub) DIAL_Z30#2261
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [2438..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2262
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [2526..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Petrumh

### (sub) DIAL_Z30#2263
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2264
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2265
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 告訴我你帶了一百個克朗多長槍騎兵來，我就敬你身體健康！

### (sub) DIAL_Z30#2266
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好心的夫人，我還沒機會回克朗多呢。要是您能給我……

### (sub) DIAL_Z30#2267
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 紳爵，再見了……

### (sub) DIAL_Z30#2268
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等等……我們還沒……唉，這個糊塗的老太婆。

### (sub) DIAL_Z30#2269
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [3079..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2270
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [3166..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Petrumh

### (sub) DIAL_Z30#2271
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2272
- speaker=0  style=0
- branches:
    - [flag 0x1ed2 in [7996..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2273
- speaker=0  style=0
- branches:
    - [flag 0x1ec6 in [6009..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2274
- speaker=0  style=0
- effects:
    - SET flag 0x0052=1
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2275
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2276
- speaker=39  style=0
- effects:
    - ?wOp12 a1=125 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 萊斯爾，你這身衣服是打哪弄來的？肯定是從哪個侯爵身上順來的吧！你膽子是越來越大了啊？

### (sub) DIAL_Z30#2277
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕您認錯人了。我叫詹姆士……

### (sub) DIAL_Z30#2278
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 叫詹姆士是吧？哈哈，那當然囉！那我大概也不是你外婆佩特魯姆了，我猜。你又在ó裝模作樣了！這該不會跟你那次在馬拉克十字鎮裝乞丐、嚼肥皂裝瘋整整一個月一樣吧？噢，不過那齣戲你可賺了不少金幣！嘴裡吐著滿嘴白沫，誰都會以為你得了爬行瘋病，肯花大錢打發你走人！萊斯爾，你一直都是個狡猾的傢伙。有沒有順點麵包回來給我？

### (sub) DIAL_Z30#2279
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你為什麼不能自己買麵包？

### (sub) DIAL_Z30#2280
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰惹你不高興了，嗯？你明明清楚，傑克死了以後我就什麼都沒有了……除非……小子，你跟個精靈混在一起做什麼！你不知道他們會招來厄運嗎？！就是他們殺了傑克，還在賽瑟儂那邊惹出了一堆麻煩事！你腦子是進水了嗎？你瘋了不成？

### (sub) DIAL_Z30#2281
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 夫人，您說的賽瑟儂那邊的麻煩事，是指什麼？

### (sub) DIAL_Z30#2282
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你……你真的不是萊斯爾，是吧？可你長得跟他一模一樣啊。這怎麼可能，除非……是某種精靈的邪術，對不對？就是這樣！某種精靈魔法，你終於是為了我來的！還變成了萊斯爾的模樣！

### (sub) DIAL_Z30#2283
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小姐，我們不是走陰暗之道的邪徒。請相信我們。也許我跟您說的這位萊斯爾長得有幾分相似，不過我們只是普通人。不過，我倒是很想跟萊斯爾談談。聽起來……聽起來他可能是我的親人。

### (sub) DIAL_Z30#2284
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唔。我看你不太像邪惡的精靈……至少不像我聽說過的那種。這麼說，萊斯爾可能是你哥哥？

### (sub) DIAL_Z30#2285
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道。我從沒見過我父親，我母親也從沒提過有個雙胞胎，可我在克朗多被囚禁的時候，幾個看守我的人一直問我一些我從沒去過的地方、和從沒見過的人。一開始我想把他們說的話當耳邊風，可後來我想起了賽瑟儂戰役之前發生的一些事。有人曾試圖安插一個亞魯莎親王的替身。也許莫瑞德人正在故技重施。

### (sub) DIAL_Z30#2286
- speaker=39  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [6392..4]] -> node 4294901761
    - [flag 0x0101 in [7497..4]] -> node 4294901761
- text: 這一切都挺有意思的，不過我已經好幾天沒吃東西了。你們能不能勻點吃的給我？

### (sub) DIAL_Z30#2287
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2288
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2289
- speaker=39  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [6392..4]] -> node 4294901761
    - [flag 0x0101 in [7497..4]] -> node 4294901761
- text: 這麼說，這位大人的心腸不是石頭做的囉？回來幫老佩特魯姆婆婆了？能不能分點你們的口糧給我，今天我就不用出去乞討了？

### (sub) DIAL_Z30#2290
- speaker=0  style=0
- branches:
    - [flag 0xc398 in [6421..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2291
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
    - consume party items kind=0x48 x1
    - SET flag 0x1ed2=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2292
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這裡有包口糧可以給你，前提是你多跟我們說說這個萊斯爾的事。

### (sub) DIAL_Z30#2293
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我最後一次見到他，他正朝萊頓去。說是要去見那邊的幾位先生什麼的。他多半會避開主要道路走。不管他再怎麼小心，他就是有那種三不五時惹上麻煩的毛病。

### (sub) DIAL_Z30#2294
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝妳，小姐。照顧好自己。

### (sub) DIAL_Z30#2295
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [6941..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2296
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7059..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Petrumh_NOT_FED_YES_GIVE_FOOD_HAS_RATIONS

### (sub) DIAL_Z30#2297
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2298
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的口糧好像用完了。抱歉……

### (sub) DIAL_Z30#2299
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士，你這抱歉還比不上我一半呢。我今天的麵包還沒著落，所以還請你別再打擾我了。祝你愉快。

### (sub) DIAL_Z30#2300
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉了，夫人。我們不打擾您了。

### (sub) DIAL_Z30#2301
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7376..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2302
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7497..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Petrumh_NOT_FED_YES_GIVE_FOOD_HAS_NO_RATIONS

### (sub) DIAL_Z30#2303
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2304
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我目前抽不出任何口糧。

### (sub) DIAL_Z30#2305
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這話說得可真像個真正的大人物，跟那些在伊夏神修道院唸書的臭小子一個樣。我真不知道自己怎麼會犯下這種錯，把你錯認成我那善良的萊斯爾。祝你愉快。

### (sub) DIAL_Z30#2306
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 抱歉了，夫人。也許店主能勻頓飯給您。

### (sub) DIAL_Z30#2307
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [7891..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2308
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [7996..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Petrumh_NOT_FED_NO_GIVE_FOOD

### (sub) DIAL_Z30#2309
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2310
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 佩特魯姆皺起了眉頭。  「我這不是在吃嗎？」佩特魯姆一邊說，一邊把麵包塞進她那沒剩幾顆牙的嘴裡。「我身體也沒好到能一直被人打斷吃飯。請容我安安靜靜地嚼完這口飯。」

### (sub) DIAL_Z30#2311
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [8279..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2312
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [8367..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Petrumh_FED

### (sub) DIAL_Z30#2313
- speaker=0  style=0
- effects:
    - event_bitmap_hi[34] bitop
    - SET flag 0x005d=1
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2314
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 一名女子正沿著路走著。  從她的步伐，以及不時回頭張望的樣子看來，她似乎擔心有人正在追她。@4擔心這名女子可能身陷危險，便出聲喊住了她……

### (sub) DIAL_Z30#2315
- speaker=39  style=0
- effects:
    - ?wOp12 a1=125 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們在這條路上做什麼！該不會是想進馬拉克十字鎮吧？

### (sub) DIAL_Z30#2316
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實……

### (sub) DIAL_Z30#2317
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊夏神修道院的院長背叛了他的學生跟他的鎮子，現在那裡被某種怪物給圍困住了！我早該知道自己躲不過那股扳倒賽瑟儂的邪惡！你這位精靈朋友，大概也脫不了干係！

### (sub) DIAL_Z30#2318
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我向您保證，戈拉斯跟這件事一點關係都沒有。這些怪物到底是什麼？牠們為什麼偏偏要攻擊馬拉克十字鎮？

### (sub) DIAL_Z30#2319
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們要是珍惜自己的性命，就該幫村民找到院長，把他的頭插在木樁上送去給那些……蛇人！牠們保證，只要把院長交出去，就會放過其他所有人。

### (sub) DIAL_Z30#2320
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是牠們真是某種怪物，您憑什麼認為牠們殺了院長就會善罷甘休？

### (sub) DIAL_Z30#2321
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰知道呢？至於我自己，我要去黑沼鎮好好喝上……  噢，天啊，我把我的麥酒忘在馬拉克十字鎮的王后街了！這下我好幾個禮拜都沒酒喝了，除非……除非你們這幾個勇敢的、ó有膽識的小夥子肯幫我去拿回來！

### (sub) DIAL_Z30#2322
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們手頭還有不少別的事要處理……

### (sub) DIAL_Z30#2323
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，拜託嘛。這能讓一個老太婆的日子亮堂一點，尤其是一個已經沒了好好一個家的老太婆。你們要是拿到了，可以送到我朋友尤拉姆在黑沼鎮的家……我暫時會待在那裡。

### (sub) DIAL_Z30#2324
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會看看能做些什麼，不過我不能ó向您保證什麼。

### (sub) DIAL_Z30#2325
- speaker=39  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這樣就好，親愛的，這樣就很好了。那就到時候見了。記得我朋友的名字是ó尤拉姆。祝你們一路順風。

### (sub) DIAL_Z30#2326
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也是。去黑沼鎮的路上小心點……

### (sub) DIAL_Z30#2327
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [10537..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2328
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [10621..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Petrumh

### (sub) DIAL_Z30#2329
- speaker=0  style=0
- branches:
    - [flag 0x1ec7 in [12380..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2330
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2331
- speaker=0  style=6
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名矮人吸了口菸斗。  裊裊菸霧從這位老頭子嘴裡緩緩吐出，他的目光在洛克利爾、歐文跟戈拉斯身上輪流打量。儘管他早年因莫瑞德人的一劍失去了左眼的視力，但他那濃密眉毛下的右眼，依然炯炯有神。

### (sub) DIAL_Z30#2332
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 矮人這輩子不會忘記自己的名字，連帶著我也認得出，眼前這個健壯的年輕人，我上次見到的時候還是個孩子。

### (sub) DIAL_Z30#2333
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 無意冒犯，不過恐怕我想不起這個場合了。

### (sub) DIAL_Z30#2334
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 跟你們人類同胞一個樣……你們誰都記不住一個禮拜以前的事。要不是有我們精明的矮人，你們大概連自己有個王國都忘了！賽瑟儂戰役的時候，我把你跟二十來個婦女從一間地窖裡救出來的！洛基，你不記得我了嗎？

### (sub) DIAL_Z30#2335
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴，當然記得！很高興見到你！沒了眼罩，我都認不出你了。

### (sub) DIAL_Z30#2336
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 矮人還能怎麼辦？這道傷疤是我堂堂正正贏來的，我要是再把它遮起來，那我就是龍他媽了。當初就不該遮著。現在我就坐在這兒，跟那個瘋瘋癲癲的圖蘭尼酒保閒聊，喝上幾杯啤酒。反正麥克莫丹卡達爾整個塌了，也沒什麼事好做。  聽說下面出現了一隻布拉克努爾。要是照老規矩，誰宰了牠肯定會有一筆豐厚的賞金。就算以矮人的標準來看，這也是個不小的挑戰，因為牠們可是兇猛得很的怪物。

### (sub) DIAL_Z30#2337
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我聽說過這種石頭生物的傳說。謝謝你，杜巴。

### (sub) DIAL_Z30#2338
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [12286..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2339
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [12380..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Dubal_An_Loch

### (sub) DIAL_Z30#2340
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2341
- speaker=0  style=6
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名矮人朝他們皺起了眉頭。  他顯然打定主意暫時不打算離開這張凳子，只顧著使勁抽著菸斗。「勞煩兩位行行好，我倒寧可你們別來煩我。矮人抽菸斗是件神聖的事，酒館就是他的神殿。也許我們晚點再聊。」

### (sub) DIAL_Z30#2342
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [12765..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2343
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [12858..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Dubal_An_Loch

### (sub) DIAL_Z30#2344
- speaker=0  style=0
- branches:
    - [flag 0x1ec7 in [14977..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2345
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2346
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  這名矮人走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2347
- speaker=40  style=0
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小子，你還挺看得起自己的嘛，是吧？

### (sub) DIAL_Z30#2348
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧。你為什麼會這麼想？

### (sub) DIAL_Z30#2349
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大多數人進房間，都會先看看左邊、看看右邊，摸清楚這地方的格局，再決定往哪走。可你大搖大擺地進來，直直往前走，活像沒什麼能擋在你面前似的。會這麼做的人，要嘛是蠢，要嘛就是耍刀的本事非常了得。

### (sub) DIAL_Z30#2350
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不蠢。

### (sub) DIAL_Z30#2351
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也沒這麼覺得，不過我敢拿一個月的薪水打賭，你當過一陣子小偷。

### (sub) DIAL_Z30#2352
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我建議你下重注。你會贏的。不過那都是很久以前的事了。我現在為親王效力。

### (sub) DIAL_Z30#2353
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是嗎？那還真有點可惜。麥克莫丹卡達爾有一段新通道，工人們才剛重新打通——你知道的，不久前那裡發生過一場嚴重的坍塌——聽說那裡有間密室，堆滿了寶藏。

### (sub) DIAL_Z30#2354
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼告訴我？你自己怎麼不去拿那些寶藏？

### (sub) DIAL_Z30#2355
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那等於是偷我自己的東西——畢竟那是矮人的寶藏——再說我也沒那個興致去試。你要是不是小偷，我告訴你也沒什麼好擔心的；你要是小偷——那我也一樣沒什麼好擔心的。我們可不會平白無故把寶藏就這麼擺著不管，總是有原因的。

### (sub) DIAL_Z30#2356
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那會是什麼原因？

### (sub) DIAL_Z30#2357
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說吧，這世上有些東西，你要嘛註定該擁有，要嘛註定不該擁有。要是你命中註定該摸到什麼，你就會摸到。要是不是，那……命運自會安排這種事。

### (sub) DIAL_Z30#2358
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴，我相信你這話說得沒錯。這是我吃了不少苦頭才學到的教訓。

### (sub) DIAL_Z30#2359
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [14883..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2360
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [14977..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Dubal_An_Loch

### (sub) DIAL_Z30#2361
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2362
- speaker=0  style=6
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名矮人朝他們皺起了眉頭。  他顯然打定主意暫時不打算離開這張凳子，只顧著使勁抽著菸斗。「勞煩兩位行行好，我倒寧可你們別來煩我。矮人抽菸斗是件神聖的事，酒館就是他的神殿。也許我們晚點再聊。」

### (sub) DIAL_Z30#2363
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [15352..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2364
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [15445..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Dubal_An_Loch

### (sub) DIAL_Z30#2365
- speaker=0  style=0
- branches:
    - [flag 0x1ec7 in [17629..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2366
- speaker=0  style=0
- effects:
    - SET flag 0x0014=1
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2367
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 杜巴皺起了臉。  他俯身對著菸斗，用拇指戳了戳海泡石菸斗鍋，直到一縷微弱的藍色菸霧冒出，瀰漫了整個房間。他不耐煩地低吼一聲，把那冒著煙的東西塞進嘴裡，用他那濃重的矮人口音低聲咕噥著。

### (sub) DIAL_Z30#2368
- speaker=40  style=0
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 點上一斗米德凱米亞菸草，你就能享受一整個鐘頭遠離塵世的清閒。可點上圖蘭尼那種菸草，能冒出蚊子吐的那麼一丁點煙，你就該偷笑了。要我說，他們大概是拿格瓦利獸的糞便摻了一半進去。

### (sub) DIAL_Z30#2369
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 介意我陪你坐一會兒嗎？

### (sub) DIAL_Z30#2370
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你想坐哪就坐哪，小子。這些凳子又不是我的，不過你要是想找人閒聊，杜巴．安洛克正是你要找的老頭子。有什麼好故事要說嗎，小夥子？

### (sub) DIAL_Z30#2371
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這問題可危險，不過我敢打賭你的故事肯定比我的久遠得多。眼下我正忙著別的事。我們正在追查一名殺人犯……

### (sub) DIAL_Z30#2372
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ñ啊ð，你這種話會污了藍輪客棧的清淨。我們這兒都是些快活人，我可沒心情讓它給毀了。你得開朗一點，像蘇馬尼那樣……

### (sub) DIAL_Z30#2373
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ñ那個酒保ð？我想他作為圖蘭尼人算是個不錯的傢伙，不過他看起來有點冷淡……不算是個開心果。

### (sub) DIAL_Z30#2374
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他呀，可是個活寶。他有個笑話能把你笑得肚子疼，笑到尿褲子都不誇張。當然，他畢竟是圖蘭尼人，他的笑話得花點時間才能習慣。他們看事情的角度，總是帶著一種奇特的智慧。

### (sub) DIAL_Z30#2375
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我同意他們是群奇特的人。我想我唯一見過的一個，是個他們叫他查爾斯的人——他原本的圖蘭尼名字我怎麼都唸不對。他在克萊迪替馬丁公爵做事……

### (sub) DIAL_Z30#2376
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，那你就去問問蘇馬尼，問他剛才跟我說的那個笑話吧。這段時間，我想我要靜靜地快快抽口菸。

### (sub) DIAL_Z30#2377
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好啊。謝謝你陪我們聊聊。

### (sub) DIAL_Z30#2378
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [17535..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2379
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [17629..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Dubal_An_Loch

### (sub) DIAL_Z30#2380
- speaker=0  style=0
- effects:
    - SET flag 0x0014=1
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2381
- speaker=0  style=6
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名矮人朝他們皺起了眉頭。  他顯然打定主意暫時不打算離開這張凳子，只顧著使勁抽著菸斗。「勞煩兩位行行好，我倒寧可你們別來煩我。矮人抽菸斗是件神聖的事，酒館就是他的神殿。也許我們晚點再聊。」

### (sub) DIAL_Z30#2382
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18024..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2383
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [18117..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Dubal_An_Loch

### (sub) DIAL_Z30#2384
- speaker=0  style=0
- branches:
    - [flag 0x1ec7 in [21802..4]] -> node 4294901761
    - [flag 0x1fd1 in [21802..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2385
- speaker=0  style=0
- effects:
    - SET flag 0x0014=1
    - ?wOp12 a1=1024 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2386
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  這名矮人走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2387
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，你這下可闖禍了，小子。我看那老圖蘭尼人以後還肯不肯跟你說話，都難講了。

### (sub) DIAL_Z30#2388
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼？我說了什麼？

### (sub) DIAL_Z30#2389
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒說錯什麼，至少按王國的標準來說沒有。可蘇馬尼，他又不是王國人，對吧？至少他腦子裡想的不是王國那一套。這些從凱勒旺來的人，看事情的角度總是怪裡怪氣的，依我看，你剛才提起他被駐軍革職的事，已經冒犯了他的榮譽。

### (sub) DIAL_Z30#2390
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不是有意冒犯他的。我只是好奇而已。

### (sub) DIAL_Z30#2391
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 誰都會好奇，誰都會好奇。可這些圖蘭尼人啊，他們把榮譽看得比什麼都重，要是失了榮譽，他們會覺得自己沒了活下去的資格。要不是我一年多前跟他撒了個小謊，我看他現在恐怕早就了結自己的性命了。

### (sub) DIAL_Z30#2392
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可他到底做了什麼，才會落得被革職？

### (sub) DIAL_Z30#2393
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他對這件事沒怎麼開過口，不過我畢竟是矮人，四處打聽了一下，我想我已經拼湊出了這故事的真相。大概三年前，蘇馬尼被誤派去看守拉姆特的墓地。那天他已經替一個朋友多站了一班崗，好讓那朋友能去完婚，前一晚他還熬夜幫忙接生一頭小牛，忙到很晚。不幸的是，伯爵手下有個蠢才忘了留意這件事，結果安排蘇馬尼一連站了二十六個小時的崗！他再怎麼撐，最終還是敵不過疲憊，在崗位上打起了瞌睡……

### (sub) DIAL_Z30#2394
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可那不是他的錯。

### (sub) DIAL_Z30#2395
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯，不過故事還沒完。等來接班的人時，來的偏偏是個傲慢的混帳隊長，他家跟蘇馬尼家有些世仇。作為懲罰，他逼蘇馬尼隔天晚上睡在一座剛挖好的墳裡，還得跟一具剛因癆病死去的屍體作伴。那個蠢書記的疏失，後來被卡蘇米伯爵查出來了，可蘇馬尼還是覺得，自己打瞌睡這件事，已經給自己跟自己原本的家族帶來了恥辱。

### (sub) DIAL_Z30#2396
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這太可怕了！他到現在還一直為這件事良心不安？

### (sub) DIAL_Z30#2397
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 問題就在這兒。換了平常，圖蘭尼人心裡要是裝著這種事，通常會服毒自盡，或是拿劍自刎。他們就是沒學過怎麼放下一個錯誤、繼續往前走。幸好他正在學著用王國人的方式來面對這種事。

### (sub) DIAL_Z30#2398
- speaker=0  style=0
- branches:
    - [flag 0x0014 in [3915..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2399
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這話什麼意思？

### (sub) DIAL_Z30#2400
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你要是見過大多數圖蘭尼人，大概會覺得他們沒一個人會笑什麼事，尤其是笑自己。可我還算走運，讓蘇馬尼學會用點幽默看待這件事。以他自己的方式來說，他還挺會說笑話的呢。

### (sub) DIAL_Z30#2401
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你不是認真的吧。他開朗得跟具屍體差不多。

### (sub) DIAL_Z30#2402
- speaker=40  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我倒不會這麼說，當著他的面肯定也不會這麼說。不過去吧，讓他跟你說說他半小時前跟我說的那個笑話。我想在你把他的心情搞得一團糟之後，這或許能讓他振作一點。去吧。這段時間，我想我要靜靜地快快抽口菸。

### (sub) DIAL_Z30#2403
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許值得一試。謝了，杜巴。

### (sub) DIAL_Z30#2404
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [21708..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2405
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [21802..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Dubal_An_Loch

### (sub) DIAL_Z30#2406
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2407
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1014 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2408
- speaker=0  style=6
- effects:
    - ?wOp12 a1=101 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這名矮人朝他們皺起了眉頭。  他顯然打定主意暫時不打算離開這張凳子，只顧著使勁抽著菸斗。「勞煩兩位行行好，我倒寧可你們別來煩我。矮人抽菸斗是件神聖的事，酒館就是他的神殿。也許我們晚點再聊。」

### (sub) DIAL_Z30#2409
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [22206..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2410
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [22299..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C6_Dubal_An_Loch

### (sub) DIAL_Z30#2411
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2412
- speaker=0  style=0
- branches:
    - [flag 0x1fc5 in [27153..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2413
- speaker=0  style=0
- branches:
    - [flag 0x1ec8 in [25039..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2414
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2415
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2416
- speaker=41  style=0
- effects:
    - ?wOp12 a1=92 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎，各位。是什麼風把你們吹來伊夏神修道院的？

### (sub) DIAL_Z30#2417
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這位年輕的受監護人一直想來參觀貴校這所馳名的貴族學堂。我看要是不來拜訪一趟，他是不會讓我們離開馬拉克十字鎮的。

### (sub) DIAL_Z30#2418
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哎呀呀。很高興見到我們的名聲早已傳開。我能不能假設，您是有意成為我們的新學生，還是您是從我們那令人敬重的對手——星塢島法師學院——來拜訪的？

### (sub) DIAL_Z30#2419
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我父親絕不會允許我正式學習法術。儘管他的財力綽綽有餘，能送我去星塢島，他卻認為讓一個年輕貴族花上一二十年的光陰埋首書堆，到頭來卻幾乎什麼都不會做，簡直是浪費時間。要不是我曾遇過一位叫派特魯斯的法師，我對法術可說是一竅不通。

### (sub) DIAL_Z30#2420
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 確實，法師的修習時間較長，顯而易見的成果卻較少，不過沒有一門學問是在浪費時間的。雖然法術並非我們這裡主要教授的科目，但帕格法師相當仁慈，偶爾會從星塢島派講師來，講授一些涉及法師的議題。要是您有興趣入學……

### (sub) DIAL_Z30#2421
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很遺憾，我們沒有時間繞這個彎路。他還有要緊的事得辦，得趕去別處。

### (sub) DIAL_Z30#2422
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那紳爵您呢？我們的課程裡有什麼引起您興趣的嗎？

### (sub) DIAL_Z30#2423
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 書本跟卷軸？我現在年紀有點太大，不適合那種東西了。

### (sub) DIAL_Z30#2424
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真的嗎？那真是可惜了。我原本正打算給您一個機會，去聽聽我們一位客座講師教授的戰術課程……不過現在想想，您大概也不會感興趣。授課的是一位，這麼說吧，有點古怪的人物，一位獨眼的紳士，名叫巴斯泰拉……

### (sub) DIAL_Z30#2425
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 巴斯泰拉？您是說居伊．杜．巴斯泰拉？萊亞姆王的首席顧問？

### (sub) DIAL_Z30#2426
- speaker=41  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [25421..4]] -> node 4294901761
    - [flag 0x0101 in [26768..4]] -> node 4294901761
- text: 是的，我想那正是他的頭銜……這是伊夏神修道院跟萊亞姆王的一項安排。作為我們撥出部分設施供教育之用的交換，國王偶爾會借調王國裡幾位最傑出的人才過來。這對雙方都有好處。要是您仍有興趣，只需捐獻二十枚金幣，我還是能替您安排入場。紳爵，您意下如何？

### (sub) DIAL_Z30#2427
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2428
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2429
- speaker=41  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=92 a2=0
- branches:
    - [flag 0x0100 in [25421..4]] -> node 4294901761
    - [flag 0x0101 in [26768..4]] -> node 4294901761
- text: 你們運氣不錯。今晚居伊．杜．巴斯泰拉那場關於戰場評估的演講，看來還剩幾個名額。你們想買票嗎？

### (sub) DIAL_Z30#2430
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [25450..4]] -> node 4294901780
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2431
- speaker=0  style=0
- effects:
    - GIVE item 'b' cond=1 to member#6 (cost 200)
    - SET flag 0x1fc5=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2432
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們能抽出時間。我們得去哪？

### (sub) DIAL_Z30#2433
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鎮上，靠近王后街的地方，有間我們為居伊的演講預留的小廳。只需在門口出示這張票，他們就會放你們進去。我相信你們會度過一個發人深省的夜晚。

### (sub) DIAL_Z30#2434
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝您。我們很期待。

### (sub) DIAL_Z30#2435
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [25881..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2436
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [25994..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Abbot_Graves_YES_TICKETS_ENOUGH_GOLD

### (sub) DIAL_Z30#2437
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2438
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 心有餘而錢包空。我手頭有點緊。

### (sub) DIAL_Z30#2439
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕沒有捐獻，我沒法讓你們入場。這是我們這裡的小小限制之一。我們修道院並不習慣經營什麼大生意，所以我們是靠門口募得的資金，來支付客座講師的旅費。你們今晚的演講大概是趕不上了，不過視學生出席的踴躍程度，我們可能會請他再開一場，所以要是你們到時候籌得出資金，或許還能聽到他的演講。

### (sub) DIAL_Z30#2440
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會設法在那之前把荷包填滿的。祝您愉快。

### (sub) DIAL_Z30#2441
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [26651..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2442
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [26768..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Abbot_Graves_YES_TICKETS_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2443
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2444
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 說真的，我們沒有時間。不過還是感謝您的好意。

### (sub) DIAL_Z30#2445
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們改變主意，我這邊應該還有票。一路順風。

### (sub) DIAL_Z30#2446
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們知道去哪找您。謝謝。

### (sub) DIAL_Z30#2447
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27053..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2448
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27153..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Abbot_Graves_NO_TICKETS

### (sub) DIAL_Z30#2449
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2450
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2451
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 院長您好。我們希望能跟您談一會兒。

### (sub) DIAL_Z30#2452
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管我很想跟你們聊聊，不過我還有點事要處理。有幾個學生需要我特別關照。也許改天我們還能再見。

### (sub) DIAL_Z30#2453
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧。我們就不打擾您照顧學生了。再見。

### (sub) DIAL_Z30#2454
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27726..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2455
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [27826..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C2_Abbot_Graves_HAS_TICKET

### (sub) DIAL_Z30#2456
- speaker=0  style=0
- branches:
    - [flag 0x1ec8 in [32123..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2457
- speaker=0  style=0
- branches:
    - [flag 0xc3b2 in [29441..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2458
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2459
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2460
- speaker=41  style=0
- effects:
    - ?wOp12 a1=92 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎來到伊夏神修道院。我是葛雷夫斯院長。有什麼能為您效勞的？

### (sub) DIAL_Z30#2461
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 最近有幾個人在羅姆尼遇害，我跟同伴正在調查這起謀殺案。我們希望您能提供一些線索。

### (sub) DIAL_Z30#2462
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們永遠聽候國王的差遣。有什麼能幫忙的？

### (sub) DIAL_Z30#2463
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 死者身上找到了兩件物品。一件是外觀相當普通的黃銅望遠鏡，另一件是一尊銀製的小蜘蛛雕像。您對這兩樣東西有任何了解嗎？

### (sub) DIAL_Z30#2464
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 望遠鏡是常見的器具，不過銀蜘蛛，那可就相當稀罕了。我在書上見過相關記載，說那是一種魔法下毒器具，但對一個尋常的殺人犯來說，價格高得離譜。用得起這種蜘蛛的人，必定家財萬貫，還得跟凱許有些淵源。那正是它們的產地。

### (sub) DIAL_Z30#2465
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝您，您幫了大忙。

### (sub) DIAL_Z30#2466
- speaker=41  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [33076..4]] -> node 4294901761
    - [flag 0x0101 in [34387..4]] -> node 4294901761
- text: 很樂意能幫上忙。順帶一提，兩位對今晚一場戰術講座有沒有興趣？是由特羅維爾男爵在我們的特別講堂授課，保證會發人深省。票價只要二十枚金幣。你們想去嗎？

### (sub) DIAL_Z30#2467
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2468
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2469
- speaker=41  style=0
- effects:
    - play sfx 92
- branches:
    - [always] -> node 0 (no jump)
- text: 兩位，歡迎回到伊夏神修道院。有什麼能為兩位效勞的？

### (sub) DIAL_Z30#2470
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 最近有幾個人在羅姆尼遇害，我跟同伴正在調查這起謀殺案。我們希望您能提供一些線索。

### (sub) DIAL_Z30#2471
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們永遠聽候國王的差遣……請儘管提問。

### (sub) DIAL_Z30#2472
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 死者身上找到了兩件物品。一件是外觀相當普通的黃銅望遠鏡，另一件是一尊銀製的小蜘蛛雕像。您對這兩樣東西有任何了解嗎？

### (sub) DIAL_Z30#2473
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 望遠鏡是常見的器具，不過銀蜘蛛，那可就相當稀罕了。我在書上見過相關記載，說那是一種魔法下毒器具，但對一個尋常的殺人犯來說，價格高得離譜。用得起這種蜘蛛的人，必定家財萬貫，還得跟凱許有些淵源。那正是它們的產地。

### (sub) DIAL_Z30#2474
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝您，您幫了大忙。

### (sub) DIAL_Z30#2475
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很樂意能幫上忙。我記得，你們買了首席顧問那場敵情評估演講的票，對吧？我相信那場演講讓你們獲益良多。

### (sub) DIAL_Z30#2476
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 其實我們沒去成。上次在馬拉克十字鎮時，時間不夠。

### (sub) DIAL_Z30#2477
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真是可惜。我記得我們一位優秀的學生——要是我沒記錯，是凱爾．費雪——當場站起來，跟首席顧問就深陶頓一役的戰術辯論了起來。我這輩子還沒見過那孩子有哪次像那幾天一樣狼狽不堪。不過你們運氣不錯，因為另一位客座講師接下來會再開一段時間的課，而既然你們的票沒用過，依然有效。

### (sub) DIAL_Z30#2478
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 主題是什麼？

### (sub) DIAL_Z30#2479
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想這個主題，你們應該早就感興趣了。還是戰術，這回由高堡的特羅維爾男爵授課。我相信他會講述他跟莫瑞德人交戰的經歷。

### (sub) DIAL_Z30#2480
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他怎麼沒在北方集結兵力？

### (sub) DIAL_Z30#2481
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他正在等黑沼鎮的一批士兵。在他們抵達之前，他相當慷慨地借調來為我們授課。我自己也很想去聽這場演講，可惜職責所在，得去別處。祝兩位玩得愉快。

### (sub) DIAL_Z30#2482
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。謝謝您。

### (sub) DIAL_Z30#2483
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [32019..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2484
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [32123..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Abbot_Graves_HAS_TICKET

### (sub) DIAL_Z30#2485
- speaker=0  style=0
- branches:
    - [flag 0x1fc6 in [32512..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2486
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2487
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2488
- speaker=41  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=92 a2=0
- branches:
    - [flag 0x0100 in [33076..4]] -> node 4294901761
    - [flag 0x0101 in [34387..4]] -> node 4294901761
- text: 你們運氣不錯。今晚特羅維爾男爵的演講，看來還剩幾個名額。你們想買票嗎？

### (sub) DIAL_Z30#2489
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2490
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2491
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管我很想跟你們聊聊，不過我還有點事要處理。有幾個學生需要我特別關照。也許改天我們還能再見。

### (sub) DIAL_Z30#2492
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧。在那之前，祝您愉快。

### (sub) DIAL_Z30#2493
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [32973..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2494
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33076..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Abbot_Graves_HAS_TICKET

### (sub) DIAL_Z30#2495
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [33105..4]] -> node 4294901780
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2496
- speaker=0  style=0
- effects:
    - SET flag 0x1fc6=1
    - GIVE item 'b' cond=1 to member#6 (cost 200)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2497
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我們能抽出時間。演講在哪？

### (sub) DIAL_Z30#2498
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鎮上，王后街旁邊，有間我們為特羅維爾的演講預留的小廳。只需在門口出示這張票，守門人就會放你們進去。我相信你們會度過一個發人深省的夜晚。

### (sub) DIAL_Z30#2499
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望如此。謝謝您。

### (sub) DIAL_Z30#2500
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [33538..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2501
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33651..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C3_Abbot_Graves_YES_TICKETS_ENOUGH_GOLD

### (sub) DIAL_Z30#2502
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2503
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 心有餘而錢包空。我手頭有點緊。

### (sub) DIAL_Z30#2504
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕沒有捐獻，我沒法讓你們入場。這是我們這裡的小小限制之一。我們修道院並不習慣經營什麼大生意，所以我們是靠門口募得的資金，來支付客座講師的旅費。你們今晚的演講大概是趕不上了，不過視學生出席的踴躍程度，我們可能會請他再開一場，所以要是你們到時候籌得出資金，或許還能聽到他的演講。

### (sub) DIAL_Z30#2505
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝您。我們會盡力試試。

### (sub) DIAL_Z30#2506
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34270..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2507
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34387..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C3_Abbot_Graves_YES_TICKETS_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2508
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2509
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 說真的，我們沒有時間。不過還是感謝您的好意。

### (sub) DIAL_Z30#2510
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們改變主意，我這邊應該還有票。一路順風。

### (sub) DIAL_Z30#2511
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您也一路順風。

### (sub) DIAL_Z30#2512
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34670..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2513
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34770..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C3_Abbot_Graves_NO_TICKETS

### (sub) DIAL_Z30#2514
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2515
- speaker=0  style=0
- branches:
    - [flag 0x1ec8 in [38404..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2516
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2517
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2518
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們挑了個不太方便的時間來訪。我……我還有事要處理。

### (sub) DIAL_Z30#2519
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 潘塔西亞人為什麼會對攻擊伊夏神修道院感興趣？他們又為什麼要怪罪到您頭上？鎮民都嚇壞了，紛紛逃離城鎮，唯恐性命不保。院長，他們都在怪您。

### (sub) DIAL_Z30#2520
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 求你……我不知道他們為什麼會提出這些……指控……這不是我的責任，我不會負這個責任。

### (sub) DIAL_Z30#2521
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是您正打算逃離這座城鎮，我勸您最好打消念頭。我們聽說，有些鎮民打算把您當成戰俘，獻給潘塔西亞人。

### (sub) DIAL_Z30#2522
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 潘塔西亞人才不留活口！他們一旦鎖定目標就會直接殺了對方！這根本是謀殺！

### (sub) DIAL_Z30#2523
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來要是您不被交出去，潘塔西亞人打算對馬拉克十字鎮做出更過分的事。您何不告訴我他們為什麼會來這裡？也許您幫我們，我們就能幫您。

### (sub) DIAL_Z30#2524
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 貪婪。他們來這裡，是因為伊夏神修道院裡有個沒骨氣的修士，抬起頭來，說自己命中註定要成就比這更大的事業。他這人毫無節操，毫不退縮，一心只為了自己那點自私的目的。他毫不留情，就像拍死一隻蒼蠅那樣，設計讓他的院長被人發現身上帶著一筆從兄弟會金庫裡失竊的錢。順理成章地，這名修士便取代了院長的位子。

### (sub) DIAL_Z30#2525
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是您。可您沒能保住這個祕密，對吧？有人發現了您的詭計。

### (sub) DIAL_Z30#2526
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的計畫天衣無縫，完美得就像最完美的珍珠，可不知怎的，他還是發現了。於是我們達成了一項協議。爬行者答應保守祕密，條件是我得聯繫帕格，安排一位法術導師定期前來馬拉克十字鎮授課。那些導師從不知道，他們教的人並非個個都是貴族，事情就這樣相安無事地過了四年……直到帕格從他在克朗多的一個手下口中查出了真相。帕格撤走了他的導師，收回了我們的書籍，讓我再也沒法履行那樁祕密交易的細節。於是爬行者又提出了新的要求。既然我沒法再訓練他的爪牙，我就得替他找出一件特定的魔法遺物，不然就得賠上性命。我...

### (sub) DIAL_Z30#2527
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 爬行者想要的那件遺物，該不會是本書吧？

### (sub) DIAL_Z30#2528
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不會再多說了。是時候安排我逃離馬拉克十字鎮了，你們兩個或許是我僅剩的希望。去找米契爾．韋蘭德，告訴他發生了什麼事。也告訴他，我不希望再有任何人受傷。等他安排妥當，回來告訴我該怎麼做。

### (sub) DIAL_Z30#2529
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？我們不能幫一個罪犯逃脫法律制裁！

### (sub) DIAL_Z30#2530
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 孩子，馬拉克十字鎮的男男女女根本不在乎我犯下的罪行。他們對此一無所知。他們只知道潘塔西亞人要我的命，而他們會不擇手段自保，哪怕這代表交出一個無辜的人。這正是他們所相信的正義。要是你們深思熟慮之後，依然認定我有罪，那就不必再回來了。

### (sub) DIAL_Z30#2531
- speaker=0  style=0
- branches:
    - [flag 0x1ea7 in [38404..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2532
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一名見習修士去請院長過來。  幾分鐘後他現身了，眼神警戒，像隻挨過打的狗。他拖著腳步走上前，低聲對@4說話。

### (sub) DIAL_Z30#2533
- speaker=0  style=0
- branches:
    - [flag 0xc3ca in [38632..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2534
- speaker=0  style=0
- effects:
    - REMOVE item 'z' cond=0
    - SET flag 0x1ed4=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2535
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們跟米契爾談過了嗎？

### (sub) DIAL_Z30#2536
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他有個計畫，自認為行得通。他把細節都帶來了。

### (sub) DIAL_Z30#2537
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 戰術，戰術，戰術，永遠是戰術。我想，我這院長生涯，也算是理所當然的下場了。祭司被一枚小卒扳倒。這循環總算圓滿了。

### (sub) DIAL_Z30#2538
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 院長，現在做正確的事還不晚。您有機會回擊爬行者。您可以告訴我怎麼取得那件遺物，不讓他得手。告訴我怎麼拿到馬克羅斯之書。

### (sub) DIAL_Z30#2539
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 馬克羅斯之書？我從沒聽說過這本書。他離開米德凱米亞時留下的藏書，我謄抄過不少，可要是真讀過一本這個書名的書，我想我應該會記得才對。除了帕格跟托馬斯對圖蘭尼裂界戰爭所寫的史評裡提到的以外，我對那位法師所知甚少。不，爬行者要的其實是一把據傳早年在馬拉克十字鎮附近失落的魔法劍。就我個人來說，我不相信瓜爾達雷凡什真有其物，不過是個神話罷了……

### (sub) DIAL_Z30#2540
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 您剛才提到一個叫托馬斯的人。那是誰？

### (sub) DIAL_Z30#2541
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嗯？托馬斯？他是艾爾凡達精靈的統帥，亞葛拉蘭娜王后的夫婿。據我所知，他跟帕格交情很深，我想他也曾與馬克羅斯有過一段淵源。也許他會知道你們要找的馬克羅斯之書的事。

### (sub) DIAL_Z30#2542
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這算是條線索。雖然單薄，但也是條線索。謝謝您，院長。看來我們還有本書要找。也許我們還會在更愉快的情況下再見面。

### (sub) DIAL_Z30#2543
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不太可能，除非你們也踏上通往凱許的路。我想那正是我接下來要去的地方。再見，珍重。

### (sub) DIAL_Z30#2544
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 凱許啊？祝您好運。

### (sub) DIAL_Z30#2545
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40422..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2546
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [40520..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Abbot_Graves_YES_NOTE

### (sub) DIAL_Z30#2547
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2548
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們跟米契爾談過了嗎？

### (sub) DIAL_Z30#2549
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還沒找到他。

### (sub) DIAL_Z30#2550
- speaker=41  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鎮上的居民不會再等太久了。你們一定要找到米契爾．韋蘭德。快去吧，我離開之前還有幾件最後的事要處理。

### (sub) DIAL_Z30#2551
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們找到他就回來。

### (sub) DIAL_Z30#2552
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [40903..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2553
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [41000..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Abbot_Graves_NO_NOTE

### (sub) DIAL_Z30#2554
- speaker=0  style=0
- branches:
    - [flag 0x1e88 in [42949..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2555
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2556
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾露出了微笑。  儘管歷經十一年歲月，眼前這名走來的男子似乎矮了半個手掌，但他那略帶跛行的步態，依然像他的簽名一樣，獨屬於他自己。多年前，艾薩克曾自豪地忍受這一瘸，把它當成戰場上留下的傷痕般看待，也因此贏得了克朗多年輕扈從們的敬重與欽佩，洛克利爾也在其中。他當年被亞魯莎宮廷悲慘地驅逐，對他們所有人來說都是一記重擊……

### (sub) DIAL_Z30#2557
- speaker=42  style=0
- effects:
    - play sfx 105
- branches:
    - [always] -> node 0 (no jump)
- text: 老扈從，這些年你保養得挺不錯的嘛，雖然你的頭髮似乎變深了些。你幹了什麼好事？把頭伸進瀝青桶裡了？

### (sub) DIAL_Z30#2558
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這個惡棍，我還以為你早就因為冒充公爵被吊死了呢！艾薩克，你近來如何？！自從亞魯莎的婚禮以來，我們就沒見過了吧？

### (sub) DIAL_Z30#2559
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就是那天。你真該聽聽司儀官德萊西發現我不是多爾金伯爵的兒子時，發的那頓脾氣。要不是他當時正忙著那場喜事的種種細節，我敢說他肯定會親自把我扔出王宮圍牆。從那之後我一直忙個不停，這幾年都在邊境一帶到處打零工。自從離開克朗多以後，我學到、見識到的事情，肯定會讓你大吃一驚。

### (sub) DIAL_Z30#2560
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就讓我開開眼界吧。你一直都是個ó長舌鬼……

### (sub) DIAL_Z30#2561
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧……你想知道些什麼？

### (sub) DIAL_Z30#2562
- speaker=0  style=0
- effects:
    - push return-address key 304654 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2563
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管我很想留下來閒聊八卦，不過我看我們三個還是得趕緊上路，免得亞魯莎親王派搜索隊來找我們。

### (sub) DIAL_Z30#2564
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這麼說，親王ó在等著你們了……請替我向殿下致意。

### (sub) DIAL_Z30#2565
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會的。保重，艾薩克！

### (sub) DIAL_Z30#2566
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [42863..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2567
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [42949..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Isaac

### (sub) DIAL_Z30#2568
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2569
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 洛克利爾看見了艾薩克。  這位紳爵朝這位老相識吹了聲口哨，示意他加入他們一行人……

### (sub) DIAL_Z30#2570
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我還以為你去見亞魯莎親王了。

### (sub) DIAL_Z30#2571
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我也是這麼想的，不過我們一直在這一帶瞎忙，處理些別的事。碰巧又遇上你，算我們走運。

### (sub) DIAL_Z30#2572
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我就當這是好運氣了。那，我能為你做點什麼？

### (sub) DIAL_Z30#2573
- speaker=0  style=0
- effects:
    - push return-address key 305600 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2574
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 儘管我很想留下來閒聊八卦，不過我看我們三個還是得趕緊上路，免得亞魯莎親王派搜索隊來找我們。

### (sub) DIAL_Z30#2575
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我可不敢耽誤你們趕路，不過……紳爵，自己小心點。外頭有些危險人物。

### (sub) DIAL_Z30#2576
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我們會多留意的。再見了，艾薩克。

### (sub) DIAL_Z30#2577
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [43875..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2578
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [43960..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Isaac

### (sub) DIAL_Z30#2579
- speaker=0  style=0
- branches:
    - [flag 0x1e88 in [45808..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2580
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2581
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士打量著這位老相識的偽裝。  他不經意地注意到，艾薩克依然裝出一副以假亂真的跛行姿態，手法多半是從克朗多的乞丐那裡學來的。他腰間掛著好幾個錢袋，裡頭想必都裝著叮噹作響的鐵片，足以讓ó一般旅人相信他是個商人，可詹姆士絕非一般人……

### (sub) DIAL_Z30#2582
- speaker=42  style=0
- effects:
    - play sfx 105
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士扈從。你大老遠跑來這一趟，是要再一次揭穿我的真面目嗎？

### (sub) DIAL_Z30#2583
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那是十一年前的事了。你當時是個冒名頂替的人，而我們正面臨著威脅親王性命的危機。在不知道你真實身分的情況下，我沒法昧著良心讓德萊西把你安排到亞魯莎跟安妮塔的攻擊範圍之內。

### (sub) DIAL_Z30#2584
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒關係，承蒙運氣眷顧，我現在的日子過得，或許比你想像的還要好。我經營自己的生意，打理自己的事務，不必操心國家大事……

### (sub) DIAL_Z30#2585
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 艾薩克，是不必操心，還是不顧他們的擔憂？我聽過關於你的一些不太妙的傳聞。

### (sub) DIAL_Z30#2586
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有關於我的傳聞，那都是我的競爭對手放出來的。尊貴的紳爵，我向您保證，我完全ó聽候王國差遣。有什麼能為您效勞的？

### (sub) DIAL_Z30#2587
- speaker=0  style=0
- effects:
    - push return-address key 307442 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2588
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該走了。我本想叫你保重，艾薩克，不過你這方面向來很在行。

### (sub) DIAL_Z30#2589
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這人從來不肯放下心結，是吧？

### (sub) DIAL_Z30#2590
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這跟心結沒關係。我只是知道，有人想ó耍我的時候，該相信自己的直覺。再見了，艾薩克。我有預感我們還會再見面。

### (sub) DIAL_Z30#2591
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [45722..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2592
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [45808..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_CX_Isaac

### (sub) DIAL_Z30#2593
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2594
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 詹姆士看見了艾薩克。  這位紳爵吹了聲口哨，示意他加入他們一行人……

### (sub) DIAL_Z30#2595
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 對一個不信任我的人來說，你倒是挺有興致找我說話的嘛。吉米，你怎麼又回來了？上次跟我說話還沒罵夠嗎？

### (sub) DIAL_Z30#2596
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 別發牢騷了。我需要一些答案，而你或許是唯一能給我答案的人。

### (sub) DIAL_Z30#2597
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧。你想知道什麼？

### (sub) DIAL_Z30#2598
- speaker=0  style=0
- effects:
    - push return-address key 308497 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2599
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該走了。我本想叫你保重，艾薩克，不過你這方面向來很在行。

### (sub) DIAL_Z30#2600
- speaker=42  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這人從來不肯放下心結，是吧？

### (sub) DIAL_Z30#2601
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這跟心結沒關係。我只是知道，有人想ó耍我的時候，該相信自己的直覺。再見了，艾薩克。我有預感我們還會再見面。

### (sub) DIAL_Z30#2602
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [46777..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2603
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [46862..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_CX_Isaac

### (sub) DIAL_Z30#2604
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2605
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2606
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文打量著這名走近的男子。  除了走路姿勢有些古怪的跛行之外，這人似乎還有些不尋常之處。他腰間掛著好幾個錢袋，裡頭想必裝著金幣、銀幣，或是這位商人選擇用來交易的任何貨幣……

### (sub) DIAL_Z30#2607
- speaker=42  style=0
- effects:
    - play sfx 105
- branches:
    - [always] -> node 0 (no jump)
- text: 你們來得正是時候。我剛才還在想，要是有人陪陪就好了。都快孤單到要跟樹說話了。有什麼我能為你們效勞的嗎？

### (sub) DIAL_Z30#2608
- speaker=0  style=0
- effects:
    - push return-address key 309635 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2609
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們該走了。還有事要辦。這次聊天挺有意思的。

### (sub) DIAL_Z30#2610
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [47617..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2611
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [47703..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Isaac

### (sub) DIAL_Z30#2612
- speaker=0  style=0
- branches:
    - [flag 0x1ec9 in [48966..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2613
- speaker=0  style=0
- effects:
    - SET flag 0x0074=1
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2614
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方有個農夫。  @4猶豫了片刻，考慮著在被發現之前躲起來會不會比較明智，還是照常行動比較好，最後判斷這人應該對他們不構成立即的威脅……

### (sub) DIAL_Z30#2615
- speaker=43  style=0
- effects:
    - ?wOp12 a1=126 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 兩位先生，為了你們的健康著想，希望你們已經找到地方躲避即將到來的暴風雨了。

### (sub) DIAL_Z30#2616
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 暴風雨？

### (sub) DIAL_Z30#2617
- speaker=43  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們想必聽說了吧。薩斯那些博學的修士預言，一場可怕的風暴正朝這裡襲來，我實在不願想像有人被困在外頭的樣子。畢竟，一個人可能會因此染上要命的熱病。要是你們願意，可以到我的穀倉躲一躲。

### (sub) DIAL_Z30#2618
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你打算從這樁買賣中賺點什麼？

### (sub) DIAL_Z30#2619
- speaker=43  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 五枚金幣，這個數目算合理了，再加上幫我看顧牛群。你們可以睡在我穀倉的乾草閣樓上，不過我跟我老婆不收留精靈……

### (sub) DIAL_Z30#2620
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 七枚金幣，精靈跟我們待在一起，而且我們每人早餐都要有一塊硬麵包捲。

### (sub) DIAL_Z30#2621
- speaker=43  style=0  flags=paged-text
- branches:
    - [flag 0x0104 in [48908..4]] -> node 4294901761
    - [flag 0x0105 in [50659..4]] -> node 4294901761
- text: 十枚金幣，而且你們三個隔天早上都得幫忙擠牛奶。這是我的條件。要嘛接受，要嘛拉倒。

### (sub) DIAL_Z30#2622
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [48937..4]] -> node 4294901770
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2623
- speaker=0  style=0
- effects:
    - TAKE gold -100
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2624
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2625
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 前方有個農夫。  @4猶豫了片刻，考慮著在被發現之前躲起來會不會比較明智，還是照常行動比較好，最後判斷這人應該對他們不構成立即的威脅……

### (sub) DIAL_Z30#2626
- speaker=43  style=0
- effects:
    - ?wOp12 a1=126 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哎呀，又見面了。你們重新考慮過我住宿的提議了嗎？

### (sub) DIAL_Z30#2627
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是考慮過了，不過還沒做出決定。這個價錢有點高。

### (sub) DIAL_Z30#2628
- speaker=43  style=0  flags=paged-text
- branches:
    - [flag 0x0104 in [49594..4]] -> node 4294901761
    - [flag 0x0105 in [50659..4]] -> node 4294901761
- text: 那就八枚金幣，而且你們不用幫我看顧牛群。這樣如何？昧著良心我也沒法再壓低多少了。

### (sub) DIAL_Z30#2629
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [49623..4]] -> node 4294901768
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2630
- speaker=0  style=0
- effects:
    - TAKE gold -80
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2631
- speaker=0  style=0
- effects:
    - SET flag 0x1ce9=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2632
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 成交。你這穀倉在哪？

### (sub) DIAL_Z30#2633
- speaker=43  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一直往南走——你們應該會經過薩斯的伊夏神修道院。等你們經過頌神神殿，就知道快到了。從那裡再繞過黃騾山就是。找到穀倉之後，敲敲門，我老婆會幫你們安頓好的。

### (sub) DIAL_Z30#2634
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你，老鄉。你的款待我們會記在心上的。

### (sub) DIAL_Z30#2635
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50136..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2636
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50237..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Cx_Rowe_TAKE_IT_ENOUGH_GOLD

### (sub) DIAL_Z30#2637
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2638
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 還請你見諒，恐怕我剛才說錯話了。我沒錢付你。

### (sub) DIAL_Z30#2639
- speaker=43  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你覺得你很快就會有錢了嗎？

### (sub) DIAL_Z30#2640
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不能確定。不管怎樣我們該走了。祝你愉快。

### (sub) DIAL_Z30#2641
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50554..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2642
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50659..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Cx_Rowe_TAKE_IT_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2643
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2644
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我看我們還是靠自己碰碰運氣好了。祝你愉快，老鄉。

### (sub) DIAL_Z30#2645
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [50791..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2646
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [50881..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Cx_Rowe_LEAVE_IT

### (sub) DIAL_Z30#2647
- speaker=0  style=0
- branches:
    - [flag 0x1eca in [52761..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2648
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1025 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2649
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2650
- speaker=44  style=0
- effects:
    - play sfx 104
- branches:
    - [always] -> node 0 (no jump)
- text: 有酒儘管喝，因為等這一切結束，迪勒肯只會讓我們的河流淌著尿、母雞下出灰塵。這場戰役根本一無所獲，可他眼裡的那點火花卻讓他瞎了眼。去他的六賢者！去他的那些法師，帶著我們走向死亡，把我們全都囚禁起來……

### (sub) DIAL_Z30#2651
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 伊爾梅林，看來你不太想讓自己的腦袋繼續留在肩膀上啊。  你這張嘴不停地說，把自己的腦子都口水似的流到了桌上，讓所有人都看在眼裡。你這是喝酒喝成了個傻子。

### (sub) DIAL_Z30#2652
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 喝酒讓我變成什麼樣，只干我跟酒館老闆的事。別管我，黃尾巴……

### (sub) DIAL_Z30#2653
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我建議你聽聽一個承受過迪勒肯之怒、還活著能講述這段經歷的人的忠告。我猜你有些相識的人，被迪勒肯的法師們給扣押了？

### (sub) DIAL_Z30#2654
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那又如何？反正也無計可施。六賢者把奧布卡丟給了維努特里爾跟他那群走狗，明天他們就會過來，把我們這群人統統趕去送死……

### (sub) DIAL_Z30#2655
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我提議我們互相幫忙，而不是互相為難。你能提供什麼，來交換奧布卡從那夫沙礦坑裡獲釋？

### (sub) DIAL_Z30#2656
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們辦得到，我能給你們相當於那男孩半個體重的黃金，或等值的東西。光是奧布卡的部族，就願意付這樣一筆贖金。

### (sub) DIAL_Z30#2657
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就去籌措這筆錢吧，我們再看看能安排些什麼。等我們讓奧布卡獲釋之後，會再來這間酒館找你。

### (sub) DIAL_Z30#2658
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [52673..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2659
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [52761..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C4_Irmelyn

### (sub) DIAL_Z30#2660
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[24] (xor=0xd1 mask=0xd0 mode=4 chapters=-)] -> node 4278256128
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2661
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2662
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2663
- speaker=44  style=0
- effects:
    - ?wOp12 a1=104 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡有消息了嗎？

### (sub) DIAL_Z30#2664
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還沒能突破六賢者的防禦，不過很快就會了。伊爾梅林，別擔心你的朋友。他會獲釋的。

### (sub) DIAL_Z30#2665
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你就去忙你的事吧，黃尾巴，我也去忙我的。

### (sub) DIAL_Z30#2666
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我會回來的。

### (sub) DIAL_Z30#2667
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [53346..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2668
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [53457..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Irmelyn_HAVENOTGIVEN_VAPOR_MASK

### (sub) DIAL_Z30#2669
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[24] (xor=0xdb mask=0x5c mode=21 chapters=8)] -> node 4278256640
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2670
- speaker=0  style=0
- effects:
    - event_bitmap_hi[24] bitop
    - ?wOp12 a1=1025 a2=0
    - GIVE gold +2000
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2671
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2672
- speaker=44  style=0
- effects:
    - play sfx 104
- branches:
    - [always] -> node 0 (no jump)
- text: 奧布卡在你們之前不久就到了這裡，還描述了兩個人……一個人類男孩，還有阿爾達尼恩氏族的戈拉斯。我原本打算把賞金自己留著，可他堅持說這是你們應得的。

### (sub) DIAL_Z30#2673
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他確實名不虛傳。也可能是他想救你一命……

### (sub) DIAL_Z30#2674
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 把你的劍留給更該死的人吧。我會付你錢。兩百枚金幣，一個銅板都不會多給……

### (sub) DIAL_Z30#2675
- speaker=0  style=0
- branches:
    - [flag 0x1ead in [54863..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2676
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓我們填飽肚子、有床可睡，這樣的交換，換一條人命也算划算。我還想再請教你一件事，之後我們就會離開這裡。你知不知道去哪能找到一位人稱庫利奇的女巫？

### (sub) DIAL_Z30#2677
- speaker=44  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 有，我聽說過她的消息。她逃去了凱恩以南、通往懷克的岔路以西一帶。多半是在那裡替迪勒肯那群走狗療傷……

### (sub) DIAL_Z30#2678
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這我就不清楚了。伊爾梅林，我們的交易就到此為止了。祝你好運、身體健康……

### (sub) DIAL_Z30#2679
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [54755..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2680
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [54863..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Irmelyn_HAVEGIVEN_VAPOR_MASK

### (sub) DIAL_Z30#2681
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 讓我們填飽肚子、有床可睡，這樣的交換，換一條人命也算划算。伊爾梅林，我們的交易就到此為止了。祝你好運、身體健康……

### (sub) DIAL_Z30#2682
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [55064..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2683
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [55172..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C4_Irmelyn_HAVEGIVEN_VAPOR_MASK

### (sub) DIAL_Z30#2684
- speaker=0  style=0
- branches:
    - [flag 0x1ecb in [58268..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2685
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2686
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 樂音隨風飄來。  洛克利爾一開始還以為自己是被旅途的勞頓給累糊塗了，隨即他分辨出附近一叢樹林裡，傳來〈ó卡爾斯ó海ó岸ó謠〉那優美的旋律。音樂忽然停了下來，一個神情不悅的年輕人從樹上跳了下來，魯特琴斜背在背上……

### (sub) DIAL_Z30#2687
- speaker=45  style=0
- effects:
    - ?wOp12 a1=130 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我剛ó從北衛城回來，今天不想再為他彈奏了。我的手指麻木，腦子空空，肚子還咕嚕作響……

### (sub) DIAL_Z30#2688
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 冷靜點。我們ó不是從城堡來的。我們只是路過的旅人，聽見你的樂聲，想看看是誰彈的。話說，一隻鳴禽ó怎麼會混在獵鷹群裡？

### (sub) DIAL_Z30#2689
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 快枯竭了，我怕是這樣。你知道嗎，我能唱〈ó艾莉亞ó與ó特里弗斯〉的愛情主題曲，還能彈奏大半部〈ó王國ó興起ó之ó篇〉組曲，也能一字不漏背出整首〈ó瓦勒林西斯ó之ó淚〉。可這些傢伙，這些怪物，就只想聽一首歌，還一遍又一遍地點——〈ó老ó頭ó的ó風〉！一首唱的是……唱的是吃豆子的歌！

### (sub) DIAL_Z30#2690
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那你怎麼還留在這裡？

### (sub) DIAL_Z30#2691
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒得選啊！有次跟一個朋友共飲一桶麥酒時，他跟我說起一個小村莊，那裡的酒格外濃烈，姑娘們也格外苗條。等我酒醒之後，便決心親自去這個奇妙的地方，好好享受一番。誰知道，讓我驚恐萬分的是，原來我朋友把比喻給搞混了，結果撲上我身的，是個能徒手把公牛的牙齒拔下來的女子。我還沒能從這種丟人的處境中脫身，她父親——一位頗有名望的準男爵——就把我流放到這裡，要我來替加博特男爵表演娛興，不然就要我的腦袋。

### (sub) DIAL_Z30#2692
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很意外他沒把你砍了頭。

### (sub) DIAL_Z30#2693
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，首先他女兒也不算多清白，其次他那年的效忠金也還沒繳清。既然加博特男爵喜愛音樂，他們便講定，由我來抵這筆債。  我看得出兩位是有些名望的貴族。要是能幫我個忙，或許能減輕一個吟遊詩人生活的壓力。

### (sub) DIAL_Z30#2694
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧。你需要什麼？

### (sub) DIAL_Z30#2695
- speaker=45  style=0
- branches:
    - [flag 0xc39d in [57720..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 一段輕型的弓弦。雖然它沒法直接派上用場，不過我找到了一種樹脂，塗上去之後就能拿來替魯特琴換弦。我有預感自己很快就需要新的琴弦了。

### (sub) DIAL_Z30#2696
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 算你走運，我們身上剛好帶著一條，我想我們可以割愛。

### (sub) DIAL_Z30#2697
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2698
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我們目前沒有能借給你的。也許加博特男爵手下的某個士兵能幫上你的忙。

### (sub) DIAL_Z30#2699
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧，不過我很懷疑。兩位，告辭了。

### (sub) DIAL_Z30#2700
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你也是，坦尼。我相信我們還會再見面的。

### (sub) DIAL_Z30#2701
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [58168..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2702
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [58268..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C1_Tamney_the_Minstrel

### (sub) DIAL_Z30#2703
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2704
- speaker=0  style=0
- branches:
    - [flag 0xc39d in [59020..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2705
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 他們並非孤身一人。  @0看見一個孤零零的身影走近，脈搏頓時加快；但看出對方並無攻擊之意後，他才稍稍放鬆下來，瞇起眼想看清楚是誰要加入他們。

### (sub) DIAL_Z30#2706
- speaker=45  style=0
- effects:
    - ?wOp12 a1=130 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢……是你們三個。你們有把我要的弓弦帶回來嗎？

### (sub) DIAL_Z30#2707
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恐怕我們目前沒有能借給你的。也許加博特男爵手下的某個士兵能幫上你的忙。

### (sub) DIAL_Z30#2708
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許吧，不過我很懷疑。兩位，告辭了。

### (sub) DIAL_Z30#2709
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你也是，坦尼。我相信我們還會再見面的。

### (sub) DIAL_Z30#2710
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [59020..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2711
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼就在附近。  這位ó吟遊藝人微弱的魯特琴聲引起了注意，@4喊他從藏身之處出來。這名吟遊詩人悶悶不樂地照做了……

### (sub) DIAL_Z30#2712
- speaker=45  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=130 a2=0
- branches:
    - [flag 0x0100 in [59327..4]] -> node 4294901761
    - [flag 0x011f in [60591..4]] -> node 4294901761
- text: 噢……是ó你啊！你們有把我要的弓弦帶回來嗎？

### (sub) DIAL_Z30#2713
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2714
- speaker=0  style=0
- effects:
    - REMOVE item 'M' cond=0
    - RAISE Barding of party by 1280
    - SET flag 0x1f89=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2715
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就禮尚往來！過去幾週，北衛城陸續有幾頭母豬被偷，所以我寫了這首小曲子來紀念這件事。這曲子又蠢又短，不過希望你們會喜歡。它叫〈ó北衛城ó的豬〉……

### (sub) DIAL_Z30#2716
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1028 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: ò-- 北衛城的豬 ò--    ó北方ó莫瑞德ó人ó兇ó殘暴  ó對ó人ó從不ó留ó情  ó你ó若ó靠得ó太近ó他們ó就ó殺你  ó怎麼ó樣ó都ó要殺  ó可ó入夜ó之後ó王國ó依然ó十分ó安全  ó因為ó守衛ó駐守ó在ó隘口  ó可是ó天亮ó一到ó清點ó豬崽ó的ó時候  ó士兵ó早就ó把ó牠們ó弄丟  ó豬崽ó歡歡喜喜ó又ó哼哼ó作樂ó開心ó不已  ó這些ó王國ó裡ó的ó豬崽  ó可是ó仔仔細細ó一頭ó一頭ó數ó過ó去  ó士兵ó早就ó把ó牠們ó弄丟

### (sub) DIAL_Z30#2717
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝你，坦尼。這真是太有意思了，不過恐怕我跟同伴又得上路了。還有事要辦。

### (sub) DIAL_Z30#2718
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那我就此告辭了。歡迎再來找我。

### (sub) DIAL_Z30#2719
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我還會再來北衛城，你儘管放心，我一定會的。祝你愉快。

### (sub) DIAL_Z30#2720
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [60481..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2721
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [60591..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Tamney_the_Minstrel_HAS_STRING

### (sub) DIAL_Z30#2722
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2723
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 真可惜。唉，算了，要是你們哪天找到了，請帶過來，也許我能為你們唱首曲子。容我先失陪了，男爵要我明晚晚餐時段表演幾首曲子，我得去練習了。

### (sub) DIAL_Z30#2724
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 祝你好運。彈得好一點，吟遊詩人。

### (sub) DIAL_Z30#2725
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [60939..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2726
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [61046..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C1_Tamney_the_Minstrel_GIVE_NO

### (sub) DIAL_Z30#2727
- speaker=0  style=0
- branches:
    - [flag 0x1ed6 in [50923..32813]] -> node 4294901761
    - [flag 0x1ed5 in [65001..4]] -> node 4294901761
    - [flag 0x1ecb in [63136..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2728
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2729
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 樂音隨風飄來。  詹姆士一開始還以為自己是被旅途的勞頓給累糊塗了，隨即他分辨出附近一叢樹林裡，傳來〈ó漁婦ó的ó女兒〉那優美的旋律。音樂忽然停了下來，一個神情不悅的年輕人從樹上跳了下來，魯特琴斜背在背上……

### (sub) DIAL_Z30#2730
- speaker=45  style=0
- effects:
    - ?wOp12 a1=130 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託告訴我，ó不是他派你們來的。我現在累得沒法彈奏了，我會的曲子也都彈到爛熟了。

### (sub) DIAL_Z30#2731
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唔。我聽說城堡裡要是連吟遊詩人都沒了魅力，那可真是不祥的一天。你在煩惱什麼？

### (sub) DIAL_Z30#2732
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵手下有個新兵想學音樂，我欣然答應了，還犧牲了自己早晨散步的時間，好挪出空來教他。我們馬上就開始上課。我示範了一段簡單的王家音階給他看——上行的八分音符，從C退位音到A加冕音，以半音階、王國拍子進行。可教了兩個禮拜，他連音符都認不全。他不肯練習，分不清調好音跟沒調音的魯特琴有什麼差別，還死活不肯學怎麼讀吟遊詩人的樂譜。我實在不明白他當初幹嘛想學。

### (sub) DIAL_Z30#2733
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許他以為會比較簡單。

### (sub) DIAL_Z30#2734
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 大家都這麼想。他們以為只要拿起樂器，它就會自己神奇地發出聲音，根本不需要花半點心思。學音樂需要紀律，就跟學劍術一樣。

### (sub) DIAL_Z30#2735
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許你哪天能教教我們。

### (sub) DIAL_Z30#2736
- speaker=45  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [63595..4]] -> node 4294901761
    - [flag 0x0101 in [64421..4]] -> node 4294901761
- text: 算你們走運，我現在剛好有空，而且魯特琴才剛換過弦。當然，加博特男爵對駐軍編制之外提供的服務，會收取一筆小額費用。這堂課要七十五枚金幣。我知道這價錢有點高，不過部分費用是拿來支付練習用魯特琴本身的成本。你們還要上課嗎？

### (sub) DIAL_Z30#2737
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2738
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼就在附近。  這位ó吟遊藝人微弱的魯特琴聲引起了注意，@4喊他從藏身之處出來。這名吟遊詩人悶悶不樂地照做了……

### (sub) DIAL_Z30#2739
- speaker=45  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [63595..4]] -> node 4294901761
    - [flag 0x0101 in [64421..4]] -> node 4294901761
- text: 你們對音樂課改變主意了嗎？要是有位小姐對你拋媚眼，會彈魯特琴可是件方便的事！七十五枚金幣，或許能換來一夜銷魂。你們覺得如何？

### (sub) DIAL_Z30#2740
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [63624..4]] -> node 4294901835
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2741
- speaker=0  style=0
- effects:
    - push return-address key 325797 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2742
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [63682..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2743
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [63786..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_1_ENOUGH_GOLD

### (sub) DIAL_Z30#2744
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2745
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我話說得太早了。看來我沒帶夠付這堂課的錢。

### (sub) DIAL_Z30#2746
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我通常都在這附近，要是你們湊到了錢，我很樂意教你們。容我先失陪了，我正忙著替弟兄們準備一個新版本的〈ó她ó蜜色ó的ó眼眸〉。他們不喜歡我上次的編曲。

### (sub) DIAL_Z30#2747
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 祝你的新編曲順利。我們有空會再回來的。

### (sub) DIAL_Z30#2748
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [64313..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2749
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [64421..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_1_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2750
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2751
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很遺憾，我們還有別的事要辦。吟遊詩人，也許改天吧。

### (sub) DIAL_Z30#2752
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我通常都在這附近，要是你們湊到了錢，我很樂意教你們。容我先失陪了，我正忙著替弟兄們準備一個新版本的〈ó她ó蜜色ó的ó眼眸〉。他們不喜歡我上次的編曲。

### (sub) DIAL_Z30#2753
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 祝你的新編曲順利。我們有空會再回來的。

### (sub) DIAL_Z30#2754
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [64898..4]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2755
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [65001..4]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_1_NO_LESSONS

### (sub) DIAL_Z30#2756
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1057 a2=0
- branches:
    - [flag 0x1ecb in [606..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2757
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2758
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 樂音隨風飄來。  詹姆士一開始還以為自己是被旅途的勞頓給累糊塗了，隨即他分辨出附近一叢樹林裡，傳來〈ó賽瑟儂ó血染ó賽瑟儂〉那哀傷的旋律。音樂忽然停了下來，一個神情不悅的年輕人從樹上跳了下來，魯特琴斜背在背上……

### (sub) DIAL_Z30#2759
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好一陣子沒見到你們了。你們三個有沒有練習我之前教的東西？

### (sub) DIAL_Z30#2760
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 練了一點。我們一直忙著搜尋夜鷹會的下落。你知道他們的事嗎？

### (sub) DIAL_Z30#2761
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我盡量不去了解刺客公會的事。對這種事知道得太多的人，通常很快就會變成知道得太多的死人。你可以說我是膽小鬼，不過我還是傾向只談些不會危及性命的話題。

### (sub) DIAL_Z30#2762
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可以理解。你還在教音樂課嗎？

### (sub) DIAL_Z30#2763
- speaker=45  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [976..5]] -> node 4294901761
    - [flag 0x0101 in [1922..5]] -> node 4294901761
- text: 是啊。既然你們已經買過練習用的魯特琴了，這次只要二十枚金幣。還要繼續上課嗎？

### (sub) DIAL_Z30#2764
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2765
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼就在附近。  這位ó吟遊藝人微弱的魯特琴聲引起了注意，@4喊他從藏身之處出來。這名吟遊詩人悶悶不樂地照做了……

### (sub) DIAL_Z30#2766
- speaker=45  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [976..5]] -> node 4294901761
    - [flag 0x0101 in [1922..5]] -> node 4294901761
- text: 你們對音樂課改變主意了嗎？我保證能讓你們學到足以在家鄉朋友面前露一手的程度。你們覺得如何？

### (sub) DIAL_Z30#2767
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [1005..5]] -> node 4294901780
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2768
- speaker=0  style=0
- effects:
    - push return-address key 328714 (GoodBye target)
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2769
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [1063..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2770
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [1171..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_2_YES_ENOUGH_GOLD

### (sub) DIAL_Z30#2771
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2772
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我想我話說得太早了。看來我沒帶夠付這堂課的錢。

### (sub) DIAL_Z30#2773
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我通常都在這附近，要是你們湊到了錢，我很樂意教你們。容我先失陪了，駐軍裡有個弟兄拿了整本〈ó歐文ó深淵ó之ó統ó治〉的劇本給我，我正埋頭研究，看能不能把它簡化到讓一個人就能單獨演出。這會是個大工程，不過我相信應該辦得到。

### (sub) DIAL_Z30#2774
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有誰辦得到，我相信一定是你，坦尼。祝你好運。

### (sub) DIAL_Z30#2775
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [1810..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2776
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [1922..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_2_YES_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2777
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2778
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很遺憾，我們還有別的事要辦。吟遊詩人，也許改天吧。

### (sub) DIAL_Z30#2779
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我通常都在這附近，要是你們湊到了錢，我很樂意教你們。容我先失陪了，駐軍裡有個弟兄拿了整本〈ó歐文ó深淵ó之ó統ó治〉的劇本給我，我正埋頭研究，看能不能把它簡化到讓一個人就能單獨演出。這會是個大工程，不過我相信應該辦得到。

### (sub) DIAL_Z30#2780
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有誰辦得到，我相信一定是你。祝你好運，坦尼。

### (sub) DIAL_Z30#2781
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [2529..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2782
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [2624..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：CX_Tamney_Lesson_2_NO

### (sub) DIAL_Z30#2783
- speaker=0  style=0
- effects:
    - SET flag 0x1ed5=1
    - SET flag 0x1ecb=0
    - bind speaker-name slot (kind=0 sub=5)
    - GIVE item 'Q' cond=125 to member#2 (cost 750)
    - RAISE Barding of party by 3840
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2784
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 樂師，我們是您順從的學生。我已經知道魯特琴上音符的位置了，不過除此之外，我可是一頭霧水……

### (sub) DIAL_Z30#2785
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我相信是這樣。你身後就有一把魯特琴。  從中央C彈到G，用四分音符彈完整個音階，只彈加冕音，然後再彈回中央C。

### (sub) DIAL_Z30#2786
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1046 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很好。這就是王家音階。現在我要你彈同一個音階，不過把E加冕音換成E退位音。其餘的音符都一樣。

### (sub) DIAL_Z30#2787
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1047 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒錯。這就是貴族音階。王家音階跟貴族音階，合在一起就是我們大部分音樂的基礎，不過我們偶爾也會用女皇音階，也就是凱許音階。女皇音階的彈法是：C加冕音、D退位音、E退位音，接著F加冕音、G加冕音、A退位音、B加冕音，最後回到C加冕音。我知道聽起來很複雜，不過試試看吧……

### (sub) DIAL_Z30#2788
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1048 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你或許還是能學會魯特琴的。我要你每天花一個鐘頭，反覆練習我教你的東西。等你能彈得得心應手了，我們再上下一課。  抱歉，我得去準備幾首歌，明天晚上加博特男爵的晚宴要用。保重，繼續練習你的魯特琴。

### (sub) DIAL_Z30#2789
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。謝謝這堂課。

### (sub) DIAL_Z30#2790
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [4087..5]] -> node 4294901761

### (sub) DIAL_Z30#2792
- speaker=0  style=0
- effects:
    - SET flag 0x1ed6=1
    - TAKE gold -200
    - RAISE Barding of party by 2304
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2793
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 樂師，我們聽候您的吩咐。

### (sub) DIAL_Z30#2794
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 用我的備用魯特琴吧。就在你身後。  幫我個忙，先撥一下琴弦……

### (sub) DIAL_Z30#2795
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1049 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊，我就猜是這樣。我今天還沒來得及調音。好，撥一下最上面那根弦。既然我的調音叉上禮拜被人偷了，我們就姑且把那根弦稱作E弦。現在，把手指放在第一弦的第五格，同時撥第一弦跟第二弦。

### (sub) DIAL_Z30#2796
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1050 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好，這樣就對了。第二弦調好音了。試試用同樣的方法調第二弦跟第三弦。

### (sub) DIAL_Z30#2797
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1051 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 第三弦有點偏退位音。轉一下第三弦的調音栓，直到兩根弦的音和諧為止……

### (sub) DIAL_Z30#2798
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1052 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在試試第四弦……

### (sub) DIAL_Z30#2799
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1053 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很好。第五弦有點特殊。不是把手指放在第五格，而是把手指放在第四弦的第四格，同時撥第四弦跟第五弦。

### (sub) DIAL_Z30#2800
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1054 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 最後一根弦的調法跟第二弦一樣。手指放在第五弦的第五格，同時撥第五弦跟第六弦。

### (sub) DIAL_Z30#2801
- speaker=45  style=0
- effects:
    - ?wOp12 a1=1055 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 太好了……可惜我沒時間再教你別的了，不過至少你現在知道怎麼替樂器調音了——畢竟，要是你的魯特琴走音，別人怎麼知道你彈對了曲子呢？  抱歉，我得趕在明晚晚餐時間之前把編曲弄好，得先走了。繼續練習。你很有天賦。

### (sub) DIAL_Z30#2802
- speaker=244  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會的。謝謝這堂課。

### (sub) DIAL_Z30#2803
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [5894..5]] -> node 4294901761

### (sub) DIAL_Z30#2805
- speaker=0  style=0
- branches:
    - [flag 0x1ecb in [8926..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2806
- speaker=0  style=0
- effects:
    - SET flag 0x1aae=1
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2807
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，緊張地來回挪動著身子。

### (sub) DIAL_Z30#2808
- speaker=45  style=0
- effects:
    - ?wOp12 a1=130 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒想到會見到……我沒想到會有人……呃……

### (sub) DIAL_Z30#2809
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ……會來找你！呸！我早該想到的。你大搖大擺地跑進北衛城，帶著你那個叮叮咚咚的小盒子，滿嘴都是榮耀跟光榮的歌，可真到緊要關頭，你根本不是那麼回事。你身上有的，是一條膽小的黃線——你從來不敢正面直視自己的問題，只會任由別人牽著你的鼻子走。總有一天，會有人把你的人生一路牽到懸崖邊去……

### (sub) DIAL_Z30#2810
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是我自己決定要離開北衛城的。是我。這是吟遊詩人坦尼自己的決定，不是別人的。我決定要活下去。

### (sub) DIAL_Z30#2811
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 莫瑞德人連影子都還沒出現，就已經把你嚇跑了。他們對你的效果，比你以前交手過的任何公爵或男爵都管用。反正我也不想跟你這種懦夫待在同一座城堡裡。

### (sub) DIAL_Z30#2812
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這不公平。我是個吟遊詩人！我能有什麼用……我不會用劍，不會治傷，也不會指揮作戰……我只會礙事。我能有什麼用？我只是……一個……ó微不足道的……人。

### (sub) DIAL_Z30#2813
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼，你沒那麼微不足道。我去克朗多任職之前，我父親常常告誡我：等你贏得了頭銜，一定要好好善待你的吟遊詩人。我當時完全不明白這句話是什麼意思，直到我親眼見識了阿曼加、高堡、賽瑟儂，以及後來的其他幾場戰役。當士兵們坐下來聽關於偉大戰役的歌謠時，他們會想起像自己一樣的人，曾面對過可怕的危險，卻活著走了出來，而這會給他們帶來ó希望。有時候，這正是一支軍隊唯一需要的東西。

### (sub) DIAL_Z30#2814
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 可他們為什麼非得依靠我不可？命運為什麼偏偏安排我這個吟遊詩人，恰好人在北衛城？

### (sub) DIAL_Z30#2815
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼，我們不會強迫你留下的。這是你的人生，你的決定。要是你選擇離開……那是你自己的事。

### (sub) DIAL_Z30#2816
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在我做出最終決定之前，能請你們幫我一個忙嗎？

### (sub) DIAL_Z30#2817
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 只要能讓你重新踏上回北衛城的路，什麼都行。

### (sub) DIAL_Z30#2818
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 離這裡不遠有個洞穴，人稱『占卜者廳堂』。裡頭有幾顆小石頭——占地師稱之為『命紋石』——能預知一個人的未來。要是你們帶一顆回來，我就做出決定。

### (sub) DIAL_Z30#2819
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 占地術！早該猜到你會信這套裝神弄鬼的玩意兒……不過又是另一種讓別的東西替你做出艱難決定的辦法罷了！

### (sub) DIAL_Z30#2820
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 派特魯斯，安靜點。坦尼，我們會看看能做些什麼。

### (sub) DIAL_Z30#2821
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [8826..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2822
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [8926..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C5_Tamney_the_Minstrel

### (sub) DIAL_Z30#2823
- speaker=0  style=0
- branches:
    - [flag 0xc3ac in [8955..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2824
- speaker=0  style=0
- effects:
    - event_bitmap_hi[20] bitop
    - SET flag 0x0081=1
    - SET flag 0x1a9b=1
    - REMOVE item '\\' cond=0
    - GIVE item '7' cond=100 to member#6 (cost 0)
    - GIVE item '7' cond=100 to member#6 (cost 0)
    - GIVE item '7' cond=100 to member#6 (cost 0)
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2825
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2826
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們去過占卜者廳堂了嗎？有帶命紋石回來嗎？

### (sub) DIAL_Z30#2827
- speaker=6  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼，別自己嚇自己了。你那些傻石頭我們拿到了……那，你是自己走回北衛城，還是要我們拖你回去？

### (sub) DIAL_Z30#2828
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 等我……研究過這顆石頭之後，我會自己走回去的。告訴加博特男爵，我很快就會到。我想他鬆的那口氣，大概會比你們想像的還要大。

### (sub) DIAL_Z30#2829
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢？為什麼這麼說？

### (sub) DIAL_Z30#2830
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我離開城堡之前，心裡就打定主意，至少得先安排好能讓自己活下去的東西才走。就算我能神不知鬼不覺地溜出城堡，也還是得面對一個問題：在抵達安全的地方之前，我要靠什麼過活。所以，調查了一番之後，我找到了金庫。看守金庫的是個叫科比的傢伙，過去幾個月來，我一直暗中撮合他跟一個叫席雅的姑娘幽會，樂在其中。我讓他相信她正在等他之後，溜進去抓走一個錢袋，便是輕而易舉的事了。

### (sub) DIAL_Z30#2831
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 男爵大概也不會少掉幾枚金幣就發現。我看他現在忙著別的事。

### (sub) DIAL_Z30#2832
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我當初也是這麼想的，可看來我在黑暗中抓走的東西，價值遠不止幾十枚金幣。是好幾ñ百枚……我一意識到自己做了什麼，就嚇得不敢回去了。

### (sub) DIAL_Z30#2833
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我能理解你為什麼會怕，不過男爵叫我們來找你的時候，完全沒提到錢財失竊的事。很有可能到現在都還沒人發現這筆錢不見了。你可以把錢還給他……

### (sub) DIAL_Z30#2834
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不能。就算我把錢還回去，男爵還是會知道，是科比擅離職守，讓我有機可乘。雖然我這樣做，實在算不上是他的朋友，可我不想再用同一樁罪，背叛他第二次……其實，我有件事得向你們坦白。我請你們替我找那些占地石頭，正是為了他。就算是對寶石商來說，那些石頭也不值幾個錢，可它們能用來做一枚吸引人的結婚戒指石……

### (sub) DIAL_Z30#2835
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 是為了科比。原來如此。這麼說，你這段時間一直在考慮要回去，只是想先把所有可能的狀況都安排妥當。

### (sub) DIAL_Z30#2836
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 除了一件事之外都安排好了。我在想，你們能不能把這袋鑽石收下，等這場戰事結束之後再說。這樣一來，誰都不會受傷，我們也都能做各自該做的事。就跟他說，這是你們從一個死掉的夜鷹會成員身上搜出來的，還是隨便編個理由……

### (sub) DIAL_Z30#2837
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你回城堡的時候，既然你的行為有點不對勁，他們有可能會搜你的身。這些鑽石我先收下，不過我晚點再來煩惱怎麼跟他說。我唯一在意的是，你得立刻回去。我們還有其他事要替馬丁公爵去辦。

### (sub) DIAL_Z30#2838
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就這麼說定了。我們城堡裡見。

### (sub) DIAL_Z30#2839
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼，你可別太得意了。你跟我以後有一筆大帳要算。別讓自己在回去的路上送了命。

### (sub) DIAL_Z30#2840
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [12403..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2841
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [12513..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C5_Tamney_the_Minstrel_WITH_STONE

### (sub) DIAL_Z30#2842
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1057 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2843
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2844
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們帶命紋石回來了嗎？

### (sub) DIAL_Z30#2845
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們還沒找到。你到底覺得自己能從這些石頭裡看出什麼？

### (sub) DIAL_Z30#2846
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我在北衛城這場戰事裡能不能活下來。要是不能，我得先給親人捎個信。

### (sub) DIAL_Z30#2847
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你真心相信盯著一顆石頭看就能告訴你這種事？這大概是我聽過最蠢的事了。

### (sub) DIAL_Z30#2848
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 他有權利有蠢念頭。他要是想坐在這兒，等一顆石頭告訴他外頭安不安全再出來，那也隨他去。我看就讓他自生自滅吧。

### (sub) DIAL_Z30#2849
- speaker=45  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們休想用羞辱來逼我做決定，你們兩個乾脆省省吧。你們也許是紳爵，可眼下，我對石頭的敬重，都比對你們兩個說的任何話還多。再見。

### (sub) DIAL_Z30#2850
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 坦尼，等等……

### (sub) DIAL_Z30#2851
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [13625..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2852
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [13738..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C5_Tamney_the_Minstrel_WITHOUT_STONE

### (sub) DIAL_Z30#2853
- speaker=0  style=0
- branches:
    - [flag 0x1ecc in [15076..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2854
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2855
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2856
- speaker=46  style=0
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這男孩看起來有法師的樣子。他有沒有受過……教育？

### (sub) DIAL_Z30#2857
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我小時候有過幾位家教——我父親請他們到我們莊園來的——我曾經有位教過我的老師，叫派特魯斯，在提……

### (sub) DIAL_Z30#2858
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 哈哈。背景真了不起啊，年輕的朋友。

### (sub) DIAL_Z30#2859
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文……拜託，你別這麼愛吹噓。別人會以為你是什麼了不起的人物。  老闆，你怎麼會對我姪兒的教育這麼感興趣？你是在替自己的孩子找家教嗎？

### (sub) DIAL_Z30#2860
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒有孩子，至少我知道的沒有。我只是擔心一個有天賦的男孩會被埋沒。

### (sub) DIAL_Z30#2861
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 到目前為止，我這個不成材的姪兒展現出來的唯一天賦，就是吃得太多、抱怨得太多。我向你保證，他絕不會被埋沒在任何事上。

### (sub) DIAL_Z30#2862
- speaker=46  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [15519..5]] -> node 4294901761
    - [flag 0x0101 in [16311..5]] -> node 4294901761
- text: 這我完全相信。要不要考慮吃點什麼？我本想提供新鮮的東西，可昨晚有個小偷溜了進來，偷走了我們大部分的存糧。我這裡還有些舊存糧，你們可以碰碰運氣。

### (sub) DIAL_Z30#2863
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1037 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2864
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2865
- speaker=46  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [flag 0x0100 in [15519..5]] -> node 4294901761
    - [flag 0x0101 in [16311..5]] -> node 4294901761
- text: 這我完全相信。要不要考慮吃點什麼？我本想提供新鮮的東西，可昨晚有個小偷溜了進來，偷走了我們大部分的存糧。我這裡還有些舊存糧，你們可以碰碰運氣。

### (sub) DIAL_Z30#2866
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [15548..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2867
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2868
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拿給我們吧。我想錢應該夠。

### (sub) DIAL_Z30#2869
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你們做這筆生意。

### (sub) DIAL_Z30#2870
- speaker=0  style=0
- effects:
    - SET flag 0x1ecc=1
    - END conversation, result=65534

### (sub) DIAL_Z30#2871
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [15743..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2872
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [15838..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C1_Joftaz_ENOUGH_GOLD

### (sub) DIAL_Z30#2873
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2874
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃……唔。看來我錢不太夠。我看這次就先算了。

### (sub) DIAL_Z30#2875
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我在這裡待了很多年了，我相信未來也還會待很多年。你們要是想跟喬夫塔茲買東西，我會在這裡。

### (sub) DIAL_Z30#2876
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興知道這一點。我們會設法再回來的。

### (sub) DIAL_Z30#2877
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [16212..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2878
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [16311..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C1_Joftaz_NOT_ENOUGH_GOLD

### (sub) DIAL_Z30#2879
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2880
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 舊存糧聽起來就不太妙……不用了，謝謝，老闆。也許等你進了新鮮的存糧再說。

### (sub) DIAL_Z30#2881
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 悉聽尊便，陌生人。喬夫塔茲跟錨首酒館會一直在這裡，等著你們回來。

### (sub) DIAL_Z30#2882
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興知道這一點。謝謝。

### (sub) DIAL_Z30#2883
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [16658..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2884
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [16750..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C1_Joftaz_DONT_BUY

### (sub) DIAL_Z30#2885
- speaker=0  style=0
- branches:
    - [flag 0x1ecc in [18437..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2886
- speaker=0  style=0
- branches:
    - [flag 0x9c42 in [16808..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2887
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝酒保打了個手勢。  這名男子從他正在清洗的酒杯中抬起頭，朝他們的方向露出微笑，顯然很高興又有客人上門。可他那歡迎的表情，隨即轉為混雜著恐懼與憤怒的神色，開始用一種@4聽不懂的語言，朝他們尖聲喊叫……

### (sub) DIAL_Z30#2888
- speaker=46  style=0
- effects:
    - ?wOp12 a1=1044 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: óRuthi óa'dibi óabas！瘟疫！瘟疫啊！

### (sub) DIAL_Z30#2889
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拜託……我跟同伴生病了，需要幫助。我們去哪能找到懂得治病的人？

### (sub) DIAL_Z30#2890
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 沒有人能治好你們！『穿梭人心之舞者』已經標記你們，要你們共赴她的死亡之舞了，沒有人能救你們！快走吧，拜託，趁還沒把病傳給我之前！

### (sub) DIAL_Z30#2891
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是一位女神標記了我們，那也只有女神才能救我們。附近有什麼神殿？這一帶的守護女神是誰？

### (sub) DIAL_Z30#2892
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的人手很快就會到！你們留在這兒會後悔的……

### (sub) DIAL_Z30#2893
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 告訴我最近的神殿在哪，不然我就過去把你按在地上，跟同伴輪流朝你喉嚨裡吐口水，直到你也染上這種病為止！神殿在哪？！

### (sub) DIAL_Z30#2894
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 迷霧惡魔號停在港裡，有時候會載乘客去神殿島上的埃奧提斯神殿。船上那個人會跟你們要十枚金幣。我希望那艘船撞毀，把你們三個一起帶去送死！現在滾吧！

### (sub) DIAL_Z30#2895
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也是時候了。等著我們再來拜訪吧，老闆。

### (sub) DIAL_Z30#2896
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [18321..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2897
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [18408..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C2_Joftaz

### (sub) DIAL_Z30#2898
- speaker=0  style=0
- effects:
    - SET flag 0x1ecc=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2899
- speaker=0  style=6
- effects:
    - ?wOp12 a1=1044 a2=0
- branches:
    - [flag 0x1fc8 in [18937..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們……

### (sub) DIAL_Z30#2900
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們會給我們所有人招來厄運……我不想做你們的生意！

### (sub) DIAL_Z30#2901
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你為什麼希望我們離開？

### (sub) DIAL_Z30#2902
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們既然在這裡，想必是跟替爬行者做事的人打過交道了。凡是招惹過他的人都會死。

### (sub) DIAL_Z30#2903
- speaker=5  style=0
- effects:
    - SET flag 0x1fc8=1
- branches:
    - [always] -> node 0 (no jump)
- text: 你該不會是指幾個ñ在鎮外守著的人吧？

### (sub) DIAL_Z30#2904
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我不會再跟你們多說了。我還想活著……

### (sub) DIAL_Z30#2905
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我能理解你的恐懼。我暫時不會再問你問題了。

### (sub) DIAL_Z30#2906
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [19144..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2907
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [19230..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C2_Joftaz

### (sub) DIAL_Z30#2908
- speaker=0  style=0
- branches:
    - [flag 0x1ecc in [22869..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2909
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2910
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2911
- speaker=5  style=0
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 身為酒館老闆，我想這裡的人來人往應該不少，很多人想買賣一些——這麼說吧——來路不明的東西？要是我對這方面感興趣，該找誰談？

### (sub) DIAL_Z30#2912
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 街上隨便一個人都行。錫爾登的顧客可不以名聲清白著稱，這你想必也看出來了。你為什麼對這個感興趣？

### (sub) DIAL_Z30#2913
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我需要打聽兩件非常特別的物品，可能在錫爾登這裡被人買走了。我在找可能賣掉它們的人。

### (sub) DIAL_Z30#2914
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是有東西在錫爾登出售，那我就是你唯一該找的人。其他的交易，都是照錫爾登的規矩來的。

### (sub) DIAL_Z30#2915
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 好吧，喬夫塔茲。我需要知道你對一支黃銅望遠鏡或一隻銀蜘蛛了解多少。我願意付金子。

### (sub) DIAL_Z30#2916
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你當然得為這個消息付出代價，不過我對你們王國的錢幣沒興趣。要是要金子，我自己就能湊出想要的數目。不，我需要的是一個竊賊的協助。

### (sub) DIAL_Z30#2917
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你為什麼覺得我能幫上忙？

### (sub) DIAL_Z30#2918
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我住在一座竊賊之城。我這輩子都在鍛鍊嗅出竊賊的本事，我非常確定你有竊賊的直覺。這就是我的條件。我會告訴你我偶爾出售的銀蜘蛛的事，你則要幫我找到一包被爬行者偷走的粉末。  那東西很可能已經被帶去他這附近的宅邸了。那棟房子是上鎖的，我猜那袋粉末大概被藏在某個箱子或櫃子之類的地方。

### (sub) DIAL_Z30#2919
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨便一個竊賊都能替你辦這件事。為什麼ó我們特別適合幹這個？

### (sub) DIAL_Z30#2920
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 因為這地方的竊賊——他們全都是爬行者的耳目。替我做事，對他們來說就等於是死路一條。

### (sub) DIAL_Z30#2921
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 為什麼？這袋粉末裡到底是什麼？

### (sub) DIAL_Z30#2922
- speaker=46  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [21544..5]] -> node 4294901761
    - [flag 0x0101 in [22133..5]] -> node 4294901761
- text: 我的提議已經說了。用消息換那個袋子。成交嗎？

### (sub) DIAL_Z30#2923
- speaker=0  style=0
- branches:
    - [flag 0x1f9e in [21573..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2924
- speaker=0  style=0
- branches:
    - [flag 0xc383 in [25206..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2925
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2926
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我的直覺告訴我不該答應這件事，不過喬夫塔茲，成交。我會替你找到那個袋子。乾脆俐落地交換，消息換物品。

### (sub) DIAL_Z30#2927
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 那就這麼說定了。我會在錨首酒館這裡等你們，直到你們帶著東西回來。

### (sub) DIAL_Z30#2928
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會回來的。別離開這裡。

### (sub) DIAL_Z30#2929
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [22024..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2930
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [22133..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Joftaz_YES_DEAL_HAS_NO_POUCH

### (sub) DIAL_Z30#2931
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2932
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 曾幾何時，我被認為是克朗多最好的竊賊，不過那早已是過去式了。我現在是亞魯莎親王宮廷裡的紳爵，我可是拚了命才配得上這個頭銜的……

### (sub) DIAL_Z30#2933
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這我不懷疑，不過我想，要是你真心想知道你問的那些事，你會改變主意的。錫爾登沒有哪個包打聽比喬夫塔茲知道得更多，也很少有人能像我這麼容易收買。我很確定我們還會再見面的。

### (sub) DIAL_Z30#2934
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你這份傲慢，總有一天會給你惹來麻煩。別自以為能看透別人的心思。祝你愉快。

### (sub) DIAL_Z30#2935
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [22774..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2936
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [22869..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C3_Joftaz_NO_DEAL

### (sub) DIAL_Z30#2937
- speaker=0  style=0
- branches:
    - [flag 0x1ed7 in [24475..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2938
- speaker=0  style=0
- branches:
    - [flag 0x1f9e in [22927..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2939
- speaker=0  style=0
- branches:
    - [flag 0xc383 in [22956..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2940
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2941
- speaker=46  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=1002 a2=0
    - ?wOp12 a1=108 a2=0
- branches:
    - [flag 0x0100 in [25206..5]] -> node 4294901761
    - [flag 0x0101 in [23878..5]] -> node 4294901761
- text: 這麼說，克朗多那位尊貴的紳爵回來了。你把我要的那個袋子帶來了嗎？

### (sub) DIAL_Z30#2942
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2943
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2944
- speaker=46  style=0
- effects:
    - ?wOp12 a1=1002 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜你們是為了我們談過的那件東西來的。你們找得ó真快啊。

### (sub) DIAL_Z30#2945
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 在你開口問之前，先說，我們還沒找到。我只是希望你能對……多透露一點……

### (sub) DIAL_Z30#2947
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2948
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，不……我們還沒找到。他那棟房子很難進去。我們原本希望，要是你能多跟我們說說錫爾登跟這裡的人……

### (sub) DIAL_Z30#2949
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們想把我當傻子耍，可我在水手堆裡混得夠久了，這種把戲騙不了我。我們的約定不變。在你們把我要的那袋粉末還給我之前，喬夫塔茲什麼都不會說。

### (sub) DIAL_Z30#2950
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我們……呃……找到了，我們會還給你的。祝你愉快。

### (sub) DIAL_Z30#2951
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [24382..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2952
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [24475..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Joftaz_SAY_NO

### (sub) DIAL_Z30#2953
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2954
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2955
- speaker=46  style=0
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 非常感謝你們的惠顧，不過我得警告你們，再來錨首酒館走動可能會……有危險？既然你們已經把我的袋子還回來了，他們就會開始搜尋偷走它的賊，而我肯定沒那個本事幹這種事。你們最好盡快離開。

### (sub) DIAL_Z30#2956
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 也許你說得對。祝你愉快。

### (sub) DIAL_Z30#2957
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [25095..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2958
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [25206..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HM_C3_Joftaz_YES_GAVE_POUCH_TO_JOFTAZ

### (sub) DIAL_Z30#2959
- speaker=0  style=0
- effects:
    - SET flag 0x1ed7=1
    - REMOVE item '3' cond=1
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2960
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 看來今天巴納斯神對我們倆都露出了笑容。我有你們想要的東西，你們顯然也知道我需要知道的事。袋子換故事，這就是我們的約定。我想聽一個關於銀蜘蛛的故事。

### (sub) DIAL_Z30#2961
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 嘿。沒錯，巴納斯神確實眷顧了你們。我還真沒想過有誰能狡猾到擊敗爬行者，不過既然這位『快活的惡作劇者』賜給了你們這份本事，我就樂意盡力幫幫你們。好了——銀蜘蛛是件稀罕物，所以每次拿到一件我都會記得，能靠它賺一筆，我肯定很高興。這東西在王國這邊需求可旺了。我上一次賣出一件，已經是好幾個月前的事了。

### (sub) DIAL_Z30#2962
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你能形容一下最後買走的那個人嗎？

### (sub) DIAL_Z30#2963
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢，能，我能形容他。駝著背，粗魯無禮，討價還價很兇的傢伙。他披著一件黑斗篷，胸口上有隻鳥的圖案——一隻老鷹。

### (sub) DIAL_Z30#2964
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你是說鷹嗎？一隻金鷹？

### (sub) DIAL_Z30#2965
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我這輩子大半時間都待在錫爾登。可能是鷹，也可能是鷗。我只知道，那天我在他跟一個叫阿布克的商人之間，虧了不少——阿布克帶來了幾件從惡作劇石那邊順來的水手小玩意兒。至於胸口有鳥圖案的那個人，我最後聽到他的消息時，他正打算買一張前往克朗多、名叫『嘲弄者的愚行號』的船票。

### (sub) DIAL_Z30#2966
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一個要去克朗多的夜鷹會成員？我上哪能找到那艘船的船長？

### (sub) DIAL_Z30#2967
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我猜是克朗多吧，不過我不明白這對你們有什麼重要的。

### (sub) DIAL_Z30#2968
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼重要、什麼不重要，由我來決定。那，黃銅望遠鏡呢？你對那個有了解嗎？

### (sub) DIAL_Z30#2969
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就像我先前跟你們說的，水手的小玩意兒在錫爾登很常見。要是你們想要的是件特別的望遠鏡，我建議你們去找那個商人阿布克。這種東西我頂多也就賺個五、十枚金幣，所以我覺得不太值得ñ花時間去管它。

### (sub) DIAL_Z30#2970
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 喬夫塔茲，你會發現，經手銀蜘蛛的代價，恐怕比你想像的還要慘重。要是我回去以後發現親王家裡有誰死於中毒，你要擔心的可就不只是賺不賺得到錢了。

### (sub) DIAL_Z30#2971
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [27621..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2972
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：GIVE_POUCH_TO_JOFTAZ // END GIVING JOFTAZ THE POUCH

### (sub) DIAL_Z30#2973
- speaker=0  style=0
- branches:
    - [flag 0x1ecc in [28197..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2974
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2975
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2976
- speaker=46  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [flag 0x0100 in [28640..5]] -> node 4294901761
    - [flag 0x0101 in [29348..5]] -> node 4294901761
- text: 這我完全相信。要不要考慮吃點什麼？我本想提供新鮮的東西，可昨晚有個小偷溜了進來，偷走了我們大部分的存糧。我這裡還有些舊存糧，你們可以碰碰運氣。

### (sub) DIAL_Z30#2977
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2978
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名男子走了過來，加入他們。他站在他們面前，饒富興味地挑起眉毛。

### (sub) DIAL_Z30#2979
- speaker=46  style=0  flags=paged-text
- effects:
    - ?wOp12 a1=108 a2=0
- branches:
    - [flag 0x0100 in [28640..5]] -> node 4294901761
    - [flag 0x0101 in [29348..5]] -> node 4294901761
- text: 這我完全相信。要不要考慮吃點什麼？我本想提供新鮮的東西，可昨晚有個小偷溜了進來，偷走了我們大部分的存糧。我這裡還有些舊存糧，你們可以碰碰運氣。

### (sub) DIAL_Z30#2980
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [28669..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2981
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 拿給我們吧。我想錢應該夠。

### (sub) DIAL_Z30#2982
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 很高興跟你們做這筆生意。

### (sub) DIAL_Z30#2983
- speaker=0  style=0
- effects:
    - SET flag 0x1ecc=1
    - END conversation, result=65534

### (sub) DIAL_Z30#2984
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [28845..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2985
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [28928..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Joftaz

### (sub) DIAL_Z30#2986
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 呃……唔。看來我錢不太夠。我看這次就先算了。

### (sub) DIAL_Z30#2987
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我在這裡待了很多年了，我相信未來也還會待很多年。你們要是想跟喬夫塔茲買東西，我會在這裡。

### (sub) DIAL_Z30#2988
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝。我們或許會再回來。

### (sub) DIAL_Z30#2989
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29265..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2990
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [29348..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Joftaz

### (sub) DIAL_Z30#2991
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 舊存糧聽起來就不太妙……不用了，謝謝，老闆。也許等你進了新鮮的存糧再說。

### (sub) DIAL_Z30#2992
- speaker=46  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 悉聽尊便，陌生人。喬夫塔茲跟錨首酒館會一直在這裡，等著你們回來。

### (sub) DIAL_Z30#2993
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 唔。我會記住你的提議的。

### (sub) DIAL_Z30#2994
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [29678..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2995
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [29761..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：C6_Joftaz

### (sub) DIAL_Z30#2996
- speaker=0  style=0
- branches:
    - [flag 0x1ecd in [30573..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2997
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#2998
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#2999
- speaker=47  style=0
- effects:
    - ?wOp12 a1=120 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎光臨六趾客棧。有什麼我能為你們做的？

### (sub) DIAL_Z30#3000
- speaker=1  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這裡怎麼還有店開著？我還以為萊亞姆王協助撤離賽瑟儂的時候，大家都收拾東西離開了。

### (sub) DIAL_Z30#3001
- speaker=47  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [35700..5]] -> node 4294901761
    - [flag 0x0101 in [36290..5]] -> node 4294901761
- text: 你也看到了，不是所有人都走了，而且自從我父親過世以後，要撐下去也不容易。不過我現在不太想談這個。你們想吃點什麼嗎？我剛準備了些口糧，一份只要七枚金幣。拜託說願意吧。要我幫你們拿一些嗎？

### (sub) DIAL_Z30#3002
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3003
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3004
- speaker=47  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [35700..5]] -> node 4294901761
    - [flag 0x0101 in [36290..5]] -> node 4294901761
- text: 又見面了。你們想吃點什麼嗎？我準備了些口糧，就像我之前說的，一份只要七枚金幣。拜託說願意吧。要我幫你們拿一些嗎？

### (sub) DIAL_Z30#3005
- speaker=0  style=0
- branches:
    - [event_bitmap_hi[8] (xor=0x27 mask=0x87 mode=5 chapters=-)] -> node 4278256640
    - [event_bitmap_hi[8] (xor=0xbb mask=0x83 mode=5 chapters=-)] -> node 4278256128
    - [event_bitmap_hi[8] (xor=0x63 mask=0x81 mode=5 chapters=-)] -> node 4278255872
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3006
- speaker=0  style=0
- effects:
    - SET flag 0x00a2=1
    - event_bitmap_hi[8] bitop
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3007
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3008
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你好，我能不能買……

### (sub) DIAL_Z30#3009
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我沒法把店打開！我不管你們出多少錢，也不管你們是誰。我沒法再進去那裡了……

### (sub) DIAL_Z30#3010
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 小姐，我剛才是ñ想請妳喝一杯。

### (sub) DIAL_Z30#3011
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 噢……噢，抱歉。我還以為你們是要來我對街的雜貨店買東西的。自從我父親過世以後，我就一手打理著這兩間店，這間酒館跟對街的雜貨店。你知道嗎，一直有人到這兒來，上次算下來一週有四個，都想出錢買一把北方隱士打造的劍。我這人真傻，把消息放了出去，可那是在我店裡開始發生怪事之前的事了。從那之後，我就把店暫時關了起來。

### (sub) DIAL_Z30#3012
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 把店關了？為什麼？裡頭發生了什麼事？

### (sub) DIAL_Z30#3013
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們會覺得我很傻……我ó自己也覺得傻。

### (sub) DIAL_Z30#3014
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 告訴我吧，我會聽的。要是我笑了哪怕一次，妳都可以把一桶麥酒倒扣在我頭上。

### (sub) DIAL_Z30#3015
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是我真那麼做，你可得賠這桶酒錢……好吧，那我告訴你。過去這幾週，我看見一個男人在我店裡鬼鬼祟祟地走動。

### (sub) DIAL_Z30#3016
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這簡單。我跟同伴聯手，明天晚餐時間之前就能替妳把那個鬼祟的傢伙解決掉。

### (sub) DIAL_Z30#3017
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們辦得到嗎？你們就這麼輕鬆地能刺穿鬼魂，閒暇之餘還能拿斧頭劈劈騷靈？

### (sub) DIAL_Z30#3018
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 鬼魂？妳說的這個鬼祟傢伙是個鬼？

### (sub) DIAL_Z30#3019
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 就說你們不會相信我。不過我把話說清楚。要是你們能想辦法讓我店裡那個鬼魂安息，我就重新開店，把我跟那隱士買的蓋隆「悲愴使者」給你們。就這麼簡單。

### (sub) DIAL_Z30#3020
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這提議幾乎跟提出它的這位女士一樣誘人。謝謝妳，美麗的女士。

### (sub) DIAL_Z30#3021
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [33084..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3022
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33123..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3023
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1056 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3024
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3025
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 希望你們不是為了喝一杯才來酒館的。我今天早上把最後的存貨用光了，也不知道貨車什麼時候才會再來。沒人願意靠近『妮雅雜貨』，就算它其實只在十字路口對面而已！

### (sub) DIAL_Z30#3026
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們會盡力而為的，夫人。

### (sub) DIAL_Z30#3027
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [33684..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3028
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [33723..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3029
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3030
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3031
- speaker=47  style=0
- effects:
    - ?wOp12 a1=120 a2=0
    - SET flag 0x1ecd=0
    - event_bitmap_hi[8] bitop
    - GIVE item '\x13' cond=100 to member#6 (cost 0)
- branches:
    - [always] -> node 0 (no jump)
- text: 我不知道你們是怎麼辦到的，不過真是謝天謝地。我這幾個鐘頭都沒再聽見店裡傳來敲擊聲或撞擊聲了！這是這幾週來第一次！等我打掃一下灰塵，應該就能重新開店做生意了。既然你們履行了自己那部分的約定，我也會履行我的。就像你們要求的，我把我跟你們說過的蓋隆「悲愴使者」給你們。再次謝謝你們，歡迎隨時來對街的店裡逛逛。我保證會給你們找得到的最優惠的價錢！

### (sub) DIAL_Z30#3032
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝妳，好心的女士。能為妳效勞是我們的榮幸。

### (sub) DIAL_Z30#3033
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [34560..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3034
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [34599..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3035
- speaker=0  style=0
- branches:
    - [flag 0x1ecd in [35199..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3036
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3037
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3038
- speaker=47  style=0
- effects:
    - ?wOp12 a1=120 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎光臨六趾客棧。有什麼我能為你們做的？

### (sub) DIAL_Z30#3039
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 這個嘛，既然這裡是酒館，我們又有點口渴，我想我們就進來吃點東西……

### (sub) DIAL_Z30#3040
- speaker=47  style=0  flags=paged-text
- branches:
    - [flag 0x0100 in [35700..5]] -> node 4294901761
    - [flag 0x0101 in [36290..5]] -> node 4294901761
- text: 我剛準備了些口糧，一份只要七枚金幣。拜託說願意吧。要我幫你們拿一些嗎？

### (sub) DIAL_Z30#3041
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1041 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3042
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3043
- speaker=47  style=0
- effects:
    - ?wOp12 a1=120 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 啊哈！我就有預感會再見到你們三個。那，來份新鮮的餐點如何？這樣行嗎？

### (sub) DIAL_Z30#3044
- speaker=5  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我們其實沒空坐下來吃飯。妳有一般的口糧嗎？

### (sub) DIAL_Z30#3045
- speaker=47  style=0
- effects:
    - SET flag 0x1ecd=1
    - END conversation, result=65534
- text: 這一帶最好的，就在克朗多這邊……

### (sub) DIAL_Z30#3046
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [36036..5]] -> node 262144
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3047
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 既然妳問得這麼客氣，我要是拒絕就太不紳士了。我們要@3。

### (sub) DIAL_Z30#3048
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 稍等一下，我盡快去拿。

### (sub) DIAL_Z30#3049
- speaker=0  style=0
- effects:
    - SET flag 0x1ecd=1
    - END conversation, result=65534

### (sub) DIAL_Z30#3050
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [35960..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3051
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36036..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Nia

### (sub) DIAL_Z30#3052
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很想接受妳的提議，不過恐怕我現在手頭有點緊。也許我們晚點再過來。

### (sub) DIAL_Z30#3053
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [36214..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3054
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36290..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Nia

### (sub) DIAL_Z30#3055
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 謝謝，不過不用了。我想我們目前的存糧還算充足。也許改天吧。

### (sub) DIAL_Z30#3056
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 你們會回來的。六趾客棧的價錢是這一帶最優惠的，我相當確定我們還會再見面……還有，要是你們遇到一個叫洛克利爾的人，能不能替我向他問聲好？這對我來說意義重大。

### (sub) DIAL_Z30#3057
- speaker=255  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。祝妳愉快。

### (sub) DIAL_Z30#3058
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [36730..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3059
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [36806..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：Nia

### (sub) DIAL_Z30#3060
- speaker=0  style=0
- branches:
    - [flag 0x1ecd in [39509..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3061
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3062
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3063
- speaker=47  style=0
- effects:
    - ?wOp12 a1=120 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歡迎光臨六趾客棧，還有……噢，又見面了！自從你們上次路過以後就沒再見過了。我記得你們當時正急著趕往克朗多……啊，你是叫奧瑞爾吧？你這位精靈朋友是索爾加斯？

### (sub) DIAL_Z30#3064
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 什麼？噢，對……索爾加斯沒錯，不過ó我的名字是歐文。我們又路過這裡，想說進來歇歇腳，吃點東西。

### (sub) DIAL_Z30#3065
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 要是你們想歇腳，儘管坐，不過我的食物全都被徵用了。

### (sub) DIAL_Z30#3066
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: ó被徵用了？被誰徵用的？

### (sub) DIAL_Z30#3067
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 被克朗多長槍騎兵團，至少那位隊長是這麼說的。他說親王要求我把存糧交給他們。他們當然也給了我補償，一千枚金幣……

### (sub) DIAL_Z30#3068
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 恭喜！對這筆意外之財有什麼打算嗎？

### (sub) DIAL_Z30#3069
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 不，沒什麼特別的。我想我會專心把這裡收拾整齊，說不定再找個瀟灑的年輕紳爵或準男爵，需要個有錢的情婦。

### (sub) DIAL_Z30#3070
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我排第幾位？

### (sub) DIAL_Z30#3071
- speaker=47  style=0  flags=paged-text
- branches:
    - [flag 0x0104 in [38450..5]] -> node 4294901761
    - [flag 0x0105 in [39066..5]] -> node 4294901761
- text: 抱歉，不過我心裡已經有人選了。不如我用一瓶波特酒補償你，如何？顯然我不能讓那些士兵把東西全拿走，所以我留了幾瓶下來賣，等這裡補貨為止。你要不要看看有什麼存貨？

### (sub) DIAL_Z30#3072
- speaker=0  style=0
- branches:
    - [flag 0x7531 in [38797..5]] -> node 262144
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3073
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 一瓶聽起來不錯，是吧，戈……索爾加斯。我正好需要點東西潤潤喉嚨裡的沙塵。

### (sub) DIAL_Z30#3074
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 當然。沒問題。

### (sub) DIAL_Z30#3075
- speaker=2  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 歐文，我不確定這樣做明不明智。

### (sub) DIAL_Z30#3076
- speaker=47  style=0
- effects:
    - SET flag 0x1ecd=1
    - END conversation, result=65534
- text: 噢，別掃興嘛……我去後面幫你們拿瓶酒。

### (sub) DIAL_Z30#3077
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 我很想接受妳的提議，不過恐怕我現在手頭有點緊。也許我們改天再過來。

### (sub) DIAL_Z30#3078
- speaker=0  style=0
- branches:
    - [flag 0x1ea8 in [38982..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3079
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [39066..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Nia

### (sub) DIAL_Z30#3080
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 現在不用了，謝謝。我們其實該上路了。

### (sub) DIAL_Z30#3081
- speaker=47  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 隨你們便。要是你們口渴了，我就在附近。要是你們想進對街的店，我會過去幫你們開門。再見。

### (sub) DIAL_Z30#3082
- speaker=3  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 妳的善心總有一天會得到回報的。謝謝妳。

### (sub) DIAL_Z30#3083
- speaker=0  style=0
- effects:
    - SET flag 0x1ecd=1
- branches:
    - [flag 0x1ea8 in [39425..5]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3084
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [flag 0x1ea7 in [39509..5]] -> node 4294901761
    - [always] -> node 0 (no jump)
- text: 這是對話路徑的結尾：HNM_C6_Nia

### (sub) DIAL_Z30#3085
- speaker=0  style=0
- effects:
    - ?wOp12 a1=1038 a2=0
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3086
- speaker=0  style=6
- branches:
    - [always] -> node 0 (no jump)
- text: @4朝房間另一頭的身影打了個手勢。  那名女子點了點頭，穿過木地板走了過來，最後站到了他們面前。

### (sub) DIAL_Z30#3087
- speaker=47  style=0  flags=paged-text
- branches:
    - [flag 0x0104 in [38450..5]] -> node 4294901761
    - [flag 0x0105 in [39066..5]] -> node 4294901761
- text: 你好，歐文。想來點波特酒嗎？後面還有幾瓶。相當物有所值。要我去拿一瓶嗎？

### (sub) DIAL_Z30#3088
- speaker=1  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3089
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3090
- speaker=2  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3091
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3092
- speaker=3  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3093
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3094
- speaker=4  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3095
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3096
- speaker=5  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3097
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3098
- speaker=6  style=0
- effects:
    - ?wOp12 a1=1043 a2=0
- branches:
    - [always] -> node 0 (no jump)
- text: 目前播放的音樂是 ACNONAGR.SND

### (sub) DIAL_Z30#3099
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3100
- speaker=7  style=0  flags=paged-text
- effects:
    - play sfx 119
    - ?wOp12 a1=1025 a2=0
- branches:
    - [flag 0x0100 in [40473..5]] -> node 4294901761
    - [flag 0x0101 in [40656..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGRIMDT.SND  你想再聽一次這個角色的提示嗎？  「是什麼風把克朗多來的訪客吹來的？」

### (sub) DIAL_Z30#3101
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3102
- speaker=8  style=0  flags=paged-text
- effects:
    - play sfx 131
    - ?wOp12 a1=1038 a2=0
- branches:
    - [flag 0x0100 in [40685..5]] -> node 4294901761
    - [flag 0x0101 in [40840..5]] -> node 4294901761
- text: 目前播放的音樂是 MDHAPPY.SND  你想再聽一次這個角色的提示嗎？  「表親！」

### (sub) DIAL_Z30#3103
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3104
- speaker=9  style=0  flags=paged-text
- effects:
    - play sfx 98
    - ?wOp12 a1=1030 a2=0
- branches:
    - [flag 0x0100 in [40869..5]] -> node 4294901761
    - [flag 0x0101 in [41046..5]] -> node 4294901761
- text: 目前播放的音樂是 COMBAT3M.SND  你想再聽一次這個角色的提示嗎？  「這是什麼意思？」

### (sub) DIAL_Z30#3105
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3106
- speaker=11  style=0  flags=paged-text
- effects:
    - play sfx 124
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [41075..5]] -> node 4294901761
    - [flag 0x0101 in [41251..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「歡迎光臨鴨頭酒館！」

### (sub) DIAL_Z30#3107
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3108
- speaker=12  style=0  flags=paged-text
- effects:
    - play sfx 99
    - ?wOp12 a1=1019 a2=0
- branches:
    - [flag 0x0100 in [41280..5]] -> node 4294901761
    - [flag 0x0101 in [41458..5]] -> node 4294901761
- text: 目前播放的音樂是 MDSAD.SND  你想再聽一次這個角色的提示嗎？  「這趟旅程似乎讓你很不舒服啊。」

### (sub) DIAL_Z30#3109
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3110
- speaker=13  style=0  flags=paged-text
- effects:
    - play sfx 117
    - ?wOp12 a1=1034 a2=0
- branches:
    - [flag 0x0100 in [41487..5]] -> node 4294901761
    - [flag 0x0101 in [41660..5]] -> node 4294901761
- text: 目前播放的音樂是 COMBAT.SND  你想再聽一次這個角色的提示嗎？  「報告吧，士兵。有什麼消息？」

### (sub) DIAL_Z30#3111
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3112
- speaker=14  style=0  flags=paged-text
- effects:
    - play sfx 96
    - ?wOp12 a1=1037 a2=0
- branches:
    - [flag 0x0100 in [41689..5]] -> node 4294901761
    - [flag 0x0101 in [41844..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGenr3A.SND  你想再聽一次這個角色的提示嗎？  「伊夏神！」

### (sub) DIAL_Z30#3113
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3114
- speaker=15  style=0  flags=paged-text
- effects:
    - play sfx 118
    - ?wOp12 a1=1036 a2=0
- branches:
    - [flag 0x0100 in [41873..5]] -> node 4294901761
    - [flag 0x0101 in [42054..5]] -> node 4294901761
- text: 目前播放的音樂是 CAMPASIN.SND  你想再聽一次這個角色的提示嗎？  「呸！我還以為抓到一隻布拉克努爾呢。」

### (sub) DIAL_Z30#3115
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3116
- speaker=16  style=0  flags=paged-text
- effects:
    - play sfx 112
    - ?wOp12 a1=1002 a2=0
- branches:
    - [flag 0x0100 in [42083..5]] -> node 4294901761
    - [flag 0x0101 in [42247..5]] -> node 4294901761
- text: 目前播放的音樂是 MDSERIUS.SND  你想再聽一次這個角色的提示嗎？  「什麼人？」

### (sub) DIAL_Z30#3117
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3118
- speaker=17  style=0  flags=paged-text
- effects:
    - play sfx 100
    - ?wOp12 a1=1011 a2=0
- branches:
    - [flag 0x0100 in [42276..5]] -> node 4294901761
    - [flag 0x0101 in [42449..5]] -> node 4294901761
- text: 目前播放的音樂是 CHEAM.SND  你想再聽一次這個角色的提示嗎？  「歡迎來到不知道哪裡，兩位大人。」

### (sub) DIAL_Z30#3119
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3120
- speaker=18  style=0  flags=paged-text
- effects:
    - play sfx 94
    - ?wOp12 a1=1044 a2=0
- branches:
    - [flag 0x0100 in [42478..5]] -> node 4294901761
    - [flag 0x0101 in [42650..5]] -> node 4294901761
- text: 目前播放的音樂是 ACTMAD.SND  你想再聽一次這個角色的提示嗎？  「我想跟你談談。」

### (sub) DIAL_Z30#3121
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3122
- speaker=19  style=0  flags=paged-text
- effects:
    - play sfx 106
    - ?wOp12 a1=1043 a2=0
- branches:
    - [flag 0x0100 in [42679..5]] -> node 4294901761
    - [flag 0x0101 in [42842..5]] -> node 4294901761
- text: 目前播放的音樂是 ACNONAGR.SND  你想再聽一次這個角色的提示嗎？  「留意大門！」

### (sub) DIAL_Z30#3123
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3124
- speaker=20  style=0  flags=paged-text
- effects:
    - play sfx 123
    - ?wOp12 a1=1042 a2=0
- branches:
    - [flag 0x0100 in [42871..5]] -> node 4294901761
    - [flag 0x0101 in [43047..5]] -> node 4294901761
- text: 目前播放的音樂是 MDMSTRYS.SND  你想再聽一次這個角色的提示嗎？  「朋友們，你們的到來是意料中事。」

### (sub) DIAL_Z30#3125
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3126
- speaker=21  style=0  flags=paged-text
- effects:
    - play sfx 102
    - ?wOp12 a1=1006 a2=0
- branches:
    - [flag 0x0100 in [43076..5]] -> node 4294901761
    - [flag 0x0101 in [43260..5]] -> node 4294901761
- text: 目前播放的音樂是 SLOBATLE.SND  你想再聽一次這個角色的提示嗎？  「我正納悶你們兩個跑哪去了。」

### (sub) DIAL_Z30#3127
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3128
- speaker=22  style=0  flags=paged-text
- effects:
    - play sfx 97
    - ?wOp12 a1=1029 a2=0
- branches:
    - [flag 0x0100 in [43289..5]] -> node 4294901761
    - [flag 0x0101 in [43497..5]] -> node 4294901761
- text: 目前播放的音樂是 CAVERN.SND  你想再聽一次這個角色的提示嗎？  「回你的北疆去吧，莫瑞德人。這裡不歡迎你。」

### (sub) DIAL_Z30#3129
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3130
- speaker=23  style=0  flags=paged-text
- effects:
    - play sfx 111
    - ?wOp12 a1=1058 a2=0
- branches:
    - [flag 0x0100 in [43526..5]] -> node 4294901761
    - [flag 0x0101 in [43710..5]] -> node 4294901761
- text: 目前播放的音樂是 TEMPLE.SND  你想再聽一次這個角色的提示嗎？  「我們的地牢不合你的胃口嗎？」

### (sub) DIAL_Z30#3131
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3132
- speaker=24  style=0  flags=paged-text
- effects:
    - play sfx 128
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [43739..5]] -> node 4294901761
    - [flag 0x0101 in [43897..5]] -> node 4294901761
- text: 目前播放的音樂是 PUZZLE.SND  你想再聽一次這個角色的提示嗎？  「站住！」

### (sub) DIAL_Z30#3133
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3134
- speaker=25  style=0  flags=paged-text
- effects:
    - play sfx 129
    - ?wOp12 a1=1043 a2=0
- branches:
    - [flag 0x0100 in [43926..5]] -> node 4294901761
    - [flag 0x0101 in [44097..5]] -> node 4294901761
- text: 目前播放的音樂是 ACNONAGR.SND  你想再聽一次這個角色的提示嗎？  「向貴府致敬。」

### (sub) DIAL_Z30#3135
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3136
- speaker=26  style=0  flags=paged-text
- effects:
    - play sfx 115
    - ?wOp12 a1=1017 a2=0
- branches:
    - [flag 0x0100 in [44126..5]] -> node 4294901761
    - [flag 0x0101 in [44309..5]] -> node 4294901761
- text: 目前播放的音樂是 MDOMINUS.SND  你想再聽一次這個角色的提示嗎？  「你們來得正是時候！」

### (sub) DIAL_Z30#3137
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3138
- speaker=27  style=0  flags=paged-text
- effects:
    - play sfx 121
    - ?wOp12 a1=1039 a2=0
- branches:
    - [flag 0x0100 in [44338..5]] -> node 4294901761
    - [flag 0x0101 in [44502..5]] -> node 4294901761
- text: 目前播放的音樂是 BARDOK.SND  你想再聽一次這個角色的提示嗎？  「你好啊，老朋友！」

### (sub) DIAL_Z30#3139
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3140
- speaker=28  style=0  flags=paged-text
- effects:
    - play sfx 113
    - ?wOp12 a1=1024 a2=0
- branches:
    - [flag 0x0100 in [44531..5]] -> node 4294901761
    - [flag 0x0101 in [44696..5]] -> node 4294901761
- text: 目前播放的音樂是 SHNTYTON.SND  你想再聽一次這個角色的提示嗎？  「普蘭鐸的牙齒啊！」

### (sub) DIAL_Z30#3141
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3142
- speaker=29  style=0  flags=paged-text
- effects:
    - play sfx 132
    - ?wOp12 a1=1001 a2=0
- branches:
    - [flag 0x0100 in [44725..5]] -> node 4294901761
    - [flag 0x0101 in [44917..5]] -> node 4294901761
- text: 目前播放的音樂是 EXPABOV1.SND  你想再聽一次這個角色的提示嗎？  「迪勒肯還沒殺了你？真了不起。」

### (sub) DIAL_Z30#3143
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3144
- speaker=30  style=0  flags=paged-text
- effects:
    - play sfx 110
    - ?wOp12 a1=1018 a2=0
- branches:
    - [flag 0x0100 in [44946..5]] -> node 4294901761
    - [flag 0x0101 in [45138..5]] -> node 4294901761
- text: 目前播放的音樂是 MDROMANC.SND  你想再聽一次這個角色的提示嗎？  「很高興看到你平安回到克朗多。」

### (sub) DIAL_Z30#3145
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3146
- speaker=31  style=0  flags=paged-text
- effects:
    - play sfx 116
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [45167..5]] -> node 4294901761
    - [flag 0x0101 in [45332..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「很高興見到你。」

### (sub) DIAL_Z30#3147
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3148
- speaker=32  style=0  flags=paged-text
- effects:
    - play sfx 107
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [45361..5]] -> node 4294901761
    - [flag 0x0101 in [45525..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「請進。」

### (sub) DIAL_Z30#3149
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3150
- speaker=33  style=0  flags=paged-text
- effects:
    - play sfx 93
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [45554..5]] -> node 4294901761
    - [flag 0x0101 in [45730..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「我是阿布克，開鎖大師。」

### (sub) DIAL_Z30#3151
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3152
- speaker=34  style=0  flags=paged-text
- effects:
    - play sfx 95
    - ?wOp12 a1=1018 a2=0
- branches:
    - [flag 0x0100 in [45759..5]] -> node 4294901761
    - [flag 0x0101 in [45942..5]] -> node 4294901761
- text: 目前播放的音樂是 MDROMANC.SND  你想再聽一次這個角色的提示嗎？  「埃奧提斯正等候著。有話請說。」

### (sub) DIAL_Z30#3153
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3154
- speaker=35  style=0  flags=paged-text
- effects:
    - play sfx 109
    - ?wOp12 a1=1006 a2=0
- branches:
    - [flag 0x0100 in [45971..5]] -> node 4294901761
    - [flag 0x0101 in [46125..5]] -> node 4294901761
- text: 目前播放的音樂是 SLOBATLE.SND  你想再聽一次這個角色的提示嗎？  「站住！」

### (sub) DIAL_Z30#3155
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3156
- speaker=36  style=0  flags=paged-text
- effects:
    - play sfx 122
    - ?wOp12 a1=1037 a2=0
- branches:
    - [flag 0x0100 in [46154..5]] -> node 4294901761
    - [flag 0x0101 in [46332..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGenr3A.SND  你想再聽一次這個角色的提示嗎？  「你這模樣看起來就是麻煩。」

### (sub) DIAL_Z30#3157
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3158
- speaker=37  style=0  flags=paged-text
- effects:
    - play sfx 103
    - ?wOp12 a1=1037 a2=0
- branches:
    - [flag 0x0100 in [46361..5]] -> node 4294901761
    - [flag 0x0101 in [46536..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGenr3A.SND  你想再聽一次這個角色的提示嗎？  「你不會想待在這裡的。」

### (sub) DIAL_Z30#3159
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3160
- speaker=38  style=0  flags=paged-text
- effects:
    - play sfx 114
    - ?wOp12 a1=1037 a2=0
- branches:
    - [flag 0x0100 in [46565..5]] -> node 4294901761
    - [flag 0x0101 in [46734..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGenr3A.SND  你想再聽一次這個角色的提示嗎？  「紳爵，您好。」

### (sub) DIAL_Z30#3161
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3162
- speaker=39  style=0  flags=paged-text
- effects:
    - play sfx 125
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [46763..5]] -> node 4294901761
    - [flag 0x0101 in [46936..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「我叫佩特魯姆婆婆。」

### (sub) DIAL_Z30#3163
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3164
- speaker=40  style=0  flags=paged-text
- effects:
    - play sfx 101
    - ?wOp12 a1=1041 a2=0
- branches:
    - [flag 0x0100 in [46965..5]] -> node 4294901761
    - [flag 0x0101 in [47135..5]] -> node 4294901761
- text: 目前播放的音樂是 MDGENER1.SND  你想再聽一次這個角色的提示嗎？  「唉，又怎麼了？」

### (sub) DIAL_Z30#3165
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3166
- speaker=41  style=0  flags=paged-text
- effects:
    - play sfx 92
    - ?wOp12 a1=1014 a2=0
- branches:
    - [flag 0x0100 in [47164..5]] -> node 4294901761
    - [flag 0x0101 in [47340..5]] -> node 4294901761
- text: 目前播放的音樂是 LAMUT.SND  你想再聽一次這個角色的提示嗎？  「修道院聽候您差遣。」

### (sub) DIAL_Z30#3167
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3168
- speaker=42  style=0  flags=paged-text
- effects:
    - play sfx 105
    - ?wOp12 a1=1013 a2=0
- branches:
    - [flag 0x0100 in [47369..5]] -> node 4294901761
    - [flag 0x0101 in [47544..5]] -> node 4294901761
- text: 目前播放的音樂是 KRONDOR.SND  你想再聽一次這個角色的提示嗎？  「我就覺得認得你。」

### (sub) DIAL_Z30#3169
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3170
- speaker=43  style=0  flags=paged-text
- effects:
    - play sfx 126
    - ?wOp12 a1=1004 a2=0
- branches:
    - [flag 0x0100 in [47573..5]] -> node 4294901761
    - [flag 0x0101 in [47751..5]] -> node 4294901761
- text: 目前播放的音樂是 EXPUNDRG.SND  你想再聽一次這個角色的提示嗎？  「現在可不是趕路的好時候。」

### (sub) DIAL_Z30#3171
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3172
- speaker=44  style=0  flags=paged-text
- effects:
    - play sfx 104
    - ?wOp12 a1=1012 a2=0
- branches:
    - [flag 0x0100 in [47780..5]] -> node 4294901761
    - [flag 0x0101 in [47948..5]] -> node 4294901761
- text: 目前播放的音樂是 ELVANDRK.SND  你想再聽一次這個角色的提示嗎？  「來坐下喝一杯。」

### (sub) DIAL_Z30#3173
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3174
- speaker=45  style=0  flags=paged-text
- effects:
    - play sfx 130
    - ?wOp12 a1=1007 a2=0
- branches:
    - [flag 0x0100 in [47977..5]] -> node 4294901761
    - [flag 0x0101 in [48145..5]] -> node 4294901761
- text: 目前播放的音樂是 BARDGOOD.SND  你想再聽一次這個角色的提示嗎？  「男爵找我？」

### (sub) DIAL_Z30#3175
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3176
- speaker=46  style=0  flags=paged-text
- effects:
    - play sfx 108
    - ?wOp12 a1=1011 a2=0
- branches:
    - [flag 0x0100 in [48174..5]] -> node 4294901761
    - [flag 0x0101 in [48333..5]] -> node 4294901761
- text: 目前播放的音樂是 CHEAM.SND  你想再聽一次這個角色的提示嗎？  「Sah, enconsi？」

### (sub) DIAL_Z30#3177
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z30#3178
- speaker=47  style=0  flags=paged-text
- effects:
    - play sfx 120
    - ?wOp12 a1=1018 a2=0
- branches:
    - [flag 0x0100 in [48362..5]] -> node 4294901761
    - [flag 0x0101 in [48531..5]] -> node 4294901761
- text: 目前播放的音樂是 MDROMANC.SND  你想再聽一次這個角色的提示嗎？  「有客人！真是太好了！」

### (sub) DIAL_Z30#3179
- speaker=0  style=0
- effects:
    - free paged image table
- branches:
    - [always] -> node 0 (no jump)
