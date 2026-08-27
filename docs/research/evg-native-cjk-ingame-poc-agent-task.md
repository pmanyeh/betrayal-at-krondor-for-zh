# EVG 遊戲內原生 16×16 中文：最小 POC Agent 工作單

## 0. 給執行 Agent 的指令

你要**實際完成、建置、執行並留下證據**，不是只提出設計建議。

> **2026-08-25 方向更正（執行中的 Agent 必讀）**
>
> Loading/startup screen 只能算 Gate A 技術探針，**不能取得最終 PASS**。
> 最終 PASS 必須進入可操作的遊戲場景，讓既有 dialogue pipeline 顯示一筆真實
> DDX 中文對話，並證明折行、背景清除與 present 後仍正確。若目前只做到 loading
> screen，請保留成果但繼續 Gate B；不要把 Gate A 寫成 in-game 成功。

本階段要回答的問題是：

> 原版 EVG 的 640×400 framebuffer 中，能否讓遊戲畫面繼續使用原本的
> 320×200 → 640×400 之 2×2 放大邏輯，但讓一個固定中文測試字串直接以
> 16×16 physical pixels 顯示，並能通過真實遊戲對話框的文字處理流程？

請嚴格遵守本文件的時間盒、檔名、報告格式與停止條件。成功標準是畫面證據，
不是「可以編譯」或「理論上可行」。

## 1. 時間盒與停止條件

- 原始碼追蹤與設計確認：最多 60 分鐘。
- 實驗修改與建置：最多 120 分鐘。
- 86Box 設定與執行：已有環境最多 90 分鐘；從零設定最多 4 小時。
- 總時間上限：半天。

遇到下列情況立即停止，將結果記為 `BLOCKED`，不要擴張工作：

- 無法取得或啟動 Video 7 VGA 1024i 相容的 86Box 環境。
- `EVG` 初始化失敗，而且 60 分鐘內無法指出明確原因。
- 必須修改 DOSBox-X 才能繼續。
- 必須重寫完整 renderer、文字折行、對話系統或資源格式。
- 需要改動三個以上的 production source modules 才能顯示固定測試字串。
- Borland/TASM 建置錯誤在 60 分鐘內仍無法縮小到單一原因。

## 2. 非目標

本 POC **不做**以下事項：

- 不做可發布版本。
- 不把所有介面改成 640×400 座標。
- 不修改 DOSBox-X。
- 不導入 FreeType、Unicode、TTF 或新字形格式。
- 不改寫 DDX 資料格式；允許為 EVG native-text mode 做最小的寬度／折行量測分支。
- 不追求 VGA、EGA 等其他 adapter 相容性。
- 不最佳化組合語言速度。
- 不更換 `ZH16.DAT`。
- 不把實驗二進位覆蓋進正式 `dist/test_v100_zh/`。

## 3. 已知事實與必讀位置

執行前先閱讀下列檔案的相關區段，並在結果報告記錄實際看到的行號。

### 3.1 EVG framebuffer

- `upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/EVG.ASM`
  - 檔頭的 640×400×256、四 plane、160 bytes/plane-row 說明。
  - `g_apfnEvgVtable`：50 個 far-pointer slots。
  - `evg_getpixel`。
  - `evg_putpixel`：輸入 logical `(x,y)`，輸出 physical 2×2 pixels。

已知 layout：

```text
physical resolution:       640 x 400 x 256 colours
plane count:               4
bytes per row per plane:   160
physical pixel plane:      x & 3
byte offset in plane:      row_lut[y] + (x >> 2)
Sequencer Map Mask:        1 << (x & 3), written through port 03C4h reg 02h
```

目前 `evg_putpixel` 會先把 logical `x`、`y` 乘二，再寫出 2×2。因此直接讓
`font_draw_zh_glyph()` 呼叫現有 `pfn_putpixel`，只會得到放大後的 32×32 字，
不是本 POC 要驗證的結果。

### 3.2 Renderer vtable

- `upstream/betrayal-at-krondor/bak/INCLUDE/structs.h`
  - `PutpixelFn`。
  - `struct RendererVtable`。
- `upstream/betrayal-at-krondor/bak/SRC/GEN/RNDVTBL.H`
- `upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VIDINIT.C`

`video_init()` 會把 driver 的 50-slot template 複製到 resident
`g_renderer_vtable`，並把每個 slot 的 segment half 改成已載入 EVG chunk 的 segment。

本 POC 建議暫借 **slot 9**：

```text
g_renderer_vtable.slot_09_unimplemented
EVG table slot 9: currently evg_unimplemented_slot
```

在修改前必須用 `rg` 再確認 slot 9 沒有 production caller。若發現 caller，禁止硬用；
在報告說明後改找另一個確定未使用、且不會被 driver-init callback copy 覆寫的 slot。
不要使用 slot 23；它在 struct 中具有 `pfn_blit_rect_buffer` 語意。不要使用 slots 40–49；
EVG 初始化期間那一段會被 host callback table 覆寫。

### 3.3 中文字形

- `upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C`
  - `font_init_chinese()`。
  - `font_draw_zh_glyph()`。
  - `font_draw_text_far()`。
- `upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.H`
- `localization/generated/ZH16.DAT`
- `localization/generated/zh_mapping.json`

`ZH16.DAT` binary format：

```text
offset  size                         meaning
0       16 bytes                     header
16      glyph_count * 32 bytes       CJK, 16 rows x 2 bytes, 1bpp, MSB first
...     256 * 16 bytes               ETen ASCII, 8 rows-bits x 16 rows
```

Header little-endian layout：

```text
<4sHBBHB5s
magic='ZHFN', version=u16, width=u8, height=u8,
glyph_count=u16, base_lead=u8, padding=5 bytes
```

本 POC 固定測試字串為「鎖鏈」。現有 mapping 中已知：

```text
鎖: glyph id 811, encoded bytes 85 2B, bitmap file offset 25968
鏈: glyph id 812, encoded bytes 85 2C, bitmap file offset 26000
```

執行 Agent 必須用 Python 從 `zh_mapping.json` 與現有 encoding 公式重新驗證，
不能只相信上述常數。

## 4. 工作目錄與現有修改保護

主 workspace：

```text
D:\git\betrayal-at-krondor-for-zh
```

上游原始碼是 nested Git repository：

```text
D:\git\betrayal-at-krondor-for-zh\upstream\betrayal-at-krondor
```

撰寫本工作單時，nested repository 已有使用者的未提交修改：

```text
bak/SRC/GFX/DRIVER/VTHUNKS.ASM
bak/SRC/SYS/DOSMEM.C
bak/SRC/SYS/EMS.C
bak/SRC/SYS/EMS.H
bak/SRC/SYS/EMSDET.C
```

這些不是本 POC 的工作，禁止還原、覆寫、stash、reset 或納入 POC patch。
開始與結束時都要保存以下命令輸出：

```powershell
git status --short
git -C upstream/betrayal-at-krondor status --short
git -C upstream/betrayal-at-krondor diff --check
```

原始碼編輯使用 patch-based editing。不要用會整檔重寫或改變換行格式的工具。

## 5. 必須使用的工具

### 5.1 原始碼與靜態檢查

```text
Git                  檢查 nested worktree、產生限定路徑的 diff
rg                   搜尋 vtable caller、函式與固定 offset
PowerShell           Windows workspace 操作與產物整理
Python 3.12+         驗證 ZH16/mapping、產出 JSON、檢查 PNG 尺寸
Pillow               僅分析/裁切證據圖；禁止生成假的成功畫面
```

### 5.2 正式 16-bit 建置

沿用專案已存在的 WSL2 build environment：

```text
WSL2 Ubuntu
uv
project CLI: uv run bak build
QEMU i386, KVM + TCG
mtools
Borland C++ 3.1 / 3.0 / 2.0
TASM / TLINK
FreeDOS image
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain
WSL build clone=~/krondor-build
```

不要嘗試用 Visual C++、MinGW、clang 或現代 32/64-bit compiler 取代 Borland build。

### 5.3 Runtime 驗證

必須使用目前官方 86Box stable release 與相符 ROM set：

- 86Box source：<https://github.com/86Box/86Box>
- ROM releases：<https://github.com/86Box/roms/releases>
- ROM 說明：<https://github.com/86Box/docs/blob/master/usage/roms.rst>
- Video 7 implementation：<https://github.com/86Box/86Box/blob/master/src/video/vid_ht216.c>

建議硬體設定：

```text
machine:       generic ISA 386 or 486
RAM:           4-8 MB
video:         Video 7 VGA 1024i (HT208)
video BIOS:    v2.19 first; record exact ROM if another version is used
video RAM:     512 KB
guest OS:      DOS/FreeDOS capable of running the built game
```

DOSBox-X 可以用來做非 EVG 的 sanity check，但**不得**作為 EVG 成功證據，也不得修改。

## 6. 建議的最小實作

允許修改的 production source files，上限三個：

```text
bak/SRC/DRIVERS/VMCODE/EVG.ASM
bak/SRC/GFX/FONT/FONT.C
bak/SRC/SYS/BOOT.C
```

只有在 compiler 需要 prototype 時，才允許另外修改：

```text
bak/SRC/GFX/FONT/FONT.H
```

### 6.1 在 EVG 加入 physical putpixel

在 `EVG.ASM` 加入一個 POC-only far procedure，例如：

```text
evg_putpixel_physical(x_physical, y_physical, colour)
```

ABI 必須與 `PutpixelFn` 相同：

```c
void far fn(int x, int y, int color);
```

行為：

```text
input range: x=0..639, y=0..399
row offset:  pRow_offset_lut[y]
byte offset: row offset + (x >> 2)
plane mask:  1 << (x & 3)
write count: exactly one framebuffer byte in exactly one selected plane
vertical duplicate: none
horizontal duplicate: none
```

最安全作法是以 `evg_getpixel`／`evg_putpixel` 的 bank、DS、ES 與 prologue/epilogue
為模板，只移除 logical coordinate doubling。不要自行猜測 bank switching。

把 EVG vtable slot 9 從 `evg_unimplemented_slot` 改指向新 procedure。優先使用
`OFFSET evg_putpixel_physical`，不要在沒有 map/listing 證據時猜一個硬編碼 offset。

### 6.2 Gate A：在 FONT.C 加入固定字形技術測試

加入 POC-only helper，直接呼叫：

```c
(*(PutpixelFn)g_renderer_vtable.slot_09_unimplemented)(physical_x,
                                                       physical_y,
                                                       color);
```

此 helper：

- 沿用 `font_init_chinese()`、EMS mapping 與 `ZH16.DAT` glyph lookup。
- 逐 row/column 解碼 16×16、1bpp、MSB-first bitmap。
- 接受 physical coordinates。
- 不修改 production `font_draw_zh_glyph()` 的正常行為。
- 僅在 `g_bRequestedVideoMode == 9` 時啟用。
- 對 physical bounds 做明確檢查。

加入固定 POC 函式，例如：

```c
void font_draw_evg_native_poc(void);
```

它要在同一畫面畫出兩組「鎖鏈」：

```text
control group:
  使用現有 font_draw_zh_glyph()
  預期 physical glyph cell = 32x32

experimental group:
  使用 slot 9 physical putpixel helper
  預期 physical glyph cell = 16x16
```

兩組必須使用相同 glyph IDs、相同 palette index，且 physical top edge 對齊。
建議位置：

```text
control:      logical  x=40, y=50 -> physical origin approximately 80,100
experimental: physical x=240, y=100
```

不要在 C source 中依賴 Big5/UTF-8 source literal；使用已重新驗證過的 encoded bytes
`85 2B 85 2C` 或直接傳入 `(lead, trail)` pairs。

### 6.3 Gate A 只在 loading screen 觸發

在 `BOOT.C`：

1. 把 `boot_engine_hardware_init()` 的 startup `video_init(8, ...)` 暫時改成 mode 9。
2. 在 `boot_startup_screen_show()` 設好 palette、destination page、foreground colour後，
   呼叫固定 POC 函式。
3. 呼叫必須位於 present/vsync 之前。

Gate A 只需停留在 loading/startup screen 取得技術證據。
如果遊戲立即切換畫面，允許加入單一按鍵等待或短暫可觀察 gate，但必須標為 POC-only，
不可加入長時間 busy loop。

**Gate A 成功後必須繼續 Gate B；Gate A 單獨完成時，最終 verdict 只能是
`INCOMPLETE` 或 `BLOCKED`，不能是 `PASS`。**

### 6.4 Gate B：真實遊戲對話框

Gate B 必須走既有 production call chain，不能在 gameplay screenshot 上另外疊一段
hard-coded 字串冒充對話：

```text
real DDX record
  -> dialog_render_text_with_tokens()
  -> textwrap_compute_lines() / textwrap_draw_aligned()
  -> font_draw_text_far()
  -> CJK glyph renderer
  -> EVG physical putpixel
```

必讀：

```text
bak/SRC/DIALOG/DIALOG.C
bak/SRC/UI/TEXTWRAP.C
bak/SRC/GFX/FONT/FONT.C
localization/translated/DIAL_Z16.json
```

首選真實測試資料：

```text
DIAL_Z16 node_id: 1600003
translation: ……戈拉斯猛然向前撲去，鎖鏈在他腕間如金屬毒蛇般扭動。
runtime save candidates:
  dist/test_v100_zh/startup.gam
  dist/test_v100_zh/TEMP.GAM
```

這是現有專案曾使用過的必經觸發點。優先從 `startup.gam` 進入並自然觸發；若實際
檔名大小寫或載入方法不同，記錄真實步驟。禁止把離線 `frame7.png` 或 Python mock
當成 Gate B 證據。

Gate B 的 native mode 至少要做到：

1. `font_draw_zh_glyph()` 在 EVG native-text mode 下，把 logical origin `(x,y)`
   轉為 physical origin `(2*x, 2*y)`，glyph bitmap 本身仍只寫 16×16 physical pixels。
2. CJK advance 從 16 logical units 改為 8 logical units，否則字雖縮小但字距仍為 32
   physical pixels。
3. `font_text_pixel_width()` 與 `font_glyph_metrics()` 在相同 mode 下回報一致的 8
   logical-unit CJK width；不得只改 drawing 而讓 wrapping 仍按 16 計算。
4. 高度／line-height 必須在報告明列採用策略。POC 可先保留原本 logical line spacing，
   但必須觀察並記錄；若改成 8 logical units，則 drawing、measurement 與 clipping
   必須一致。
5. 若真實句子含 ASCII，必須明列 ASCII 是維持 2× 還是也走 8×16 physical renderer；
   不得讓 CJK 與 ASCII layout measurement 各用不同假設。
6. 正常 dialogue erase/redraw、換行與一次 acknowledge/pagination 操作後，文字不能
   殘留或被 present 覆蓋。

若要啟用 native mode，使用一個明確 POC-only global flag，且僅在 requested mode 9
與 mixed Chinese dialogue rendering 時開啟。不要讓 VGA mode 呼叫 EVG-only vtable slot。

Gate B 若需要修改 `TEXTWRAP.C` 或 `DIALOG.C`，可將 production source file 上限由三個
提高為五個，但每一個新增檔案都必須在報告解釋為何不能只改 `FONT.C`。這仍是 POC，
不要藉機重構整套文字系統。

## 7. 建置流程

### 7.1 建置前記錄

在主 workspace 建立產物目錄：

```text
scratchpad/evg-native-cjk-poc/
```

先記錄：

```powershell
git rev-parse HEAD
git -C upstream/betrayal-at-krondor rev-parse HEAD
git status --short
git -C upstream/betrayal-at-krondor status --short
```

### 7.2 同步到 WSL build clone

`~/krondor-build` 位於 WSL ext4，不要直接在 `/mnt/d` 執行 build。只同步本 POC
實際修改的檔案。不要用會刪除目的端其他檔案的 mirror/recursive sync。

同步後先確認：

```powershell
wsl -e bash -lc "cd ~/krondor-build && git status --short"
```

### 7.3 Build command

```powershell
wsl -e bash -lc "cd ~/krondor-build && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain && export PATH=\$HOME/.local/bin:\$PATH && uv run bak build"
```

將完整 stdout/stderr 保存成：

```text
scratchpad/evg-native-cjk-poc/build.log
```

預期至少產生：

```text
~/krondor-build/work/KRONDOR.EXE
~/krondor-build/work/VMCODE.OVL
```

如果實際 CLI 放在其他 output path，記錄實際路徑，不要假造。

複製並重新命名為：

```text
scratchpad/evg-native-cjk-poc/KRONDOR-EVG-NATIVE-POC.EXE
scratchpad/evg-native-cjk-poc/VMCODE-EVG-NATIVE-POC.OVL
```

`SX.OVL` 沒有修改；runtime 測試可使用既有相容版本，但在 manifest 記錄其來源與 hash。

### 7.4 Hash 與 binary identity

產出 SHA-256：

```text
scratchpad/evg-native-cjk-poc/sha256.txt
```

至少包含：

```text
KRONDOR-EVG-NATIVE-POC.EXE
VMCODE-EVG-NATIVE-POC.OVL
runtime ZH16.DAT
runtime SX.OVL
```

此 POC 預期 `KRONDOR.EXE` 與 `VMCODE.OVL` 都不再 byte-identical；這本身不是失敗。

## 8. Runtime 測試流程

1. 建立獨立的 guest 測試目錄，不覆蓋正式 distribution。
2. 放入 POC EXE，guest 內檔名仍須為 `KRONDOR.EXE`。
3. 放入 POC `VMCODE.OVL`、相容 `SX.OVL`、現有遊戲資料及正式 `ZH16.DAT`。
4. 啟動 86Box，確認 adapter 是 Video 7 VGA 1024i (HT208)。
5. 執行遊戲並先取得 Gate A loading/startup POC 畫面。
6. 載入 `startup.gam`（或記錄實際使用的等價 save），進入可操作 gameplay。
7. 自然觸發 DIAL_Z16 node `1600003`；不得直接從 BOOT 畫一段相同文字冒充。
8. 在真實 dialogue frame 中取得 native 16×16 中文畫面。
9. 至少完成一次 acknowledgement、換行重繪或下一頁操作，確認 erase/present 正常。
10. 取得未經平滑縮放的 framebuffer screenshots；優先使用 86Box 內建 screenshot。
11. 記錄 screenshot 原始 pixel dimensions。不得把 320×200 mock 當成 runtime 證據。
12. 用 Pillow 做只讀分析，確認 Gate A bounding boxes，並記錄 Gate B 每行字數與行數。

若 86Box 畫面有黑屏、花屏或 driver fallback，仍要截圖並記錄，不要只寫文字敘述。

## 9. 驗收標準

### PASS

必須全部成立：

- 遊戲確實載入 `OVL:EVG:`，不是 VGA fallback。
- 顯示模式實際為 640×400×256。
- 背景／一般 loading graphics 維持 EVG 2×2 外觀。
- control「鎖鏈」每字約 32×32 physical cell。
- experimental「鎖鏈」每字約 16×16 physical cell。
- experimental glyph 沒有隔行、缺 plane、錯色、水平錯位或重影。
- 畫完字形後沒有破壞後續整頁 present、palette 或 plane mask。
- 已進入可操作 gameplay，而不是停在 loading/startup screen。
- 真實 DIAL_Z16 node `1600003` 經過既有 DDX → dialogue → textwrap → font call chain 顯示。
- 真實對話的 native CJK advance、折行結果與 glyph 寬度一致。
- 至少一次 dialogue acknowledge／重繪後沒有文字殘影或被 present 覆蓋。
- POC binaries、hash、runtime screenshot、patch 與報告全部存在。

### FAIL

任一成立即 FAIL：

- EVG 成功運作，但 physical putpixel 無法穩定寫出單一 pixel。
- 16×16 字形出現 plane fan、bank、row LUT 或 page destination 錯誤。
- 寫字後畫面其他區域被破壞。
- 只能靠修改 emulator 才能顯示。
- 需要大幅改寫 engine 才能完成固定字串。

### BLOCKED

只用於外部環境無法進行，例如沒有可用 ROM、86Box 無法建立、工具鏈不可用。
`BLOCKED` 必須列出已執行命令、完整錯誤與下一個最小解除動作。

### INCOMPLETE

Gate A 成功、但尚未完成真實 gameplay dialogue 的狀態必須記為 `INCOMPLETE`，不能 PASS。
執行 Agent 應在剩餘時間內優先完成 Gate B，而不是繼續美化 loading screen。

## 10. 產出檔名與格式

所有 runtime/build artifacts 放在：

```text
scratchpad/evg-native-cjk-poc/
```

| 檔名 | 格式 | 必要性 | 內容 |
|---|---|---:|---|
| `KRONDOR-EVG-NATIVE-POC.EXE` | 16-bit DOS MZ executable | 必須 | POC 遊戲執行檔 |
| `VMCODE-EVG-NATIVE-POC.OVL` | BAK packed driver chunk archive | 必須 | 包含修改後 EVG chunk |
| `build.log` | UTF-8 plain text | 必須 | 完整 build stdout/stderr |
| `sha256.txt` | UTF-8 plain text | 必須 | 二進位及 runtime dependency hashes |
| `source.patch` | unified diff, UTF-8 text | 必須 | 僅含本 POC 修改路徑 |
| `runtime-manifest.json` | UTF-8 JSON | 必須 | machine、ROM、binary、結果與證據 metadata |
| `evg-native-cjk-startup-full.png` | PNG, 原始 framebuffer 尺寸 | 必須 | Gate A 完整 640×400 畫面 |
| `evg-native-cjk-startup-closeup.png` | PNG, lossless crop，禁止 resize | 必須 | Gate A 兩組「鎖鏈」對照 |
| `evg-native-cjk-gameplay-dialogue-full.png` | PNG, 原始 framebuffer 尺寸 | PASS 必須 | Gate B 真實遊戲與對話框 |
| `evg-native-cjk-gameplay-dialogue-closeup.png` | PNG, lossless crop，禁止 resize | PASS 必須 | Gate B 真實 DDX 中文近照 |
| `evg-native-cjk-gameplay-after-ack.png` | PNG, 原始 framebuffer 尺寸 | PASS 必須 | acknowledge／重繪後無殘影證據 |
| `evg-native-cjk-failure.png` | PNG | 失敗時必須 | 黑屏、花屏或錯誤畫面 |
| `86box.cfg.txt` | UTF-8 plain text | 必須 | 去除私人路徑後的 86Box 關鍵設定 |
| `measurement.json` | UTF-8 JSON | 必須 | 圖片尺寸、字形 bounding boxes 與觀察值 |

最終結論另外寫到 tracked documentation：

```text
docs/research/evg-native-cjk-ingame-poc-result.md
```

### 10.1 runtime-manifest.json schema

```json
{
  "schema_version": 1,
  "result": "PASS | FAIL | BLOCKED | INCOMPLETE",
  "timestamp": "ISO-8601 with timezone",
  "source": {
    "root_commit": "hex sha",
    "upstream_commit": "hex sha",
    "modified_files": []
  },
  "build": {
    "command": "exact command",
    "toolchain": "Borland versions / bak CLI",
    "exit_code": 0,
    "log": "build.log"
  },
  "machine": {
    "emulator": "86Box exact version",
    "machine": "exact model",
    "cpu": "exact CPU",
    "ram_mb": 8,
    "video": "Video 7 VGA 1024i (HT208)",
    "video_bios": "exact ROM version",
    "video_ram_kb": 512
  },
  "runtime": {
    "requested_video_mode": 9,
    "loaded_chunk": "OVL:EVG:",
    "physical_resolution": [640, 400],
    "font_file": "ZH16.DAT",
    "gate_a_startup_complete": true,
    "gate_b_gameplay_complete": true,
    "dialogue_file": "DIAL_Z16.DDX",
    "dialogue_node_id": 1600003,
    "save_file": "startup.gam"
  },
  "artifacts": {
    "exe": "KRONDOR-EVG-NATIVE-POC.EXE",
    "vmcode": "VMCODE-EVG-NATIVE-POC.OVL",
    "startup_full": "evg-native-cjk-startup-full.png",
    "startup_closeup": "evg-native-cjk-startup-closeup.png",
    "gameplay_dialogue_full": "evg-native-cjk-gameplay-dialogue-full.png",
    "gameplay_dialogue_closeup": "evg-native-cjk-gameplay-dialogue-closeup.png",
    "gameplay_after_ack": "evg-native-cjk-gameplay-after-ack.png",
    "measurement": "measurement.json"
  },
  "notes": []
}
```

### 10.2 measurement.json schema

```json
{
  "source_image": "evg-native-cjk-startup-full.png",
  "source_dimensions": [640, 400],
  "image_resized": false,
  "control": {
    "text": "鎖鏈",
    "renderer": "existing logical EVG putpixel",
    "expected_cell": [32, 32],
    "observed_ink_bbox": [0, 0, 0, 0],
    "notes": ""
  },
  "experimental": {
    "text": "鎖鏈",
    "renderer": "POC physical EVG putpixel",
    "expected_cell": [16, 16],
    "observed_ink_bbox": [0, 0, 0, 0],
    "notes": ""
  },
  "gameplay_dialogue": {
    "source_image": "evg-native-cjk-gameplay-dialogue-full.png",
    "dialogue_file": "DIAL_Z16.DDX",
    "node_id": 1600003,
    "cjk_advance_logical_px": 8,
    "cjk_cell_physical_px": [16, 16],
    "rendered_line_count": 0,
    "characters_per_line": [],
    "after_ack_clean": false,
    "notes": ""
  }
}
```

`observed_ink_bbox` 是實際非背景 pixels 的 tight bounding box，不一定等於 cell size；
報告必須同時說明 advance/cell 與 ink bbox，不能把兩者混為一談。

## 11. source.patch 產生規則

Nested repository 的 patch 只能包含本 POC 路徑：

```text
bak/SRC/DRIVERS/VMCODE/EVG.ASM
bak/SRC/GFX/FONT/FONT.C
bak/SRC/GFX/FONT/FONT.H    # only if changed
bak/SRC/SYS/BOOT.C
```

禁止把既有 `VTHUNKS.ASM`、`DOSMEM.C`、`EMS.*`、`EMSDET.C` 修改放入 patch。
產生後必須以 `git diff --name-only` 或解析 patch header 驗證路徑白名單。

## 12. 結果報告格式

建立 `docs/research/evg-native-cjk-ingame-poc-result.md`，不得只回聊天訊息。
使用以下固定結構：

```markdown
# EVG Native CJK In-Game POC Result

## Verdict

PASS | FAIL | BLOCKED | INCOMPLETE

一句話回答：是否在未修改 emulator 的情況下，同時得到 2×2 遊戲畫面與
1×1 physical 16×16 中文。

## Time Spent

- Reconnaissance:
- Implementation:
- Build:
- Runtime setup/test:
- Total:

## Environment

- Root commit:
- Upstream commit:
- Build command:
- Toolchain:
- 86Box version:
- Machine/CPU/RAM:
- Video device/BIOS/VRAM:

## Source Changes

逐檔說明修改與理由。明列 vtable slot、ABI 與 physical address formula。

## Build Result

- Exit code:
- EXE size/SHA-256:
- VMCODE size/SHA-256:
- Warnings/errors:

## Runtime Result

- Requested mode:
- Loaded driver chunk evidence:
- Physical resolution evidence:
- Gate A control glyph observation:
- Gate A experimental glyph observation:
- Gate B gameplay/save reached:
- Gate B DDX file/node:
- Gate B dialogue call-chain evidence:
- Gate B wrap/advance/line-height observation:
- Gate B acknowledge/redraw observation:
- Plane mask / palette / present side effects:

## Evidence

使用 repository-relative links 連到 full screenshot、closeup、manifest、measurement、
build log、hash 與 source patch。

## Acceptance Checklist

- [ ] EVG loaded
- [ ] 640×400 physical mode
- [ ] ordinary graphics remain 2×2
- [ ] control glyph approximately 32×32 cell
- [ ] native glyph approximately 16×16 cell
- [ ] entered interactive gameplay
- [ ] real DIAL_Z16 node 1600003 rendered through dialogue pipeline
- [ ] native glyph advance and textwrap measurement agree
- [ ] dialogue redraw/acknowledge leaves no residue
- [ ] no plane/bank corruption
- [ ] no emulator modification
- [ ] all required artifacts exist

## Problems and Deviations

列出與本工作單不同之處；沒有則寫 None。

## Recommendation

只選一項：

- GO — 下一步把 physical text path 接到一個真實 dialogue surface。
- NO-GO — 停止 EVG mixed-resolution 路線。
- RETRY — 只有一個明確、低成本且尚未驗證的 blocker；寫出精確下一步。
```

## 13. 最終自我檢查

交付前執行並記錄：

```powershell
python -m pytest tests/unit/test_mock_hd_text.py -q
python tools/visual/mock_hd_text.py --suite
git diff --check
git -C upstream/betrayal-at-krondor diff --check
```

另外逐項確認：

- 沒有修改 DOSBox-X。
- 沒有覆蓋 `dist/test_v100_zh/`。
- 沒有清掉或混入使用者既有 nested-repo changes。
- 報告中的所有相對連結都存在。
- JSON 可由 `python -m json.tool` 解析。
- PNG 保持 lossless；closeup 只 crop、沒有 resize。
- PASS 結論有 runtime screenshot 支持，不是 offline mock。
- PASS 結論包含 gameplay dialogue screenshot；只有 startup screenshot 時必須是 INCOMPLETE。

## 14. 本 POC 成功後才可討論的下一步

只有 PASS 才提出下一階段，而且不要在本階段實作：

1. 將 physical text renderer 從暫借 slot 改成正式、可維護的 driver capability。
2. 定義 logical UI rectangle 與 physical glyph coordinates 的轉換規則。
3. 讓 `font_text_pixel_width()`／`TEXTWRAP.C` 在 EVG native-text mode 使用 8 logical
   units 的 CJK advance，或改成清楚的 physical-layout API。
4. 選一個真實 dialogue surface 做完整 render/erase/present/input 測試。
5. 評估 VGA fallback 與發行環境，不讓遊戲綁死修改版 emulator。

不要把離線 mock PASS 或固定字串 PASS 誤寫成「整個中文化已可改用 640×400」。
