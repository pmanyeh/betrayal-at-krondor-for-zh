# Phase 5 Redo: Source-Level Chinese Rendering via the Real Borland Toolchain

## 1. 背景 (Background)

先前 Phase 5 採用「反組譯猜位址 + 手刻 x86 binary patch」的方式修改 `KRONDOR.EXE`，
在 DOSBox-X 實測時造成 CPU 卡死在除法溢位無窮迴圈（黑畫面、不閃退）。追查後確認：

1. 補丁的位址從未在真正執行時的記憶體中驗證過，`font_text_pixel_width`
   （折行寬度計算）也從未同步修改，只改了 `font_draw_text_far`（繪圖）。
2. 已回滾至 `phase4: verify first chinese rendering poc`（commit `5f1149c`）。

調查過程中發現 `upstream/betrayal-at-krondor`（本地 clone）已有一個本地 commit
`2dcb2b0 feat(font): add chinese 16x16 glyph rendering and text wrapping support`，
直接在還原後的 C 原始碼（`FONT.C` / `TEXTWRAP.C`）中正確實作了雙位元組中文邏輯
（`font_draw_zh_glyph`、`font_init_chinese`，且 `font_draw_text_far` 與
`font_text_pixel_width` 都同步處理 `0x80-0xDF` 前導位元組）。本次 Phase 5 重做，
改為**直接用原廠 1993 年 Borland C++ 工具鏈編譯這份原始碼**，完全避開手刻二進位
補丁的位址風險。

## 2. 建置環境 (Build Environment)

- WSL2 + Ubuntu（`wsl --install`，需管理員權限 + 重開機，使用者手動完成）。
- WSL2 內安裝：`qemu-system-x86`（提供 `qemu-system-i386`，KVM 加速）、`mtools`、`uv`。
- 使用者需被加入 `kvm` 群組（`usermod -aG kvm <user>`）才能存取 `/dev/kvm`；
  未加入時 KVM-accelerated boot 會靜默失敗、不產生任何 log（無 log 卻回報
  `KRONDOR.EXE / VMCODE.OVL / SX.OVL: not produced`，需特別注意這個症狀）。
- 週邊工具鏈（Borland C++ 3.1 / 3.0 / 2.0 + TASM + FreeDOS 開機映像）從專案自己的
  GitHub Release 取得並雜湊驗證：
  `https://github.com/canassa/betrayal-at-krondor/releases/download/toolchain-v1/toolchain.tar.gz`
  （SHA-256 `99c83ad0...dc8dfb`，與 `flake.nix` 記錄的 pin 完全相符）。
- **建置必須在 WSL 原生 Linux 檔案系統上執行**（例如 `~/krondor-build`），不可直接在
  `/mnt/d/...`（Windows 掛載磁碟機）上跑 `uv sync` 或 `git clone --local`：
  DrvFs 對檔案的 `utime`/硬連結操作會回報 `Operation not permitted` /
  `Invalid cross-device link`。做法：`git clone --local --no-hardlinks` 複製一份到
  WSL home 目錄後再建置，完成後把 `work/KRONDOR.EXE` 等產物複製回 Windows 端。

## 3. 建置結果 (Build Result)

```
uv run bak build --clean
```

- `VMCODE.OVL`：**BYTE-IDENTICAL**（44582 bytes，sha256 `cd0cf73d...56237e0`）
- `SX.OVL`：**BYTE-IDENTICAL**（40742 bytes，sha256 `d73d92d8...4dabdb`）
- `KRONDOR.EXE`：454704 bytes（原版 453904 bytes，多 800 bytes）——**預期中的差異**，
  因為原始碼確實多了中文渲染邏輯；兩個 `.OVL` 完全比對相符已足以證明工具鏈與流程正確。

兩個 `.OVL` byte-identical 是關鍵證據：證明 WSL2 + QEMU-KVM + 原廠工具鏈的整條建置
管線完全正確，`KRONDOR.EXE` 的差異可歸因於刻意的原始碼修改，而非建置環境問題。

## 4. 實機驗證 (Live Verification in DOSBox-X)

- 測試環境：獨立複製 `betrayal-at-krondor/` 至 `dist/test_v100_zh/`（**不覆寫使用者
  原始遊戲資料**），替換 `krondor.exe` / `vmcode.ovl` / `sx.ovl` 為新編譯產物，放入
  `ZH16.DAT` 及一份修改過的 `DIAL_Z16.DDX`。
- 修改對象：`DIAL_Z16.DDX` node `1600003`（原文
  `"...Gorath leapt forward, his chains writhing between his wrists like metallic vipers."`），
  這是 Chapter 1 開場埋伏戰鬥前置對話，**每次遊戲流程都必經、極容易穩定觸發**，
  比原本 Phase 4 選定的岔路對話（node `100009`）更適合作即時驗證。
- 修改方式：`tools/text/ddx_extract.py` / `ddx_pack.py` 正常 extract→edit→pack；
  中文替換文字刻意 padding 到與原文**完全相同的 byte 長度**，避免變更任何後續 record
  的 offset（DDX 內部 opcode 可能以絕對 offset 定址，長度不同會導致封裝後的檔案
  在別的地方跳轉錯誤——實測中曾因為省略 padding 而觀察到播放流程跳過被修改的
  record）。
- 結果：DOSBox-X 實機執行新編譯的 `KRONDOR.EXE`，於埋伏戰鬥開場正確顯示
  「戈拉斯攻擊」四個繁體中文字，英文文字全程正常，無當機、無記憶體錯亂。

## 5. 字型 (Font)

`ZH16.DAT` 目前由 `tools/font/build_font.py` 的 `render_glyph_from_ttf()`
使用 Windows 內建「微軟正黑體」（`msjh.ttc`）點陣化產生（16x15 視窗，
size=15pt，經驗值 crop offset y=3 可穩定置中筆劃）。這是**現代 UI 字體**風格，
非 1993 年代點陣字美術；曾嘗試尋找倚天（ETen）點陣字作為更具時代感的替代來源，
但手邊 `D:\git\Fonts` 內的 `stdfont.15`（實為文字檔）與 `ET353S.iso`（毀損，
7z/Windows 皆無法開啟）皆不可用。若日後取得完整可用的倚天點陣字庫，
可比照 `u5-cht` 專案（另一個繁中化專案）的 `tools/build_eten_font.py` 做法
（Big5 線性索引公式 + oracle 驗證）重新產生更道地的 `ZH16.DAT`。

## 6. 結論 (Conclusion)

M4 里程碑（「原 DOS Krondor 顯示第一句繁體中文」）達成，且是透過**正確、可重現、
無需手刻機器碼**的路徑達成：C 原始碼修改 → 原廠工具鏈編譯 → 二進位比對驗證 →
DOSBox-X 實機顯示驗證。相較於先前的二進位補丁方案，此方案完全消除了位址猜測與
手動組語帶來的風險類別。
