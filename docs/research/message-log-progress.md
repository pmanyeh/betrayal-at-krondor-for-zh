# 訊息紀錄：施工進度

配套文件：[功能與技術規劃](message-log-design.md)、[逐階段施工與驗收](message-log-agent-tasks.md)。

本檔案逐階段追加。**每階段只追加自己那一節，不改寫前面已定案的證據**。

---

## 第 0 階段：接入點查核與可行性

- **狀態**：完成（純調查；未修改任何遊戲程式碼）
- **日期**：2026-09-06
- **基準**：主 repo `df989af16cbcaeb487cda295164f0b830d7f67cf`（master，工作區僅有未追蹤檔）；引擎 `upstream/betrayal-at-krondor` = `5c3ed49a62716f631f26445f083c047ae4721751`（master，工作區乾淨）
- **本階段新增檔案**：只有本檔 `docs/research/message-log-progress.md`。**未新增／未修改任何 `.C`／`.H`／資源／工具檔。**

### 0.1 已讀文件與環境

| 項目 | 結果 |
|---|---|
| `HANDOFF.md` | 已讀（130 KB，重點為「環境設置」「關鍵原始碼位置」「重要教訓」三節） |
| `engine-patches/README.md` | 已讀。固定範圍 `1fc2a69` → `5c3ed49`，套用後 tree 必須 = `8bb689a1fe45f4ecc3637bce322e73044c9aa21c`。**禁止 push `canassa/betrayal-at-krondor`** |
| `docs/workflows/ddx-safe-rebuild.md` | 已讀（`ddx_rebuild_all.py` 全量 all-or-nothing 重建） |
| `docs/workflows/release-packaging.md` | 已讀（`package_release.py` 為每次必跑；`game_data/` 安全檢查） |
| 主專案 `AGENTS.md` | **不存在**（`find . -name AGENTS.md` 無結果）。僅 `upstream/betrayal-at-krondor/CLAUDE.md` 為引擎側說明 |
| 上階段結果 | 無（本功能首次執行） |

### 0.2 Git 與 WSL 建置 clone 狀態（**與 HANDOFF 敘述不符，必讀**）

```
主 repo    HEAD df989af  master  乾淨（僅 5 個未追蹤項：3 個 .pytest-* 目錄 + 2 份本功能規劃文件）
引擎 repo  HEAD 5c3ed49  master  完全乾淨、無 stash
WSL clone  ~/krondor-build
           HEAD  566e11c31f730105fcd76868cc191d6922b7338f
                 "zh: translate the item More-Info detail popup, encampment stat headers, and Party Gold label"
           落後 Windows 端 5c3ed49 共 136 個提交（已驗證 566e11c 是 5c3ed49 的祖先）
           已修改 7 檔（VESA/EVG WIP）：
             bak/INCLUDE/gfx169d.h、bak/SRC/DIALOG/DIALOG.C、bak/SRC/GFX/DRIVER/VTHUNKS.ASM、
             bak/SRC/GFX/FONT/FONT.C、bak/SRC/SYS/DOSMEM.C、bak/SRC/SYS/EMSDET.C、bak/SRC/UI/TEXTWRAP.C
             （+288 / −220 行）
           未追蹤：toolchain/
           git stash list：**空**
           工具鏈 ~/bak-toolchain 存在（bc20 / bc30 / bc31 / freedos）
```

**阻礙／風險（後續階段必須先處理，本階段刻意不動）**

1. **HANDOFF 第 6 步的 `git reset --hard d702c75` 現在是錯的、且具破壞性。** WSL clone 目前的 WIP 基底是 `566e11c`，不是 `d702c75`（`d702c75` 仍存在但已非基底）。照抄會丟掉使用者的 VESA/EVG WIP。**正確做法**：建置前先 `git rev-parse HEAD` 記錄實際值（現為 `566e11c3`），建置後 reset 回該值再 `git stash pop`。
2. HANDOFF 描述的 WIP 檔案清單（`EVG.ASM`／`VIDDRV.C`／`BOOT.C` ＋未追蹤 `VSV.ASM`）與現況**不同**；HANDOFF 提到的 `stash@{0}` 已不存在。
3. WSL clone 落後 136 個提交，`git pull --ff-only` 前必須先 stash，且 stash 中的 `DIALOG.C`／`TEXTWRAP.C`／`FONT.C` 修改**與本功能要動的檔案高度重疊**，pop 時很可能衝突。**建議第 1 階段先與使用者確認是否可改用另一個乾淨 clone（例如 `~/krondor-build-msglog`）建置，避免動到這批平行實驗。**
4. `dist/release_v100_zh` 的 DOSBox-X conf 樣板 `tools/release/dosbox_krondor.conf.template` **仍然沒有 `[dos]` 區塊**（只有 `[dosbox] [sdl] [render] [cpu] [sblaster] [autoexec]`）。HANDOFF 早已記為待補；本功能會再吃記憶體，第 7 階段前必須補上 `dos=high,umb`。

### 0.3 建置與驗證命令（本階段實際執行的）

| 命令 | 結果 |
|---|---|
| `git log -1 --format=%H` / `git status --short`（兩個 repo） | 見 0.2 |
| `wsl -e bash -lc "cd ~/krondor-build && git rev-parse HEAD && git status --short && git stash list"` | 見 0.2 |
| `wsl … git merge-base --is-ancestor 566e11c 5c3ed49` | YES（0） |
| `wsl … git rev-list --count 566e11c..5c3ed49` | `136` |
| `python -m unittest discover -s tests/unit` | **Ran 113 tests，FAILED (errors=1, skipped=1)** |
| `python -m unittest tests.unit.test_overhead_map_controls` | `ModuleNotFoundError: No module named 'pytest'` |

**測試基準說明**：唯一失敗是 `tests/unit/test_overhead_map_controls.py` 的 `import pytest` 失敗——這是**既有環境問題，與本功能無關**（該檔用 pytest 寫、但 `python` 直譯器沒裝 pytest；`.pytest_cache/` 存在代表使用者是用另一個直譯器跑的）。其餘 112 項通過。後續階段回報測試數時請以此為基準。

**尚未執行的建置**：本階段沒有新增／修改任何 C 檔，因此**沒有跑 Borland 建置**。第 1 階段第一次加檔時的命令序列（依 HANDOFF 修正版）：

```bash
# 1) Windows 端改 C 原始碼並只 add 自己改的檔
git -C upstream/betrayal-at-krondor add bak/SRC/DIALOG/MSGLOG.C bak/SRC/DIALOG/MSGLOG.H … && git -C … commit
# 2) 記錄 WSL clone 現況（不要用 HANDOFF 寫死的 d702c75）
wsl -e bash -lc "cd ~/krondor-build && git rev-parse HEAD"     # 目前應得 566e11c3…
wsl -e bash -lc "cd ~/krondor-build && git stash push -u -m msglog-wip && git pull --ff-only"
# 3) 建置
wsl -e bash -lc "cd ~/krondor-build && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain && export PATH=\$HOME/.local/bin:\$PATH && uv run bak build"
# 4) 取出 exe、還原 WSL clone 到步驟 2 記錄的那個 commit
cp ~/krondor-build/work/KRONDOR.EXE scratchpad/KRONDOR_msglog.EXE
wsl -e bash -lc "cd ~/krondor-build && git reset --hard <步驟2記錄的HEAD> && git stash pop"
```

（`❌ KRONDOR.EXE: size differs` 屬正常；`VMCODE.OVL`／`SX.OVL` 必須維持 `✅ BYTE-IDENTICAL`。）

### 0.4 DOSBox-X 現實時間驗證（**已驗證**）

設計文件第 2 節要求「不可將 DOS 時鐘宣稱成已驗證的宿主時間」。本階段實測：

- **不打擾使用者現有實例**：`Get-Process dosbox-x` 顯示有一個 12:12:05 啟動、正在跑遊戲的實例（`capture_frame` 拍到中文說明泡泡）。`read_memory` 需要 debugger 停住，而 HANDOFF 明載真斷點曾反覆讓 `dosbox-x.exe` 當掉，**故未對該實例下斷點**。改用另起隔離實例的方式。
- 兩個隔離實例，各自 mount 一個 scratchpad 目錄、在 autoexec 執行 `date < NUL` / `time < NUL` 導向檔案後 `exit`：

| 設定來源 | 宿主時間 | DOS 回報 |
|---|---|---|
| 複製自 `dist/dosbox_zh_test.conf`（含 `[dos] dos=high,umb`、`memsize=16`） | 2026-09-06 12:40:04 | `Current date: Sun 2026/09/06` / `Current time: 12:40:04.94` |
| 複製自 `tools/release/dosbox_krondor.conf.template`（**無** `[dos]` 區塊、`cputype=486_prefetch`） | 2026-09-06 12:40:52 | `Current date: Sun 2026/09/06` / `Current time: 12:40:52.94` |

宿主時區 `Taipei Standard Time`。**結論：DOSBox-X 的 DOS 日期與時間 = 宿主 Windows 本地時間，誤差 < 1 秒，且與 `[dos]` 區塊無關。**

**引擎內第二重佐證**（比 shell 測試更強，因為它走的正是 C 端 `getdate()` / INT 21h AH=2Ah）：`mainmenu_autosave_service()`／`mainmenu_quicksave_write()` 用 `getdate()` 產生存檔標題 `%04u%02u%02u_%u`。現有測試存檔的標題實際是：

```
dist/test_v100_zh/GAMES/AUTOSAVE.G99/SAVE01.GAM : 20260905_7
dist/test_v100_zh/GAMES/AUTOSAVE.G99/SAVE02.GAM : 20260904_32
dist/test_v100_zh/GAMES/QSAVE.G98/SAVE01.GAM    : 20260904_1
```

與那幾天的實際 session 日期相符。

**尚未驗證**：`gettime()`（INT 21h AH=2Ch，取時分秒百分秒）在本引擎中**尚未被任何現有程式碼呼叫過**，因此「引擎內取得秒級時間」只有 `getdate()` 這一半有實證。`gettime()` 是同一支 Borland RTL 的姊妹函式、同樣走 DOS 服務，風險極低，但第 1 階段第一次寫入時間戳時仍應在畫面上印一次值做實機確認。`MAINMENU.C` 已 `#include <dos.h>`（`struct date` 可用），`struct time` 同在 `dos.h`。

### 0.5 呼叫表 A：來源 → 顯示 → token 展開 → 翻頁 → 關閉

**四條平行顯示路徑**（HANDOFF 只記了三條；`TOWNSCN.C` 是第四條，本次查出）：

```
路徑 1  dialog_play_record(key, modal)            DIALOG.C:992
        └ dialog_load_record_by_key()             DIALOG.C:114   ← alloc_far 出 DDXRecord
        └ dialog_combatant_name_table_init()      DIALOG.C:965   ← 清空並預填 @0/@3/@4/@5
        └ [主迴圈] op wOp==1 → dialog_cmbt_name_assign_kind()  DIALOG.C:487  ← 填 @0..@5
        └ 解析 record->wSpeaker_id                 DIALOG.C:1068-1152
        └ pSpeakerName = askabout_name_or_keyword_lookup(wSpeaker_id & 0xff)   DIALOG.C:1155
        └ dialog_frame_draw()                     DIALOG.C:1251/1261/1266
        └ **dialog_render_text_with_tokens()**    DIALOG.C:1252/1262/1267  ← 第一頁（scroll=0）
        └ 翻頁迴圈：
             0x400 選項頁 → askabout_dialog_run()              DIALOG.C:1524
             0x200 選單頁 → 迴圈 render(i) + askabout_menu_page_run_selection()  DIALOG.C:1531-1547
             其他        → do{ dialog_wait_for_acknowledge(); i += g_wTextWrapLinesDrawn;
                               dialog_frame_draw(); render(i); } DIALOG.C:1554-1573
        └ askabout_keyword_table_free()           DIALOG.C:1675  ← **說話者名字指標在此失效**
        └ dialog_freemem_if_not_null(record)      DIALOG.C:1655  ← **DDX 本文指標在此失效**

路徑 2  dialog_show_by_key(key, interactive)      DIALOG.C:827
        └ dialog_combatant_name_table_init()      DIALOG.C:839
        └ dialog_render_text_with_tokens(rec, NULL, -1,0,0, 0)  DIALOG.C:849
        └ for(;;){ wait; if(!remaining) break; i += drawn; frame_draw; render(i); }  DIALOG.C:863-873
        └ dialog_freemem_if_not_null(record)      DIALOG.C:879

路徑 3  ttmscript_show_dialog_action(arg, mode)   TTMDLG.C:23        ← 劇本／過場
        └ mode 0/3：dialog_load_record_by_key(arg+1600000)  TTMDLG.C:89
                    **dialog_render_text_with_tokens(rec, NULL, …, i)**  TTMDLG.C:107（迴圈翻頁 103-119）
                    ※ 這條路徑**不呼叫** dialog_combatant_name_table_init()，@N 沿用前次殘值
        └ mode 1/4：dialog_show_by_key(arg+1600000, 0)      → 走路徑 2
        └ mode 5  ：dialog_play_record(arg+1600000, 0)      → 走路徑 1
        └ mode 2  ：gmain_play_chapter_intro(arg/10, arg%10)

路徑 4  townscene_dlg_draw_page(record, scroll)   TOWNSCN.C:414      ← 城鎮／室內場景說明條
        └ townscene_dlg_split_title() 先把 #標題# 切出來   TOWNSCN.C:373
        └ dialog_combatant_name_table_init()      TOWNSCN.C:423
        └ **dialog_render_text_with_tokens(record, body, -1,0,0, scroll)**  TOWNSCN.C:424
        ※ 註解明寫「safe to call repeatedly from the hotspot loop」——**同一 scroll 會被重畫多次**
```

**四條路徑唯一的匯流點就是 `dialog_render_text_with_tokens()`（DIALOG.C:594）。建議把擷取 hook 放在它的結尾（第 824 行 `g_bSmallZhMode = 0;` 之後）。** 在 `dialog_play_record()` 攔截會漏掉路徑 3 的過場文字與路徑 4 的場景說明。

`dialog_render_text_with_tokens()` 內部順序（重要細節）：

| 行 | 內容 |
|---|---|
| 609 | `dialog_resolve_style()`（會**寫回** `record->bStyle`） |
| 611 | `dialog_apply_style_state()` → `applied[4]` = 版面矩形 |
| 621-681 | `#標題#` 解析：把結尾 `#` **就地改成 `\0`**，`pTitle` 指向標題；已修好中文 trail byte 0x23 誤判 |
| 683-741 | 本文複製到 `g_pMainScratchBuf`，同時展開 `@0..@5` |
| 743 | `g_pMainScratchBuf[nScratchLen] = '\0'` ← **token 已展開完畢、緩衝尚未被覆寫，這是唯一安全的擷取點** |
| 744-779 | 計算 `g_bMixedZhMode` / `g_bSmallZhMode`（含三個寫死的 rect 特例） |
| 814-819 | 若 `pStyle->header[3] != 0`：畫**陰影**（第一次 `textwrap_draw_aligned`） |
| 820-822 | 畫正文（第二次 `textwrap_draw_aligned`，同樣參數） |

**陰影不會造成重複紀錄**：陰影與正文是**同一次呼叫內**的兩次 `textwrap_draw_aligned`，參數相同，覆寫同一組全域值。只要 hook 放在函式**結尾**，一次呼叫 = 一頁 = 一筆。

**已顯示字串範圍的取得方式**（`TEXTWRAP.C:113-194`）：

- `textwrap_draw_aligned(text, x, y, max_width, max_height, spacing, flags, first_line)`
- 內部把整段切成 `lines[]`（`{start, end}` 為 **byte offset**，最多 0x5a=90 行），本次畫的是 `lines[first_line] … lines[count-g_wTextWrapLinesRemaining-1]`
- 三個全域輸出（`TEXTWRAP.C:165-188`）：
  - `g_wTextWrapLinesRemaining` — 還沒畫的行數（0 = 最後一頁）
  - `g_wTextWrapLinesDrawn` — 本次畫了幾行
  - `g_wTextWrapXAccum` — 本次畫出的**總 byte 數**（`Σ(end-start)`），但**不含行首 offset**
- **`lines[]` 是區域變數，沒有輸出起始 byte offset。**

> **第 3 階段建議（需一行極小的行為中性修改）**：在 `TEXTWRAP.C` 的繪製迴圈補兩個全域 `g_wTextWrapByteStart = lines[first_line].start;` 與 `g_wTextWrapByteEnd = lines[fl-1].end;`，就能得到本頁在 `g_pMainScratchBuf` 中的精確 byte 區間，不必重算。替代方案是在 hook 裡再呼叫一次 `textwrap_compute_lines()`（同樣是決定性函式，結果相同，但多一次 O(n) 掃描）。**本階段未實作，僅記錄選項。**

**去重規則**（以原始碼為據，不是猜測）：

| 情形 | 證據 | 處理 |
|---|---|---|
| 陰影 + 正文 | 同一次 `dialog_render_text_with_tokens` 內 | 結構上就不會重複 |
| `wFlags & 0x200` 選單頁 | DIALOG.C:1252 已用 scroll=0 畫過一次，1531-1535 的 `while` 首圈**又用 i=0 畫一次** | **會重複第 0 頁**，必須用 (display instance, scroll_start) 去重 |
| 城鎮場景說明條 | `townscene_dlg_draw_page` 註解自陳「safe to call repeatedly」 | 同一 scroll 只記一次 |
| 一般翻頁 | `i += g_wTextWrapLinesDrawn` 單調遞增 | 天然不重複 |
| 往回翻 | 目前所有路徑都只往前，**沒有回看** | 無此問題（若第 4 階段的 viewer 自己有回看，那是 viewer 路徑不是擷取路徑） |
| 玩家跳過未顯示頁 | `dialog_wait_for_acknowledge` 回 0 時只設 `g_bCutsceneEscPressed`，迴圈仍是先畫再等 | 只要 hook 在「畫完」之後就不會提前記錄 |

### 0.6 呼叫表 B：存／讀所有入口 → 最終提交

`savegame_write(` / `savegame_read(` 的**完整**呼叫者（`grep -rn` 全 `bak/` 只有這幾處）：

```
savegame_write(char *filename)   SAVEGAME.C:23
  ← MAINMENU.C:980    手動存檔      目標 "GAMES\<slot>.G%02d\SAVE%02d.GAM"（直接寫正式路徑，無暫存）
  ← MAINMENU.C:1501   書籤 Bookmark 目標 "GAMES\<slot>.G%02d\SAVE00.GAM"（同上，直接寫）
  ← MAINMENU.C:1686   自動存檔      目標 "GAMES\AutoSave.G99\AUTONEW.GAM"（暫存 → commit）
  ← MAINMENU.C:1823   快速存檔      目標 "GAMES\QSave.G98\QSNEW.GAM"    （暫存 → commit）

savegame_read(char *filename)    SAVEGAME.C:81
  ← GMAIN.C:189  gmain_start_dispatch() 唯一呼叫點
       iMode==2 新遊戲 → path = "STARTUP.GAM"
       iMode==3 讀檔   → path = "GAMES\%s.G%02d\SAVE%02d.GAM"（由 g_szSaveSlotDirName_51cc /
                                g_wCurrentSaveSlotKey / g_wCurrentSaveFileKey 組出）
       iMode==4/5/7    → path == NULL，**不讀檔**（沿用 TEMP.GAM）
```

**沒有略過已知入口的寫入路徑。** `savegame_write` 一律先 `gstate_temp_file_close()`，把 `TEMP.GAM` 整份複製到目標，寫 0x5a 標頭 + `g_gameState` 前 2 byte + 3 個書籤欄位 + `version=0x16`（共 100 byte），再 `gstate_temp_file_open()`。`savegame_read` 反向：讀 100 byte 標頭、檢查 `*(u16*)(buf+0x62) == 0x16`、其餘寫回 `TEMP.GAM`。

**四個上層入口的觸發點**：

| 入口 | 觸發 | 檔案:行 |
|---|---|---|
| 手動存檔 | 選項頁 `Save Game`（action 0x1F）→ `mainmenu_save_save_game_dialog()` | MAINMENU.C:236 → 580 |
| 書籤 | 世界迴圈按鍵 → `mainmenu_save_bookmark()` | WORLDLP.C:709 |
| 快速存檔 | `QUICKSAVE_SCANCODE` → `mainmenu_quicksave_write()` | WORLDLP.C:567 |
| 自動存檔 | `mainmenu_autosave_request()`（HOTSPOT.C:538,793／GMAIN.C:204,207／ENCAMP.C:296／MODALSCR.C:97,842／TOWNSCN.C:963）→ 世界迴圈 `mainmenu_autosave_service()` | WORLDLP.C:434 |
| 快速讀檔 | `QUICKLOAD_SCANCODE` → `mainmenu_quickload_prepare()`（**只設槽位變數，回 exit_mode=3**）→ 上層 `gmain_start_dispatch(3)` 才真的讀 | WORLDLP.C:579 → GMAIN.C:189 |

**現行自存／快存提交協議**（`mainmenu_autosave_commit` MAINMENU.C:1575、`mainmenu_quicksave_commit` MAINMENU.C:1719——兩者結構完全相同）：

```
remove(backup)                       # AUTOB%02d.GAM / QSB%02d.GAM
if exists(target): rename(target, backup)   失敗 → return 0
rename(temp, target)                 失敗 → 若 backup 在則 rename(backup, target)；return 0
remove(backup)
return 1
```

**現行恢復**（`mainmenu_autosave_recover_files` MAINMENU.C:1557、`mainmenu_quicksave_recover_files` MAINMENU.C:1701）：

```
remove(AUTONEW.GAM / QSNEW.GAM)
for i in 1..COUNT:
    if exists(backup): 
        if exists(target): remove(backup)      # 新檔已就位 → 丟掉備份
        else:              rename(backup, target)
```

> **第 2 階段警告**：`*_recover_files()` 在「target 存在」時會**直接 `remove(backup)`**。新的 pair-save 協議如果還需要那份 backup 來還原 `.MLG`，這個既有恢復函式會先把它刪掉。設計文件第 2 階段的「舊恢復函式不得先刪掉新協議仍需要的備份」講的就是這裡。此外 `mainmenu_quickload_prepare()`（MAINMENU.C:1851）與 `mainmenu_quicksave_write()`（:1767）**在讀檔前也會跑一次 recover**。

**手動存檔／書籤完全沒有暫存與備份**——`savegame_write()` 直接 `open(filename, …, 0x180)` 覆寫正式檔，失敗才 `remove(filename)`（SAVEGAME.C:66-67）。也就是**手動覆蓋存檔本來就不是原子的、失敗會直接毀掉舊檔**。第 2 階段的協調器等於同時修好了這個既有缺陷，但**不要在報告中把它說成「原本安全、現在維持安全」**。

**檔案複製／更名／刪除的完整清單**（`grep -rn "\bremove(\|\brename(\|\bunlink(\|\brmdir(\|\bmkdir("` 全 `bak/SRC`）：

| 檔案:行 | 動作 | 用途 |
|---|---|---|
| SAVEGAME.C:67 | `remove(filename)` | 寫失敗時刪掉半成品目標 GAM |
| SAVEGAME.C:131 | `remove(temp_path)` | 讀失敗時刪掉 TEMP.GAM |
| MAINMENU.C:888 | `remove("GAMES\\%s.G%02d\\SAVE%02d.GAM")` | **刪單一存檔**（action 0xC2） |
| MAINMENU.C:940 | `mkdir` | 建新存檔目錄 |
| MAINMENU.C:1277 | `remove("KRONDOR.CFG")` | 偏好設定重設 |
| MAINMENU.C:1344-1351 | `findfirst("<dir>\\*.*")` + `remove` 迴圈 + `rmdir` | **刪整個存檔目錄**（action 0xC3）。**wildcard 是 `*.*`，會一併刪掉 `.MLG`** |
| MAINMENU.C:1417-1419 | `mkdir("GAMES")` / `mkdir(szPath)` | 建 GAMES 根目錄 |
| MAINMENU.C:1562/1581/1586/1591 | autosave 的 remove/rename | 見上 |
| MAINMENU.C:1706/1725/1730/1735 | quicksave 的 remove/rename | 見上 |
| MAINMENU.C:1685/1692、1822/1829 | 暫存檔 remove | 見上 |

**存檔清單的 glob（決定 `.MLG` 會不會被誤列）**：

- 槽位目錄：`GAMES\*.G??`，attr `0x10`（目錄）— MAINMENU.C:2013, 2034
- 槽內檔案：`GAMES\<slot>.G%02d\SAVE??.GAM` — MAINMENU.C:2094

→ **`SAVE01.MLG` 不會出現在存檔選單**（副檔名不符）。`AUTONEW.GAM`／`AUTOB01.GAM`／`QSNEW.GAM`／`QSB01.GAM` 同樣不符 `SAVE??.GAM`，是既有的安全命名先例。新協議的暫存／備份沿用 `MLGNEW.MLG`／`MLGB01.MLG` 這類命名即可，**但整目錄刪除仍是 `*.*`，會一併清掉，這正是我們要的**。

**暫存位置規則**：`g_cfgTempDrive`（`CFGPARSE.C:40/82`，由 `KRONDOR.CFG` 的 token 首字大寫而來）。若非 0 → `"%c:TEMP.GAM"`；否則 `"TEMP.GAM"`（當前目錄）。使用點：`SAVEGAME.C:36,93`、`GSTATE.C:172`。設計文件第 5 節「提交用的暫存檔必須建在目標保存目錄，不能跨磁碟 rename」在這裡有直接支持：`TEMP.GAM` 可能在別的磁碟，所以 `.MLG` 的提交暫存**不能**放在 temp drive。

**死亡後載入**：**沒有獨立入口**。戰鬥全滅 → `g_gameState.bCombatExitRequest` → `world3d_main_loop` 回 `exit_mode = 6`（WORLDLP.C:796-798），先 `dialog_play_record(0x145, 0)`（WORLDLP.C:811，「遊戲結束」文字），回到 `main()` 的 `mode==6` → `mainmenu_save_main_menu(0)`，之後走一般讀檔路徑。

**重開遊戲**：`main()`（GMAIN.C:720-764）是唯一的模式迴圈，`mode` ∈ {1 退出, 2 新遊戲, 3 讀檔, 4 章節目錄回歸, 5 下一章, 6 主選單, 7 其他離場}。

### 0.7 Who / Where / When 的實際來源（逐項附函式與範例值）

#### `@0..@5` 與 `wSpeaker_id` 的區別（**設計文件要求的「特別證明」**）

**兩者完全無關，是兩套獨立機制。**

**`wSpeaker_id`（Who，真正的發話者）**
- 型別：`DDXRecord.wSpeaker_id`（`unsigned short`），來自 DDX 記錄本身
- 正規化：`DIALOG.C:1068-1152`
  - `0xFE` → `gstate_event_read(0x7535) + 1`（主角）
  - `0xFF` → 上一個隊伍發話者 `partySpeaker`
  - `0xFD` → 上一個 NPC 發話者 `npcSpeaker`
  - `>= 0xF0` → `g_speaker_kinds[id - 0xF0]` 指定的隊員
  - `1..6` → 隊員槽（同時設 `g_gameState.nEvtArgActor0 = id-1`）
  - 其他非 0 → NPC id，存進 `npcSpeaker`
- 取名：`pSpeakerName = askabout_name_or_keyword_lookup(record->wSpeaker_id & 0xff)`（`DIALOG.C:1155`）
  - `ASKABOUT.C:68-78`：`id == 0` → `NULL`（**無說話者 → 旁白**）
  - `id < 7` → 隊員 `name` 欄位（`&g_gameState.zoneDefaultCameraPos.nWorld_x + 3 + id*0x5f` 的指標算術）
  - `id >= 7` → `*(u16*)((char*)g_pKeywordTable + (id + 0x124)*2 + 2)` ← **KEYWORD.DAT 的執行期說話者名字表**
- **範例值（已用 `localization/translated/KEYWORD.json` 對照證實）**：該表在 JSON 中的 `index` = `wSpeaker_id + 293`，且這幾筆的 `notes` 欄位就寫著 `"Runtime speaker-name table."`：

  | `wSpeaker_id` | KEYWORD.json index | source | translation |
  |---|---|---|---|
  | 7 | 300 | `Navon du Sandau` | 納馮．杜桑多 |
  | 33 | 326 | `Abuk` | 阿布克 |
  | 50 | 343 | `Delekhan` | 迪勒肯 |

- **重要**：`record->wFlags & 1 == 0` 時 `pSpeakerName` 被強制設回 `NULL`（`DIALOG.C:1156-1158`）——**有 speaker id 不代表要顯示名字**。
- **生命週期陷阱**：這個名字是 `g_pKeywordTable` 內的 **near 指標**（`askabout_keyword_table_load()` 在 ASKABOUT.C:57-60 把表內偏移就地 relocate 成 DS 位址）。`dialog_play_record()` 在 **DIALOG.C:1675** 呼叫 `askabout_keyword_table_free()` → `galloc_zfree()`。**離開對話後指標即失效，必須當場 `strcpy` 快照。**

**`@0..@5`（純文字 token，**不是**說話者）**
- 來源：`g_speaker_names[6][32]` + `g_speaker_kinds[6]`（`DIALOG.C:82-83`）
- 展開：`DIALOG.C:695-735`。`@` 後接數字 → `idx = digit`，取 `g_speaker_names[idx]`；`@` 後**不是**數字 → 一律用 `g_gameState.characters[g_gameState.nEvtArgActor0].name`
- 填值：`dialog_cmbt_name_assign_kind(slot, kind, aux, name_token)`（`DIALOG.C:487-592`），由 DDX op `wOp == 1` 驅動（`DIALOG.C:1050`）。**`kind` 決定內容是什麼**：

  | kind | 內容 | 證據行 |
  |---|---|---|
  | 1-6 | 隊員名 | 505-506 |
  | 7 | 主角名 | 510-511 |
  | 10/11/12/30 | 事件參數指定的隊員名 | 516-531 |
  | 13-16, 31 | 隨機隊員名 | 539 |
  | 17 | **怪物名**（`combatenc_mnames_lookup_dest`） | 543-545 |
  | 18 | **物品名**（`itemtbl_record_ptr_by_id`） | 549-550 |
  | **19** | **金額**（`gstate_format_money(…, lEvtArgGoldCost, 2)`） | **554** |
  | **20** | **隊伍持有金錢** | **558** |
  | **21/22/23** | **純整數**（`ltoa`） | **562-570** |
  | 27/29 | **屬性名**（`g_abStatNames`） | 574, 585 |
  | 28 | 固定字串「紮營休息」／「旅店」 | 581 |
  | 32 | KEYWORD 表查表 | 521 |

- **實例證明（`localization/translated/DIAL_Z18.json`，node 1800022，即 `SHOP.C` 的 `dialog_play_record(0x1b7756, 0)`）**：
  ```
  "I can offer only @1 for it," explained the @0.
  ```
  這裡 `@1` 是**金額**（kind 19/20），`@0` 是**商人的稱謂**（kind 32 查 KEYWORD）。同一筆記錄的 `wSpeaker_id` 則另外指向真正的說話者。
- 另一例（node 1300080，`MODALSCR.C:0x13d670`）：`Carefully, he laid the @0 on a low table…` — 這裡 `@0` 是**物品名**（kind 18）。

> **結論（可直接寫進第 3 階段規格）**：`@N` 只是文字替換槽，內容可能是金額、數字、物品名、怪物名或屬性名。**絕不可拿 `@0` 當說話者**。Who 只能來自 `wSpeaker_id` → `askabout_name_or_keyword_lookup()`；`wSpeaker_id == 0` 或 `wFlags & 1 == 0` 時應記為「旁白」或「未知說話者」，不得捏造。

#### 玩家實際選擇的話題／回答

| 路徑 | 擷取點 | 取標籤的方法 |
|---|---|---|
| Ask-About 話題頁（`wFlags & 0x400`） | `DIALOG.C:1524-1527`，`i = askabout_dialog_run(...)` 回傳 **已確認**的 choice index（`i < 0` = 玩家按了「道別」／取消） | choice 的 `wCond` 即 topic id；標籤 = `*(u16*)((char*)g_pKeywordTable + (wCond - 1)*2 + 2)`（與 `ASKABOUT.C:278-280` 建清單時同一算式） |
| 一般選單頁（`wFlags & 0x200`） | `DIALOG.C:1546`，`nResult = askabout_menu_page_run_selection(record)` | `ASKABOUT.C:532-535`：非隊伍選擇時 topic id = `*(u16 far*)((u8 far*)record + selected*10 + 9)`；隊伍選擇（`wFlags & 0x1000`）時標籤 = 隊員名，`selected == wEntry_count-1` 代表「取消」 |

**不要在建立選項清單時記錄**——`askabout_menu_page_build()`（`ASKABOUT.C:244`）會列出所有**可用**話題，那是候選不是選擇。取消／道別（`askabout_dialog_run` 回 -1、或 `menu_page_run_selection` 選到最後一項）**不得記成已選話題**。

#### Where（地點）

**引擎沒有「現在位置名稱」這個字串。** 可用的來源只有這些，逐項附證據：

| 來源 | 型別／取得 | 證據 | 適用情境 |
|---|---|---|---|
| `g_gameState.nZoneId` | `unsigned char`（`GMAIN.H:37`） | 全域可讀，例如 `DIALOG.C:1145` | **永遠可用的區域 ID**（fallback「區域 N」） |
| 城鎮／室內場景檔 | `GDS<chapter><sub>.DAT`，`chapter`／`sub` 為 `townscene_load(chapter, sub, preserve)` 參數 | `TOWNSCN.C:163, 185-190` | 場景身分（`g_dialog_in_scene != 0` 時有效） |
| **場景說明的 `#標題#`** | `townscene_dlg_split_title()` 切出的 `title` | `TOWNSCN.C:373-395` | **這是唯一的可讀室內地名**。例：`DIAL_Z13.DDX#0`（node 1300001）標題 = `#Three Hillmen Pawn#`／`#三山當鋪#` |
| 大地圖城鎮標籤 | `g_pFmapTownLabels[i]`（來自 `fmap_twn.dat`），配 `g_pFmapTownXCoords/YCoords` | `FMAP.C:268-303` | **只在大地圖畫面開著時存在**，`fmap_hotspots_unload()`（`FMAP.C:320-330`）會 `galloc_zfree` 掉。**不能在對話當下直接讀** |
| 玩家世界座標 | `g_world_camera->base.pos` | `MAINMENU.C:973` 等 | 診斷用 |
| 大地圖標記座標 | `fmap_xy_lookup_for_chapter(&x, &y)` | `FMAP.C:358` | 存檔已用它算書籤圖示；不需另外開大地圖畫面 |

> **第 3 階段建議**：Where 的快照 = `{nZoneId, 城鎮場景 chapter/sub（若 g_dialog_in_scene）, 最近一次場景說明的 #標題#（已解碼中文字串）, fmap_xy_lookup_for_chapter 的 x/y}`。顯示名優先用場景標題；沒有就用「區域 N」。**`fmap_twn.dat` 的城鎮名要當顯示名的話，需要另外做一個 (x,y) → 城鎮 index 的離線對照表**（建置期產生小表，不在執行時開大地圖），這是**尚未決定**的事項，見 0.11。

#### When（現實時間）

`getdate(&struct date)` 已在 `MAINMENU.C:1631, 1768` 實際使用並驗證正確（見 0.4）。秒級需要 `gettime(&struct time)`（`dos.h`，`ti_hour/ti_min/ti_sec/ti_hund`），**引擎目前尚未使用過**。

### 0.8 對話 session（conversation）邊界

**建議邊界 = `dialog_play_record()` 的最外層（深度 0）進出。**

證據與注意事項：

- `dialog_play_record()`（`DIALOG.C:992`）本身就是整個節點圖主迴圈：載入 → 逐節點顯示 → choice 分派 → `chapterStack/keyStack` 的巢狀跳轉（`DIALOG.C:1630-1633, 1657-1664`，深度上限 5）→ 結束清理。**同一次呼叫內的多個 DDX 節點、玩家選項、巢狀跳轉，天然就是一場交談。**
- **不可重用 `g_dialog_running`**：`DIALOG.C:1034` 設 1，`:1036` 與 `:1691` 設 0，**沒有存回舊值**。目前實測沒有確認的巢狀呼叫路徑（`evtcond_dialog_action_dispatch()`（EVTCOND.C:180）本身不呼叫 `dialog_play_record`；會呼叫的 `evtcond_dispatch_key_to_handler()` 只由 `HOTSPOT.C:578, 836` 在對話**之外**呼叫），但這個旗標一旦巢狀就會提早歸零。**請用自己的深度計數器，進入時 `depth++`、離開時 `depth--`，並在所有 early return 出口平衡。**
- `dialog_play_record()` 的 early return 出口：`DIALOG.C:1035-1036`（載入失敗）、`:1709`（`done != 0`）、`:1712`（正常）。三個都要平衡。
- 路徑 2（`dialog_show_by_key`）與路徑 3（`ttmscript_show_dialog_action` mode 0/3）**不經過 `dialog_play_record`**，屬「非 NPC 劇情」，各自建立獨立的 conversation 範圍。
- 路徑 4（`townscene_dlg_draw_page`）是場景說明條，**不是交談**；建議獨立 kind。
- `dialog_play_record()` 從**選項頁本身**被呼叫的情形（`MAINMENU.C:211/221/…` 的 overlay 說明、確認框、錯誤框）也會建立 conversation 範圍——這些必須靠分類表排除，見 0.9。

### 0.9 分類（收錄／排除）來源表

**分類鍵 = 「呼叫情境 + record key」**，不是 DDX 檔名。反證：`DIAL_Z13` 同時包含**系統交易**（1300082 旅店住宿確認）與**場景敘事**（1300001「三山當鋪」場景說明）。

`record_key / 100000` 決定 DDX 檔名（`DIALOG.C:138`：`g_nDialogChapterId = record_key / 100000`，再組成 `DIAL_Z%02d.DDX`）。

已用 `localization/translated/DIAL_Z*.json` 的 `source` 欄位逐筆核對過的分類基礎（節錄，**非完整清單**）：

| record key | 檔案 | 呼叫點 | 英文原文摘要 | 第一版分類 |
|---|---|---|---|---|
| `0x126`-`0x12E` (294-302) | Z00 | `GMAIN.C:178` `dialog_play_record(chapter + 0x125, 0)` | `Chapter One: Into a Dark Night / Escort Gorath to Krondor!` | **讀檔展示 → 依情境**（見 0.10） |
| `0x1e8497` (2000023) | Z20 | `SAVEGAME.C:249` `savegame_chapter_start_dispatch()` 結尾 | （無本文，控制節點；後續才是真正的換章敘事） | **收錄**（真正新章敘事） |
| `0x145` (325) | Z00 | `WORLDLP.C:811` 戰鬥全滅 | 遊戲結束提示 | 排除（系統） |
| `0x13b` (315) | Z00 | `GMAIN.C:190` `savegame_read` 失敗 | `An important data file could not be created!` | 排除（系統） |
| `0x6e`-`0x71` (110-113) | Z00 | `MAINMENU.C` 各確認框 | `Are you sure you would like to exit to DOS?` … | 排除（系統） |
| `0x73`-`0x79` (115-121) | Z00 | `MAINMENU.C:211,221,233,246,258,272,286` overlay 說明 | 選項按鈕說明 | 排除（選單說明） |
| `0x86`-`0x99` | Z00 | `MAINMENU.C` 存讀檔錯誤 | `The game could not be saved!` … | 排除（系統） |
| `0x8f`, `0x90`, `0x14c`-`0x14e` | Z00 | `MAINMENU.C:1468-1508` 書籤 | `Left click to save Bookmark file.` / `Saving Bookmark...` | 排除（系統；**保存動作本身不計入歷史**） |
| `0x149`, `0x14a` (329,330) | Z00 | `GMAIN.C:476,634` 章節目錄 overlay | `Left clicking in this area will view the scenes…` | 排除（選單說明） |
| `0x13d65e`-`0x13d673` (1300062-83) | Z13 | `MODALSCR.C` 神殿／旅店、`CHARSCRN.C` 治療 | 神殿收費、住宿確認、餘額不足 | **排除（交易）** |
| `0x1b7741`-`0x1b7773` (1800001-48) | Z18 | `SHOP.C`／`ITEMUSE.C`／`INVENTOR.C`／`CMBINV.C`／`INVINSP.C`／`MODALSCR.C`／`PICKLOCK.C` | `"I can offer only @1 for it," explained the @0.` `"That will be @1," demanded the @0.` | **排除（交易／物品系統）** |
| `0x200b30`-`0x200b33` (2100288-91) | Z21 | `EVTCOND.C:357,359` 戰後能力提升 | 「隊伍的各項能力都提升了。」 | 排除（系統）。**注意這幾筆被 `DIALOG.C:764-767` 強制小字，且 HANDOFF 記載其字模來源特殊** |
| `0x47` (71) | Z00 | `TOWNSCN.C` | `@ strummed the lute. "Before you get started, I think you should know we've tapped out our entertainment fund," the tavern keeper said quietly.` | **收錄（旅店內劇情，非交易）** |
| `0x9a` (154) | Z00 | `WCURSOR.C` ×18 處 | `@0 shrugged. "This must not be very important,"` | 收錄（旁白）— 高頻，量測時注意 |
| `0x9b` (155) | Z00 | `WCURSOR.C:1113` | `The small mound of dirt seemed to indicate that someone had recently dug a hole here.` | 收錄（旁白） |
| `0x61`, `0x62` (97,98) | Z00 | `WCURSOR.C:1290, 973` | `"I'd guess it's a way marker," @0 said.` | 收錄（旁白） |
| `pSubrec->interact_msg.dwMessage_id` | 動態 | `WCURSOR.C` 多處 | 世界物件互動訊息 | 收錄（動態 key，**只能靠呼叫情境分類**） |
| `pA->dwDialogKey` / `pA->dwAltDialogKey` | 動態 | `TOWNSCN.C:720, 752, 871` | 城鎮場景熱區對話 | 收錄（動態 key） |
| `0x249f1b`-`0x249f1f` (2400027-31) | Z24 | `TOWNSCN.C` 寶箱密碼 | `All were silent. In their minds only one thought prevailed…` | 收錄（劇情） |
| `1600000 + n` | Z16 | `TTMDLG.C:89/127/136/142`、`SHOWMSG.C:6` | 過場文字 | **收錄已顯示部分** |

**分類原則（可直接生成表格）**

- **靜態 key（原始碼中是常數）**：直接查表，明確標記排除／收錄。這是絕大多數系統與交易文本。
- **動態 key（`dwMessage_id`／`dwDialogKey`／`interact_msg`）**：無法在建置期列表，**改用呼叫情境分類**——來自 `WCURSOR.C`／`TOWNSCN.C`／`HOTSPOT.C` 的動態 key 預設**收錄**（都是敘事互動）；來自 `MAINMENU.C`／`MODALSCR.C`／`SHOP.C`／`ITEMUSE.C`／`INVENTOR.C`／`CMBINV.C`／`INVINSP.C`／`PICKLOCK.C`／`CHARSCRN.C` 的預設**排除**。
- 建置期用 JSON 產生小型 C 常數表（排序後二分查找），**執行時不引入 JSON parser**。
- **已依產品決策完成**：`COMBAT.C`、`CSPELL.C`、`SPELLFX.C`、`CIPHER.C`、`PICKLOCK.C` 的戰鬥、法術與謎題訊息全部排除，不再區分敘事或數值提示。所有 literal `dialog_play_record()` key 均由單元測試掃描並要求落入排除政策；`CIPHER.C` 以動態 key 直接呼叫底層 renderer 的謎題正文沒有 capture hook，因此也不會寫入紀錄。

### 0.10 轉場與章節：確切的初始化／隔離順序（**設計文件的關鍵未解項，已解決**）

```
main()  GMAIN.C:720
  mode==6 → mainmenu_save_main_menu(0)          # 主選單
  mode==2 → gmain_play_chapter_cutscene(1,1,1)  # 新遊戲片頭（ADS/TTM → 路徑 3）
  mode==4 → gmain_restart_from_save_flow()      # 章節目錄
  mode==5 → gmain_play_chapter_cutscene(n,2,1) + gmain_play_chapter_cutscene(n+1,1,1)
  → gmain_start_dispatch(mode)   GMAIN.C:66
```

`gmain_start_dispatch()` 內部**確切順序**：

```
GMAIN.C:92-108   決定 path：
                   iMode==2 → "STARTUP.GAM"，chapter=1，doFullmap=1
                   iMode==3 → "GAMES\…\SAVE%02d.GAM"，chapter 由存檔標頭讀出，doFullmap=1
                   iMode==4 → path=NULL，doFullmap=0
                   iMode==5 → chapter = g_nChapterAtLoopExit+1，doFullmap=1
GMAIN.C:157-181  if (doFullmap) 畫大地圖 + **dialog_play_record(chapter + 0x125, 0)**   ← 章節橫幅
GMAIN.C:188-195  if (path) { if (savegame_read(path)==0) { dialog_play_record(0x13b,1); return 6; } }
GMAIN.C:197-199  gstate_temp_file_open(); uiwidget_tile_sprite_load(); boot_party_state_load_from_temp();
GMAIN.C:202-207  if (iMode==2) savegame_chapter_start_dispatch(1);   mainmenu_autosave_request();
                 if (iMode==5) savegame_chapter_start_dispatch(n+1); mainmenu_autosave_request();
                   └ SAVEGAME.C:141-251，結尾 **dialog_play_record(0x1e8497L, 0)**  ← 真正的換章敘事
GMAIN.C:212-219  zone_subsystem_init(); … world3d_main_loop();
```

**因此，明確的隔離／初始化順序建議（有呼叫順序證據支持）**：

| 事件 | 時機 | 動作 |
|---|---|---|
| 進入 `gmain_start_dispatch()` 最開頭（GMAIN.C:79-88） | 在任何 `dialog_play_record` 之前 | **進入 `transition` 狀態，停記** |
| `savegame_read()` 成功後（GMAIN.C:195 之後、197 之前） | 遊戲狀態已確定 | `iMode==3` → **啟用該存檔的候選歷史**；`iMode==2` → **建立空的新時間線** |
| `savegame_read()` 失敗（GMAIN.C:189-194，`return 6`） | | **維持原工作歷史不變**（不得先清空），照引擎回主選單 |
| `iMode==4/5/7`（`path==NULL`） | 沒有讀檔 | **沿用現有工作歷史**，只需離開 `transition` |
| `gstate_temp_file_open()` 之後（GMAIN.C:197） | | **離開 `transition`，恢復收錄** |
| `savegame_chapter_start_dispatch()`（GMAIN.C:203/206） | 已在收錄狀態 | 其結尾的 `dialog_play_record(0x1e8497)` 換章敘事**正常收錄** |

→ **章節橫幅（`chapter + 0x125`）永遠落在 `transition` 內，永遠不會被記錄。**這同時滿足了「讀檔展示不污染」與「新遊戲／自然換章的真正敘事要收錄」，因為真正的敘事在 `savegame_chapter_start_dispatch()` 裡、在 transition 之後。**不需要「先寫隔離候選暫存再合入」的複雜方案。**

**章節目錄（`Contents`，action 0x2E）— 是否建立不同遊玩進度？答：不會。**

- 遊戲內按下（`MAINMENU.C:261-266`，`reentering != 0`）：`mainmenu_save_party_to_tmp()`（把當前狀態寫進 `TEMP.GAM`）→ `result = 4` → `main()` 的 `mode==4` → `gmain_restart_from_save_flow()` → `gmain_start_dispatch(4)`。
- `gmain_restart_from_save_flow()`（`GMAIN.C:417-699`）**從頭到尾沒有 `savegame_read`、沒有改 `g_gameState`**。它只做：載 `contents.dat` 選單、依 `mainmenu_save_scan_highest_slot()` 開關項目、選中章節時呼叫 `gmain_play_chapter_cutscene()` / `gmain_cutsc_play_fullmap_scene()` 播放過場，然後回到選單。**純粹是過場回放藝廊。**
- `gmain_start_dispatch(4)` 因 `path == NULL` 不讀檔，直接 `gstate_temp_file_open()` + `boot_party_state_load_from_temp()` 回到剛才那份 `TEMP.GAM`。
- 主選單按下（`reentering == 0`，`MAINMENU.C:267`）：直接 inline 呼叫 `gmain_restart_from_save_flow()` 後留在選單。

→ **章節目錄的處理 = 進入前 `transition`，離開後恢復同一條時間線。回放的過場（走路徑 3 `ttmscript_show_dialog_action`）全部停記。不需要「恢復來源快照或新建歷史」的分支。**

### 0.11 UI：選項按鈕（原始座標、entry index、action id、enable gate）

用 `tools/text/menupage_translate.py` 的 codec 解出的**實際**結構（`scratchpad/pristine_menu/REQ_OPT*.DAT` 原版 + `dist/test_v100_zh/req_opt*.dat` 中文版，兩者結構一致）：

`MenuPage` 頁面框：`x=0, y=0, w=320, h=200`，`wBg_color=169`，`pTitle=0xFFFF`（無標題），`wEntry_count=7`。
`MenuEntry` 大小 0x21，`wAction_id` 在 entry 內 +2，rect 在 +11（`hhhh`），三個字串 slot 在 +19/+21/+23。

**REQ_OPT0.DAT（主選單，未載入遊戲）**

| idx | action | 掃描碼 | active | gate | rect (x,y,w,h) | 標籤 | 可見 |
|---|---|---|---|---|---|---|---|
| 0 | 0x31 | N | 1 | 0 | (118, **71**, 78, 15) | 開始新遊戲 | ✔ |
| 1 | 0x13 | R | 1 | 0 | (118, **87**, 78, 15) | 讀取進度 | ✔（`pEntries[1].wEnable_gate` 由程式改寫，見下） |
| 2 | 0x1F | S | **0** | **1** | (121, **145**, 78, 15) | （無） | ✘ 停用停放 |
| 3 | 0x19 | P | 1 | 0 | (118, **103**, 78, 15) | 偏好設定 | ✔ |
| 4 | 0x2E | C | 1 | 0 | (118, **119**, 78, 15) | 章節目錄 | ✔ |
| 5 | 0x20 | D | 1 | 0 | (118, **135**, 78, 15) | 退出至 DOS | ✔ |
| 6 | 0x12 | E | **0** | **1** | (145, **176**, 30, 15) | （無） | ✘ 停用停放 |

**REQ_OPT1.DAT（遊戲中，reentering）**

| idx | action | 掃描碼 | active | gate | rect (x,y,w,h) | 標籤 |
|---|---|---|---|---|---|---|
| 0 | 0x31 | N | 1 | 0 | (118, **60**, 78, 15) | 開始新遊戲 |
| 1 | 0x13 | R | 1 | 0 | (118, **76**, 78, 15) | 讀取進度 |
| 2 | 0x1F | S | 1 | 0 | (118, **92**, 78, 15) | 儲存進度 |
| 3 | 0x19 | P | 1 | 0 | (118, **108**, 78, 15) | 偏好設定 |
| 4 | 0x2E | C | 1 | 0 | (118, **124**, 78, 15) | 章節目錄 |
| 5 | 0x20 | D | 1 | 0 | (118, **140**, 78, 15) | 退出至 DOS |
| 6 | 0x12 | E | 1 | 0 | (140, **176**, 34, 15) | 取消 |

（設計文件第 2 節提醒過「截圖是放大畫面，不能當座標」——以上是 320×200 的實際 DAT 值。）

**`wAction_id` 就是 DOS 掃描碼**，`MENUPAGE.C:347-362` 直接拿 `g_key_scancode` 比對 `entry->wAction_id`。

**`wEnable_gate` 是完整的三重閘門（鍵盤／滑鼠／方向鍵都擋得住，已逐條驗證）**：

| 輸入方式 | 證據 | 行為 |
|---|---|---|
| 快捷鍵 | `MENUPAGE.C:355-362` | `wEnable_gate != 0` 且 type ∈ {0,1,3,4,6,7} → `key = 0`，**吞掉** |
| 滑鼠 hover / 點擊 | `MENUPAGE.C:457-463` | `wEnable_gate != 0` 且 type != 2 → 跳過 hit-test |
| Tab / Shift-Tab | `MENUPAGE.C:263, 278` | 只在 `wEnable_gate == 0` 的項目間循環 |
| 方向鍵 | `MENUPAGE.C:284` | 同上 |

→ **設計文件「按鈕停用；鍵盤也不能繞過停用狀態」的需求，用 `wEnable_gate = 1` 就完全滿足，不需改引擎。**

**`pEntries[N]` 的既有硬編碼依賴（插入新 entry 時的地雷）**

| 位置 | 程式碼 | 意義 |
|---|---|---|
| `MAINMENU.C:158/160` | `page->pEntries[1].wEnable_gate = (mainmenu_save_any_exists() != 0) ? 0 : 1;` | **`pEntries[1]` = 讀取進度**，依「有沒有存檔」開關 |
| `GMAIN.C:464-466` | `for (i = highest_slot; …) page->pEntries[i].wEnable_gate = 1;` | `contents.dat`（**另一個檔**，不受影響） |
| `GMAIN.C:479,496,513,530,547,…` | `page->pEntries[0..8].wEnable_gate` | 同上，`contents.dat` |

`req_opt*.dat` 上只有 `pEntries[1]` 這一個 index 依賴。**只要新 entry 插在 index ≥ 2，`pEntries[1]` 就不受影響。**

**新增按鈕的具體建議**

新 action id：**`0x32`（掃描碼 `M`，Message log）**。

- 檢查過的既有佔用：`req_opt*.dat` 用 `0x31, 0x13, 0x1F, 0x19, 0x2E, 0x20, 0x12`；`mainmenu_save_main_menu()` 的 `switch` 另外處理 `0x01`（ESC）與 `0x2F`（`mainmenu_save_show_ctrd_modal`）。存讀檔對話框的 `0xC2/0xC3` 屬於 `req_save.dat`／`req_load.dat`，不同頁面。
- `0x32` 在 `req_opt*.dat` 與 `mainmenu_save_main_menu()` 中**皆未使用**，`default: continue` 也不會誤觸其他功能。

現成的注入機制**已經存在**：`localization/translated/MENUPAGE.json` 有 `injected_entries` 與 `action_overrides` 兩個陣列，`menupage_translate.py` 的 `_inject_entries()`（:291-323）與 `_override_actions()`（:326-346）負責套用。既有先例：`REQ_CHET.DAT` 的「啟動進階密技中心」按鈕。

**套用順序（`cmd_build`，:388-391）：先套翻譯（用 pristine index）→ 再 `_override_actions` → 最後 `_inject_entries`。所以注入時 index 已是最終的。**

`injected_entries` 的 spec 欄位：`file`、`insert_at`、`copy_entry`、`action_id`、`rect[4]`、`label`/`primary`/`alt`、`notes`。**它只覆寫 `action_id`、rect、三個字串 slot；其餘欄位（含 `wWidget_type`、`bActive_flag`、`wEnable_gate`、`wClick_flags`、`wCursor_shape`）全部繼承 `copy_entry`。**

因此建議：

```jsonc
// REQ_OPT1.DAT（遊戲中，按鈕要可用）
{ "file": "REQ_OPT1.DAT", "insert_at": 7, "copy_entry": 2,   // 抄「儲存進度」→ 得到 active=1, gate=0
  "action_id": 50,                                            // 0x32 = M
  "rect": [118, 108, 78, 15], "primary": "訊息紀錄" }

// REQ_OPT0.DAT（主選單，按鈕要停用）
{ "file": "REQ_OPT0.DAT", "insert_at": 7, "copy_entry": 2,   // 抄那個停用停放的 Save → active=0, gate=1
  "action_id": 50,
  "rect": [121, 145, 78, 15], "primary": null }
```

- **`insert_at: 7`（附加在最後）而不是插在中間**，可同時保住 `pEntries[1]` 與**所有既有翻譯 entry index**（`MENUPAGE.json` 裡 `REQ_OPT1.DAT#0..#6#primary` 全部不用改）。視覺順序靠 rect 的 y 決定，不靠陣列順序（`menupage_draw_entries` 依陣列順序畫，重疊不會發生，因為 y 各不相同）。
- 視覺上要「在儲存進度之後、偏好設定之前」，所以 REQ_OPT1 需要把既有的偏好設定/章節目錄/退出各往下移 16px：

  | entry | 現 y | 新 y |
  |---|---|---|
  | 3 偏好設定 | 108 | **124** |
  | 4 章節目錄 | 124 | **140** |
  | 5 退出至 DOS | 140 | **156** |
  | 6 取消 | 176 | 176（不動） |
  | 新 訊息紀錄 | — | **108** |

  退出至 DOS 的底邊 = 156+15 = 171 < 176，**放得下，不會壓到取消**。
- **第 0 階段發現的阻礙（第 4 階段已解決）**：`menupage_translate.py` 當時沒有修改既有 entry rect 的機制；現已加入帶 `expected_rect` 驗證的 `rect_overrides`，沒有手改 `dist/` DAT。
- **REQ_OPT0 的停放 rect**：抄用既有 Save 的 (121,145,78,15)。注意它與「退出至 DOS」(118,135,78,15) 在 y 上本來就重疊（135-150 vs 145-160）——**這是原版遊戲既有的做法**，因為 `wEnable_gate=1` 已經讓它完全不參與 hit-test 與繪製（`primary=null` 也沒有字可畫）。第 4 階段仍應實機截圖確認沒有殘影。

**overlay 說明模式的缺口**：`mainmenu_save_main_menu()` 的每個 case 開頭都有 `if (overlay != 0) { dialog_play_record(0x7X, 1); continue; }`，7 個按鈕各自對應 `0x73`-`0x79`。新按鈕**沒有**對應的說明記錄。要補一筆就得在 `DIAL_Z00.DDX` **新增**一筆 record——而 HANDOFF 教訓 2 明載 DDX 改動必須維持原始 byte 長度、否則 offset 連鎖錯位。`ddx_pack.py` 是否支援「新增 record 並重建目錄與所有 offset」**尚未確認**。見 0.12 未解事項。

### 0.12 可借用的 renderer / modal、makefile 加檔方式、記憶體餘量

**可借用的純閱讀畫面**

| 候選 | 位置 | 評語 |
|---|---|---|
| `BOOKVIEW.C`（232 行） | `bookview_init/show/shutdown`、`bookview_load_page_directory`、`bookview_find_page_by_number` | **最貼近的範本**：本來就是「載入一份分頁資料 → 只讀顯示 → 翻頁 → 關閉」，而且**不執行 DDX 事件**。第 4 階段的 `MSGVIEW.C` 建議照它的骨架寫 |
| `MenuPage`（`MENUPAGE.C` + `menupage_load/begin/draw/run/end/free`） | 清單頁的按鈕（上一頁／下一頁／閱讀／返回）用它最省事，且 `wEnable_gate` 開關現成 | 需要新的 `req_*.dat`，會進 build manifest |
| `ListWidget`（`LISTWDG.C`，`listwidget_attach/insert_item/get_current_entry/set_selection/destroy`） | 存讀檔對話框在用（`MAINMENU.C:1992`） | 清單頁可直接沿用 |
| `textwrap_draw_aligned()` | 內容頁分頁 | **共用全域** `g_wTextWrapLinesDrawn/Remaining/XAccum` 與 `g_bMixedZhMode/g_bSmallZhMode` — viewer 期間必須保存／還原，且**viewer 開啟時必須抑制擷取**（否則 viewer 自己畫的字會被記進歷史） |

**Modal 進出規則**：`worldloop_mouselook_release_for_modal()`（`WORLDLP.C:124-130`）是既有的統一入口，`dialog_play_record()`（:1018）與 `dialog_show_by_key()`（:833）開頭都呼叫它。**新 viewer 開啟時照做即可。** 它會檢查 `g_pMouseLookCaptureActive`／`g_pMouseLookUiX`／`g_pMouseLookUiY` 是否為 NULL，安全。

**makefile 加檔方式（三處都要改，缺一不可）**

1. `bak/SRC/<模組>/<模組>.MAK`：加進 `<模組>_OBJS` 變數，並補一條規則。格式（抄 `DIALOG.MAK`）：
   ```make
   DIALOG_OBJS = OUT\ASKABOUT.OBJ OUT\DIALOG.OBJ OUT\EVTCOND.OBJ OUT\MSGLOG.OBJ
   OUT\MSGLOG.OBJ : SRC\DIALOG\MSGLOG.C
       $(C_3O1Y) $(INC) -c -zCS<XXXX>_TEXT -nOUT SRC\DIALOG\MSGLOG.C
   ```
   `-zC<class>` 是**每個原始檔各自的程式碼段名稱**，原版都是為了 byte-match 而挑的。**新檔沒有 byte-match 需求，可以沿用同模組既有的 class 或另取一個新名**——第 1 階段要實測連結器接受哪一種，並記錄結果。
2. `bak/MAKEFILE`：加進 `KVMOBJ`（bc31 編的 C，絕大多數）或 `TCGOBJ`（bc30/bc20 編的）清單。新的 C 檔用 `C_3O1Y`（bc31）→ 放 `KVMOBJ`。
3. `bak/KRONDOR.RSP` **和** `bak/KRN102.RSP`：加進物件清單。

**Overlay 分帶（`KRONDOR.RSP`）**

```
行 1-44    常駐（含 MENUPAGE.OBJ:40）
行 45      /o+     ← overlay 帶開始
行 46-121  overlay（SAVEGAME:55、DIALOG:68、TEXTWRAP:70、TOWNSCN:74、MAINMENU:106 都在這裡）
行 122     /o-+    ← overlay 帶結束
行 123-243 常駐（GFXCTX、驅動、音效…）
```

→ **`MSGLOG.OBJ` 與 `MSGVIEW.OBJ` 都應放在 46-121 這一帶**（與呼叫它們的 DIALOG／MAINMENU／SAVEGAME 同帶），只有全域變數常駐，程式碼可換出。

**near / far 記憶體餘量（**這是本功能最大的技術風險**）**

| 事實 | 證據 |
|---|---|
| `krondor.exe` 原版 453904 → 中文版 458992 bytes（+5 KB 常駐） | HANDOFF「神殿場景點」章節；目前 `dist/test_v100_zh/krondor.exe` = 468720 bytes（`2c55433` 重編後又長了 ~10 KB） |
| **2026-08-31 曾因傳統記憶體不足而三重錯誤重置**：`czone_subsystem_init()` 要 `0xf308` = 62216 bytes 連續傳統記憶體，實測 `largest_free = 59232`，**差 ~3 KB** | HANDOFF 同章節 |
| 修法是 `alloc_far_umb()`（`DOSMEM.C:18`），**只在那一次呼叫**期間 link DOS UMB chain（INT 21h AX=5803h BX=1）+ first-fit high（AX=5801h BX=80h），配置完立刻還原 | `bak/SRC/SYS/DOSMEM.C` |
| 需要 conf 有 `[dos] dos=high,umb`。`dist/dosbox_zh_test.conf` 有；**`tools/release/dosbox_krondor.conf.template` 沒有** | 本階段實際 grep 確認 |

> **結論：傳統記憶體幾乎沒有餘裕。** 第 1 階段的 MLG 核心必須：
> - 常駐（DS）佔用壓到最小——**不要**開 near 陣列，狀態結構只放指標與少量純量。
> - I/O 緩衝用 `alloc_far()`，**大小 4 KiB 起跳、上限 8 KiB**（設計文件的建議值），**不要**開 15 KiB 以上。
> - 若 `alloc_far` 失敗，考慮 `alloc_far_umb()` 後援（既有函式，DOSMEM.H 已導出），但**不要**改成全域配置策略（HANDOFF 記載 `17e0f24` 那版全域改策略是被否決的做法）。
> - **實際量測方式**：`bak build` 後看 `OUT\KRONDOR.MAP`（`KRONDOR.RSP` 已指定產出 MAP 檔）的 DGROUP 大小，並比較 EXE 大小差。第 1 階段必須記錄這兩個數字。

**`g_pMainScratchBuf` 是三方共用的（**擷取實作的關鍵陷阱**）**

```
BOOT.C:206      g_pCodecScratchFp = g_pMainScratchBuf = alloc_far(0x3c8c, 0);   // 15500 bytes
DIALOG.C:685-743  展開後的對話全文寫在這裡
SAVEGAME.C:58,60  savegame_write/read 的 15000-byte 區塊 I/O 緩衝
MODALSCR.C / BLITAA.C / POLYRAST.ASM  也在用
```

→ **擷取時必須立刻把本文複製到自己的緩衝**；**MLG 的寫入絕對不能借用 `g_pMainScratchBuf`**（`savegame_write()` 正在用它搬 `TEMP.GAM`）。同理，`dialog_render_text_with_tokens()` 展開後的字串長度上限 = 15499 bytes，這也是單筆事件本文的天然上限。

### 0.13 至少 6 個可重現的遊戲案例

以下每個都附「怎麼觸發」與「原始碼證據」，第 3–5 階段可直接拿來當驗收腳本。

| # | 案例 | 觸發步驟 | 期待（第一版） | 原始碼證據 |
|---|---|---|---|---|
| 1 | **NPC 話題對話（Who + 玩家選擇）** | 第 1 章任一城鎮找可交談 NPC → 出現話題頁 → 選一個話題 → 讀完 → 選「道別」 | 一筆 conversation，含 NPC 名（來自 `wSpeaker_id` → KEYWORD 表）、玩家選中的話題標籤、NPC 回答全文。**未選的話題不入紀錄；「道別」不記成已選話題** | `DIALOG.C:1522-1530`（0x400 分支）、`ASKABOUT.C:319-364`、`ASKABOUT.C:310`「道別」 |
| 2 | **多頁中文對話（翻頁去重）** | 找一段長對話（例如 `DIAL_Z16` node 1600006/1600007 Arutha/Locklear 王宮場景，HANDOFF archive 記載它需要多頁），按空白／點擊逐頁翻完 | 全文完整、無重複、無半個中文字、無「還沒顯示就先記」 | `DIALOG.C:1554-1573` 翻頁迴圈、`TEXTWRAP.C:148-193` 分頁、`TTMDLG.C:103-119` |
| 3 | **旅店：任務消息 vs 住宿交易** | 旅店裡先和老闆談任務／傳聞（例：`0x47` 樂手／娛樂基金劇情），再去櫃檯住宿到確認扣錢 | 任務對話**收錄**；住宿確認（`0x13d672` 及 `0x13d65e/0x13d661` 餘額不足／取消）**排除** | `TOWNSCN.C` `0x47`；`MODALSCR.C:793` `dialog_play_record(0x13d672, 0)`、`MODALSCR.C:720` `modalscreen_rest_until_time` |
| 4 | **商店買賣（純交易 + 證明 `@N` 不是說話者）** | 進商店賣一件物品，看到 `"I can offer only <金額> for it," explained the <商人>.` | 該筆**排除**。且第 3 階段的 decoder 要能證明 `@1` 展開成金額字串而不是人名 | `SHOP.C` `dialog_play_record(0x1b7756, 0)`；`DIAL_Z18.json` node 1800022；`DIALOG.C:554`（kind 19 = `gstate_format_money`） |
| 5 | **章節橫幅 vs 真正的換章敘事** | (a) 讀一份第 3 章存檔 → 大地圖上出現「Chapter Three: The Spyglass and the Spider」橫幅。(b) 在遊戲中正常打完第 1 章 → 換章 | (a) 橫幅**不入紀錄**（在 `savegame_read` 之前、`transition` 內）。(b) 換章後 `savegame_chapter_start_dispatch()` 結尾的敘事**入紀錄** | `GMAIN.C:178`（橫幅，在 `:189` 的 `savegame_read` 之前）、`SAVEGAME.C:249`（`dialog_play_record(0x1e8497L, 0)`，在 read 之後）；`DIAL_Z00.json` node 296 = Chapter Three 橫幅原文 |
| 6 | **章節目錄回放（不得污染時間線）** | 遊戲中開選項 → 章節目錄 → 點一個已解鎖章節看過場 → 退出 → 回到遊戲 | 過場文字**全部不入紀錄**；回到遊戲後歷史與進入前**完全相同**（不是新分支） | `MAINMENU.C:261-266`（`mainmenu_save_party_to_tmp(); result=4`）、`GMAIN.C:417-699`（無 `savegame_read`）、`GMAIN.C:109-110`（`iMode==4` → `path=NULL`） |
| 7 | **A/B/C 存檔分支** | 看到訊息 1..10 → 存 A → 再看 11、12 → 存 B → 讀 A（只剩 1..10）→ 看 13 → 存 C | A=1..10、B=1..12、C=1..10+13，A 不變 | 設計文件第 5 節；`MAINMENU.C:967-989` 手動存檔、`GMAIN.C:100-108` 讀檔路徑 |
| 8 | **世界物件旁白（動態 key）** | 在野外點一個可互動熱區（例如新翻的土堆 `0x9b`、路標 `0x61`） | 收錄為「旁白」（`wSpeaker_id == 0` → `pSpeakerName == NULL`） | `WCURSOR.C:1113` `0x9b`、`WCURSOR.C:1290` `0x61`；`ASKABOUT.C:69-70`（id==0 回 NULL） |
| 9 | **城鎮場景說明條（第 4 條顯示路徑 + 地名來源）** | 進入一個店鋪／室內場景，看下方說明條（例：`#三山當鋪#` + 場景描述），若很長就翻頁 | 標題可當 Where 的顯示名；說明本文只記已顯示頁、重複重畫不重記 | `TOWNSCN.C:373-426`；`DIAL_Z13.json` node 1300001 標題 `#Three Hillmen Pawn#` |
| 10 | **戰後能力提升訊息（系統，排除）** | 打完一場戰鬥，看到「隊伍的各項能力都提升了。」 | **排除**。順帶檢查它走的是強制小字路徑，不影響擷取 | `EVTCOND.C:357,359`（`0x200b30`-`0x200b33`）；`DIALOG.C:761-767` 強制 `g_bSmallZhMode` |

### 0.14 未解事項（**不得在實作中猜測**）

| # | 項目 | 影響 | 建議處理階段 |
|---|---|---|---|
| U1 | **WSL 建置 clone 有 136 commit 落後 + 7 檔 VESA/EVG WIP（含 `DIALOG.C`／`TEXTWRAP.C`／`FONT.C`）**，且 HANDOFF 的 `reset --hard d702c75` 已過期 | 第一次建置就可能衝突或誤刪使用者 WIP | **第 1 階段開始前先問使用者**：要 stash/pop，還是另開乾淨 clone |
| U4 | **`gettime()` 在本引擎尚未被使用過** | 秒級時間戳是設計要求 | 第 1 階段第一次寫時間戳時實機印值確認 |
| U5 | **`fmap_twn.dat` 城鎮名無法在對話當下讀取**（只在大地圖畫面存在，`fmap_hotspots_unload()` 會釋放） | 野外地點只能顯示「區域 N」 | 第 3 階段：要嘛接受「區域 N」，要嘛做建置期的 (x,y)→城鎮 index 對照表 |
| U7 | **`TEXTWRAP.C` 需不需要加 `g_wTextWrapByteStart/End`**（見 0.5） | 決定擷取是「零成本讀全域」還是「重算一次 compute_lines」 | 第 3 階段擇一，兩者都可行 |
| U8 | **`-zC<class>` 段名要不要為新檔另取** | 連結器可能拒絕重複／未知段名 | 第 1 階段實測記錄 |
| U9 | **傳統記憶體只剩約 3 KB 的臨界餘裕**（見 0.12） | 加了模組可能重現 2026-08-31 的三重錯誤重置 | 第 1 階段量測 `KRONDOR.MAP` 的 DGROUP 與 EXE 大小；第 5 階段做多場景進出回歸 |
| U10 | **`tools/release/dosbox_krondor.conf.template` 缺 `[dos]` 區塊** | 發布包的 UMB 後援失效 | 第 7 階段（也是 HANDOFF 早已記錄的待辦） |
| U11 | **手動存檔／書籤原本就沒有暫存與備份**（`savegame_write` 直接覆寫正式檔） | 第 2 階段的協調器會順帶修好；報告不可寫成「原本安全」 | 第 2 階段如實記錄 |
| U12 | **`mainmenu_*_recover_files()` 在 target 存在時直接 `remove(backup)`** | 新協議若還需要那份 backup 還原 `.MLG`，會被先刪掉 | 第 2 階段必須改寫恢復順序 |

### 0.15 完成門檻自評

| 門檻 | 狀態 |
|---|---|
| 存檔所有路徑能以原始碼支持 | ✔ 見 0.6，`savegame_write`/`savegame_read` 的呼叫者已列全（`grep -rn` 全 `bak/`），無漏網寫入路徑 |
| 文本擷取位置能以原始碼支持 | ✔ 見 0.5，四條顯示路徑匯流於 `dialog_render_text_with_tokens()`，擷取點在 `DIALOG.C:743` 之後 |
| 沒有修改正式遊戲行為 | ✔ **本階段只新增本文件一個檔案**。兩個 repo 的 `.C`/`.H`/資源/工具檔皆未變動。使用者正在跑的 DOSBox-X 實例未被下斷點、未被中止 |
| 未做的實機驗證明確標未驗證 | ✔ 見 U4、U7-U9；DOSBox-X 日期時間**已驗證**（0.4） |

### 0.16 第 1 階段起點建議

**先做與 UI／對話 VM 完全分離的資料核心，第一步只碰兩個新檔：**

1. **`upstream/betrayal-at-krondor/bak/SRC/DIALOG/MSGLOG.C` / `MSGLOG.H`**（新檔，放 DIALOG 模組是因為 `DIALOG.MAK` 最小、且 `DIALOG.OBJ` 已在 overlay 帶內）。
   - 第一輪**只實作純資料層**：header 讀寫、事件 append/scan、CRC32、分塊 I/O、邊界檢查。
   - **先不要 `#include` 任何 DIALOG/MAINMENU 的東西**，只依賴 `SRC/IO/DOSRW.H`（`dos_read`/`dos_write`）、`SRC/SYS/DOSMEM.H`（`alloc_far`/`alloc_far_umb`/`_freemem`）與 C RTL。
   - I/O 緩衝 4–8 KiB，用 `alloc_far()`，**絕不碰 `g_pMainScratchBuf`**（理由見 0.12）。
2. **`tools/text/message_log.py`** + **`tests/unit/test_message_log.py`**（主 repo），Python decoder/validator，共用 `tools/font/build_font.py` 的 `encode_string`/`decode_string` 與 `localization/generated/zh_mapping.json`（mapping 指紋由此生成常數）。
3. **格式規格另寫 `docs/research/message-log-format.md`**（byte offset 表 + 至少兩份可手算的 golden fixture）。

**第一次建置的驗證重點**（照 0.3 的修正版命令，且先解決 U1）：
- `VMCODE.OVL` / `SX.OVL` 必須維持 `✅ BYTE-IDENTICAL`
- 記錄 `OUT\KRONDOR.MAP` 的 DGROUP 大小與 `KRONDOR.EXE` 大小（與 468720 比較），量出常駐增量（U9）
- 記錄 `-zC<class>` 段名的實測結果（U8）

**第 1 階段不要碰的**：`DIALOG.C`、`MAINMENU.C`、`SAVEGAME.C`、`GMAIN.C`、`TEXTWRAP.C`、`req_opt*.dat`、`MENUPAGE.json`。這些全部留到第 2–4 階段。

---

## 第 1 階段：格式與資料核心（中斷後續作）

- **狀態**：資料核心、跨語言互讀與完整引擎編譯已驗證；尚未接入遊戲，實際時鐘取得與遊戲記憶體壓力驗證待補，不代表整個訊息紀錄功能完成。
- **日期**：2026-09-06。
- **基準**：主 repo `df989af`、Windows 引擎與獨立 WSL clone `5c3ed49`。本功能原始碼仍為未提交修改／未追蹤檔；本次沒有 commit、更新正式補丁或發布包。
- **工作範圍**：接手前一 agent 在新增 corrupt-snapshot driver/test 時用盡 context 的現場，補完測試並驗證現有第 1 階段成果；沒有開始第 2 階段存檔協調器。

### 1.1 現有實作檔案

| 檔案 | 用途 |
|---|---|
| `bak/SRC/DIALOG/MSGLOG.C/.H`（引擎） | MLG v1 檔案核心、CRC、事件追加／掃描、工作檔恢復、snapshot prepare/candidate/activate、抑制狀態機 |
| `bak/TOOLS/MLGTEST.C` | 真正 DOS C 測試程式，直接連結上述核心 |
| `bak/MAKEFILE`、`bak/TOOLS/TOOLS.MAK` | 新增 `mlgtest` target |
| `bak/SRC/DIALOG/DIALOG.MAK`、`bak/KRONDOR.RSP`、`bak/KRN102.RSP` | 將核心加入引擎物件與 overlay 連結；本次只驗證 v1.00 建置 |
| `tools/text/message_log.py` | Python codec／validator／fixture／UTF-8 診斷工具 |
| `tools/text/mlg_dos_check.py` | FreeDOS/Borland 與 Python 雙向契約驗證 |
| `tests/unit/test_message_log.py`、`tests/fixtures/message_log/*.mlg.hex` | 44 項單元測試與 4 份 hex fixture |
| `docs/research/message-log-format.md` | v1 byte layout、限制、校驗範圍與狀態機 |

### 1.2 本次發現與修復

1. 前一 agent 用 `str.replace()` 插入 `BADLENS.MLG` 執行命令時未匹配原文：檔案有產生，但 `_batch()` 沒有 `CAND` 命令。已真正加入 `CAND \\BADLENS.MLG 1 2`。
2. `SCRIPTED_CREATED` 雖已 import，建立時間斷言沒有插入。已補上 snapshot `created_time` 比對，以及工作歷史／快照 data region 完全相等檢查。
3. candidate 原本只在整份 log 搜尋成功／失敗字串，可能由另一案例的輸出冒充。改為核對按 batch 順序的完整 5 個結果：`0, -13, -8, 0, -12`。
4. Windows `MSGLOG.C` 已有還原 `g_mlgCreated` 的修正，但 WSL 副本還少那段。先確認差異，再同步到獨立 `~/krondor-build-msglog`，DOS 重建確實包含該修正。
5. 最新 core overlay 大小與格式文件先前數字不同，已更新為 8157 bytes；舊常駐增量數字標明未在本次重做基準對照。

### 1.3 可重跑命令與實際結果

Windows 主 repo：

```powershell
python -m unittest tests.unit.test_message_log
python -m unittest discover -s tests/unit
```

- 訊息紀錄：**44 tests，OK**，包含重新計算 data CRC 後仍因中途 record length 損壞而拒絕快照的案例。
- 全專案 discovery：**157 tests，errors=1，skipped=1**；唯一 error 仍為既有 `test_overhead_map_controls` 無法 import `pytest`。不是全數通過。未為本功能擅自安裝套件。

在 WSL shell 的獨立 clone 執行：

```bash
cd ~/krondor-build-msglog
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain /home/pmanyeh/.local/bin/uv run python /mnt/d/git/betrayal-at-krondor-for-zh/tools/text/mlg_dos_check.py
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain /home/pmanyeh/.local/bin/uv run bak build
```

- `mlgtest` 由 Borland C++ 3.1／Turbo Link 5.1 編譯並在 FreeDOS 執行，driver 結果 **ALL CHECKS PASSED**。
- C 產生的 `CGEN.MLG` **1141 bytes**，與 Python scripted fixture 完全相同；7 個事件、中文安全分片、建立時間與本文保留通過。
- Python → C：有效 fixture、超過 64 KiB 的 180 事件檔、snapshot 綁定／啟用、11 種錯誤工作檔，以及結構損壞 snapshot 皆得到預期結果。
- `BADLENS.MLG` 全歷史 CRC 已按損壞資料重算，DOS 仍回 **MSGLOG_E_RANGE (-12)**，證明不是僅靠整檔 CRC 驗證。
- split 邊界與 FAILED 狀態不因進出 viewer 而恢復 ACTIVE 的實際 DOS 測試通過。
- 完整 v1.00 引擎編譯／連結完成。建置工具仍顯示 EXE 與原版不同，這是本專案繁中／功能修改的預期結果；兩個 OVL 均 **BYTE-IDENTICAL**。

### 1.4 產物與資源證據

產物在 `/home/pmanyeh/krondor-build-msglog/work/`，未複製到正式遊戲目錄：

| 產物 | bytes | SHA-256 |
|---|---:|---|
| `KRONDOR.EXE` | 483760 | `b0f58638f057b568a762be141160bdd7b3cc56cfe6550380ed1b6ae65fc5ccc0` |
| `VMCODE.OVL` | 44582 | `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0` |
| `SX.OVL` | 40742 | `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb` |

- 完整建置 log：`work/msglog-resume-build.log`。
- DOS 編譯 log：`work/MLGT.LOG`；DOS 執行 log 與互讀產物：`work/mlgout/MLG.LOG`、`work/mlgout/*.MLG`。
- `work/KRONDOR.MAP`：`MSGLOG_TEXT` stub = `0xCF`（207 bytes）、overlay = `0x1FDD`（8157 bytes）；`_DATA` = `0x3DE0`、`_BSS` = `0x2A44`、`_STACK` = `0x80`。
- 本次未重新建無 MSGLOG 的對照版本，不能把總 DGROUP／EXE 大小當新增量；也不能把資料核心零自行配置當成未來整個功能零 RAM。
- 獨立 clone 已存在，直接沿用即可。第 0 階段要求先詢問是否建立 clone 的舊建議已無需執行；不要動 `~/krondor-build` 的 VESA/EVG WIP，也不要照抄舊 reset/stash 指令。

### 1.5 尚未完成與下一個起點

- **真實時間取得**：核心目前由呼叫者傳入 `MsgLogTime`；DOS fixture 使用固定時間，證明的是序列化與保留，不是 `gettime()` 或宿主同步。第 0 階段的 DOSBox-X shell 時間實測仍有效，但引擎取得秒級時間的那一項尚未驗證；接入擷取時需要補。
- **實際遊戲啟動／連續記憶體餘量**：本次是 FreeDOS 測試程式與完整引擎建置，尚未以這份新 EXE 在 DOSBox-X 跑場景壓力／UI。不能把 ALL CHECKS PASSED 說成玩家功能已實機驗收。
- **scratch 所有權**：目前核心由呼叫者 `msglog_set_scratch()` 提供區塊緩衝，沒有自行配置；第 2 階段需決定安全配置／釋放時機，不能借用存檔正在使用的 `g_pMainScratchBuf`。
- **未接入功能**：不曾修改 `DIALOG.C`／`MAINMENU.C`／`SAVEGAME.C`／`GMAIN.C` 或選項資源；目前不會自動記錄對話，也沒有玩家入口。
- **第 2 階段起點**：先讀格式文件與 `msglog_prepare_snapshot`／candidate／activate API（依 header 中實際名字），實作共同 pair-save 與可恢復交易，覆蓋手動、書籤、自存、快存；現有 snapshot API 不等於已實現 GAM+MLG 成對提交。使用合成事件驗證 A/B/C，之後才進行第 3 階段文本 hook。
- **交付狀態**：所有原始碼仍未提交。後續 agent 先看兩個 repo status，不能漏掉未追蹤的 C/H 或把 `.pytest-*` 目錄納入本功能。

---

## 第 2 階段：保存／載入與時間線（第一輪）

- **狀態**：進行中。成對提交、基本恢復、四個寫入入口與讀檔切換已實作；DOS 合成測試和 v1.00 完整建置通過。尚缺完整 I/O 故障矩陣、v1.02 建置與遊戲內實機存讀檔，因此不能標為完成。
- **日期**：2026-09-06。
- **基準**：主 repo `df989af`；Windows 引擎與獨立 WSL clone 起點 `5c3ed49`。仍未 commit、未更新正式 engine patch、未封裝發布。

### 2.1 本輪實作

- 新增引擎 `SRC/DIALOG/MSGSAVE.C/.H`，負責目前工作時間線、DOS `getdate/gettime`、GAM 指紋、MLG snapshot，以及 GAM/MLG 成對提交與載入候選。
- 每個目標存檔目錄使用 DOS 8.3 內部檔：`MLGNEW.GAM`、`MLGNEW.MLG`、`MLGOLD.GAM`、`MLGOLD.MLG`、`MLGTXN.DAT`。交易標記含目標槽、舊檔存在狀態、新 GAM 長度／CRC 與標記 checksum。
- 提交前驗證新 GAM 在既有大小範圍且 header version 為 `0x16`，再建立並重新驗證綁定 snapshot。只有新對檔完整有效才清理舊備份。
- 啟動恢復依實際檔案狀態處理：正式位置已是完整新對時完成提交；否則回復完整舊對。恢復可重跑，不用交易 phase 欄位猜測最後完成的 rename。
- `MAINMENU.C` 的手動存檔、書籤、自動存檔、快速存檔均改走 `msgsave_write_pair()`。單檔刪除同步刪除同槽 MLG；整目錄原本的 `*.*` 遞迴刪除可包含 MLG。
- 存檔列舉及 F9 快讀選槽前會先嘗試恢復該目錄的中斷交易。既有 autosave/quicksave 舊版 `AUTOBnn/QSBnn` 恢復仍保留，兼容先前版本殘檔。
- `GMAIN.C` 在啟動初始化／退出關閉訊息系統。新遊戲成功讀入 `STARTUP.GAM` 後建立新工作時間線；讀既有存檔先驗證候選，GAM 成功後才啟用；取消或 GAM 載入失敗不切換。MLG 缺失／損壞／錯配時載入 GAM，建立含一筆 GAP 的新歷史。
- 讀檔前章節展示位於 transition 抑制範圍內，不會寫進剛離開的時間線。第 3 階段接上文本擷取後，仍須為真正的新遊戲／自然換章劇情確認收錄時機。

建置檔已加入 `MSGSAVE.OBJ`；另新增 DOS 測試 `TOOLS/MSGPTEST.C`、`msgptest` target 及主 repo driver `tools/text/msgpair_dos_check.py`。

### 2.2 DOS 測試證據

執行：

```bash
cd ~/krondor-build-msglog
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain /home/pmanyeh/.local/bin/uv run python /mnt/d/git/betrayal-at-krondor-for-zh/tools/text/msgpair_dos_check.py
```

結果：`ALL PAIR CHECKS PASSED`。測試程式由 Borland C++ 3.1 編譯並在 FreeDOS 執行，使用符合現有 GAM 最小長度和 `0x16` header version 的合成 GAM。

- A=1 筆，B=2 筆；讀回 A 後追加另一筆，C=2 筆，證明讀檔回到當時且分支不混入 B 後段。
- 覆蓋 A 成功。
- 模擬在交易標記建立、舊 GAM 備份、舊 MLG 備份、新 GAM 就位、新 MLG 就位後各自斷電（步驟 7–11）。步驟 7–10 恢復完整舊對；步驟 11 偵測完整新對並完成提交。
- 刪除 A 的 MLG 再載入：GAM 可用，工作歷史只有 GAP，header `HAS_GAP` 設起。
- 第一次測試因 32 MB build image 剩餘空間不足，第三個完整合成 GAM 寫入失敗；正式槽未留下半對檔案。測試後調整為每個分支驗證完即刪除不再需要的合成槽，最終全數通過。這同時提供了早期寫入失敗的實際降級證據，但不取代完整 fault injection。
- DOS `getdate/gettime` 經 MLG header 往返解析為 `2026-09-06 14:27:03`，與宿主差 2 秒；秒級現實時間取得已從「推定」提升為 DOS C 實測。

測試專用 `MSGSAVE_TEST` 只在單一測試編譯單元啟用，正式引擎不包含斷電注入全域或分支。

### 2.3 編譯與產物

v1.00 完整建置命令：

```bash
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain /home/pmanyeh/.local/bin/uv run bak build
```

---

## 第 3 階段：NPC、選項、劇情擷取

- **狀態**：工程實作完成，待遊戲內驗收。擷取核心、主要顯示入口、選項確認、場景說明與完整來源分類已接入；DOS 合成驗證、來源掃描與 v1.00 完整建置通過。戰鬥、法術與謎題訊息依產品決策全部排除，分類政策無未決項。尚缺可互動 DOSBox-X 工具才能逐句對照實際遊戲畫面與蒐集六類驗收證據。
- **日期**：2026-09-06。

### 3.1 本輪實作

- `TEXTWRAP.C` 在既有分頁結果之外輸出 `g_wTextWrapByteStart/End`。值直接取本頁第一行的 `start` 與最後一行的 `end`，所以擷取的是 token 已展開後、這次實際畫出的 byte 範圍；沒有畫出任何行時兩者都為 0。
- 新增 `SRC/DIALOG/MSGCAP.C/.H`。模組在 append 前立即快照 DOS `getdate/gettime`、章節、zone、scene、解析後說話者與地點，不保存 DDX／KEYWORD 暫存指標。
- `dialog_play_record()` 以最外層函式生命週期建立／關閉 conversation。每個實際顯示的 DDX record 更新 source key 與說話者，所有既有清理出口都先平衡 capture scope。
- `dialog_show_by_key()` 與 `TTMDLG.C` 的直接／腳本過場路徑建立各自 conversation；`TOWNSCN.C` 的說明條使用獨立 `SCENE` event。章節目錄回放期間由 transition counter 抑制，離開後恢復原記錄狀態。
- 頁面 append 發生在正文 `textwrap_draw_aligned()` 完成之後、`g_pMainScratchBuf` 被其他系統覆寫之前。去重以同一 display instance 已寫入的最大 byte end 為準，因此陰影正文只記一次、scroll=0 重畫不記、翻回舊頁不記；下一個 DDX record 或下一輪重訪會取得新 display id。
- Ask-About 只在 `askabout_dialog_run()` 回傳已確認 index 後查出該 topic 標籤並 append。一般選單頁也只在 `askabout_menu_page_run_selection()` 返回後記錄；隊員選擇的取消結果不記。
- Who 只使用正規化後 `wSpeaker_id` 與 `askabout_name_or_keyword_lookup()` 的結果。`@0..@5` 仍由原 renderer 展開到本文，沒有被當成說話者；無顯示姓名時設 narration flag。
- Where 在場景內優先使用 `#標題#`，並保存 `scene_id=(scene kind<<8)|scene index`；同場景內沒有標題的 actor 說明沿用場景標題。其他位置先採穩定的 ASCII `Zone N` fallback。
- 來源政策新增 `message-log-source-policy.json`，由 `tools/text/message_log_sources.py` 產生 DOS 8.3 相容的 `CAPCLASS.INC`。明確排除選單／存讀錯誤、書籤提示、Game Over、旅店／神殿／治療交易、商店／物品系統、戰後能力提示，以及所有已定位的戰鬥、法術與謎題訊息。`--check` 與單元測試會阻止政策和 C 產物漂移。
- 來源政策的 `unresolved` 為空。測試會遞迴掃描整個 `SRC/COMBAT`，並掃描 `CIPHER.C`、`PICKLOCK.C` 內所有 literal `dialog_play_record()` 呼叫，要求每個 key 都被排除；`CIPHER.C` 的動態謎題正文直接走底層 renderer，沒有 capture hook，另以 `excluded_direct_paths` 記錄。

### 3.2 DOS capture 驗證

新增 `TOOLS/CAPTEST.C`、`msgcaptest` target 與 `tools/text/msgcap_dos_check.py`。執行：

```bash
cd ~/krondor-build-msglog
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain /home/pmanyeh/.local/bin/uv run python /mnt/d/git/betrayal-at-krondor-for-zh/tools/text/msgcap_dos_check.py
```

結果：`ALL CAPTURE CHECKS PASSED`。

- 兩個可見 span 分別寫成 `first`、`second`；相同第一頁重畫與翻回第一頁都回 `MSGLOG_E_SUPPRESSED (-16)`。
- 實際確認的 `Topic` 形成一筆 `CHOICE`；商店交易來源 `1800022` 的 scope、文字與選項全數抑制。
- 戰鬥來源 `254`、法術來源 `199`、謎題來源 `11` 在 DOS classifier probe 中都回 `MSGLOG_E_SUPPRESSED (-16)`，證明生成後的 C 分類表在實際 DOS 程式中生效。
- 場景 `0x1301`、來源 `1300001` 只寫一筆 `SCENE`，Where 為當下標題 `Inn`；重畫不追加。
- DOS 產物由 Python 完整驗證 CRC 與結構，事件順序為 `CONV_BEGIN, TEXT, TEXT, CHOICE, CONV_END, SCENE`，共 6 筆。NPC span 的 Who=`NPC`、Where=`Zone 9`、chapter=3、zone=9。
- `msgpair_dos_check.py` 在加入 capture 初始化後重跑，結果仍為 `ALL PAIR CHECKS PASSED`。

單元測試：訊息格式 44 項加來源政策 5 項，共 **49 tests，OK**。來源測試包含整個 combat source tree 與兩個謎題 C 檔的 literal key 全量掃描。全專案 discovery 為 **162 tests，errors=1，skipped=1**；唯一 error 仍是既有 `test_overhead_map_controls` 缺少 `pytest`，與本功能無關。

### 3.3 v1.00 建置與資源

完整建置 log：`~/krondor-build-msglog/msgcap-phase3-final.log`。

| 產物 | bytes | SHA-256 |
|---|---:|---|
| `KRONDOR.EXE` | 489632 | `9a166a416e0df291041ab88aa08e0535a5d13e22328af61fdddc8bd169c4b5cf` |
| `VMCODE.OVL` | 44582 | `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0` |
| `SX.OVL` | 40742 | `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb` |

- `MSGCAP_TEXT` stub=`0x4D`、overlay=`0x6F9`；`MSGLOG_TEXT` stub=`0xCF`、overlay=`0x1FDD`；`MSGSAVE_TEXT` stub=`0x48`、overlay=`0xC38`。
- `_DATA=0x3E80`、`_BSS=0x2AE8`、`_STACK=0x80`。capture 新增的常駐資料主要是 64-byte speaker／location 快照與少量狀態；仍須以遊戲內連續場景測試確認傳統記憶體餘量。
- 兩個 OVL 仍為 byte-identical；本輪沒有複製產物到正式遊戲目錄，也沒有封裝發布。

### 3.4 遊戲內驗收與後續階段事項

- 尚未用實際中文畫面與 Python decoder 逐句比對，因此「實際看見的中文頁面」完成門檻仍未通過。特別要測 NPC 多說話者、長中文翻頁、Ask-About 道別、一般選單取消、旅店任務與交易相鄰出現、場景說明反覆重畫。
- 戰鬥、法術、謎題及已定位交易來源已全部排除，`unresolved` 為空；後續若新增或改動呼叫 key，來源掃描測試會要求同步更新政策。
- v1.02 仍受第 2 階段記錄的既有 build path／命令長度問題阻擋，未驗證。
- 尚未做遊戲內存檔後讀回 A/B/C、場景記憶體壓力、寫入延遲與 MLG 長時間容量測試。

---

## 第 4 階段：選項按鈕與閱讀器

- **狀態**：工程實作完成，待遊戲內畫面與操作驗收。
- **日期**：2026-09-06。

### 4.1 選項資源

- `MENUPAGE.json` 對 `REQ_OPT0.DAT`、`REQ_OPT1.DAT` 注入 action `0x84` 的「訊息紀錄」按鈕。兩頁都位於可見按鈕序列的儲存／讀取之後、偏好設定之前；偏好設定、章節目錄、退出按鈕下移 16px，取消按鈕維持原位。
- `menupage_translate.py` 新增帶 `expected_rect` 驗證的 `rect_overrides`，scaffold 會保留設定。來源矩形漂移時停止建置，不會靜默改錯按鈕。
- 實際重建結果：`REQ_OPT0.DAT`、`REQ_OPT1.DAT` 均由 7 entries 增至 8 entries；新 action 分別位於 `(118,103,78,15)` 與 `(118,108,78,15)`。
- 重新生成 `localization/generated/ZHSTAT.DAT`：997 glyphs、21944 bytes；新增的「訊」已通過所有小字 UI 來源覆蓋測試。

### 4.2 唯讀閱讀器

- 新增 `SRC/SCREENS/MSGVIEW.C/.H`，由 `MAINMENU.C` 的 action `0x84` 開啟。overlay help 模式忽略此 action；返回後沿用 Options 的完整重繪路徑。
- 清單預設選取最新可顯示事件，略過 conversation begin/end；上下鍵瀏覽新舊事件，Enter 進內容，Esc 先回清單、再關閉閱讀器。
- 內容頁顯示現實時間、Who、Where 與 What；正文使用既有 `textwrap_draw_aligned()` 分頁。空時間線與讀取錯誤各有明確畫面。
- 閱讀器只呼叫 `msglog_read_event()` 與 offset 導航 API，不執行 DDX。整段生命週期包在 `msglog_enter_viewer()`／`leave_viewer()`，因此畫面重繪不會形成新紀錄。

### 4.3 驗證

- MenuPage、訊息格式、來源政策、中文字型相關測試共 **65 tests，OK**；新增矩形覆寫成功與 source-drift 拒絕測試。
- 全專案 discovery 為 **164 tests，errors=1，skipped=1**；唯一錯誤仍是既有 `test_overhead_map_controls` 在目前 Python 環境無法 import `pytest`，與訊息紀錄變更無關。
- v1.00 Borland 完整建置通過。`KRONDOR.EXE` 491152 bytes，SHA-256 `4b8218729452e407ca7010fc0cb0ca9d5d7f70fe4004affcaefb019a38edcadf`；`VMCODE.OVL` 與 `SX.OVL` 維持 byte-identical。
- linker map：`MSGVIEW_TEXT` stub=`0x25`、overlay=`0x4BF`；`_DATA=0x3F20`、`_BSS=0x2AE8`、`_STACK=0x80`。建置器報告剩餘 conventional memory 384 KB。
- 建置 log：`~/krondor-build-msglog/msgview-phase4-build.log`。
- 尚未以實際 DOSBox-X 畫面驗證滑鼠、Esc、中文排版、長文翻頁及反覆開關 30 次；目前環境沒有可互動 debugger 工具，因此不能把 Phase 4 標為實機驗收完成。

## 第 2 階段補充證據（第 3 階段開始前的基準）

以下保留第 2 階段完成時的產物與待辦，供比較第 3 階段新增量。

- `KRONDOR.EXE`：486976 bytes，SHA-256 `9e168c02a79cc73ab7864179f4d1d03e451d67d44b0310bc677b12bc9dc9d360`。工具顯示與原版 453904 bytes 不同，屬目前繁中及新增功能的預期 divergent build。
- `VMCODE.OVL`：44582 bytes，SHA-256 `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0`，BYTE-IDENTICAL。
- `SX.OVL`：40742 bytes，SHA-256 `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb`，BYTE-IDENTICAL。
- MAP：`MSGSAVE_TEXT` stub 0x48（72 bytes）、overlay 0xC33（3123 bytes）；總 `_DATA` 0x3E60、`_BSS` 0x2A44、`_STACK` 0x80。
- `python -m unittest tests.unit.test_message_log`：44 tests，OK。兩個 Python DOS drivers 可通過 `py_compile`。

v1.02 尚未完成：一般 `bak build --version 102` 因工具把目前 divergent v1.00 判為 tree unchanged 而只重驗 v1.00；直接執行 `link102` 時缺 OUT102 物件，先跑 `kvmobjs102` 又在既有 `AUDIO.C` 編譯命令遇到 Borland `Fatal: Command arguments too long`。這不是 MSGSAVE 的編譯錯誤，但 v1.02 仍視為未驗證，後續需用專案已驗證的 v1.02 clean build 路徑處理。

### 2.4 尚缺項目與下一起點

- 建立受控 I/O wrapper，逐一注入新 GAM write/close、MLG write/close、marker write/close、每個 rename 與清理中斷。現有測試完整覆蓋 rename 之間的程序中止，但沒有覆蓋每個系統呼叫直接回錯。
- 增加損壞／截斷 `MLGTXN.DAT`、恢復連跑兩次、舊檔原本只有 GAM、工作檔建立／candidate activation 空間不足等測試。損壞 marker 目前會停止該目錄的新保存並保留證據，不會自動猜測或刪檔。
- 在隔離遊戲資料目錄用實際新 EXE 完成手動、書籤、F5/F9、自存與 A/B/C 實機測試；確認提示只在 pair commit 成功後出現。尚未把此 EXE 複製到玩家遊戲目錄。
- 量測遊戲場景內配置 2048-byte scratch 的成功率和保存延遲。核心會優先經 `alloc_far_umb` 配置，操作完成立即解除並釋放，不借用 `g_pMainScratchBuf`。
- 修通 v1.02 建置並記錄結果。
- 第 3 階段已在上述未驗項仍公開列出的前提下開始；第 2 階段仍維持「進行中」，不因後續功能接入而標為完成。
