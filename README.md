# Betrayal at Krondor 繁體中文化計畫

將 1993 年 Dynamix / Sierra 發行的 DOS 經典 RPG《*Betrayal at Krondor*》製作成可在**原版遊戲引擎**上執行的繁體中文版。

## 專案理念

這不是一個「破解字型顯示」或手刻二進位補丁的專案。做法是：

1. 使用 [`canassa/betrayal-at-krondor`](https://github.com/canassa/betrayal-at-krondor) 這個逆向工程還原專案，取得**完整還原自原始 1993 年二進位檔的 C 原始碼**。
2. 直接在原始碼層級加入中文渲染邏輯、修改文字排版/換行邏輯。
3. 用**真正的 1993 年 Borland C++ 3.1 工具鏈**（透過 WSL2 + QEMU-KVM 重建的建置環境）重新編譯。
4. 每次修改都跟原版二進位做雜湊比對——確保「沒改到的部分」保證與原版逐位元組相同，只有刻意修改的邏輯才會不同。

這個方法完全避開了「反組譯猜位址、手刻機器碼補丁」的風險（早期版本曾因此讓遊戲卡死在無窮迴圈）。所有改動都是可讀、可審查、可重新編譯驗證的原始碼。

## 目前狀態

**Phase 5（穩健中文文字引擎）已完成**，並在 DOSBox-X 實機驗證：

- 雙位元組中文偵測、字碼查表、寬度計算、自動換行
- 多行中文行距、中英混排基線對齊
- 置中對齊、超長文本換頁（沿用原生捲動機制）
- 異常/不完整雙位元組序列的容錯處理

字型使用真正的**倚天 3.53 點陣字**（`STDFONT.15` 漢字 + `ASCFONT.15` 英數），目前示範字庫有 82 個中文字（POC 階段，離完整翻譯還很遠）。

詳細進度、環境設定、已知問題與下一步規劃，請看：

- [`HANDOFF.md`](HANDOFF.md) — 給下一個工作階段（人類或 AI agent）的交接備忘錄，**建議從這份開始看**
- [`Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`](Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md) — 完整分階段（Phase 0–12）專案計畫，目前主線採用中
- [`docs/baseline/`](docs/baseline/) — 各 Phase 的建置環境與驗證證據
- [`docs/decisions/`](docs/decisions/) — 中文編碼、字型格式等架構決策紀錄（ADR）

## 專案結構

```
localization/generated/   已產生的中文字型與編碼對照表（正式產物）
tools/font/                字型產生工具（ZH16.DAT）與中文編碼（encode/decode）
tools/text/                DDX 對話檔 extract / pack 工具
tests/unit/                對照原始碼演算法的 deterministic 單元測試
docs/                       各階段驗證文件、架構決策紀錄
upstream/                   還原專案原始碼的本地 clone（獨立 git repo，不隨本專案 push）
dist/                       本機測試用產物（gitignored，隨時可能被覆寫，非正式產物）
```

## 建置與測試

完整的建置環境設定（WSL2、Borland 工具鏈來源、DOSBox-X 測試流程）請見 [`HANDOFF.md`](HANDOFF.md) 第 2 節。

執行既有的 Python 單元測試：

```bash
python -m unittest discover -s tests/unit -v
```

## 關於遊戲資料

**本專案不散布原版遊戲資產。** 若要實際建置、測試修改後的 `KRONDOR.EXE`，需要自行提供合法取得的遊戲資料檔（原版光碟、數位重製版等）。`.gitignore` 已排除遊戲資料相關的副檔名與資料夾，避免誤 commit 進版本控制。

## 如何取得中文化版本

基於上述「不散布原版遊戲資產」的原則，發布的中文化「補丁」本身**不包含**任何原版遊戲檔案，也不包含編譯好的 `KRONDOR.EXE`——`KRONDOR.EXE` 是重編出來的原版商業執行檔衍生物，同樣不直接發布。實際發布內容分三部分：

- **`KRONDOR.EXE` 二進位差異補丁**：使用者拿自己合法版本的 v1.00 Floppy 版（1993-06-16）EXE，在本機套用差異補丁重建出中文版，安裝程式會先驗證雜湊值，版本不符會直接中止、不動任何檔案。
- **`STARTUP.GAM` 隊伍角色名**：對使用者自己的存檔範本檔做原地欄位替換，同樣不隨附任何 `.GAM` 檔。
- **翻譯資源檔**（DDX/BOK/DAT/字型等）：這些是本專案工具從翻譯內容重新產生的全新檔案，直接以 loose 覆蓋檔形式複製進遊戲目錄（引擎本身支援 loose 檔優先於封裝檔的載入順序）。

發布包還會內附官方預先編譯的 **DOSBox-X**（GPLv2 授權的開源 DOS 模擬器，跟原版遊戲無關，可以合法重新散布）與一個雙擊即可啟動的「玩遊戲.bat」，讓使用者不用自己另外找/裝 DOS 模擬器。

開發端依序執行 `tools/release/build_exe_patch.py`（產生 EXE 補丁）、`tools/release/vendor_dosboxx.py`（下載並驗證雜湊後內附 DOSBox-X）、`tools/release/package_release.py`（組出完整發布包 `dist/release_v100_zh/`），使用者端只要執行裡面免 Python 套件依賴的 `installer.py` 即可安裝／解除安裝。目前只支援 v1.00 Floppy 版，其餘版本尚未支援。

## 致謝

- [`canassa/betrayal-at-krondor`](https://github.com/canassa/betrayal-at-krondor) — 原始碼還原與 byte-perfect 重建工具鏈，本專案所有中文化修改都建立在這份工作之上，是整個計畫能成立的基礎。
- [`old-games/bak-translation-tools`](https://github.com/old-games/bak-translation-tools) — 原由 Andrey Fedoseev 開發、後由 Old-Games.RU 社群維護的 DDX / FNT / BOK 等資源格式研究工具，是本專案早期格式調查的重要參考。
- [`xavieran/BaKGL`](https://github.com/xavieran/BaKGL) — 現代 OpenGL 重製專案，作為文字/資源格式與遊戲行為的輔助研究參考（目前戰鬥系統尚未完成，本專案未採用其作為主要 runtime）。
- xBaK — 更早期的開源重製／逆向工程成果，BaKGL 與 `canassa/betrayal-at-krondor` 皆承認其研究貢獻；本專案僅在還原原始碼無法回答問題時，作為次要的歷史參考。
- [DOSBox-X](https://github.com/joncampbell123/dosbox-x) — 本專案所有實機驗證都在 DOSBox-X 上執行，發布包也內附官方預先編譯的 DOSBox-X（GPLv2，見 `tools/release/vendor_dosboxx.py`）方便使用者直接開玩。
- [`pmanyeh/DOSBox-X-MCP-Debugger`](https://github.com/pmanyeh/DOSBox-X-MCP-Debugger) — 基於 DOSBox-X 打造、可由 AI agent 操作的除錯/自動化驗證分支（截圖、按鍵模擬、記憶體讀寫等），本專案每一輪中文渲染的實機驗證都靠它自動化完成。
