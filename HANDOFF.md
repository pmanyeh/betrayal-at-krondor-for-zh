# 交接備忘錄 (Session Handoff Memo)

**最後更新：** 2026-09-02（本輪遊戲體驗改造均已由使用者實機驗收：**按住 Tab 顯示可互動熱區**、**法術分類顯示已學數量／空分類顯示「尚未學習」**、**10 槽輪替自動存檔**、**地圖顯示已發現洞穴入口記號**、**俯瞰地圖支援 WASDQE 與 T 紮營**。完整紀錄見 [`docs/research/ux-improvements-2026-09-02.md`](docs/research/ux-improvements-2026-09-02.md)。）

- **免安裝整合包架構**：`game_data/`（空，玩家把自己合法取得的 v1.00 Floppy 版遊戲檔案丟進來）＋內附的 `python-embed/`（PSF 授權可嵌入版 Python 3.12.10）＋`dosbox-x/`（GPLv2，`dosbox-x-v2026.08.02` win64）——兩者都是官方原始二進位、下載時驗證雜湊、跟原版遊戲版權無關可合法重新散布＋`installer.py`（純標準函式庫，內嵌自寫的 `bspatch_apply.py` BSDIFF4 patch-apply，不需要 `pip install`）。玩家流程：解壓整合包 → 遊戲資料丟進 `game_data/` → 雙擊「安裝中文化.bat」→ 雙擊「玩遊戲.bat」，整個資料夾可搬移。全程不散布任何原版資產或編譯好的 EXE——`build_exe_patch.py` 只發布 EXE 二進位差異補丁，`installer.py` 在使用者自己的 `game_data/krondor.exe` 上套用並驗證雜湊，版本不符會安全中止、不動任何檔案；`STARTUP.GAM` 角色名同樣是原地欄位替換，不隨附 `.GAM` 檔。`package_release.py` 從 `dist/test_v100_zh/` 的 `*_BUILD_MANIFEST.json` 抓已翻譯資源檔清單組出 74 個 loose 覆蓋檔，打包前檢查 `game_data/` 沒有夾帶真的遊戲資料（防止開發測試時不小心把原版資產包進發布 zip）。頂層新增 `LICENSE`（比照 upstream 寫法）。**完整的出包標準流程（何時該重跑哪支腳本、驗證步驟、已知地雷）見新文件 [`docs/workflows/release-packaging.md`](docs/workflows/release-packaging.md)。**
- **新手輕鬆開局存檔**（`GAMES/Plus.G01/`，`tools/release/build_starter_save.py`）：裡面兩個存檔點，`SAVE01.GAM` 起始金幣調成 1000（其餘不動）、`SAVE02.GAM` 是使用者自己另一輪遊玩的章節 1 進度（只套中文姓名 patch，金幣/進度保留原樣，已跟使用者確認是自己玩出來的、不是別人提供，沒有授權疑慮）。**踩過的雷**：第一版直接拿 `STARTUP.GAM` 改，實機讀取會閃退（`cannot load gi block` / Null pointer assignment）——`GMAIN.C: gmain_start_dispatch()` 顯示 New Game 與 Load Game 雖然都走 `savegame_read()`，但 `STARTUP.GAM` 原版只走過 New Game 路徑，缺了 Load Game 預期已存在的某些狀態（很可能是 `shared_inventory`/`ground_pile` 相關區域）。改成一律以本專案自己過去測試留下、已知能正常 Load Game 讀取的真實存檔當基準（`tools/release/starter_save_base/`），只 patch 需要的欄位，其餘原封不動。金幣欄位 offset（file offset 102、4-byte signed LE）推導與交叉驗證方式見指令碼 docstring。**這兩份存檔都還沒有實機重新驗證過**（session 當下 DOSBox-X AI bridge 沒有連線中的遊戲程序）——下次有機會請優先確認「讀取進度→Plus」兩個存檔點都不閃退、`SAVE01` 金幣顯示 1000。
- 同一時間，使用者自己修好 `patch_character_names.py` 兩個問題：(1) `zh_mapping.json` 原本用 cwd 相對路徑找，從 `tools/text/` 以外的目錄執行會 `FileNotFoundError`，改用 `__file__` 推導 repo root；(2) 外來存檔的姓名欄位在 NUL 結尾後常留有非零 stale bytes 而非全零 padding，原本嚴格驗證會拒絕，現在改成只要求「英文名＋NUL」開頭就接受、安全覆寫整個 10-byte slot。
- **踩過的坑**（皆已修好並重新驗證，細節見 `docs/workflows/release-packaging.md`「已知地雷」）：`.bat` 檔要用 CRLF（純 LF 會被 `cmd.exe` 解析器打散）；批次檔呼叫執行檔要用明確路徑（有些 Windows 機器關掉「目前目錄」隱含搜尋）；DOSBox-X 2026.08.02 版拿掉了 `cputype=486_slow`，改用 `486_prefetch`；`vendor_dosboxx.py`／`vendor_python_embed.py` 的輸出有快取，設定檔改動要靠 `package_release.py` 每次重寫才會生效，不能指望重跑 vendor 腳本。
- 已在乾淨複本上完整跑過：解壓整合包＋丟入原版遊戲檔案＋雙擊「安裝中文化.bat」＋雙擊「玩遊戲.bat」（`dosbox-x.exe` 正常啟動、無警告）＋`--uninstall` 還原，EXE／GAM／74 個資源檔都跟 `dist/test_v100_zh/` 位元組一致。**這只是工具鏈就緒，不代表翻譯本身已達可公開發布狀態**——下方「待處理」清單的實機驗收/校對項目仍待完成。先前（2026-08-30）：法術三檔／戰鬥面板／`MNAMES.DAT`／`fmap_twn.dat` 見下；**新增遊戲選單 `req_*.dat`（MenuPage 家族）**——通用 `menupage_translate.py` codec，翻 11 個玩家會看到的選單畫面（主選單／存讀檔／偏好設定／治療／物品欄／傳送清單），約 45 個場景編輯器／作弊 `req_*` 檔掃描但不翻；`WIDGET.C` 按鈕標籤改小字。`upstream dbf3288`、`krondor.exe` 458816 bytes（`MODALSCR.C` 旅店/休息畫面「隊伍金幣」行也改小字）。主線翻譯 checkpoint：`86f9d93`／`adf87e0`／`18e48ec`。主選單已實機確認中文＋不閃退。其餘皆待完整實機驗收）。先前：GoodBye 修正與 Ask About 選項翻譯／小字型已實機驗收。

**這份文件刻意保持精簡，設計成每個新 session 開始前整份讀完就好。** 完整的逐 session 歷史敘事（每個 bug 怎麼定位根因、怎麼修、學到什麼教訓）都搬到 [docs/HANDOFF_ARCHIVE.md](docs/HANDOFF_ARCHIVE.md) 了——只有在需要追查某個舊問題的細節（例如「這個 bug 之前是怎麼修的」）時才去那份用關鍵字搜尋進去讀一小段，不需要整份讀過。**下方每次有新進度，把對應項目從「待處理」搬到別處或刪掉，不要只往後面加，保持這份文件短小。**

## 目前狀態

- **2026-09-02 遊戲體驗改造已完成並實機驗收**：3D／城鎮場景可按住 `Tab` 顯示現行可互動物件角框，放開即清除；法術瀏覽器六學派圖示顯示已學數量，空分類顯示「尚未學習」；五種安全時機會輪替寫入 `GAMES\AutoSave.G99` 的 10 個自動存檔；玩家看見指定洞穴入口後，俯瞰地圖會持久顯示菱形記號；俯瞰地圖也已補齊 `W/S` 前後、`A/D` 轉向、`Q/E` 平移、`T` 紮營。現行洞穴地標目錄**只有 zone 1／shape 50 這一個入口**，不是自動辨識全部洞穴；日後可依相同目錄結構擴充。引擎最終提交 `6fcffc0`，主專案資源提交 `9b0a5f1`；100 項測試通過。現行 `KRONDOR.EXE` 466896 bytes、SHA-256 `0807073954f793b2fc3c2ad183586b883e99c5c99db07f10ec1c7bfe744dad13`。
- **WASDQE 移動後「循路前進」按鈕不刷新已修正並通過實機驗收**（2026-09-01）：成功的 W/S/Q/E 位移原本都跟方向鍵共用 `worldmove_party_attempt_move()`，並正確呼叫 `worldloop_set_flag_8b_preds()` 更新 entry 4 的 `wEnable_gate`；真正漏掉的是 WASDQE 為 raw scan code，沒有匹配 `REQ_MAIN.DAT` 的方向箭頭 action ID，因此 `menupage_run()` 不會像 UI／方向鍵輸入那樣設定 `redraw_menu=1`。按鈕內部狀態已更新，畫面卻留著舊亮暗狀態。`WORLDLP.C` 的共用 `after_move` 現改為 `redraw_menu = render_dirty = 1`，讓所有成功移動／轉向都重畫 3D 場景與按鈕列；引擎提交 `65c7985`。Borland 3.1 增量編譯成功，`KRONDOR.EXE` **461456 bytes**、SHA-256 `cad5c758d419bb1f03ffc040e4ac09836f7efc0dd233790e845c555243cb7379`，`VMCODE.OVL`／`SX.OVL` byte-identical；舊 EXE 備份為 `scratchpad/krondor_pre_road_button_refresh.exe`。bspatch **40217 bytes**、SHA-256 `579eb49663873fe241a1724a44957cc08994fea08e7f4fa0480e28d6ff6be0bd`，77 資源整合包均已重建。**使用者實機確認：以 WASDQE 操作移動、進出可循路位置時，「循路前進」按鈕會正常重新判斷並切換亮暗狀態。**
- **互動式角色法術瀏覽器已定版並通過使用者實機驗收**（2026-09-01）：進階密技「學會所有法術」先暴露原版六類法術總覽以矮英文字型行高排 16×16 中文而重疊的問題；`f12b00d` 曾先做穩定的雙行大字過渡版，之後依使用者偏好的「方案 3」完整改造 `CHARSCRN.C:charscreen_draw_spell_book_actor()`。左側六個學派圖示現在是可點選頁籤，中間逐項列出該學派已知法術，右側直接按需讀取 `SPELLDOC.DAT` 七列資料顯示標題與完整說明，不會載入戰鬥施法子系統、音效或特效資源。操作為滑鼠點學派／法術、`←/→` 換學派、`↑/↓` 換法術、`Esc` 或右鍵離開。選中法術使用深底＋原本金黃色文字與框線。右側說明保留 16×16 大中文字；`消耗／傷害／持續／視線` 各自強制分行，效果敘述前空一行，行距 20px；ASCII 改走 8×16 倚天混排，與中文垂直對齊。最終欄位配置為中間清單 clip 至 x=`0x7e`、選取框寬 `0x50`，說明由 x=`0x80` 起、寬 `0xbe`，可讓「消耗：10-15 生命／體力」維持同一行。相關引擎提交依序為 `745c684`／`ce04564`／`890ccd7`／`3c31a9f`／最終 `a15baca`；Borland 3.1 編譯成功，該版 `KRONDOR.EXE` **461472 bytes**、SHA-256 `213274e1216bf3860551c0d18ef31296bb704711a4b5d3bd9c975339aa0b0796`，`VMCODE.OVL`／`SX.OVL` byte-identical，96 項單元測試通過；之後已由上方 `65c7985` 的按鈕刷新修正版取代並完成出包。
- **兩套密技中心均已中文化，寶箱選單新增「啟動進階密技中心」，已實機驗收**（2026-09-01）：`REQ_KNOC.DAT` 八個按鈕翻成「取得 5000 金幣／取得任意物品／調整角色能力／前往下一章／治療全隊／學會所有法術／開放所有傳送地點／離開密技中心」；其中原文雖寫 `500 Gold`，程式實際增加 5000，故依真實效果翻譯。`menupage_translate.py` 新增可測試、可由 JSON 宣告的 `injected_entries` 機制，在 `REQ_CHET.DAT` 的 y=130 插入第四個 action `0x83` 按鈕「啟動進階密技中心」；點擊後 `TOWNSCN.C` 將 `g_cfgKnockKnock=TRUE` 並關閉寶箱，當次遊戲執行期間即可在 3D 行走畫面使用 `左 Alt＋右 Shift＋反引號`，不會修改 `resource.cfg`，重新啟動後恢復原設定。使用者已實機確認按鈕可啟動進階密技、熱鍵可叫出八按鈕頁面，並以「學會所有法術」完成法術瀏覽器壓力測試。`MENUPAGE.json` 現為 64 筆已翻譯標籤＋1 筆注入按鈕，小字庫重建為 **987 glyph／21724 bytes**。引擎提交 `9fc2b19`；Borland 3.1 完整編譯成功，`KRONDOR.EXE` **459040 bytes**、SHA-256 `94586a75e619474e248eb03f81b75f3add90f19beaeab72725503c8523f69569`，兩個 OVL byte-identical。`REQ_CHET.DAT`／`REQ_KNOC.DAT` 均已加入發布包（資源共 76 檔）；bspatch **38376 bytes**及整合包已重建，96 項單元測試通過。
- **角色資訊右上角狀態名稱已中文化並重編部署，待實機複驗**（2026-09-01）：`STAT.C:g_aConditionInfo[7]` 原先七個 runtime 英文狀態全部翻譯為 `Sick`→生病、`Plagued`→瘟疫、`Poisoned`→中毒、`Drunk`→酒醉、`Healing`→治療中、`Starving`→飢餓、`Near-death`→瀕死；使用者截圖中的紅字因此會從 `Near-death (100%)` 變成 `瀕死 (100%)`，百分比與紅色狀態色維持不變。`CHARSCRN.C` 只在繪製有效狀態清單時暫時啟用 10×10 小字，無狀態時的「正常」不受影響；這也避免同時存在多個狀態時，16×16 中文依原本 9px 行距互相嚴重重疊。`UI_HARDCODED.json` 新增完整 7 筆來源，小字庫重建為 **975 glyph／21460 bytes**。引擎提交 `ba90bd0`；Borland 3.1 增量編譯成功，`KRONDOR.EXE` **459072 bytes**、SHA-256 `924cdd9dd646911305a2b95faadb0707870f1539740c05da6e9bcfc05f9c741d`，兩個 OVL byte-identical。發布 bspatch（37445 bytes；SHA-256 `822b448abe00fbb8e52109ee48b250bc77554e0a63e832f7fd8bb31e82102bae`）與整合包均已重建；95 項單元測試及 3 項補丁往返測試通過。
- **物品數量選擇框已調整並重編部署，待實機複驗**（2026-09-01）：`INVINSP.C:invinspect_quantity_picker_dlg()` 的 runtime 英文已改為「給予：數量（全部）」／「無（取消）」，標題「選擇數量：」則在 `invinspect_dialog_panel_render()` 內暫時啟用 10×10 小字；按鈕與動態狀態列原本即經共用 Widget 小字路徑，故整個彈窗文字現在統一為小字。三組硬編碼 byte literal 已用目前 `zh_mapping.json` 反向解碼驗證，`UI_HARDCODED.json` 新增對應 3 筆來源；小字庫新增「予」，重建為 **969 glyph／21328 bytes**。引擎提交 `c9880a3`；Borland 3.1 增量編譯成功，`KRONDOR.EXE` **459056 bytes**、SHA-256 `6f2ebe3d5ac1980780bee3cfdf92b4d4940287a2cd8907b631ed5c139474d5d7`，兩個 OVL byte-identical。發布 bspatch（37357 bytes；SHA-256 `622d51fc27f6c89c0f8dfeb686bc07ce4465b5e97b893265e3cb1b5055531fc7`）與整合包均已重建；95 項單元測試及 3 項補丁往返測試通過。
- **神殿治療報價文案裁切已修正並通過實機驗收**（2026-09-01）：`DIAL_Z13#64`（node `1300077`）在治療介面的固定 `(20,75,280,90)` 文字框原本以 16×16 中文顯示，受下方按鈕區限制只看得到三行，導致「以你們的情……」之後整段服務費與動態價格被裁掉。此矩形／flags 組合經掃描全部正式 DDX 後確認全遊戲僅此一筆；`DIALOG.C` 現只對這個精確簽章啟用 10×10 小字，不影響一般對話。使用者已實機確認完整服務費文案與價格均可呈現。`DIAL_Z13.json#64` notes 同步標記 `10x10 Chinese font path`，重建 `ZHSTAT.DAT` 為 **968 glyph／21306 bytes**，確保完整文案均有小字字形。引擎提交 `96ee8b9`；Borland 3.1 增量編譯成功，`KRONDOR.EXE` **459040 bytes**、SHA-256 `bfdc2ef4ed633f639f92212aec3413e98b4e06371a8bdb6c919ba89a65e4dd37`，`VMCODE.OVL`／`SX.OVL` byte-identical。發布 bspatch 已重建（37499 bytes；SHA-256 `3e62cee9cc0ab2c0c223fdd0ebf0789e2d125db5d96b3246f34b8fc5fa15bb3e`），整合包已重新產生；95 項單元測試與 bspatch 3 項往返測試全數通過。舊 EXE／小字庫備份在 `scratchpad/krondor_pre_temple_heal_small.exe`、`scratchpad/ZHSTAT_pre_temple_heal_small.DAT`。
- **物品詳情「種族加成」亂碼已修正並重編部署，待實機複驗**（2026-08-31）：使用者在「精靈鎧甲」詳情畫面發現 `Racial Mod: Elf` 顯示成「種族加成：親接」。`localization/translated/UI_HARDCODED.json` 的翻譯來源原本就正確（`Tsurani / Elf / Dwarf / Human` → `圖蘭尼 / 精靈 / 矮人 / 人類`）；真正原因是 `INVINSP.C:invinspect_render_details()` 內三個種族名稱仍使用舊版 `zh_mapping.json` 的硬編碼 byte pair。依目前正式 mapping 解碼後，舊值實際會顯示成 `籃躬— / 親接 / 競人 / 人類`，所以前三項全數重新編碼，`人類` 原本正確、未動。整個 More Info 區塊的其餘硬編碼中文字串亦逐項反向解碼核對，只有這三項過期。引擎原始碼提交為 `upstream/betrayal-at-krondor` **`8e86f32`**（只改 `bak/SRC/SCREENS/INVINSP.C` 3 行）；Borland 工具鏈重編成功，`VMCODE.OVL`／`SX.OVL` 維持 BYTE-IDENTICAL。新版 `dist/test_v100_zh/krondor.exe` 為 **458816 bytes**、SHA-256 **`762aad46f36f0eee1100610a41ac946aa2ff18ee92fee039fd6faf9721b1b77b`**。發布補丁 `dist/release_v100_zh/exe_patch/krondor_v100_zh.bspatch` 已重建（36465 bytes，SHA-256 `82cdb2fb0dbc391a1f60b2c888dad407da8e92048ff3d5cb1419861465438fef`），以內建 `bspatch_apply.py` 從乾淨 v1.00 EXE 往返套用後與目標 EXE byte-identical；`tests/unit/test_bspatch_apply.py` **3 passed**。WSL 編譯 clone 的既有 VESA/EVG WIP 已完整 stash/pop 還原，Windows upstream 工作樹原有的 4 個 VESA/字型實驗修改也未被納入這次 commit。
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
- **部署狀態**：全部 32 個章節確認部署在 `dist/test_v100_zh/`（2026-08-26 用 `DDX_BUILD_MANIFEST.json` 的 `applied` 欄位重新驗證過，不是只看文件敘述——之前一度誤判過，詳見 archive §16.1。這次驗證：32 個檔案、5,931 筆全數套用、0 個 skipped_token_mismatch、0 個 skipped_source_drift）。`dist/test_v100_zh/krondor.exe` 目前 = `e3d9ef9`（含 2026-08-25 那輪修的 6 個中文專屬引擎 bug：`#Name#` 標題解析截斷、兩處分頁邏輯缺口、標題橫幅蓋內文、多餘空行、螢幕雜訊迴歸，細節見 archive §16）+ `b066d52`（BOOKTEXT 雙位元組）+ `c801185`~`15ccd73`（TOWNSCN 離開按鈕／說明翻頁），**458064 bytes，`VMCODE.OVL`／`SX.OVL` byte-identical**。`DIAL_Z30`（跟先前的 `DIAL_Z20`／`Z31`／`Z19`／`Z17`／`Z15` 一樣）尚未在實機（DOSBox-X）上實際跑過驗收，只跑過 build/validate 的離線驗證。
- 主字庫 `ZH16.DAT` **5695 glyph**（`zh_mapping.json` **3420** 個相異字元；法術 +1 `／`，戰鬥面板標籤＋怪物名的字全都已在字庫內），全真倚天點陣、零 fallback。小字庫 `ZHSTAT.DAT` **987 glyph／21724 bytes**（含神殿治療報價框、物品數量框、角色狀態及兩套密技選單）。詞彙表 `glossary.json` 共 **501** 筆（`spell` 45 筆、`creature` 32 筆）。`UI_HARDCODED.json` **88 筆**（含 CBENC/COMBAT 戰鬥面板硬編碼標籤 18 筆、物品數量框 3 筆、角色狀態 7 筆及密技標題 2 筆——改原始碼套用、不走 packer，但列進去 `build_small_font.py` 才會收字）。**`build_small_font.py` 標準來源清單現為**：`UI_HARDCODED.json`＋`KEYWORD.json`＋`CHARACTER_NAMES.json`＋`OBJINFO.json`＋`SPELLS.json`＋`MNAMES.json`＋`MENUPAGE.json`＋`--ddx-title-dir localization/translated`。**注意**：`build_font.py`／`build_small_font.py` 的預設輸出是相對路徑（`ZH16.DAT`／`zh_mapping.json`，會落在 repo 根目錄，且沒有既有 map 當 base 時會 `--fresh` 全部重編 ID），一定要帶 `--output-font localization/generated/ZH16.DAT --output-map localization/generated/zh_mapping.json`。
- **全遊戲 DDX 對話翻譯進度：5,931 / 5,931（100%）。** 剩餘工作只剩 `TEST.json`（1 筆）的打包，見下方「待處理」。
- **BOK 書籍系統：全部 22 個章節書已翻譯部署**（2026-08-27，原本 [text-surface-inventory.md §3](docs/research/text-surface-inventory.md) 標「未動工」的一整塊，Phase 7）。C11 試點（codec＋引擎＋實機驗收）之後，其餘 21 個章節書（`C12`/`C21`/`C23`/`C31`/`C32`/`C41`/`C43`~`C46`/`C51`~`C53`/`C61`/`C63`/`C71`/`C81`/`C83`/`C91`/`C92`/`C94`）一次翻完——共 **294 筆文字 run**，`bok_rebuild_all.py` 批次重建 0 個 token-mismatch／0 個 source-drift，全數部署為 `dist/test_v100_zh/` 底下的 loose `Cxx.BOK`（manifest：`dist/test_v100_zh/BOK_BUILD_MANIFEST.json`）。部署前的全字庫涵蓋率掃描抓到 **38 個新增中文字**沒收錄，已用 `build_font.py --from-translations` 重新產生字庫（5656 → **5694 個 ID 槽位**），DDX 譯文不受影響（只 append）。`glossary.json` +6 筆（小徑／大徑法門、西境之主、預言、霍丘佩帕、王夫、統帥莫萊伍夫），共 **424** 筆。**只有 C11 在實機上跑過**——其餘 21 個章節書只跑過 round-trip／build／字庫離線驗證，尚未實機驗收（章節開場書只在對應章節轉場時觸發，需要對應章節邊界的存檔才看得到；用中途存檔無法重播）。分割 run（inline `F4` 強調區塊把一句話拆成三段，例如 C12「你真該聞聞／冬天／的味道」）翻譯時已確保重組後語句通順、強調詞完整。以下三件事仍未做：
  - **BOK 文字 codec**（`tools/text/bok_extract.py`／`bok_pack.py`／`bok_rebuild_common.py`／`bok_translate.py`／`bok_extract_pristine.py`，跟 DDX pipeline 對稱）。`Cxx.BOK` 格式已完整逆向：`u32 檔長 + i16 頁數 + 每頁 u32 blob 相對 offset + 56-byte BookPage 頁首（`Rect` + 9 個 u16 導覽欄位）+ 避讓矩形 + 圖片記錄 + `0xF1`版面(17B)／`0xF4`樣式(11B)／`0xF3`hook(3B)／`0xF0`結束 控制標籤文字流`。跟 DDX 不同，BOK 導覽全靠邏輯頁號（`wPageNumber`），不靠檔案 offset，所以中文變長／變短都行——`bok_pack.py` 會重算頁 offset 表與檔長 header。全 22 個原版 BOK round-trip 位元組完全一致（`tests/unit/test_bok_roundtrip.py` 3 個測試）。**全部 22 個 BOK 檔的文字都只掛在第一頁的文字流上，其餘頁是引擎 render 時才填的溢流承接頁**——一個檔等於一段連續文字流，總量約 48 KB 英文／294 段落。
  - **引擎改動**（`upstream/betrayal-at-krondor` commit `b066d52`，只改 `BOOKTEXT.C`，`VMCODE.OVL`／`SX.OVL` 維持 BYTE-IDENTICAL）。`BOOKTEXT.C` 自己刻了逐 byte 的排版／齊行／繪圖迴圈、從沒走過 `font_draw_text_far()`，所以只認單位元組字元跟 `0xE0`/`0xF0` 控制碼。比照 `TEXTWRAP.C`／`font_draw_text_far()` 既有做法，教它三個 byte-walk 迴圈認得 `0x80`–`0xDF` 前導＋非 NUL 後隨的雙位元組配對：齊行計數把配對當一個字、量測把配對當 16px 一個單位（每個寬字邊界都是合法斷行點，斷點記在配對粒度上，`pResumeSave` 不會切開配對）、繪圖新增 `booktext_draw_zh_pair_kerned()` 呼叫 `font_draw_zh_glyph()`。ASCII 書本文字不動（仍用 `BOOK.FNT`）。**沒有設 `g_bMixedZhMode`**（設了會讓 `font_glyph_metrics` 對 ASCII 回報 8px、但繪圖仍走 `BOOK.FNT` 比例寬度，量測跟繪圖對不上）。
  - **翻譯部署**：22 檔 294 run 全翻（`localization/translated/BOK_C*.json`），`bok_rebuild_all.py --manifest dist/test_v100_zh/BOK_BUILD_MANIFEST.json` 批次重建，全數為 `dist/test_v100_zh/` 底下的 loose `Cxx.BOK`（`res_fopen` 先找 loose 檔再翻 RMF，跟 DDX 部署同機制）。**只有 C11 實機驗收過**：DOSBox-X 開新遊戲跑到第一章開場書，14 段全數在 2 頁內正確顯示——整段內文齊行、短對話行靠左、段距、`——`／`……`／`「」`／`，` 全形標點、翻頁、退出書本接 TTM 過場都正常。其餘 21 檔（C94 = 全篇尾聲，54 段最長）尚未實機看過。
  - **行距已調高（15 → 18）**：原廠 `0xF1` 版面塊的 `nLineHeight=15`，比 16px 中文字模還矮 1px，中文書行與行糊在一起。`tools/text/bok_layout.py` 在 zh build 時把每個版面塊拉到 18（`bok_rebuild_common` 預設套用）。逐頁流動模擬確認 22 本都還塞得進原本的頁數（`C32`／`C63`／`C83` 剛好滿，實機驗收時要看最後一句有沒有被截）。實機驗過：行距舒服、世界地圖無迴歸。
  - **⚠️ 踩到雷：不能對 `.BOK` 加頁面**。`bok_layout.append_overflow_pages()` 本來想在書尾串接空白溢流頁（讓行距變高後文字不會被截），結果部署後**世界地圖（旅行畫面）出現整片彩色雜紋條**——是 world-renderer 的 palette-remap 狀態被寫壞（症狀類似 archive §9.5-9.8 那個已修好的 palette offset bug，但根因不同，尚未查明）。把備用頁還原（行距 18、頁數不變）後雜紋就消失。**結論：`spare_pages` 預設關閉（=0），`bok_pack.py` 目前只安全支援「改頁面內容／改長度」，不支援「增減頁數」。** 函式與單元測試保留供日後查根因。
  - **已知 & 待辦**（見下方「其他待辦」）：(1) 首字放大圖目前仍是英文燙金字母（互動式暫留，等 BMX codec，設計決定已定為「重繪成中文首字」）；(2) CJK 行首標點（`。」？`）未做避頭尾，跟 DDX 那條「孤兒行／孤立標點」是同一個引擎層限制，非迴歸；(3) 21 檔 BOK 尚未實機驗收（含 `C32`／`C63`／`C83` 行距 18 下最後一句是否被截）；(4) 加 `.BOK` 頁面會壞 world-render，根因未明。
  - **踩過的坑**：一開始把「開工前的 git 備份」做成把 upstream 那批**未提交的 VESA/EVG 原生 CJK POC WIP**（`video_init(9)`、`font_draw_evg_native_poc()`、`EVG.ASM`）一起 commit 進去，結果編出來的 exe 帶了 VESA POC、`VMCODE.OVL` 也 diverge。已解開：upstream 現在是 `e3d9ef9` → `b066d52`（只有 `BOOKTEXT.C`），VESA POC 退回成 working-tree 未提交狀態（原本就是這樣）。WSL 編譯 clone（`~/krondor-build`）的 VESA WIP 也還原了，且多留一份 `stash@{0}` 當保險（確認實驗沒壞後可 `git stash drop`）。**教訓：備份未提交 WIP 時，不同來源的實驗改動要分開，不要一鍋 commit。**
- **隊伍六名固定角色的名字已翻譯部署**（2026-08-27，原本 Phase 8 盤點標記「暫不處理」的 §8，見 [text-surface-inventory.md §8](docs/research/text-surface-inventory.md)）：`Locklear`／`Gorath`／`Owyn`／`Pug`／`James`／`Patrus` 這六個名字**不是 DDX/BOK 資源，原始碼裡也沒有任何字串常數**，是直接烙在遊戲資料檔（`STARTUP.GAM`「新遊戲」範本＋`TEMP.GAM`／`SAVE*.GAM` 存檔）裡的固定 10-byte／欄位二進位資料。查明來源後確認：(1) 顯示路徑（駐紮營地角色名單、對話發言者標籤）最終都走 `font_draw_text_far()`，跟全部 DDX 文字共用同一支已支援雙位元組中文的渲染函式，不需要改引擎；(2) 詞彙表既有譯名（洛克利爾／戈拉斯／歐文／帕格／詹姆士／派特魯斯）全部在 9 bytes 以內，塞得進既有的 10-byte 欄位，不需要放大結構體。新增工具 `tools/text/patch_character_names.py`（動態定位＋驗證＋原地替換，檔案長度不變），已套用到 `dist/test_v100_zh/startup.gam`、`TEMP.GAM`，以及 `GAMES/` 底下全部既有測試存檔（共 40 個檔案，修改前備份在 `scratchpad/gam_backup_pre_hero_names/`）。原始未修改的 `betrayal-at-krondor/startup.gam` 沒有被動到。**2026-08-31 補修外來存檔相容性**：使用者載入別人提供的 `SAVE05.GAM` 後仍顯示英文名，實證角色名會跟著存檔保存，安裝程式只改 `STARTUP.GAM` 因而不會回溯修改既有存檔；`patch_character_names.py` 原先又把 `localization/generated/zh_mapping.json` 當成相對 cwd 路徑，從 `tools/text/` 執行會 `FileNotFoundError`，現已改由 `__file__` 推導 repo root。該外來存檔的固定欄位在英文名 NUL 結尾後留有非零 stale bytes（例如 `Locklear\x00c`），不是全零 padding；這些 bytes 不屬於 C 字串，工具驗證現改為只要求欄位開頭是「英文名＋NUL」，再安全覆寫完整 10-byte slot。已用 `SAVE05.GAM` → `SAVE01.GAM` 驗證：檔案長度同為 334605 bytes，只有 offset 159–218 的六個姓名欄位改變，姓名區塊外 0 byte 變動。**中文姓名顯示效果仍尚未在實機上驗證**（見下方「待處理」）。
- **場景畫面（村莊／寺廟／客棧／王宮…）的「離開」按鈕＋說明翻頁已完成並實機驗收**（2026-08-29，`upstream` commit `c801185`~`15ccd73`，只改 `TOWNSCN.C`，`VMCODE.OVL`／`SX.OVL` 維持 byte-identical，krondor.exe 458064 bytes）。這是使用者提的一整塊 UX 改動——起因是中文說明比英文長、一個框塞不下要翻頁，但原本點畫面沒有「翻頁」這個動作，點下方一律觸發「離開」，文本永遠看不完。做法：
  - **右上角「離開」按鈕**：畫在上緣羊皮紙（`draw_rect_filled` + `font_draw_text_far("離開")`），熱區是**整條上緣**（`0,0,320,24`），排在 menupage 的**第 0 位**（先被 hit-test，贏過任何延伸到角落的 NPC 熱區）。
  - **原本的底部「離開條」**（每個場景最後一個 actor，寬又低的矩形 `~(0,114,316,83)`）在組 menupage 熱區時用**矩形形狀**判斷丟掉（不是只看 `cKind`——王宮 `GDS2B` 的離開條是 `cKind==2`）。
  - **點「離開」＝跑那條離開 actor 的真實 dispatch**（不是寫死的 `nExitScene`）：`townscene_load` 掃描時記下該 actor 的 `index+0x80` 存進 `s_exitBarAction`，按鈕的 `wAction_id` 就設成它；左鍵點按鈕會落進既有的「啟動」分支（非右鍵「檢視」分支），照原樣播 `dwAltDialogKey`、依結果 remap `di`、再離開。王宮就是靠這個播出「不能從正門走、走下水道」那段（`DIAL_Z15` node 1500147）。ESC 也 remap 到 `s_exitBarAction`。
  - **說明翻頁改成熱區**（`wAction_id==2`，rect = 下方 `y 130..200` 整條，排在**最後**讓 NPC 熱區優先）：點文字區前進一頁、翻到底再點回第一頁；**不阻塞**，NPC／商店／旅店／離開隨時可點。翻頁在場景**淡入之後**才跑（進場時 palette 是黑的，`palette_screen_clear_black()` 會把 page2 也清黑，翻頁若在淡入前跑，除了最後一頁全是黑的）。翻頁之間用 `cga_save_rect_to_buffer`／`cga_rect_paste_from_buffer` 存/貼「乾淨說明區」快照來清舊字（重跑 idle 動畫會讓只做 ambient overlay 的場景底圖沒被重畫）。
  - 標題 `#…#` 掃描改成 CJK pair-aware（trail byte 可能是 `0x23`）。
  - **教訓**：(a) menupage 熱區 **hit-test 取第一個命中**，要贏過別人就排前面；(b) actor dispatch 分左鍵「啟動」／右鍵「檢視」兩條分支（`menupage_state_0e7c() == 2` 判斷），離開這種動作是「啟動」分支；(c) 進場淡入期間 palette 全黑，任何需要玩家看畫面的互動都要等 `palette_fade_in` 之後。

## 待處理 / 已知問題

### ✅ WASD/QE 行走操控 + Q/E 平移 + T 紮營——已實機驗收（大致）

3D 行走探索畫面的鍵盤操控。方向鍵 ↑↓←→ 全程原封不動保留，以下為新增的鍵：

| 鍵 | 掃描碼 | 動作 |
|---|---|---|
| W / S | `0x11` / `0x1f` | 前進 / 後退（`worldmove_party_attempt_move` mode 1 / 4）|
| A / D | `0x1e` / `0x20` | 左轉 / 右轉（`worldmove_apply_turn_step` 2 / 3）|
| Q / E | `0x10` / `0x12` | 左平移 / 右平移（mode 2 / 3，新增）|
| T | `0x14` | 紮營（原本掛在 E）|

- **迭代過程**：`1b2196b` WASD 等同方向鍵（實機 OK）→ `c4b9775` 加平移、當時放 A/D、轉向移到 Q/E → 使用者實測覺得「道路鎖定時 A/D 平移被忽略」在主要鍵上手感怪 → `5a1df68`（現行）把轉向換回 A/D、平移降級到次要的 Q/E。使用者已測：方向都對、帳篷圖示與 T 鍵開紮營正常。
- **引擎改動**（`upstream` 最終 commit **`5a1df68`**，改 `WORLDLP.C` + `WORLDMOV.C`）：
  - `WORLDMOV.C`：`worldmove_step_free_move()` 新增 `mode==2`→`heading + R3D_DEG(90)`（左平移）、`mode==3`→`heading + R3D_DEG(-90)`（右平移），沿用既有 `worldmove_probe_walkable_at()` 碰撞探測與位移（步長＝`g_nWorldStepSpeed`，同前進）。`worldmove_party_attempt_move()` 開頭加 `(mode==2||mode==3) && g_gameState.nWorldStepPending != 0` → `return 0`（**道路鎖定時靜默忽略平移**）。撞牆「沿牆滑行」fallback 是 `mode==1` 限定，平移撞牆＝停住＋擋住音效。
  - `WORLDLP.C` 主 dispatch：`0x10`(Q)→`worldmove_party_attempt_move(2)`、`0x12`(E)→`(3)`；`0x1e`(A) 併入 `0x4b`(←) 左轉、`0x20`(D) 併入 `0x4d`(→) 右轉；`0x12` 原本的 `encamp_run()` 整段搬到新的 `case 0x14`(T)。refusal 對白沿用既有 DDX record（左向用 `0xe1`、右向用 `0xe2`），不需新資料。
- **資源改動（已納入可重建流程）**：`REQ_MAIN.DAT` 螢幕圖示列的「紮營帳篷」圖示（entry 8）action_id 原本是 `0x12`——引擎讓圖示點擊與鍵盤捷徑共用 action_id，不改的話點帳篷會觸發 E 鍵的動作（平移右）。`localization/translated/MENUPAGE.json` 的 `action_overrides` 現由 `menupage_translate.py` 在每次選單重建時驗證原值並改成 `0x14`；`tools/text/patch_req_main_wasd.py` 保留為單檔修復工具。已部署 loose `dist/test_v100_zh/req_main.dat`（494 bytes，只差 1 byte @0x128），並納入 `MENUPAGE_BUILD_MANIFEST.json` 與發布包。改完：點帳篷／按 T→`0x14`→紮營；按 E→不 match 任何 entry→raw `0x12`→右平移。
- **`區域地圖`畫面（`MAP.C`，按 M 進入）已於 2026-09-02 補齊並實機驗收**：使用與 3D 探索相同的 `W/S` 前後、`A/D` 轉向、`Q/E` 平移及 `T` 紮營；方向鍵與滑鼠操作維持不變。`REQ_MAP.DAT` entry 8 的 action 已由 `0x12` 改為 `0x14`，由 `MENUPAGE.json` 的 action override 納入可重建流程。引擎提交 `6fcffc0`，資源提交 `9b0a5f1`。
- **hold 行為**：WASD/QE/T 走 `menupage_run` 回傳原始掃描碼那條路徑，長按靠 DOS BIOS typematic 自動重複（約 0.5s 延遲後連發），跟方向鍵的 `focused_entry`+`g_nFrameTickCountdown` 自訂連發手感略不同。使用者已接受。
- **現行編譯部署**：`dist/test_v100_zh/krondor.exe` = **466896 bytes**、SHA-256 **`0807073954f793b2fc3c2ad183586b883e99c5c99db07f10ec1c7bfe744dad13`**（引擎 `6fcffc0`）；`REQ_MAP.DAT` entry 8 已確認為 `0x14`。逐版舊備份仍保留於 `scratchpad/`；Windows／WSL 兩套引擎工作樹原有的 VESA/EVG WIP 均未納入提交。
- **還沒細驗**：站在道路上（按 R 進入單步行走）時 Q/E 平移＝沒反應（預期）；平移撞牆的擋住音效；平移方向是否 Q 左 E 右（若相反＝`WORLDMOV.C` 的 `90` ↔ `-90` 對調）。

### ✅ 神殿場景點「離開」／按 ESC 閃退重開——根因＝傳統記憶體耗盡，已修（`alloc_far` UMB 後援）

使用者 2026-08-31 測 WASD 時發現：頌恩神殿場景點右上「離開」或按 ESC，「閃退後遊戲立刻重開」（實為整台 DOS 虛擬機三重錯誤重置 → autoexec 重跑 `krondor.exe`）。**跟當天的 WASD/平移/紮營改動無關**——換回動任何操控前的 `8e86f32` exe 一樣崩潰。城鎮離開正常、只有這個神殿中獎。

**根因（逐段 on-screen 印值二分定位）**：離開任何城鎮/神殿時，世界迴圈的 `zone_refresh_visible(0)` → `zone_load_audio_proximity()` → **`czone_subsystem_init()`（`CZONE.C`）** 會用 `alloc_far()`（DOS INT 21h/48h）要一塊 `0xf308`＝**62216 bytes 的連續傳統記憶體**。中文化版累積加進的引擎程式碼（`krondor.exe` 從原版 453904 → 458928，+5KB 常駐）＋中文 DDX 記錄約英文兩倍大，讓這塊配置在**部分場景退出時剛好差 ~3KB**（實測 `largest_free=59232` vs `need=62216`）。`alloc_far` 失敗回傳 **segment 0 的假指標**（`0000:E808`，`p` 在後續 `p += 300` 迴圈裡從 `0000:0000` 走出來的），`czone_load_actors()` 透過它寫入 → 踩爛低位記憶體/IVT → VM 重置。**這是 archive §5.0／§16 記過的同一類「翻譯內容變多 → 傳統記憶體不足 → `alloc_far` 失敗」，只是這次是 czone pool 而非字庫。**

- **DOSBox 設定調校無效**：`dist/dosbox_zh_test.conf` 加 `[dos] dos=high,umb shellhigh=true` 後，`MEM` 顯示啟動時傳統記憶體已有 611K free（DOS 全在 HMA、COMMAND.COM 在 UMB）——已經是天花板，缺口是**執行期**遊戲自己吃掉的。
- **修法**（`upstream` commit **`870a87f`**，`DOSMEM.C`＋`DOSMEM.H`＋`CZONE.C`，`VMCODE.OVL`／`SX.OVL` byte-identical）：新增 `alloc_far_umb(size)`——**只在這一次呼叫**期間 link DOS UMB chain（INT 21h AX=5803h BX=1）＋設配置策略為 first-fit high-then-low（AX=5801h BX=80h），配置完立刻把兩者都還原成預設（策略 0、UMB unlink）。`czone_subsystem_init` 那行 `alloc_far(sz,0)` 改叫 `alloc_far_umb(sz)`。**其他所有配置（DDX／字型／貼圖…）完全不受影響。** 這塊 62KB 於是會先用那 ~77KB 閒置 UMB，補回缺口還有大量餘裕；`czone_cache_evict_lru_slot` 的 `_freemem` 釋放 UMB 區塊照常運作。
  - 先前有一版（`17e0f24`）是在 `main()` 開頭全域改策略——會讓別的緩衝區也跑進 UMB，實測仍有「隊伍能力提升」訊息缺字（見下），改成現在這個外科手術版後**缺字依舊**，證實缺字是既有問題、非此修法造成。
- **需搭配 conf**：`dosmem_enable_umb_alloc` 需要 host DOS 有 UMB 可 link，`dist/dosbox_zh_test.conf` 已加 `[dos]` 區塊（`dos=high,umb`）。**發布整合包（`dist/release_v100_zh/`）內附的 DOSBox-X conf 也要同步加這個 `[dos]` 區塊**，否則 UMB 後援失效、缺口 3KB 的臨界場景仍會崩——出包流程 `docs/workflows/release-packaging.md` 待補這一項。
- **部署**：`dist/test_v100_zh/krondor.exe` = **458992 bytes**、SHA-256 `fc86dd01a907a74db784962c24ccdfe27a071166d73eaf9ef5c89e17a7fb5ac7`。舊 exe 備份 `scratchpad/krondor_pre_umbfix.exe`。**使用者實機確認：頌恩神殿離開不再崩潰。** 待做：多進出幾個城鎮/神殿、正常長時間玩，確認沒有別的臨界場景。

### ✅ 「隊伍的各項能力都提升了。」訊息缺字——小字庫漏字，已補建部署

戰鬥後能力提升訊息（`DIAL_Z21.DDX#0`~`#3`，node 0x200b30-0x200b33）實機顯示成「隊伍的　　能力　提」。**不是截斷、不是 `@1` token 問題**——是小字庫 `ZHSTAT.DAT` 缺 `各`(1281)／`項`(1347)／`都`(165)／`升`(3127)／`了`(91)／`。`(8) 這 6 個 glyph，小字模式下缺字靜默顯示成空白（archive line 485 記過的坑）。

- **為什麼掉字**：archive §11 對這個訊息框（`flags=0x0014`、rect `(70,40,180,35)`、28px 可用高放不下兩行 16px 中文）強制啟用 `g_bSmallZhMode` 小字。§11 當時驗過是好的，但之後 `ZHSTAT.DAT` 為法術／怪物名／選單重建過多次，而 `build_small_font.py` 的 `--ddx-title-dir` 只抓 DDX `#title#` 正文，抓不到這個訊息的正文字，這 6 個字就掉出去了。
- **修法（純資源）**：`DIAL_Z21.json#0`~`#3` 的 `notes` 加上觸發字串「`10x10 Chinese font path`」，`chars_from_ddx_small_text()` 就會收錄這 4 筆的完整正文。重建 `ZHSTAT.DAT`：**943 → 949 glyph（20888 bytes）**，deploy 到 `dist/test_v100_zh/`。**不用重編 exe。** commit `78b54b3`。
- **教訓補充**：archive §11 只實機驗了 `#1`「隊伍的各項能力都提升了。」——但那是**在當時的小字庫來源清單下**驗的。小字庫來源清單後來變過，任何「被 DIALOG.C 強制切小字的 DDX 訊息」如果正文字沒進 `build_small_font.py` 的收字範圍，都會這樣掉字。**新的規則：凡是 DIALOG.C／ASKABOUT.C 等強制小字的 DDX 記錄，都要在 `notes` 標「10x10 Chinese font path」。**
- **待實機複驗**：DOSBox-X 已完整重啟（讓新 `ZHSTAT.DAT` 重載進 EMS）。要驗戰鬥後能力提升訊息完整顯示「隊伍的各項能力都提升了。」。含 `@1` 的 `#0`／`#2`（單一技能）順帶看 `@1`（技能名，來自 `g_abStatNames`，走 `UI_HARDCODED.json` 收字）有沒有正常。

### ✅ 對話模式 GoodBye 異常——已修復並實機驗收

根因不是 `ASKABOUT.C` 清理，而是 `ddx_pack.py` 過去漏掉 `DdxOp 0x10` 的 32-bit 對話返回位址重映射。中文改變 record 長度後，`DIAL_Z30` 的 111 個本地返回目標全指向舊位址；點 GoodBye 因此返回錯誤記錄，先出現空白人物／重複話題頁，之後才當機。packer 現已重映射 `nA1:nA2`，validator 也會拒絕未落在 record boundary 的本地返回目標；32 個 DDX 已全量重建，單元測試 66 項通過，使用者冷啟動後確認 GoodBye 正常退出。

Ask About 翻譯也已接續完成：新增 `keyword_translate.py` codec、`KEYWORD.json`（171 個話題＋36 個通用選項），部署 loose `KEYWORD.DAT`；`GoodBye`／`Cancel`／`asked about:` 改為「道別」／「取消」／「詢問：」。`ASKABOUT.C` 讓所有對話選項按鈕使用 10×10 小中文字；這一版暫時讓標題與本文維持大字。完整單元測試目前 68 項通過。使用者重新開啟 BIOS 虛擬化後，WSL2/KVM 正式重編成功（upstream commit `5bc1574`）：`KRONDOR.EXE` 458128 bytes、SHA-256 `AF01A9FE09982EA34EB42804F90A7CEE76DF118C26EDF56ACC7558C783D0FFAE`；`VMCODE.OVL`／`SX.OVL` 仍 BYTE-IDENTICAL。新版 EXE、`KEYWORD.DAT`、`ZHSTAT.DAT` 已部署到 `dist/test_v100_zh/`，待使用者實機確認畫面與點選行為。

使用者已實機確認上述選項翻譯、小字型與「道別」運作正常。接著將 `dialog_draw_speech_bubble()` 本身設為只在函式內暫時啟用 `g_bSmallZhMode`，所以同一泡泡區不論內容來自 Ask About 組字、DDX `#title#`、runtime 發言者名字或城鎮說明標題，中文都會用 10×10 小字，呼叫結束即恢復原狀，不影響正文。`build_small_font.py --ddx-title-dir localization/translated` 只擷取 115 個已翻 DDX `#title#` 的 283 個相異字，不把整篇正文塞進線性搜尋的小字庫；另新增 `CHARACTER_NAMES.json` 涵蓋六名隊員。`ZHSTAT.DAT` 現為 745 glyphs／16400 bytes。upstream commit `29a3751`，新版 `KRONDOR.EXE` 458144 bytes、SHA-256 `5C44F1F44055B999CE04CB0A524AE77E82FA2FE5E9C46AEE73BA14CEC754E47A`；兩個 OVL 再次 BYTE-IDENTICAL，69 項單元測試通過，已部署待實機驗收。

實機隨後抓到兩個字庫／資源涵蓋缺口：(1) 章節頁面是 DIAL_Z00 九筆整段使用 10×10 的特殊 panel，不是 `#title#`，先前建置器漏收而掉字；現改為同時收錄 notes 明確標記 `10x10 Chinese font path` 的完整記錄，章節 9 筆逐字檢查 0 missing，使用者重啟後確認恢復。(2) `Squire Phillip`／`Sumani` 等非 hardcode，而是 `KEYWORD.DAT` 槽 300–346 的 runtime speaker-name table；47 名已依現有 DDX／glossary 譯名全數翻譯。`KEYWORD.DAT` 現為 254 translated／0 source drift，逐槽編碼＋小字形覆蓋檢查 0 error；`ZHSTAT.DAT` 現為 797 glyphs／17544 bytes。兩項皆為資源修正，不需再重編 EXE。

### ✅ 法術系統翻譯（SPELLS/SPELLDOC/INVSPELL）＋戰鬥面板小字化——已重編部署，待實機驗收

`text-surface-inventory.md` §4「MenuPage/NamedTable 資源家族」裡的法術相關檔案，是 §4 這一整塊第一個真正動工的部分。

- **新工具 `tools/text/spell_translate.py`**（`scaffold`／`status`／`build`，一支涵蓋三檔）＋`tests/unit/test_spell_translate.py`（6 項）。三個資源檔格式：
  - `SPELLS.DAT`：`u16 count + 45×22B SpellDef（u16 pName offset + 10×i16）+ u16 長度欄位（原檔存整檔長度、引擎超額配置後 short-read，重建時照抄）+ NUL 字串池`。45 個法術名，戰鬥施法選單用。
  - `SPELLDOC.DAT`：`u16 rowCount(=45×7) + rowCount×u32 offset + u16 長度欄位 + 字串池（有共用子字串）`。每個法術 7 列：標題＋6 行說明（Cost／Damage／Duration／Line of sight／效果句）。**注意 `CSPELL.C: cspell_info_panel_show()` 會在執行期用硬編碼字串蓋掉可施放法術的第 1、2 行**（計算後的 Cost／Damage），所以那兩行的 SPELLDOC 譯文常看不到。
  - `INVSPELL.DAT`：6 個系別面板，每面板 `u16 icon + u16 count + count×(char name[24] + u16 spellIdx)`。角色資訊畫面的「法術書」清單，24B 固定名稱欄（中文需 ≤23B）。
  - `SPELL.DAT`／`REQ_CAST.DAT`：純版面／熱區，**無文字**。
- **重建策略**：`SPELLS.DAT`／`SPELLDOC.DAT` 用 append-only（原字串池位元組完全不動，只把已翻列的 offset 改指向尾端新增字串）→ 全未翻時 build 出來與原檔 byte-identical（build 內建此斷言）。`INVSPELL.DAT` 24B 欄位就地替換（比照 `objinfo`）。安全防線：SPELLDOC 每行 ≤58B、INVSPELL 名稱 ≤23B、整檔 <0x8000（避開引擎 `alloc_far((long)(int)blobLen)` 符號轉換）、source-drift 自動 fallback 英文。
- **翻譯**：`localization/translated/SPELLS.json` 398 筆——45 法術名（全譯，另回填 `glossary.json` 新 `spell` 分類 45 筆）＋188 說明列（127 筆為原版空白列，依設計留空）＋38 法術書條目（依 `spellIdx` 對應同一法術名，INVSPELL 少數英文拼法不一致如 Life Drain vs Strength Drain 一律統一）。build 0 fallback／0 source-drift。說明列走公式化對照（`消耗：1-20 生命／體力`、`傷害：3 x 消耗`、`持續：48 分鐘 x 消耗`、`視線：需要／不需`）——`×` 一律用 ASCII `x`（原文本來就是 `3 x Cost`），避開 lesson #7 的區段外靜默漏字。
- **引擎改動**（`upstream` `f4cd826`→`1993e61`→`46d03e2`，`VMCODE.OVL`／`SX.OVL` 全程 BYTE-IDENTICAL，`KRONDOR.EXE` 458768 bytes、SHA-256 `27d2119f226ccde749139e1b397f555324f81e1abbd75f098306f7bc55ebd6e4`）。統一手法：比照 `ASKABOUT.C` 在 draw 函式內 `savedSmallZhMode = g_bSmallZhMode; g_bSmallZhMode = 1; …; g_bSmallZhMode = savedSmallZhMode;`（每個 return 前都要還原），硬編碼英文字串換成中文 byte literal（含 `%d` 的用相鄰字串常數隔開，避免 `\x` 吃掉後續 hex digit；不含 `%d` 的每個 byte 都寫成 `\xNN` 即可）：
  - **`f4cd826` `CSPELL.C`**：戰鬥施法畫面 167×89 面板的 `cspell_list_draw_castable()`（可施放法術名清單、10px 行距）＋`cspell_info_panel_show()`（資訊面板、11px 行距），16px 中文會上下重疊 → 小字。三行硬編碼 `Cost: %d Health+Stamina`／`Damage: %d`／`Health/Stamina: %d of %d`（後兩者執行期會蓋掉 SPELLDOC 對應行）→ `消耗：%d 生命／體力`／`傷害：%d`／`生命／體力：%d／%d`。
  - **`1993e61` `CBENC.C`**：戰鬥中「觀察敵人」的屬性擲骰面板 `combatenc_anim_actor_stat_rolls()`（`Health:`／`Stamina:`／`Speed:`／`Strength:`／`Missle:`(原文拼錯)／`Melee:`／`Cast:`／`Defense:`，10px 行距、數值欄在 +50px），→ `生命：`／`體力：`／`速度：`／`力量：`／`弩弓：`／`近戰：`／`施法：`／`防禦：`（2 字＋全形冒號，30px，穩穩在數值欄左側）。
  - **`46d03e2` `COMBAT.C`**：三個 `combat_arena_*` 底部羊皮紙 HUD 面板——`combat_arena_hud_melee_panel()`（`Thrust`／`Swing`／`Damage`／`Accuracy`／`Left`／`Right` → `刺擊`／`揮砍`／`傷害`／`命中`／`左鍵`／`右鍵`，3 欄式：左值｜置中標籤｜右值）；`combat_arena_draw_tgt_info_hud()` 與 `combat_arena_draw_tgt_info_panel()`（施法／遠攻瞄準面板：`Choose a target`／`Accuracy:`／`Damage:`／`quarrels remaining` → `選擇目標`／`命中：`／`傷害：`／`剩餘弩箭`）。`font_text_width_ds()` 在小字模式回報 10px/字，置中／靠右計算會自動對。
- **角色資訊畫面的法術書清單後續已另行修正**：取得全部法術後，實機證明原本的 30px 面板並不能可靠容納通用換行產生的 16×16 中文；現已由 `f12b00d` 改成專用雙行大字 renderer（只在法術名稱邊界換行、逐列裁切），詳見本文件最上方「目前狀態」。角色資訊畫面的「法術」按鈕本身仍使用小字（`upstream 9773c90`／`bd9d4b4`）。
- **部署**：loose `SPELLS.DAT`／`SPELLDOC.DAT`／`INVSPELL.DAT`（`res_fopen` 先找 loose 再翻 RMF）＋`ZH16.DAT`／`ZHSTAT.DAT`＋新 `krondor.exe` → `dist/test_v100_zh/`，manifest：`dist/test_v100_zh/SPELL_BUILD_MANIFEST.json`。部署前 `dist` 的舊字庫／exe 備份在 `scratchpad/dist_backup_pre_spells/`。**尚未實機驗收**——見下方「其他待辦」。
- **編譯環境註記**：這次重編發現 WSL clone `~/krondor-build` 的 master 落後 Windows `upstream` 很多（`566e11c`，落後 33 個 commit），但是**線性落後可 fast-forward、沒有分岔**。標準循環仍可用：Windows 端 `git add <改的檔> && git commit` → WSL `git stash push -u` → `git pull --ff-only` → `uv run bak build` → 複製 `work/KRONDOR.EXE` → WSL `git reset --hard 566e11c && git stash pop`（還原成落後狀態＋那 7 個 parked WIP 檔）。WSL working tree 那 7 個未 commit 檔（`DIALOG.C`／`FONT.C`／`TEXTWRAP.C`／`DOSMEM.C`／`EMSDET.C`／`VTHUNKS.ASM`／`gfx169d.h`）＋`toolchain/` 是使用者另一條平行實驗，別動、別 commit。

### ✅ 遊戲選單 `req_*.dat`（MenuPage 家族）——玩家可見的已翻部署，編輯器／作弊選單不翻，待實機驗收

`text-surface-inventory.md` §4「MenuPage 資源家族」的主體。RMF 裡約 **52 個 `req_*.dat`＋`contents.dat`**。

- **格式**（已完整逆向，`SRC/UI/MENUPAGE.C: menupage_load`）：`28B 檔頭（file offset 18 的 u16 = title 字串在 blob 的 offset，或 0xFFFF）｜u16 按鈕數｜每按鈕 0x21B（file offset +19/+21/+23 各一個 u16：pLabel／pPrimary_label／pAlt_label 的 blob offset，或 0xFFFF）｜u16 blobSize｜NUL 字串池`。**注意 blobSize 是引擎 `res_fread` 實際要讀的位元組數，重建時要寫正確值**（跟法術檔那種「存整檔長度」的 quirk 不同）。
- **新工具 `tools/text/menupage_translate.py`**（一支吃整個 pristine 目錄、一份 `MENUPAGE.json` 涵蓋所有檔；**有翻譯的檔整個字串池重建**、未翻的檔 byte-identical——原因見下方「踩過的坑」）＋`tests/unit/test_menupage_translate.py`（5 項）。
- **範圍決策**：255 個標籤、167 個相異字串，但**絕大多數是內建場景編輯器／作弊選單**（`REQ_DBUG`＝除錯選單、`REQ_GE*`＝Game Element 編輯器、`REQ_TE1~15`＋`REQ_TE_*`＝觸發器/場景編輯器、`REQ_ZONE`、`REQ_KNOC`／`REQ_CHET`＝敲門作弊碼選單，「Trap Situation」「Movement Style」「Get: 500 Gold」「Chapter1 Yes」之類），**正常玩家永遠看不到**——這些**掃描但不翻**。實際翻的是 **11 個玩家畫面**：`req_opt0/opt1`（主選單／暫停選單）、`req_pref`（確定／取消／預設值）、`req_save`／`req_load`、`req_heal`（治療角色／下一位／完成）、`req_inv`（詳細資訊）、`req_inv2`（選擇數量：／分給隊伍）、`req_gi`（離開）、`req_info`（離開；「法術」鈕由 `CHARSCRN.C` runtime patch 負責，這裡不碰）、`req_tele`（傳送目的地清單 12 處：X神殿／方位＋取消，神名沿用 glossary）。共 **53 個標籤**。build 0 fallback。
- **引擎改動**（`upstream 0cfa32c`＋`dbf3288`）：
  - `0cfa32c` `WIDGET.C`：`widget_button_render_full()` 與 `widget_draw_text_button()` 兩條按鈕標籤繪製路徑（置中在 `rect.height/2 - 4`，按鈕高 ~15px）原本假設 ASCII 字，16px 中文會上下爆出斜角邊框——包 `g_bSmallZhMode` → **全遊戲所有選單按鈕**的中文都走 10×10。ASCII 標籤不受影響。
  - `dbf3288` `MODALSCR.C`：`modalscreen_inv_draw_gold_amount()`（旅店住宿／`modalscreen_rest_until_time` 休息確認畫面上緣那塊 party-stats 面板的「隊伍金幣 X金幣 Y銀盾」行）——標籤 16px 5 字會撞進右邊 60px 處的金額字串（實機截到糊在一起）；面板上面的欄位標題／角色名／數值本來就是小字（平行工作 `encamp_draw_party_stats` 已包），這行補上 `g_bSmallZhMode` 對齊。
  - `VMCODE.OVL`／`SX.OVL` byte-identical，`krondor.exe` **458816 bytes**（SHA-256 `16a5998caf0789c8d1599bf4af416581b7ef61bee6077f84f6aeba0afec5fe93`）。
- **翻不到的**：(1) 「Options」等**選單大標題**是背景圖 `z01l.scr` 畫死的（`pTitle`=none），要改得重繪圖檔；(2) **Preferences 裡各設定項的文字**（音量／速度…）走 `lbl_*.dat`（`NAMEDTBL.C` NamedTable 格式，另一套，未做）；(3) `contents.dat` 的章名來源在別處（該檔 10 個項目全無文字）；(4) `cred.dat` 片尾名單（未做）；(5) 大地圖右下角「Exit」鈕是 `req_fmap.dat` 但該檔那個按鈕**沒有文字欄位**（`type=3` 純 sprite），文字可能烙在圖裡。
- **部署**：11 個改過的檔以小寫檔名 loose 到 `dist/test_v100_zh/`（`req_opt1.dat` 等）＋新 exe＋`ZHSTAT.DAT`（943 glyph）。manifest：`MENUPAGE_BUILD_MANIFEST.json`。舊 exe／字庫備份 `scratchpad/dist_backup_pre_menu/`。`ZH16.DAT` 不變（111 個相異字全在庫）。
- **⚠️ 踩過的坑（已修）：MenuPage 的 `.dat` 不能用 append-only 重建**。第一版 `menupage_translate.py` 比照法術／MNAMES 用「保留原 blob、只把已翻 offset 指到尾端新增字串」——結果**一開遊戲就 `MEM:34 (Heap Corrupt!)` + Null pointer assignment 閃退**。根因：`MENUPAGE.C: menupage_free()` **不記錄字串池的 malloc 起點**，而是掃 title＋所有按鈕的三個標籤指標、取**最小值**當 `stringBlob` 基底來 `my_free()`。append-only 會把原本在 blob offset 0 的字串變成孤兒（沒有標籤再指它），於是最小指標變成 `stringBlob + N`，`free()` 一個非塊首的內部指標 → 堆積損毀，下一次 `galloc_safe_zcalloc` 的 `heapcheck()` 才報 `MEM:34`（滯後偵測，跟 archive §那次 DDX offset bug 同樣的滯後特徵）。**修法：`_build_one` 改成整個字串池重建**（已翻＋未翻全部重新排、去重），依「title→各按鈕」參照順序排，保證 offset 0 有活字串；未翻的檔走 byte-identical 快速路徑。`spell_translate`／`mnames_translate`／`fmap_translate` 不受影響——它們的引擎端是用載入時存下的指標直接 free，或逐筆 free，不做這種「掃最小指標推基底」。**教訓：新資源格式寫 codec 前，先看引擎怎麼 free 它**——如果是「從內容反推 buffer 基底」，就不能 append-only。

### ✅ `fmap_twn.dat` 大地圖城鎮標籤——已翻譯部署（含一行引擎修正），待實機驗收

旅行大地圖（`FMAP.C`）上各地點的城鎮名（`Eldpoint`／`Krondor`…）。全遊戲最簡單的文字容器：`u16 mapW／mapH／熱區W／熱區H／城鎮數` 檔頭，接著每筆 `u16 字串長度（含 NUL）｜字串本文｜u16 X｜u16 Y`——**沒有 offset 表、沒有 dedup**。`fmap_twn_load()` 依 `len` 逐筆 `galloc`＋讀取，所以名字長度自由；標籤走 `font_draw_text_ds`／`font_text_width_ds`（已支援中文、寬字回報 16px，置中與 rect 寬度自動對）。

- **新工具 `tools/text/fmap_translate.py`**（`scaffold`／`status`／`build`，全未翻時 byte-identical）＋`tests/unit/test_fmap_translate.py`（6 項）。
- **翻譯**：`localization/translated/FMAP_TWN.json` **33 個城鎮名全譯**，32 個直接沿用 `glossary.json` 既有 `place` 譯名（`Lyton` 有 place／person 兩條，取 place 的「萊頓」），只有 `Dencamp-On-The-Teeth` 是新的——地圖標籤用精簡的「世界之齒紮營地」（跟 `DIAL_Z13` 地點標題橫幅一致；`DIAL_Z31` 內文用「丹肯營地」，屬既有不一致，glossary 已加註）。build 0 fallback。
- **引擎修正**（`upstream 229ece5`，只改 `FMAP.C` 一行：`g_wFmapLabelRectH` 下限拉到 17）。原本 `g_wFmapLabelRectH = pFont_height[0] + 1`（≈10px，ASCII 字高），但標籤是 16px 中文——hover 切換城鎮時用來擦掉舊標籤的 save/restore 矩形太矮，中文名下緣會殘影。拉到 17 蓋滿。副作用：標籤位置比原本高約 7px（`labelY = townY - rectH`），無妨。`VMCODE.OVL`／`SX.OVL` byte-identical。
- **部署**：loose `dist/test_v100_zh/fmap_twn.dat`（455 bytes，比原 511 小，中文名較短）＋新 `krondor.exe` 458784 bytes（SHA-256 `881938d418a128639a79e0218e7dfc7180bb8d8d433d9c20a26d23641edac229`）。`ZH16.DAT`／`ZHSTAT.DAT` 不變（76 個相異字全在字庫；大字渲染）。manifest：`FMAP_TWN_BUILD_MANIFEST.json`。舊 exe 備份 `scratchpad/dist_backup_pre_fmap/`。
- **待做**：地圖右下角「Exit」按鈕是 `req_fmap.dat`（MenuPage 家族），不在這次範圍，要等 §4 通用 codec。

### ✅ `MNAMES.DAT` 怪物/敵人類型名稱表——已翻譯部署，待實機驗收

戰鬥中「觀察敵人」講評對白（DDX record `0x84`／`0x85`，由 `combatenc_anim_actor_stat_rolls()` 播）內文裡的「moredhel warrior」之類敵人名，來源是 `MNAMES.DAT`——一張 64 槽的怪物類型名稱表，`combatenc_mnames_lookup_dest()`（`CBENC.C`）依 `creatureType` 索引撈出，`DIALOG.C` case 17 展開 `@` token 時 `strcpy` 進 `g_speaker_names[slot]`（`[6][32]` buffer）就地插進內文；每個敵方戰鬥單位的 `.name`（`CBENC.C:100`）也是同一來源。走 DDX 文字路徑（已支援中文），**不用改引擎**。

- **格式**：`u16 count｜count×u16 offset（相對 blob）｜u16 尺寸欄（原檔存整檔長度、引擎超額配置＋EOF 截斷，重建照抄）｜NUL 字串池（有 dedup——24 個 `INVALID MONSTER` 佔位槽共用一個字串）`。跟 `SPELLS.DAT` 家族同型。
- **新工具 `tools/text/mnames_translate.py`**（`scaffold`／`status`／`build`，append-only：原 blob 位元組不動、只改寫已翻槽的 offset，全未翻時 build 出來 byte-identical）＋`tests/unit/test_mnames_translate.py`（6 項）。
- **翻譯**：`localization/translated/MNAMES.json`，**40 個真名全譯**（24 個 `INVALID MONSTER` 佔位不動）。隊員名沿用既有譯名（戈拉斯／歐文／洛克利爾／帕格／派特魯斯／詹姆士），其餘 32 個怪物名回填 `glossary.json` 新 `creature` 分類。`moredhel warrior`→莫瑞德戰士、`moredhel spellcaster`→莫瑞德施法者、`Black Slayer`→黑衣殺手、`Nighthawk`→夜鷹刺客、`Servitor of Lims-Kragma`→林絲克拉格瑪僕役、各種 Giant/Ogre/Wyvern、`Great One`→至尊法師 等。build 0 fallback。
- **部署**：loose `dist/test_v100_zh/MNAMES.DAT` ＋ 重建的 `ZHSTAT.DAT`（908→926 glyph，加了 `MNAMES.json` 當來源以防敵人名走 speaker-bubble 小字路徑）。`ZH16.DAT` 不變（103 個相異字全在字庫；原本要用的 `嫗`／`雛` 已改成 `巫婆`／`幼體雙足飛龍` 避免加冷僻字）。manifest：`dist/test_v100_zh/MNAMES_BUILD_MANIFEST.json`。舊 `ZHSTAT` 備份 `scratchpad/dist_backup_pre_mnames/`。**不用重編 EXE。**

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
9. **法術系統＋戰鬥面板實機驗收**（見上方「法術系統翻譯」）：資源檔＋`CSPELL.C`／`CBENC.C`／`COMBAT.C` 已部署（`krondor.exe` 458768 bytes），尚未在 DOSBox-X 完整驗過（使用者 2026-08-30 已快速看過施法面板、觀察敵人面板、melee HUD 面板前一版，回報「看起來 OK」但還在多試）。要驗的畫面：
   - (a) **戰鬥中施法畫面**——選會法術的角色（歐文／帕格）開施法選單：滑鼠移到法術符文上看**資訊面板**（標題＋消耗／傷害／視線／效果行）小字不重疊、Cost/Damage 行是中文；移開看**可施放法術名清單**小字不重疊。重點：89px 高面板在法術多的系別會不會爆行、`持續打擊全體對手至死`(10 字) 有沒有超出右緣。
   - (b) **角色資訊畫面 → 法術書（2026-09-01 已實機驗收完成）**——最終已改成六學派頁籤＋單項清單＋右側完整大字說明，並由使用者逐輪確認選取色、欄位分行、行距、左右配置與長欄位不掉字；不再使用六類雙行總覽。
   - (c) **戰鬥中「觀察敵人」**（`CBENC.C`）——上方羊皮紙屬性面板 `生命：／體力：／速度：／力量：／弩弓：／近戰：／施法：／防禦：` 小字、標籤不壓到數值欄。
   - (d) **戰鬥中近戰 HUD**（`COMBAT.C combat_arena_hud_melee_panel`）——底部小面板 `刺擊／揮砍`、`傷害`、`命中`、`左鍵／右鍵` 三欄不重疊。
   - (e) **戰鬥中遠攻／施法瞄準**（`combat_arena_draw_tgt_info_hud`／`_panel`）——`選擇目標`、`命中：`、`傷害：`、`剩餘弩箭`（弩箭數不足時那行）小字排版；施法瞄準時中間那行法術名（已中文）置中是否正常。
10. **`MNAMES.DAT` 怪物名實機驗收**（見上方「MNAMES.DAT 怪物…」）：loose `MNAMES.DAT` 已部署，不用重編。要驗：戰鬥中「觀察敵人」講評對白裡的敵人名（例如「莫瑞德戰士」）是否正確顯示中文、內文銜接是否通順；戰鬥 UI 其他顯示敵人名的地方（若有）也順帶看。留意 `冥界召喚師`／`公種雙足飛龍` 這類 5-6 字長名在內文裡斷行是否正常。
11. **`fmap_twn.dat` 大地圖城鎮標籤實機驗收**（見上方「fmap_twn.dat…」）：新 exe（458784）已部署。要驗：旅行大地圖上滑鼠移到各城鎮，標籤是否顯示中文名、**在城鎮間移動時舊標籤有沒有殘影**（`FMAP.C` rect 高度修正的重點）、標籤置中與位置是否正常、地圖上緣附近的城鎮（薩薩戈斯／凱恩／拉格蘭姆）標籤會不會被切到。右下角「Exit」鈕仍是英文（`req_fmap.dat`，待 §4 codec）。
12. **遊戲選單 `req_*.dat` 實機驗收**（見上方「遊戲選單…」，`krondor.exe` 458800）：**主選單已實機確認中文顯示、不再 `MEM:34` 閃退**（修掉 append-only 的堆積損毀 bug 後）。其餘畫面待驗：(a) **暫停選單**（遊戲中按 Esc）——「開始新遊戲／讀取進度／儲存進度／偏好設定／章節目錄／退出至 DOS／取消」7 個按鈕，小字置中、不爆出斜角邊框、78px 寬按鈕塞得下（最長「開始新遊戲」5 字）；(b) **偏好設定**下方「確定／取消／預設值」；(c) **存／讀檔**畫面的「儲存／讀取／刪除存檔／刪除存檔夾／取消」；(d) **神殿治療**畫面「治療角色／下一位／完成」；(e) **傳送**（施放傳送術或 GDS）目的地清單「基利安神殿／尊恩以東…」12 項＋取消，清單列高夠不夠；(f) 物品欄分堆時的「選擇數量：」與「分給隊伍」。標題（如「Options」「Preferences」）仍是英文——那是背景圖，非文字。

## 環境設置（下個 session 不用重裝，但要知道在哪）

### WSL2（已裝好）
- Ubuntu，使用者 `pmanyeh`，已加入 `kvm` 群組（沒加入的話 QEMU-KVM 會靜默失敗、且不留下任何 log——這是踩過的坑）。
- `uv` 裝在 `~/.local/bin`。
- Borland 工具鏈（bc31/bc30/bc20/FreeDOS）解壓在 `~/bak-toolchain`（來自上游 GitHub Release，雜湊已驗證）。

### 編譯用的 WSL 原生 clone
- 位置：`~/krondor-build`（WSL 原生 ext4 檔案系統，**不是** `/mnt/d/...`）。
- 這是 `upstream/betrayal-at-krondor` 的 clone，`origin` 指向 Windows 端的 `/mnt/d/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/.`。
- **永久規則：絕對不要向上游 `canassa/betrayal-at-krondor` push，也不要再嘗試 push。** Windows 端 `upstream/betrayal-at-krondor` 的 `origin` 指向原作者的還原保存專案，只供 fetch／比對；本專案的中文化引擎提交依既定慣例永久保留在本機獨立 repo。已提交的完整引擎修改另以 [`engine-patches/`](engine-patches/) 的 binary-safe 合併 Git patch＋93 筆提交清單保存在本主專案；目前固定範圍為上游 `1fc2a69` 到最終 `8585fb3`，套用後 tree 必須等於 `cf3491c8610b632d8ebe91241747a7598c0c0654`。若日後需要保存完整引擎 Git 歷史，必須由使用者另行明確指定自己的 fork／遠端，不能推往 `canassa`。
- **重要**：`uv sync` / `uv run` 絕對不能在 `/mnt/d/...`（Windows 掛載磁碟）上跑，DrvFs 對 `utime`/硬連結操作會直接報錯（`Operation not permitted` / `Invalid cross-device link`）。一定要在 WSL 原生檔案系統上跑，跑完再把 `work/KRONDOR.EXE` 複製回 Windows 端。

### 重新編譯的標準流程
**⚠️ WSL 編譯 clone（`~/krondor-build`）目前有一批未提交的 VESA/EVG POC WIP**（`EVG.ASM`／`VIDDRV.C`／`FONT.C`／`BOOT.C` 等 8 檔＋`VSV.ASM` 未追蹤），是使用者另一條平行實驗。它會擋 `git pull --ff-only`，所以每次編譯要先 stash、編完再還原。另外 `~/krondor-build` 還留了一個 `stash@{0}`（"VESA/EVG native-CJK WIP - parked for BOK C11 build"）是早期 pop 衝突留下的重複保險，跟現在的 working tree 內容相同，使用者確認實驗沒壞後可 `git stash drop`。**別把這批 WIP 一起 commit 進去**（教訓：2026-08-27 誤把它包進「備份」commit，編出來的 exe 帶了 `video_init(9)` VESA POC，`VMCODE.OVL` 也 diverge）。
1. 在 `upstream/betrayal-at-krondor/bak/SRC/...`（Windows 端）改 C 原始碼、`git add <該檔> && git commit`（只 add 你改的檔，別 `git add -A`）。
2. `wsl -e bash -lc "cd ~/krondor-build && git stash push -u -m wip && git pull --ff-only"`
3. `wsl -e bash -lc "cd ~/krondor-build && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain && export PATH=\$HOME/.local/bin:\$PATH && uv run bak build"`（增量編譯，通常一兩分鐘）
4. 看到 `❌ KRONDOR.EXE: size differs` 是**正常的**——只要 `VMCODE.OVL`/`SX.OVL` 都還是 `✅ BYTE-IDENTICAL` 就代表工具鏈跟連結沒問題，是我們自己故意改了 `KRONDOR.EXE`。
5. `cp ~/krondor-build/work/KRONDOR.EXE scratchpad/KRONDOR_xxx.EXE`（先複製到 scratchpad，因為 DOSBox-X 常鎖住 dist 的 exe）。
6. 還原 WSL clone：`wsl -e bash -lc "cd ~/krondor-build && git reset --hard e3d9ef9 && git stash pop"`（回到 VESA WIP 狀態）。
7. 關掉 DOSBox-X（`Get-Process dosbox-x | Stop-Process -Force`，常有殘留行程），再 `cp scratchpad/KRONDOR_xxx.EXE dist/test_v100_zh/krondor.exe`。
8. 目前 `dist/test_v100_zh/krondor.exe` 由 Windows upstream `6fcffc0` 重編，**466896 bytes**，SHA-256 `0807073954f793b2fc3c2ad183586b883e99c5c99db07f10ec1c7bfe744dad13`；最新功能包含 Tab 可互動熱區、法術分類數量／空狀態、輪替自動存檔、已發現洞穴地標與俯瞰地圖 WASDQE/T 操作。同時部署 loose `REQ_MAIN.DAT` 與 `REQ_MAP.DAT`（兩者帳篷圖示 action_id 均為 `0x14`）。**`dist/dosbox_zh_test.conf` 的 `[dos]` 區塊（`dos=high,umb`）仍不可移除，UMB 後援需要它。**

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
- §17：2026-08-30 這輪——資源檔翻譯大推進：新增 `spell_translate.py`／`mnames_translate.py`／`fmap_translate.py`／`menupage_translate.py` 四支 codec，翻掉法術系統三檔、`MNAMES.DAT` 怪物名、`fmap_twn.dat` 大地圖城鎮標籤、11 個玩家可見的 `req_*.dat` 遊戲選單；`CSPELL/CBENC/COMBAT/FMAP/WIDGET/MODALSCR` 六個 C 檔加小字（`upstream f4cd826`→`dbf3288`）；踩到並修好「MenuPage `.dat` 不能 append-only 重建，否則 `menupage_free()` 取最小指標當基底 → free 內部指標 → `MEM:34` 一開遊戲閃退」的地雷。
