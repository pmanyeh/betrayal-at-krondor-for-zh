# DOSBox-X VESA 640x400 CJK Gate POC — Agent 任務書

## 0. 任務結論與最高優先級限制

這是一個**獨立、可在數小時內結束的可行性閘門**，不是完整遊戲 driver
實作。唯一要回答的問題是：

> 一個使用本專案 16-bit DOS 工具鏈編譯的程式，能否在**未修改的標準
> DOSBox-X** 中，透過 VESA/VBE 的 640x400x256 模式，可靠畫出 2x 放大的
> 320x200 圖形與 1:1 physical 16x16 繁中文字形？

本任務必須實際執行 DOS 程式並取得 runtime 證據。只寫設計文件、只做 Python
mock、只證明 DOSBox-X 原始碼「理論上有 mode 0x100」，都不能判定 PASS。

### 強制停止線

- **不得修改 DOSBox-X 的 source、binary 或 renderer。**
- **不得繼續排查 86Box、Video 7 BIOS、JEMM386 或 EVG runtime。**
- **不得修改目前任何 production game source。** 尤其不得碰：
  - `upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/EVG.ASM`
  - `upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VTHUNKS.ASM`
  - `upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C`
  - `upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.H`
  - `upstream/betrayal-at-krondor/bak/SRC/SYS/BOOT.C`
  - `upstream/betrayal-at-krondor/bak/SRC/SYS/DOSMEM.C`
  - `upstream/betrayal-at-krondor/bak/SRC/SYS/EMS.C`
  - `upstream/betrayal-at-krondor/bak/SRC/SYS/EMS.H`
  - `upstream/betrayal-at-krondor/bak/SRC/SYS/EMSDET.C`
- **不得把 VESA driver 接入 `VMCODE.OVL`。** 本 Gate 通過後才另開下一階段。
- 不得覆蓋 `dist/test_v100_zh/` 的遊戲檔案或使用者存檔。
- 不得把離線產生的 PNG 冒充 DOSBox-X runtime screenshot。
- 不得下載或散佈遊戲本體、Borland 工具鏈或其他有授權限制的檔案。

所有新檔案先放在：

```text
scratchpad/vesa-640x400-cjk-poc/
```

唯一必須新增到正式文件區的結果報告為：

```text
docs/research/vesa-640x400-cjk-gate-poc-result.md
```

## 1. 為何現在做這個 Gate

既有 EVG POC 已完成 Video 7 planar physical-putpixel 與中文字形程式碼，卻因
86Box BIOS、磁碟開機及 FreeDOS/JEMM386 環境問題，沒有取得遊戲內驗證。EVG 又
依賴 DOSBox-X 並未模擬的特定 Video 7 硬體，因此不適合作為一般玩家的發布路徑。

標準 VBE mode `0x100` 的目標規格是：

```text
resolution:    640 x 400
colour depth:  8 bpp / 256 colours
memory model:  packed pixel
frame size:    at least 256,000 bytes (use BytesPerScanLine, not 640 as an assumption)
access:        real-mode banked VGA window, normally at segment A000h
```

完整 framebuffer 大於 64 KiB，所以成功設定模式還不夠；本 POC 必須真的跨越
bank boundary 寫入，才算驗證到將來 driver 最重要的硬體介面。

## 2. 時間盒

目標總工時為 **2～6 小時**：

| 階段 | 建議上限 |
|---|---:|
| 現況、工具鏈與 DOSBox-X binary 盤點 | 30 分鐘 |
| 獨立 DOS EXE 實作與編譯 | 120 分鐘 |
| DOSBox-X runtime、截圖與 readback | 120 分鐘 |
| 證據整理與結果報告 | 60 分鐘 |

超過 6 小時仍未取得 runtime 畫面，停止擴大實作，依第 12 節如實標記
`BLOCKED` 或 `INCONCLUSIVE`。不要因此開始改遊戲 driver 或模擬器。

## 3. 開始前的唯讀盤點

工作目錄：

```text
D:\git\betrayal-at-krondor-for-zh
```

先記錄：

```powershell
git rev-parse HEAD
git -C upstream/betrayal-at-krondor rev-parse HEAD
git status --short
git -C upstream/betrayal-at-krondor status --short
```

既有未提交內容全部視為使用者資料。不得 reset、stash、checkout、clean 或混入本
POC。把開始與結束時的 status 寫入報告。

盤點 DOSBox-X 時，依序採用：

1. 已安裝的官方 release binary。
2. `docs/baseline/phase0-baseline.md` 記載的官方測試版本。
3. 若只有 `D:\git\DOSBox-X-AI\build-memory\dosbox-x.exe` 可自動擷取畫面，可用它
   做輔助測試；但因它是專案 build，**不得單獨作為「標準 DOSBox-X 相容」的最終
   證據**。仍要用未修改 release binary 再跑一次，否則 verdict 至多
   `INCONCLUSIVE`。

必須記錄 DOSBox-X：

- 完整執行檔路徑
- 顯示的版本字串
- executable SHA-256
- 使用的設定檔 SHA-256
- `machine`、VESA/SVGA 類型、記憶體與輸出 renderer 設定

不得重新編譯 DOSBox-X，也不得為 POC 新增 emulator patch。

## 4. 必須使用／可使用的工具

### 4.1 原始碼與環境盤點

```text
Git / git status / git diff       保護 dirty worktree、記錄 commit
rg                                搜尋既有 VBE、字庫與 build 線索
PowerShell                        Windows 路徑、hash、啟動與產物整理
WSL2 Ubuntu                       若需取用既有 DOS/Borland build 環境
```

### 4.2 DOS 程式編譯

首選使用專案已驗證的 **Borland C++ 3.1 real-mode** 工具鏈。允許 agent 依現有環境
選擇最快的一次性方法：

- 在 DOSBox-X 內執行 `BCC.EXE`/`TLINK.EXE`；或
- 重用 `~/bak-toolchain` 的 FreeDOS/QEMU build environment；或
- 寫一個只服務本 POC 的 build batch/image wrapper。

不得為了方便改用 Win32/Win64 compiler 產出 Windows EXE，因為那不能證明原遊戲
所處的 16-bit real-mode 環境。若 Borland 實在不可用，可以 Open Watcom 16-bit DOS
target 作為診斷，但報告必須標記 compiler 差異，且 verdict 至多
`INCONCLUSIVE`，直到 Borland build 也通過。

必須保存 exact compile/link command 與完整文字 log。建議原始碼保持 C89/Borland
C++ 3.1 可接受語法，必要的 BIOS 呼叫可用少量 inline assembly 或獨立 `.ASM`。

### 4.3 Runtime 與證據

```text
DOSBox-X official release         唯一主要 runtime
DOSBox-X built-in screenshot      優先取得實際 guest framebuffer capture
Python 3.12+                      解析 JSON、RAW 與量測 PNG
Pillow                            lossless crop、像素與尺寸量測；禁止美化或縮放證據圖
certutil/Get-FileHash             SHA-256
```

可使用 DOSBox-X AI Debugger 做啟動、按鍵或擷取輔助，但 PASS 不得依賴修改過的顯示
行為；結果報告要清楚區分 official release 與 debug build 的證據。

## 5. POC 原始碼與目錄布局

建立：

```text
scratchpad/vesa-640x400-cjk-poc/
  src/
    VESAPOC.C
    VBE.H                 # 可選；VBE packed structs/prototypes
    VBE.ASM               # 可選；只在 C inline asm 不足時建立
    BUILD.BAT
    RUN.BAT
  runtime/
    VESAPOC.EXE
    ZH16.DAT
    RUN.BAT
  artifacts/
```

檔名可因 DOS 8.3 限制保持大寫短檔名。若 build wrapper 需要額外 Python 或
PowerShell script，放在本 POC 目錄內，不要擴散到 production build system。

## 6. VBE 實作要求

### 6.1 啟動前文字模式診斷

程式啟動後先在文字模式建立 `VESA.TXT`，逐步追加狀態，確保即使 graphics mode
失敗仍留下原因。至少記錄：

1. VBE controller info：`INT 10h, AX=4F00h`
2. 回傳是否為 `AX=004Fh`
3. `VESASignature`、VBE version、total memory
4. mode `0x100` info：`INT 10h, AX=4F01h, CX=0100h`
5. `ModeAttributes`
6. `XResolution`、`YResolution`、`BitsPerPixel`
7. `MemoryModel`
8. `BytesPerScanLine`
9. `WinAAttributes`、`WinBAttributes`
10. `WinGranularity`、`WinSize`、`WinASegment`、`WinBSegment`

VBE 資料結構必須 1-byte packed，並以 compile-time 或 runtime size check 防止
Borland alignment 造成 BIOS 填錯欄位。傳給 BIOS 的 buffer 必須位於 real-mode
可尋址 conventional memory，並正確設定 `ES:DI`。

### 6.2 模式驗證

只有下列條件成立才進入繪圖：

```text
mode supported
graphics mode
XResolution == 640
YResolution == 400
BitsPerPixel == 8
MemoryModel == packed-pixel-compatible value
at least one writable bank window exists
BytesPerScanLine >= 640
WinGranularity > 0
WinSize > 0
```

設定 mode：

```text
INT 10h, AX=4F02h, BX=0100h
success: AX=004Fh
```

本 Gate 不使用 linear framebuffer。原遊戲是 16-bit real mode，優先驗證最保守、
可移植的 banked window 路徑。

### 6.3 Bank switching

使用：

```text
INT 10h, AX=4F05h
BH=00h                  set window
BL=00h or 01h           selected writable window A/B
DX=window position in WinGranularity units
```

像素線性位址必須由 mode info 計算：

```text
linear_offset = y * BytesPerScanLine + x
```

不可硬編碼每列 640 bytes，也不可假設 `WinSize == WinGranularity == 64 KiB`。
選定一個能涵蓋目標 offset、依 `WinGranularity` 對齊的 window base，再將：

```text
DX             = window_base_bytes / granularity_bytes
window_offset  = linear_offset - window_base_bytes
```

限制在該 window 的有效大小內。快取目前 bank，只有跨 bank 時才呼叫 BIOS。

至少實作：

```c
int  vbe_detect(void);
int  vbe_query_mode(unsigned mode);
int  vbe_set_mode(unsigned mode);
int  vbe_set_bank(unsigned bank_units);
void vbe_putpixel(unsigned x, unsigned y, unsigned char color);
void vbe_fill_rect(...);
void vbe_restore_text_mode(void);
```

任何失敗路徑都要恢復 BIOS text mode `03h`，關檔並輸出錯誤碼。

## 7. 必須繪製的測試畫面

最終 guest 畫面必須同時包含以下內容，禁止只畫一句字：

### 7.1 VESA 與 bank boundary 證據

- 四周 1-pixel 邊框，必須真的到 `(0,0)` 與 `(639,399)`。
- 256 色或足以辨識 palette index 的色條。
- 一條從左上到右下的 1-pixel diagonal line。
- 在每個計算出的 bank boundary 前後畫不同顏色的水平標記。
- 畫面下半部必須有內容，以證明不是只寫第一個 64 KiB window。

### 7.2 320x200 邏輯畫面 2x 放大

用程式生成一個小型 320x200 logical test pattern，不需載入遊戲素材。每個 logical
pixel 必須寫成 physical 2x2 block，至少包含 checkerboard、矩形與圓或斜線，使
截圖可辨認其為 nearest-neighbour 2x，而非 DOSBox host scaling。

### 7.3 16x16 native CJK 與 32x32 對照組

從 runtime `ZH16.DAT` 讀取「鎖鏈」兩字；不得把 glyph bitmap 手工複製進 source。
開始實作前，用 `localization/generated/zh_mapping.json` 驗證本次檔案中的 glyph ID／
encoded bytes。既有研究資料指出候選值如下，但必須重新核對，不可盲信：

```text
鎖: glyph id 811, encoded bytes 85 2B
鏈: glyph id 812, encoded bytes 85 2C
```

同一畫面畫兩組：

```text
CONTROL:       每個 glyph bitmap pixel 畫成 2x2，cell 約 32x32 physical
NATIVE:        每個 glyph bitmap pixel 畫成 1x1，cell 為 16x16 physical
```

兩組要有英文 ASCII label、固定座標與可量測的外框。NATIVE 兩字的 advance 必須是
16 physical pixels。這個 Gate 不處理完整 Big5 parser、text wrapping 或 FreeType。

### 7.4 等待與退出

完成畫面後等待按鍵，讓人或自動化工具能取得 screenshot。按鍵後恢復 mode `03h`，
輸出摘要並正常結束。不得使用無法退出的 infinite loop。

## 8. DOSBox-X 設定與執行

建立獨立設定檔：

```text
scratchpad/vesa-640x400-cjk-poc/dosbox-x-vesa-poc.conf
```

要求：

- 使用 DOSBox-X 支援 VESA 的標準 SVGA machine；優先 `svga_s3`。
- 不使用 Video 7 machine。
- 不載入 FreeDOS、JEMM386、第三方 VESA TSR 或 UniVBE；本測試直接使用 DOSBox-X
  內建 DOS 與顯示 BIOS，排除先前 UMB 衝突。
- mount **只包含 POC runtime bundle** 的目錄，不 mount `dist/test_v100_zh/` 為可寫
  工作目錄。
- 設定獨立 capture directory。
- renderer/scaler 可以控制 host window 大小，但不能改變 guest 模式判定；記錄 exact
  config。

`RUN.BAT` 至少執行：

```bat
@echo off
VESAPOC.EXE
```

Agent 要保存實際啟動命令。若 DOSBox-X 支援命令列 `-c`，可自動 mount 與啟動；但
不得因 automation 困難跳過 runtime。

## 9. Runtime readback 與截圖

### 9.1 必要證據

使用 DOSBox-X 內建 screenshot/capture 功能取得：

```text
artifacts/vesa-640x400-full.png
artifacts/vesa-640x400-native-cjk-closeup.png
```

- `full.png` 必須是完整 guest framebuffer 畫面；若 DOSBox-X 輸出不是原生
  640x400，記錄原始尺寸與原因，不得偷偷 resize。
- `closeup.png` 只能做 lossless crop，不可 scale、濾鏡、銳化或重畫。
- 若只能取得 host-window screenshot，要清楚標記 `window capture`，並另外用程式的
  framebuffer readback 補強證據。

### 9.2 強烈建議的 readback

若 VBE window 可讀，程式在離開 graphics mode 前逐 bank 讀回
`BytesPerScanLine * 400` bytes，輸出：

```text
artifacts/FRAME.RAW
artifacts/PALETTE.RAW       # 若有讀取 DAC palette；768 bytes
```

再由 Python/Pillow 無縮放轉成：

```text
artifacts/vesa-640x400-readback.png
```

這只能作為 runtime readback 證據，不取代 DOSBox-X screenshot。若 window 不可讀，
把 `readback_supported=false` 與原因寫入 manifest，不因這一點單獨判 FAIL。

## 10. 量測與自動驗證

建立 `artifacts/measurement.json`，至少包含：

```json
{
  "source_image": "vesa-640x400-full.png",
  "source_kind": "dosbox-x guest capture | window capture",
  "source_dimensions": [640, 400],
  "image_resized": false,
  "mode": {
    "number_hex": "0x100",
    "x": 640,
    "y": 400,
    "bpp": 8,
    "bytes_per_scanline": 0,
    "window_granularity_kb": 0,
    "window_size_kb": 0,
    "writable_window": "A | B",
    "window_segment_hex": "0xA000",
    "bank_switch_count": 0
  },
  "control": {
    "text": "鎖鏈",
    "expected_cell_physical_px": [32, 32],
    "observed_ink_bbox": [0, 0, 0, 0]
  },
  "native": {
    "text": "鎖鏈",
    "expected_cell_physical_px": [16, 16],
    "observed_ink_bbox": [0, 0, 0, 0],
    "advance_physical_px": 16
  },
  "bank_boundary_markers_visible": false,
  "bottom_half_written": false,
  "notes": []
}
```

`observed_ink_bbox` 是實際非背景 ink 的 tight bbox，不要把 cell 外框當成字形 ink。
另外驗證：

- PNG 可由 Pillow 開啟。
- full capture 的尺寸與 capture 種類相符。
- 右下角 marker 存在。
- bank boundary 前後的指定像素顏色正確。
- CONTROL 與 NATIVE 的相對尺寸約為 2:1。
- `VESA.TXT` 報告所有關鍵 VBE calls 成功。

## 11. 必須產出的檔案、格式與檔名

所有 runtime/build artifacts 放在：

```text
scratchpad/vesa-640x400-cjk-poc/artifacts/
```

| 檔名 | 格式 | 必要性 | 內容 |
|---|---|---:|---|
| `VESAPOC.EXE` | 16-bit DOS MZ executable | 必須 | 可獨立執行的 POC |
| `BUILD.LOG` | UTF-8 plain text | 必須 | exact compiler/link stdout/stderr |
| `VESA.TXT` | DOS text；複製後可轉 UTF-8 | 必須 | VBE controller/mode/call 結果 |
| `dosbox-x-vesa-poc.conf` | INI-style text | 必須 | 實際 runtime config 副本 |
| `runtime-manifest.json` | UTF-8 JSON | 必須 | binary、環境、模式及 verdict metadata |
| `measurement.json` | UTF-8 JSON | 必須 | screenshot 與 glyph/bank 量測 |
| `sha256.txt` | UTF-8 plain text | 必須 | EXE、字庫、config、screenshots、source hashes |
| `vesa-640x400-full.png` | PNG, lossless | PASS 必須 | DOSBox-X 完整 runtime 畫面 |
| `vesa-640x400-native-cjk-closeup.png` | PNG, lossless crop | PASS 必須 | CONTROL/NATIVE 近照 |
| `FRAME.RAW` | raw 8bpp scanlines | 建議 | VBE framebuffer runtime readback |
| `PALETTE.RAW` | raw RGB triplets | 可選 | 256-entry palette |
| `vesa-640x400-readback.png` | PNG, lossless | readback 時必須 | RAW 無縮放轉檔 |
| `source-files.zip` | ZIP | 必須 | `src/`、build/run scripts；不得含工具鏈 |
| `failure.png` | PNG | 失敗時必須 | 可視錯誤或模式異常 |

不得把 `ZH16.DAT` 包進 `source-files.zip`；只記錄測試時所用字庫的 SHA-256。

### 11.1 runtime-manifest.json schema

```json
{
  "schema_version": 1,
  "result": "PASS | FAIL | BLOCKED | INCONCLUSIVE",
  "timestamp": "ISO-8601 with timezone",
  "source": {
    "root_commit": "hex sha",
    "upstream_commit": "hex sha",
    "preexisting_modified_files": [],
    "poc_source_files": []
  },
  "build": {
    "compiler": "Borland C++ 3.1",
    "memory_model": "exact model",
    "compile_command": "exact command",
    "link_command": "exact command",
    "exit_code": 0,
    "log": "BUILD.LOG"
  },
  "emulator": {
    "product": "DOSBox-X",
    "version": "exact version",
    "binary_path": "absolute path used",
    "binary_sha256": "hex",
    "official_unmodified_release": true,
    "machine": "svga_s3",
    "config": "dosbox-x-vesa-poc.conf"
  },
  "vbe": {
    "controller_call_ax_hex": "0x004F",
    "version_hex": "0x0000",
    "requested_mode_hex": "0x0100",
    "mode_info_call_ax_hex": "0x004F",
    "set_mode_call_ax_hex": "0x004F",
    "resolution": [640, 400],
    "bits_per_pixel": 8,
    "memory_model": 0,
    "bytes_per_scanline": 0,
    "window": "A | B",
    "window_segment_hex": "0xA000",
    "window_granularity_kb": 0,
    "window_size_kb": 0,
    "bank_switch_count": 0
  },
  "glyphs": {
    "font_file": "ZH16.DAT",
    "font_sha256": "hex",
    "text": "鎖鏈",
    "control_cell": [32, 32],
    "native_cell": [16, 16],
    "native_advance": 16
  },
  "artifacts": {
    "full_capture": "vesa-640x400-full.png",
    "closeup": "vesa-640x400-native-cjk-closeup.png",
    "runtime_log": "VESA.TXT",
    "measurement": "measurement.json",
    "readback": null
  },
  "notes": []
}
```

所有 JSON 用 `python -m json.tool` 驗證。

## 12. Verdict 規則

### PASS

以下全部成立才可判 PASS：

- 使用 16-bit DOS build；主要 build 是 Borland C++ 3.1。
- 使用未修改的標準 DOSBox-X release。
- `4F00h`、`4F01h`、`4F02h` 均回傳 `AX=004Fh`。
- mode info 實際為 640x400x8 packed-pixel compatible mode。
- 程式使用 mode info 回傳的 pitch/window/granularity，不依賴 64 KiB 假設。
- 上、下半部與跨 bank marker 都正確顯示。
- 320x200 pattern 在 guest framebuffer 內由程式放大成 2x。
- CONTROL 約 32x32 cell、NATIVE 為 16x16 cell，且「鎖鏈」可辨識。
- 有 DOSBox-X runtime full screenshot、closeup、VESA.TXT、manifest、measurement 與
  hashes。
- 程式可恢復 text mode 並正常退出。
- 沒有修改遊戲、DOSBox-X、86Box 或使用第三方 VESA TSR。

### FAIL

環境完整、程式與 bank 計算經檢查正確，但標準 DOSBox-X 的 mode `0x100` 不存在、
無 writable bank window、持續資料毀損，或必要畫面無法顯示，即判 FAIL。報告必須
區分是「VESA 路線不可行」還是「目前程式 bug」。

### BLOCKED

必要 compiler 或 official DOSBox-X binary 客觀缺失，且在時間盒內找不到已存在的
合法替代環境。必須提供已完成的 source、build/run instructions 與精確 blocker；
不能只寫「需要使用者操作」。DOSBox-X 不像 86Box 需要 BIOS CMOS/F1 流程，因此 GUI
自動化不便本身原則上不構成 blocker。

### INCONCLUSIVE

例如只有 Open Watcom build、只有修改版 DOSBox-X、只有 window capture 而無足夠
runtime/readback 證據，或 mode 成功但 bank boundary 尚未驗證。

## 13. 結果報告格式

建立：

```text
docs/research/vesa-640x400-cjk-gate-poc-result.md
```

內容至少包含：

```markdown
# DOSBox-X VESA 640x400 CJK Gate POC Result

## Verdict

PASS | FAIL | BLOCKED | INCONCLUSIVE

一句話回答：是否值得進入「遊戲內 VESA driver」下一階段。

## Time Spent

- Reconnaissance:
- Implementation:
- Build:
- Runtime/evidence:
- Total:

## Environment

- Root/upstream commits:
- Compiler/linker and exact commands:
- DOSBox-X path/version/SHA-256:
- Official unmodified release evidence:
- Config and machine type:

## VBE Detection and Mode Info

- 4F00h result:
- 4F01h result:
- 4F02h result:
- Resolution/bpp/memory model/pitch:
- Window attributes/segment/granularity/size:

## Implementation

- Packed struct and ES:DI handling:
- Bank calculation:
- Putpixel/fill/2x scaler:
- ZH16.DAT glyph lookup:
- Error recovery/text-mode restoration:

## Runtime Observation

- Boundary markers:
- Lower framebuffer:
- 2x logical graphics:
- CONTROL 32x32:
- NATIVE 16x16:
- Exit/restoration:

## Evidence

使用 repository-relative links 列出所有 artifacts。

## Acceptance Checklist

- [ ] Borland 16-bit DOS EXE
- [ ] official unmodified DOSBox-X
- [ ] VBE 0x100 detected and set
- [ ] mode is 640x400x8 packed pixel
- [ ] bank switching crosses full frame
- [ ] 320x200 graphics are programmatically scaled 2x
- [ ] ZH16 control glyphs are approximately 32x32 cells
- [ ] ZH16 native glyphs are 16x16 cells
- [ ] text mode restored and clean exit
- [ ] runtime screenshot and metadata complete
- [ ] no production/emulator changes

## Problems and Deviations

列出所有偏離；沒有則寫 None。

## Recommendation

GO | NO-GO | RETRY

只允許選一個，並附下一個最小行動。
```

## 14. Gate 通過後才可以提出的下一階段

若 PASS，**本次 agent 仍不可直接實作遊戲 driver**。只在結果報告最後提出一頁以內
的 integration outline，供下一張任務書使用：

1. 新增獨立 VESA driver chunk，不覆寫 `EVG`。
2. 追查 `VIDDRV.C` 的 mode/tag 對應、`DRIVERS.MAK`、`VMCODE.PAK` 與 50-slot
   renderer vtable。
3. 普通 320x200 graphics 維持 2x physical output。
4. 增加明確的 physical text primitive/capability，不再偷借 undocumented slot。
5. 先做 startup Gate，再做真實 DDX dialogue Gate。
6. 保留 VGA fallback；沒有 VBE 時顯示可理解錯誤或回退，不讓程式黑畫面。

不要預先把 `VIDEO_MODE_NEW` 或 `NEW:` tag 當成可自由占用的空位；目前 source 雖有
名稱線索，仍需先追完實際 caller、packer 與 runtime mapping。

## 15. 最終檢查命令

至少執行並記錄：

```powershell
Get-FileHash scratchpad/vesa-640x400-cjk-poc/artifacts/* -Algorithm SHA256
python -m json.tool scratchpad/vesa-640x400-cjk-poc/artifacts/runtime-manifest.json
python -m json.tool scratchpad/vesa-640x400-cjk-poc/artifacts/measurement.json
git diff --check
git -C upstream/betrayal-at-krondor diff --check
git status --short
git -C upstream/betrayal-at-krondor status --short
```

最後確認：

- production dirty files 與開始前完全一致。
- 沒有把 compiler/toolchain、遊戲資料或字庫塞進 source ZIP。
- screenshot 是 runtime 證據，closeup 只有 crop、沒有 resize。
- `VESA.TXT`、JSON、PNG 與 hashes 彼此對得上。
- 未完成 runtime 就不能寫 PASS。
- 不因 Gate PASS 宣稱完整遊戲 driver 已完成。
