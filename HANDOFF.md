# 交接備忘錄 (Session Handoff Memo)

**最後更新：** 2026-08-26（新增 `DIAL_Z20` 翻譯與部署；修正詞彙表 Katala 誤植、回填字庫缺字）

**這份文件刻意保持精簡，設計成每個新 session 開始前整份讀完就好。** 完整的逐 session 歷史敘事（每個 bug 怎麼定位根因、怎麼修、學到什麼教訓）都搬到 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md) 了——只有在需要追查某個舊問題的細節（例如「這個 bug 之前是怎麼修的」）時才去那份用關鍵字搜尋進去讀一小段，不需要整份讀過。**下方每次有新進度，把對應項目從「待處理」搬到別處或刪掉，不要只往後面加，保持這份文件短小。**

## 目前狀態

- **已完整翻譯並跑過驗證流程**：27 個 DDX 章節檔，共 3723 筆對話（`DIAL_Z00`／`Z01`／`Z02`／`Z03`／`Z04`／`Z05`／`Z06`／`Z07`／`Z08`／`Z10`／`Z11`／`Z12`／`Z13`／`Z14`／`Z15`／`Z16`／`Z17`／`Z18`／`Z19`／`Z20`／`Z21`／`Z22`／`Z23`／`Z24`／`Z27`／`Z29`／`Z31`），加上 `OBJINFO.DAT` 物品名稱系統（137 筆）、`UI_HARDCODED.json` 硬編碼字串（55 筆）。`TEST.json`（1 筆）已翻完但**還沒打包**，缺一份乾淨的 `TEST.DDX` 可以對（見下方「待處理」）。
  - `DIAL_Z20`（867 筆）是目前為止最大的一批翻譯——拉姆特／艾格利／薩斯／馬拉克十字鎮／卡瓦爾堡／北衛城／艾爾凡達等地的支線劇情大合集，劇情密度極高：圖蘭尼客棧老闆蘇馬尼的格鬥／討價還價課程、矮人礦坑（含大量口音體矮人台詞，比照 archive 既有慣例用語氣粗獷但不刻意造字的方式呈現）、薩斯地窖藏書任務、北衛城圍城前置戰備（含派特魯斯／馬丁公爵／詹姆士／洛克利爾的軍務支線）、艾爾凡達精靈王子卡林的隱匿術與十字弓教學，以及**烏格妮．科瓦利斯的追求者「納馮．杜桑多」其實是她「亡故」多年的哥哥內維爾、如今是夜鷹會頭目的重大劇情反轉**（詳見 `glossary.json` 新條目）。翻譯過程中順手修正了詞彙表一處既有誤植——`Katala` 先前誤記為托馬斯之妻，經本章對話明確證實她其實是帕格之妻（多爾根王之妻是亞葛拉蘭娜王后，兩人在此之前未被清楚區分過）。含少量 `ñ`／`ó` 局部強調標記，867 筆全部 0 個 token-mismatch fallback。新增 40 餘個專有名詞已全數回填進 `glossary.json`。**部署前的全字庫涵蓋率掃描抓到 77 個新增中文字沒收錄在字庫裡**，已用 `build_font.py --from-translations` 重新產生字庫補齊，字庫從 3216 字擴充到 3293 字。
  - `DIAL_Z31`（374 筆）是歐文／戈拉斯／詹姆士等人分頭在各城鎮／北境村落挨家挨戶探訪的支線資料表，NPC 密度全遊戲數一數二，新增近 30 個一次性小角色與地名（盧肯、塔德．奎斯托、弗拉爾．威根、蕭拉爾、戴爾希納德、丹肯營地、艾爾德角、龍尾井等），已全數回填進 `glossary.json`（見下方「其他待辦」）。含少量 `ñ`／`ð`／`ó` 局部強調標記與一段 22 字元的逐字元招牌（`á`，entry #75，湊字數對齊原文樣式位元組數），374 筆全部 0 個 token-mismatch fallback。**部署前的全字庫涵蓋率掃描抓到 115 個新增中文字沒收錄在字庫裡**（`build_font.py --from-translations` 重新產生字庫後補齊，見下方「重要教訓」），字庫因此從 3101 字擴充到 3216 字。
  - `DIAL_Z17`（152 筆）是「莫瑞德人字鎖」猜字小遊戲的資料表，跟其他章節性質不同：每筆記錄用 `#` 分三段——答案單字／候選字母轉盤表／提示謎語詩句。前兩段是 `CIPHER.C`（`cipher_puzzle_is_solved()`）逐 byte 比對的遊戲邏輯，經使用者確認後**只翻第三段的提示詩句，答案單字與轉盤字母表維持原文英文**，猜字遊戲玩法完全不變；只翻中文的部分靠 152 筆逐一人工翻譯，`\x0a`／`\x00` token 數量都跟原文對齊，`ddx_translate.py build` 驗證 0 個 fallback。
  - `DIAL_Z15`（159 筆）是主線旅途的城鎮／地點探索敘事（拉姆特、克朗多、馬拉克十字鎮、薩薩戈斯、薩斯、羅姆尼、高堡、北衛城、卡瓦爾堡、阿曼加、錫爾登、厄提斯島、賽瑟儂等），含大量地名／人名專有名詞與逐字元樣式標記（`ó`／`ñ`／`ð`，用來標示原文局部強調語氣，翻譯時比照 archive 既有慣例把標記字元原樣保留在對應中文詞前後，`\t`／`\n`／`@N`／`\x00` token 都跟原文逐一核對過，`ddx_translate.py build` 驗證 0 個 fallback）。
  - `DIAL_Z19`（362 筆）是帕格／歐文／戈拉斯一行人探索卡爾贊遺址、跟「提米里安雅七神」（達沙梵、蘇塔卡米等）逐一對話的支線，是目前為止樣式標記密度最高的一個章節：
    - 除了慣用的 `ó`／`ñ`／`ð` 局部強調標記外，這章大量出現**逐字元樣式**段落（原文每一個字元、包含空白與標點，都各自前綴一個樣式位元組 `ã`）——這是諸神說話時的「神諭」特效，用來讓引擎逐字顯示。因為 `ddx_rebuild_common.py` 的 `extract_tokens()` 把每個 `ã` 都算成獨立 token，翻譯這類段落時中文字數必須跟原文段落的樣式位元組數量**逐一對齊**，不能只求語意通順——由於中文表達同樣語意通常遠比英文精簡，實務上得靠「先翻、量字數、不夠就加古語化贅詞（『凡人啊』『不容有失』『天機難測、玄妙莫名』之類）反覆迭代湊字數」的做法逐段湊到精確長度，單一段落最長湊到 368 字元（entry #441）。
    - 另外發現一種**先前章節沒出現過的樣式標記字元 `á`（0xE1）**，用於帕格與歐文之間的「心靈感應／念力交談」段落（entry #429），處理方式跟 `ã` 完全相同（逐字元湊長度），只是換一個標記位元組。
    - 這章新增了一批專有名詞（加米娜、卡爾贊、潘納斯提安登、提米里安雅、達沙梵、蘇塔卡米、阿爾瑪洛達卡、瓦爾赫魯等），**尚未回填進 `glossary.json`**，見下方「待處理」。
    - 跟 `DIAL_Z15` 一樣，`\t`／`\n`／`@N`／`\x00` 及所有樣式標記 token 都用 `extract_tokens()` 逐筆自動比對驗證過，362 筆全部 0 個 token-mismatch fallback。
- **部署狀態**：上述 27 個章節全部確認部署在 `dist/test_v100_zh/`（2026-08-26 用 `DDX_BUILD_MANIFEST.json` 的 `applied` 欄位重新驗證過，不是只看文件敘述——之前一度誤判過，詳見 archive §16.1）。`dist/test_v100_zh/krondor.exe` 目前對應 upstream 子模組 commit `e3d9ef9`，含 2026-08-25 那輪修的 6 個中文專屬引擎 bug（`#Name#` 標題解析截斷、兩處分頁邏輯缺口、標題橫幅蓋內文、多餘空行、螢幕雜訊迴歸——細節見 archive §16）。`DIAL_Z20`（跟先前的 `DIAL_Z31`／`DIAL_Z19`／`DIAL_Z17`／`DIAL_Z15` 一樣）尚未在實機（DOSBox-X）上實際跑過驗收，只跑過 build/validate 的離線驗證。
- 字庫 **5503 個 ID 槽位**（實際 **3293** 個相異字元），全真倚天點陣、零 fallback。**2026-08-26 部署 `DIAL_Z20` 前重新做過一次全字庫涵蓋率掃描**，抓到 77 個新增翻譯用到、字庫裡還沒有的字，已用 `build_font.py --from-translations` 重新產生字庫補齊。詞彙表 `glossary.json` 共 **344** 筆（`DIAL_Z20` 新增的 40 餘個專有名詞已全數回填，同時修正了 `Katala` 誤植為托馬斯之妻的舊錯誤——她其實是帕格之妻）。
- 全遊戲 DDX＋TEST 對話總量 5,932 筆，剩餘約 **2,208 筆**待翻，只剩最後一個檔案：`Z30`（2208）。

## 待處理 / 已知問題

### ⚠️ 分頁「孤兒行／孤立標點」——尚未解決

某些對話框分頁到最後一頁時，只剩極少內容甚至一個標點符號（CJK 句號「。」的點陣圖案本身就是個小圓圈，容易誤認成別的東西）孤零零佔一整頁。已知：

- 框大小是每筆 DDX 記錄各自的資料（`wOp==6` 操作碼可自訂 x/y/寬/高），但目前 `ddx_translate.py` 的翻譯 JSON 沒有把這個資訊帶出來，翻譯當下看不到某句話原文用的框有多小。
- 已嘗試把 `TEXTWRAP.C` 的分頁演算法從「貪婪填滿當前頁」改成「平均分配剩餘行數到所需頁數」，理論上任何一頁都不該只分到 1 行——**部署後實機重測，孤立標點依然重現，代表根因不在這個層次**。
- 順手修正的 `font_glyph_metrics()` 樣式控制位元組零寬度 bug 是對的、有保留，但也證實不是這次症狀的根因。
- **使用者明確表示不希望用動態調整文字框大小的方式解決**（框跟畫框的 `dialog_frame_draw()` 是分開算的兩套邏輯，同步改風險較高），這個方向先不要主動提。
- 下一步建議：比照抓分頁缺口 bug 的做法，重新加臨時 log（印 `textwrap_compute_lines()` 逐行切出來的 `lines[]` 內容跟每行實際 byte range），實機重現同一句話，直接比對 log 裡切出來的行跟畫面上看到的是否一致，先確認問題出在「算」還是「畫」。完整背景見 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md) §16.7。

### 其他待辦

1. **繼續翻譯（只剩最後一個檔案）**：`Z30`（2208 筆）——翻完這個，全遊戲 DDX＋TEST 對話就全數翻譯完畢了。
2. **補齊 `TEST.json` 打包**：`bak rmf list` 裡有 `TEST.DDX`，但手上的 `scratchpad/pristine/` 快照沒包含它，需要先用 `bak rmf extract` 補一份乾淨的 `TEST.DDX` 進去，再跑 `ddx_translate.py build`。
3. **既有詞彙表不一致清理**：`DIAL_Z14` 裡的「加波特男爵」應統一改成「加博特男爵」（其餘章節都用後者）。
4. **翻譯品質校對**：27 個已翻章節目前都還沒有第二人核對過，尤其樣式位元組密集／逐字元排版的段落（書信、告示、古籍引文、`DIAL_Z19` 的諸神神諭獨白）排版風險最高，建議找機會抽查。`DIAL_Z17`／`DIAL_Z15`／`DIAL_Z19`／`DIAL_Z31`／`DIAL_Z20` 都還沒在實機上實際驗收（見上方「目前狀態」）——`Z17` 優先看提示詩句在猜字畫面上的排版是否正常、答案單字／轉盤字母表是否維持英文原文不受影響；`Z15` 優先看 24 個地點敘述段落跟含 `ó`／`ñ`／`ð` 強調標記的對話（例如 #60/#61/#62/#84/#100/#142/#156/#162/#163/#167）排版跟強調效果是否正常顯示；`Z19` 優先看那幾段逐字元湊出來的諸神獨白（entry #382/#383/#384/#385/#387/#388/#429/#433/#441/#465）實機顯示時逐字動畫的節奏跟斷行是否正常，以及新增的 `á`（0xE1）樣式標記（entry #429）是否跟 `ã` 一樣正確渲染；`Z31` 優先看散布各城鎮的挨家挨戶對話排版是否正常，尤其 entry #75 那段 22 字元逐字元招牌（`á`）跟 #557 波斯維奇夫人議事廳那段長對話；`Z20` 優先看北衛城圍城前置戰備那幾段長篇軍務對話（例如 #1183/#1416/#1539）跟矮人口音角色的台詞排版，以及納馮／內維爾反轉劇情那幾段（#1479-#1490）語氣是否連貫。
5. **考慮對全部已翻章節跑一次 `ddx_rebuild_all.py` 全量驗證**，確認沒有 archive §15.2 那種「早期翻完、後來沒人再檢查」導致的舊 token-mismatch fallback 死角。

## 環境設置（下個 session 不用重裝，但要知道在哪）

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
- 設定檔：`dist/dosbox_zh_test.conf`。掛載的是 `dist/test_v100_zh/`（獨立測試資料夾，**不是**原始遊戲資料夾，這點很重要，見下方「重要教訓」）。
- 啟動：`Start-Process "D:\git\DOSBox-X-AI\build-memory\dosbox-x.exe" -ArgumentList "-conf","dist\dosbox_zh_test.conf"`
- 有 DOSBox-X AI Debugger MCP 工具可用（`.mcp.json` 已設定好）：`capture_frame`／`key_tap`／`click_mouse` 這幾個穩定可用，2026-08-25 這輪 session 大量靠它們直接觸發翻頁、驗證修法有沒有生效。**沒有滑鼠絕對定位/點擊**支援（`click_at`/`move_mouse_absolute` 都回 `UNKNOWN_METHOD`）。`pause_execution`／`set_breakpoint` 這類真斷點手法過去曾讓 `dosbox-x.exe` 反覆當掉斷線，優先用「加臨時 log／改行為觀察畫面」代替即時斷點除錯。

### 倚天字型來源（**不在 git 裡，本機外部依賴**）
- `D:\git\Fonts\iso\FILES\STDFONT.15` / `SPCFONT.15` / `ASCFONT.15`（真的倚天 3.53 點陣字，索引公式已用 oracle 驗證過）。路徑寫死在 `tools/font/build_font.py`（`_ETEN_STD_PATH` 等常數）。**別台機器上不存在的話，字型工具會自動退回 TTF 點陣化或合成佔位圖案，不會報錯，但字型會變成備用方案。**
- `D:\git\Fonts\ET353S.iso`（原始 ISO）本身是**損毀的**，能用的是使用者手動解壓在 `D:\git\Fonts\iso\` 底下的內容，這個資料夾如果被清掉，字型來源就沒了。
- `D:\git\Fonts\Fusion_Pixel_10px.ttf`：小字級字型（`ZHSTAT.DAT` 等），`build_small_font.py`／`build_font.py` 的 TTF fallback 都會用到，路徑寫死在 `build_font.py` 的 `_FUSION_PIXEL_PATH`。同樣是本機外部依賴，缺檔案時小字型會建置成全空白字形（不報錯，但字看不見）。

## 關鍵原始碼位置

都在 `upstream/betrayal-at-krondor`（獨立 git repo，子模組式的 clone，不是本專案 git 歷史的一部分）：

- `bak/SRC/GFX/FONT/FONT.C` / `FONT.H`：中文/ETen ASCII 繪圖、寬度計算（`font_glyph_metrics`）、`g_bMixedZhMode` 判斷。
- `bak/SRC/UI/TEXTWRAP.C`：折行、分頁（`textwrap_compute_lines`／`textwrap_draw_aligned`，讀 `g_bMixedZhMode`）。
- `bak/SRC/DIALOG/DIALOG.C`：`dialog_render_text_with_tokens()`（token 展開、標題解析、`g_bMixedZhMode` 設定處）、`dialog_play_record()`（節點圖對話主迴圈，含分頁）、`dialog_show_by_key()`。
- `bak/SRC/SCRIPT/TTMDLG.C`：`ttmscript_show_dialog_action()`——劇本驅動的另一條對話顯示路徑，跟 `dialog_play_record()`／`dialog_show_by_key()` 是三套平行機制，2026-08-25 才第一次發現（見 archive §16.3）。

本專案（`betrayal-at-krondor-for-zh`）這邊：

- `tools/font/build_font.py`：字型產生工具（ETen 優先 → TTF → 合成佔位圖案），也是 `encode_string`/`decode_string`（中文編碼）的定義處。
- `tools/text/ddx_extract.py` / `ddx_pack.py`：DDX 對話檔 extract/pack，`ddx_translate.py` 在這兩個之上組出 scaffold/status/build 的翻譯 pipeline，`ddx_rebuild_all.py` 是安全的全量重建工具（見下方流程）。
- `localization/generated/`：目前的 `ZH16.DAT`、`zh_mapping.json`（已 commit，是正式產物）。
- `localization/translated/`：翻譯來源檔（`DIAL_*.json`），含 id/node_id/source（英文原文）/tokens/translation/status/notes。原文會一起 commit 進 git，方便覆核翻譯（原文本身是原廠已免費公開下載的遊戲內容）。
- `dist/test_v100_zh/`：**測試用**遊戲資料夾（gitignored，不進 git），裡面混了乾淨遊戲檔 + 目前測試中的中文補丁檔案。內容隨時可能被下一輪測試覆寫，不要當成正式產物看待。**要確認「是不是真的部署了」，讀 `dist/test_v100_zh/DDX_BUILD_MANIFEST.json` 的 `applied` 欄位，不要只信文件敘述。**

### 標準全量重建＋部署指令

```bash
python tools/text/ddx_rebuild_all.py --manifest dist/test_v100_zh/DDX_BUILD_MANIFEST.json
```

這會用 `scratchpad/pristine/`（乾淨原始 DDX）+ `localization/translated/*.json` + `localization/generated/zh_mapping.json`，把全部章節重建進 `dist/test_v100_zh/`，全部驗證過才會真的覆蓋（all-or-nothing）。字庫要重建才需要另外跑 `build_font.py --from-translations`（見上方「關鍵原始碼位置」）。

## 重要教訓／踩過的坑（不要重踩）

1. **絕對不要把補丁檔案複製進 `betrayal-at-krondor/`（真正的原始遊戲資料夾）**。之前的教訓：舊版設定檔直接掛載原始遊戲資料夾又執行複製指令，把 `krondor.exe` 永久覆寫掉了，已從乾淨封存檔還原過一次。現在改成掛載獨立的 `dist/test_v100_zh/`，原始遊戲資料夾應保持完全不動。
2. **DDX record 修改要維持原始 byte 長度**（同長度 padding），除非你有把握處理好 offset 連鎖影響。DDX 的 opcode 可能用絕對 offset 定址，改變某個 record 長度會讓後面所有 record 的 offset 錯位，導致播放邏輯跳到錯的地方（實測撞過）。
3. **手刻二進位補丁的位址風險極高**——舊版做法位址從未在真正執行時驗證過，加上漏改一個函式，導致 CPU 卡死在無窮迴圈。現在的作法（改 C 原始碼、用真工具鏈編譯）完全避開這類風險，遇到新需求優先考慮改原始碼，不要回頭手刻機器碼。
4. **老 DOS 繪圖函式完全不做邊界檢查**：任何對 `applied[]` 這類座標／尺寸做加減的修改，都要先確認結果不會變負值或超出畫面範圍，否則座標算歪可能寫壞任意記憶體（2026-08-25 撞過一次螢幕整片雜訊，見 archive §16.6）。
5. **一個功能可能有好幾條平行的顯示路徑**：中文對話目前已知至少三套獨立機制（`dialog_play_record()` 節點圖、`dialog_show_by_key()`、`TTMDLG.C` 的 `ttmscript_show_dialog_action()`），同一類 bug（例如「沒有分頁邏輯」）可能要在每一條路徑分別修，不要修好一處就假設全部路徑都好了（archive §16.3 就是先修錯路徑、繞了一圈才找到真正的呼叫點）。
6. Bash 工具的 cwd 會在 `cd a && cd b` 這種複合指令後**跨呼叫持續存在**，容易不小心卡在子目錄裡，下指令前如果不確定就先 `pwd` 確認。
7. **`build_font.py` 只自動收錄特定 Unicode 區段的字元**（`glyphs_from_translations()`：CJK 統一表意文字 `0x4E00`–`0x9FFF`、CJK 標點 `0x3000`–`0x303F`、全形符號 `0xFF00`–`0xFFEF`，加上單獨列舉的破折號／刪節號），**落在區段外的字元會被靜默跳過、不報錯、也不會反映在 `+N` 差異數字裡**。2026-08-26 部署 `DIAL_Z19` 前重新掃描才發現三個既有漏洞：`DIAL_Z00`／`DIAL_Z19` 用來分隔西方人名音譯的間隔點（分別是 `‧` U+2027 跟 `·` U+00B7，兩個都在區段外）從來沒有對應字模；`DIAL_Z13`／`DIAL_Z22` 有一處「高䠷」的「䠷」（U+4837，落在 CJK 擴充 A 區，同樣在區段外）明顯是「高挑」的「挑」（U+6311）誤植。前者比照 `DIAL_Z17` 當時處理片假名間隔點 `・`（U+30FB）的既有慣例，直接把間隔點字元整個拿掉（不補字模）；後者是單純的錯字，改成正確的字即可。**教訓：`build_font.py` 印出來的 `Generated N glyphs (+M vs. existing mapping)` 只能證明「這次新掃到的字都補上了」，不能證明「所有翻譯用到的字都在字庫裡」——部署前務必另外寫一支腳本，把所有 `localization/translated/*.json` 的 `translation` 欄位掃過一遍、逐字元比對 `zh_mapping.json` 的 `char_to_id`，才能抓到這種「字元本來就不在收錄範圍內」的漏洞。**

## 完整歷史

逐 session 的詳細敘事（每個 bug 的根因調查過程、修法、教訓、翻譯內容摘要）都在 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md)，章節對照：

- §1：Phase 5 完成（雙位元組偵測、換行、混排等基礎中文渲染）。
- §5～§5.4：Phase 6 DDX 翻譯 pipeline 建立、第一批章節翻譯、EMS 字庫容量瓶頸、換行編碼避碰、BOK 書籍系統前置調查。
- §6～§7：Phase 8 文字介面盤點、角色屬性面板中文化＋小字級字型。
- §8～§8.5：`DIAL_Z00` 翻譯、字庫編號穩定性 bug、`TEXTWRAP.C` 無號數下溢 bug、章節橫幅卡死與撿屍體閃退（皆已解決）。
- §9～§9.8：新章節翻譯、`OBJINFO.DAT` 物品名稱系統、UI 硬編碼字串、物件貼圖雜色 bug。
- §10～§11：撿屍／物件說明停住、戰鬥後升級訊息空白死機（皆 RESOLVED）。
- §12～§15：逐次翻譯 session（`DIAL_Z06`／`Z21`／`Z14`／`Z13`／`Z27`／`Z22`／`Z23`），含 DOSBox-X MCP 除錯工具設定、逐字元樣式排版工具、`DIAL_Z16` 既有 token-mismatch bug 修正。
- §16：2026-08-24~25 這輪——補完真正的部署、`#Name#` 標題解析截斷、兩處分頁邏輯缺口（`ttmscript_show_dialog_action()`／`dialog_show_by_key()`）、標題橫幅蓋內文、多餘空行、螢幕雜訊迴歸，以及還沒解決的分頁孤兒行問題。
