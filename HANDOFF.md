# 交接備忘錄 (Session Handoff Memo)

**最後更新：** 2026-08-27（BOK 書籍系統：codec＋`BOOKTEXT.C` 雙位元組引擎改動＋全部 22 個章節書翻譯部署；C11 實機驗收通過，其餘 21 檔待實機看）

**這份文件刻意保持精簡，設計成每個新 session 開始前整份讀完就好。** 完整的逐 session 歷史敘事（每個 bug 怎麼定位根因、怎麼修、學到什麼教訓）都搬到 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md) 了——只有在需要追查某個舊問題的細節（例如「這個 bug 之前是怎麼修的」）時才去那份用關鍵字搜尋進去讀一小段，不需要整份讀過。**下方每次有新進度，把對應項目從「待處理」搬到別處或刪掉，不要只往後面加，保持這份文件短小。**

## 目前狀態

- **全遊戲 DDX 對話翻譯已全數完成並跑過驗證流程**：32 個 DDX 章節檔（`DIAL_Z00`～`DIAL_Z31` 全數，含先前敘述遺漏的 `Z09`／`Z16`／`Z18`／`Z25`／`Z26`／`Z28`），共 **5,931** 筆對話，加上 `OBJINFO.DAT` 物品名稱系統（137 筆）、`UI_HARDCODED.json` 硬編碼字串（55 筆）。`TEST.json`（1 筆）已翻完但**還沒打包**，缺一份乾淨的 `TEST.DDX` 可以對（見下方「待處理」）。
  - `DIAL_Z30`（2208 筆）是全遊戲最大的一批翻譯，也是收官之作——內容橫跨北衛城圍城戰備（芬恩中尉／馬丁公爵／坦尼吟遊詩人的逃兵抉擇與音樂課）、羅姆尼公會戰爭與夜鷹會謀殺案調查（米契爾．韋蘭德／傑森／銀蜘蛛與黃銅望遠鏡線索）、馬拉克十字鎮潘塔西亞人圍城與葛雷夫斯院長的真實身分反轉、錫爾登地下情報網（阿布克的開鎖教學／喬夫塔茲的銀蜘蛛情報交易）、埃奧提斯神殿治療支線（貝拉／露莎卡水靈）、戈拉斯與奧布卡（實為堂表兄弟替死）的礦坑逃脫、帕格夫人凱塔拉與馬克羅斯之書的追查，以及貫穿全篇的萊斯爾．瑞格（詹姆士失散雙胞胎）身世線。新增 70 餘個專有名詞已全數回填進 `glossary.json`。含大量 `ó`／`ñ`／`ð` 局部強調標記，其中一首完整的〈北衛城的豬〉打油詩（entry #2716）靠逐句拆解湊出跟原文一致的 69 個 `ó` 標記數量。2208 筆全部 0 個 token-mismatch fallback。**部署前的全字庫涵蓋率掃描抓到 88 個新增中文字沒收錄在字庫裡**，已用 `build_font.py --from-translations` 重新產生字庫補齊，字庫從 5503 個 ID 槽位（3293 相異字）擴充到 **5656 個 ID 槽位（3381 相異字）**。
  - `DIAL_Z20`（867 筆）是目前為止最大的一批翻譯——拉姆特／艾格利／薩斯／馬拉克十字鎮／卡瓦爾堡／北衛城／艾爾凡達等地的支線劇情大合集，劇情密度極高：圖蘭尼客棧老闆蘇馬尼的格鬥／討價還價課程、矮人礦坑（含大量口音體矮人台詞，比照 archive 既有慣例用語氣粗獷但不刻意造字的方式呈現）、薩斯地窖藏書任務、北衛城圍城前置戰備（含派特魯斯／馬丁公爵／詹姆士／洛克利爾的軍務支線）、艾爾凡達精靈王子卡林的隱匿術與十字弓教學，以及**烏格妮．科瓦利斯的追求者「納馮．杜桑多」其實是她「亡故」多年的哥哥內維爾、如今是夜鷹會頭目的重大劇情反轉**（詳見 `glossary.json` 新條目）。翻譯過程中順手修正了詞彙表一處既有誤植——`Katala` 先前誤記為托馬斯之妻，經本章對話明確證實她其實是帕格之妻（多爾根王之妻是亞葛拉蘭娜王后，兩人在此之前未被清楚區分過）。含少量 `ñ`／`ó` 局部強調標記，867 筆全部 0 個 token-mismatch fallback。新增 40 餘個專有名詞已全數回填進 `glossary.json`。**部署前的全字庫涵蓋率掃描抓到 77 個新增中文字沒收錄在字庫裡**，已用 `build_font.py --from-translations` 重新產生字庫補齊，字庫從 3216 字擴充到 3293 字。
  - `DIAL_Z31`（374 筆）是歐文／戈拉斯／詹姆士等人分頭在各城鎮／北境村落挨家挨戶探訪的支線資料表，NPC 密度全遊戲數一數二，新增近 30 個一次性小角色與地名（盧肯、塔德．奎斯托、弗拉爾．威根、蕭拉爾、戴爾希納德、丹肯營地、艾爾德角、龍尾井等），已全數回填進 `glossary.json`（見下方「其他待辦」）。含少量 `ñ`／`ð`／`ó` 局部強調標記與一段 22 字元的逐字元招牌（`á`，entry #75，湊字數對齊原文樣式位元組數），374 筆全部 0 個 token-mismatch fallback。**部署前的全字庫涵蓋率掃描抓到 115 個新增中文字沒收錄在字庫裡**（`build_font.py --from-translations` 重新產生字庫後補齊，見下方「重要教訓」），字庫因此從 3101 字擴充到 3216 字。
  - `DIAL_Z17`（152 筆）是「莫瑞德人字鎖」猜字小遊戲的資料表，跟其他章節性質不同：每筆記錄用 `#` 分三段——答案單字／候選字母轉盤表／提示謎語詩句。前兩段是 `CIPHER.C`（`cipher_puzzle_is_solved()`）逐 byte 比對的遊戲邏輯，經使用者確認後**只翻第三段的提示詩句，答案單字與轉盤字母表維持原文英文**，猜字遊戲玩法完全不變；只翻中文的部分靠 152 筆逐一人工翻譯，`\x0a`／`\x00` token 數量都跟原文對齊，`ddx_translate.py build` 驗證 0 個 fallback。
  - `DIAL_Z15`（159 筆）是主線旅途的城鎮／地點探索敘事（拉姆特、克朗多、馬拉克十字鎮、薩薩戈斯、薩斯、羅姆尼、高堡、北衛城、卡瓦爾堡、阿曼加、錫爾登、厄提斯島、賽瑟儂等），含大量地名／人名專有名詞與逐字元樣式標記（`ó`／`ñ`／`ð`，用來標示原文局部強調語氣，翻譯時比照 archive 既有慣例把標記字元原樣保留在對應中文詞前後，`\t`／`\n`／`@N`／`\x00` token 都跟原文逐一核對過，`ddx_translate.py build` 驗證 0 個 fallback）。
  - `DIAL_Z19`（362 筆）是帕格／歐文／戈拉斯一行人探索卡爾贊遺址、跟「提米里安雅七神」（達沙梵、蘇塔卡米等）逐一對話的支線，是目前為止樣式標記密度最高的一個章節：
    - 除了慣用的 `ó`／`ñ`／`ð` 局部強調標記外，這章大量出現**逐字元樣式**段落（原文每一個字元、包含空白與標點，都各自前綴一個樣式位元組 `ã`）——這是諸神說話時的「神諭」特效，用來讓引擎逐字顯示。因為 `ddx_rebuild_common.py` 的 `extract_tokens()` 把每個 `ã` 都算成獨立 token，翻譯這類段落時中文字數必須跟原文段落的樣式位元組數量**逐一對齊**，不能只求語意通順——由於中文表達同樣語意通常遠比英文精簡，實務上得靠「先翻、量字數、不夠就加古語化贅詞（『凡人啊』『不容有失』『天機難測、玄妙莫名』之類）反覆迭代湊字數」的做法逐段湊到精確長度，單一段落最長湊到 368 字元（entry #441）。
    - 另外發現一種**先前章節沒出現過的樣式標記字元 `á`（0xE1）**，用於帕格與歐文之間的「心靈感應／念力交談」段落（entry #429），處理方式跟 `ã` 完全相同（逐字元湊長度），只是換一個標記位元組。
    - 這章新增了一批專有名詞（加米娜、卡爾贊、潘納斯提安登、提米里安雅、達沙梵、蘇塔卡米、阿爾瑪洛達卡、瓦爾赫魯等），**尚未回填進 `glossary.json`**，見下方「待處理」。
    - 跟 `DIAL_Z15` 一樣，`\t`／`\n`／`@N`／`\x00` 及所有樣式標記 token 都用 `extract_tokens()` 逐筆自動比對驗證過，362 筆全部 0 個 token-mismatch fallback。
- **部署狀態**：全部 32 個章節確認部署在 `dist/test_v100_zh/`（2026-08-26 用 `DDX_BUILD_MANIFEST.json` 的 `applied` 欄位重新驗證過，不是只看文件敘述——之前一度誤判過，詳見 archive §16.1。這次驗證：32 個檔案、5,931 筆全數套用、0 個 skipped_token_mismatch、0 個 skipped_source_drift）。`dist/test_v100_zh/krondor.exe` 目前對應 upstream 子模組 commit `e3d9ef9`，含 2026-08-25 那輪修的 6 個中文專屬引擎 bug（`#Name#` 標題解析截斷、兩處分頁邏輯缺口、標題橫幅蓋內文、多餘空行、螢幕雜訊迴歸——細節見 archive §16）。`DIAL_Z30`（跟先前的 `DIAL_Z20`／`Z31`／`Z19`／`Z17`／`Z15` 一樣）尚未在實機（DOSBox-X）上實際跑過驗收，只跑過 build/validate 的離線驗證。
- 字庫 **5656 個 ID 槽位**（實際 **3381** 個相異字元），全真倚天點陣、零 fallback。詞彙表 `glossary.json` 共 **418** 筆。
- **全遊戲 DDX 對話翻譯進度：5,931 / 5,931（100%）。** 剩餘工作只剩 `TEST.json`（1 筆）的打包，見下方「待處理」。
- **BOK 書籍系統：全部 22 個章節書已翻譯部署**（2026-08-27，原本 [text-surface-inventory.md §3](docs/research/text-surface-inventory.md) 標「未動工」的一整塊，Phase 7）。C11 試點（codec＋引擎＋實機驗收）之後，其餘 21 個章節書（`C12`/`C21`/`C23`/`C31`/`C32`/`C41`/`C43`~`C46`/`C51`~`C53`/`C61`/`C63`/`C71`/`C81`/`C83`/`C91`/`C92`/`C94`）一次翻完——共 **294 筆文字 run**，`bok_rebuild_all.py` 批次重建 0 個 token-mismatch／0 個 source-drift，全數部署為 `dist/test_v100_zh/` 底下的 loose `Cxx.BOK`（manifest：`dist/test_v100_zh/BOK_BUILD_MANIFEST.json`）。部署前的全字庫涵蓋率掃描抓到 **38 個新增中文字**沒收錄，已用 `build_font.py --from-translations` 重新產生字庫（5656 → **5694 個 ID 槽位**），DDX 譯文不受影響（只 append）。`glossary.json` +6 筆（小徑／大徑法門、西境之主、預言、霍丘佩帕、王夫、統帥莫萊伍夫），共 **424** 筆。**只有 C11 在實機上跑過**——其餘 21 個章節書只跑過 round-trip／build／字庫離線驗證，尚未實機驗收（章節開場書只在對應章節轉場時觸發，需要對應章節邊界的存檔才看得到；用中途存檔無法重播）。分割 run（inline `F4` 強調區塊把一句話拆成三段，例如 C12「你真該聞聞／冬天／的味道」）翻譯時已確保重組後語句通順、強調詞完整。以下三件事仍未做：
  - **BOK 文字 codec**（`tools/text/bok_extract.py`／`bok_pack.py`／`bok_rebuild_common.py`／`bok_translate.py`／`bok_extract_pristine.py`，跟 DDX pipeline 對稱）。`Cxx.BOK` 格式已完整逆向：`u32 檔長 + i16 頁數 + 每頁 u32 blob 相對 offset + 56-byte BookPage 頁首（`Rect` + 9 個 u16 導覽欄位）+ 避讓矩形 + 圖片記錄 + `0xF1`版面(17B)／`0xF4`樣式(11B)／`0xF3`hook(3B)／`0xF0`結束 控制標籤文字流`。跟 DDX 不同，BOK 導覽全靠邏輯頁號（`wPageNumber`），不靠檔案 offset，所以中文變長／變短都行——`bok_pack.py` 會重算頁 offset 表與檔長 header。全 22 個原版 BOK round-trip 位元組完全一致（`tests/unit/test_bok_roundtrip.py` 3 個測試）。**全部 22 個 BOK 檔的文字都只掛在第一頁的文字流上，其餘頁是引擎 render 時才填的溢流承接頁**——一個檔等於一段連續文字流，總量約 48 KB 英文／294 段落。
  - **引擎改動**（`upstream/betrayal-at-krondor` commit `b066d52`，只改 `BOOKTEXT.C`，`VMCODE.OVL`／`SX.OVL` 維持 BYTE-IDENTICAL）。`BOOKTEXT.C` 自己刻了逐 byte 的排版／齊行／繪圖迴圈、從沒走過 `font_draw_text_far()`，所以只認單位元組字元跟 `0xE0`/`0xF0` 控制碼。比照 `TEXTWRAP.C`／`font_draw_text_far()` 既有做法，教它三個 byte-walk 迴圈認得 `0x80`–`0xDF` 前導＋非 NUL 後隨的雙位元組配對：齊行計數把配對當一個字、量測把配對當 16px 一個單位（每個寬字邊界都是合法斷行點，斷點記在配對粒度上，`pResumeSave` 不會切開配對）、繪圖新增 `booktext_draw_zh_pair_kerned()` 呼叫 `font_draw_zh_glyph()`。ASCII 書本文字不動（仍用 `BOOK.FNT`）。**沒有設 `g_bMixedZhMode`**（設了會讓 `font_glyph_metrics` 對 ASCII 回報 8px、但繪圖仍走 `BOOK.FNT` 比例寬度，量測跟繪圖對不上）。
  - **翻譯部署**：22 檔 294 run 全翻（`localization/translated/BOK_C*.json`），`bok_rebuild_all.py --manifest dist/test_v100_zh/BOK_BUILD_MANIFEST.json` 批次重建，全數為 `dist/test_v100_zh/` 底下的 loose `Cxx.BOK`（`res_fopen` 先找 loose 檔再翻 RMF，跟 DDX 部署同機制）。**只有 C11 實機驗收過**：DOSBox-X 開新遊戲跑到第一章開場書，14 段全數在 2 頁內正確顯示——整段內文齊行、短對話行靠左、段距、`——`／`……`／`「」`／`，` 全形標點、翻頁、退出書本接 TTM 過場都正常。其餘 21 檔（C94 = 全篇尾聲，54 段最長）尚未實機看過。
  - **行距已調高（15 → 18）**：原廠 `0xF1` 版面塊的 `nLineHeight=15`，比 16px 中文字模還矮 1px，中文書行與行糊在一起。`tools/text/bok_layout.py` 在 zh build 時把每個版面塊拉到 18（`bok_rebuild_common` 預設套用）。逐頁流動模擬確認 22 本都還塞得進原本的頁數（`C32`／`C63`／`C83` 剛好滿，實機驗收時要看最後一句有沒有被截）。實機驗過：行距舒服、世界地圖無迴歸。
  - **⚠️ 踩到雷：不能對 `.BOK` 加頁面**。`bok_layout.append_overflow_pages()` 本來想在書尾串接空白溢流頁（讓行距變高後文字不會被截），結果部署後**世界地圖（旅行畫面）出現整片彩色雜紋條**——是 world-renderer 的 palette-remap 狀態被寫壞（症狀類似 archive §9.5-9.8 那個已修好的 palette offset bug，但根因不同，尚未查明）。把備用頁還原（行距 18、頁數不變）後雜紋就消失。**結論：`spare_pages` 預設關閉（=0），`bok_pack.py` 目前只安全支援「改頁面內容／改長度」，不支援「增減頁數」。** 函式與單元測試保留供日後查根因。
  - **已知 & 待辦**（見下方「其他待辦」）：(1) 首字放大圖目前仍是英文燙金字母（互動式暫留，等 BMX codec，設計決定已定為「重繪成中文首字」）；(2) CJK 行首標點（`。」？`）未做避頭尾，跟 DDX 那條「孤兒行／孤立標點」是同一個引擎層限制，非迴歸；(3) 21 檔 BOK 尚未實機驗收（含 `C32`／`C63`／`C83` 行距 18 下最後一句是否被截）；(4) 加 `.BOK` 頁面會壞 world-render，根因未明。
  - **踩過的坑**：一開始把「開工前的 git 備份」做成把 upstream 那批**未提交的 VESA/EVG 原生 CJK POC WIP**（`video_init(9)`、`font_draw_evg_native_poc()`、`EVG.ASM`）一起 commit 進去，結果編出來的 exe 帶了 VESA POC、`VMCODE.OVL` 也 diverge。已解開：upstream 現在是 `e3d9ef9` → `b066d52`（只有 `BOOKTEXT.C`），VESA POC 退回成 working-tree 未提交狀態（原本就是這樣）。WSL 編譯 clone（`~/krondor-build`）的 VESA WIP 也還原了，且多留一份 `stash@{0}` 當保險（確認實驗沒壞後可 `git stash drop`）。**教訓：備份未提交 WIP 時，不同來源的實驗改動要分開，不要一鍋 commit。**
- **隊伍六名固定角色的名字已翻譯部署**（2026-08-27，原本 Phase 8 盤點標記「暫不處理」的 §8，見 [text-surface-inventory.md §8](docs/research/text-surface-inventory.md)）：`Locklear`／`Gorath`／`Owyn`／`Pug`／`James`／`Patrus` 這六個名字**不是 DDX/BOK 資源，原始碼裡也沒有任何字串常數**，是直接烙在遊戲資料檔（`STARTUP.GAM`「新遊戲」範本＋`TEMP.GAM`／`SAVE*.GAM` 存檔）裡的固定 10-byte／欄位二進位資料。查明來源後確認：(1) 顯示路徑（駐紮營地角色名單、對話發言者標籤）最終都走 `font_draw_text_far()`，跟全部 DDX 文字共用同一支已支援雙位元組中文的渲染函式，不需要改引擎；(2) 詞彙表既有譯名（洛克利爾／戈拉斯／歐文／帕格／詹姆士／派特魯斯）全部在 9 bytes 以內，塞得進既有的 10-byte 欄位，不需要放大結構體。新增工具 `tools/text/patch_character_names.py`（動態定位＋驗證＋原地替換，檔案長度不變），已套用到 `dist/test_v100_zh/startup.gam`、`TEMP.GAM`，以及 `GAMES/` 底下全部既有測試存檔（共 40 個檔案，修改前備份在 `scratchpad/gam_backup_pre_hero_names/`）。原始未修改的 `betrayal-at-krondor/startup.gam` 沒有被動到。**尚未在實機上驗證顯示效果**（見下方「待處理」）。

## 待處理 / 已知問題

### ⚠️ 分頁「孤兒行／孤立標點」——尚未解決

某些對話框分頁到最後一頁時，只剩極少內容甚至一個標點符號（CJK 句號「。」的點陣圖案本身就是個小圓圈，容易誤認成別的東西）孤零零佔一整頁。已知：

- 框大小是每筆 DDX 記錄各自的資料（`wOp==6` 操作碼可自訂 x/y/寬/高），但目前 `ddx_translate.py` 的翻譯 JSON 沒有把這個資訊帶出來，翻譯當下看不到某句話原文用的框有多小。
- 已嘗試把 `TEXTWRAP.C` 的分頁演算法從「貪婪填滿當前頁」改成「平均分配剩餘行數到所需頁數」，理論上任何一頁都不該只分到 1 行——**部署後實機重測，孤立標點依然重現，代表根因不在這個層次**。
- 順手修正的 `font_glyph_metrics()` 樣式控制位元組零寬度 bug 是對的、有保留，但也證實不是這次症狀的根因。
- **使用者明確表示不希望用動態調整文字框大小的方式解決**（框跟畫框的 `dialog_frame_draw()` 是分開算的兩套邏輯，同步改風險較高），這個方向先不要主動提。
- 下一步建議：比照抓分頁缺口 bug 的做法，重新加臨時 log（印 `textwrap_compute_lines()` 逐行切出來的 `lines[]` 內容跟每行實際 byte range），實機重現同一句話，直接比對 log 裡切出來的行跟畫面上看到的是否一致，先確認問題出在「算」還是「畫」。完整背景見 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md) §16.7。

### 其他待辦

1. **補齊 `TEST.json` 打包**：`bak rmf list` 裡有 `TEST.DDX`，但手上的 `scratchpad/pristine/` 快照沒包含它，需要先用 `bak rmf extract` 補一份乾淨的 `TEST.DDX` 進去，再跑 `ddx_translate.py build`。這是全專案剩下唯一還沒完成的翻譯／打包工作。
2. **既有詞彙表不一致清理**：`DIAL_Z14` 裡的「加波特男爵」應統一改成「加博特男爵」（其餘章節都用後者）。
3. **翻譯品質校對**：32 個已翻章節目前都還沒有第二人核對過，尤其樣式位元組密集／逐字元排版的段落（書信、告示、古籍引文、`DIAL_Z19` 的諸神神諭獨白、`DIAL_Z30` 的〈北衛城的豬〉打油詩）排版風險最高，建議找機會抽查。`DIAL_Z17`／`DIAL_Z15`／`DIAL_Z19`／`DIAL_Z31`／`DIAL_Z20`／`DIAL_Z30` 都還沒在實機上實際驗收（見上方「目前狀態」）——`Z17` 優先看提示詩句在猜字畫面上的排版是否正常、答案單字／轉盤字母表是否維持英文原文不受影響；`Z15` 優先看 24 個地點敘述段落跟含 `ó`／`ñ`／`ð` 強調標記的對話（例如 #60/#61/#62/#84/#100/#142/#156/#162/#163/#167）排版跟強調效果是否正常顯示；`Z19` 優先看那幾段逐字元湊出來的諸神獨白（entry #382/#383/#384/#385/#387/#388/#429/#433/#441/#465）實機顯示時逐字動畫的節奏跟斷行是否正常，以及新增的 `á`（0xE1）樣式標記（entry #429）是否跟 `ã` 一樣正確渲染；`Z31` 優先看散布各城鎮的挨家挨戶對話排版是否正常，尤其 entry #75 那段 22 字元逐字元招牌（`á`）跟 #557 波斯維奇夫人議事廳那段長對話；`Z20` 優先看北衛城圍城前置戰備那幾段長篇軍務對話（例如 #1183/#1416/#1539）跟矮人口音角色的台詞排版，以及納馮／內維爾反轉劇情那幾段（#1479-#1490）語氣是否連貫；`Z30` 優先看 entry #2716〈北衛城的豬〉打油詩實機顯示時逐句換行跟 `ó` 強調效果是否正常、entry #2053 起戈拉斯與奧布卡的重逢／逃脫長對話排版，以及 entry #1119 那段多角色連續引號對話（洛克利爾／歐文交替發言）的斷行是否正常。
4. **考慮對全部已翻章節跑一次 `ddx_rebuild_all.py` 全量驗證**，確認沒有 archive §15.2 那種「早期翻完、後來沒人再檢查」導致的舊 token-mismatch fallback 死角。
6. **BOK 21 檔實機驗收**：C11 以外的 21 個章節書只跑過離線驗證，還沒在 DOSBox-X 上看過。章節開場書只在該章轉場時觸發（`GMAIN.C: gmain_play_chapter_intro`，透過 `TTMDLG.C` 的劇本 opcode），用中途存檔重播不出來——要在對應章節邊界存檔，或用作弊選單跳章。優先看：`C94`（尾聲，54 段最長，含大量分割 run）逐頁排版；`C12`／`C83` 那幾段 inline `F4` 強調詞（「冬天」「浪漫」「那個」「意思」「別的」等）是否跟前後文接得起來、強調樣式有沒有生效；`C21`／`C63` 的長段落齊行與段距。
7. **BOK 首字放大圖改中文（設計決定已拍板：重繪成中文首字點陣圖）**：需要新寫 `BOOK.BMX` 影像 codec（IFF `BMP:INF:/BIN:/VGA:/AMG:` chunk＋BAK 專有壓縮，可參考 xbak/OpenBAK 文件），解出全部 19 張圖、只重編對應 index、用 `build_font.py` 的倚天點陣器把每章中文首字放大到約 72×80 套 `BOOK.PAL` 顏色回填；`bok_pack.py` 對應把該段文字開頭那個字移除（原文就是靠圖補首字母，中文翻譯目前把首字留在文字裡）。每章的中文首字＝該檔 `#0#0` run 開頭第一個字（例如 C11=「血」、C43/C46=「歐」、C94=「這」）。這是整個 BOK 工作剩下最大的單一新元件。
8. **BOK 行首標點避頭尾（選作）**：`BOOKTEXT.C`／DDX 兩條路徑都沒做 CJK 避頭尾，行首可能出現 `。」？`。跟「孤兒行／孤立標點」是同一層問題，若要做建議兩條路徑一起。
5. **隊伍角色名字實機驗證**：`Locklear`／`Gorath`／`Owyn`／`Pug`／`James`／`Patrus` 已翻譯部署（見上方「目前狀態」），但還沒在 DOSBox-X 實機上確認過顯示效果——優先看駐紮營地角色名單畫面跟對話發言者標籤兩處是否都正確顯示中文名字、沒有殘留英文或亂碼。

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
