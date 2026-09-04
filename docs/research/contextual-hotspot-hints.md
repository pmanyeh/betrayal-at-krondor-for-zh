# 可互動熱區

## 操作

- 在 3D 探索或城鎮／室內場景按住 `Tab`，會以角框標出目前有效的可互動區；放開後立即隱藏。
- 不顯示首次進場或滑鼠左右鍵文字提示；遊戲的互動方式固定，避免提示干擾畫面。
- 城鎮的離開按鈕區與說明文字翻頁區已有明確 UI，因此不列入熱區角框。

## 實作範圍

- `WORLDLP.C` 使用遊戲原生點擊判定的 `WorldHotspot` 命中表，最多顯示目前可互動的 10 個物件。
- 一般場景 renderer 不會更新這份命中表；按下 `Tab` 時會改走原生 hit-test renderer，同一次重畫現行場景並依目前物件位置重建命中表，避免使用上一個畫面或互動後殘留的舊框。
- 3D 命中矩形會先與目前 viewport 求交集；完全在 3D 畫面外的框略過，部分超出的框裁切在世界視窗邊界內，不會蓋到羅盤、角色頭像或功能按鈕。
- `TOWNSCN.C` 使用動態建立的 `MenuEntry` 人物／物件熱區，並排除離開與說明翻頁項目。
- `UIWIDGET.C` 提供共用的高對比角框；原先的文字提示繪圖器已移除。
- 框線先合成到背頁，翻頁後再同步另一頁；按住 `Tab` 時兩個 VGA 頁面維持相同框線，避免乾淨頁與框線頁交替造成閃爍。
- 3D 場景在框線狀態改變時重繪乾淨 viewport；城鎮／室內使用一份約 16 KB 的暫時畫面快照還原，不重新播放進場動畫，離開場景時立即釋放。
- 探索場景攔截 `Tab` 的通用選單導覽行為，顯示框線時不會同時移動滑鼠游標；其他選單畫面的 `Tab` 行為不變。

## 驗證紀錄

- Borland C++ 3.1 編譯／Turbo Link 5.1 連結完成，無新增編譯錯誤。
- `VMCODE.OVL`、`SX.OVL` 與基準 byte-identical。
- Python 單元測試：99 passed。
- `KRONDOR.EXE`：463,024 bytes，SHA-256 `dc58aef6078ca7a64a972546c4c3b65fae083e70d0b3df805f2c4adad873a2e8`。
- `ZHSTAT.DAT`：21,724 bytes、987 個小字 glyph，SHA-256 `001d6f4a580259ee33720712bc3c2c982ec5be8d37af2e4690e4bd118f07fe0c`；由全部既有小字介面來源合併重建並涵蓋全部法術名稱，已移除不再使用的操作提示字串。

## 實機驗收清單

- [x] 使用者已確認 `Tab` 按住顯示、放開清除，且框線不超出 3D viewport。
- [x] 已確認不再沿用前一畫面或已消失物件的命中框。
- [x] 已移除首次進場與滑鼠左右鍵文字提示。
- [x] 使用者完成整體功能驗收（2026-09-02）。

## 2026-09-04：第二章羅姆尼「黑羊酒館」熱區迴歸修正

### 現象

- 第二章抵達羅姆尼後，右側的 Black Sheep Tavern（黑羊酒館）無法點擊；按住 `Tab` 也沒有該建築的物件框，因此主線無法由此繼續。
- 異常版畫面只顯示另外三個有效 actor 的角框；修正後黑羊酒館恢復為第四個可互動熱區。

### 根因

- `GDS6A.DAT` 的 actor 0 是黑羊酒館劇情入口：矩形 `(196, 9, 58, 65)`、`wChapterMask = 0x01fd`、游標 7、`cKind = 15`、對話鍵 `1500069`（`To the Black Sheep Tavern.`）。依城鎮場景的遮罩語意，它只在第二章啟用。
- `cKind = 15` 的真正語意是章節結束／主線推進觸發器；全套 GDS 資源中只有這一個 actor 使用 kind 15。
- 城鎮熱區功能先前在 `TOWNSCN.C` 的兩處篩選中，把 `cKind == 0xf` 一併當成底部離開列：一處用來尋找離開 action，另一處略過建立 actor 的 `MenuEntry`。因此 actor 0 在點擊判定與 `Tab` 框線建立之前就被排除了。

### 修正

- 從上述兩處離開列判斷移除 `pActor->cKind == 0xf`；只保留真正的底部寬幅離開列與 `cKind == 3` 排除條件。
- 沒有針對羅姆尼座標硬編碼例外，而是讓 kind 15 actor 重新走原有的資料驅動 `MenuEntry`、點擊 dispatch 與 `Tab` 框線流程。
- 引擎提交：`2e97009ba429b4315ccac47379cf1e7efccd0388`（`fix: restore Romney chapter-end hotspot`）。

### 驗證與留存

- Borland C++ 3.1 增量重編完成；`KRONDOR.EXE` 468768 bytes，SHA-256 `5f2cace7d6d31f7bbe1e6c2d8a2e4f5b1e70d5c532ba8d423e67e7096be28acb`。
- `VMCODE.OVL`、`SX.OVL` 與修正前 byte-identical；Python 單元測試 100 passed。
- 測試版已部署至 `dist/test_v100_zh/krondor.exe`；修正前備份為 `scratchpad/krondor_pre_romney_hotspot_fix.exe`，本次修正版另存為 `scratchpad/KRONDOR_romney_hotspot_fix.EXE`。
- 執行階段已成功由該熱區進入黑羊酒館屍體劇情；截圖留存在 `scratchpad/romney_fix_progress.png`。使用者於 2026-09-04 確認修復。

### 防止復發

- 不應以 actor 的劇情結果（例如離開場景或結束章節）推斷其 UI 身分；離開列應以實際 kind 與版面幾何識別。
- 新增或修改 `MenuEntry` 篩選時，先盤點所有 GDS actor kind 的實際用途，並在其限定章節中比對「有效 actor 數」與「可點擊／Tab 框線數」。羅姆尼第二章應有四個一般 actor 熱區，另有一個不顯示框線的底部離開列。
