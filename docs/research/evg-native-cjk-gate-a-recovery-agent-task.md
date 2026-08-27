# EVG Native CJK Gate A：開機救援與實機字形驗證工作單

## 0. 執行指令

你要完成的是一個**範圍非常窄的 recovery task**：建立正確可開機的 FreeDOS
硬碟映像，在未修改 86Box/DOSBox-X 的情況下執行現有 POC binaries，取得 startup
畫面中 32×32 與 16×16「鎖鏈」的實際 runtime 證據。

本工作完成 Gate A 後立即停止。不要實作 Gate B，不要修改 DDX、dialogue、textwrap
或 production source code，也不要再新增鍵盤／視窗／截圖自動化實驗工具。

## 1. 已確認的根因

目前失敗的映像：

```text
scratchpad/evg-native-cjk-poc/vm/krondor_evg.img
```

已由主 Agent 直接讀取 binary sectors，確認：

```text
file size:                  42,519,040 bytes (977 x 5 x 17 x 512)
MBR bootstrap non-zero:     0 bytes
MBR signature [510:512]:    00 00
partition entry 1:          all zero
LBA 17 VBR jump:            00 00 00
LBA 17 VBR signature:       00 00
```

這不是可修復的「小 geometry 誤差」；它實際上是未成功格式化的全零開機區。
`tools/build_type17_disk.py` 忽略了 `sfdisk`／mtools 失敗結果，因此錯誤映像仍被複製成
最終檔案。禁止再使用它的輸出。

目前 86Box 設定：

```ini
hdd_01_parameters = 63, 16, 65, 0, ide
```

這組 geometry 與現成 FreeDOS base image 相符；不需要改成 Type-17。

## 2. 成功定義

Gate A PASS 必須全部成立：

1. FreeDOS 硬碟映像有有效 MBR、active partition 與 VBR。
2. FreeDOS 啟動並提供 EMS。
3. Guest 實際執行 `KRONDOR.EXE`，不是只看到主機板或 Video 7 BIOS。
4. 遊戲載入 EVG mode 9／`OVL:EVG:`。
5. Startup 畫面同時看得到：
   - control「鎖鏈」：現有 logical EVG putpixel，約 32×32 physical cell。
   - experimental「鎖鏈」：slot 9 physical putpixel，約 16×16 physical cell。
6. 畫面沒有明顯 plane fan、隔行、錯色、重影或 framebuffer corruption。
7. 有 runtime screenshot，不以 source code 或 offline mock 代替。

只有 BIOS POST、FreeDOS prompt、build success 或 source inspection 都不算 PASS。

## 3. 時間盒與停止條件

- 修正 canonical disk builder：30 分鐘。
- 建圖與靜態驗證：20 分鐘。
- 86Box runtime／人工 F1：30 分鐘。
- 單一明確 runtime bug 修正：最多 60 分鐘。
- 總時間上限：2 小時。

若有效磁碟已啟動，但 POC 在進入 startup 畫面前 crash，保留畫面與錯誤，結果記為
`FAIL`。若唯一阻塞是必須由使用者按 F1，立即明確通知使用者，不要再花時間撰寫
Win32 synthetic-input scripts。

## 4. 禁止事項

- 不修改以下 production source：

```text
upstream/betrayal-at-krondor/bak/SRC/DRIVERS/VMCODE/EVG.ASM
upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C
upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.H
upstream/betrayal-at-krondor/bak/SRC/SYS/BOOT.C
```

- 不修改或重建 POC EXE/OVL。
- 不修改 86Box 或 DOSBox-X source/binary。
- 不建立 Type-17、128 MB 或其他替代 CHS 實驗。
- 不再新增 `test_*input.py`、`send_*key.py`、window-focus 或連續截圖 scripts。
- 不刪除使用者既有檔案或 nested-repository changes。
- 不覆蓋壞 image；新的輸出使用不同檔名。
- 不進行 Gate B。

## 5. 必須使用的輸入

### 5.1 Bootable FreeDOS base

```text
/home/pmanyeh/bak-toolchain/freedos/freedos.img
size:   33,554,432 bytes
SHA256: e6b9a2e7694d92209ea3ab2a99ca820de1bc9fe3dd3360350b6a0103967bf58b
```

已驗證 base：

```text
MBR bootstrap:       present
MBR signature:       55 AA
partition 1:         active, FAT16 type 04
partition start LBA: 63
partition size:      65,457 sectors
filesystem offset:   32,256 bytes
geometry:            65 cylinders, 16 heads, 63 sectors
```

### 5.2 現有 POC binaries

```text
scratchpad/evg-native-cjk-poc/KRONDOR-EVG-NATIVE-POC.EXE
SHA256 4b71c99013732ed63561680689d7483325f498a7e2268dbdff8f0b59d6ff57ac

scratchpad/evg-native-cjk-poc/VMCODE-EVG-NATIVE-POC.OVL
SHA256 a1d138e069553fc45c235a3647009602fa5e5d07ed7e4482ceeba5c542f64e1a

scratchpad/evg-native-cjk-poc/SX.OVL
SHA256 d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb

localization/generated/ZH16.DAT
SHA256 0a36619ba5dc257da820147ba38bcddedc3aa6686b8ddfe45037cb851420598d
```

先重新計算 hashes。任何不一致都停止並報告，不要自行挑另一版 binary。

### 5.3 Game data

```text
dist/test_v100_zh/
```

只複製 runtime 必要檔案。延用既有 filter，略過：

```text
*.wri, *.bmp, *.sol, *.hlp, *.txt, *.doc
*.pre-*, *.new.*, ZH_MAP*, DDX_BUILD*
```

POC 的 `KRONDOR.EXE`、`VMCODE.OVL`、`SX.OVL`、`ZH16.DAT` 必須最後複製，覆蓋
distribution 中同名版本。

## 6. 允許使用的工具

```text
WSL2 Ubuntu
Python 3
mtools: mcopy, mdir, mtype, mdel, mdeltree
sha256sum / PowerShell Get-FileHash
86Box 6.0 build 9001（現有官方安裝）
Video 7 VGA 1024i (HT208), 512 KB VRAM
Pillow（只做 screenshot 尺寸確認與 lossless crop）
```

不要使用 `sfdisk`、`fdisk`、`mformat` 或自行產生 MBR/VBR。本工作直接複製已知可開機
base，避免再次破壞 boot chain。

## 7. Canonical disk builder

只修正並使用：

```text
tools/build_clean_freedos_disk.py
```

不要建立第五個 disk builder。若原檔名稱不夠清楚，可在報告註明，但本階段不要重新命名。

### 7.1 新輸出檔名

```text
scratchpad/evg-native-cjk-poc/vm/krondor_evg_gate_a.img
```

禁止覆蓋既有壞檔 `krondor_evg.img`。

### 7.2 Builder 必須 fail-fast

所有 subprocess 必須：

- 檢查 non-zero exit code。
- 顯示 command、stdout、stderr。
- 任一步失敗就停止，禁止繼續複製「完成」映像。
- 最終 static validation 失敗時不得輸出成功訊息。

不要再使用只印 `Notice` 然後繼續的 `run_mtool()`。

### 7.3 正確建圖順序

1. 將 FreeDOS base 複製到暫存檔。
2. 以 mtools partition offset `@@32256` 操作 FAT filesystem。
3. 刪除 `SETUP.BAT` 與不需要的 `PACKAGES` tree，取得遊戲空間。
4. 保留 `\FREEDOS\BIN`，尤其 `HIMEMX.EXE`、`JEMM386.EXE`、`COMMAND.COM`。
5. 寫入新的 `FDCONFIG.SYS` 與 `FDAUTO.BAT`。
6. 複製 filtered game data。
7. 最後複製四個指定 POC/runtime files。
8. 在暫存檔完成所有 static validation。
9. 驗證全部通過後，才 copy/replace 新輸出檔
   `krondor_evg_gate_a.img`。

## 8. FreeDOS startup files

### 8.1 FDCONFIG.SYS

必須保留 FreeDOS command shell，並啟用 EMS。建議最小內容：

```text
!LASTDRIVE=Z
!BUFFERS=20
!FILES=40

DOS=HIGH
DOS=UMB
DOSDATA=UMB

DEVICE=\FREEDOS\BIN\HIMEMX.EXE
DEVICE=\FREEDOS\BIN\JEMM386.EXE

SHELLHIGH=\FREEDOS\BIN\COMMAND.COM \FREEDOS\BIN /E:2048 /P=\FDAUTO.BAT
```

若 JEMM386 在此 486 machine 上需要參數，只允許依其內建 help/官方用法做最小修正，
並在報告記錄。禁止用 `NOEMS`。

### 8.2 FDAUTO.BAT

```bat
@echo off
SET DOSDIR=\FREEDOS
SET PATH=%DOSDIR%\BIN
SET LANG=
SET TZ=
CD \
echo EVG Native CJK Gate A
MEM /C
KRONDOR.EXE
echo KRONDOR returned ERRORLEVEL %ERRORLEVEL%
pause
```

`MEM /C` 是 EMS runtime 證據的一部分。不要清除其輸出後立刻結束 VM；若遊戲啟動，
startup POC 畫面才是主要證據。

## 9. 必要 static validation

Builder 必須驗證並輸出：

```text
file size == 33,554,432
MBR [510:512] == 55 AA
partition entry 1 boot flag == 80
partition type == 04
partition start LBA == 63
VBR at LBA 63 [510:512] == 55 AA
VBR first byte is EB or E9
```

使用 `mdir -i image@@32256 ::` 驗證至少存在：

```text
KERNEL.SYS
FDCONFIG.SYS
FDAUTO.BAT
KRONDOR.EXE
VMCODE.OVL
SX.OVL
ZH16.DAT
STARTUP.GAM
```

使用 `mtype` 驗證：

```text
FDCONFIG.SYS contains HIMEMX.EXE
FDCONFIG.SYS contains JEMM386.EXE
FDAUTO.BAT contains KRONDOR.EXE
```

從 image 抽出四個 runtime files，重新計算 SHA-256，必須等於 Section 5.2。不可只驗證
host source files。

靜態驗證產出：

```text
scratchpad/evg-native-cjk-poc/gate-a-disk-validation.json
scratchpad/evg-native-cjk-poc/gate-a-disk-build.log
```

### 9.1 gate-a-disk-validation.json 格式

```json
{
  "schema_version": 1,
  "result": "PASS | FAIL",
  "image": "vm/krondor_evg_gate_a.img",
  "size_bytes": 33554432,
  "geometry": {
    "cylinders": 65,
    "heads": 16,
    "sectors": 63
  },
  "mbr": {
    "signature": "55aa",
    "active": true,
    "partition_type": 4,
    "start_lba": 63
  },
  "vbr": {
    "lba": 63,
    "jump_valid": true,
    "signature": "55aa"
  },
  "ems_configured": true,
  "required_files": {},
  "embedded_sha256": {},
  "errors": []
}
```

## 10. 86Box configuration

沿用現有 machine/video 設定，僅把 disk filename 指向新 image：

```ini
[Machine]
machine = award495
mem_size = 4096

[Video]
gfxcard = v7_vga_1024i
vram = 512

[Hard disks]
hdd_01_fn = krondor_evg_gate_a.img
hdd_01_ide_channel = 0:0
hdd_01_parameters = 63, 16, 65, 0, ide
```

不要再改 geometry。設定副本輸出：

```text
scratchpad/evg-native-cjk-poc/86box-gate-a.cfg.txt
```

## 11. Runtime 流程

1. 啟動既有 86Box profile。
2. 若 BIOS 顯示 `Press F1 to resume`：
   - 立即請使用者在實際視窗手動按 F1。
   - 不再嘗試 synthetic keyboard automation。
3. 確認 FreeDOS 啟動。
4. 從 `MEM /C` 畫面確認 EMS provider 與可用 EMS。
5. 確認 `FDAUTO.BAT` 執行 `KRONDOR.EXE`。
6. 等待 startup screen。
7. 取得包含兩組「鎖鏈」的完整畫面。
8. 取得 lossless closeup；只 crop，不 resize、不重新繪製。
9. 目視檢查 plane、palette、重影與 corruption。
10. 到此停止，不進 gameplay/Gate B。

若顯示 `partition signature != 55AA`，立即停止並重新比對實際掛載 image filename 與
static validation；不要改 CHS 猜測。

## 12. Runtime 產出檔名與格式

全部放在：

```text
scratchpad/evg-native-cjk-poc/
```

| 檔名 | 格式 | 內容 |
|---|---|---|
| `gate-a-disk-build.log` | UTF-8 plain text | 完整 builder stdout/stderr |
| `gate-a-disk-validation.json` | UTF-8 JSON | MBR/VBR/files/hash 靜態驗證 |
| `86box-gate-a.cfg.txt` | UTF-8 plain text | 實際使用的關鍵設定 |
| `gate-a-ems.png` | PNG | FreeDOS EMS 證據；若畫面來不及保留，可在報告解釋 |
| `gate-a-startup-full.png` | PNG | 實際遊戲 startup 完整畫面 |
| `gate-a-startup-closeup.png` | PNG, crop only | 兩組「鎖鏈」近照 |
| `gate-a-measurement.json` | UTF-8 JSON | screenshot 與 glyph 量測 |
| `gate-a-failure.png` | PNG | FAIL 時的實際錯誤畫面 |

### 12.1 gate-a-measurement.json 格式

```json
{
  "source_image": "gate-a-startup-full.png",
  "source_dimensions": [640, 400],
  "capture_kind": "raw framebuffer | 86Box window",
  "image_resized": false,
  "game_executed": true,
  "evg_mode_observed": true,
  "control": {
    "text": "鎖鏈",
    "expected_cell_physical": [32, 32],
    "observed_ink_bbox": [0, 0, 0, 0],
    "visible": true
  },
  "experimental": {
    "text": "鎖鏈",
    "expected_cell_physical": [16, 16],
    "observed_ink_bbox": [0, 0, 0, 0],
    "visible": true
  },
  "plane_corruption": false,
  "notes": []
}
```

若只能取得 86Box window screenshot，`source_dimensions` 必須填真實視窗圖尺寸，
`capture_kind` 填 `86Box window`；不得謊稱 640×400 raw framebuffer。量測時要扣除
整數顯示縮放，並清楚標為推算值。

## 13. 結果報告

建立：

```text
docs/research/evg-native-cjk-gate-a-recovery-result.md
```

固定格式：

```markdown
# EVG Native CJK Gate A Recovery Result

## Verdict

PASS | FAIL | BLOCKED_USER_INPUT

## What Was Fixed

說明舊 image 為何不可開機、新 image 如何建立。

## Static Validation

列出 size、geometry、MBR、partition、VBR、required files、embedded hashes。

## Runtime Environment

列出 86Box version、machine、CPU、RAM、Video 7 BIOS、VRAM、disk geometry。

## Runtime Evidence

說明 FreeDOS、EMS、KRONDOR execution、EVG startup 畫面。

## Glyph Observation

- Control 32×32:
- Experimental 16×16:
- Plane/palette/present problems:

## Acceptance Checklist

- [ ] valid bootable image
- [ ] EMS present
- [ ] KRONDOR.EXE executed
- [ ] EVG startup screen visible
- [ ] control glyph visible
- [ ] physical glyph visible
- [ ] no obvious framebuffer corruption
- [ ] screenshots and JSON exist

## Evidence

使用 repository-relative links。

## Next Decision

只選一項：

- GATE_A_PASS — 可以另開 Gate B 工作。
- GATE_A_FAIL — physical EVG primitive 本身需要除錯。
- BLOCKED_USER_INPUT — 只差使用者在 86Box 視窗按 F1；寫出精確操作。
```

## 14. 交付前檢查

```powershell
python -m json.tool scratchpad/evg-native-cjk-poc/gate-a-disk-validation.json
python -m json.tool scratchpad/evg-native-cjk-poc/gate-a-measurement.json
git diff --check
git -C upstream/betrayal-at-krondor diff --check
```

確認：

- production source diff 與開始本工作前完全相同。
- 沒有覆蓋 `krondor_evg.img`。
- 沒有建立新的 disk/input/focus automation scripts。
- 新 image 不是 sparse/all-zero image。
- 報告 hash 與 JSON、實體檔案一致。
- 沒有把 BIOS、FreeDOS 或 offline mock 截圖誤稱為遊戲 startup 成功。

Gate A 完成後停止，把結果交給主 Agent 判讀；不要自行開始 Gate B。
