# Keyboard Controls Reference 鍵盤控制清單

Extracted directly from `upstream/betrayal-at-krondor/bak/SRC/` — every `key_is_down()` check and menu hotkey in the game, organized by the screen it works on. Research only, no source files were modified to produce this. Also published as a formatted bilingual [Artifact](https://claude.ai/code/artifact/85cfa618-a8a2-4b13-a5b2-62c482d6bc56).

直接從原始碼萃取，遊戲手冊沒有記載完整的鍵盤操作，所以整理這份清單，純研究記錄，沒有修改任何程式碼。也發布成一份排版過的雙語 [Artifact](https://claude.ai/code/artifact/85cfa618-a8a2-4b13-a5b2-62c482d6bc56) 給使用者參考／分享。

## How input actually works here 輸入機制備忘

- Movement and most menu keys are read as raw PC scancodes, not letters — `SRC/UI/MENUPAGE.C`'s generic widget engine treats a keypress and a mouse click on the same button identically, which is why the same numeric "action ID" shows up for both throughout the code.
  移動跟大部分選單按鍵讀的是原始 PC 掃描碼，不是字母——通用元件引擎把「按鍵」跟「滑鼠點擊」當成同一種動作處理，所以原始碼裡很多數值其實就是掃描碼。
- **Shift** (either side) is a universal modifier on party portraits and item slots: the plain click/key does the primary action (switch character, buy/equip), holding Shift instead opens that character's sheet or that item's inspect panel.
  Shift（左右都算）在隊伍頭像／物品格上是通用修飾鍵：單純點擊是主要動作（切換角色、購買/裝備），按住 Shift 則改成打開角色面板或物品檢視面板。
- **Confirm/cancel** dialogs also accept Numpad 5 or Numpad 0 (confirm) and Numpad + (cancel) alongside the left/right mouse buttons.
  確認/取消對話框除了滑鼠左右鍵，也接受數字鍵盤 5 或 0（確認）、數字鍵盤 +（取消）。
- On a 101-key keyboard, the dedicated arrow/Home/End/PgUp/PgDn cluster is remapped in the keyboard driver back onto the classic numpad codes — so anywhere below that says "Numpad", the separate arrow-key cluster works identically.
  101 鍵鍵盤上獨立的方向鍵/Home/End/PgUp/PgDn 叢集，會被鍵盤驅動層轉換回經典數字鍵盤碼——下面標「Numpad」的按鍵，獨立方向鍵叢集一樣能用。
- Ctrl+Alt+Del and Ctrl+Break are caught by the driver so the game can restore the video mode before rebooting, rather than crashing out.
  Ctrl+Alt+Del、Ctrl+Break 會被驅動層攔截，讓遊戲能先復原顯示模式再重開機，不會直接當掉。

## Core Movement 核心移動

| Key 按鍵 | Action 動作 |
|---|---|
| ↑ | Step forward 前進一步 |
| ↓ | Step backward 後退一步 |
| ← | Turn left 左轉 |
| → | Turn right 右轉 |
| R | Follow the road forward, one tile per press 沿著道路走（偵測到可通行道路時，每按一次前進一格） |
| Enter | Confirm / activate 確認／啟用 |
| Esc | Back / cancel 返回／取消 |
| Tab | Next menu widget 切換到下一個選單項目 |

## World-Map Exploration 世界地圖移動

`WORLDLP.C — worldloop_run`. Walking the 3D overland/dungeon view; every action here is refused with a dialogue line instead of firing while a modal is open.
走 3D 地圖/地城視角時用。有彈窗開著的時候，這些動作都會被拒絕、改播一段對話台詞。

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| ↑ | Move the party forward one step 隊伍前進一步 | WORLDLP.C:259 |
| ↓ | Move the party backward one step 隊伍後退一步 | WORLDLP.C:270 |
| ← | Turn the party left 隊伍左轉 | WORLDLP.C:281 |
| → | Turn the party right 隊伍右轉 | WORLDLP.C:288 |
| R | Auto-step forward along a detected road, one tile per press 沿著道路走 | WORLDLP.C:295 |
| C | Cast a spell 施放法術 | WORLDLP.C:306 |
| M | Open the local zone map 開啟區域地圖 | WORLDLP.C:316 |
| F | Open the full world map 開啟世界地圖 | WORLDLP.C:324 |
| E | Open the encampment screen 開啟紮營畫面 | WORLDLP.C:328 |
| B | Save a bookmark 儲存書籤 | WORLDLP.C:336 |
| O | Open the Options / main menu 開啟選項/主選單 | WORLDLP.C:343 |
| 1 / 2 / 3 | Select a party member — opens inventory, or the character sheet if held with Shift 選取隊伍成員（開物品欄；按住 Shift 改開角色面板） | WORLDLP.C:355 |
| \` | Open Cheat Central *(hidden)* — only if a `knockknock` token is set in the config file, and only with an exact Right-Shift+Alt hold combo 開啟隱藏的 Cheat Central（需設定檔裡有 knockknock token，且要按住右 Shift+Alt 的精確組合） | WORLDLP.C:379 |

## Full World-Map Screen 全螢幕世界地圖

`MAP.C — fmap_screen_run`, opened via **F** above. Same ↑ ↓ ← → and R as world-map movement, plus camera altitude control.
跟世界地圖一樣的 ↑↓←→ 跟 R，另外多了鏡頭高度控制。

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| Numpad 9 / PgUp | Raise camera altitude one step 鏡頭升高一格 | MAP.C:331 |
| Numpad 3 / PgDn | Lower camera altitude one step 鏡頭降低一格 | MAP.C:322 |
| Numpad 7 / Home | Raise altitude by a large step (×5, clamped to max) 鏡頭大幅升高（×5，有上限） | MAP.C:352 |
| Numpad 1 / End | Lower altitude by a large step (×5, clamped to min) 鏡頭大幅降低（×5，有下限） | MAP.C:340 |
| N | Toggle non-rotating map mode *(CD build only)* 切換「地圖不旋轉」模式（僅 CD 版） | MAP.C:377 |
| 2 / 3 / 4 | Select a party member, same Shift behavior as world map 選取隊伍成員，Shift 行為同世界地圖 | MAP.C:405 |
| Esc | Exit the map screen 離開地圖畫面 | MAP.C:420 |

## Combat — Action Menu 戰鬥行動選單

`COMBAT.C — combat_arena_show_message_by_id`. Each combatant's turn menu; numbers 1–8 pick the highlighted command slots directly.
每個角色的回合選單。數字 1–8 直接選取當時顯示的指令格。

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| 1–8 | Select combat-menu item 0–7 選取戰鬥選單第 0–7 項 | COMBAT.C:1948 |
| M | Toggle the "more commands" menu page 切換「更多指令」選單頁 | COMBAT.C:2004 |
| R | Enter a defense stance 進入防禦姿態 | COMBAT.C:2011 |
| S | Open the shoot / missile-weapon menu 開啟射擊/遠程武器選單 | COMBAT.C:2018 |
| C | Open the spellcasting menu 開啟施法選單 | COMBAT.C:2032 |
| A | Run the turn / advance the arena loop (terrain permitting) 執行/推進本回合（視地形而定） | COMBAT.C:2069 |
| F | Ends the actor's turn, with a trap check *(exact intent unclear)* 結束該角色回合，附帶陷阱檢查（確切用途不完全明確） | COMBAT.C:2080 |
| D | Clears an actor flag *(purpose unclear)* 清除某個角色旗標（用途不明確） | COMBAT.C:2054 |
| V | Sets a parameter flag *(purpose unclear)* 設定某個參數旗標（用途不明確） | COMBAT.C:2062 |
| U | Suspend combat to open the character sheet or inventory 暫停戰鬥，開角色面板或物品欄 | COMBAT.C:2111 |
| G | Toggle a debug combat-grid overlay *(debug)* 切換除錯用戰鬥格線疊圖 | COMBAT.C:2148 |
| Ctrl+Q | Instantly kill every remaining enemy, ending the fight *(debug)* 秒殺場上所有敵人、直接結束戰鬥 | COMBAT.C:2128 |
| Esc | Cancel the current spell / target selection 取消目前法術/目標選取 | COMBAT.C:2140 |

## Spellcasting Menu 施法選單

`CSPELL.C — cspell_cast_menu_loop`

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| 1–6 | Select a spell school 選取法術學派 | CSPELL.C:2236 |
| M | Close the spell menu 關閉施法選單 | CSPELL.C:2285 |
| Esc | Cancel spell selection 取消選取 | CSPELL.C:2278 |

## Character Sheet 角色屬性面板

`CHARSCRN.C — charscreen_info_loop`

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| Space / N | Cycle to the next party member 切換到下一位隊伍成員 | CHARSCRN.C:360 |
| S | Show the spell book 顯示法術書 | CHARSCRN.C:380 |
| Esc | Exit the character sheet 離開角色面板 | CHARSCRN.C:387 |

## Save / Load Game 存讀檔

`MAINMENU.C`

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| ↑ | Scroll up the file list — hold Ctrl to scroll the slot list instead 捲動檔案清單（按住 Ctrl 改捲動存檔格清單） | MAINMENU.C:504 |
| ↓ | Scroll down, same Ctrl modifier 同上，方向相反 | MAINMENU.C:511 |
| Enter | Confirm the selected save/load entry 確認選取的存/讀檔項目 | MAINMENU.C:524 |
| Esc | Cancel and close the dialog 取消並關閉視窗 | MAINMENU.C:540 |

## Options / Main Menu Overlay 選項/主選單

`MAINMENU.C`, opened via **O** from the world map.

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| N | New Game 開新遊戲 | MAINMENU.C:200 |
| R | Restore Game 讀取存檔 | MAINMENU.C:210 |
| S | Save Game 儲存遊戲 | MAINMENU.C:222 |
| O | Preferences / Options submenu 偏好設定子選單 | MAINMENU.C:235 |
| C | Continue / confirm (context-dependent) 依情境繼續/確認 | MAINMENU.C:247 |
| D | Quit to DOS 離開到 DOS | MAINMENU.C:261 |
| E | Exit menu, resume the game 關閉選單、回到遊戲 | MAINMENU.C:275 |
| V | Show the About / version credits 顯示版本/製作名單 | MAINMENU.C:289 |
| Esc | Close (party-creation context only) 關閉（僅限開角色重新進入的情境） | MAINMENU.C:283 |

Inside Preferences: O saves & closes, Esc/C cancels, D resets to defaults. 偏好設定子選單內：O 儲存並關閉，Esc/C 取消，D 重設為預設值。（MAINMENU.C:1216）

## Item Quantity Spinner 物品數量調整器

`INVINSP.C` — buying, selling, splitting stacks 買賣/拆分堆疊時用

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| ↑ / → / . / Numpad + | Increase by 1 — hold Shift to jump by 5 數量 +1（按住 Shift 改 +5） | INVINSP.C:127 |
| ↓ / ← / , / Numpad − | Decrease by 1 — hold Shift to drop by 5 數量 −1（按住 Shift 改 −5） | INVINSP.C:111 |
| S | Select all (max quantity) 選取全部（最大值） | INVINSP.C:165 |
| Space | Confirm the chosen quantity 確認數量 | INVINSP.C:169 |
| Esc | Cancel 取消 | INVINSP.C:175 |

## Dialogue & Cutscenes 對話/過場動畫

`DIALOG.C — dialog_poll_arrow_or_button`

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| Any key / mouse / joystick | Advance / dismiss the current line 推進/關閉目前這段文字 | DIALOG.C:174 |
| Num Lock / Scroll Lock | Pause — waits for any further key 暫停，等待下一次按鍵 | DIALOG.C:174 |
| ↑ ↓ ← → | Deliberately ignored here, so walking doesn't skip dialogue 刻意被忽略，避免移動鍵不小心跳過對話 | DIALOG.C:182 |

## Credits & Book/Scroll Viewer 製作名單/書籍檢視器

`CREDITS.C` · `BOOKVIEW.C`

| Key 按鍵 | Action 動作 | Source |
|---|---|---|
| Any key / mouse / joystick | Turn the page in a book or scroll 翻頁 | BOOKVIEW.C:182 |
| N (held) | Forces an Easter-egg name swap on some credit rows *(exact swap unclear)* 觸發某些製作名單列的彩蛋換名（確切內容從程式碼看不出來） | CREDITS.C:80 |

## Cheat Central — hidden, gated 隱藏除錯選單

`TOWNSCN.C` — a developer debug menu shipped in the original 1993 game. Reached only through the \` combo on the world map above, and only if a `knockknock` token is set in the config file. Documented here as-is, straight from the shipped code — not something this project added.

原版遊戲本來就內建的開發者除錯選單，只能透過世界地圖的 ` 組合鍵進入，且需要設定檔裡有 knockknock token。這裡只是照原始碼如實記錄，不是這個中文化專案新增的功能。

| Menu item | Action 動作 | Source |
|---|---|---|
| Add gold | Grants 5000 gold 增加 5000 金幣 | TOWNSCN.C:710 |
| Spawn inventory | Opens an inventory screen for a chapter-9 actor 開啟第九章某個角色的物品欄 | TOWNSCN.C:713 |
| Dialogue test | Plays dialogue record 0x249f1b *(effect unclear)* 播放對話紀錄 0x249f1b（效果不明確） | TOWNSCN.C:722 |
| End world loop | Force-exits the current world loop 強制結束目前的世界迴圈 | TOWNSCN.C:726 |
| Heal party | Heals the entire party to 100% 全隊回滿血 | TOWNSCN.C:730 |
| Grant spells | Gives every party member all spells 給所有隊員全部法術 | TOWNSCN.C:733 |
| Visit all towns | Marks all 15 towns as visited 把全部 15 座城鎮標記為已造訪 | TOWNSCN.C:740 |

## Screens With No Dedicated Hotkeys 沒有專屬快捷鍵的畫面

Encampment, the lock-cipher puzzle, picklocking, the shop screen, and the base inventory screen all run entirely on the generic arrow/Enter/Esc/Shift-click navigation described above — no screen-specific keys were found in the source for any of them.

紮營畫面、密碼盤解謎、開鎖小遊戲、商店畫面、基本物品欄畫面，全部只靠上面提到的通用方向鍵/Enter/Esc/Shift+點擊操作，原始碼裡找不到任何畫面專屬的快捷鍵。

---

Compiled from `upstream/betrayal-at-krondor/bak/SRC/` — every row cites the file and line it came from.
整理自遊戲原始碼，每一列都附上檔案與行號出處。
