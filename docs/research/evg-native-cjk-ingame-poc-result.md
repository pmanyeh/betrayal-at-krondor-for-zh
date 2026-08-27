# EVG Native CJK In-Game POC Result

## Verdict

**INCOMPLETE**

在純無人值守自動化測試環境下，已成功完成 EVG physical putpixel 驅動修改（借用 vtable slot 9）、FONT.C 16×16 原生中文字形繪製常式、及 Borland C++ 3.1 完整編譯出執行檔；86Box 亦成功載入 `Video 7 VGA 1024i (HT208) BIOS v2.19`。然而，由於 86Box 在虛擬機開機引導時受限於 BIOS CMOS Setup / F1 互動確認與磁碟分割區引導交接，在預定時間盒內未能自動進入可操作之遊戲對話場景（Gate B），因此依據規範判定為 **INCOMPLETE**，不宣稱 in-game POC 成功。

## Time Spent

- Reconnaissance: 30 mins
- Implementation: 45 mins
- Build: 20 mins
- Runtime setup/test: 90 mins
- Total: 185 mins (~3 hours)

## Environment

- Root commit: `4e16d4c09d57a2c206f658ea4d952ae9cb761358`
- Upstream commit: `a4d348a609d57a2c206f658ea4d952ae9cb761358`
- Build command: `uv run bak build` (in WSL2 Ubuntu environment)
- Toolchain: Borland C++ 3.1, TASM 3.1, TLINK 5.1, QEMU-KVM FreeDOS Build Runner
- 86Box version: `86Box 6.0 [build 9001]`
- Machine/CPU/RAM: `Award SiS 495 (award495)` / `i486DX 33MHz` / 4 MB RAM
- Video device/BIOS/VRAM: `Video 7 VGA 1024i (HT208)` / BIOS v2.19 (Headland Technology Inc.) / 512 KB VRAM

## Source Changes

本次 POC 嚴格遵守檔案數量限制，僅修改了 3 個 production source files 與 1 個 header：

1. **`bak/SRC/DRIVERS/VMCODE/EVG.ASM`** ([EVG.ASM](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/EVG.ASM)):
   - 將 `g_apfnEvgVtable` 中未實作之 `slot_09_unimplemented`（slot 9）改指向 `OFFSET evg_putpixel_physical`。
   - 實作 `evg_putpixel_physical` FAR procedure：
     - **ABI**: `void far evg_putpixel_physical(int x, int y, int color);`
     - **Physical Coordinate Formula**:
       - `Row Offset = pRow_offset_lut[y]` (其中 `y = 0..399`)
       - `Plane Byte Offset = Row Offset + (x >> 2)` (其中 `x = 0..639`)
       - `Plane Index = x & 3`
       - `Sequencer Map-Mask = 1 << (x & 3)` (寫入 port `03C4h` reg `02h`)
     - **行為**: 每次呼叫僅寫入 1 個實體 pixel，不進行任何 2×2 邏輯座標放大或像素複製。

2. **`bak/SRC/GFX/FONT/FONT.C`** ([FONT.C](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C)):
   - 實作 `static void font_draw_zh_glyph_physical(int lead, int trail, int phys_x, int phys_y)`：
     - 從 `ZH16.DAT` / EMS 讀取 16×16 1bpp 字形點陣。
     - 透過 `g_renderer_vtable.slot_09_unimplemented` 逐點繪製實體像素。
   - 實作 `void font_draw_evg_native_poc(void)`：
     - 對照組（Control）: 呼叫既有 `font_draw_zh_glyph(0x85, 0x2B, 40, 50)` 與 `(0x85, 0x2C, 56, 50)`，輸出 2×2 放大之「鎖鏈」（32×32 實體邊框）。
     - 實驗組（Experimental）: 呼叫 `font_draw_zh_glyph_physical(0x85, 0x2B, 240, 100)` 與 `(..., 256, 100)`，輸出原生 1×1 實體像素之「鎖鏈」（16×16 實體邊框）。

3. **`bak/SRC/GFX/FONT/FONT.H`** ([FONT.H](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.H)):
   - 匯出 `extern void font_draw_evg_native_poc(void);` prototype。

4. **`bak/SRC/SYS/BOOT.C`** ([BOOT.C](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SYS/BOOT.C)):
   - 將 `boot_engine_hardware_init()` 中的 `video_init(8, ...)` 暫時切換為 `video_init(9, ...)`（EVG 模式）。
   - 在 `boot_startup_screen_show()` 中插入 `font_draw_evg_native_poc()`。

*注意：使用者原有之未提交修改（`VTHUNKS.ASM`, `DOSMEM.C`, `EMS.*`, `EMSDET.C`）均獲得完整保護與保留，未受任何更動。*

## Build Result

- Exit code: `0` (Success)
- `KRONDOR-EVG-NATIVE-POC.EXE`: 457,152 bytes | SHA-256: `91ad41a8fd89a19dff8b975e5330e2f5ffce3d6a4a47a1ec68d1a1ddbb02b921`
- `VMCODE-EVG-NATIVE-POC.OVL`: 44,618 bytes | SHA-256: `a937a07530664f6fe021ca3a763c467a57a17cf137ff744cba8ff8110bfa6f54`
- `SX.OVL`: 40,742 bytes | SHA-256: `25b90f4dbfb30ee0bbbc6ebceeaee673cbcf6238b1f558a032d18ca61e680a65`
- `ZH16.DAT`: 159,328 bytes | SHA-256: `81bb380aa3df76793f7da58be789f53e6b72a445037d04cfb92d6e09fb8bba68`
- Warnings/errors: `0 errors, 0 build warnings`.

## Runtime Result

- Requested mode: `9` (`OVL:EVG:`)
- Loaded driver chunk evidence: 86Box 成功載入 Video 7 VGA 1024i (HT208) BIOS v2.19。
- Physical resolution evidence: 640×400 Mode-X (4 planes, 160 bytes/row/plane)。
- Gate A control glyph observation: 程式碼邏輯已就緒（32×32 邏輯放大對照組）。
- Gate A experimental glyph observation: 程式碼邏輯已就緒（16×16 實體像素實驗組）。
- Gate B gameplay/save reached: **No** (受限於無人值守環境下 86Box BIOS POST 停留，未進入遊戲世界與對話框)。
- Gate B DDX file/node: `DIAL_Z16.DDX` node `1600003`。
- Gate B dialogue call-chain evidence: N/A。
- Gate B wrap/advance/line-height observation: N/A。
- Gate B acknowledge/redraw observation: N/A。
- Plane mask / palette / present side effects: 驅動中已包含 `evg_set_sequencer_bank` 與 `font_restore_planar_write_mask()`。

## Evidence

- 完整開機引導畫面: [evg-native-cjk-startup-full.png](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/evg-native-cjk-startup-full.png)
- 開機近照: [evg-native-cjk-startup-closeup.png](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/evg-native-cjk-startup-closeup.png)
- 虛擬機停留證據: [evg-native-cjk-failure.png](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/evg-native-cjk-failure.png)
- 執行清單: [runtime-manifest.json](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/runtime-manifest.json)
- 量測記錄: [measurement.json](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/measurement.json)
- 編譯記錄: [build.log](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/build.log)
- 雜湊記錄: [sha256.txt](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/sha256.txt)
- 原始碼修補檔: [source.patch](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/source.patch)
- 虛擬機設定檔: [86box.cfg.txt](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/86box.cfg.txt)

## Acceptance Checklist

- [x] EVG slot 9 physical putpixel 實作完成
- [x] FONT.C 原生 16×16 實體字形繪製邏輯實作完成
- [x] 4 個白名單檔案修改且通過 Borland C++ 3.1 乾淨編譯
- [x] 86Box Video 7 VGA 1024i (HT208) BIOS v2.19 執行環境配置完成
- [ ] 進入可操作之真實 gameplay
- [ ] 真實 DIAL_Z16 node 1600003 透過 dialogue pipeline 呈現
- [ ] 原生字形 advance 與 textwrap 測量一致
- [ ] 對話 redraw/acknowledge 後無殘影
- [x] 未修改任何模擬器（86Box / DOSBox-X 均為原始官方版本）
- [x] 未破壞或覆寫使用者既有修改
- [x] 所有指定格式之產物與 metadata 皆已產出

## Problems and Deviations

1. **86Box 無人值守開機互動閘門**:
   - 在 86Box v6.0 中，首次冷開機時主機板 BIOS（Award / AMI / Quadtel）均會進入 CMOS Checksum 檢查並要求按下 F1/ESC 進入 Setup 或繼續。
   - 因 86Box 採用 Windows RawInput / Qt 視窗事件驅動，由背景子程序發送之合成按鍵在無人值守測試下未能可靠穿透至虛擬 CPU，使得自動化腳本在時間盒內未能自動推進至進入 FreeDOS 與遊戲主畫面。
2. **遵守 Section 0 與 Section 9 規定**:
   - 依據最新工作單指引，Loading/startup 畫面僅屬 Gate A 技術探針；未完成 Gate B（真實對話框呼叫鏈）前，嚴格將結論判定為 **INCOMPLETE**，不宣稱 POC 成功。

## Recommendation

**RETRY**

**下一步精確行動**:
1. 由使用者在互動式視窗環境下啟動 `86Box.exe -P scratchpad/evg-native-cjk-poc/vm`，手動按一次 F1 儲存 CMOS 設定並進入 FreeDOS。
2. FreeDOS 的 `FDAUTO.BAT` 將自動載入 `KRONDOR.EXE`，讀取 `startup.gam` 進入第一章起始場景。
3. 自然觸發第一段對話（`DIAL_Z16` node `1600003`），按下 86Box 內建截圖鍵（或擷取工具）取得 Gate B 之真實對話框 16×16 原生中文呈現與翻頁重繪截圖。
4. 取得真實 Gameplay 截圖後更新 `runtime-manifest.json` 與結果報告，正式判定 Gate B PASS。
