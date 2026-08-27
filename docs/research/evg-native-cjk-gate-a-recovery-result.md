# EVG Native CJK Gate A Recovery Result

## Verdict

**BLOCKED_USER_INPUT**

硬碟映像檔開機磁區損壞問題已完全修復。新的標準映像檔 `krondor_evg_gate_a.img` 已通過 100% 嚴格靜態驗證（MBR/VBR/分區表/檔案完整性/SHA256 雜湊完全相符）。目前因背景代理程式執行環境（Windows Session 隔離）無法在使用者桌面直接顯示 GUI 視窗並自動傳送 BIOS POST 按鍵，因此停留在等待使用者於本機開啟 86Box 並按下 `F1` 繼續開機。

## What Was Fixed

1. **舊 Image 失敗根因**:
   - `scratchpad/evg-native-cjk-poc/vm/krondor_evg.img` 原先因 `tools/build_type17_disk.py` 在執行 `sfdisk` 與 `mformat` 時參數錯誤且忽略失敗回傳值，導致產出之 MBR、分區表及 LBA 17 VBR 全為零（全零損壞磁區）。
2. **新 Image 建立方式**:
   - 修正並使用標準建置工具 `tools/build_clean_freedos_disk.py`。
   - 直接複製已驗證可開機之 FreeDOS base image（`/home/pmanyeh/bak-toolchain/freedos/freedos.img`，33,554,432 bytes）。
   - 透過 mtools offset `@@32256` 移除不需要之套件以釋放空間，保留 `\FREEDOS\BIN` 與系統核心。
   - 寫入支援 EMS 之 `FDCONFIG.SYS`（載入 HIMEMX 與 JEMM386）與 `FDAUTO.BAT`（執行 `MEM /C` 並自動呼叫 `KRONDOR.EXE`）。
   - 複製遊戲資料及 4 個指定 POC 二進位檔案。
   - 新輸出映像檔命名為 `scratchpad/evg-native-cjk-poc/vm/krondor_evg_gate_a.img`，不覆蓋舊壞檔。

## Static Validation

依據 `scratchpad/evg-native-cjk-poc/gate-a-disk-validation.json` 驗證結果：

- **Size**: `33,554,432` bytes (32 MiB)
- **Geometry**: 65 Cylinders, 16 Heads, 63 Sectors
- **MBR**:
  - Signature: `55aa`
  - Partition 1 Active: `True` (0x80)
  - Partition Type: `0x04` (FAT16 <32M)
  - Start LBA: `63`
- **VBR**:
  - LBA 63 Signature: `55aa`
  - Jump Byte: `0xeb` (Valid)
- **Required Files**:
  - `KERNEL.SYS`: Present
  - `FDCONFIG.SYS`: Present (包含 `HIMEMX.EXE` 與 `JEMM386.EXE`)
  - `FDAUTO.BAT`: Present (包含 `KRONDOR.EXE`)
  - `KRONDOR.EXE`: Present
  - `VMCODE.OVL`: Present
  - `SX.OVL`: Present
  - `ZH16.DAT`: Present
  - `STARTUP.GAM`: Present
- **Embedded SHA-256 Hashes**:
  - `KRONDOR.EXE`: `4b71c99013732ed63561680689d7483325f498a7e2268dbdff8f0b59d6ff57ac` (MATCH)
  - `VMCODE.OVL`: `a1d138e069553fc45c235a3647009602fa5e5d07ed7e4482ceeba5c542f64e1a` (MATCH)
  - `SX.OVL`: `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb` (MATCH)
  - `ZH16.DAT`: `0a36619ba5dc257da820147ba38bcddedc3aa6686b8ddfe45037cb851420598d` (MATCH)

## Runtime Environment

- **Emulator**: 86Box 6.0 [build 9001]
- **Machine**: Award SiS 495 (`award495`)
- **CPU**: i486DX 33MHz
- **RAM**: 4096 KB (4 MB)
- **Video Device**: Video 7 VGA 1024i (HT208)
- **Video BIOS**: Video 7 VGA 1024i BIOS v2.19 (Headland Technology Inc.)
- **Video RAM**: 512 KB
- **Disk Configuration**: `hdd_01_parameters = 63, 16, 65, 0, ide` (檔案: `krondor_evg_gate_a.img`)

## Runtime Evidence

- 待使用者於桌面執行 86Box 並按下 F1 進入開機流程後截圖補齊。

## Glyph Observation

- **Control 32×32**: 待執行截圖量測
- **Experimental 16×16**: 待執行截圖量測
- **Plane/palette/present problems**: 待執行截圖觀察

## Acceptance Checklist

- [x] valid bootable image
- [x] EMS present in configuration
- [ ] KRONDOR.EXE executed
- [ ] EVG startup screen visible
- [ ] control glyph visible
- [ ] physical glyph visible
- [ ] no obvious framebuffer corruption
- [x] validation JSON and configuration exist

## Evidence

- [gate-a-disk-validation.json](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/gate-a-disk-validation.json)
- [gate-a-disk-build.log](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/gate-a-disk-build.log)
- [86box-gate-a.cfg.txt](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/86box-gate-a.cfg.txt)
- [gate-a-measurement.json](file:///d:/git/betrayal-at-krondor-for-zh/scratchpad/evg-native-cjk-poc/gate-a-measurement.json)

## Next Decision

**BLOCKED_USER_INPUT**

**精確操作步驟**:
1. 請在您的 Windows 檔案總管或終端機中執行：
   ```cmd
   d:\git\betrayal-at-krondor-for-zh\scratchpad\evg-native-cjk-poc\run_86box.bat
   ```
2. 86Box 視窗開啟後，請點選視窗並按下鍵盤 **`F1`** 鍵。
3. 系統將引導 FreeDOS 並自動啟動 `KRONDOR.EXE` 進入 Startup 畫面。
4. 按下 86Box 工具列上的相機按鈕（或截圖鍵）儲存截圖，即可驗證 Gate A 成功。
