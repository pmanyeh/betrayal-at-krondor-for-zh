# DIAL_Z12

5 records, 4 keyed nodes

## node 1200001  (DIAL_Z12#0)
- speaker=0  style=0
- effects:
    - frame/rect style override x=100 y=58 w=120 h=25
- text: 六賢者

## node 1200002  (DIAL_Z12#1)
- speaker=0  style=0
- effects:
    - END conversation, result=1
- text: 「迪勒肯正是在此地統一了北境諸部族。凡到訪此地者，皆應跪下讚頌諸神，感念他的偉大力量與智慧。」

## node 1200003  (DIAL_Z12#2)
- speaker=0  style=0
- branches:
    - [always] -> node 0 (no jump)
- text: 雷瑟姆．麥肯 「熱愛礦坑，從未想過離開。」

## node 1200004  (DIAL_Z12#3)
- speaker=0  style=0
- branches:
    - [flag 0xc360 in [0..0]] -> node 0 (no jump)
    - [flag 0x1fca in [0..0]] -> node 0 (no jump)
    - [flag 0x1fcb in [0..0]] -> node 4294901761
    - [always] -> node 0 (no jump)

### (sub) DIAL_Z12#4
- speaker=0  style=6
- effects:
    - SET flag 0x1fcb=1
- text: 思緒湧上心頭。  戈拉斯放緩了回憶的腳步，將注意力集中在四周環境上。這些洞穴本身看似平凡無奇，卻是古老遺跡的殘骸……院長日誌裡寫的是什麼來著？一只木箱……貝殼……會是這個嗎？
