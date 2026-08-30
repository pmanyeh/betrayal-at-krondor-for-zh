# Text Surface Inventory (Phase 8)

## 0. 文件目的與範圍

本文件依據 [`Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`](file:///d:/git/betrayal-at-krondor-for-zh/Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md) 第 14 節（Phase 8 — Text Surface Inventory）的規範產出，目的是盤點遊戲內**所有**會顯示文字給玩家看的子系統，讓後續翻譯／工程排程不會遺漏任何一塊。

調查方法：在 `upstream/betrayal-at-krondor/bak/SRC/` 全樹搜尋字串常數、`sprintf`/`printf` 呼叫、資源載入函式（`res_fopen`/`res_fread_far`）、以及所有文字繪圖函式（`font_draw_text_far`/`font_draw_text_ds`/`font_render_glyph_or_ctrl`）的呼叫鏈，逐一回溯每個介面的文字最終來源與繪圖路徑。不含程式碼修改或翻譯，純研究。

Phase 6（DDX 對話）與 Phase 7（BOK 書籍）已各自有獨立文件（見 [`ddx-resource-specification.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/research/ddx-resource-specification.md) 與 §1/§2 下方摘要），本文件將它們一併收錄以求完整，但細節不重複展開。

---

## 1. 總體結論

全遊戲的文字系統可分成三條路徑：

1. **DDX 對話系統**（`SRC/DIALOG/DIALOG.C`）——`KRONDOR.RMF` 內的 `DIAL_Zxx.DDX` 檔，Phase 6 已建立完整 extract/translate/pack pipeline。
2. **BOK 書籍系統**（`SRC/UI/BOOKTEXT.C`）——`krondor.001` 內的 `Cxx.BOK` 私有二進位格式，Phase 7 前置調查已完成（見 §3）。
3. **MenuPage / NamedTable / DialogWidget 資源系統**（`SRC/UI/MENUPAGE.C`、`NAMEDTBL.C`、`DLGWIDG.C`）——大量 `*.dat` 檔（`req_opt0.dat`、`spells.dat`、`cred.dat` 等數十個），涵蓋主選單、存讀檔、法術選單、戰鬥選單等**幾乎所有按鈕/選單標籤**。這條路徑先前完全沒有文件記錄，是本次盤點最主要的新發現。

**⚠️ 重要澄清（原盤點遺漏，經玩家實機截圖發現後補上）**：「DDX 對話系統已完成」**不等於**「對話畫面裡的所有文字都已涵蓋」。對話畫面下方的「話題詢問選單」（`<角色> asked about:` + `Nearest Town`／`Inns`／`GoodBye` 等按鈕格，見 §4a）是**第四條獨立路徑**，資料來源是另一個資源檔 `KEYWORD.DAT`，DDX pipeline 完全碰不到它。往後凡是提到「對話已支援中文」，指的僅是 DDX 本文與 `#Name#`/`@` token，**不包含話題選單按鈕**。

此外還有**大量硬編碼於 C 原始碼的字串常數**（`INVENTOR.C`、`INVINSP.C`、`CHARSCRN.C`、`ENCAMP.C`、`TOWNSCN.C`、`COMBAT.C`、`CACTOR.C` 等），可直接編輯原始碼處理，不需要新工具。

**渲染引擎結論**：不論走哪條路徑，最終繪圖呼叫幾乎全部收斂到 `font_draw_text_far`／`font_draw_text_ds`（`FONT.C`，已支援雙位元組中文）或其薄包裝（`textwrap_draw_aligned`、`invui_draw_text_aligned_shadow`、`uiwidget_draw_text_shadowed[_dflt]`）。**`BOOKTEXT.C`（BOK 書籍）是目前唯一繞過此路徑、需要額外引擎改動才能支援中文的子系統**，本次盤點沒有發現第二個這樣的例外。

---

## 2. DDX 對話系統（Phase 6，已完成基礎設施）

- **SOURCE**：`KRONDOR.001`／`KRONDOR.RMF` 內的 `DIAL_Zxx.DDX`（32 個章節檔）。
- **FORMAT**：`DDXRecord` 定長標頭 + `DdxChoice`/`DdxOp` 陣列 + 變長文字本文，見 [`ddx-resource-specification.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/research/ddx-resource-specification.md) §1。
- **EXTRACTABLE**：是——`tools/text/ddx_extract.py`。
- **PACKABLE**：是——`tools/text/ddx_pack.py` + `tools/text/ddx_translate.py build`。
- **RUNTIME PATH**：`DIALOG.C: dialog_render_text_with_tokens()` → `font_draw_text_far()`。
- **CHINESE READY**：是（Phase 5 完整驗證：雙位元組偵測、自動換行、置中/靠右對齊、混排、異常序列皆已修正）。
- **STATUS**：DIAL_Z01（40 筆）＋DIAL_Z16（211 筆）＋DIAL_Z18（364 筆）共 615 筆已翻譯；其餘 29 個章節檔已 `scaffold`，共 5,932 筆待翻譯。

---

## 3. BOK 書籍系統（Phase 7，全部 22 章已翻譯部署；C11 實機驗收過，其餘 21 章待實機看）

- **SOURCE**：`krondor.001` 內的 22 個 `Cxx.BOK` 章節書籍檔（觸發點：`SRC/GAME/GMAIN.C: gmain_play_chapter_intro`，檔名樣板 `"C00.BOK"` + chapter/part 偏移）。
- **FORMAT**：全新私有二進位格式——`u32` 總長 + 頁面目錄 + 每頁 56-byte 頁首（文字避開矩形、圖片清單）+ 帶控制標籤的文字流（`0xF4`=樣式區塊、`0xF1`=版面區塊、`0xF3`=保留 no-op、`0xF0`=結束符）。共用資源：`BOOK.FNT`／`BOOK.SCX`／`BOOK.BMX`／`BOOK.PAL`。
- **EXTRACTABLE**：是。`tools/text/bok_extract.py`／`bok_extract_pristine.py` 已完整解析內部結構（頁面目錄／頁首導覽欄位／避讓矩形／圖片記錄／控制標籤文字流）。
- **PACKABLE**：是。`tools/text/bok_pack.py`（＋`bok_rebuild_common.py`／`bok_translate.py` scaffold/build pipeline，跟 DDX 對稱）。BOK 導覽靠邏輯頁號不靠檔案 offset，所以中文變長／變短都行，packer 會重算頁 offset 表與檔長 header。全 22 個原版 BOK round-trip 位元組完全一致。
- **RUNTIME PATH**：`BOOKTEXT.C` 自己刻的逐 byte 排版/換行/齊行邏輯（`booktext_draw_glyph_kerned`／`booktext_layout_rndr_one_line`／`booktext_compute_justify_spacing`／`booktext_render_line_aligned`），**繞過** `font_draw_text_far()`。
- **CHINESE READY**：**是**（upstream commit `b066d52`）。那三個 byte-walk 迴圈已加 `0x80`–`0xDF` 雙位元組配對支援，繪圖走 `font_draw_zh_glyph()`（新增 `booktext_draw_zh_pair_kerned()` helper）；ASCII 書本文字不動、仍用 `BOOK.FNT`；`VMCODE.OVL`／`SX.OVL` 維持 byte-identical。
- **STATUS**：**全部 22 個 `Cxx.BOK`（294 筆文字 run）已翻譯部署**（`localization/translated/BOK_C*.json`、`bok_rebuild_all.py` 批次重建、`dist/test_v100_zh/BOK_BUILD_MANIFEST.json`）。**C11 在 DOSBox-X 實機驗收通過**——齊行／換行／段距／全形標點／翻頁都正常；其餘 21 檔尚未實機看過。剩：(1) 21 檔實機驗收；(2) 左上角放大首字圖——設計決定已定為「重繪成中文首字點陣圖」，需另寫 `BOOK.BMX` 影像 codec（目前中文首字留在文字流裡，圖仍是英文燙金字母）；(3) CJK 行首標點避頭尾未做（與 DDX 同一引擎層限制）。細節見 `HANDOFF.md`。

---

## 4. MenuPage / NamedTable / DialogWidget 資源系統（MenuPage 玩家可見部分已完成；NamedTable／DialogWidget 未動）

涵蓋主選單、存讀檔、Options、片尾名單、法術選單、戰鬥行動選單、城鎮/地圖選單等幾乎所有按鈕與選單標籤。**先前懷疑「主選單是預渲染圖片」的推測已被排除**——確認是真正的文字資源，只是走一套獨立於 DDX/BOK 的資源系統。

- **SOURCE**：`KRONDOR.RMF` 內數十個 `*.dat` 檔，例如 `req_opt0.dat`／`req_opt1.dat`（主選單）、`req_load.dat`＋`lbl_load.dat`（讀檔）、`req_save.dat`＋`lbl_save.dat`＋`in_save.dat`（存檔，含檔名輸入框）、`req_pref.dat`＋`lbl_pref.dat`（Options）、`cred.dat`（片尾名單）、`req_info.dat`／`req_heal.dat`（角色資訊/治療）、`InvSpell.dat`（角色已知法術清單）、`spells.dat`／`spelldoc.dat`／`req_cast.dat`（戰鬥法術選單/說明）、`combat.dat`／`shoot.dat`（戰鬥行動選單）、`req_inv.dat`／`req_inv2.dat`（物品欄操作）、`req_camp.dat`（紮營選單）、`req_gds.dat`／`req_knoc.dat`／`req_chet.dat`（城鎮/公會/敲門）、`req_map.dat`／`req_fmap.dat`（地圖選單）、`req_tele.dat`（傳送彈窗）、`contents.dat`（章節目錄）、`req_puzl.dat`（密碼盤外框，見 §6）。
- **FORMAT**：自訂「字串池 + offset 修補」二進位格式，同一套手法在 `MENUPAGE.C`／`NAMEDTBL.C`／`DLGWIDG.C`／`CREDITS.C`／`CSPELL.C`／`CHARSCRN.C` 各自重複實作了一次（讀 count → 讀定長記錄 → 讀字串池 → 依 offset 修補指標）；`MenuPage` 每筆記錄約 `0x21` bytes，`DialogWidget` 記錄另含 rect/color 等欄位。
- **EXTRACTABLE**：可用既有 `bak rmf` 工具撈出原始 bytes，**內部結構解析工具尚不存在**。
- **PACKABLE**：否，需要從零開發，但因為多個檔案共用同一套手法，可望寫出一套通用 codec 涵蓋大部分檔案，比 DDX 簡單。
- **RUNTIME PATH**：最終走 `font_draw_text_far`／`font_draw_text_ds` 或其包裝函式，**已支援中文**。
- **CHINESE READY**：渲染層是；**資源層否**（需要新 parser/packer）。
- **STATUS**：
  - **✅ MenuPage（`req_*.dat`）玩家可見部分已完成**（2026-08-30，細節在 `HANDOFF.md`「遊戲選單 `req_*.dat`」一節）。通用 codec `tools/text/menupage_translate.py`（格式：`28B 檔頭含 title offset｜u16 按鈕數｜每按鈕 0x21B 含 3 個字串 offset｜u16 blobSize｜字串池`）＋`test_menupage_translate.py`。52 個 `req_*.dat`＋`contents.dat` 全掃（255 標籤／167 相異），只翻 **11 個玩家畫面共 53 標籤**（主選單／存讀檔／偏好設定／治療／物品欄分堆／傳送清單）；約 40 個場景編輯器／作弊 `req_*` 檔（`REQ_DBUG`／`REQ_GE*`／`REQ_TE*`／`REQ_ZONE`／`REQ_KNOC`／`REQ_CHET`）**掃描但不翻**。引擎：`WIDGET.C` 的 `widget_button_render_full`／`widget_draw_text_button` 包 `g_bSmallZhMode`（`upstream 0cfa32c`，全遊戲選單按鈕中文走 10×10；OVL byte-identical）。部署 11 個 loose 檔＋新 exe，manifest `MENUPAGE_BUILD_MANIFEST.json`。待實機驗收。
  - **未做**：選單大標題（背景圖）、`lbl_*.dat`（NamedTable，Preferences 設定項文字）、`contents.dat` 章名（來源在別處）、`cred.dat` 片尾、`DLGWIDG.C` DialogWidget。
- **✅ 已完成的部分——法術系統三檔**（2026-08-30，細節在 `HANDOFF.md`「法術系統翻譯」一節）：
  - `spells.dat`（45 法術名）／`spelldoc.dat`（45×7 說明列）／`InvSpell.dat`（6 系別面板法術書清單）已用新工具 `tools/text/spell_translate.py`（`scaffold`／`status`／`build`）全部翻譯部署為 `dist/test_v100_zh/` 底下的 loose 檔（manifest：`SPELL_BUILD_MANIFEST.json`）。這三檔各有自己的格式（**不是** MenuPage 的 `0x21`-byte 記錄格式），`spell_translate.py` 各別處理。
  - `spell.dat`／`req_cast.dat` 掃過確認**無可見文字**（純版面／熱區），不需翻譯。
  - 引擎：`CSPELL.C` 的戰鬥施法面板（`cspell_list_draw_castable`／`cspell_info_panel_show`）比照 `ASKABOUT.C` 加 `g_bSmallZhMode` 小字化，並中文化三行硬編碼 Cost/Damage/Health-Stamina（`upstream f4cd826`）。後續 `CBENC.C`（觀察敵人屬性擲骰面板）＋`COMBAT.C`（三個 `combat_arena_*` 底部 HUD 面板：近戰面板、遠攻/施法瞄準面板）同樣加 `g_bSmallZhMode` 並中文化其硬編碼標籤（`upstream 1993e61`／`46d03e2`，OVL 全程 byte-identical）。角色資訊畫面的「法術」按鈕另由平行工作處理（`upstream 9773c90`／`bd9d4b4`）。
  - 待實機驗收。
- **✅ 已完成的部分——`MNAMES.DAT` 怪物/敵人類型名稱表**（2026-08-30，細節在 `HANDOFF.md`「MNAMES.DAT 怪物…」一節；這是本盤點原本沒列到的第五條獨立文字路徑——不是 DDX、不是 §4 MenuPage 家族、也不是 §4a `KEYWORD.DAT`）：
  - 戰鬥「觀察敵人」講評對白內文裡的敵人名（`moredhel warrior` 等）來源。`combatenc_mnames_lookup_dest()`（`CBENC.C`）依 `creatureType` 撈字串，`DIALOG.C` case 17 展開 `@` token 塞進 `g_speaker_names[]`；每個敵方戰鬥單位的 `.name` 也是同一表。走 DDX 文字路徑（已支援中文），**不用改引擎**。
  - 格式：`u16 count｜count×u16 offset｜u16 尺寸欄｜NUL 字串池（dedup）`，64 槽（40 真名＋24 `INVALID MONSTER` 佔位）。新工具 `tools/text/mnames_translate.py`（append-only，全未翻時 byte-identical）＋`tests/unit/test_mnames_translate.py`。
  - 40 名全譯（`localization/translated/MNAMES.json`），32 個非隊員怪物名回填 `glossary.json` 新 `creature` 分類。部署 loose `dist/test_v100_zh/MNAMES.DAT`＋重建 `ZHSTAT.DAT`（926 glyph），manifest `MNAMES_BUILD_MANIFEST.json`。待實機驗收。

`SRC/UI/MENULBL.C`（`menulbl_scroll_step_and_draw`）是另一套獨立的「捲動標籤圖片」機制，透過 `blit_sprite_indirect` 逐格 blit `ImageRecord`，**不是文字繪製**，服務於 `SRC/SCRIPT/TTM.C` 劇本腳本系統的某種通用捲動元件；本次未追查其實際呼叫來源腳本，不確定是否有玩家可見的文字用途，留待後續確認。

---

## 4a. 話題詢問選單（Ask About / Keyword System，已完成資源與引擎修改）

對話畫面下方常見的「`<角色> asked about:`」話題選單格（見玩家截圖：`Nearest Town`／`Inns`／`GoodBye` 等按鈕），**不屬於 DDX 系統**，是第三條獨立的文字路徑——先前誤以為「DDX 對話系統已完成」涵蓋所有對話互動，這裡是明確的例外，補列於此。

- **SOURCE**：`KRONDOR.RMF`／`KRONDOR.001` 內的 `KEYWORD.DAT`（獨立資源檔，話題關鍵字字串表）；另有硬編碼於 [`SRC/DIALOG/ASKABOUT.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/DIALOG/ASKABOUT.C) 的固定字串 `"GoodBye"`（L310）、`"Cancel"`（L456）、`" asked about:"`（L331，跟角色名字組合成標題列）。
- **FORMAT**：檔頭是 `u16 total_size`、`u16 count`，接著 `count` 個以檔頭為基準的 `u16 offset`，最後是 NUL 結尾字串池；載入後 `askabout_keyword_table_load()` 會把 offset 就地修成絕對指標。原檔共 346 槽，包含空槽與共用字串。
- **EXTRACTABLE / PACKABLE**：是。`tools/text/keyword_translate.py` 提供 `scaffold`／`status`／`build`，重建時保留穩定的一基索引、空槽與重複字串語意，並檢查檔長、offset、NUL 結尾及 source drift。單元測試在 `tests/unit/test_keyword_translate.py`。
- **RUNTIME PATH**：話題按鈕清單透過 `askabout_menu_page_run_selection()`（L459 起）／`menupage_draw_entries()` 繪製——與 §4 MenuPage 家族**共用同一套繪圖函式**，最終仍是 `font_draw_text_ds`。
- **CHINESE READY**：是。`localization/translated/KEYWORD.json` 已翻譯 171 個話題、36 個通用對話選項，以及 47 個 runtime 發言者姓名（槽 300–346）；純數字段維持原資料。`ASKABOUT.C` 的 `GoodBye`／`Cancel`／標題後綴也已改為「道別」／「取消」／「詢問：」。
- **小字型**：`ASKABOUT.C` 只在話題格與 DDX 選擇按鈕的寬度計算、初繪、按下與重繪期間啟用 `g_bSmallZhMode`，中文固定走 10×10 `ZHSTAT.DAT`；標題泡泡與對話本文不受影響。upstream commit `5bc1574` 已用 WSL2/Borland 工具鏈重編並部署（`KRONDOR.EXE` 458128 bytes；兩個 OVL byte-identical），待實機畫面驗收。
- **標題泡泡小字型**：後續 upstream commit `29a3751` 把 `g_bSmallZhMode` 的 save／set／restore 放進共用 `dialog_draw_speech_bubble()`，因此 Ask About 標題、DDX `#title#`、runtime 人名與城鎮標題都走 10×10 中文字，來源是否硬編碼已無差別。`build_small_font.py --ddx-title-dir` 收 DDX `#title#` 與明確標記使用 10×10 的章節面板，另以 `CHARACTER_NAMES.json` 收六名隊員名字；修正章節頁漏字及補齊 47 名 runtime speaker 後，小字庫為 797 glyphs／17544 bytes。新版 EXE 458144 bytes，兩個 OVL byte-identical。

---

## 4b. 大地圖城鎮標籤（`fmap_twn.dat`，已完成翻譯＋一行引擎修正）

呼應 §9 原先列為待確認的開放項目，已追查完成：世界地圖（`FMAP.C`）上顯示的城鎮名稱標籤，來源是另一個獨立資源檔 `fmap_twn.dat`，同樣不屬於 DDX，也不是 §4 的 MenuPage 系列（沒有共用同一個 loader）。

- **SOURCE**：`KRONDOR.RMF` 內的 `fmap_twn.dat`，由 [`SRC/SCREENS/FMAP.C:227`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/FMAP.C#L227) `fmap_twn_load()` 讀取。
- **FORMAT**：檔頭 `地圖寬(u16)/地圖高(u16)/熱區寬(u16)/熱區高(u16)/城鎮數(u16)`，接著每筆城鎮記錄依序是 `字串長度(u16) + 字串本文 + X座標(u16) + Y座標(u16)`——**沒有 offset 表**，比 §4a 的 `KEYWORD.DAT` 更簡單，是純序列式的長度前綴字串。
- **EXTRACTABLE / PACKABLE**：是——`tools/text/fmap_translate.py`（`scaffold`／`status`／`build`，比照 `mnames_translate.py`；每筆記錄改寫 `字串長度` 即可，全未翻時 byte-identical）。單元測試 `tests/unit/test_fmap_translate.py`。
- **RUNTIME PATH**：`FMAP.C:160/183/193` 呼叫 `font_draw_text_ds`／`font_text_width_ds`，與其餘介面共用同一套已支援中文的繪圖/量測函式。
- **CHINESE READY**：是。
- **STATUS**：**已完成**（2026-08-30）。33 個城鎮名全譯（`localization/translated/FMAP_TWN.json`，32 個沿用 glossary `place` 譯名），部署 loose `dist/test_v100_zh/fmap_twn.dat`（manifest `FMAP_TWN_BUILD_MANIFEST.json`）。另需一行引擎修正（`upstream 229ece5`，`FMAP.C`：`g_wFmapLabelRectH` 下限拉到 17，讓 hover 切城鎮時的 label-erase 矩形蓋得住 16px 中文字，否則會殘影；OVL byte-identical）。右下角「Exit」按鈕是 `req_fmap.dat`（§4 MenuPage 家族），不含在內。待實機驗收。

---

## 4c. `OBJINFO.DAT` — 物品名稱（新發現，已完成基礎設施＋翻譯）

§10 先前把「item names/descriptions」標成已盤點，但當時只涵蓋了物品風味文字（DDX_Z18）跟物品欄位標籤（§5），漏掉了物品**本身的簡短名稱**（如「Long Sword」「Healing Potion」這種顯示在物品欄格子裡的名字）真正的資料來源——這次補上。

- **SOURCE**：`KRONDOR.RMF`／`KRONDOR.001` 內的 `OBJINFO.DAT`，由 [`SRC/GAME/ACTOR/ITEMTBL.C:49`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GAME/ACTOR/ITEMTBL.C#L49) `itemtbl_load()` 讀取整包 `0x2b7a`（11,130）bytes 進 `g_pItemDefTable`。
- **FORMAT**：全遊戲**最簡單**的格式——沒有字串池、沒有 offset 修補表，就是 138 筆固定 80-byte 的 `ItemRecord`（定義於 [`INCLUDE/structs.h:837`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/INCLUDE/structs.h#L837)）緊接在一起：前 32 bytes 是 NUL 補齊的 `pName`，接著是 `wFlags`／`wName_split_off`（物品欄格子內兩行斷行位置，字元索引）／傷害／價格等數值欄位。檔案結尾另有一段跟文字無關的 90-byte 小表（特殊價格用）。138 筆之後（index 0 為空、不使用）實際約 137 筆有名稱。
- **EXTRACTABLE / PACKABLE**：新增 `tools/text/objinfo_translate.py`（`scaffold`／`status`／`build`，介面比照 `ddx_translate.py`）。因為 `pName` 是**固定** 32 bytes（不像 DDX 文字變長），`build` 會檢查編碼後是否 ≤31 bytes（留 1 byte 給 NUL），超過就安全 fallback 回英文，不會截斷或溢位。
- **RUNTIME PATH**：`INVENTOR.C`／`INVINSP.C` 都是直接 `sprintf`／`invui_draw_text_aligned_shadow()` 印 `item->pName`，最終一樣走 `font_draw_text_far()`，跟其餘介面共用同一套已支援中文的引擎路徑。
- **CHINESE READY**：是。
- **STATUS**：137 筆已全數翻譯完成（`localization/translated/OBJINFO.json`），翻譯時發現不少物品名稱其實已經在 `DIAL_Z18`（物品風味文字）的譯文內文裡被直接引用過（例如「銀刺」「禁制鑰匙」「那夫沙油」「真視茶」），逐一核對後採用那些已翻好的既有譯名，並回頭修正了兩筆 Z18 沒被抓到的舊譯名不一致（Aventurine 東陵石→砂金石、Flame Root Oil 火根精油→火根油等）。
- **`wName_split_off` 處理**：這個欄位是「物品欄格子內把名字拆成兩行」用的英文字元斷點索引，換成中文後完全對不上，且中文譯名普遍比對應英文短很多（多半 2-6 個全形字），目前策略是**全部強制設回 0**（單行置中顯示），不搬用舊的斷行位置。這是實機測試前的暫定決策，需要之後在遊戲畫面裡確認物品欄格子夠不夠寬、有沒有任何中文譯名仍然被裁切或跑版，若有，屆時再針對個別過長的名稱手動加回斷行。

---

## 5. 硬編碼於 C 原始碼的字串常數（可直接沿用，無需新工具）

以下全部經 `font_draw_text_far`／`font_draw_text_ds`／`invui_draw_text_aligned_shadow` 繪製，做法與 DDX 翻譯相同——直接編輯原始碼字串即可，**已可開始，不受阻於任何工具開發**。

| 子系統 | 檔案／函式 | 範例字串 |
|---|---|---|
| 物品欄格線/金額 | [`SRC/SCREENS/INVENTOR.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/INVENTOR.C) `invui_grid_render` | `"Unavailable"`、`"%ld gold %ld silver"` |
| 物品檢視面板 | [`SRC/SCREENS/INVINSP.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/INVINSP.C) `invinspect_render_details`／`invinspect_item_flow` | `"Thrust"`、`"Base Dmg:"`、`"Accuracy:"`、`"Condition: %d%%"`、`"Tsurani"`／`"Elf"`／`"Dwarf"`／`"Human"` |
| 角色狀態列/技能名（**同時被 DDX `%s` token 共用，優先度最高**） | [`SRC/DIALOG/DIALOG.C:25`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/DIALOG/DIALOG.C#L25) `g_abStatNames[16][15]` | `"Health"`、`"Stamina"`、`"Speed"`、`"Strength"`、`"Defense"`、`"Accy: Crossbow"`、`"Lockpick"`、`"Stealth"` |
| 角色畫面其它字串 | [`SRC/CHAR/CHARSCRN.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/CHAR/CHARSCRN.C) | `"of"`、`"N/A"`、`"Ratings:"`、`"Normal"` |
| 紮營統計欄標題 | [`SRC/SCREENS/ENCAMP.C:541`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/ENCAMP.C#L541) `g_apszEncampStatColHeaders[2]` | `"Health/Stamina"`、`"Rations"` |
| 旅行/城鎮畫面 | [`SRC/SCREENS/TOWNSCN.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/TOWNSCN.C) | `"From:"`、`"To:"`、`"Cost:"`、`"Party Gold:"` |
| 戰鬥狀態提示 | [`SRC/COMBAT/ACTOR/CACTOR.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/COMBAT/ACTOR/CACTOR.C) | `"Object will be pushed."`、`"Path is blocked!"` |
| 存檔書籤標題 | `SRC/SCREENS/MAINMENU.C` `mainmenu_save_bookmark` | `"Copied Bookmark"`、`"Bookmark"` |
| 除錯/作弊選單（非正常玩家路徑，仍存在於 EXE 內） | `SRC/SCREENS/MODALSCR.C` | `"-> CHEAT CENTRAL <-"` |

- **EXTRACTABLE / PACKABLE**：不適用（原始碼字串，非資源檔）。
- **CHINESE READY**：是。
- **STATUS**：未翻譯，但無需等待任何工具開發，建議列為 Phase 8 之後第一個動工項目。注意 `g_abStatNames` 每列僅 15 bytes 緩衝，中文譯名需控制在 7 個全形字以內。

---

## 6. 特殊案例：密碼盤謎題（Cipher）— 需要設計決策，非純翻譯

- **SOURCE**：[`SRC/SCREENS/CIPHER.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/CIPHER.C) `g_apCipherDialRows`（英文字母替換式密碼轉盤資料表）。
- **RUNTIME PATH**：`cipher_menu_draw_hotkey_labels` 等逐字元透過 `font_draw_text_ds` 畫出 A–Z 字母，技術上支援中文。
- **CHINESE READY**：渲染層是，但**遊戲機制本身建立在英文 26 字母替換上**，直接把字母換成中文字沒有意義。
- **STATUS**：需要先做設計決策（保留英文字母、改拼音/注音替換、或改用其他等價機制），才能決定要不要／怎麼翻譯。不計入一般翻譯工作量。

---

## 7. 查無此功能／不需處理

| 項目 | 調查結果 |
|---|---|
| 滑鼠游標提示／tooltip | 全樹搜尋 `tooltip`/`hint` 相關符號無命中；游標只切換形狀（`screen_cursor_set_shape`），沒有文字浮窗。 |
| DOS 層級系統/錯誤訊息（磁碟/記憶體不足） | `SRC/IO/RESOURCE.C` 的 INT 24h 危急錯誤處理只回傳重試/失敗代碼給 DOS 內建常式，無自訂錯誤字串。 |
| 遊戲內「系統訊息」 | `SRC/UI/SHOWMSG.C: show_message_plus_1600000` 把訊息 ID 轉發進 `dialog_play_record(id+1600000,…)`，**已經是 DDX 基礎設施的一部分**（§2），不需另外處理。 |
| 開鎖解謎（picklock）介面 | `SRC/SCREENS/PICKLOCK.C` 全程只有精靈圖動畫（`resblit_sprite`），無任何 `font_draw_text` 呼叫，純圖示小遊戲，沒有文字。 |
| 商店（shop）介面自身文字 | `SRC/SCREENS/SHOP.C` 只有喊價/計價邏輯，無 `font_draw_text` 呼叫；畫面重用 `INVENTOR.C` 物品格繪製（§5）與 DDX 對話（§2），不引入新文字來源。 |

---

## 8. 隊伍角色名字（2026-08-27 已完成翻譯）

- **SOURCE**：`GameState.characterNames[6][10]`，從 `TEMP.GAM`／`STARTUP.GAM` 用 `gstate_temp_file_read_at` 把整個 `GameState` 結構當一塊記憶體 blob 直接讀進來（`SYS/BOOT.C`／`GAME/STATE/GSTATE.C`）。**原始碼裡沒有任何字串常數**——`Locklear`／`Gorath`／`Owyn`／`Pug`／`James`／`Patrus` 這幾個 ASCII 名字完全不在 `KRONDOR.EXE` 裡，是純遊戲資料。
- **格式來源已查明**：原始未修改遊戲資料夾 `betrayal-at-krondor/startup.gam` 就是這份「新遊戲」範本，六個角色名字固定從 offset 159 起、每個 10-byte 一個欄位、依 `CharacterId` 順序（`GMAIN.H`）排列，NUL 補滿到 10 bytes；`TEMP.GAM`（執行期存檔／續存 swap file）與所有 `SAVE*.GAM` 存檔都是同一份 `GameState` 佈局的複本（只是 offset 因額外 header 而不同，例如某次遊玩中的 `TEMP.GAM` 是 offset 59），用同一個固定 ASCII 名字＋NUL 的位元組樣式即可可靠地動態定位，不需要寫死絕對位址。
- **渲染路徑已確認相容中文，不需改引擎**：這個欄位有兩個顯示路徑——駐紮營地角色名單畫面（`SCREENS/ENCAMP.C` 的 `font_draw_text_ds`）跟對話發言者標籤（`DIALOG.C` 透過 `strcpy` 複製進 `g_speaker_names[6][32]`）——兩者最終都會走到 `font_draw_text_far()`，也就是全遊戲 DDX 文字共用的同一支渲染函式，`c >= 0x80 && c <= 0xDF` 判斷雙位元組中文 lead byte 的邏輯本來就在，完全不用額外修改。另外 `DIALOG.C` 裡有一段依 `g_speaker_names[idx][0] == 'A' || == 'O'`（英文冠詞 a/an）跟名字最後一個字母是否為 `h`/`y`（英文複數/所有格變化）的舊有文法邏輯，因為中文編碼的 lead/trail byte 值永遠不會等於這些 ASCII 字母，這段邏輯對中文名字會自然跳過、不會誤觸發，不需要處理。
- **編碼驗證**：六個詞彙表既有譯名（洛克利爾／戈拉斯／歐文／帕格／詹姆士／派特魯斯，2 bytes/字 + 1 byte NUL 終止）全部落在 9 bytes 以內，舒服塞進既有的 10-byte 欄位，不需要放大結構體、不影響其後欄位的 offset。
- **STATUS**：已完成。新增工具 `tools/text/patch_character_names.py`（動態搜尋原始 ASCII 名字＋NUL 樣式定位欄位、驗證欄位內容跟長度、原地替換成中文編碼＋NUL 補滿，檔案總長度不變），已套用到 `dist/test_v100_zh/startup.gam`、`TEMP.GAM`，以及 `GAMES/` 底下全部既有測試存檔（共 40 個檔案），修改前的版本備份在 `scratchpad/gam_backup_pre_hero_names/`。**原始未修改的 `betrayal-at-krondor/startup.gam` 完全沒有被動到**，符合「絕不修改原始遊戲資料夾」的鐵律。尚未在實機（DOSBox-X）上驗證顯示效果，見 `HANDOFF.md`「待處理」。

---

## 9. 待確認的開放項目

- ~~大地圖城鎮名稱標籤~~ **已確認**：來源是獨立資源檔 `fmap_twn.dat`，見 §4b。
- **`MENULBL.C` 捲動標籤機制的實際呼叫場景**：機制本身已確認——`TTM.C` 腳本系統的通用「捲動貼圖」opcode（`0x1051`／`0xf02f`／`0xb000`／`0xb013`），`pAhPagedImage[slot] = resblit_load_asset_table(腳本內指定的檔名, 2)` 載入**預先渲染好的圖片素材**，`blit_sprite_indirect` 逐格貼圖，**確認是圖片、不是文字**（`font_draw_text` 系列完全沒有被呼叫）。變數命名（`g_nCreditsScrollYOffset`／`g_nCreditsMaxLabelHeight`）容易讓人誤以為是片尾名單，但片尾名單另有 `CREDITS.C`／`cred.dat` 一套獨立的真文字實作（見 §4 表格），兩者是不同機制。**唯一還沒查出的是：哪個實際場景（哪支 `.TTM` 腳本）在用這組 opcode**——`.TTM` 是封裝在 `KRONDOR.RMF`/`KRONDOR.001` 裡的資料檔（劇本位元組碼），要確認呼叫場景必須實際解出 `.TTM` 內容比對腳本裡引用的圖片檔名，屬於資料檔調查，靜態原始碼分析到此為止。若解出來發現是某段捲動的圖片化文字美術（例如遊戲開場片頭的出品公司/製作名單卡），則歸入「純圖片素材」類別，需要重繪而非翻譯。

---

## 10. Phase 8 Acceptance 對照

- [x] 已盤點 DDX dialog（§2，Phase 6 既有基礎設施）
- [x] 已盤點 BOK books（§3，Phase 7；codec＋引擎已完成，C11 試點實機驗收通過，其餘 21 章待翻）
- [x] 已盤點 UI labels（§4 MenuPage/NamedTable/DialogWidget 資源家族——**MenuPage `req_*.dat` 玩家可見部分已翻譯部署**，2026-08-30；NamedTable `lbl_*` 與 DialogWidget 未做；§4a 話題詢問選單 `KEYWORD.DAT` 已完成）
- [x] 已盤點 inventory（§5 INVENTOR.C/INVINSP.C）
- [x] 已盤點 item names/descriptions（物品風味文字＝DDX_Z18 已完成；物品欄位標籤＝§5；物品簡短名稱＝§4c `OBJINFO.DAT`，已完成翻譯，`wName_split_off` 斷行仍待實機驗證）
- [x] 已盤點 spell names/descriptions（§4 spells.dat/spelldoc.dat/InvSpell.dat）—— **已翻譯部署**（`tools/text/spell_translate.py`，2026-08-30，待實機驗收）
- [x] 已盤點 character names（§8，確認為存檔二進位欄位、暫不處理）
- [x] 已盤點 location names（§4b `fmap_twn.dat` 大地圖城鎮標籤——**已翻譯部署**，2026-08-30；其餘地名多半走 DDX）
- [x] 已盤點 combat messages（§5 CACTOR.C 硬編碼提示 ＋ §4 combat.dat/shoot.dat 選單 ＋ §4 已完成的 `CBENC.C`／`COMBAT.C` HUD 面板硬編碼標籤 ＋ `MNAMES.DAT` 怪物名稱表，後者已翻譯部署）
- [x] 已盤點 system messages（§7，證實已併入 DDX 基礎設施）
- [x] 已盤點 save/load UI（§4 req_load.dat/req_save.dat 按鈕**已翻**；lbl_load.dat/lbl_save.dat/in_save.dat 為 NamedTable，未做）
- [x] 已盤點 chapter titles（§4 contents.dat；BOK 章節開場文字見 §3）
- [x] 已盤點 image-embedded text（§3 BOK 放大首字母；§7 picklock 純圖示；§9 MENULBL.C 已確認為圖片機制，僅呼叫場景待資料檔調查）

**Gate 狀態**：本文件涵蓋 PROJECT_PLAN 第 14 節列出的全部類別，**全部完整**（location names 的城鎮標籤來源已於 §4b 確認）。唯一剩餘的開放項目（§9：`MENULBL.C` 實際被哪支 `.TTM` 腳本呼叫）屬於資料檔內容調查，不影響「文字來源盤點」本身的完整性——就算查出答案，也只會歸類到既有的「圖片素材」或「查無需要翻譯內容」分類，不會新增文字來源類別。可視為「完整中文化工具鏈完成」宣稱的前提盤點已達成，但 §4（MenuPage 資源家族）與 §3（BOK）本身的 parser/packer 工具與翻譯工作尚未開始，不代表這些子系統已可翻譯——僅代表**已知道要做什麼**。

---

## 11. 建議工程順序（給後續 Phase 排程參考）

1. **§5 硬編碼字串**——工作量小、無需新工具，可比照 DDX 翻譯經驗直接動手，`g_abStatNames` 優先度最高（跨系統影響既有 DDX 譯文）。
2. **§4 MenuPage/NamedTable/DialogWidget 資源家族**（含 §4a `KEYWORD.DAT`、§4b `fmap_twn.dat`）——需要先寫通用 codec，工程量與 DDX pipeline 相當，但格式更簡單；`fmap_twn.dat`（無 offset 表）與 `KEYWORD.DAT`（有 offset 表但單一扁平字串池）格式最簡單，適合作為此類 codec 開發的前兩個試點。
3. **§3 BOK 書籍**——新工具＋引擎改動（`BOOKTEXT.C` 雙位元組支援）＋設計決策（首字母圖片），三者缺一不可，工程量最大。
4. **§6 密碼盤**——純設計決策，不涉及翻譯工作量，可與其他項目平行處理。
5. **§9 `MENULBL.C` 呼叫場景**——資料檔調查（解 `.TTM` 腳本），優先度低，不影響其他項目排程。
6. **§7/§8**——確認不需處理，無需排入排程。
