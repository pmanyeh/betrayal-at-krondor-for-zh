# VESA In-Game Startup Gate A — Agent 任務書

## 0. 任務目的

本任務包含兩個依序執行、不可跳級的 Gate：

```text
Gate 0：修正並封存獨立 VESA 640x400 POC
    ↓ PASS
Gate A：讓真正的 KRONDOR.EXE 載入新的 VESA driver，
        在 640x400x256 顯示原遊戲 startup/loading 畫面，
        並疊加 32x32 CONTROL 與 16x16 NATIVE「鎖鏈」
```

本任務不是完整 VESA driver 製品化，也不是遊戲內真實對話 Gate。唯一核心問題是：

> 原遊戲的 driver loader、`VMCODE.OVL`、50-slot renderer vtable 與 startup
> pipeline，能否在 VESA mode `0x100` 下維持 320x200 logical graphics，輸出
> 640x400 的 2x2 physical graphics，並容納 1:1 physical CJK？

只有真正的 `KRONDOR.EXE` 載入新 chunk 並顯示 startup/loading 畫面，Gate A 才能
PASS。獨立 `VESAPOC.EXE`、Python mock、driver-init 自測或離線圖片都不能單獨算
Gate A PASS。

## 1. DOSBox-X 驗收條件

使用者接受 `D:\git\DOSBox-X-AI` 內的 MCP build 作為正式 runtime：

- 這是使用者自己維護的 fork。
- 修改範圍只有 MCP／自動化與除錯介面。
- 使用者確認沒有修改 VBE、VGA、renderer、framebuffer 或顯示輸出層。
- 不需要另找官方 release 重跑。

報告必須寫成：

> 本專案維護的 DOSBox-X MCP build；顯示、VBE 與渲染程式碼維持上游行為，未為
> 本 POC 特製。

不得寫「官方原版 binary」。必須記錄實際完整路徑、版本和重新計算的 SHA-256。
上一輪 artifacts 對應的候選檔為：

```text
D:\git\DOSBox-X-AI\dosbox-src\bin\x64\Release\dosbox-x.exe
version: 2026.06.02
previously observed SHA-256:
6C9985A7F91B2B5F557AF6332C3E3BCC321F73DE565BEE82DC6BE116CA53C88B
```

不可直接抄舊 hash，因為目錄內有多份 build。

## 2. 工作樹保護

```text
workspace: D:\git\betrayal-at-krondor-for-zh
nested repo: D:\git\betrayal-at-krondor-for-zh\upstream\betrayal-at-krondor
```

目前已有使用者翻譯、新字庫、EVG POC 與 EMS 等未提交修改。全部視為使用者資料。
嚴禁 `git reset`、`checkout --`、`restore`、`clean`、`stash`，也不得覆寫
`dist/test_v100_zh/` 或使用者 save files。

不得再修改：

```text
bak/SRC/DRIVERS/VMCODE/EVG.ASM
bak/SRC/GFX/DRIVER/VTHUNKS.ASM
bak/SRC/SYS/DOSMEM.C
bak/SRC/SYS/EMS.C
bak/SRC/SYS/EMS.H
bak/SRC/SYS/EMSDET.C
```

`BOOT.C`、`FONT.C`、`FONT.H` 已有 EVG POC 變動。若需加入 VESA hook，必須先保存
逐檔 snapshot，並讓本次 patch 只包含新 delta，不得把 EVG 修改冒充新成果。

開始先保存：

```powershell
git status --short
git -C upstream/betrayal-at-krondor status --short
git diff --binary > scratchpad/vesa-ingame-startup-gate-a/preexisting-root.patch
git -C upstream/betrayal-at-krondor diff --binary > scratchpad/vesa-ingame-startup-gate-a/preexisting-upstream.patch
```

把所有可能重疊的白名單檔案原樣複製至：

```text
scratchpad/vesa-ingame-startup-gate-a/pre-task-snapshot/
```

snapshot 只供稽核，不得用來覆蓋工作樹。

## 3. 時間盒與停止線

| 階段 | 建議上限 |
|---|---:|
| Gate 0 修正、重跑與封存 | 90 分鐘 |
| Mode/chunk/vtable 稽核 | 90 分鐘 |
| Gate A1 driver init probe | 180 分鐘 |
| Gate A2 startup/loading | 240 分鐘 |
| 證據與報告 | 60 分鐘 |

總目標 6～10 小時：

- Gate 0 未 PASS：停止，不進 Gate A。
- 只能顯示 driver-init 自測：判 `INCOMPLETE_A1`。
- startup 需要大量尚未理解的 renderer slots：停止並提交 coverage，不擴成完整重寫。
- 不轉回 86Box、Video 7、JEMM386。
- 不開始真實 DDX dialogue、完整 textwrap 或全遊戲測試。

## 4. 必讀來源

```text
docs/research/vesa-640x400-cjk-gate-poc-agent-task.md
docs/research/vesa-640x400-cjk-gate-poc-result.md
docs/research/evg-native-cjk-ingame-poc-result.md
docs/research/hd-text-fast-feasibility-poc.md
HANDOFF.md

upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VIDDRV.C
upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VIDDRV.H
upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VIDINIT.C
upstream/betrayal-at-krondor/bak/SRC/GFX/DRIVER/VIDDET.ASM
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/DRIVERS.MAK
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE.PAK
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/VGA.ASM
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/EVG.ASM
upstream/betrayal-at-krondor/bak/SRC/GEN/VIDVTBL.ASM
upstream/betrayal-at-krondor/bak/INCLUDE/structs.h
upstream/betrayal-at-krondor/bak/SRC/SYS/BOOT.C
upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C
```

已知事實：

- `video_init()` 呼叫 FAR driver init，再複製 50 slots／200 bytes 到
  `g_renderer_vtable`，並 patch far-pointer segments。
- `VMCODE.PAK` 與 `DRIVERS.MAK` 目前只有八個 video drivers。
- `VIDDRV.C` 雖有 `NEW:`、`HVG:` suffix，但 archive 沒有相應 chunk。
- modes 12～15 有特殊 remap；不能把 `NEW:` 當成可直接使用的空位。
- `BOOT.C` 已被 EVG POC 暫改為 `video_init(9, ...)`，不是原版基線。
- EVG 可作為 320x200 logical → 640x400 physical 行為參考，但其 Video 7 planar
  register code 不可搬進 VESA packed-pixel driver。

## 5. 工具

```text
Git / git diff / diff --check    保護兩層 dirty worktree
rg                               caller、mode、slot、tag 稽核
PowerShell                       Windows runtime、hash、artifact
WSL2 Ubuntu                      既有 build clone/toolchain
uv run bak build                 BCC 3.1 + TASM/TLINK + PACKOVL
DOSBox-X MCP build               runtime、按鍵與截圖
Python 3.12+ / Pillow            RAW、PNG 與真正像素量測
```

Python mock、Win32 prototype 或 EVG/86Box 舊截圖都不可取代 Gate A runtime。

## 6. Gate 0：獨立 POC 最終修正

工作目錄：

```text
scratchpad/vesa-640x400-cjk-poc/
```

### 必修項目

1. 修正 `FRAME.RAW` readback：現有前三 bank 使用 `65535U`，會讓邊界後各位移一
   byte。改為：

   ```text
   frame_bytes  = BytesPerScanLine * YResolution
   window_bytes = WinSize * 1024
   chunk         = min(window_bytes, remaining_frame_bytes)
   bank position 依 WinGranularity units 計算
   ```

2. `INT 10h AX=4F05h` 每次檢查 `AX==004Fh`；失敗要記 log、恢復 text mode、以
   非零 exit code 結束。
3. NATIVE「鎖」「鏈」origins 相差 16 pixels，不是現有的 18。
4. 完成繪圖後等待明確按鍵，不再自動於約 2.5 秒退出。
5. 分開保存：

   ```text
   vesa-standalone-dosbox-runtime.png  真正 DOSBox-X runtime/window capture
   vesa-standalone-readback.png        FRAME.RAW 轉圖
   vesa-standalone-cjk-closeup.png     runtime capture 的 lossless crop
   ```

   不可用 readback PNG 覆寫 runtime capture。
6. `measurement.json` 必須從 PNG pixels 計算 glyph ink bbox、origin distance、bank
   markers、lower-framebuffer marker 與右下角 border；不可把 source constants 當
   observed values。
7. artifacts 固定後才產生 `sha256.txt` 和報告；報告 hash 必須與目前檔案一致。
8. `scratchpad/vesa-640x400-cjk-poc/bc31/` 是 local toolchain cache，不得進 Git、
   source ZIP、artifact archive 或發布物。未獲刪除授權時可保留原處並標記
   `do not commit/distribute`。

### Gate 0 PASS

- Borland C++ 3.1 16-bit DOS EXE。
- 使用者接受的 DOSBox-X MCP build，exact path/version/hash 完整。
- VBE `4F00/4F01/4F02/4F05` 成功。
- 完整 framebuffer readback 無 bank 拼接位移。
- 真正 runtime capture 顯示完整 VESA 畫面。
- Native origin distance 16 px。
- measurement、manifest、hash、報告一致。

更新：

```text
docs/research/vesa-640x400-cjk-gate-poc-result.md
```

開頭標記：

```text
Gate 0 final audit: PASS
Accepted runtime: user-maintained DOSBox-X MCP build; display/VBE paths unchanged
```

Gate 0 未 PASS 就停止。

## 7. Gate A Phase 1：Mode、Chunk、Vtable 稽核

建立：

```text
scratchpad/vesa-ingame-startup-gate-a/driver-integration-map.md
scratchpad/vesa-ingame-startup-gate-a/slot-coverage.json
```

### Mode/tag 決策

追查所有 `video_init()`、`g_bRequestedVideoMode`、`video_detect_adapter()`、
`g_apVideoDriverChunkNames`、`VIDEO_MODE_NEW`、`HVG:`、`NEW:` caller，回答：

- `video_init` 參數與 adapter detection 如何決定實際 chunk？
- mode 10 (`HVG:`) 是否有 caller、driver 或資料依賴？
- modes 12～15 remap 是否阻止 `NEW:` 直接載入？
- 擴充 mode table 是否有 binary/setup assumptions？

新 driver tag 使用：

```text
VSV:
```

優先新增明確 suffix/mapping。若快速 POC 必須暫用經證實未使用的 `HVG:` mode slot，
archive tag 仍須為 `VSV:`，並標記 `POC-only mode-slot reuse`。不得覆寫 `EVG:`、
`VGA:`，也不得未經稽核直接占用 `NEW:`。

### 50-slot coverage

`slot-coverage.json`：

```json
{
  "schema_version": 1,
  "reference_driver": "EVG | VGA | mixed",
  "slots": [
    {
      "index": 0,
      "name": "slot_00_null",
      "called_during_startup": false,
      "required_for_gate_a": false,
      "implementation": "stub | native | adapted | not_implemented",
      "reference_symbol": "",
      "vsv_symbol": "",
      "notes": ""
    }
  ],
  "startup_required_slot_count": 0,
  "implemented_slot_count": 0
}
```

以 static caller search、thunks 和必要 runtime trace 判斷 startup 需要哪些 slots，不能
假設只有 putpixel。優先稽核 slots 1～8、13～24、29～40。

## 8. Gate A Phase 2：VSV driver

新增：

```text
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/VSV.ASM
```

VSV 硬體層必須是：

```text
detect:    INT 10h AX=4F00h
query:     INT 10h AX=4F01h CX=0100h
set mode:  INT 10h AX=4F02h BX=0100h
set bank:  INT 10h AX=4F05h
format:    640x400x8 packed pixel
address:   y * BytesPerScanLine + x
window:    mode-info-selected writable A or B
```

不得保留 EVG 的 Video 7 probe、mode `0x66`、Sequencer F6 banking、plane mask 或 planar
addressing。

### Driver init

- 驗證 640x400x8、MemoryModel、pitch、WinSize、WinGranularity、writable window。
- 不符就回報 failure，不進黑畫面。
- 設 mode `0x100`、初始化 bank cache。
- 填入 startup pipeline 需要的 `GraphicsContext` page/screen fields。
- 依 ABI 回傳 `DX:SI = driver segment:vtable offset`。
- 提供完整 50-slot template；確認 Gate A 不會呼叫的 slot 使用安全 FAR stub。

### Logical 與 physical paths

```text
logical putpixel(x=0..319,y=0..199)
  -> physical (2x,2y), (2x+1,2y), (2x,2y+1), (2x+1,2y+1)

physical putpixel(x=0..639,y=0..399)
  -> exactly one framebuffer pixel
```

slot 22 維持 logical semantics。Gate A 可暫用已證明無 production caller 的 slot 9
暴露 physical putpixel，但必須記入 coverage 並標示 POC ABI；不得修改
`VTHUNKS.ASM` 全域改變其他 driver。

### Bank 與最低效能要求

- 不硬編碼 pitch/WinSize/WinGranularity。
- window position 用 granularity units，window offset 必須小於 WinSizeBytes。
- 每次 `4F05h` 檢查成功，並 cache current bank。
- 不可在同一連續 span 的每個 pixel 重複切 bank。
- 記錄 startup bank switches 與 BIOS ticks。
- startup 超過 10 秒或無法互動，不可宣稱可製品化。

## 9. Build system 與白名單

```text
新增：
bak/SRC/DRIVERS/VMCODE/VSV.ASM

允許修改：
bak/SRC/DRIVERS/DRIVERS.MAK
bak/SRC/DRIVERS/VMCODE.PAK
bak/SRC/GFX/DRIVER/VIDDRV.C
bak/SRC/GFX/DRIVER/VIDDRV.H
bak/SRC/SYS/BOOT.C
bak/SRC/GFX/FONT/FONT.C
bak/SRC/GFX/FONT/FONT.H
```

需要白名單外 production file 時先停止並報告，不得自行擴大。

- `DRIVERS.MAK`：加入 `VSV.EXE` TASM/TLINK rule，保留原八個 driver。
- `VMCODE.PAK`：新增 `VSV: OUT\VSV.EXE`，不重排原 chunks。
- `VIDDRV`：依稽核結果接 mode/tag，避免 array out-of-bounds，保留 VGA fallback。
- `BOOT.C`：只做最小 VSV mode 與 marker hook，以 mode guard 隔離 EVG POC。
- `FONT.C/H`：從 `ZH16.DAT`／現有 EMS 字庫路徑取「鎖鏈」，CONTROL 走 logical
  renderer，NATIVE 走 physical renderer；不可烘焙 bitmap。

用 packer/list/extract 驗證 `VMCODE.OVL` 含 `OVL:VSV:` 且原八 chunks 仍存在。

## 10. Runtime Gate

### Gate A1：Driver load/init probe

先證明：

- `KRONDOR.EXE` 開啟 `VMCODE.OVL` 並載入 `OVL:VSV:`，不是 fallback。
- VSV init 設定 mode `0x100`。
- physical primitive 畫四角、bank markers 與 `VSV A1` signature。
- 可安全等待／繼續，不死鎖。

A1 自測是診斷，不是完整 PASS。

### Gate A2：真正 startup/loading pipeline

讓遊戲正常經過：

```text
boot_engine_hardware_init()
  -> video_init(VSV mode)
  -> real startup/loading rendering calls
  -> present/palette
```

必須看到：

- 原 startup/loading graphics 可辨認、構圖正確。
- 320x200 logical graphics 在 640x400 中為程式內 2x2 blocks。
- palette 正確，沒有 bank tearing、全黑、錯色或 plane fan。
- CONTROL「鎖鏈」約 32x32 physical cell。
- NATIVE「鎖鏈」16x16 cell、origin distance 16。
- 可繼續至下一正常 startup state 或主選單，不靠 infinite loop 截圖。

遇到未實作 slot，記錄 index、caller、參數與畫面狀態，只補 Gate A 需要的最小實作。

## 11. Build 與隔離部署

使用 WSL ext4 clone：

```text
~/krondor-build
BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain
```

```powershell
wsl -e bash -lc "cd ~/krondor-build && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain && export PATH=\$HOME/.local/bin:\$PATH && uv run bak build"
```

Windows dirty source 以明確白名單同步到 WSL；不得使用帶 `--delete` 的 mirror。保存 exact
sync commands。

新增 VSV 後 `VMCODE.OVL` 不會與原版 byte-identical，fingerprint mismatch 不是 build
failure。真正 acceptance：

- BCC/TASM/TLINK/PACKOVL 無 error。
- `KRONDOR.EXE`、`VMCODE.OVL`、`SX.OVL` 產生。
- VMCODE 可列出/extract `OVL:VSV:` 與原八 chunks。
- `SX.OVL` 不應因本任務改變；記錄 hash。

建立隔離 runtime：

```text
scratchpad/vesa-ingame-startup-gate-a/runtime/
```

可從 `dist/test_v100_zh/` 複製執行所需檔案，但不得覆寫原目錄，也不得把完整遊戲資料
加入 Git／ZIP／artifacts archive。

## 12. DOSBox-X 設定

建立：

```text
scratchpad/vesa-ingame-startup-gate-a/dosbox-x-vsv-gate-a.conf
```

要求：

- `machine=svga_s3`
- 不載入 JEMM386、UniVBE、Video 7 BIOS 或第三方 VESA TSR。
- mount 隔離 runtime，capture 指向本 POC artifacts。
- 不 mount/write `dist/test_v100_zh/`。
- 記錄 cycles、core、memsize、renderer、scaler、aspect。
- 保存 launch command、等待條件、按鍵、capture 與 exit sequence。

Gate A2 必須保留帶 DOSBox-X chrome 的 window capture；若能取得 built-in guest capture
也要保留。readback PNG 不得冒名為 runtime screenshot。

## 13. 必須產出的檔案

目錄：

```text
scratchpad/vesa-ingame-startup-gate-a/artifacts/
```

| 檔名 | 格式 | 必要性 | 說明 |
|---|---|---:|---|
| `KRONDOR-VSV-GATE-A.EXE` | 16-bit DOS MZ | 必須 | Gate A 遊戲執行檔 |
| `VMCODE-VSV-GATE-A.OVL` | RES/OVL | 必須 | 含 `OVL:VSV:` |
| `VSV-GATE-A.EXE` | 16-bit DOS MZ | 必須 | PACKOVL 前 driver |
| `VSV-GATE-A.MAP` | TLINK map text | 必須 | symbols/offsets |
| `build.log` | UTF-8 text | 必須 | sync/build/link/pack log |
| `vmcode-list.txt` | UTF-8 text | 必須 | VSV 與原 chunks |
| `preexisting-root.patch` | binary diff | 必須 | 開始前 root dirty state |
| `preexisting-upstream.patch` | binary diff | 必須 | 開始前 nested dirty state |
| `source-delta.patch` | unified diff | 必須 | 只含本 Gate delta |
| `driver-integration-map.md` | Markdown | 必須 | mode/tag/loader 決策 |
| `slot-coverage.json` | UTF-8 JSON | 必須 | 50-slot coverage |
| `runtime-manifest.json` | UTF-8 JSON | 必須 | build/runtime metadata |
| `measurement.json` | UTF-8 JSON | 必須 | screenshot 實際量測 |
| `sha256.txt` | UTF-8 text | 必須 | 最終 hashes |
| `vsv-gate-a1-driver-init-window.png` | PNG | A1 必須 | driver init 自測 |
| `vsv-gate-a2-startup-window.png` | PNG | PASS 必須 | startup + window chrome |
| `vsv-gate-a2-startup-guest.png` | PNG | PASS 建議 | guest 原尺寸 capture |
| `vsv-gate-a2-cjk-closeup.png` | PNG crop | PASS 必須 | CONTROL/NATIVE |
| `vsv-gate-a-failure.png` | PNG | 失敗時必須 | 可視失敗證據 |

不得把 runtime game data、`ZH16.DAT`、BC31 或 DOSBox-X binary 放入 artifact archive。

## 14. runtime-manifest.json 最小 schema

```json
{
  "schema_version": 1,
  "result": "PASS | FAIL | BLOCKED | INCOMPLETE_A1 | INCONCLUSIVE",
  "timestamp": "ISO-8601 with timezone",
  "source": {
    "root_commit": "hex",
    "upstream_commit": "hex",
    "preexisting_modified_files": [],
    "gate_delta_files": []
  },
  "build": {
    "command": "exact command",
    "compiler": "Borland C++ 3.1",
    "assembler": "TASM exact version",
    "linker": "TLINK exact version",
    "packer": "PACKOVL",
    "exit_code": 0,
    "log": "build.log"
  },
  "emulator": {
    "description": "user-maintained DOSBox-X MCP build; display/VBE paths unchanged",
    "path": "absolute path",
    "version": "exact version",
    "sha256": "hex",
    "machine": "svga_s3",
    "config": "dosbox-x-vsv-gate-a.conf"
  },
  "driver": {
    "requested_mode": 0,
    "loaded_tag": "OVL:VSV:",
    "vbe_mode_hex": "0x0100",
    "resolution": [640, 400],
    "bpp": 8,
    "memory_model": 4,
    "bytes_per_scanline": 0,
    "window": "A | B",
    "window_segment_hex": "0xA000",
    "window_granularity_kb": 0,
    "window_size_kb": 0,
    "gate_a_required_slots": [],
    "gate_a_implemented_slots": [],
    "startup_bank_switches": 0,
    "startup_elapsed_ticks": 0
  },
  "runtime": {
    "gate_a1_driver_init": true,
    "gate_a2_real_startup": true,
    "original_startup_graphics_visible": true,
    "logical_graphics_2x": true,
    "control_cjk_cell": [32, 32],
    "native_cjk_cell": [16, 16],
    "native_advance_physical_px": 16,
    "palette_ok": true,
    "continued_past_startup": true
  },
  "artifacts": {},
  "notes": []
}
```

## 15. Verdict

### PASS

- Gate 0 final audit PASS。
- 真正 `KRONDOR.EXE` 載入 `OVL:VSV:`。
- VBE `0x100` 為 640x400x256 packed pixel。
- 真實 startup/loading graphics 正確 2x。
- palette、banks、present 無明顯損壞。
- CONTROL 約 32x32、NATIVE 16x16、advance 16。
- 可繼續到下一正常狀態，沒有 infinite loop。
- runtime screenshots、build/map/hash/manifest 可重現且一致。
- 未修改 DOSBox-X 顯示層、EVG、VGA、EMS 或使用者 distribution/save。

### INCOMPLETE_A1

VSV 已由遊戲載入並顯示 init probe，但真實 startup pipeline 尚未完成。

### FAIL

獨立 VESA 已通過，但 engine ABI/page model 與本 VESA 方案經證據確認不可行。單一尚未
實作 slot 不得草率判 FAIL。

### BLOCKED

同一 blocker 經三輪合理嘗試仍無法排除。GUI automation 不便本身不算 blocker。

### INCONCLUSIVE

只有離線圖、driver 未證明載入，或 artifacts 與 runtime binary 無法對應。

## 16. 結果報告

建立：

```text
docs/research/vesa-ingame-startup-gate-a-result.md
```

必須包含：

```markdown
# VESA In-Game Startup Gate A Result

## Verdict
PASS | FAIL | BLOCKED | INCOMPLETE_A1 | INCONCLUSIVE

一句話回答：是否進入真實 DDX Gate B。

## Gate 0 Final Audit
## Time Spent
## Environment and DOSBox-X MCP Build
## Mode and Chunk Integration
## VSV Architecture
## Renderer Slot Coverage
## Build and Pack Result
## Gate A1 Runtime
## Gate A2 Startup Runtime
## Typography and Pixel Measurements
## Evidence
## Acceptance Checklist
## Problems and Deviations
## Recommendation
GO_TO_GATE_B | RETRY_GATE_A | NO_GO
```

## 17. Source delta 稽核

`source-delta.patch` 必須由 `pre-task-snapshot` 與最後檔案逐一產生；不能直接用整個
nested repo 的 `git diff`，否則會混入 EVG/EMS 舊修改。

報告分列：

```text
pre-existing dirty files
Gate A modified existing files
Gate A newly created files
```

比較開始與結束的非白名單 hashes；非白名單不得改變。

## 18. 最終驗證

```powershell
python -m json.tool scratchpad/vesa-ingame-startup-gate-a/artifacts/slot-coverage.json
python -m json.tool scratchpad/vesa-ingame-startup-gate-a/artifacts/runtime-manifest.json
python -m json.tool scratchpad/vesa-ingame-startup-gate-a/artifacts/measurement.json
Get-FileHash scratchpad/vesa-ingame-startup-gate-a/artifacts/* -Algorithm SHA256
git diff --check
git -C upstream/betrayal-at-krondor diff --check
git status --short
git -C upstream/betrayal-at-krondor status --short
```

另驗證：

- VMCODE 可列出 `OVL:VSV:` 與原八 chunks。
- artifact EXE/OVL hashes 等於 runtime 使用的檔案。
- screenshot timestamp 屬於該次 session。
- screenshot 不是 mock/readback 冒名。
- observed measurement 來自 PNG，不是 source 常數。
- 報告 hashes 與現有檔案完全一致。
- Gate A2 未通過，絕不寫「遊戲內 VESA 已完成」。

## 19. PASS 後唯一下一步

Gate A PASS 後只提出下一張任務書，不在本任務繼續：

```text
Gate B：真實 DDX dialogue
  DIAL_Z16 node 1600003
  -> dialog pipeline
  -> textwrap measurement
  -> FONT.C
  -> VSV physical 16x16 CJK
  -> pagination / erase / redraw / acknowledge
```

Gate B 才處理正式 physical capability/API、CJK logical metrics 8px、ASCII/CJK 混排、
clipping 與翻頁。
