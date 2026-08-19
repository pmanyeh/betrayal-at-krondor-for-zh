# 交接備忘錄 (Session Handoff Memo)

**寫於：** 2026-08-19　**目前狀態：** Phase 5（穩健中文文字引擎）驗收清單已全部跑過；Phase 6（DDX 翻譯正式流程）pipeline 已建立，已完成 **DIAL_Z01（40 筆）＋ DIAL_Z16（211 筆）＋ DIAL_Z18（364 筆，全遊戲共用的物品檢視說明文字）共 615 筆真實翻譯**，字庫從 82 字長到 **2198 字**，全部真倚天點陣、零 fallback。DIAL_Z18 build 驗證 0 mismatch/0 drift fallback，測試套件 48/48 過。

這份文件的目的：讓下一個對話 session（不管是不是同一個 agent）不需要重新摸索環境，能直接接續開發。詳細技術過程另見 `docs/baseline/phase5-toolchain-build-verification.md`；長期規劃見 `Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`（主線，目前採用中）；另有一份 `Betrayal_at_Krondor_HD_Traditional_Chinese_PROJECT_PLAN.md`（HD host-side overlay 替代方案，尚未採用，僅供未來評估）。

---

## 1. 現在做到哪裡了

用**真正的 1993 年 Borland C++ 工具鏈**（不是手刻二進位補丁）重新編譯出含中文邏輯的 `KRONDOR.EXE`，並在 DOSBox-X 實機驗證下列都正常：

- 雙位元組中文偵測、字碼查表、寬度計算、自動換行
- 多行中文行距（修過一個真的 bug：原本用 ASCII 字高算行距，中文 16px 會疊字）
- 中英混排基線一致（修過：對話 token 系統的 `@` 展開邏輯會誤吃中文編碼的 trail byte；也新增了「中英混排時英文改用中文字型自己的倚天 ASCII 點陣」的功能）
- 超長文本換頁（確認原生引擎既有的捲動機制在中文模式下正常運作，不需要額外處理）

字型目前用的是**真正的倚天 3.53 點陣字**（`STDFONT.15` 漢字 + `SPCFONT.15` 符號 + `ASCFONT.15` 英數），不是合成佔位圖案或現代 TTF 點陣化。

字庫已經不是 82 字的 POC 示範集了——現在是**從實際翻譯內容動態長出來的 1385 字**（見下方「Phase 6 產出：第一章完整翻譯」），`tools/font/build_font.py` 新增了 `--from-translations` 模式，直接掃 `localization/translated/*.json` 裡狀態為 `translated` 的譯文收字，不用再手動維護一份固定字表。

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

1. **繼續翻譯其他章節**：`DIAL_Z01`＋`DIAL_Z16`（第一章開場，251 筆）＋`DIAL_Z18`（全遊戲共用物品說明，364 筆）已經全部翻完，共 615 筆。其餘 30 個 DDX 章節檔（`DIAL_Z00`、`DIAL_Z02`～`DIAL_Z17`、`DIAL_Z19`～`DIAL_Z31`、`TEST`）都已經 `scaffold` 好骨架、躺在 `localization/translated/` 裡等著填（剩餘筆數見 §5.2，總量 5,932 筆已扣掉本次翻完的部分）。可以挑接下來玩家會碰到的章節繼續（但要注意：§5.2 已經證實 `DIAL_Zxx.DDX` 的編號**不對應故事章節**，無法單靠檔名判斷「這是第幾章的內容」，需要用其他方式判斷優先順序，例如照 node_id 的遊戲內觸發順序，或乾脆按檔案大小/內容概覽挑）。翻譯專有名詞密集的內容時，切記先查 `glossary.json`，翻完後也要記得跑一次關鍵字掃描確認沒有憑印象翻出跟既有譯名不一致的版本（見 §5.0 的教訓）。
2. **盤點其他文字介面**（PROJECT_PLAN Phase 8 範疇）：目前只測過 DDX 對話，BOK 書籍、主選單、UI 標籤都還沒碰過，`textwrap_draw_aligned` 理論上是共用管線，但實際行為沒驗證過（`font_glyph_metrics` 對「字串結尾孤立前導位元組」目前沒有跟 §1 提到的修正版本同步處理寬度，因為它沒有下一個 byte 的上下文可看——BOK/UI 若要重用中文渲染，這點需要重新評估）。
3. **翻譯品質校對**：§5.2 的 251 筆翻譯是這次一口氣翻完的，語氣/用詞一致性有靠 `localization/glossary/glossary.json` 把關，但畢竟沒有第二個人核對過，建議找懂《裂谷之戰》原作或至少通順中文的人抽查一輪。

## 5.0 Phase 6 追加產出：DIAL_Z18（全遊戲物品檢視說明文字，364 筆）完整翻譯（本次 session 完成）

在 §5.2 的第一章劇情之後，接著翻完 `DIAL_Z18.json`——這個檔案**不是特定章節的劇情**，而是玩家在任何章節檢視/使用物品時都會用到的通用說明文字（拿起某樣物品的描述、商人討價還價台詞、法術卷軸標題、修理匠/開鎖匠對話等），364 筆全數翻完，`ddx_translate.py status` 顯示 364/364 `translated`，`ddx_translate.py build` 對照本機原版 `DIAL_Z18.DDX` 驗證：**0 筆 token-mismatch fallback、0 筆 source-drift fallback**，全部使用真實翻譯內容。

翻譯過程中遇到幾種原本沒處理過的樣式控制位元組排列方式，順手擴充了工作流程：

- **逐字元樣式（每個字元、含換行/定位符都各自帶一個控制位元組）**：少數幾筆間諜密函（`#276`、`#283`）連換行/定位符都被前後包了樣式位元組，原本逐詞 `interleave()` 沒辦法處理。新寫了 `restyle(source, translation_text)`（在 scratchpad，未進 repo——如果之後常態需要這招，建議正式收進 `ddx_translate.py`）：逐字掃描原文，只把「前一個字元是樣式位元組、且自己不是控制字元」的位置換成譯文的下一個字，控制位元組本身跟真正的換行/定位符一律原樣保留，這樣不需要手算每段確切字數就能保證 token 結構完全一致。
- **`interleave()` 的 target_count 是「原文有幾個被樣式位元組標記的詞」，不是「譯文要精確幾個字」**——因為 `interleave()` 本身就會自動 pad `…` 或截斷，所以譯文只要語意合理、長度大致接近即可，不用逐字精算；但**要小心 target_count 太小時把重要專有名詞截掉**（這次踩過一次：Pug 的簽名檔 target_count 只有 3，原本寫「星塢的帕格」被截成「星塢的」，帕格的名字整個消失，改成「自帕格」才在 3 字內保留人名）。

### ⚠️ 詞彙表沒認真核對就翻，出現多筆跟已建立譯名不一致的錯誟

批次翻譯這 364 筆時，好幾個先前已經在 `glossary.json` 建立好譯名的專有名詞，翻譯當下沒有回頭查表，憑印象翻出了不同的版本（例如 Tanneurs 誤譯成「坦諾斯」、Gamina 誤譯成「加米娜」、Sethanon 誤譯成「賽山農」、Northwarden 誤譯成「北衛堡」等，共抓出約 10 處）。後來寫了一個小的關鍵字掃描腳本（比對已知的錯誤字串是否還留在 `translation` 欄位裡）逐一抓出並修正，修正後重新 build 確認 0 fallback、重新收字庫、重新跑測試套件全過。**教訓：批次翻譯專有名詞較密集的內容時，翻完不能只做 token 結構驗證，一定要另外跑一次「掃描是否用了非 glossary 譯名」的檢查**，不然結構正確但譯名不一致的錯誤不會被任何現有機制攔下來。

`glossary.json` 這次新增：Isunatus（人名）、Killian／Eortis（神名，僅見於法術卷軸標題）、Guild of Thieves（盜賊公會，與既有的刺客公會不同）。

### ⚠️ 真正的記憶體容量瓶頸：中文字庫長到 2198 字後，實機閃退＋文字亂碼——已修正（EMS 分頁儲存）

字庫從 1385 字長到 2198 字、部署實機測試時，使用者回報：部分文字顯示亂碼（英數字母碎片混在中文裡），且從開場動畫進入互動 3D 畫面時必定閃退、DOSBox-X 自動重啟。

追查後定位到根因：`FONT.C` 的 `font_init_chinese()` 用 `alloc_far()`（DOS INT 21h AH=48h）把整個中文點陣字（含 ASCII 區塊）配置在**傳統記憶體（640KB 以下）**，而且**整局遊戲都不釋放**。1385 字約占 44KB，2198 字約占 70KB，多出的 ~26KB 常駐配置，在遊戲進入互動 3D 畫面（需要額外配置場景/美術資料）時把傳統記憶體榨乾，導致配置失敗、資料寫壞、當機。用「先退回 1385 字＋只有 DIAL_Z01/Z16（上一個 session 驗證過沒問題的組合）」重新部署測試，確認問題消失，坐實這就是純粹的容量瓶頸，不是這次翻譯內容或編碼邏輯出錯。

**修法**：中文點陣字資料改存進 **EMS 擴充記憶體**，只留一塊固定 4KB 的 ASCII 區塊在傳統記憶體。遊戲引擎本來就有 EMS 子系統（`SRC/SYS/EMS.C`／`EMSIMG.C`，原本是給圖片資源用的），直接沿用同一套 `ems_alloc_pages()` / `ems_map_at_offset()` API：

- `font_init_chinese()`：偵測到 EMS（`g_ems_present`）就把 CJK 點陣資料以 16KB 為單位串流讀進 EMS 分頁鏈（`g_nZhFontEmsChain`，新增的全域變數），沒有 EMS 才退回舊的傳統記憶體配置法。
- `font_draw_zh_glyph()`：畫字前用 `ems_map_at_offset(chain, gid*32L)` 把對應分頁映射進 EMS page frame 再讀，因為每個字圖正好 32 bytes、16384 整除 32，保證不會跨分頁邊界，不需要處理字圖被切成兩半的情況。
- 「已初始化」的判斷旗標從 `g_pZhFontBitmap`（EMS 模式下這個指標故意保持不設） 改成一定會配置的 `g_pZhAsciiBitmap`，避免每次畫字都重新觸發初始化。

改完用 WSL2 Borland 工具鏈重新編譯（`bak/SRC/GFX/FONT/FONT.C`／`FONT.H`，upstream commit `378050c`），`VMCODE.OVL`／`SX.OVL` 仍 BYTE-IDENTICAL（工具鏈/連結沒問題），部署 2198 字字庫＋DIAL_Z01/Z16/Z18 全部翻譯內容到 `dist/test_v100_zh/` 後實機重測：DIAL_Z18 的物品檢視文字（開鎖工具描述）正確顯示、無亂碼，進入互動畫面不再閃退，使用者確認 OK。

**這對之後的章節翻譯很重要**：EMS 分頁的空間遠大於傳統記憶體剩餘的空間，所以字庫還能再長很多，但**傳統記憶體本身還是有限**——如果之後其他子系統（不是中文字型）的配置需求也一起成長，理論上還是有可能撞到别的容量瓶頸，只是不會再是「中文字庫」這個特定原因了。下次如果又遇到「翻譯內容變多之後開始閃退/亂碼」，先懷疑記憶體容量，不要只查編碼邏輯。

### ⚠️ 換行演算法誤把中文字「第二個位元組」當成斷行點——已修正（改編碼配置，沒動到 C 原始碼）

實機測試部署 2198 字字庫後，使用者截圖抓到：明明一行還有很多空間，卻莫名其妙提早換行（例如「……刺客」後面留一大片空白才換到下一行）。

追到根因：`TEXTWRAP.C` 的 `textwrap_is_break_point()` 把任何落在 `0x80-0xDF` 範圍的位元組都當成「可以斷行的地方」——這是照英文（配合中文*前導*位元組）設計的假設，只認位元組**數值**，不知道自己讀到的究竟是某個中文字的「前導位元組」（真正的字元起點）還是前一個字的「後隨位元組」（字元的第二個 byte）。我們的 BAK-ZH 2-byte 編碼原本後隨位元組有一部分（65/160）剛好也落在 `0x80-0xDF`——當連續幾個中文字剛好都用到這個重疊範圍時，往回找斷行點的迴圈會一路把好幾個字都誤判成斷點，斷得比預期早很多。

**修法**：不動 C 原始碼，改成**重新分配中文字的編碼位元組**，讓後隨位元組永遠只落在 `0x20-0x7E`（跟前導位元組的範圍完全不重疊），這樣 `0x80-0xDF` 就永遠只可能是真正的字元起點，換行判斷不用改也自動正確。代價是每個前導位元組底下能用的槽位從 160 降到 95（總容量 15,360→9,120），但以目前 2198 字（含跳過的空位共佔 3693 個槽位）來看還有很大餘裕。改法在 `tools/font/build_font.py` 的 `build_zh_font()`，跳過會落在後半段（`gid % 160 >= 95`）的 ID、用空白 32-byte 填補，字庫、`zh_mapping.json`、全部已翻譯內容都要重新產生/重新編碼一次（純 Python 端操作，不用重編 exe）。

### ⚠️ 「@」佔位符號緊接中文字時顯示亂入一個「n」——已修正（`isdigit()`/`tolower()` 餵到負數）

修完換行後，使用者又抓到：好幾筆帶「@」的物品文字裡，party 成員的名字位置顯示成單一字母「n」而不是真正的英文名字（因為隊伍成員名字目前仍保留英文，見 §5.3.1）。

這次沒辦法用 Python 模擬重現（模擬顯示斷行本身沒問題），改嘗試接上 DOSBox-X 的即時偵錯 MCP 工具，但這個環境下 `pause_execution`/`set_breakpoint` 這類「需要偵錯器真的停下來」的方法反覆讓整個 `dosbox-x.exe` 當掉斷線（`AGENT_GUIDE.md` 有提到這類方法需要開一個真正的主控台視窗，我方 launch 出來的 process 顯然沒有滿足這個前提，換了好幾種啟動方式——`-defaultdir`、去掉輸出重導向、`-break-start`——都沒能穩定接上），只好放棄即時偵錯，回頭重新逐行看 `DIALOG.C` 的原始碼。

根因：`DIALOG.C` 判斷「@」是「@0~@4 數字形式」還是「純 @（代入當前隊伍成員名字）」的地方，寫的是 `isdigit((char)text[1])`——檢查緊接在 @ 後面那個位元組。中文不需要空格，我們的翻譯常常是「@把這只……」這種 @ 後面直接接中文字、沒有空格；中文字的前導位元組數值偏高（例如 `0x84`），這個編譯器的 `char` 是有號數，轉型成 `(char)` 後這個位元組會變成**負數**——把負數（`EOF` 以外）丟給 `isdigit()` 是 C 標準的未定義行為。實際跑起來很可能讀到界外記憶體、誤判成數字形式，用一個離譜的負數陣列索引（`(char)0x84 - '0' ≈ -172`）誤闖進一段完全不相干、原本是「a→an」英文文法校正用的分支，把字串 `"n "` 插進了輸出裡。

**修法**：把 `isdigit((char)text[1])` 改成 `isdigit((unsigned char)text[1])`，同段落裡另一處 `tolower((char)...)` 也一併改成 `(unsigned char)`（同一類 bug，雖然邏輯上因為 isdigit 修好後這條分支對中文字已經不會再進去，但保留一致修正比較保險）。這是 C 語言的經典地雷——ctype.h 系列函式的參數只要不是先轉成 `unsigned char`，遇到任何最高位元是 1 的 byte 就有 UB 風險；掃過整個專案原始碼確認**只有這兩處**有這個 cast 手法，其餘 `isdigit`/`isalpha`/`toupper` 呼叫處理的都是純 ASCII 資料（檔名、設定檔 token），沒有中文字節混進去的風險，沒有一併改動。改完用 WSL2 Borland 工具鏈重新編譯（`bak/SRC/DIALOG/DIALOG.C`，commit `0e2f249`），實機重測「Gorath 把這只棕色包裹放到一旁……」正確顯示，人名跟中文字都正常，問題解決。

## 5.1 Phase 6：DDX 翻譯正式流程（本次 session 完成）

新增 `tools/text/ddx_translate.py`，三個子指令組成完整 pipeline：

- `scaffold <本機原始 DDX>`：從使用者本機的原版 DDX 讀取，產生/更新 `localization/translated/<CHAPTER>.json`（id、node_id、**source 英文原文**、tokens、translation、status、notes）。重跑不會蓋掉已翻譯的內容（用 id 比對合併），但**每次都會用本機 DDX 重新覆蓋 `source`**，如果發現跟檔案裡已有的 `source` 不一樣會印警告（就是靠這個機制才抓到 §5.1 那個資料夾污染問題）。
- `status <翻譯 json>`：印進度統計，只讀 json 本身，不需要本機 DDX；加 `--show-untranslated` 直接印出未翻譯項目存好的原文。
- `build <本機原始 DDX> <翻譯 json> <輸出 DDX>`：把翻譯內容編碼、合併回 DDX 結構。status 不是 `translated`、token 數量/種類跟原文對不上、或**存好的 `source` 跟本機 DDX 現在讀到的文字不一樣**，一律 fallback 用本機 DDX 的原文（不會半路生出亂碼或播放錯位，也不會拿舊/錯的原文去蓋掉正確的遊戲資料）。

id 命名規則是 `<檔名>#<rec_index>`（結構性索引，不用文字內容當 key，避免抓不到人或改了文字就對不上）。`tokens` 欄位記錄每筆文字裡的結構性標記（`@0` 這類發言者代入、`\t`/`\n`、`0xE0-0xFF` 控制位元組），build 時會拿翻譯裡實際出現的 tokens 跟原文比對，不一致就安全 fallback。

**驗收結果**：結構性 round-trip（choices/opcodes 的 nA3 指標正確重新指到同一筆語意上的目的地、node_id 目錄表不變）用程式驗證過；也在 DOSBox-X 實機播放驗證過。對照 Phase 6 Acceptance 清單：20 筆 round-trip、10 筆有繁中、tokens 正常、實機可播放、全程不需手工 hex edit——皆已達成（後續 §5.2 用整個第一章的量再次驗證過一次，規模遠超這個門檻）。

**⚠️ 重要教訓：`betrayal-at-krondor/` 曾經被污染過，本次已修復，但要小心不要重蹈覆轍。**
這次要抓乾淨原文時才發現，這個「應該完全不動」的原始遊戲資料夾，`DIAL_Z01.DDX`／`DIAL_Z16.DDX`／`ZH16.DAT` 其實在更早某次 session 被拿來當「組裝發布補丁包」的暫存區用過（資料夾裡還躺著一份沒清掉的 `README~1.TXT`「繁體中文化補丁安裝說明」＋ `CHECKS~1.SHA`），導致這幾個檔案早就不是原版。已用 `bak rmf extract`（見下方指令）從沒被動過的 `krondor.rmf` 重新解出乾淨版本、蓋掉污染檔案，並清掉多餘的 `ZH16.DAT`／`ZH_MAP~1.JSO`／`README~1.TXT`／`CHECKS~1.SHA`／`TEMP.GAM`。`krondor.exe`／`vmcode.ovl`／`sx.ovl` 這次檢查大小都正常，沒被動過。**教訓：不要無條件信任本機任何「看起來像原版」的資料夾，尤其是拿來測試/組裝過東西的資料夾；要抓乾淨原文時，優先直接從 `krondor.rmf`／`krondor.001` 用 `bak rmf extract` 現場解，不要信任鬆散檔案。**

```bash
wsl -e bash -lc "cd ~/krondor-build && export PATH=\$HOME/.local/bin:\$PATH && \
  uv run bak rmf extract <本機 krondor.rmf 路徑> DIAL_Z01.DDX DIAL_Z16.DDX --out <輸出資料夾>"
```

`bak rmf list <krondor.rmf>` 可以看到全部可解的資源，光是對話檔就有 `DIAL_Z00.DDX` 到 `DIAL_Z31.DDX`（外加一個 `TEST.DDX`），共 32 個章節檔。

## 5.2 Phase 6 產出：第一章開場（DIAL_Z01 + DIAL_Z16）完整翻譯（本次 session 完成）

在 §5.1 的 pipeline 基礎上，這次直接把兩個確認可達的章節檔**全部**翻成有意義的正式繁體中文，不再是佔位測試字串：

- `localization/translated/DIAL_Z01.json`：40 筆全翻完（開場旅途旁白、地名、一整組墓誌銘）。
- `localization/translated/DIAL_Z16.json`：211 筆全翻完——這其實是**整個第一章的主線劇情**：埋伏戰後續 → 帶戈拉斯回克朗多見亞魯莎王子 → 羅姆尼查案（詹姆士／洛克利爾／派特魯斯）→ 北衛城戰報 → 帕格與馬卡拉的衝突 → 幽暗林裂界機 → 賽瑟儂生命石高潮戰。

同時把其餘 31 個章節檔（`DIAL_Z00`、`DIAL_Z02`～`DIAL_Z31`、`TEST`）都跑過 `scaffold`，骨架（含英文原文、tokens，空的 translation/status）已建好、commit 進 git，全部章節共 **5,932 筆**待翻譯項目，供下次接續。

### 詞彙表：`localization/glossary/glossary.json`（本次新增）

翻譯前先查證過：**這款遊戲本身跟它的小說化版本《Krondor: The Betrayal》都沒有正式中文譯本**（不管簡體繁體），唯一查到的官方依據是雷蒙費斯特《裂谷之戰》本傳小說台灣正式譯本（蓋亞文化／尖端）裡 Pug 的譯名「帕格」。其餘所有人名/地名/專有名詞（Owyn→歐文、Gorath→戈拉斯、Krondor→克朗多……近 70 筆）都是這次自建的一致音譯，風格上盡量貼近「帕格」這個已知基準。**之後翻其他章節、遇到新的人名地名，一定要先查這份檔案、新詞也要往裡面加，不要每次臨場自己翻一個。**

### 字庫從 82 字長到 2198 字

`tools/font/build_font.py` 新增 `glyphs_from_translations()` / `--from-translations` 選項：直接掃 `localization/translated/*.json` 裡 `status=="translated"` 的譯文，收集所有用到的 CJK 漢字**與中文標點**（頓號、句號、引號『』「」、破折號、刪節號——這些原本用 `0x4E00-0x9FFF` 的過濾條件會漏掉，已修正涵蓋 `0x3000-0x303F`／`0xFF00-0xFFEF`／破折號刪節號），取代寫死的 82 字 `POC_GLYPHS`。第一章翻完時收出 1385 字，加上 §5.0 的 DIAL_Z18 之後長到 **2198 字**，全部由真正的倚天 3.53 點陣字繪製（`STDFONT.15` + `SPCFONT.15`，零 fallback 到 TTF 或合成佔位圖案）。

```bash
python tools/font/build_font.py --from-translations localization/translated \
  --output-font localization/generated/ZH16.DAT --output-map localization/generated/zh_mapping.json
```

### ⚠️ 修了一個會讓翻譯全部變亂碼的真 bug：`encode_string()` 不認得控制位元組

對話文字裡常有 `0xE0-0xFF` 的樣式控制位元組（斜體/變色等，`font_render_glyph_or_ctrl` 處理），翻譯時必須原樣保留在譯文字串裡（例如 Python 字串裡的 `'\xf3'`）才能讓 `extract_tokens()` 的 token 比對過關。但 `tools/font/build_font.py` 的 `encode_string()` 原本只認得「ASCII（<0x80）」跟「在 `char_to_id` 裡的中文字」兩種，其他一律 fallback 成 `'?'`（0x3F）——等於**每一個保留下來的樣式控制位元組，實際編碼進 DDX 時都會被寫成問號**，把後面的雙位元組配對全部撞歪、變成亂碼。已修正：`0xE0-0xFF` 的位元組現在會原樣直接寫入輸出（不查表，因為這個範圍本來就不可能是中文前導位元組）。**這個 bug 在寫這份 pipeline 的當下沒被抓到，是這次真的餵了含樣式位元組的完整章節翻譯進去才炸出來的**——以後如果又新增什麼「文字裡混了控制碼」的情境，要記得比照這次的方式驗證：不要只信任 `decode_string()`（它本來就是有損的除錯用途，控制位元組會印成 `\xNN` 文字而不能還原），要直接比對 `encode_string()` 產出的原始 bytes。

### 實機驗證

打包重建 `DIAL_Z01.DDX`／`DIAL_Z16.DDX`（用 `ddx_translate.py build`）+ 新的 1385 字 `ZH16.DAT`，部署到 `dist/test_v100_zh/` 後在 DOSBox-X 跑了章節一開場埋伏戰整段：長句正確換行、`#Name#` 說話者名稱正確翻譯顯示（如「戈拉斯」名牌）、樣式控制位元組沒有破壞任何文字，一路播到把控制權交給玩家（進入 3D 世界地圖畫面）為止都正常。往後的王宮覲見／羅姆尼查案等場景需要滑鼠操作走位才能觸發，這個 session 沒有繼續往下實測，但編碼／round-trip 已經用程式驗證過（見下）。

**注意上面這句「`#Name#` 說話者名稱正確翻譯顯示」只對「文字本身內嵌 `#Name#` 標記」的那類記錄成立**——見下方 §5.3 的第二個發現，還有另一種完全不同機制畫出來的名牌，目前**沒有**跟著翻譯。

## 5.3 使用者實機截圖抓到的兩個新發現（本次 session 尾聲）

翻完第一章、使用者自己開著 DOSBox-X 實際玩過一輪後，肉眼抓到兩個 §5.2 實機驗證沒覆蓋到的問題：

### 5.3.1 隊伍角色名牌（Gorath／Owyn 等六人）目前不會翻譯——不是渲染問題，是資料來源問題

實機截圖發現：部分對話畫面下方會冒出一塊木紋名牌（例如「Gorath」），但那筆記錄的**文字本身根本沒有 `#Name#` 標記**（純敘述文字，直接以 `\t` 開頭）。追查後發現這是完全不同的第二條路徑：

- 畫這塊名牌的是 `DIALOG.C:1083-1090`（`dialog_play_record` 主迴圈裡，`record->wSpeaker_id != 0 && wSpeaker_id < 0x46` 時觸發），呼叫的還是 `dialog_draw_speech_bubble()` → **`font_draw_text_far()`**——跟 `#Name#` 那條路徑走的是同一個、已驗證支援中文的繪圖函式，**不是渲染端的問題**。
- 但名字字串來源完全不同：`askabout_name_or_keyword_lookup()`（`ASKABOUT.C:68-78`），對隊伍角色（id<7）追到底是 `g_gameState.characters[id-1].name`，最終指向 `g_gameState.characterNames[6][10]`——**`GameState` struct 裡固定 10 bytes 一筆的原始二進位欄位**，開新遊戲/讀檔時整包從 `TEMP.GAM` 用 `res_fread_far` 直接讀進記憶體（`SYS/BOOT.C:124-131`、`GAME/STATE/GSTATE.C:190-200`），**原始碼裡完全沒有任何字串常數**，我們現有的 DDX extract/pack 工具完全碰不到這份資料。
- 使用者決定：**這六個名字暫時保留英文，之後有空再處理**（要處理的話，需要另外調查 `TEMP.GAM` 的確切 offset／預設範本從哪裡來，是全新的資源格式調查，不在 DDX pipeline 範圍內）。

### 5.3.2 主選單（Options / Start New Game...）用的字體看起來完全不同，很可能是圖片素材，不是動態文字

使用者截圖了 Options 選單，字體是花體風格，跟對話框裡用的字型明顯不同。快速搜過原始碼，**找不到這幾個字串（"Start New Game" 等）的硬編碼位置**，初步推測這些選單文字可能是預先渲染好的圖片素材（不是走文字繪圖路徑），但**這只是初步推測，還沒有像 §5.3.1 那樣深入追過原始碼確認**。

另外要注意：`FONT.C` 的字型系統本來就是多槽位設計（`g_font_bitmap_data[20]`、`font_activate(slot)`，最多 20 種字型資源可同時登記），但我們目前的中文渲染邏輯是寫死掛在「槽位 0」上，而且**全域只有一套 16×16 大小的中文點陣字**——如果查出主選單真的是動態文字、且用的是明顯更大的字級，會需要規劃「不同地方用不同大小中文字」的機制，目前完全沒有這塊。

這兩點都屬於 `PROJECT_PLAN.md` Phase 8（文字介面盤點）範疇，下一個 session 可以接著查。

## 5.4 Phase 7（BOK 書籍）前置調查：開新遊戲後的「故事書」開場畫面（本次 session 完成）

使用者開新遊戲後截圖了一個章節開場的敘事畫面（羊皮紙背景、花體斜體字、左上角有裝飾性放大首字母、頁碼），懷疑不是 DDX 對話。派 agent 深入原始碼＋實際解出對應資料檔確認：**這是完全獨立的 BOK 書籍系統**（對應 `PROJECT_PLAN.md` Phase 7），跟 DDX 對話是兩套不同機制，此次只做調查，沒有動任何程式碼或翻譯。

- **觸發點與檔名規則**：`SRC/GAME/GMAIN.C:292`（`gmain_play_chapter_intro`）用樣板檔名 `"C00.BOK"`，把章節數加到 byte 1、部數加到 byte 2（`bookName[1] += chapter; bookName[2] += part;`）算出實際檔名，呼叫 `bookview_show(bookName, -1)`。第一章第一部對應到 `C11.BOK`，實際觸發是從 `TTMDLG.C:111` 的劇本 opcode 呼叫，不是「新遊戲」程式碼直接觸發的。
- **資料位置**：`C11.BOK` 連同其餘 21 個章節書籍檔（`C12`、`C21`、`C23`、`C31`、`C32`、`C41`、`C43`~`C46`、`C51`~`C53`、`C61`、`C63`、`C71`、`C81`、`C83`、`C91`、`C92`、`C94`，共 22 個）都封裝在 `krondor.001` 裡，靠 `krondor.rmf` 索引。用既有的 `bak rmf extract` 就能把原始 bytes 挖出來（這部分工具已經有了），解出來的 `C11.BOK` 內容跟截圖文字完全對得上（"lood soaked rags collected at the boy's feet." 開頭，後面接 Owyn 幫傷兵包紮的敘述）。
- **檔案格式是全新的、跟 DDX 完全不同的私有二進位格式**：開頭 `u32` 總長 + 頁面目錄（`int` 頁數 + 每頁一個 `u32` offset），每頁一個 56-byte 頁首（文字欄位矩形、頁碼、上/下一頁指標、圖片數、「文字避開矩形」數、頁碼顯示旗標等），接著是避開矩形清單、圖片清單（`x, y, imageIndex, mirrorFlags`），最後才是帶控制標籤的文字流：`0xF4`=樣式區塊（字型槽位/基線/前景背景色/旗標，10 bytes）、`0xF1`=版面區塊（邊界/行高/縮排，16 bytes）、`0xF3`=保留用的 2-byte「word hook」（目前是 no-op）、`0xF0`=結束符。共用資源（`BOOK.FNT` 字型、`BOOK.SCX` 羊皮紙背景、`BOOK.BMX` 插圖/首字母圖庫、`BOOK.PAL` 調色盤）只在 `bookview_init()` 載入一次，不分書共用。**目前完全沒有任何工具能解析/重新封裝這個格式**，等於要比照當初寫 `ddx_extract.py`/`ddx_pack.py` 的方式，從零開發一套 BOK 專用工具。
- **左上角那個花體放大字母是獨立圖片，不是文字**——已用資料直接驗證：`C11.BOK` 第一頁 `wImageCount=2`，其中 `imageIndex=0` 的圖片座落在頁面設定的「文字避開矩形」正中間，而緊接在後的文字流開頭就是 `"lood soaked..."`——「Blood」的「B」完全沒有出現在文字裡，是靠這張圖片畫出來的。交叉比對其他 BOK 檔案也一致：`C71.BOK` 用同一張圖庫的另一個 index，文字從 `"ells to..."` 開頭（對應「Bells tolled...」缺開頭 B）；`C91.BOK` 用另一個 index，文字從 `"ocklear..."` 開頭（對應「Locklear...」缺開頭 L）。**中文沒有「放大首字」這個概念，這塊必須是設計決定（重畫圖或整個拿掉），不是翻譯能解決的問題。**
- **渲染管線目前不支援中文**——`BOOKTEXT.C` 雖然呼叫的是跟 DDX 共用的同一個 `FONT.C`（`font_activate`、`font_glyph_metrics`、`font_draw_text_ds`），寬度計算 (`font_glyph_metrics`) 也已經有處理 0x80-0xDF 前導位元組（回報 16×16），**但實際畫字元的呼叫（`font_render_glyph_or_ctrl`，被 `BOOKTEXT.C` 的 `booktext_draw_glyph_kerned` 直接呼叫）只認得 0xE0/0xF0 開頭的樣式控制位元組，其餘一律當成單位元組英文字元繪製**——雙位元組配對繪圖 (`font_draw_zh_glyph`) 跟 `text+=2` 的邏輯只存在於再上一層的 `font_draw_text_far()`，而 `BOOKTEXT.C` 完全沒有呼叫到那一層，是自己另外刻了一套逐 byte 掃描的排版/換行/齊行邏輯（`booktext_layout_rndr_one_line` 等）。現在如果直接塞中文字進去，前導位元組會被畫成錯的英文字圖案，後面的後隨位元組會被當成獨立字元繼續解析，整行後面全部跳掉。**要支援中文，得改 `BOOKTEXT.C` 原始碼**（教它認得雙位元組配對，或乾脆改成呼叫已經支援中文的 `textwrap_draw_aligned`），不是單純資料/翻譯層的工作，這點呼應上面 §5.3.2 提到的「不同介面可能各自需要獨立驗證中文渲染」。

**盤點結論**：Phase 7（BOK）是獨立的一塊工程量——新工具（解析/封裝 BOK 格式）+ 新引擎改動（`BOOKTEXT.C` 支援中文雙位元組）+ 設計決定（放大首字母怎麼處理），不能只算翻譯量。排優先序時要把這個獨立成本算進去，不能假設「反正 DDX 都能翻了，BOK 應該差不多」。

## 6. Git 狀態

- 主專案 `betrayal-at-krondor-for-zh`：`master` 分支，最新 commit 見 `git log --oneline -10`。`origin` 已設定指向使用者自己的 GitHub repo（`https://github.com/pmanyeh/betrayal-at-krondor-for-zh`）——commit/push 都對這裡，不是上游來源。
- `upstream/betrayal-at-krondor`：本地領先 origin 7 個 commit（`2dcb2b0`、`90be31b`、`e7f94c0`、`1276b58`、`4b681d3`、`378050c`、`0e2f249`）。**這些 commit 永久只留在本地 clone，不 push 回 origin、不對上游開 PR**——這是專案的固定規則，不是暫時待確認事項。上游是還原保存專案、不是 modding 專案，我們的中文化修改只在自己的專案（`betrayal-at-krondor-for-zh`）裡管理和 commit。
