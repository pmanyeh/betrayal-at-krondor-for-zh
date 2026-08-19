# 交接備忘錄 (Session Handoff Memo)

**寫於：** 2026-08-19　**目前狀態：** Phase 5（穩健中文文字引擎）驗收清單已全部跑過，Phase 6（DDX 翻譯正式流程）的核心 pipeline 已建立、實機驗證可播放。

這份文件的目的：讓下一個對話 session（不管是不是同一個 agent）不需要重新摸索環境，能直接接續開發。詳細技術過程另見 `docs/baseline/phase5-toolchain-build-verification.md`；長期規劃見 `Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`（主線，目前採用中）；另有一份 `Betrayal_at_Krondor_HD_Traditional_Chinese_PROJECT_PLAN.md`（HD host-side overlay 替代方案，尚未採用，僅供未來評估）。

---

## 1. 現在做到哪裡了

用**真正的 1993 年 Borland C++ 工具鏈**（不是手刻二進位補丁）重新編譯出含中文邏輯的 `KRONDOR.EXE`，並在 DOSBox-X 實機驗證下列都正常：

- 雙位元組中文偵測、字碼查表、寬度計算、自動換行
- 多行中文行距（修過一個真的 bug：原本用 ASCII 字高算行距，中文 16px 會疊字）
- 中英混排基線一致（修過：對話 token 系統的 `@` 展開邏輯會誤吃中文編碼的 trail byte；也新增了「中英混排時英文改用中文字型自己的倚天 ASCII 點陣」的功能）
- 超長文本換頁（確認原生引擎既有的捲動機制在中文模式下正常運作，不需要額外處理）

字型目前用的是**真正的倚天 3.53 點陣字**（`STDFONT.15` 漢字 + `SPCFONT.15` 符號 + `ASCFONT.15` 英數），不是合成佔位圖案或現代 TTF 點陣化。

目前示範字庫只有 82 個中文字（POC 階段，夠測試用，離完整翻譯還很遠）。

本次 session 額外完成 Phase 5 驗收清單剩下的部分（對齊／裁切／異常位元組），詳見
`docs/baseline/phase5-toolchain-build-verification.md` §4.4：

- **置中對齊**：查證 `wFlags & 4`（DDX 記錄自帶的旗標，非我們新增）在真實遊戲資料裡
  確實有在用（單一章節就有 13 筆），拿既有必經觸發點（node `1600003`）開這個位元、
  塞中文字重新編譯測試，實機確認中文字正確置中。靠右對齊在現有遊戲資料裡找不到任何
  真的會走到的路徑，只用 Python simulation 覆蓋，沒有另外做實機測試。
- **異常/不完整雙位元組序列**：發現並修正一個真的 bug（commit `4b681d3`，upstream
  子模組）——字串結尾若剛好是一個沒有 trail byte 的中文前導位元組，`font_draw_text_far`
  本來就會跳過不畫，但寬度計算函式 (`font_text_pixel_width`／`textwrap_compute_lines`)
  卻仍算它 16px 寬，兩邊不一致。修正後拿同一批必經觸發點實機測試畸形序列，確認會被
  安靜跳過、不當機、不影響後續劇情。
- 新增 `tests/unit/test_phase5_chinese_textwrap_sim.py`：逐行對照目前
  `FONT.C`／`TEXTWRAP.C` 演算法的 deterministic test，涵蓋 Phase 5 Acceptance
  清單全部類別（17 個測試全過）。順手修好一個無關但過期的既有測試
  (`test_chinese_font.py`，`ZH16.DAT` 預期檔案大小公式沒算進 ASCII 區塊)。
- `dist/test_v100_zh/` 裡的 `DIAL_Z01.DDX`／`DIAL_Z16.DDX` 目前內容是這次 Phase 6
  pipeline 測試用 `ddx_translate.py build` 產出的版本（見 §5.1），提醒：這個資料夾
  本來就是暫時性測試產物，下一輪測試會直接覆寫，不用特別還原。

## 2. 環境設置（下個 session 不用重裝，但要知道在哪）

### WSL2（已裝好）
- Ubuntu，使用者 `pmanyeh`，已加入 `kvm` 群組（沒加入的話 QEMU-KVM 會靜默失敗、且不留下任何 log——這是踩過的坑）。
- `uv` 裝在 `~/.local/bin`。
- Borland 工具鏈（bc31/bc30/bc20/FreeDOS）解壓在 `~/bak-toolchain`（來自上游 GitHub Release，雜湊已驗證）。

### 編譯用的 WSL 原生 clone
- 位置：`~/krondor-build`（WSL 原生 ext4 檔案系統，**不是** `/mnt/d/...`）。
- 這是 `upstream/betrayal-at-krondor` 的 clone，`origin` 指向 Windows 端的 `/mnt/d/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/.`。
- **重要**：`uv sync` / `uv run` 絕對不能在 `/mnt/d/...`（Windows 掛載磁碟）上跑，DrvFs 對 `utime`/硬連結操作會直接報錯（`Operation not permitted` / `Invalid cross-device link`）。一定要在 WSL 原生檔案系統上跑，跑完再把 `work/KRONDOR.EXE` 複製回 Windows 端。

### 重新編譯的標準流程
1. 在 `upstream/betrayal-at-krondor/bak/SRC/...`（Windows 端）修改 C 原始碼，commit。
2. `wsl -e bash -lc "cd ~/krondor-build && git pull --ff-only"`
3. `wsl -e bash -lc "cd ~/krondor-build && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain && export PATH=\$HOME/.local/bin:\$PATH && uv run bak build"`（增量編譯，通常一兩分鐘）
4. 看到 `❌ KRONDOR.EXE: size differs` 是**正常的**——這個檢查是設計來抓「不小心改壞」用的，只要 `VMCODE.OVL`/`SX.OVL` 都還是 `✅ BYTE-IDENTICAL` 就代表工具鏈跟連結沒問題，是我們自己故意改了 `KRONDOR.EXE`。
5. 先關掉 DOSBox-X（不然 `work/KRONDOR.EXE` 複製會被鎖檔擋掉），再 `cp ~/krondor-build/work/KRONDOR.EXE /mnt/d/git/betrayal-at-krondor-for-zh/dist/test_v100_zh/krondor.exe`。

### DOSBox-X 啟動
- 執行檔：`D:\git\DOSBox-X-AI\build-memory\dosbox-x.exe`
- 設定檔：`dist/dosbox_zh_test.conf`（這次交接新建的，之前用的是 session 暫存檔、不會保留）。掛載的是 `dist/test_v100_zh/`（獨立測試資料夾，**不是**原始遊戲資料夾，這點很重要，見下方 §4）。
- 啟動：`Start-Process "D:\git\DOSBox-X-AI\build-memory\dosbox-x.exe" -ArgumentList "-conf","dist\dosbox_zh_test.conf"`
- 有 DOSBox-X AI Debugger MCP 工具可用（`capture_frame`、`key_tap` 等），但目前這個 build **沒有滑鼠絕對定位/點擊**支援（`click_at`/`move_mouse_absolute` 都回 `UNKNOWN_METHOD`），選單要嘛用鍵盤字母縮寫（例如主選單按 `n` = New Game），要嘛請使用者自己用滑鼠操作、截圖回報。

### 倚天字型來源（**不在 git 裡，本機外部依賴**）
- `D:\git\Fonts\iso\FILES\STDFONT.15` / `SPCFONT.15` / `ASCFONT.15`（真的倚天 3.53 點陣字，索引公式已用 oracle 驗證過）。
- 這個路徑是寫死在 `tools/font/build_font.py` 裡的（`_ETEN_STD_PATH` 等常數）。**如果下個 session 是在別台機器上，這些檔案不會存在**，字型產生工具會自動退回 TTF 點陣化（微軟正黑體/新細明體）或合成佔位圖案，不會報錯，但字型會變成備用方案，這點要注意。
- `D:\git\Fonts\ET353S.iso`（原始 ISO）本身是**損毀的**（7z、Windows 內建掛載都打不開），能用的是使用者自己手動解壓出來放在 `D:\git\Fonts\iso\` 底下的內容，這個資料夾如果之後被清掉，字型來源就沒了。

## 3. 關鍵原始碼位置

都在 `upstream/betrayal-at-krondor`（獨立 git repo，子模組式的 clone，不是本專案 git 歷史的一部分）：

- `bak/SRC/GFX/FONT/FONT.C` / `FONT.H`：中文/ETen ASCII 繪圖、寬度計算、`g_bMixedZhMode` 判斷。
- `bak/SRC/UI/TEXTWRAP.C`：折行、行高（讀 `g_bMixedZhMode`）。
- `bak/SRC/DIALOG/DIALOG.C`：`dialog_render_text_with_tokens()`——token 展開（含 `@` 修正）、設定 `g_bMixedZhMode` 的地方。

本專案（`betrayal-at-krondor-for-zh`）這邊：

- `tools/font/build_font.py`：字型產生工具（ETen 優先 → TTF → 合成佔位圖案），也是 `encode_string`/`decode_string`（中文編碼）的定義處。
- `tools/text/ddx_extract.py` / `ddx_pack.py`：DDX 對話檔 extract/pack（Phase 4 就有，格式已驗證），`ddx_translate.py`（Phase 6 新增）在這兩個之上組出 scaffold/status/build 的翻譯 pipeline。
- `localization/generated/`：目前的 `ZH16.DAT`、`zh_mapping.json`（已 commit，是正式產物）。
- `localization/translated/`：Phase 6 的翻譯來源檔（`DIAL_Z01.json`、`DIAL_Z16.json`，已 commit）——含 id/node_id/source（英文原文）/tokens/translation/status/notes。**設計上原文本來只存 id/tokens/translation，刻意不存英文原文以避免公開散布原始劇本；後來使用者實際用起來發現沒有原文對照很難覆核翻譯，決定推翻這個設計，改成原文也一起 commit 進 git**——這是使用者知情後的決定，不是疏忽（原文終究是原廠已免費公開下載的遊戲內容，見 §6）。
- `dist/test_v100_zh/`：**測試用**遊戲資料夾（gitignored，不進 git），裡面混了乾淨遊戲檔 + 目前測試中的中文補丁檔案（`krondor.exe`、`ZH16.DAT`、`DIAL_Z16.DDX`）。**這個資料夾內容是暫時性、隨時可能被下一輪測試覆寫**，不要當成正式產物看待。

## 4. 重要教訓 / 踩過的坑（不要重踩）

1. **絕對不要把補丁檔案複製進 `betrayal-at-krondor/`（真正的原始遊戲資料夾）**。之前的教訓：舊版 `dosbox_zh.conf` 直接掛載原始遊戲資料夾又執行複製指令，把 `krondor.exe` 永久覆寫掉了，已經從 `betrayal-at-krondor.zip`（未觸碰過的原始封存檔）還原過一次。現在改成掛載獨立的 `dist/test_v100_zh/`，原始遊戲資料夾應保持完全不動。
2. **DDX record 修改要維持原始 byte 長度**（同長度 padding），除非你有把握處理好 offset 連鎖影響。DDX 的 opcode 可能用絕對 offset 定址，改變某個 record 長度會讓後面所有 record 的 offset 錯位，導致播放邏輯跳到錯的地方（實測撞過）。
3. **手刻二進位補丁的位址風險極高**——舊版 Phase 5 就是因為位址從未在真正執行時驗證過，加上漏改一個函式，導致 CPU 卡死在無窮迴圈。現在的作法（改 C 原始碼、用真工具鏈編譯）完全避開這類風險，遇到新需求優先考慮改原始碼，不要回頭手刻機器碼。
4. **`git ls-files` / 手動確認 `.gitignore`**：`tools/build/`（舊版二進位補丁的建置腳本）目前被 `.gitignore` 的 `build/` pattern 意外排除在外，如果之後要恢復類似工具要注意這點。
5. Bash 工具的 cwd 會在 `cd a && cd b` 這種複合指令後**跨呼叫持續存在**，容易不小心卡在子目錄裡，下指令前如果不確定就先 `pwd` 確認。

## 5. 建議下一步（挑一個開始）

1. **擴充字庫**（現在最大的瓶頸）：Phase 6 的翻譯 pipeline 已經打通、實機驗證可播放，但目前只有 82 個示範字，能翻的內容非常有限。建議規劃系統化擴充流程（例如先對全遊戲 DDX 對話跑一輪詞頻統計，抓出高頻字優先做）。
2. **大規模跑 `ddx_translate.py scaffold`**：對全部章節的 DDX（`bak rmf list` 看到至少 `DIAL_Z00`～`DIAL_Z19`）批次執行 scaffold，把 `localization/translated/*.json` 骨架建齊，方便後續分批翻譯。
3. **盤點其他文字介面**（PROJECT_PLAN Phase 8 範疇）：目前只測過 DDX 對話，BOK 書籍、主選單、UI 標籤都還沒碰過，`textwrap_draw_aligned` 理論上是共用管線，但實際行為沒驗證過（`font_glyph_metrics` 對「字串結尾孤立前導位元組」目前沒有跟 §1 提到的修正版本同步處理寬度，因為它沒有下一個 byte 的上下文可看——BOK/UI 若要重用中文渲染，這點需要重新評估）。

## 5.1 Phase 6：DDX 翻譯正式流程（本次 session 完成）

新增 `tools/text/ddx_translate.py`，三個子指令組成完整 pipeline：

- `scaffold <本機原始 DDX>`：從使用者本機的原版 DDX 讀取，產生/更新 `localization/translated/<CHAPTER>.json`（id、node_id、**source 英文原文**、tokens、translation、status、notes）。重跑不會蓋掉已翻譯的內容（用 id 比對合併），但**每次都會用本機 DDX 重新覆蓋 `source`**，如果發現跟檔案裡已有的 `source` 不一樣會印警告（就是靠這個機制才抓到 §5.1 那個資料夾污染問題）。
- `status <翻譯 json>`：印進度統計，只讀 json 本身，不需要本機 DDX；加 `--show-untranslated` 直接印出未翻譯項目存好的原文。
- `build <本機原始 DDX> <翻譯 json> <輸出 DDX>`：把翻譯內容編碼、合併回 DDX 結構。status 不是 `translated`、token 數量/種類跟原文對不上、或**存好的 `source` 跟本機 DDX 現在讀到的文字不一樣**，一律 fallback 用本機 DDX 的原文（不會半路生出亂碼或播放錯位，也不會拿舊/錯的原文去蓋掉正確的遊戲資料）。

id 命名規則是 `<檔名>#<rec_index>`（結構性索引，不用文字內容當 key，避免抓不到人或改了文字就對不上）。`tokens` 欄位記錄每筆文字裡的結構性標記（`@0` 這類發言者代入、`\t`/`\n`、`0xE0-0xFF` 控制位元組），build 時會拿翻譯裡實際出現的 tokens 跟原文比對，不一致就安全 fallback。

**驗收結果**：`localization/translated/DIAL_Z01.json`（40 筆，21 筆已填測試用譯文）、`DIAL_Z16.json`（211 筆，2 筆已填）皆已 commit。結構性 round-trip（choices/opcodes 的 nA3 指標正確重新指到同一筆語意上的目的地、node_id 目錄表不變）用程式驗證過；DIAL_Z16 那 2 筆（node `1600003`／`1600004`，還是用同一個必經的章節一開場埋伏戰鬥觸發點）也在 DOSBox-X 實機播放驗證過，正確顯示、不影響前後的原文對話。對照 Phase 6 Acceptance 清單：20 筆 round-trip、10 筆有繁中、tokens 正常、實機可播放、全程不需手工 hex edit——皆已達成。

**⚠️ 重要教訓：`betrayal-at-krondor/` 曾經被污染過，本次已修復，但要小心不要重蹈覆轍。**
這次要抓乾淨原文時才發現，這個「應該完全不動」的原始遊戲資料夾，`DIAL_Z01.DDX`／`DIAL_Z16.DDX`／`ZH16.DAT` 其實在更早某次 session 被拿來當「組裝發布補丁包」的暫存區用過（資料夾裡還躺著一份沒清掉的 `README~1.TXT`「繁體中文化補丁安裝說明」＋ `CHECKS~1.SHA`），導致這幾個檔案早就不是原版。已用 `bak rmf extract`（見下方指令）從沒被動過的 `krondor.rmf` 重新解出乾淨版本、蓋掉污染檔案，並清掉多餘的 `ZH16.DAT`／`ZH_MAP~1.JSO`／`README~1.TXT`／`CHECKS~1.SHA`／`TEMP.GAM`。`krondor.exe`／`vmcode.ovl`／`sx.ovl` 這次檢查大小都正常，沒被動過。**教訓：不要無條件信任本機任何「看起來像原版」的資料夾，尤其是拿來測試/組裝過東西的資料夾；要抓乾淨原文時，優先直接從 `krondor.rmf`／`krondor.001` 用 `bak rmf extract` 現場解，不要信任鬆散檔案。**

```bash
wsl -e bash -lc "cd ~/krondor-build && export PATH=\$HOME/.local/bin:\$PATH && \
  uv run bak rmf extract <本機 krondor.rmf 路徑> DIAL_Z01.DDX DIAL_Z16.DDX --out <輸出資料夾>"
```

`bak rmf list <krondor.rmf>` 可以看到全部可解的資源，光是對話檔就有 `DIAL_Z00.DDX` 到至少 `DIAL_Z19.DDX`（遠比目前 `dist/`／`betrayal-at-krondor/` 裡原本以為只有的 Z01、Z16 多）。

## 6. Git 狀態

- 主專案 `betrayal-at-krondor-for-zh`：`master` 分支，最新 commit 見 `git log --oneline -10`。`origin` 已設定指向使用者自己的 GitHub repo（`https://github.com/pmanyeh/betrayal-at-krondor-for-zh`）——commit/push 都對這裡，不是上游來源。
- `upstream/betrayal-at-krondor`：本地領先 origin 5 個 commit（`2dcb2b0`、`90be31b`、`e7f94c0`、`1276b58`、`4b681d3`）。**這些 commit 永久只留在本地 clone，不 push 回 origin、不對上游開 PR**——這是專案的固定規則，不是暫時待確認事項。上游是還原保存專案、不是 modding 專案，我們的中文化修改只在自己的專案（`betrayal-at-krondor-for-zh`）裡管理和 commit。
