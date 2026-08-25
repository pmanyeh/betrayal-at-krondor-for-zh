# 交接備忘錄封存 (Session Handoff Archive)

> **這是歷史封存檔，不是目前的交接文件。** 2026-08-25 把原本持續累積的 `HANDOFF.md` 拆成兩份：目前的部署狀態、還沒解決的問題、下一步待辦，改放在專案根目錄的 `HANDOFF.md`（保持精簡，每個 session 應該整份讀完）；這份檔案保留拆分當下的完整歷史敘事（逐 session 的 bug 根因、修法細節、教訓），只有在需要追查某個舊問題的來龍去脈時才用關鍵字搜尋進來讀，不需要整份讀過一遍。檔案內部的章節編號（§1、§8.3 這類）都是相對這份封存檔本身，不是 `HANDOFF.md`。

---

**最後更新：** 2026-08-25　**目前部署狀態：** `dist/test_v100_zh/` 裡的 `DIAL_Z00.DDX`（418 筆，含 §8.3 那 9 筆章節橫幅）已經**完整部署且實機驗證通過**——§8.3／§8.4 當時記錄的「章節橫幅卡死」「撿屍體閃退」兩個問題都已經在 §8.5（2026-08-21）跟緊接著的這次 session（§9，2026-08-21~23）修好。§10 的撿屍／物件說明停住與 §11 的戰鬥後升級訊息空白死機也已解決；**下面第 1～3 點與 §8.3／§8.4 的「尚未解決」結論已經過時，不要照著繼續排查，直接看 §8.5／§9／§10／§11**。§12 記錄了緊接在 §10／§11 之後的一輪翻譯 session：新增 `DIAL_Z06`／`DIAL_Z21`／`DIAL_Z14` 三個章節檔，其中 `DIAL_Z21` 的「隊伍能力提升」系統訊息正是**觸發 §11 那個分頁死機 bug 的第一批中文內容**，兩邊要對照著看。§13（2026-08-23，同日稍晚的新 session）新增 `DIAL_Z13`（商店／旅店／神殿系統，128 筆）並已打包部署到 `dist/test_v100_zh/`。§14（同日再稍晚，延續 §13 的同一輪對話）又新增 `DIAL_Z27`（95 筆，已部署）與 `DIAL_Z22`（96 筆，**已驗證但暫緩部署**），並確立「後續翻譯章節一律按筆數由少到多排序」的原則。§15（同日再稍晚）新增 `DIAL_Z23`（100 筆），並意外抓到修好 `DIAL_Z16` 兩筆既有的 token-mismatch bug（見 §15.3）。2026-08-24：使用者測完 §13／§14 後確認可以部署，`DIAL_Z22`／`DIAL_Z23`／修正版 `DIAL_Z16`／新字庫已全部部署到 `dist/test_v100_zh/`；使用者同時回報「亞魯莎」的「莎」字顯示異常，已排查確認字庫資料本身沒問題（逐 byte 比對過），懷疑是 DOSBox-X 進程跨多輪部署沒有完全重啟過導致 EMS 殘留舊字庫，**已請使用者這次部署後務必完整重啟 `krondor.exe` 再重新測試**，詳見 §15.3 結尾。§16（2026-08-24~25，新 session）先補完了 §15.3 其實從未真正部署成功的 `DIAL_Z13`／`DIAL_Z22`／`DIAL_Z23`／`DIAL_Z27` 四個章節（manifest 顯示先前 applied 都是 0，「莎」字異常其實跟 EMS 殘留無關），接著實機測試揪出並修好一連串跟中文有關、原本潛伏著的引擎 bug（`#Name#` 標題解析截斷、`ttmscript_show_dialog_action()` 跟 `dialog_show_by_key()` 完全沒有分頁邏輯、中文標題橫幅蓋住內文、換行寬度計算沒排除樣式控制位元組等），詳見 §16 全文；**§16.7 留了一個還沒解決的已知問題（分頁「孤兒行/孤立標點」在改用平均分頁演算法後依然重現，根因還沒抓到）**，下一個 session 如果要接著查，直接看那一節。

目前累計已完整翻譯並跑過驗證流程：**22 個** DDX 章節檔共 **1809 筆對話**（`DIAL_Z00`／`Z01`／`Z02`／`Z03`／`Z04`／`Z05`／`Z06`／`Z07`／`Z08`／`Z10`／`Z11`／`Z12`／`Z13`／`Z14`／`Z16`／`Z18`／`Z21`／`Z22`／`Z23`／`Z24`／`Z27`／`Z29`，全部都已部署到 `dist/test_v100_zh/`，其中 `Z16` 另有兩筆這次順手修好的既有 token-mismatch bug 一併部署，見 §15.3），加上全新的 `OBJINFO.DAT` 物品名稱系統（137 筆全譯）、`UI_HARDCODED.json` 硬編碼字串 55 筆；另外 `TEST.json`（1 筆，`TEST.DDX` 的旁支小插曲）已經翻完但**還沒打包**，手上缺一份乾淨的 `TEST.DDX` 可以對，見 §12.1。字庫 **4816 個字庫 ID 槽位**（實際 **2866** 個相異字元，槽位數大於字元數是因為 §5.2 的編碼避碰機制本來就會跳過部分 ID），全部真倚天點陣、零 fallback。詞彙表 `glossary.json` 已有 **273 筆**詞條。全遊戲 DDX＋TEST 對話總量 5,932 筆，扣掉已翻的 1,810 筆（1809 已跑過驗證 + 1 待打包），其餘約 4,122 筆待翻，依筆數由少到多排序：`DIAL_Z17`（152）→`Z15`（159）→`Z19`（362）→`Z31`（374）→`Z20`（867）→`Z30`（2208）（scaffold 都已建好）。

以下第 1～3 點是 2026-08-21 當天寫下、**現已被 §8.5 取代**的舊結論，保留僅供追溯排查歷史：

1. **字庫編號洗牌 bug（已修正為預設行為，不會再重演）**：`build_font.py --from-translations` 原本每次都把所有中文字的字庫編號重新洗牌一遍；這次因為 `DIAL_Z00.json` 檔名排序在 `DIAL_Z01`/`Z16`/`Z18` 之前，導致這幾個「這次根本沒改過」的已翻譯章節全部跟著錯位、螢幕全部變亂碼。已改成**穩定、只增不變（append-only）**的編號分配：`build_font.py` 現在預設會讀取既有的 `--output-map`（若存在）當作基準，只給新字元分配新編號，舊字元的編號永遠不變──這樣以後任何時候擴充字庫，都不會再讓已經 build 好的舊 DDX 檔案報廢。細節見 §8.1。
2. **`TEXTWRAP.C` 真的 infinite loop（已修正並重新編譯進 `KRONDOR.EXE`）**：`textwrap_draw_aligned()` 用來計算「這個對話框裝得下幾行」的迴圈，用 `unsigned short` 型別的 `g_wTextWrapLinesRemaining` 做減法，沒有上界檢查；一旦超過應有範圍，C 的無號數提升規則會讓減法結果從負數變成一個巨大正數，導致迴圈條件永遠成立、遊戲整個卡死（黑畫面、無法操作，但 DOSBox-X 進程本身沒當掉）。這個 bug 原本潛伏著沒被發現，因為原文英文內容從來沒觸發過這個邊界；**是這次翻譯章節標題文字（`DIAL_Z00` 的 `#291`~`#299`，node_id 294~302）第一次讓中文內容跑進這條路徑才炸出來**。已在 `bak/SRC/UI/TEXTWRAP.C` 修正（加一個上界檢查）並重新編譯，`VMCODE.OVL`／`SX.OVL` 仍 byte-identical。細節見 §8.2。~~這 9 筆章節標題目前仍暫時還原成英文~~ **已在 §8.5 用 `g_bSmallZhMode` 小字模式解決，9 筆章節橫幅現在正常顯示中文，見 §8.5 B 段。**
3. ~~⚠️ 尚未解決：撿屍體會讓遊戲直接閃退~~ **已在 §8.5 A 段解決**：根因是 `ddx_pack.py` 把 `DdxChoice` 的 32-bit `dwTarget_key` 誤當成獨立 16-bit 欄位重映射，中文版 record 長度改變後子記錄位址跳錯，讀到未初始化資料寫穿記憶體。已修正 `ddx_pack.py`，實機確認撿屍體不再閃退。

這份文件的目的：讓下一個對話 session（不管是不是同一個 agent）不需要重新摸索環境，能直接接續開發。詳細技術過程另見 `docs/baseline/phase5-toolchain-build-verification.md`；長期規劃見 `Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`（主線，目前採用中）；另有一份 `Betrayal_at_Krondor_HD_Traditional_Chinese_PROJECT_PLAN.md`（HD host-side overlay 替代方案，尚未採用，僅供未來評估）。**下一個 session 開始前，務必先讀 §10／§11／§12（最新三次 session 的完整記錄）**——§9.5 的物件貼圖雜色 bug 已在 §9.7／§9.8 解決，§10／§11 記錄的撿屍/物件說明停住、戰鬥後升級訊息空白死機也都已解決並實機驗收過，都不用再重新排查。

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
- `D:\git\Fonts\Fusion_Pixel_10px.ttf`（本次 session 新增依賴，見 §6.2 小字級字型）：一款像素字型，`tools/font/build_small_font.py` 跟 `build_font.py` 的 TTF fallback 都會用到，路徑寫死在 `tools/font/build_font.py` 的 `_FUSION_PIXEL_PATH`。同樣是本機外部依賴，別台機器上若沒有這個檔案，`render_glyph_from_ttf_sized()` 會回傳 `None`，小字型建置會產生全空白字形（不會報錯，但字看不見），這點要注意。

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

1. **繼續翻譯其他章節**：`DIAL_Z01`＋`DIAL_Z16`（第一章開場，251 筆）＋`DIAL_Z18`（全遊戲共用物品說明，364 筆）＋`DIAL_Z00`（全遊戲共用隨機遭遇/UI/章節標題，409／418 筆，9 筆章節標題暫留英文，本次 session 完成並實機驗證通過，見 §8）已經全部翻完，共 1,024 筆。其餘 29 個 DDX 章節檔（`DIAL_Z02`～`DIAL_Z17`、`DIAL_Z19`～`DIAL_Z31`、`TEST`）都已經 `scaffold` 好骨架、躺在 `localization/translated/` 裡等著填（總量 5,514 筆，已扣掉本次翻完的 418 筆）。**下個 session 開始翻新章節前，務必先讀過 §8.1／§8.2 這兩個修過的真 bug**（字庫編號穩定性、`TEXTWRAP.C` 無號數下溢），確認自己不會重蹈覆轍；如果有興趣，也可以先挑戰 §8.3 還沒解決的章節橫幅卡死問題，把 `#291`~`#299` 這 9 筆補完。繼續翻譯新章節時，記得每次翻完一批都要**實機測試過再收工**，不要只靠結構驗證（token round-trip／build fallback 計數）就當作完成——這次 session 就是活生生的教訓：結構驗證 100% 過關，實機還是炸出兩個真 bug。可以挑接下來玩家會碰到的章節繼續（但要注意：§5.2 已經證實 `DIAL_Zxx.DDX` 的編號**不對應故事章節**，無法單靠檔名判斷「這是第幾章的內容」，需要用其他方式判斷優先順序，例如照 node_id 的遊戲內觸發順序，或乾脆按檔案大小/內容概覽挑）。翻譯專有名詞密集的內容時，切記先查 `glossary.json`，翻完後也要記得跑一次關鍵字掃描確認沒有憑印象翻出跟既有譯名不一致的版本（見 §5.0 的教訓）。
2. ~~盤點其他文字介面~~ **已完成**（見 §6.1，`docs/research/text-surface-inventory.md`）；已挑了優先度最高的 `g_abStatNames` 開始做（見 §6.2）。接下來可以挑：§5 剩餘的硬編碼字串（`INVENTOR.C`／`INVINSP.C`／`TOWNSCN.C`／`CACTOR.C`）——不需要新工具，跟 `g_abStatNames` 一樣直接改原始碼；或是 §4／§4a／§4b 的 MenuPage/`KEYWORD.DAT`/`fmap_twn.dat` 資源家族——需要先開發通用 `.dat` parser/packer，工程量較大。（`font_glyph_metrics` 對「字串結尾孤立前導位元組」的處理缺口仍未評估，BOK 之外目前還沒撞到這個情境。）
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

## 6. Phase 8 文字介面盤點 + 角色屬性面板中文化（本次 session 完成）

### 7.1 Phase 8：文字介面盤點正式完成

新增 [`docs/research/text-surface-inventory.md`](docs/research/text-surface-inventory.md)，系統性盤點遊戲內**所有**文字來源，不只 DDX/BOK。結論：全遊戲文字分四條路徑——

1. **DDX 對話系統**（Phase 6 既有基礎設施）。
2. **BOK 書籍系統**（Phase 7 前置調查，見 §5.4）。
3. **MenuPage / NamedTable / DialogWidget 資源系統**（新發現）——主選單、存讀檔、Options、片尾名單、法術選單、戰鬥選單等幾乎所有按鈕標籤，走一套獨立於 DDX/BOK 的 `*.dat` 資源家族（`req_opt0.dat`、`spells.dat`、`cred.dat`……數十個檔案），**先前懷疑「主選單是圖片」的推測已排除，其實是文字**，只是需要新開發一套 parser/packer。
4. **話題詢問選單 `KEYWORD.DAT`**（新發現，`ASKABOUT.C`）——對話畫面下方「`<角色> asked about:`」的關鍵字按鈕格，**不屬於 DDX**，玩家實機截圖抓到才發現這個缺口。另外還有 `fmap_twn.dat`（大地圖城鎮標籤）也是獨立資源。

加上大量硬編碼 C 字串常數（`INVENTOR.C`／`INVINSP.C`／`CHARSCRN.C`／`ENCAMP.C`／`TOWNSCN.C`／`COMBAT.C`／`CACTOR.C`）可以直接改原始碼、不需要新工具。**渲染引擎結論**：不管走哪條路徑，最終繪圖幾乎全部收斂到 `font_draw_text_far`／`font_draw_text_ds`（已支援中文），`BOOKTEXT.C` 是唯一的例外。詳細分類、每項的 SOURCE/FORMAT/EXTRACTABLE/PACKABLE/RUNTIME PATH/CHINESE READY/STATUS 欄位、建議工程順序都在該文件裡，下一步要挑戰哪個介面直接查那份文件就好，不用重新盤點。

### 7.2 角色屬性面板（Ratings 面板）全部中文化 + 兩個真的 bug

盤點完成後，挑 §5「硬編碼字串」裡優先度最高的 `g_abStatNames`（[`DIALOG.C:25`](upstream/betrayal-at-krondor/bak/SRC/DIALOG/DIALOG.C#L25)，16 個屬性/技能名，同時被 DDX `%s` token 共用）先做，連帶把 `CHARSCRN.C` 的 `"Ratings:"`／`"Condition:"`／`"Normal"`／`"of"` 也翻完，新增 `localization/translated/UI_HARDCODED.json` 追蹤這類「非 DDX 硬編碼字串」的翻譯來源（格式仿照 DDX 的 translated json，但欄位精簡，`id` 直接寫「檔名#變數名」）。這個檔案會被 `build_font.py --from-translations` 自動掃到，字庫因此照常長大，不用額外收字。

過程中在 DOSBox-X 實機測試抓到兩個真的 bug（不是這次新翻譯內容寫錯，是既有引擎邏輯本來就有問題，只是之前沒有中文字經過這幾段程式碼所以沒暴露出來）：

- **`charscreen_draw_stat_row()` 的行距是照英文字型調校的，中文字塞不下**（[`CHARSCRN.C`](upstream/betrayal-at-krondor/bak/SRC/CHAR/CHARSCRN.C) 原本 `y = stat_idx * 0xb + 0x1c`，11px 行距）——這個「Ratings:」方框本來就設計給一個明顯比 16×16 矮的英文字型用，塞進標準 16×16 中文字會四行疊在一起。**沒有把行距硬拉大了事**（那樣會讓中文字比旁邊的數字明顯粗大、比例失調，使用者實機測試後回報「字太大」），而是新刻了一套**小字級中文點陣字**：`font_init_chinese_small()`／`font_draw_zh_glyph_small()`（新增於 `FONT.C`／`FONT.H`），從 `Fusion_Pixel_10px.ttf`（一款真正的像素字型，風格貼近年代）用 `tools/font/build_small_font.py` 烘焙出 10×10 點陣，存成稀疏格式的 `ZHSTAT.DAT`（用跟主字庫**同一套 glyph ID**，只是稀疏儲存實際用到的幾十個字，不用整個 3695 字全複製一份，佔用記憶體極小、放在傳統記憶體即可不用碰 EMS）。`CHARSCRN.C` 新增 `charscreen_draw_small_zh_label()` 這個獨立的小字繪圖輔助函式，只有這個「Ratings:」面板（含下面技能清單，兩處都套用以保持視覺一致）呼叫它，DDX 對話跟其他地方的中文渲染完全不受影響。**這個做法之後很可能會一直重複用到**——凡是「中文字在原本設計給窄字型的緊湊 UI 區塊裡顯得過大/比例不搭」，都可以照這個模式辦理，不用每次重新設計。
- **`g_bMixedZhMode` 全域旗標離開對話框後沒有重設**——這個旗標是 Phase 5 加的「中英混排時英文改用中文字型自己的倚天 ASCII 點陣」功能，只在 `DIALOG.C: dialog_render_text_with_tokens()` 裡設定（含中文字就設 1），但**這個函式結束時從來沒有把它重設回 0**。結果是：玩家只要看過一段有中文的對話，這個旗標就會一直殘留是 1，直到下一段對話重新計算為止；期間打開任何其他畫面（角色畫面、可能還有其他畫面），裡面**純英文/數字的文字**（"60"、"Gorath"、"Exit"、"N/A"……）也會被誤判成「中英混排」，改用比較粗大的倚天 ASCII 點陣去畫，不是遊戲原本的小字體。使用者實機測試（先經過中文對話、再開角色畫面）才抓到這個症狀，跟這次新翻譯的內容本身無關，是曝光了一個潛藏已久的既有 bug。**修法**：在 `dialog_render_text_with_tokens()` 唯一的出口（函式結尾，`}` 前）加一行 `g_bMixedZhMode = 0;`，這是它的單一 return path，不影響函式內部其餘繪圖呼叫仍然正確使用這個旗標。

全部改動都在 `upstream/betrayal-at-krondor` 個別 commit（`c7feb11`、`f38a089`、`12b9a14`、`42f6fd4`、`8ddc763`、`d0af98c`，共 6 個，細節見 §7），實機在 DOSBox-X 逐步驗證過（疊字消失、字級比例正常、`g_bMixedZhMode` 修好後數字恢復小字體、間距對齊使用者要求）。

## 8. Phase 6 追加產出：DIAL_Z00 完整翻譯（418 筆，本次 session 完成）

在 §5 建議的「繼續翻譯章節」方向下，這次挑了 `DIAL_Z00.DDX`（418 筆，是繼 DIAL_Z01/Z16/Z18 之後第四個翻完的章節檔）。跟 DIAL_Z18 一樣，這個檔案**不是特定章節劇情**，而是全遊戲共用的內容，具體可分四類：

- **隨機遭遇/伏擊敘事模板**（佔絕大多數，約 300 筆）：地下城、荒野各種隨機戰鬥觸發前的敘事文字，大量使用 `@0`~`@5` 隊伍成員代稱與樣板化措辭（同一組「毫無防備／早已等待／殺了對方一個措手不及」三態變化反覆出現在不同生物類型上），翻譯時建立了一套固定的中文句式對應，同一模板不同觸發條件時保持譯文一致。
- **存讀檔／Options／戰鬥按鈕 UI 提示文字**（約 90 筆）：滑鼠停留說明，格式高度一致（「Left clicking on this button will...」），逐筆翻成「左鍵點擊這個按鈕可……」的固定句式。
- **九個章節標題與任務目標**（`#291`~`#299`，例如 "Chapter One: Into a Dark Night / Escort Gorath to Krondor!"）：這是玩家會在「目錄」畫面看到的九章標題，翻譯時第一次處理到 `wFlags`／樣式位元組**沒有配對、逐詞觸發**的排版方式（源文字每個英文單字前都有一個 `\xf1` 標記但結尾沒有對應的關閉標記，是這款引擎既有的逐詞樣式開關機制，不是本專案自創的格式），對應譯文一樣拆成對應數量的詞組、在每個詞組前插入同樣數量的 `\xf1`，token 結構才會過。
- **四位主角背景介紹段落**（Locklear/Gorath/Owyn/Pug/James/Patrus，`#284`~`#289`）：這是玩家開新遊戲挑角色時會看到的人物簡介，帶出不少先前翻譯內容沒出現過的背景設定名詞（見下方 glossary 新增清單），是這批裡文學性最高、最需要查證的部分。

**`glossary.json` 這次新增**（約 20 筆）：Crenard（傭兵）、Guild of Death（死亡公會，跟既有 Nighthawks/Guild of Assassins 是不同的公會）、Ruthia（幸運女神）、Guiswa（獵神）、**Milamber**（帕格的圖蘭尼法師名，這次才第一次出現在已翻譯內容裡）、Kulgan（帕格的啟蒙師父）、Crydee（帕格的故鄉）、Great One(s)（圖蘭尼「至尊法師」頭銜）、William（帕格之子）、the Upright Man（克朗多盜賊公會首領「正直人」，是詹姆士的生父）、Brak Nurr（礦坑巨獸）、bulldrake（牛蜥，常見小型龍族怪物）、**Riftwar**（裂界之戰，跟遊戲本身的「大崛起之戰」是兩場不同戰爭，先前的翻譯內容裡都還沒正式收錄這個詞，是這次才發現的缺漏）、the Great Rising（大崛起之戰，正式收錄）、Armengar、Land's End、Ardanien（戈拉斯的氏族名）、Green Heart（莫瑞德人家園森林）、Great Northern Mountains、Beleforte（歐文的家族姓氏）、Duke of Euper、Ran（城市）。**下次翻到背景設定或人物簡介類文字時，先查這批新詞，不要重新音譯。**

**驗收**：418 筆全數翻完，`ddx_translate.py build` 對照 `bak rmf extract` 現場解出的乾淨原始檔驗證 **0 筆 token-mismatch fallback、0 筆 source-drift fallback**（結構層面完全正確）。字庫用 `build_font.py --from-translations` 重新收字，從 2198 字長到 **4072 字**。**部署後第一次實機測試就炸出了兩個影響全域的真 bug（§8.1、§8.2），另外還有一個目前沒解決、已知會卡死遊戲的問題（§8.3，這次繞過了但沒修好）**——這次 session 大部分時間都花在抓這兩個 bug 跟隔離第三個問題，過程與教訓詳細記錄在下面三節，下一個 session 如果要繼續深挖 §8.3，或未來又遇到類似「明明結構驗證都過、實機卻卡死」的狀況，務必先看這幾節，不要重新從頭排查。

另外這次順手發現：其餘 30 個待翻章節檔中，`DIAL_Z18` 之後真正翻完的是 `DIAL_Z00`，代表 §5.2 提到的「檔名不對應章節」問題持續成立——`DIAL_Z00` 雖然編號最前，內容卻是全遊戲共用的隨機遭遇模板，不是開場章節劇情。

## 8.1 真 bug：字庫編號沒有穩定性，新增一個排序較前的翻譯檔會讓所有舊 DDX 變亂碼

`DIAL_Z00.json` 翻完後跑 `build_font.py --from-translations` 重新收字，**部署後發現 `DIAL_Z01`／`DIAL_Z16`／`DIAL_Z18`（這次完全沒有改動的既有翻譯）在畫面上全部變成亂碼**，使用者截圖抓到的第一個異狀就是這個。

**根因**：`glyphs_from_translations()` 用 `sorted(translated_dir.glob("*.json"))`（依檔名字母序）掃描 `localization/translated/*.json`，`build_zh_font()` 再依掃描到字元的**先後順序**依序分配字庫編號（`char_to_id`）。在這次 session 之前，`DIAL_Z00.json` 全部是 `status: untranslated`，完全沒有貢獻任何字元，所以 `DIAL_Z01.json` 的字元最先被掃到、拿到最低的編號區段。這次把 `DIAL_Z00.json` 全部翻完後，因為檔名排序在 `DIAL_Z01` 之前，它的字元變成**最先**被掃到、搶走了原本屬於 `DIAL_Z01`/`Z16`/`Z18`/`UI_HARDCODED` 字元的低編號——`ZH16.DAT`（字庫點陣圖）用新編號重新產生了，但**那幾個既有的 DDX 檔案還是用舊編號 encode 的、完全沒有重新 build**，於是同一個編號現在指向了完全不同的字，滿螢幕亂碼。

**修法（已改成永久預設行為，不是一次性補丁）**：`tools/font/build_font.py` 的 `build_zh_font()` 新增 `base_mapping` 參數；`main()` 預設會讀取既有的 `--output-map`（若已存在）當作基準，把裡面每個字元的編號**原封不動保留**，只給「這次新出現的字元」依序分配編號、接在舊字庫最大編號之後。驗證方式：用 `git show HEAD~1:...zh_mapping.json` 拿出這次改動前、跟目前部署的 `DIAL_Z01`/`Z16`/`Z18` 一致的舊 mapping 當基準，重新跑 append 模式，逐一比對舊 mapping 裡全部 2200 個字元的編號，**0 筆變動**，新字庫變成 4072 字（多出的 377 字全部接在後面）。新增 `--fresh` 旗標保留「真的要從零重算」的退路（會在說明文字裡明講這樣做很危險），但預設一律安全。**這個修正是永久性的，以後任何時候擴充字庫都不會再重演這個 bug**，不用每次都手動注意檔名排序。

## 8.2 真 bug：`TEXTWRAP.C` 一個潛伏的無號數下溢 infinite loop，被中文文字第一次踩中

修好字庫編號問題、實機重新測試後，遊戲會在「看完開場擄劫戰的對話、正式切換到互動 3D 畫面」的那一刻卡死——黑畫面、鍵盘滑鼠都沒反應，但 DOSBox-X 進程本身沒當掉（工作管理員看 `Responding: True`）。這個卡死點無論是新遊戲開場、還是讀取存檔進度，只要是「正式進入遊戲」都會發生。

**排查過程**（很長，記錄下來是為了下次遇到類似「結構驗證都過、實機卻卡死」的情況時，知道怎麼有效率地二分排查，而不是靠猜）：
1. 先懷疑是不是 §5.0 那次 EMS 記憶體瓶頸重演（字庫又變大了，4072 字比當時的 2198 字幾乎翻倍）。做了一個對照組：新字庫（4072 字）＋**原始英文** `DIAL_Z00.DDX`，結果順利進入 3D 畫面——證明**不是字庫大小/記憶體的問題**。
2. 改用二分法排查：寫了一個小工具（`scratchpad/apply_z00.py`，本 session 用完即丟，沒進 repo）反覆把 `DIAL_Z00.json` 一部分筆數還原成英文、一部分保留中文，逐次縮小範圍，每次都要完整重跑一次「主選單 → 開新遊戲 → 走過場書 → 對話 → 切換 3D 畫面」的操作序列（用 DOSBox-X AI Debugger MCP 的 `key_tap`／`capture_frame`，全程無滑鼠，靠固定的按鍵序列可靠重現）。十輪二分後鎖定到單一筆：**`DIAL_Z00.DDX#291`（node_id 294，「第一章：Into a Dark Night」章節標題／任務目標橫幅）**。
3. 派 agent 讀 `bak/SRC/DIALOG/DIALOG.C`／`bak/SRC/UI/TEXTWRAP.C` 追根因，同時自己動手驗證。找到：`gmain_start_dispatch()`（`GMAIN.C:178`）在切換到每一章的那一刻，會直接呼叫 `dialog_play_record(chapter + 0x125, 0)`（第一章 = node 294）播放這個章節橫幅，用的是跟一般對話框相同的 `dialog_render_text_with_tokens()` → `textwrap_draw_aligned()` 路徑，但**這筆記錄的 opcode（`wOp=6`）會覆寫掉這個對話框原本的版位（位置/寬高），換成一個窄很多的自訂尺寸**——這是本專案第一次有中文內容跑過這條「非預設版位」的路徑。
4. 讀 `TEXTWRAP.C` 的 `textwrap_draw_aligned()`：裡面有一段算「這個版位裝得下幾行、超出的幾行要捨棄」的迴圈，用全域變數 `g_wTextWrapLinesRemaining`（宣告成 `unsigned short`）當迴圈變數做減法：
   ```c
   for (g_wTextWrapLinesRemaining = 0;
        max_height < (int)((line_height + line_spacing) * ((count - fl) - g_wTextWrapLinesRemaining) - line_spacing);
        g_wTextWrapLinesRemaining++) { }
   ```
   這裡完全**沒有上界檢查**。當中文內容觸發 `g_bMixedZhMode` 把 `line_height` 強制拉高到 16px（比這個窄版位原本預期的字體高很多）、導致可用高度不夠裝下哪怕一行時，`g_wTextWrapLinesRemaining` 會一路遞增超過 `count - fl`。C 的無號數提升規則（`unsigned short` 在 16-bit int 平台上，因為 `int` 裝不下它的完整值域，會被提升成 `unsigned int` 而非 `int`）讓 `(count - fl) - g_wTextWrapLinesRemaining` 這個減法一旦被減數超過被減數，結果不會變成負數、而是**環繞成一個巨大正數**（例如 `2 - 3` 在無號 16-bit 下變成 `65535`），導致迴圈條件永遠成立、卡死——這正是黑畫面＋無回應、但進程沒當的行為模式。這個 bug 原本就潛伏在原始（英文）程式碼裡，只是英文內容從來沒有讓 `line_height` 超出版位預期過，直到這次中文橫幅才第一次踩中。
5. **修法**：在迴圈條件加一個上界檢查，防止 `g_wTextWrapLinesRemaining` 超過 `count - fl`：
   ```c
   for (g_wTextWrapLinesRemaining = 0;
        g_wTextWrapLinesRemaining < (unsigned short)(count - fl) &&
        max_height < (int)((line_height + line_spacing) * ((count - fl) - g_wTextWrapLinesRemaining) - line_spacing);
        g_wTextWrapLinesRemaining++) { }
   ```
   改在 `upstream/betrayal-at-krondor` commit `47d0a32`（`bak/SRC/UI/TEXTWRAP.C`），用 WSL2 Borland 工具鏈重新編譯，`VMCODE.OVL`／`SX.OVL` 仍 BYTE-IDENTICAL。**用最小重現案例驗證過修法有效**：把 `#291` 的內容換成純 ASCII `"AAA\x00"`（單行、無任何中文）在修法前會卡死，修法後順利進入 3D 畫面。

## 8.3 已知未解問題：即使修好 §8.2，中文內容在這個特定「章節橫幅」版位裡還是會卡死

修好 §8.2 後，原本期待 `#291`~`#299` 這 9 筆章節標題可以直接用完整中文翻譯，但**實測發現只要內容含有中文字（哪怕只有 4~5 個字、雙行），這個特定版位還是會卡死**；反而是純 ASCII 的兩行文字（例如 `"A\nB\x00"`）不會卡死。已經排除的假說：
- ~~字庫太大／EMS 記憶體不足~~——§8.2 步驟 1 已排除。
- ~~`\xf1`／`\xf0` 樣式控制位元組的處理方式~~——測過完全不含任何樣式位元組、純中文字的版本，一樣卡死。
- ~~文字太長、換行溢出成 3 行以上~~——測過極短的中文（4+5 個字，遠低於任何合理的寬度上限），一樣卡死；而更長的純 ASCII 兩行反而沒事。
- ~~§8.2 的無號數下溢 bug 本身~~——修法對純 ASCII 案例證實有效，但對短中文案例無效，代表**中文內容在這個版位裡踩到的是另一個、目前還沒定位到的問題**，不是同一個 bug 的殘留。

**追加排查（§8.2 修好之後又繼續查了一輪，找到一個很有機會就是真正答案的線索，但沒能在時限內百分之百證實）**：讀完 `DIALOG.C:850` 起的 `dialog_play_record()` 全文，發現我們這筆記錄（`wFlags=0x4014`，`wFlags & 0x200`／`0x400` 都是 0）走的是 `DIALOG.C:1405`~`1431` 那個 `else` 分支，這是一段**逐頁顯示、需要玩家按鍵/點滑鼠才能翻頁**的迴圈：

```c
do {
    if (dialog_wait_for_acknowledge(
            g_wTextWrapXAccum,
            g_wTextWrapLinesRemaining != 0 ? 0 : record->wFlags, 0, 1) == 0) {
        g_bCutsceneEscPressed = '\x01';
    }
    ...
    if ((done != 0) || (g_wTextWrapLinesRemaining == 0)) break;
    i = i + g_wTextWrapLinesDrawn;
    dialog_frame_draw(record, (int far *)0L);
    dialog_render_text_with_tokens(record, (unsigned char far *)0L, -1, 0, 0, i);
    ...
} while (done == 0);
```

關鍵在 `dialog_wait_for_acknowledge()`（`DIALOG.C:216`）收到的 `flags` 參數：**`g_wTextWrapLinesRemaining != 0` 時傳入的是 `0`，否則傳入 `record->wFlags`**。而 `dialog_wait_for_acknowledge` 開頭第一件事就是 `if (flags & 0x4000) return 1;`——`record->wFlags = 0x4014` 剛好有設這個 bit（`0x4014 & 0x4000 = 0x4000`），代表**這筆記錄原本設計成「不需要等玩家確認、自動繼續」**。純 ASCII 的 `"AAA"`／`"A\nB"` 之所以順利過關，很可能正是因為內容全部塞得進**一頁**（`g_wTextWrapLinesRemaining` 在渲染完就是 0），直接吃到 `record->wFlags` 那個自動繼續的路徑。**中文因為 `g_bMixedZhMode` 把行高強制拉到 16px，兩行塞不進這個窄版位、必須分兩頁顯示，`g_wTextWrapLinesRemaining` 變成非 0，這時傳進去的 `flags` 被換成 `0`（不含 `0x4000`），於是真的進入了「等玩家按鍵/點滑鼠翻頁」的迴圈——而且因為畫面在這整段期間都還是黑的（`gmain_start_dispatch` 要等 `dialog_play_record` 整個回傳才會 `palette_fade_in`，見 §8.2 步驟 3），玩家完全看不到有東西在等他確認。**

這個理論如果成立，代表**這根本不是傳統意義上的無窮迴圈 bug，而是「原文一頁裝得下、中文裝不下要多一頁，但這個特定橫幅的顯示流程本來就沒設計成會需要多頁」的情境沒被考慮到**。

**⚠️ 這個理論已經被實機測試明確推翻，不要再往這個方向查**：把這 9 筆重新翻回中文部署後，請使用者本人坐在電腦前、**親自用滑鼠實際點擊**卡住的黑畫面——完全沒有反應，跟先前 MCP 鍵盤模擬的結果一致。這排除了「只是在等分頁確認、滑鼠點一下就會過去」的可能性，**證實這確實是貨真價實的卡死，不是分頁等待輸入**。已經把這 9 筆（`DIAL_Z00.DDX#291`~`#299`）重新還原成英文（`localization/translated/DIAL_Z00.json` 的 `notes` 欄位記錄了這個結論），讓遊戲維持正常可玩，其餘 409 筆翻譯不受影響。

**下一個 session 如果要繼續查，已排除的假說清單（不要重複測試）**：
- ~~字庫太大／EMS 記憶體不足~~
- ~~`\xf1`／`\xf0` 樣式控制位元組的處理方式~~
- ~~文字太長、換行溢出成 3 行以上~~
- ~~§8.2 的無號數下溢 bug 本身（已修好但對這個問題無效）~~
- ~~分頁等待玩家按鍵/點滑鼠確認（`dialog_wait_for_acknowledge` 的 `flags&0x4000` 理論）~~——**已用真人滑鼠實測推翻**。

**下一步真正該做的**：`pause_execution` 抓到的 CS:EIP 每次都停在同一個 VGA 垂直回掃熱迴圈（`55FA:134A`~`134D`），已經證實這個訊號在游戲**正常運作**跟**真的卡死**兩種情況下都會出現、完全沒有鑑別度，不要再靠它判斷。真正需要的是**設一個落在 `textwrap_draw_aligned`／`dialog_render_text_with_tokens`／`dialog_wait_for_acknowledge` 這幾個函式範圍內的真斷點**，但目前沒有這幾個函式在 `KRONDOR.EXE` 裡的實際記憶體位址（`KRONDOR.MAP` 只有 segment 層級的資訊，沒有個別 public symbol 位址）。可行的做法：
1. 在 WSL 工具鏈重新編譯時，想辦法讓 Turbo Link 產生**含 public symbol 的完整 `.MAP` 檔**（目前的編譯指令似乎沒開這個選項），這樣就能查到這幾個函式的確切位址，直接下記憶體斷點。
2. 或者從 `dialog_apply_style_state()`（`DIALOG.C` 裡處理 `wOp==6` 版位覆寫的那個函式，用 grep `"sub2->wOp == 6"` 找）開始，比對這個窄版位覆寫後的實際數值（`nA1`/`nA2`/`nA3`/`nA4` = `12`/`160`/`160`/`30`，但欄位對應到 `StyleState` struct 的哪個成員還沒確認），配合 `dialog_render_text_with_tokens()`（`DIALOG.C:564`）裡 `g_bMixedZhMode` 被設起來後受影響的所有分支，逐一比對「中文開啟 `g_bMixedZhMode`」跟「純 ASCII 不開啟」兩條路徑在這個窄版位下實際算出來的數值差異——這次沒能算出 `pStyle->header[]` 的實際數值就是因為沒有斷點可以直接讀暫存器/記憶體，只能純推理。
3. 或者乾脆参考 §7.2 已經建立的「小字級中文字型」機制（`font_draw_zh_glyph_small`／`ZHSTAT.DAT`）——如果這個章節橫幅版位本來就是設計給比 16×16 小的字體用，比照角色屬性面板的解法（改用 10×10 小字型，不強制 `g_bMixedZhMode` 把行高拉到 16px），也許能繞開整個問題的根源（`line_height` 被拉高導致的一連串效應），不用再深究這個特定的排版計算 bug 到底卡在哪一行——**這可能是投資報酬率最高的方向**，因為不需要先找到卡死的確切原因，只要讓中文在這個版位裡也維持跟原文差不多的行高，很可能就不會再觸發這整條有問題的路徑。

## 8.4 尚未解決：撿屍體導致 Heap Corrupt 閃退

**症狀**：開新遊戲，一路看完擄劫戰對話、進入互動 3D 畫面後，畫面上有一具被幹掉的刺客屍體。點擊這具屍體，本來應該顯示一段描述文字（`DIAL_Z00.DDX#365`，「Gorath looked for supplies...」／中文「@0搜尋著補給……」），接著進入戰利品／物品畫面。**用中文版 `DIAL_Z00.DDX` 時，遊戲會直接閃退**，畫面顯示：

```
A system error has occured.  Please write down the following data and contact Sierra Customer Support:
MEM:34 (Heap Corrupt!)
Null pointer assignment
```

這是遊戲自己的記憶體管理員在偵測到堆積（heap）內部結構被破壞時印出的錯誤，代表某處發生了越界寫入，而且偵測到的當下（撿屍體、切換到物品畫面）不一定就是實際寫壞記憶體的那一刻——經典的「破壞發生在早，偵測在晚」情況。

**排查記錄（已用實機測試逐一驗證，不要重複測試）**：
1. **不是字庫大小的問題**——用這次 session 之前的舊字庫（3695 字）配上目前的中文版 `DIAL_Z00.DDX`，**一樣閃退**；用原始英文版 `DIAL_Z00.DDX`（不管哪個字庫），完全正常，文字顯示、物品畫面都沒問題。
2. **不是特定「撿屍體」相關的那幾筆翻譯**——把最直接相關的 4 筆（`#364`／`#365`／`#367`／`#368`，內容都是「檢查屍體」「翻找補給」之類）還原成英文，其餘 405 筆仍是中文，**還是一樣閃退**。代表觸發原因不是這幾筆本身的內容，可能是其餘 405 筆裡的某一筆（甚至可能是更早顯示過的其他章節的中文內容，只是損壞效應延後才被偵測到），也可能不是單一筆文字內容的問題。
3. **過程中額外抓到並修好一個真的越界讀取 bug，但這個 bug 不是這次閃退的根因**：`DIALOG.C` 的 `dialog_render_text_with_tokens()` 在展開 `@0`／`@1` 這類角色代稱時，會讀取 `g_pMainScratchBuf[nScratchLen - 2]` 來判斷前一個字是不是英文的 `a`（用來決定要不要插入 `an` 的文法修正）；如果 `@0` 出現在字串最前面（例如 `"\t@0..."`，`\t` 之後緊接著就是 `@0`，這時 `nScratchLen` 只有 1），`nScratchLen - 2` 會變成 `-1`，讀到配置緩衝區起始位置**前面**的位元組——貨真價實的越界讀取，剛好完全符合 `#365`（`"\t@0搜尋著補給"`）的樣式，一度以為就是這次閃退的原因。已在 `upstream/betrayal-at-krondor` commit `4ecd59d` 修正（加 `nScratchLen >= 2` 的防呆檢查），`VMCODE.OVL`／`SX.OVL` 仍 byte-identical。**但修好之後閃退依然發生**，代表這不是（或不是唯一）根因，只是一個順手抓到、值得留著的獨立修正。

**目前處理方式**：`localization/translated/DIAL_Z00.json` 裡 409 筆翻譯內容**完全保留**（`status` 沒有改動），但**部署到 `dist/test_v100_zh/` 的 `DIAL_Z00.DDX` 暫時整個換回原始英文版**，直到抓到真正原因為止——已經花了不少輪二分法測試把範圍縮小到「4 筆明顯相關的以外，還有別的東西」，但每一輪都需要真人重新開新遊戲、走到屍體、點擊才能驗證，成本很高，這次先在此打住。

**下一個 session 建議的做法**：
1. **繼續二分法縮小範圍**：目前已知 405 筆裡有問題（或問題其實在別的章節，只是延遲發作），可以從 `localization/translated/DIAL_Z00.json` 挑一半還原成英文、重新 build、請使用者重新測試，比照這次的方法對半找，大概還要 3~4 輪就能鎖定到單一筆或一小群。
2. **認真考慮「破壞發生得更早」的可能性**：這次只测試了「還原 DIAL_Z00 的某些筆」，還沒測過「如果連 `DIAL_Z16`（擄劫戰對話）都還原成英文，撿屍體會不會就正常了」——如果連 `DIAL_Z16` 都需要還原才會沒事，代表問題根本不在 `DIAL_Z00`，而是更早顯示的對話內容造成的延遲性堆積損毀，那整個排查方向都要重新來過。這個測試成本較低（因為 `DIAL_Z16` 只有 211 筆而非 405 筆），建議下次優先做。
3. 如果想避免每輪都要真人操作，值得評估看看能不能請使用者**存一個「剛進入 3D 畫面、還沒撿屍體」的存檔**，之後每輪二分法就能直接讀檔測試、不用重新看一次過場對話，大幅降低每輪的操作成本。

## 7. Git 狀態

- 主專案 `betrayal-at-krondor-for-zh`：`master` 分支。**目前工作目錄裡大量檔案都還是未 commit 的異動**（`localization/translated/*.json` 新翻譯內容、`localization/generated/ZH16.DAT`／`zh_mapping.json`、`localization/glossary/glossary.json`、`docs/research/text-surface-inventory.md`、多個 `tools/text/*.py`／`tools/font/build_small_font.py`、新增的 `tools/text/objinfo_translate.py`、`tests/unit/test_objinfo_translate.py` 等）——這是本專案一貫的作法（只在使用者明確要求時才 commit，翻譯/工具異動不會自動 commit），下一個 session 接手前**先 `git status` 確認清楚哪些是已完成、待 commit 的工作，不要誤以為是別人動過的髒狀態**。`origin` 指向使用者自己的 GitHub repo（`https://github.com/pmanyeh/betrayal-at-krondor-for-zh`）——commit/push 都對這裡，不是上游來源。
- `upstream/betrayal-at-krondor`：本地領先 origin 多個 commit，且**這個 sub-repo 裡的 commit 是本專案慣例會直接做的**（每次重編譯 exe 前，先在這裡 commit C 原始碼異動，才能讓 WSL clone `git pull` 取到）。目前分支最新（由舊到新）：`...` → `1276b58` → `4b681d3` → `378050c` → `0e2f249` → `c7feb11` → `f38a089` → `12b9a14` → `42f6fd4` → `8ddc763` → `d0af98c` → `47d0a32`（§8.2 `TEXTWRAP.C` 無窮迴圈修正）→ `4ecd59d`（§8.4 過程中順手修好的 `DIALOG.C` `@N` 越界讀取）→ 本次 session 新增的 8 個 commit：`bddbfe0`（`g_bSmallZhMode` 章節橫幅 + `dialog_show_by_key` 名稱表初始化）→ `ddb10ea`（角色屬性面板 `Ratings:`/`Condition:` 標題改小字）→ `78a0ad1`（物品欄格子名稱＋耐久度改小字）→ `62c8bb1`（`shopkeeper`／貨幣字串翻譯）→ `591d041`（物品欄價格行也改小字）→ `9ec0558`（物品檢視面板名稱/耐久度標籤）→ `284b7ae`（補 `INVINSP.C` 缺的 `FONT.H` include）→ `566e11c`（More Info 詳情彈窗＋紮營畫面＋Party Gold 翻譯）。詳見 §9。**這些 commit 永久只留在本地 clone，不 push 回 origin、不對上游開 PR**——這是專案的固定規則，不是暫時待確認事項。上游是還原保存專案、不是 modding 專案，我們的中文化修改只在自己的專案（`betrayal-at-krondor-for-zh`）裡管理和 commit。

## 8.5 2026-08-21 Debug 收尾：DDX 子記錄位址、章節橫幅與 `@N` 名稱替換

> **本節是 §8.3／§8.4 的後續實測結論；其中「章節橫幅仍無法中文化」與「屍體閃退尚未解決」的舊結論，均已被下列修正取代。**

### A. 屍體互動的 `MEM:34 (Heap Corrupt!)` 已定位並修正

**根因不是 DOSBox cycles，也不是中文字型或特定一段屍體文稿。** `tools/text/ddx_pack.py` 重建 DDX 時，錯把 `DdxChoice` 的 `dwTarget_key` 當作獨立的 16-bit `nA3` 欄位處理；實際上它由 `nA3`（低 16 位）和 `nA4`（高 16 位）組成 32-bit 的子記錄檔案位址。

中文翻譯改變各 record 長度後，父選項仍跳往英文檔的舊位址（例如屍體路徑由 record `#363` 跳往舊 `0x12CC4`，但中文版正確子記錄已移到 `0xC347`）。遊戲從檔案尾端以外讀到未初始化資料，誤配出超大矩形高度，`draw_rect_filled()` 的 span table 寫穿記憶體，最終才在之後配置 `KEYWORD.DAT` 時由 heapcheck 報 `MEM:34`。

**修正：**

- `ddx_pack.py` 現在會合併 choice 的 `nA3 | (nA4 << 16)`，依新 record offset 重映射後再拆回兩個 word。
- `DdxOp.nA3` 是一般運算元，**絕不能**當指標重映射；舊作法也已移除。
- `tests/unit/test_ddx_roundtrip.py` 新增 32-bit child target 測試，以及「opcode operand 不變」斷言；相關 DDX tests 共 **15 passed**。
- 重新執行 `ddx_translate.py build scratchpad/pristine/DIAL_Z00.DDX localization/translated/DIAL_Z00.json dist/test_v100_zh/DIAL_Z00.DDX` 後，實機點擊屍體已正常顯示文字、不再閃退。

**重要：** 任何已經用舊版 packer 建出的本地化 DDX，都必須從原始 DDX **重新 build** 才會帶到此修正；只改 Python 工具不會回頭修好既有 `.DDX` 成品。

### B. 章節橫幅已恢復中文，並使用 10×10 小字形

章節橫幅是 `DIAL_Z00.DDX#291`～`#299`，不是另一份英文圖片文字。先前畫面仍顯示英文，是因為部署目錄裡仍是舊打包的 `DIAL_Z00.DDX`；用正確的重建成品後已帶入九筆中文。

這個版位高度只有 30 px，16×16 中文會造成舊有排版/流程問題。因此新增 `g_bSmallZhMode` 小字模式：

- `DIALOG.C` 識別章節橫幅版位（`wFlags == 0x4014` 與 style rect `12,160,160,30`）後啟用小字模式。
- `FONT.C`／`FONT.H` 讓中文字的繪製、像素寬度與 glyph metrics 在此模式使用 10×10。
- `TEXTWRAP.C` 在小字模式採 10 px 行高及 10 px 中文寬度；其他對話仍是 16×16。
- 初始 `ZHSTAT.DAT` 只有角色面板所需的 35 個字，章節字出現時只會留少數字形。已用 `tools/font/build_small_font.py localization/translated/DIAL_Z00.json --zh-mapping localization/generated/zh_mapping.json --output dist/test_v100_zh/ZHSTAT.DAT` 重建為 **1,735** 個小字 glyph，實機確認章節一完整顯示中文。

未來只要新的小字版位會使用其他 DDX 的中文，必須把那些譯稿字元也納入 `ZHSTAT.DAT` 的建置來源；不能沿用只含 35 字的舊檔。

### C. `@0`～`@5` 角色佔位字元

屍體文稿 `DIAL_Z00.DDX#365` 的 `@0` 曾顯示成一大片空白，並不是在 `@0` 後直接接中文字的編碼問題；引擎已吃掉 placeholder，但直接由腳本呼叫的 `dialog_show_by_key()` 沒有建立 `g_speaker_names[]` 表，所以得到空字串。

`dialog_show_by_key()` 現在先呼叫 `dialog_combatant_name_table_init()`，因此 `@0` 已可正常替換為 `Gorath`。在 `@0` 後加空白只會影響排版間距，不是修正必要條件。角色資料本身目前仍儲存英文名稱；若要讓 `Gorath` 顯示為「戈拉斯」，需另做角色名稱在執行期的本地化，不能只改 DDX 文稿。

### D. 實機驗證結果

1. 點擊第一章 3D 畫面屍體：中文文稿正常顯示，後續不再 `MEM:34`／`Null pointer assignment`。
2. 章節一地圖橫幅：正常顯示「第一章：踏入黑暗之夜／護送戈拉斯前往克朗多！」的 10×10 中文小字。
3. `@0`：可替換為 `Gorath`，不再留下空白佔位區。

## 9. 2026-08-21～23 Session：新章節翻譯 + 物品名稱系統 + UI 版面修正（大量小字模式擴充）

延續 §8.5 之後的同一輪對話 session（跨了兩次日期換日，實際是連續工作）。內容分五塊：新翻譯章節、全新的物品名稱系統、一大批 UI 硬編碼字串＋版面 bug 修正、確認「More Info」按鈕屬於未開發的資源系統、以及一個**還沒解決但已經有明確線索**的物件貼圖雜色 bug。

### 9.1 新翻完的 DDX 章節（共 201 筆，+ 之前累計＝1234 筆）

- `DIAL_Z02`（38）／`DIAL_Z03`（38）／`DIAL_Z07`（26）：三個結構很像的「路口濃霧敘事＋墓誌銘」章節，一起翻完，順便在 §5.0 已有的墓誌銘翻譯風格（`姓氏．名字\n「雙關語式墓誌銘」`）基礎上繼續套用。過程中發現的新地名/人名見詞彙表新增清單。
- `DIAL_Z04`／`DIAL_Z05`／`DIAL_Z08`／`DIAL_Z10`／`DIAL_Z11`／`DIAL_Z12`（合計 46 筆）：全都是小檔案，一次翻完。`Z04` 是卡瓦爾堡被摧毀的後續劇情（呼應 `Z03` 埋下的伏筆）；`Z08` 是戈拉斯／歐文往艾爾凡達路上的對話，帶出新種族詞 `eledhel`（光精靈，仿照 `moredhel` 音譯為「伊列德人」）；`Z12` 提到「六賢者」洞穴，直接呼應 `Abbot's Journal`／`Wooden Chest`／`Shell` 這幾個物品名稱（見 §9.2），是刻意的劇情道具伏筆。
- `DIAL_Z24`（28 筆）：幽暗林商店群（八間店名＋制式風味文字）＋一段**開發者留下的 meta 玩笑對話**（`#21`／`#27`／`#29`／`#30`，逐字元樣式標記，內容是角色們在討論「要不要用作弊手段開鎖」「這一章該不該現在結束」，玩家看不太出來但翻譯時要小心逐字元 `\xf1`/`\xf3` token 對齊，這批是本次 session token 結構最複雜的幾筆）。
- `DIAL_Z29`（25 筆）：**帕格在生命石洞穴前向歐文/戈拉斯揭露真相**的主線高潮劇情——冒牌穆爾曼達穆斯其實是潘塔西亞人偽裝、瓦爾赫魯靈魂被封印在生命石裡、帕格自曝出身克萊迪宮廷廚房小廝、馬克羅斯早已預見兩人的介入。新詞彙全部加入 glossary（`false Murmandamus`→冒牌穆爾曼達穆斯，比照既有的「冒牌夜鷹會」譯法）。

全部經過跟之前批次一樣的驗證流程：`ddx_translate.py scaffold` 確認無 source drift、`extract_tokens()` 逐筆比對 token 結構、`ddx_rebuild_all.py` 全量重建 0 fallback、`pytest tests/unit` 全過。

### 9.2 全新發現：物件簡短名稱其實在 `OBJINFO.DAT`，已完整翻譯（137 筆）

之前的 Phase 8 文字盤點（`docs/research/text-surface-inventory.md`）漏掉了一塊：物品欄格子裡顯示的**物品本身的簡短名稱**（如「Long Sword」，不是 `DIAL_Z18` 那種長篇風味文字，也不是 `INVENTOR.C`／`INVINSP.C` 的欄位標籤）到底存在哪裡，一直沒查過。這次查到：

- **來源**：`KRONDOR.RMF` 裡的 `OBJINFO.DAT`，由 `ITEMTBL.C:itemtbl_load()` 整包讀進 `g_pItemDefTable`。
- **格式**：全遊戲**目前碰過最簡單**的格式——沒有字串池、沒有 offset 表，就是 138 筆固定 80-byte 的 `ItemRecord`（`INCLUDE/structs.h:837`）緊接著排列：前 32 bytes 是 NUL 補齊的 `pName`，接著 `wFlags`（32-33 byte）、`wName_split_off`（**34-35 byte，不是 32-33！**，見下面的踩坑記錄）、傷害/價格等數值欄位。
- **新工具**：`tools/text/objinfo_translate.py`（`scaffold`／`status`／`build`，介面比照 `ddx_translate.py`）。因為 `pName` 是固定 32 bytes，`build` 會檢查編碼後是否 ≤31 bytes，超過就安全 fallback。
- **翻譯內容**：137 筆（index 0 為空、不使用）全數譯完，存在 `localization/translated/OBJINFO.json`。翻譯時發現大量物品名稱其實已經在 `DIAL_Z18` 的風味文字內文裡被直接引用過（例如「銀刺」「禁制鑰匙」「那夫沙油」「真視茶」「基爾迪斯棘刺」），逐一比對後採用了那些既有譯名，並回頭修正兩處 `DIAL_Z18` 自己沒抓到的舊譯名不一致（`Aventurine` 東陵石→砂金石、`Flame Root Oil` 火根精油→火根油）。約 20 個新詞彙加入 glossary（`Fadamor`、`Dalatail`、`Sarig`、`Coltari`、`Kalem`、`Dorcas`、`Nivek`、`Glazer's Guild` 等），並回頭修正了先前 `DIAL_Z02`/`DIAL_Z07` 兩筆墓誌銘裡跟這批新詞撞名但拼法不一致的地方（人名 `Dalatail`／`Fadamor` 統一轉寫）。

**⚠️ 真 bug（已修正）：`objinfo_translate.py` 寫錯了 `wName_split_off` 的位元組偏移量，把 `wFlags` 清空了。**
`ItemRecord.pName[32]` 後面接的是 `wFlags`（32-33 byte），**再來才是** `wName_split_off`（34-35 byte）——第一版 `build()` 把「重設成單行」這行寫在 `offset + NAME_SIZE`（=32），以為那是 `wName_split_off`，實際上蓋掉的是 `wFlags`。`wFlags` 正是耐久度百分比／堆疊數量徽章要不要顯示、顯示成 `%d%%` 還是純數字的判斷依據，全部清零後，**所有翻譯後物品的耐久度/數量徽章完全消失**（使用者實機截圖抓到，物品欄格子空白一片、講價視窗數字不見）。已修正偏移量（`offset + NAME_SIZE + 2`），逐位元組驗證除了名字本身跟 `wName_split_off` 外其餘欄位跟原版一致，並新增 `tests/unit/test_objinfo_translate.py` 防止同樣的偏移量錯誤再發生。**這是一個很好的教訓：手動計算 C struct 的欄位偏移量一定要對照原始 struct 定義逐欄位算，不要憑印象假設「名字後面接著的就是我要的那個欄位」。**

`wName_split_off`（物品欄格子裡「英文名字太長要拆兩行」的斷行位置，字元索引）目前策略是**全部強制設回 0**（單行置中顯示）——中文譯名普遍只有 2-6 個全形字，早期在物品欄格子裡測試時（§9.3 的排版問題出現前）名稱本身沒有塞不下的狀況，因為後來發現的排版問題其實是「名稱＋耐久度那一行」用了 16×16 標準字高、跟下面的價格行擠在一起（見下方 §9.3），不是名稱本身太長，所以維持強制單行的做法沒有改。

### 9.3 一整批 UI 硬編碼字串＋版面重疊 bug（`g_bSmallZhMode` 應用範圍大幅擴大）

使用者實機截圖陸續抓到好幾個「中文字比原本設計的英文字高，擠壓/裁切到旁邊文字」的情況，全部照 §7.2 已經驗證過的模式解決：**把該處的中文改用既有的 10×10 `g_bSmallZhMode` 小字模式**（不是重新設計版面座標，先前 §7.2 已確認這個模式好用、可重複套用）。這次一口氣把小字模式的套用範圍擴大到：

- `INVENTOR.C` 物品欄格子（`invui_grid_render`，商店／裝備格通用）：「名稱＋耐久度」那一行、下面的「NN金幣 NN銀盾」價格行，兩行都改小字（原本只改了名稱那行，使用者截圖抓到價格行還是大字、又擠在一起，第二輪才補齊）。
- `INVINSP.C` 物品檢視面板（`invinspect_item_flow`）：物品名稱＋`數量：`／`剩餘次數：`／`價值評等：`／`耐久度：` 這行，跟底下的 `使用中、可修復`／`已損壞` 狀態行，都改小字，耐久度行的 y 座標額外往下微調 2px 留呼吸空間（比照 §7.2 `charscreen_draw_stat_row` 的先例）。
- `INVINSP.C` 的「More Info」詳情彈窗（`invinspect_render_details`）：`突刺`／`揮砍`（Thrust/Swing）欄位標題跟底下所有數值列，整個函式都包進小字模式。
- `ENCAMP.C` 紮營畫面的「生命/體力」「口糧」欄位標題也改小字（這處實測沒有明顯重疊，但基於一致性跟預防性一併處理）。

**每次擴大 `g_bSmallZhMode` 涵蓋範圍，都要記得把新用到的中文字元也餵進 `ZHSTAT.DAT`**（這是 §8.5-B 自己寫下但這次還是差點忘記的教訓）——`tools/font/build_small_font.py` 原本**只能吃一個翻譯來源檔**，這次把它改成可以吃多個（`nargs="+"`），現在標準呼叫方式是：

```bash
python tools/font/build_small_font.py \
  localization/translated/UI_HARDCODED.json \
  localization/translated/DIAL_Z00.json \
  localization/translated/OBJINFO.json \
  --zh-mapping localization/generated/zh_mapping.json \
  --output dist/test_v100_zh/ZHSTAT.DAT
```

**每次改完任何一個小字模式涵蓋的畫面，都要重跑這行**（目前 1827 個小字 glyph）。忘記跑的話，新用到的字會安靜顯示成空白（不會報錯、不會當機，很容易漏看）——這正是這次踩過的坑（角色屬性面板漏了「鑑」「甲」「偵」三個字，起因是 §8.5-B 重建 `ZHSTAT.DAT` 時只用了 `DIAL_Z00.json` 一個來源，沒帶入 `UI_HARDCODED.json`）。

**同時翻掉的純硬編碼字串**（跟 DDX 無關，直接改 C 原始碼字串常數，記錄在 `localization/translated/UI_HARDCODED.json`，目前共 55 筆）：

- `shopkeeper`→店主、`tavernkeeper`→酒館老闆（`DIALOG.C` 的 `@N` 通用 NPC 稱呼預設值）。
- **貨幣用詞統一**：原始英文其實用兩套不一致的說法指同一種貨幣——`gstate_format_money()` 的 mode 1 用 `gold`/`silver`，mode 2 用 `sovereign`/`royal`；`INVENTOR.C` 自己還有一份重複的 `gold`/`silver` inline 版本。全部統一成物品名稱系統已經確立的「金幣」／「銀盾」，順便把英文版原本的複數字尾邏輯（`strcat(buf,"s")`、`%c` 三元運算子）整段刪掉——中文名詞不需要複數變化，刪之前先確認過兩個分支在數值上會輸出一樣的字串，才敢刪。
- `INVINSP.C` More Info 彈窗內容：`Base Dmg:`／`Accuracy:`／`Armor Mod:`／`Active Mods:`／`Resistances:`／`Bless Type:`／`Racial Mod:`／`None`／附魔詞（`Poisoned`/`Frosted`/`Flaming`/`Steelfired`/`Enhanced`）／種族名（`Tsurani`/`Elf`/`Dwarf`/`Human`）／`Strength`/`Skill`／`Quarrel`/`CrossBow`／`Affecting`/`Can affect player statistics`，整批翻完。
- `ENCAMP.C` 的 `Health/Stamina`／`Rations` 欄位標題、` of ` 分隔字（改成 ` / `，故意保留半形斜線不用中文字元，因為它只會出現在兩個 `itoa()` 數字之間）。
- `MODALSCR.C` 的 `Party Gold:`→隊伍金幣：、旅費顯示的 `%d sovereigns`。
- `INVENTOR.C` 的 `Unavailable`（物品無法估價時顯示）→無法估價。

翻譯這批之前都先跑過關鍵字掃描，確認沒有跟已有 glossary／既有 DDX 譯名衝突（例如 `Condition:` 在角色面板脈絡是「狀態」，但在物品脈絡刻意改用「耐久度」，避免玩家搞混兩種不同概念）。

**順手發現並修正一個完全無關的既有 bug**：`DIAL_Z18.DDX#319`（「伊夏之眼」法術卷軸標題）的翻譯裡多了一個 `\xf1` 樣式位元組（4 個而不是原文的 3 個），導致這筆早就翻好、早就部署過的內容其實一直在悄悄 fallback 回英文，只是因為 §5.2 當初驗收時沒有針對這筆特別測到而沒被抓到。已修正字元分組讓 token 數對齊。

### 9.4 確認：「More Info」按鈕本身沒辦法翻——屬於還沒開發的 `MenuPage`／`.dat` 資源系統

`invinspect_render_details()`（§9.3 翻完的詳情彈窗）內容本身是硬編碼 C 字串沒錯，但**觸發它的「More Info」按鈕、以及旁邊「Repair」之類的按鈕標籤，全文搜尋 `upstream/betrayal-at-krondor/bak/SRC/` 完全找不到對應字串**——追進呼叫端（`INVINSP.C` 裡 `page->pEntries + 0x23` 那段）確認它是從 `MenuPage` 結構的 `pEntries[...].pPrimary_label` 讀出來的，屬於 `docs/research/text-surface-inventory.md` §4 早就盤點過、但**還沒開發解析/封裝工具**的 `MenuPage`／`NamedTable`／`DialogWidget` 資源家族（`.dat` 檔，字串池＋offset 修補格式）。這不是這次能翻的範圍，工程量遠大於改幾個硬編碼字串，需要專門排一個 phase 去寫通用 codec（§4 文件裡已經有建議的技術路線，`fmap_twn.dat`／`KEYWORD.DAT` 格式最簡單，適合當作第一個試點）。**下次使用者截圖抓到某個按鈕/選單標籤沒被翻譯時，先確認它是不是也屬於這個資源家族，不要預期能像硬編碼字串一樣三兩下翻完。**

### 9.5 ⚠️ 尚未解決：物件貼圖縮小後會出現雜色噪點（已有具體線索，缺live驗證）

使用者實機截圖抓到：世界地圖上**距離較遠、貼圖被縮小**的樹木／物件，邊緣會冒出一堆不該有的藍色雜點；同一個物件放大／靠近觀察時完全乾淨。同樣情形也出現在物品欄圖示（木杖等）。

**已經確認、可以排除的假說**（不要重複測試）：

- ~~字庫大小/EMS 佔用~~——把字庫砍到只剩 500 字（EMS 佔用從 9 個分頁降到 1 個），雜點仍在。
- ~~畫面上正在畫中文字~~——把 DDX／物品名稱全部換回純英文（該畫面完全沒有任何中文字被畫出來），雜點仍在。
- ~~DOSBox-X 的 OpenGL 縮放濾波器（fringe/halo 效應）~~——用完全沒被動過的原版英文遊戲資料夾（複製到 `scratchpad/pristine_playtest/`，同一份 `dosbox_zh_test.conf` 設定只是改掛載路徑）重現同一場景，**貼圖完全乾淨**，證實不是 DOSBox-X 顯示設定的問題，是我們的 build 才有的問題。
- **使用者明確表示：這個問題在這次 session 幫字型加上 EMS（更早的 §5.0）之前就已經存在，不是這次新引入的回歸。**

**目前最有機會的理論**：`upstream/betrayal-at-krondor/bak/SRC/SYS/EMSIMG.C` 裡負責把 EMS 分頁映射回可讀記憶體位址的四個函式（`emsimg_sprite_blit_scaled_paged`／`emsimg_gouraud_blit_paged`／`emsimg_putsprite_ems_swap`／`emsimg_map_then_call_180c`），全部用同一種寫法判斷「這個 `wImageData` 數值到底是 EMS 分頁鏈編號還是已經解析好的記憶體 segment」：

```c
page_id = sprite->wImageData;
if (page_id < 300) {
    mapped = ems_map_resource_pages(page_id);
    sprite->wImageData = FP_SEG(mapped);
}
```

這是一個**用數值大小猜測型別**的脆弱寫法（EMS 分頁鏈編號是小整數，真正的記憶體 segment 通常遠大於 300，所以原作者假設「< 300 就一定是分頁編號」）。物件縮放繪製 (`emsimg_sprite_blit_scaled_paged`) 正好是這條路徑；如果某個圖片資源的分頁鏈編號剛好落在這個門檻附近或超過（例如整局遊戲下來，EMS 分頁鏈編號的計數真的超過 300），就會被誤判成「已經是位址」，跳過映射步驟，直接拿一個不是真正 segment 的小整數當記憶體位址去讀，讀到的是垃圾資料——完全符合「縮小的遠處物件才會出現雜點」的現象（如果不同縮放比例的貼圖是分開存放、各自有獨立分頁編號，數值較大/較晚配置的那批更容易越過 300 這個門檻）。使用者確認這個問題比字型 EMS 化還早，代表這個 `< 300` 門檻很可能本來就已經脆弱、只是這次才被踩中或才被注意到，不一定是我們自己的新增程式碼直接造成。

**已經嘗試但還沒成功的即時驗證**：這次 session 難得拿到含 public symbol 的完整 `.MAP` 檔（跑 `bak build link` 這個獨立 stage 會強制用 `tlink /m` 而不是平常增量建置預設的快速 relink，之前 §8.3 卡住的「沒有函式位址」限制解除了——`_EMSIMG_SPRITE_BLIT_SCALED_PAGED` 靜態位址是 `26CE:024D`），但**要把這個靜態位址換算成遊戲實際執行時的記憶體位址，需要知道程式載入時的 load segment**，而這個只能在程式剛啟動、第一行指令都還沒執行的那一刻準確量到（`e_cs`/`e_ip` 在這個 EXE 的 MZ header 裡都是 0，代表入口點就在 load segment 本身，是最乾淨的校準點）。這次沒有用 `-break-start` 重新啟動遊戲去抓這個校準點（會中斷使用者當時的遊戲進度），改用「中途 `pause_execution()` 抓到的 CS 反推」的土法煉鋼方式，但抓到的 CS 每次都落在一個底層 VGA 垂直回掃等待迴圈（`55FA` 附近），這段程式碼**不在 `krondor.exe` 檔案內容裡**（搜尋編譯後的 exe 檔案位元組找不到對應片段，可能是連結進來的圖形函式庫，來源不明），沒辦法拿來反推。

**下一個 session 如果要繼續查，建議直接做**：
1. 用 `-break-start` 搭配 AGENT_GUIDE.md 說明的方式重開一次遊戲（`dosbox-x.exe -defaultdir -break-start C:\KRONDOR.EXE`，需要注意 AGENT_GUIDE 提到的「不能用管道重導向 stdout，否則偵錯器主控台初始化會讓整個 process 當掉」那個限制），在**入口點那一刻**用 `get_debug_status()` 抓 CS，這個 CS 值減去 0（因為 `e_cs=0`）就是 load segment。
2. 用這個 load segment 加上 MAP 檔裡的靜態位址（`26CE:024D`），算出 `emsimg_sprite_blit_scaled_paged` 的實際執行位址，下斷點。
3. 想辦法讓遠處縮小的物件被畫出來那一刻剛好停下（可能需要先 `continue_execution()` 讓遊戲跑到那個場景、視角轉到有遠處小物件的地方，再觸發斷點），讀出 `page_id`（`sprite->wImageData`）的實際數值。
4. 同時讀 `g_ems_total_pages`／`g_free_memory_kb`（`SRC/SYS/EMS.C`）目前的值，確認 EMS 分頁鏈編號有沒有真的逼近或超過 300。
5. 如果數值確實接近/超過 300，代表理論成立，修法方向可以考慮：（a）評估把 `< 300` 的門檻調高到一個更有把握的安全值（但要先搞清楚這個 300 是不是有什麼別的理由不能隨便調），或（b）幫 `ImageRecord`／`sprite` 結構額外加一個明確的「是否為 EMS 分頁編號」旗標欄位，不要再用數值大小猜測型別——這是治本的作法但改動面較廣，屬於 §prefer-proper-fix-over-workaround 那種值得花力氣做對的情況。

臨時測試留下的檔案：`scratchpad/pristine_playtest/`（原版遊戲資料夾的可寫入副本，用來對照測試，可以留著給下次用）、`dist/dosbox_pristine_compare.conf`（掛載那個副本資料夾的 DOSBox-X 設定檔）。

### 9.6 下一步建議

1. ~~**優先**：§9.5 的物件貼圖雜色 bug。~~ **已完成**：根因與原始碼修正見 §9.7，正式重建、部署及冷啟動實機驗收見 §9.8。
2. **繼續翻譯**：還有約 4,700 多筆待翻（29 個章節檔的 scaffold 都已建好）；`OBJINFO.DAT`／`UI_HARDCODED.json` 兩個系統目前已知範圍內都翻完了，如果之後又發現新的硬編碼字串或新的資源類別，照這次的模式（先讀原始碼確認是硬編碼還是資源檔、查 glossary、翻完後關鍵字掃描比對）處理即可。
3. **`MenuPage`／`.dat` 資源系統**（§9.4）：如果想解決「More Info」這類按鈕標籤，需要先開發通用 parser/packer，工程量比字串翻譯大很多，§4 文件裡已經有建議的技術路線跟起步難度排序。
4. 翻譯品質校對：這次新翻的 201+137+55 筆內容都還沒有第二人核對過，尤其 `DIAL_Z29` 是重要主線劇情，建議找機會抽查。

### 9.7 2026-08-23：物件縮放雜色根因已定位並修正原始碼

§9.5 的 EMS page-id 理論已用 live debugger **推翻**。中文版實際偵測到 932 個 EMS pages，但重現雜點時 200 次 `emsimg_sprite_blit_scaled_paged()` 呼叫只使用 page 1、10、43、50；當時整個遊戲也只配置約 22 pages，沒有任何 `page_id >= 300` 的呼叫。

真正根因是 `gfx169d.h` 把 `POLYRAST.ASM` 內兩個 CS-resident palette remap table 的 near offset 寫死：1.00 用 `0x005c/0x0a5c`，1.02 用 `0x0066/0x0a66`。原版 EXE 的 rasterizer 確實位於 `CS:1324`、fog table 位於 `CS:005c`；但中文 resident code 變大後，TLINK 為該 segment 選出的 paragraph frame 改變，中文版 rasterizer 位於 `CS:1322`、fog table 實際位於 `CS:005a`。呼叫端仍傳入 `0x005c + bucket*0x100`，導致 `XLAT CS:[BX+AL]` 每次都從 palette table 晚兩個 bytes 開始讀，遠處縮小物件的少量色碼因而被映射成亮藍／紅色雜點。物品欄使用的 cursor remap table 同樣錯位。

原始碼修正位於 `bak/INCLUDE/gfx169d.h`：移除版本別的 magic constants，改用 `FP_OFF(&g_abFogRemapTable[0])` 與 `FP_OFF(&g_abCursorPaletteLut[0])`，讓 linker far-symbol fixup 提供該次 link 真正的 near offset。原版 byte-identical layout 下仍會解析成原本常數；resident code 改變後也會自動跟著正確位址。

實機驗證採同一份存檔、同一視角：未修時右側小樹有穩定藍色雜點；在每次縮放呼叫入口把 `0x005c/0x015c` 即時改成 `0x005a/0x015a` 後重新繪製，雜點完全消失。對照截圖為 `scratchpad/remap-before.png` 與 `scratchpad/remap-after-hotpatch.png`。

本次 Windows session 的 WSL2/KVM 功能不可用，且 host 沒有 QEMU/Docker，因此尚未用 Borland 工具鏈產生正式新 EXE。下一步只需在既有 `~/krondor-build` 可用的環境執行標準流程：pull 原始碼、`uv run bak build`、複製 `work/KRONDOR.EXE` 到 `dist/test_v100_zh/`，再用同一存檔做一次冷啟動對照。不要再調整 `EMSIMG.C` 的 `< 300` 作為這個雜點問題的修法。

### 9.8 2026-08-23：WSL2 正式重建、部署與冷啟動驗收通過

使用者完成 Windows BIOS 虛擬化與 WSL2 安裝後，已在全新的 Ubuntu 26.04 LTS 環境重建 §9.7 的正式修正版。環境檢查結果如下：

- WSL distribution：`Ubuntu`，WSL version `2`。
- Linux kernel：`6.18.33.2-microsoft-standard-WSL2`。
- 使用者：`pmanyeh`，已加入 `kvm` 群組，且對 `/dev/kvm` 具備實際讀寫權限。
- QEMU：`qemu-system-i386 10.2.1 (Debian 1:10.2.1+ds-1ubuntu3.2)`。
- mtools：`4.0.49`。
- uv：`0.12.5`。

建置全程在 WSL 原生 ext4 目錄 `/home/pmanyeh/krondor-build` 執行，沒有在 `/mnt/d` 上執行 `uv sync`／`uv run`。Borland／FreeDOS 工具鏈解壓至 `/home/pmanyeh/bak-toolchain`；來源為上游 `toolchain-v1` release，下載後已驗證完整 SHA-256：

```text
99c83ad04f77c503b3795127645810f7977e647514e91a03da2c697d93dc8dfb
```

正式建置命令：

```bash
cd /home/pmanyeh/krondor-build
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain ~/.local/bin/uv run bak build
```

這是首次建置，因此走完整 clean build，並由 QEMU 分別使用 KVM／TCG 完成 Borland C++ 3.1、TASM 與 BC++ 2.0/3.0 的編譯及連結。建置驗證結果：

- `VMCODE.OVL`：**BYTE-IDENTICAL**，44,582 bytes，SHA-256 `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0`。
- `SX.OVL`：**BYTE-IDENTICAL**，40,742 bytes，SHA-256 `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb`。
- `KRONDOR.EXE`：456,112 bytes，SHA-256 `aa819f9a1be34c5de86999daf6894e4caa8ac9f37dd3af27e175f844fa2cd31d`。它與原版大小不同是中文引擎修改及本次修正的預期結果；兩個未修改 OVL 的 byte-identical 結果證明工具鏈與整條建置管線正確。

新產生的 `KRONDOR.MAP` 再次確認同一 CS segment 內的實際符號位置：

```text
070E:005A  _G_ABFOGREMAPTABLE
070E:0A5A  _G_ABCURSORPALETTELUT
070E:1322  _POLYRAST_SPR_SCALED_BLIT_PLANAR
```

這與 §9.7 的根因完全吻合：中文版正確 offset 是 `0x005a/0x0a5a`，不是原先硬編碼的 `0x005c/0x0a5c`。`gfx169d.h` 改用 `FP_OFF(...)` 後，由 linker fixup 自動填入本次 link 的正確值。

正式產物已部署至 `dist/test_v100_zh/krondor.exe`。部署前的舊版沒有覆蓋後丟失，而是備份為：

```text
dist/test_v100_zh/krondor.pre-remap-fix-5e924bda.exe
SHA-256 5e924bda558d1faab7eda8c8b8cabe9bc7191afae6e82388c445f8661b56734d
```

最後以 DOSBox-X 2026.06.02 **完整冷啟動**修正版，載入既有存檔並檢查物品欄貼圖。使用者於 2026-08-23 目視確認：原先會出現的藍色／紅色雜點已消失，物品圖示顯示正常，回報「正常了」。因此 §9.5 的物件縮放雜色問題已完成「根因定位 → 原始碼修正 → 正式重建 → 部署 → 冷啟動實機驗收」全流程，可正式標記為 **RESOLVED**。

後續注意事項：不要再以調整 `EMSIMG.C` 的 `page_id < 300` 作為此問題的修法；該假說已由 live debugger 數據推翻。真正且已驗證的修正是 `bak/INCLUDE/gfx169d.h` 中以 linker-resolved `FP_OFF(...)` 取代 palette remap table 的版本別 magic offsets。

## 10. 2026-08-23：撿屍／物件說明停住（RESOLVED）

### 10.1 症狀與重現

使用 `dist/test_v100_zh/GAMES/SAVES.G01/SAVE00.GAM` 可穩定重現：戰鬥後第一次點擊屍體會顯示描述，第二次點擊原應進入物品界面，但遊戲停在描述且不再接受輸入。另一路徑是在物品界面對物件按右鍵開啟物件說明，同樣會停住。換回原始英文 `DIAL_Z00.DDX` 後，撿屍流程可進入物品界面，但只要之後觸發中文版物件說明仍會停住，因此排除 DDX 結構、特定屍體 record 與 actor 資料本身。

### 10.2 Live debugger 證據與根因

當表面症狀發生時，CPU 最後會執行到 `CS:IP = 0000:0000`。堆疊證明上一層是 `INT 21h` 返回點，而 IVT 中 INT 21h 的四個向量 bytes 已被清成零。對實體位址 `0000:0084`～`0000:0087` 設寫入監看點後，精準抓到：

```text
CS:IP = 0824:4819   repe movsw (_fmemcpy / res_fread_far)
ES:DI = 0008:0008
來源 = ZHSTAT.DAT 的 128-byte 讀取區塊
目的 = alloc_far() 回傳的 0008:0000
呼叫者 = font_init_chinese_small()
```

`ZHSTAT.DAT` 為 40,204 bytes（1,827 glyphs，每筆 22 bytes）。進入中文小字型說明時，低於 640 KB 的傳統記憶體已不足；配置路徑出現 DOS error 8，重建的 `alloc_far()` 路徑卻把 `AX=0008` 接受成有效 segment，導致 `res_fread_far()` 從實體位址 `0x80` 開始覆寫 IVT。這解釋了「描述仍留在畫面、任何輸入都無效」：INT 21h 向量已遭破壞，並非遊戲輸入迴圈真的卡死。

### 10.3 正式修正

- `bak/SRC/GFX/FONT/FONT.C`
  - 補上 `SRC/IO/RESFAR.H` 的正式 prototype。
  - `ZHSTAT.DAT` 小字型優先配置於 EMS，依 16 KB 分頁載入，不再永久占用約 40 KB conventional memory。
  - 40,194-byte glyph payload 可完整映射在四個連續 EMS page-frame slots 中，因此 22-byte record 即使跨邏輯頁面也可直接搜尋。
  - 無 EMS 時仍保留原 conventional-memory fallback。

排查途中曾嘗試修改 `DOSMEM.C` 與 EMS 欄位語意，但 live debugger 後續證明原重建程式的 EMS 全域欄位名稱雖具誤導性，執行期語意仍能工作；這些實驗性邏輯均已撤回。現在正式修正只在既有 `FONT.C` 指標中以 `0000:chain` 記錄小字型 EMS chain，避免增加 DGROUP/BSS 全域欄位並改變舊程式記憶體布局。工作樹中的 `DOSMEM.C`／`EMSDET.C` 若仍顯示 diff，是換行格式差異，不代表部署了上述實驗修法。

### 10.4 建置與驗收

WSL2/KVM 增量建置成功；`VMCODE.OVL` 與 `SX.OVL` 均維持 byte-identical。正式部署產物：

```text
dist/test_v100_zh/krondor.exe
size    456,480 bytes
SHA-256 b98ff9a194c5bfaa6f120b140a979aff6a2cb8964c0a1673d77de73afb8ec7a0

dist/test_v100_zh/ZHSTAT.DAT
size    40,204 bytes
SHA-256 a28b74ad5a03bc9baef907b414e2c4983363f7ec986d35913a400a70a1f93d7c
```

使用者以相同存檔完成以下人工驗收：

1. 第一次點擊屍體：正常顯示描述。
2. 第二次點擊屍體：正常進入物品界面。
3. 在物品上按右鍵：正常開啟物件說明。

驗收後暫停 CPU 並讀取 IVT，`0000:0084`～`0000:0087` 仍為 `00 D1 00 F0`，即有效的 `F000:D100` INT 21h 向量，且全程未觸發 IVT 寫入監看點。此問題已完成「交叉排除 → 精準寫入監看 → 根因定位 → 原始碼修正 → 重建部署 → 兩條路徑實機驗收」，正式標記為 **RESOLVED**。

## 11. 2026-08-23：戰鬥後能力提升訊息空白死機（RESOLVED）

### 11.1 症狀與關鍵對照

使用同一份 `SAVE00.GAM` 完成戰鬥後，能力提升通知可能只顯示第一段文字；再次點擊時訊息框變空白，滑鼠與鍵盤均無法使流程繼續。曾將 `DIAL_Z21.DDX` 暫時換成原始英文版做 A/B：第一頁可顯示 `Locklear's 近戰命中`，按下後仍進入空白死機。這排除了中文翻譯 body、`@1` 替換與 DDX 結構本身是唯一根因。

Debugger 在空白畫面抓到的 CPU 位於原版 VGA vertical-retrace wait，但這只是 `screen_frame_present()` 正準備呈現空白頁時停留的位置。嘗試替 retrace wait 加 timeout 會造成戰鬥畫面嚴重閃爍，並非正確修法，相關 VMCODE 實驗已全部撤回；目前 `VMCODE.OVL` 仍與原版 byte-identical。

### 11.2 真正根因：兩行／單行頁面的零進度分頁

當下記憶體中的 record 仍是 node `2100018`（`@'s @1 ability has increased.`），證明使用者看到的不是「下一筆訊息」，而是同一筆訊息換頁。`TEXTWRAP.C:textwrap_draw_aligned()` 原有防孤行規則：若只剩一行，就再把一行移到下一頁。當「總共剩 2 行、版位每頁只能畫 1 行」時，它把 remaining 由 1 加成 2，造成：

```text
g_wTextWrapLinesDrawn = (2 - 2) - 0 = 0
```

`DIALOG.C` 隨後以 `scroll_start += g_wTextWrapLinesDrawn` 前進，因此永遠加 0：每輪都繪製空白頁、每輪都停在相同 acknowledge/present 流程，看起來就像遊戲死機。

正式修正位於 `bak/SRC/UI/TEXTWRAP.C`：只有在增加 remaining 後，本頁仍至少有一行可畫時才套用防孤行規則，即 `remaining == 1 && (count - first_line) > 2`。這保證分頁每一輪都有正進度。

### 11.3 緊湊通知框的小字版面

能力提升 record 使用 `flags=0x0014`、矩形 `(70,40,180,35)`；扣除樣式內距後可用高度只有 28px，放不下兩行 16×16 中文（含 1px 行距需 33px）。因此 `DIALOG.C` 對這個精確版位啟用既有 `g_bSmallZhMode`，改用 10×10 中文字，讓完整通知可在同一框顯示。

另在 `FONT.C` 修正小字混排：`g_bSmallZhMode` 下的 ASCII（包含動態代入的角色姓名）改走遊戲原本的小型英文字型，字寬與 glyph metrics 也使用同一路徑，不再出現姓名仍為 8×16、中文已縮成 10×10 的比例不一致。全隊通知不含姓名；此輪實測只直接覆蓋全隊版本，單人姓名分支已編入同一版，之後遇到單人升級事件時可再做視覺回歸確認。

### 11.4 最終部署與實機驗收

本機 upstream 原始碼 commit：`4da895b`（`fix: stabilize Chinese rendering and dialog pagination`）。依本專案慣例，此 commit 保存在 `upstream/betrayal-at-krondor` 的本機歷史，不推送至原作者的 GitHub repository。

```text
dist/test_v100_zh/krondor.exe
size    456,480 bytes
SHA-256 b98ff9a194c5bfaa6f120b140a979aff6a2cb8964c0a1673d77de73afb8ec7a0

dist/test_v100_zh/DIAL_Z21.DDX
size    7,926 bytes
SHA-256 d9492290e9cc8b293e7bc0f3a256b9ed1927356ab5ed6246c38276e825bee367

dist/test_v100_zh/VMCODE.OVL
size    44,582 bytes
SHA-256 cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0

dist/test_v100_zh/SX.OVL
size    40,742 bytes
SHA-256 d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb
```

使用者重新完成戰鬥後確認：全隊升級訊息「隊伍的各項能力都提升了。」以小字完整顯示於同一訊息框，標點正常，連續操作不再空白或死機，回報「沒當機了」。主問題正式標記為 **RESOLVED**。

## 12. 2026-08-23：翻譯 session——DIAL_Z06／DIAL_Z21／DIAL_Z14（157 筆）+ 新增 DOSBox-X MCP 除錯工具設定

延續 §9 之後的新一輪對話 session，過程中跟 §10／§11 那次除錯 session 交錯進行（見下方 §12.4 的因果關係）。

### 12.1 新翻完的三個章節檔

- **`DIAL_Z06`（61 筆）**：薩薩戈斯的「恐懼之石」墓園——戈拉斯／歐文自己的假墓碑（唱名各種聳動的死法，用來威嚇即將處決的莫瑞德死囚）、其餘幾名真正被囚禁的莫瑞德氏族囚犯（貝爾多加／戈爾班德克／尤爾文德／波貝爾四個新氏族名）、一批無關的通用陣亡將士墓誌銘（人類名字，提到「守護者」「阿曼加之戰」，經查證跟這個地點沒有敘事關聯，是跟 §5.0／§9.1 一樣的通用墓誌銘素材池）。後段接著戈拉斯帶隊繞開哈勒克鎮、盤算怎麼假裝把歐文賣給奴隸販子維努特里爾以救出被囚禁的莫瑞德人奧布卡。
- **`DIAL_Z21`（42 筆）**：兩塊內容——(a) 隊伍能力提升的系統通知（`The party's @1 ability has increased.` 這類，共 4 筆，**這幾筆正是 §11 那個分頁死機 bug 的第一批觸發內容**，見 §12.4）；(b) 城鎮裡四款虛構賭博小遊戲的完整對局文字（骰子、林嵐牌、帕夏瓦牌、波基爾牌〔`óPokiir`，凱許狗兵玩意兒〕、西洋棋），大量模板化的贏/輸/平手/告辭台詞跨遊戲類型重複使用，翻譯時建立固定句式、逐一比對哪幾筆該共用同一份中文、哪幾筆看似相同其實有語意差異（例如「roll the dice」跟「deal out the cards」在同一句式模板裡是不同動詞，不能照搬）。
- **`DIAL_Z14`（53 筆，本次份量最大也最複雜）**：前段是自成一體的小插曲——巫婆庫利奇的空屋、瀑布、龍形石像（`#9` 是一整段刻意寫成古英文拼法的石碑銘文，遊戲原始資料用 42 個逐字獨立的 `0xF4` 樣式位元組標記幾乎每一個英文字，翻譯時沒有逐字對應，而是寫一套程式化的分段函式把中文句子切成 42 份、依序各自掛上一個 `0xF4`，結構驗證正確且維持了可讀性）、抵達艾爾凡達。後段是一大段酒館分支劇情：跟形形色色的酒客搭話（傭兵聊疤痕/矮人礦坑怪物/長矛比武賣『法達莫爾秘方』的辛酸事、女人賣貝殼/聊禁書/控訴貴族拿孩子換利益、假奸細裝出的假奎格語打鬥戲碼——這幾句刻意保留原文不翻譯，因為它們在遊戲設計上本來就是玩家聽不懂的異國語言，翻成別種亂碼反而失真），最後收束到詹姆士主線：向酒館裡的傭兵打探「爬行者的鑰匙」下落，得知「正直人」已死、嘲弄幫（克朗多盜賊公會，`the Upright Man` 手下的組織）陷入混亂；接著戈拉斯把風、詹姆士潛入一間屋子用嘲弄幫的老手法（門框夾層裡的暗鑰）開鎖，在唐迪爾花罐裡找到藏起來的粉末袋。

三個檔案全部先用 `ddx_translate.py scaffold` 對照 `scratchpad/pristine/` 裡的乾淨原始 DDX 確認零 source drift，翻完後逐筆用 `extract_tokens()` 驗證 token 結構一致（含大量 `\xf1`／`\xf3`／`\xf4` 樣式位元組、`@N` 角色代稱、逐段落 `\t`/`\n`），全部 0 mismatch 才寫入。

### 12.2 詞彙表新增 34 筆（174 → 208）

分三批：Thorgath（戈拉斯化名「索爾加斯」）／Lin-Lan／Pashawa／Pokiir 四款虛構遊戲名；接著薩薩戈斯周邊的 Harlech／Caern／Wyke／Raglam 四個地名、the Protector（守護者頭銜）、Guy du Bas-Tyra（燒毀阿曼加的歷史人物）、Obkhar／Irmelyn／Venutrier 三個劇情人物、四個莫瑞德氏族名；最後 DIAL_Z14 的 Mockers（嘲弄幫）／the Crawler（爬行者）／Black Slayers（黑衣殺手）／Kasumi／Gabot／Silden／tondill／Lyton／Max Feeber／Kivo／Brock Noor／Cullich／Rhandra／Delong the Great／Malac the Pious／Anita／Quegian，共 17 筆。既有詞條（Ruthia、moredhel、Nighthawks、Guild of Assassins、Fadamor's Formula、七鰓鰻、悲愴使者……）在這批翻譯裡全部先查表後使用，沒有再犯 §9.3 那種「憑印象翻出跟既有譯名不一致版本」的錯。

### 12.3 打包流程（三輪 append-only 字庫重建，全部驗證 0 舊字元變動）

跟 §8.1 建立的規則一致：每次翻完一批，先跑 `build_font.py --from-translations`（預設 append-only，讀取既有 `--output-map` 當基準），重建前後逐一比對 `char_to_id`，確認舊字元 0 筆變動，才繼續。三輪分別是 `DIAL_Z06`＋`DIAL_Z21`（+15 相異字元）、`DIAL_Z14` 前段（+22）、`DIAL_Z14` 後段（+84），字庫從 2522 字長到 **2643 字**（4398 個 ID 槽位）。每輪都接著跑 `ddx_translate.py`／`ddx_rebuild_all.py` 全量重建 32 個 DDX 檔（0 fallback、0 token-mismatch、0 source-drift），部署到 `dist/test_v100_zh/` 前，`ZH16.DAT` 一律先備份成帶舊 SHA256 前綴的檔名再覆蓋（例如 `ZH16.pre-z14p2-1ca8d552.DAT`），沒有任何一次是直接覆蓋不留退路。**這個 session 全程沒有本機 WSL2 環境可以重編 `KRONDOR.EXE`**，所以只做了字庫／DDX 這類純 Python 端可以處理的部分，沒有牽動任何 C 原始碼或 `.exe`／`.ovl`。

`TEST.json` 的 1 筆翻譯**沒有**跟著打包——`bak rmf list` 裡確實有 `TEST.DDX`，但這次 session 手上的 `scratchpad/pristine/` 快照沒有包含它（推測是先前擷取時漏抓），`ddx_rebuild_all.py` 的 glob 也只認 `DIAL_*.json`、本來就不會處理它。下次要打包這 1 筆時，先用 `bak rmf extract` 補一份乾淨的 `TEST.DDX` 進 `scratchpad/pristine/`，再手動跑一次 `ddx_translate.py build`（不需要動 `ddx_rebuild_all.py` 的邏輯）。

### 12.4 重要教訓：這次翻譯直接觸發了 §11 那個分頁死機 bug

`DIAL_Z21` 最前面 4 筆是全遊戲共用的「隊伍能力提升」系統通知（`The party's @1 ability has increased.` 等），內容極短、乍看完全不像會踩雷的那種長篇文字。但把它們翻成中文、部署後，使用者實機戰鬥完就卡在空白訊息框動彈不得——根因追出來是 `TEXTWRAP.C` 的防孤行規則在「剩 2 行、每頁只能畫 1 行」這個特定情境下把分頁進度算成 0，每一輪都重畫同一張空白頁（詳細技術根因、修法、驗收見 §11，是另一個對話 session 用 DOSBox-X AI Debugger MCP 工具即時除錯抓出來的，這次 session 本身沒有除錯工具）。

**教訓**：判斷一段文字會不會踩到版位/分頁類的 bug，不能只看「這段話長不長」，中文跟英文的斷行方式、字元寬度、`@1` 代入的技能名稱長度都會讓同一句話在不同語言版本裡佔用的行數不同——哪怕原文一行就放得下，中文版換算下來可能就是「剛好多出一行」這種最容易踩到分頁邊界 bug 的情況。這類系統通知/彈出框類的短文字，之後如果又出現顯示異常，優先懷疑分頁／行數計算，而不是先去查編碼或字庫。

### 12.5 新增：`.mcp.json` 專案層級 DOSBox-X AI Debugger 設定

這次 session 使用者回報物品介面卡死時，發現目前的 Claude Code 環境沒有接上 `D:\git\DOSBox-X-AI` 提供的 DOSBox-X AI Debugger MCP 工具（`ai/server.py`，`.venv` 早已裝好，只是沒有註冊進這個 VSCode 側邊欄的 Claude Code session）。已在專案根目錄新增 `.mcp.json`：

```json
{
  "mcpServers": {
    "dosbox-x-debugger": {
      "command": "D:\\git\\DOSBox-X-AI\\.venv\\Scripts\\python.exe",
      "args": ["D:\\git\\DOSBox-X-AI\\ai\\server.py"]
    }
  }
}
```

**這個檔案目前是未 commit 的專案層級設定**（第一次載入時 VSCode 通常會跳出信任確認）。加上這個設定、重新開一個新對話後，使用者接上了 MCP 工具、另開一個 session 用即時除錯查出並修好了 §10／§11 兩個 bug（見上方對應章節，過程用到 `pause_execution`／記憶體寫入監看點等真斷點手法，不是這份文件裡舊的「CS 落在 VGA retrace 迴圈、沒有鑑別度」那種土法煉鋼）。**下一個 session 如果又要做即時除錯，直接確認 `.mcp.json` 還在、對話有沒有接上 `dosbox-x-debugger` 這個工具群組即可，不用重新設定。**

### 12.6 下一步建議

1. **繼續翻譯**：剩餘約 4,541 筆分散在 `DIAL_Z13`／`Z15`／`Z17`／`Z19`／`Z20`／`Z22`／`Z23`／`Z27`／`Z30`／`Z31` 這幾個大檔（`Z20` 867 筆、`Z30` 2208 筆是目前最大的兩個），scaffold 都已建好。
2. **補齊 `TEST.json` 的打包**：見 §12.1，只差一份乾淨的 `TEST.DDX`。
3. **翻譯品質校對**：這次新翻的 `DIAL_Z06`／`DIAL_Z21`／`DIAL_Z14` 157 筆都還沒有第二人核對過，`DIAL_Z14` 的詹姆士查案段落是重要支線劇情，建議找機會抽查；§12.1 提到的古老銘文（`DIAL_Z14#9`）跟假奎格語打鬥戲（`DIAL_Z14#44`）是這批裡最容易在實機上看出排版異常的內容，實機測試時可以優先看這兩筆。

## 13. 2026-08-23：翻譯 session——DIAL_Z13（128 筆，商店／旅店／神殿系統）

延續 §12 之後的新一輪對話 session，使用者僅要求「繼續翻譯」，沒有提供新的除錯線索或需求。

### 13.1 新翻完的章節：DIAL_Z13（128 筆全遊戲共用的商店／旅店／神殿系統文字）

跟 `DIAL_Z00`／`DIAL_Z18` 一樣，這不是特定章節劇情，而是玩家在任何城鎮都會用到的通用場景文字，可分四塊：

- **商店進場敘述**（#0～#21，22 筆）：當舖、雜貨店、武器店、藥草店等，大量重複樣板句式（例如「這間雜貨店的擺設令人感到熟悉又自在……」在 7 間不同店名下重複出現），翻譯時歸納成共用範本函式，確保同一句式在不同店名下譯文完全一致。
- **旅店／夜間值夜掌櫃互動**（#22～#60，約 35 筆）：旅店進場敘述（6 種樣板房型敘述）+ 一整組「值夜掌櫃」對話樹（登記入住、隔天退房抱怨、Delekhan 送錢的伏筆訊息、賒帳被趕出門等）+ 3 筆治療介面 UI 提示。
- **神殿治療／附魔／祝福系統**（#61～#97，約 30 筆）：12 座神殿（基利安、伊夏、席爾班、頌恩、林絲克拉格瑪、露西亞、巴納斯、卡胡利、達拉、提斯、圭斯瓦——含 2 座新神，見下方詞彙表）的冥想室共用樣板文字、治療祭司對話、武器／甲冑附魔祝福流程。
- **神殿傳送（曼陀羅）系統與大祭司支線劇情**（#99～#159，約 40 筆，本批最長最複雜的部分）：傳送機制的完整說明對話；接著是好幾條獨立的大祭司支線——基利安神殿「收集者」褻瀆祭典懸案（貝蘭德拉、戴文）、頌恩神殿凱蘭祭司的「夢境傳訊」失眠懸案（與莫瑞德法師納戈交手的兩種對話分支）、林絲克拉格瑪神殿的黑衣殺手／夜鷹會神學背景說明、卡胡利神殿詹姆士追查夜鷹會首領納馮．杜桑多的長篇多輪劇情（護法身分、誦經長老、主教）、達拉神殿麗莎大祭司的穀糧懸賞與祝福儀式、提斯神殿教長的凱許戰局評論、阿斯塔隆神殿新任誦經長老法蘭西斯神父（接替病故的提摩西神父）、以及馬拉克十字鎮修道院院長葛瑞夫斯與薩斯修道院約翰神父兩段藏書／學者支線的鋪陳。

翻譯時遇到的樣式控制位元組結構跟先前章節相似（`\xf1`／`\xf3` 逐詞觸發、無需配對關閉），沒有出現新的排版特例。比較特別的是 #124/#126 兩筆幾乎整段重複的祭司對話（玩家是否已經打倒納戈的兩種分支），刻意保持兩者共用段落的譯文完全一致，只有分歧點（是否已知道兇手身分）不同，方便之後比對維護。

### 13.2 詞彙表新增 22 筆（208 → 230）

新增兩位先前從未出現過的神明：Silban（席爾班神）、Astalon（阿斯塔隆神，克朗多王宮內設有神殿，詹姆士曾在此跟隨已故的提摩西神父學習）。新增多個支線 NPC：凱蘭、瑪莉亞、貝拉大祭司、貝蘭德拉、麗莎大祭司、瓦邦、弗蘭德爾．哈夫蓋特、蒂雅、戴文、「收集者」（頭銜，仿照「正直人」的處理方式保留引號）、提摩西神父、法蘭西斯神父、約翰神父、安東尼修士、哈斯坦。另外新增幾個神明的稱號／別名（不是新角色，是既有神明的另一種稱呼，供以後遇到同一稱號時查表沿用）：圭斯瓦的「紅顎獵神」、卡胡利的「逃亡者的怒吼者」／「不倦追獵者」、林絲克拉格瑪的「收網者」、基利安的「大地之母」。翻譯過程中全程先查表沿用既有譯名（基利安、伊夏、頌恩、林絲克拉格瑪、露西亞、巴納斯、卡胡利、達拉、提斯、圭斯瓦、夜鷹會、刺客公會、黑衣殺手、納馮．杜桑多、里蘭儂、肯廷拉什等），沒有再犯 §9.3 那種印象翻譯不一致的錯。

### 13.3 打包與驗證（append-only 字庫重建，32 個 DDX 全量重建 0 fallback）

流程與 §12.3 完全一致：

```
python tools/font/build_font.py --from-translations localization/translated \
  --output-font localization/generated/ZH16.DAT --output-map localization/generated/zh_mapping.json
```

字庫從 2643 相異字元（4398 槽位）長到 **2762 相異字元（4647 槽位）**，append-only 驗證（逐一比對舊 `char_to_id` 的全部 2643 筆）**0 筆變動**。接著跑 `ddx_rebuild_all.py`（以 `scratchpad/pristine/` 的乾淨原始 DDX 為基準，32 個 DDX 全量重建 + 結構驗證）：

```
python tools/text/ddx_rebuild_all.py --source-dir scratchpad/pristine \
  --translations-dir localization/translated --output-dir scratchpad/rebuilt_ddx \
  --mapping localization/generated/zh_mapping.json --manifest scratchpad/rebuild_manifest.json
```

結果：32 個 DDX 全部重建成功，共套用 1518 筆翻譯（1390 筆先前累積 + 這次新增 128 筆）；manifest 顯示 `DIAL_Z13.DDX` 的 128 筆 **`skipped_token_mismatch: 0`、`skipped_source_drift: 0`、`skipped_untranslated: 0`**，結構層面完全正確。`pytest tests/unit`（54 個測試）全過。

部署到 `dist/test_v100_zh/`：`ZH16.DAT` 先備份成 `ZH16.pre-z13-cac3fa8a.DAT`（帶舊 SHA256 前綴）才覆蓋，`DIAL_Z13.DDX` 直接複製（該檔案先前是純 scaffold、還沒部署過，沒有舊版可比對）。**這次 session 沒有進行實機測試**——連上 DOSBox-X AI Debugger MCP 後發現遊戲畫面正停在使用者自己的一場戰鬥對話中（跟 `DIAL_Z13` 無關），為了不干擾使用者當下的遊玩進度／存檔狀態，沒有送出任何按鍵去導航測試商店／旅店／神殿場景。**下一個 session 開始前，務必先請使用者（或在確認不會干擾其現有進度的情況下）實機走一趟至少一間商店、一間旅店、一座神殿，確認 `DIAL_Z13` 的中文顯示與排版正常**，尤其是 #66/#136/#140/#152 這幾筆多輪對話、樣式位元組較密的長篇劇情，是這批裡最容易在實機上看出排版異常的內容。

### 13.4 下一步建議

1. **實機驗收 `DIAL_Z13`**（見 §13.3 結尾）——這是本次 session 唯一還沒完成的步驟。
2. **繼續翻譯**：剩餘約 4,414 筆分散在 `DIAL_Z15`／`Z17`／`Z19`／`Z20`／`Z22`／`Z23`／`Z27`／`Z30`／`Z31`，`Z20`（867 筆）、`Z30`（2208 筆）是目前最大的兩個，scaffold 都已建好。
3. **補齊 `TEST.json` 的打包**：見 §12.1／§12.6，只差一份乾淨的 `TEST.DDX`，這次 session 沒有處理。
4. **翻譯品質校對**：`DIAL_Z13` 128 筆還沒有第二人核對過，尤其卡胡利神殿詹姆士查案那幾筆（#136/#139/#140/#142）是較長的多輪劇情，建議找機會抽查。

## 14. 2026-08-23：翻譯 session（延續）——DIAL_Z27（95 筆）＋ DIAL_Z22（96 筆），改採「小檔案優先」排序

延續 §13 之後同一天的新一輪對話。使用者確認：（1）§13.3 提到的實機驗收之後有看到（可能是暫時性的）「右鍵物品說明失效」異狀，重新測試幾次後恢復正常，暫時視為已解決但仍待觀察，下一個 session 如果又碰到同樣症狀，優先懷疑跟本節新增的字庫成長／DDX 部署有沒有關聯；（2）後續翻譯章節請按「筆數由少到多」排序，大檔案（`Z20` 867 筆、`Z30` 2208 筆）留到最後——**這是使用者明確表達的標準排序原則，之後每次挑新章節翻都要照這個順序**，不用每次重新問。

### 14.1 新翻完的兩個章節

- **`DIAL_Z27`（95 筆）**：北方山區地形選擇的樣板敘事（山口、路口、洞穴/樓梯導覽），內容跟 `DIAL_Z00`／`DIAL_Z24` 一樣是全遊戲共用的路徑選擇旁白，大量重複樣板句式（「幾天過去了……」「@4 的雙腿痠痛不已……」等），翻譯時歸納成共用範本函式。夾雜幾筆非樣板的劇情:詹姆士／洛克利爾北衛城前的老友追憶、帕格在提米里安亞遺跡的回憶片段、戈拉斯／歐文地牢逃脫前的對話。詞彙表新增 8 筆（Finn、High Wold、Thunderhell Steppes、Cutter's Gap、Naddur、Bronwynn、Captain Moyiet、Corvalis）。
- **`DIAL_Z22`（96 筆）**：高堡（Highcastle）周邊支線劇情合集，是這次 session 內容最豐富的一個檔案，涵蓋好幾條獨立支線：波斯維奇夫人集結地的賄賂／唬弄守衛橋段、莫瑞德語守橋密碼（「屠蛇者」）、詹姆士一行人跟哥布林傭兵首領古拉的過路費／換約談判、奧布卡救援行動的那夫沙油洞穴泅泳橋段（呼應 `DIAL_Z06`）、化裝成奎格傭兵滲透莫瑞德酒館刺探北衛城攻勢情報、放款人伊蘇納圖斯（沿用 `DIAL_Z18` 已建立角色）核對帳冊、科瓦利斯伯爵宅邸／烏格妮尋人（沿用 `DIAL_Z03`／`DIAL_Z20` 已建立角色）、特羅維爾／凱文兩位男爵的軍情交流與哥布林密信獎賞、失蹤吟遊詩人調查（帶出勞瑞後來成為薩拉多公爵的背景八卦）、以及拉格蘭姆投石機破壞任務（找零件、修復、瞄準莫瑞德小鎮）。詞彙表新增 23 筆。

**⚠️ 特別記錄一筆逐字元樣式的技術難題已解出（DIAL_Z22#51）**：一張貼在「燭匠的笑臉」酒館門上的手寫公告字條，原文用 `ã` 逐字元包裹每一個英文字母（包含空白），這種排版之前 §5.0 的 `restyle()` 土法只處理過小規模案例，這次首度遇到大段落（90 個英文字元）。實測確認了兩條新規則：(1) 每個「真實字元」前面都要有一個對應的樣式位元組，且該樣式片段結尾處，只要後面接的是 `
`（換行）就要再補一個「收尾用」的樣式位元組（不對應任何真實字元）；(2) 但如果樣式片段後面直接接的是 ` `（記錄結尾），則**不需要**收尾位元組，字元數等於樣式位元組數,1 對 1。這次為了湊滿原文 90 個英文字元對應的字數,中文譯文刻意寫成较長的正式公告語氣（"因近日酒水存量嚴重短缺……"），不是隨便湊字數,是真的把公告內容用更詳盡的中文官方公告語氣展開,讀起來自然不生硬。**這個規則以後遇到類似逐字元樣式的整段文字（例如书信、告示、刻字）都適用,建議之後正式收進 `ddx_translate.py` 或至少寫進工具文件,不要每次都重新在 scratchpad 里推導。**

### 14.2 詞彙表新增與一致性註記

`glossary.json` 這兩個檔案共新增 31 筆，總數來到 **261 筆**。特別記一筆既有的翻譯不一致但這次刻意沿用舊版、沒有回頭修正：`Baron Gabot` 在 `DIAL_Z00`（§8）建立時譯作「加博特男爵」，但 `DIAL_Z14`（§12）另一筆再次出現時誤譯成「加波特男爵」，這次 `DIAL_Z22` 的哥布林談判橋段也提到同一位男爵，**採用了最早建立的「加博特男爵」**，`DIAL_Z14` 那筆舊的不一致沒有動。下次翻譯校對時可以順手把 `DIAL_Z14` 那筆改掉統一。

另外這次識別出一個容易混淆的「同名不同群體」陷阱：`DIAL_Z22` 裡莫瑞德陣營的「The Six」（一個位於北境邊境、由莫萊伍夫授權過橋的指揮議會）跟先前 `DIAL_Z00`／`DIAL_Z29` 已建立的「The Six」（賽瑟儂生命石洞穴的圖蘭尼六賢者）雖然原文拼法完全一樣，但顯然是兩個不相干的組織。已刻意分開翻譯（六人議會 vs. 六賢者），避免玩家看了誤以為是同一批人。

### 14.3 打包驗證與部署狀態

兩個檔案都各自跑過完整流程（`build_font.py --from-translations` append-only 重建、`ddx_rebuild_all.py` 32 檔全量重建、`pytest tests/unit`），過程與結果：

- `DIAL_Z27`：字庫 2643→2778（+16 相異字元），0 skipped_token_mismatch / 0 skipped_source_drift，已部署到 `dist/test_v100_zh/`（`ZH16.DAT` 備份為 `ZH16.pre-z27-<sha>.DAT`）。
- `DIAL_Z22`：字庫 2778→2834（+56 相異字元），append-only 驗證 0 筆舊字元變動，0 skipped_token_mismatch / 0 skipped_source_drift，**打包產物停留在 `scratchpad/rebuilt_ddx/DIAL_Z22.DDX` 跟 `localization/generated/ZH16.DAT`，尚未複製進 `dist/test_v100_zh/`**——使用者要求先確認 §13.3 那次「右鍵物品說明失效」的異狀不會再犯，才要繼續部署新內容，避免變動疊在一起難以排查。**下一個 session（或這次 session 使用者確認 OK 之後）記得比照 §13.3／本節的模式,把 `ZH16.DAT` 備份後覆蓋、複製 `DIAL_Z22.DDX`,再請使用者實機驗收。**

累計已翻譯並「完整跑過驗證流程」的章節：`DIAL_Z00`／`Z01`／`Z02`／`Z03`／`Z04`／`Z05`／`Z06`／`Z07`／`Z08`／`Z10`／`Z11`／`Z12`／`Z13`／`Z14`／`Z16`／`Z18`／`Z21`／`Z22`／`Z24`／`Z27`／`Z29`（21 個檔案，共 1709 筆對話），其中 `Z22` 尚未部署到測試資料夾。全遊戲 DDX＋TEST 對話總量 5,932 筆，剩餘待翻約 4,222 筆，分散在 `DIAL_Z15`（159）／`Z17`（152）／`Z19`（362）／`Z20`（867）／`Z23`（100）／`Z30`（2208）／`Z31`（374），依筆數排序，`Z23`（100 筆）是下一個最小的候選。

### 14.4 下一步建議

1. **確認 `DIAL_Z13`／`DIAL_Z27` 實機穩定後,部署 `DIAL_Z22`**（見 §14.3）。
2. **繼續翻譯（小檔案優先）**：`DIAL_Z23`（100）→ `Z17`（152）→ `Z15`（159）→ `Z19`（362）→ `Z31`（374）→ `Z20`（867）→ `Z30`（2208）。
3. **翻譯品質校對**：`DIAL_Z27`／`DIAL_Z22` 都還沒有第二人核對過；`DIAL_Z22` 內容特別龐雜,建議找機會抽查幾條支線（尤其是 #51 那則逐字元樣式的公告字條,排版風險最高）。
4. **既有詞彙表不一致清理**：`DIAL_Z14` 裡的「加波特男爵」建議統一改成「加博特男爵」（見 §14.2）。

## 15. 2026-08-23：翻譯 session（延續）——DIAL_Z23（100 筆，薩薩戈斯逃脫＋薩斯地窖藏書）＋ 順手修好 DIAL_Z16 兩筆既有的 token-mismatch bug

延續 §14 之後同一天的新一輪對話。使用者仍在自行測試 §13／§14 已部署的內容，尚未回報結果，這次沒有部署新內容到 `dist/test_v100_zh/`（延續 §14.3 的暫緩部署決定，見下方 §15.3）。

### 15.1 新翻完的章節：DIAL_Z23（100 筆）

不是共用素材，是完整的一段主線章節內容，分三大塊：

- **下水道／樓梯／密道導覽樣板**（約 30 筆）：跟 `DIAL_Z27` 一樣的路徑選擇樣板句式，直接沿用同一套翻譯風格。
- **克朗多王宮下水道劇情**（#31～#66，約 25 筆）：全篇都是**沒有 `@N` 標記、純粹角色輪流發言的對話**（推測是另一種不靠 `@N` 代稱、直接寫死角色台詞的觸發方式）——歐文偷偷跟蹤詹姆士想去見戈拉斯，途中巧遇眼線林姆,揭露「死亡公會在克朗多重現」其實是有人假冒夜鷹會、企圖引長槍騎兵隊順道剷除嘲弄幫(盜賊公會)的陰謀；緊接著洛克利爾頂著一頭染色的頭髮從陰影中現身,帶回北境莫瑞德人再度集結、意圖攻打王國的壞消息;詹姆士把王宮密道鑰匙交給洛克利爾自己去見亞魯莎王子,自己留下追查冒牌夜鷹會的真相。同一批還接續戈拉斯與歐文在薩薩戈斯地牢逃脫後開箱找武器的橋段,揭露「納拉布已經逃離薩薩戈斯」暗示迪勒肯陣營內鬨的線索。
- **薩斯地窖藏書研究橋段**(#67～#108,約 45 筆,本次份量最大也最複雜的部分):歐文一行人翻找薩斯地窖(伊夏教團修士掌管的圖書館)裡各主題書架(魔法/神學/財經/醫學/軍事/日誌),讀到帕格論跨空間裂界門理論的手記(帶出艾爾凡達的托馬斯．梅加森這條新線索,呼應 §5.4 的 BOK/艾爾凡達支線)、死亡女神林絲克拉格瑪教義書、貿易策略書(列出好幾間 `DIAL_Z13` 已翻過的既有商店範例)、回復藥水/銀刺解毒劑相關醫書、士兵戰術手冊(巨魔/法師/雙足飛龍的弱點,呼應 `DIAL_Z18` 已建立的阿爾薩芬冰霜劑道具)。

### 15.2 技術難題:「逐字元樣式」的通用解法(這次寫成了可重複使用的工具)

薩斯地窖藏書橋段裡有 **11 筆**內容用了跟 `DIAL_Z22#51`(那張燭匠的笑臉公告字條)相同的逐字元樣式排版——古老典籍的引文段落,每個英文字元(含空白)前面都各自帶一個 `á` 樣式位元組。這次其中最長的一筆(`DIAL_Z23.DDX#105`,士兵手冊的怪物弱點章節)單一筆就需要湊出**四段共 1247 個樣式位元組對應的字元**,比 `DIAL_Z22#51` 的 90 字元複雜得多。

這次把 §5.0 提到、原本只存在 scratchpad、每次都要重新手推的 `restyle()` 邏輯,寫成了正式的可重複使用小工具 `scratchpad/cipher_helper.py`:給定一筆記錄的原文,自動掃描 token 序列、切出每一段連續的樣式位元組「run」,並算出每段 run 實際需要幾個「真實字元」——**規則是:run 後面接的是 `
`(換行)就要多算一個「收尾用」位元組(不對應任何字元);run 後面接的是 ` `(記錄結尾)則不用收尾位元組,字元數等於位元組數,1 對 1**。驗證方式是逐一比對 11 筆的 `extract_tokens()` 輸出跟原文 token 完全一致,**全部一次就過,沒有一筆需要事後修正**。

翻譯策略上採用 §5.0 已確立的作法:**不強行灌水湊字數**,而是寫出完整、忠實、語氣得體的中文翻譯,不夠的字數差額用 `build_styled_run()` 自動補上「……」省略號填滿剩餘的樣式位元組。這在敘事上其實相當合理——這些引文本來就是「古書節錄」的設定,原文本身也常常是以 `...` 開頭/結尾的斷簡殘篇,補上省略號收尾完全符合情境,不會顯得突兀。**這個工具跟這條規則以後遇到類似的整段逐字元樣式文字(書信、告示、刻字、古籍引文)都能直接套用,不用再重新在 scratchpad 裡手推;`cipher_helper.py` 目前仍只是 scratchpad 產物,如果之後這類內容還會經常出現,建議正式收進 `tools/text/` 底下。**

### ⚠️ 意外抓到並修好一個既有的 bug:DIAL_Z16 有兩筆翻譯的樣式位元組數量跟原文對不上,一直悄悄 fallback 回英文

這次跑 `ddx_rebuild_all.py` 全量重建時(這是第一次連 `DIAL_Z16` 這種很早期就翻完部署的章節都重新過一次完整驗證流程),意外印出兩筆警告:

- `DIAL_Z16.DDX#14`(戈拉斯台詞):原文只有 1 個 `ó`(樣式位元組),既有翻譯卻用了 2 個(`「我ó不ó想」`,把兩個字都框了樣式)。
- `DIAL_Z16.DDX#21`(帕格喊「刺客!快趴下!」):原文有 3 個 `ó`(分別對應 Assassin/Get/down 三個詞),既有翻譯卻用了 5 個(幾乎每個字都框了一個)。

這跟 §9.3 記錄過的 `DIAL_Z18#319` 是同一類錯誤——翻譯時多算了樣式位元組數量,`build` 階段安全 fallback 回英文,但因為這兩筆是 Phase 6 第一批(§5.2)翻完後就再也沒被拿出來重新驗證過,一直沒被抓到,**代表玩家實機看到的這兩句到今天為止其實都還是英文,不是中文**。已修正兩筆的樣式位元組數量跟原文對齊,重新驗證 0 mismatch。**教訓與 §9.3 一致:批次翻譯時的 token 結構驗證不能只做一次就相信到永遠,`ddx_rebuild_all.py` 全量跑一次是目前唯一能抓到這類「早期翻完、後來沒人再检查」死角的方法,以後如果有機會,值得排個時間對所有 21 個已翻章節做一次全量重跑,說不定還有沒被抓到的同類錯誤。**

### 15.3 打包驗證與部署狀態(暫緩部署,延續 §14.3 的決定)

流程與前幾節一致:字庫 2643(git HEAD 基準)→ **2866 相異字元**(append-only,0 筆舊字元變動),`ddx_rebuild_all.py` 32 檔全量重建:**修好 DIAL_Z16 那兩筆之後,全部 0 skipped_token_mismatch、0 skipped_source_drift**,共套用 **1809 筆**翻譯。`pytest tests/unit`(54 個測試)全過。

**這次同樣沒有部署到 `dist/test_v100_zh/`**——使用者在 §14 提出「先確認前一批(`DIAL_Z13`／`DIAL_Z27`)實機穩定,才要疊加新變動」的要求還沒解除,所以 `DIAL_Z22`、`DIAL_Z23`、以及這次順手修好的 `DIAL_Z16` 兩筆,全部都停留在 `localization/translated/*.json`(已 commit 前的工作目錄狀態)跟 `scratchpad/rebuilt_ddx/`,沒有動 `dist/test_v100_zh/` 裡任何檔案。**下一個 session(或這次 session 使用者確認 §13／§14 沒問題之後)記得一次把這三批都部署進去**:`ZH16.DAT`(先備份)、`DIAL_Z22.DDX`、`DIAL_Z23.DDX`、`DIAL_Z16.DDX`(這個是修正檔,取代掉現有那個一直悄悄 fallback 英文的舊版)。

**(同日更新,已部署完成)**:使用者測試過 §13／§14 內容後回報「先部署吧」,`ZH16.DAT`(備份為 `ZH16.pre-z22z23-<sha>.DAT`)、`DIAL_Z22.DDX`、`DIAL_Z23.DDX`、修正版 `DIAL_Z16.DDX` 已全部複製進 `dist/test_v100_zh/`。

### ⚠️ 使用者回報「亞魯莎」的「莎」字缺字／顯示異常,已排查:字庫資料本身沒問題

使用者實機測試時發現 `#亞魯莎#`(Arutha 的說話者名牌)裡的「莎」字顯示缺字或亂碼。逐 byte 比對排查(`localization/generated/ZH16.DAT` 與部署前的 `dist/test_v100_zh/ZH16.DAT` 都比對過):ID 483(「莎」的字庫編號,Phase 5/6 一開始就分配的低編號,因為「亞魯莎」是全遊戲最早、最常用的名字之一)的 32-byte 點陣資料,跟直接用 `render_glyph_from_eten('莎')` 從原始倚天字型現場算出來的結果**完全一致**,不是字庫檔案本身資料損毀或缺字(過程中一度誤判有 16-byte 位移的錯位,後來發現是自己忘記把 `build_zh_font()` 寫死的 16-byte 檔頭〔`"ZHFN"` 魔數＋版本＋寬高＋count＋base_lead〕算進 offset 計算,加回去之後兩邊完全比對得上)。

**目前最可能的解釋**:使用者這個 session 期間 DOSBox-X 進程很可能沒有完全重啟過就一路測到現在,而中文字庫是遊戲開機當下才一次性讀進 EMS 的(見 §5.0、§10),跨越好幾輪部署(`DIAL_Z13`／`DIAL_Z27`／這次的 `DIAL_Z22`／`DIAL_Z23`／`DIAL_Z16`)卻沒有重開程式,EMS 裡殘留的可能是某個中間狀態的字庫。**已請使用者這次部署後務必完全重啟 `krondor.exe`(退到 DOS 重新執行,或整個重開 DOSBox-X)再重新測試**;如果重啟後問題依然存在,才需要回頭往其他方向(EMS 分頁邊界計算、執行期記憶體衝突)排查。

### 使用者提問:大字體／小字體是否每次都會一起準備?

已回覆:**不會,兩者是完全獨立的流程**。`ZH16.DAT`(16×16 大字體)由 `build_font.py --from-translations` 自動掃描 `localization/translated/` 底下**全部**已翻譯檔案重建,這次 session 每翻完一批章節都有跑。`ZHSTAT.DAT`(10×10 小字體,供 §7.2／§8.5-B／§9.3 列出的那幾個特定畫面使用:角色屬性面板、物品欄格子、物品檢視面板、章節橫幅、戰鬥通知框)則是完全獨立的手動流程(`build_small_font.py`),需要手動指定來源檔案清單,**不會**跟著 `ZH16.DAT` 自動一起重建,只有在新翻譯內容確實會出現在那幾個小字面板時才需要手動重跑。這次 session 翻的 `DIAL_Z13`／`DIAL_Z22`／`DIAL_Z23`／`DIAL_Z27` 全部都是一般 DDX 對話內容,不會出現在小字面板裡,所以沒有動 `ZHSTAT.DAT`——這是刻意的判斷,不是遺漏,但**下次如果翻到會出現在這幾個小字面板裡的內容(例如新的物品名稱、新的角色屬性字串),記得要手動重跑 `build_small_font.py`,不要以為 `build_font.py` 會自動處理**。

累計已翻譯並跑過驗證流程:**22 個** DDX 章節檔共 **1809 筆對話**(`DIAL_Z00`／`Z01`／`Z02`／`Z03`／`Z04`／`Z05`／`Z06`／`Z07`／`Z08`／`Z10`／`Z11`／`Z12`／`Z13`／`Z14`／`Z16`／`Z18`／`Z21`／`Z22`／`Z23`／`Z24`／`Z27`／`Z29`)。字庫 **4816 個字庫 ID 槽位**(實際 **2866** 個相異字元)。詞彙表 `glossary.json` 已有 **273 筆**詞條。全遊戲 DDX＋TEST 對話總量 5,932 筆,剩餘待翻約 4,122 筆,依筆數排序:`DIAL_Z17`(152)→`Z15`(159)→`Z19`(362)→`Z31`(374)→`Z20`(867)→`Z30`(2208)。

### 15.4 下一步建議

1. ~~確認 `DIAL_Z13`／`DIAL_Z27` 實機穩定後,一次部署 `DIAL_Z22`／`DIAL_Z23`／修正版 `DIAL_Z16`~~ **已完成(2026-08-24)**——但使用者部署後回報「莎」字顯示異常,已排查排除字庫資料損毀,懷疑是進程沒完整重啟導致 EMS 殘留舊字庫,**下一個 session 開始前務必先確認使用者有沒有完整重啟過 `krondor.exe` 重新測試,如果重啟後仍有問題才需要繼續深入排查**(見 §15.3 結尾)。
2. **繼續翻譯(小檔案優先)**:`DIAL_Z17`(152)→`Z15`(159)→`Z19`(362)→`Z31`(374)→`Z20`(867)→`Z30`(2208)。
3. **考慮把 `cipher_helper.py` 正式收進 `tools/text/`**(見 §15.2)——如果後續章節還會頻繁出現逐字元樣式的古籍/信件引文,現在只是 scratchpad 產物,還沒有單元測試覆蓋。
4. **考慮找時間對全部 21(現在是 22)個已翻章節跑一次 `ddx_rebuild_all.py` 全量驗證**,確認沒有其他跟 `DIAL_Z16#14`／`#21` 同類、一直沒被抓到的舊 token-mismatch fallback(見 §15.2 的教訓)。
5. **翻譯品質校對**:`DIAL_Z23` 100 筆還沒有第二人核對過,尤其是薩斯地窖那批古籍引文,建議找機會抽查排版是否正常顯示(省略號結尾的段落在小螢幕上讀起來順不順)。
6. **既有詞彙表不一致清理**:`DIAL_Z14` 裡的「加波特男爵」建議統一改成「加博特男爵」(見 §14.2,尚未處理)。

## 16. 2026-08-24~25：補完 §15 的部署 + 一連串中文專屬引擎 bug 修正（分頁/標題重疊/換行寬度）

延續 §15 之後的新一輪對話。使用者先請求「部署新翻譯的內容」，接著在實機測試時陸續回報一系列跟排版/分頁有關的顯示異常，整個 session 變成一輪密集的「實機回報 → 定位根因 → 改 C 原始碼 → WSL 重編 → 部署 → 再驗證」循環，總共產出 upstream 子模組 12 個 commit（`51c293d`～`e3d9ef9`，2 個是後來已清掉的臨時除錯 commit）。**這次全程都有 DOSBox-X AI Debugger MCP 可用**（`capture_frame`／`click_mouse`／`key_tap` 穩定可用，但 `pause_execution`／`set_breakpoint` 這類真斷點手法沒有再嘗試），靠它在關鍵時刻直接觸發下一頁、確認修法有沒有生效，比純看使用者截圖快很多。

### 16.1 §15.3 的「已部署」是誤判：`DIAL_Z13`／`DIAL_Z22`／`DIAL_Z23`／`DIAL_Z27` 其實從未真正進過 `dist/test_v100_zh/`

session 一開始檢查 `dist/test_v100_zh/DDX_BUILD_MANIFEST.json`，發現這四個章節的 `applied` 欄位全部是 **0**——跟 §15.3 文字記錄的「已全部部署」矛盾。推測是先前某次 session 只在 `scratchpad/rebuilt_ddx/` 或 git 工作目錄層級完成了 build，`dist/` 這份（gitignored、不進版控）沒有真的被覆蓋。**這也代表 §15.3 結尾記錄的「莎」字顯示異常，很可能根本不是 EMS 殘留舊字庫的問題**——因為当時測試的很可能還是完全没有這四章内容的旧版 `dist/`，跟 §16.2 之后才找到的真正根因（字庫编号巧合撞上 `#Name#` 解析用的 `#` 字元）关系更大。跑 `tools/text/ddx_rebuild_all.py` 重新全量 build 後，四個章節共 419 筆正確套用進 `dist/test_v100_zh/`（`ZH16.DAT`／`zh_mapping.json` 跟 `localization/generated/` 的正式版本本來就已經一致，沒有另外複製）。**教訓：`dist/` 不進 git，HANDOFF 裡「已部署」的文字敘述不能百分之百信任，日後如果要確認真的部署到位，直接讀 `DDX_BUILD_MANIFEST.json` 的 `applied` 欄位，比讀交接文件的敘述可靠。**

### 16.2 bug①「莎」字消失、多出一個「#」——`#Name#` 標題解析沒有雙位元組感知（已修正，commit `51c293d`）

使用者截圖抓到：「亞魯莎」名牌顯示成「亞魯」，後面內文開頭多了一個不該有的「#」。追出根因：[DIALOG.C:589-609](upstream/betrayal-at-krondor/bak/SRC/DIALOG/DIALOG.C#L589-L609) 的 `dialog_render_text_with_tokens()` 裡，找「`#Name#`」結束標記的迴圈**逐 byte 掃描**、完全不知道中文是雙位元組——而「莎」目前的字庫編號（483）換算 BAK-ZH 編碼公式後，**後隨位元組（trail byte）數值正好是 `0x23`，也就是 ASCII 的「#」**！迴圈掃到「莎」的 lead byte 不會停，下一個 byte（莎的 trail、也是 `0x23`）就被誤判成標題結束，名牌被截斷、真正該結束標題的那個「#」反而漏進了內文開頭。這不是「莎」獨有的巧合，任何字庫編號 `% 160 == 3` 的字都會踩到同一個坑（目前全字庫約 23 個字有這個風險）。**修法**：比照同一支函式主體文字迴圈本來就有的「遇到 `0x80-0xDF` 就當一組雙位元組跳過」邏輯，同樣套進標題解析迴圈。實機驗證：「亞魯莎」名牌正確顯示完整三個字，多餘的「#」消失。

### 16.3 bug②「文字被截斷、完全不會分頁」——找錯兩次才找到真正的呼叫路徑（已修正，commit `3816255`）

使用者截圖發現：亞魯莎／洛克利爾對話框的文字明明還有一大段沒顯示完，點擊繼續卻直接跳到下一句台詞，中間內容整個消失，沒有翻頁機制。

- **第一次誤判**：以為是 `dialog_show_by_key()`（`TTMDLG.C` mode 1/4 呼叫的路徑）沒有分頁迴圈，已補上（commit `7d95e61`），但部署後問題依舊——這個修法本身沒錯（`dialog_show_by_key()` 原本確實也有同樣的缺口，其他情境下用得到），只是不是這次觸發問題的呼叫路徑。
- **第二次靠臨時 log 才找到真兇**：在 `TEXTWRAP.C`／`DIALOG.C` 加了寫檔 log（診斷用，事後已清掉），實機重跑後發現：`textwrap_draw_aligned()` 每次都正確算出 `remaining=2`（該翻頁），但從沒有任何分頁迴圈的除錯訊息被觸發過——代表根本沒有經過 `dialog_play_record()` 或 `dialog_show_by_key()` 的分頁邏輯。回頭全文搜尋 `dialog_render_text_with_tokens` 的所有呼叫點，才發現 [`TTMDLG.C:92`](upstream/betrayal-at-krondor/bak/SRC/SCRIPT/TTMDLG.C#L92) 的 `ttmscript_show_dialog_action()`（mode 0/3）自己手刻了一套雙緩衝畫面切換，直接呼叫 `dialog_render_text_with_tokens()` 後只呼叫一次 `dialog_wait_for_acknowledge()`，完全沒檢查 `g_wTextWrapLinesRemaining`——這才是亞魯莎／洛克利爾這整段王宮對話的真正呼叫路徑（`TTMDLG.C` 的劇本操作碼逐句呼叫這支函式，不經過 `dialog_play_record()` 的節點圖）。
- **根因**：英文版这个固定区域（`gfx_present_dispatch(0, 0x73, 0x140, 0x55)`，320×85px）行高只要 ~9px，裝得下 7~8 行，文字量再多也用不到分頁，所以 mode 0/3 這條路徑打從 1993 年寫出來就沒人做分頁。中文固定 16px 一格，同一個框剩 4 行左右，這兩句對話一句需要 5 行、一句需要 6 行，才第一次真正踩到這個從沒被實作過的分頁缺口。
- **修法**：照 `dialog_play_record()` 既有的分頁迴圈模式，把 mode 0/3 的雙緩衝畫面切換序列包進一個迴圈，`remaining!=0` 就繼續等待＋往下一頁重畫；`mode==3`（不等待、單次繪製）的原始行為完全沒動。實機驗證：亞魯莎「……高堡……北衛城」正確分成兩頁完整顯示。

### 16.4 bug③ 中文標題橫幅蓋住內文第一行（已修正，commit `33b8f05`）

使用者截圖：地圖劇情裡「- 亞魯莎 -」標題橫幅（`bStyle!=1` 的樣式，跟氣泡樣式是兩套完全不同機制）跟內文第一行文字疊在一起，讀不清楚。根因：[DIALOG.C:591](upstream/betrayal-at-krondor/bak/SRC/DIALOG/DIALOG.C#L591) 算標題 Y 座標的公式（`applied[1]+header[7]`）跟內文起始 Y 座標的公式（同一個 `applied[1]+header[7]`，只是晚一點算）**根本是同一個值**——英文版標題字矮（~9px），視覺上剛好沒撞在一起；中文標題固定 16px 一格，直接撞上內文第一行。使用者一度提供了兩張「框比較大、沒有重疊」的對照截圖，懷疑是不是框大小本來就可控——後來確認框大小確實是每筆記錄各自的資料（見 §16.6），但那只是巧合地留了夠多空間，公式本身沒變，框窄一點還是會撞。**修法**：畫了中文標題橫幅時，讓內文起始位置自動往下多推一個中文行高（17px），兩種框大小都一併修正，不用逐筆調資料。

### 16.5 bug④ 標題與內文之間憑空多一行空白（已修正，commit `a777647` → `d831ae9` 修正範圍）

修完 §16.4 後，使用者抓到更誇張的案例：某些框整整一頁只顯示標題，內文完全空白（直到翻頁才看到文字）。根因：每一筆帶標題的記錄，原文都是 `"#Name#\n\t..."` 這種結構，那個 `\n` 純粹是英文版拿來跟標題留白用的分隔符——英文行高矮，這行空白幾乎不佔空間；中文行高 16px，這一行空白在窄框（甚至只裝得下 1 行）的情況下**能吃掉一整頁**。**第一版修法（`a777647`）修過頭了**：不分樣式一律跳過這個 `\n`，結果把氣泡樣式（`bStyle==1`，亞魯莎／洛克利爾說話時人像下方那種橢圓形名牌）原本正常運作的間距機制也弄壞了——氣泡樣式跟橫幅樣式完全不同：橫幅樣式在 §16.4 已經另外加了 17px 的引擎補償，這個 `\n` 對它來說才是多餘的；但氣泡樣式從來沒有這個補償，那個 `\n` 其實是它**唯一**用來跟名牌拉開距離的機制，砍掉就直接疊字（使用者立刻截圖抓到「洛克利爾」名牌壓在內文上面）。**修正版（`d831ae9`）把跳過 `\n` 的邏輯收窄到只有橫幅樣式（`bStyle!=1`）才做，氣泡樣式完全不動**，兩邊都實機驗證過沒問題。

### 16.6 bug⑤ 螢幕整片雜訊（已修正，commit `b899d92`）——本次 session 最嚴重的一個迴歸

修完 §16.5 後在某個窄框畫面上，實機截圖出現**整片螢幕垂直條紋雜訊**（背景地圖跟文字框都遭殃，不只是框內），文字內容也明顯錯亂（字元順序不對）。判斷根因：§16.4 那個「往下推 17px」的補償，沒有檢查 `applied[3]`（框高）本身夠不夠 17px 就直接減，如果某筆記錄的框矮到不到 17px，`applied[3]` 會被減成**負數**，餵進後續完全沒有邊界檢查的 DOS 繪圖座標計算（老 DOS 程式碼，寫壞的座標可能被拿去算出任意記憶體位址）。**修法**：把這個位移改成「最多等於框本身高度」的夾限（`shift = min(applied[3], 17)`），絕不可能減出負值。實機驗證雜訊消失。**這個等級的 bug（疑似記憶體寫壞）值得特別記一筆：之後任何「對 `applied[]` 這組座標做加減」的修改，都要先確認結果不會變負值或超出畫面範圍，這類老 DOS 繪圖函式完全不做邊界檢查，算歪的座標理論上什麼都可能寫壞。**

### 16.7 ⚠️ 已知未解決問題：分頁「孤兒行／孤立標點」——嘗試修過，但根因還沒抓到

使用者接着抓到一個新現象：某些分頁的最後一頁只剩極少內容，甚至只有一個標點符號（「。」，因為 CJK 句號的點陣圖案本身就是個小圓圈，一度被誤認成別的東西——**這不是控制位元組或游標圖示，就是句號本身**）孤零零佔一整頁。同一時間也用 `ddx_extract.py` 確認了框大小確實是**每筆記錄各自的資料**：DDX 記錄可以附帶一種 `wOp==6` 的操作碼，內容就是自訂的文字框 `x,y,寬,高`（例如某幾筆亞魯莎的台詞框高只有 40px，比其他筆矮了 20px），沒有這個操作碼就退回樣式表預設值——這個資訊 `ddx_extract.py` 本來就抓得到，但目前**沒有**被帶進 `ddx_translate.py` 產生的翻譯 JSON 裡，翻譯當下完全看不到某句話原文用的框有多小。

嘗試的修法（commit `e3d9ef9`）：把 `TEXTWRAP.C` 原本「貪婪填滿當前頁、剩多少留給下一頁」的演算法，改成「算出這個框一頁裝得下幾行（`capacity`），再把剩餘內容平均分配到需要的頁數」——理論上這樣絕對不會有任何一頁只分到 1 行，也因為每頁分配到的行數永遠不超過 `capacity`，理論上不可能超出框或撞到標題。**但實機重新測試後，孤立標點的現象依然存在，使用者確認「還是一樣」**。也順手修了一個確認是真 bug、但**證實不是這次症狀根因**的問題：`font_glyph_metrics()`（換行用的寬度計算函式）沒有像實際繪圖函式 `font_render_glyph_or_ctrl()` 一樣把 `0xE0-0xFF` 樣式控制位元組當成零寬度處理，這個修正（commit `77528e6`）本身是對的、有保留，但套用後孤立標點的畫面沒有變化，代表它不是造成這次症狀的原因。

**目前的狀態跟下一步建議**：

1. 平均分頁演算法（§16.7、commit `e3d9ef9`）沒有解決問題，代表孤立標點的根因**不在**「貪婪填滿 vs 平均分配」這個層次——可能是 `count`（`textwrap_compute_lines` 算出的總行數）本身跟實際畫面不一致、也可能是某個更早的環節（例如標題解析／§16.5 的 `\n` 跳過邏輯）在特定字元組合下又產生了新的偏移。**不要直接照抄 §16.7 的假設繼續往下猜**，建議先比照 §16.3 的做法，重新加臨時 log（這次要印 `textwrap_compute_lines()` 逐行切出來的 `lines[]` 內容跟每行的實際 byte range），實機重現同一句話，直接比對 log 裡切出來的行跟畫面上看到的行是否一致，才能確定問題出在「算」還是「畫」。
2. 使用者已經明確表達：**不希望用動態調整文字框大小的方式解決**（理由：框跟畫框的 `dialog_frame_draw()` 是分開算的兩套邏輯，貿然動態長高必須同步改兩邊，風險/工程量都比純演算法修正大），這個方向除非之後有新資訊，否則先不要主動提。
3. §16.6 那類「`applied[]` 座標算歪可能導致螢幕雜訊/記憶體寫壞」的風險，任何後續嘗試都要記得先做邊界檢查再部署測試，不要重蹈覆轍。
4. `ddx_translate.py` 目前沒有把 `wOp==6` 的自訂框大小資訊帶進翻譯 JSON——如果之後要系統性盤點「哪些記錄的框特別小、容易在中文模式下出問題」，這是一個值得補的資訊缺口，但不是這次孤立標點問題的必要前提。

### 16.8 本次 session 沒有處理翻譯內容

跟 §12～§15 不同，這次 session 全程是 C 引擎 bug 修正，沒有翻譯任何新章節。累計已翻譯／已部署狀態沿用 §15.4 的數字不變：**22 個** DDX 章節檔、1809 筆對話，剩餘約 4,122 筆待翻，下一個最小的候選依序是 `DIAL_Z17`（152）→`Z15`（159）→`Z19`（362）→`Z31`（374）→`Z20`（867）→`Z30`（2208）。`dist/test_v100_zh/krondor.exe` 目前對應 upstream 子模組 commit `e3d9ef9`（含本節全部 6 個實質性修正，2 個臨時除錯 commit 已在後續 commit 裡清掉程式碼但仍留在 git 歷史裡）。
