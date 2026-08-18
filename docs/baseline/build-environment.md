# Betrayal at Krondor — Build Environment & Toolchain Analysis (Phase 0)

## 1. 上游構建架構分析 (Upstream Build Architecture)

依據 `canassa/betrayal-at-krondor`（Commit `1fc2a69`）之設計，原版《Betrayal at Krondor》是透過 1993 年代的 Borland C++ 與 TASM 工具鏈編譯而成。上游專案為了達成 **100% Byte-perfect** 的還原，採用了多編譯器與虛擬機器分流構建架構：

```text
Host (Python CLI: uv run bak build)
  │
  ├─► FreeDOS Disk Image (FAT16 base.img via mtools)
  │     ├─ C:\BC\BIN   (Borland C++ 3.1 & TASM & TLINK)
  │     ├─ C:\BC30     (Borland C++ 3.0)
  │     ├─ C:\BC20     (Borland C++ 2.0 / BCCX protected mode)
  │     └─ C:\EXIT.COM (QEMU isa-debug-exit utility)
  │
  ├─► Pass 1: QEMU KVM Accelerator (Linux /dev/kvm)
  │     └─ 編譯 ~213 個 BCC 3.1 + TASM 目標檔案 (kvmobjs)
  │
  ├─► Pass 2: QEMU TCG Accelerator (-accel tcg -cpu 486)
  │     └─ 編譯 ~18 個 BCC 2.0 (BCCX) + 3.0 目標檔案 (tcgobjs via real-mode MAKER)
  │
  └─► Pass 3: QEMU KVM Accelerator + Clock Pinning
        ├─ 鎖定 RTC 1993-06-16 (1.00) 或 1994-03-21 (1.02)
        └─ TLINK @KRONDOR.RSP / @KRN102.RSP 產生 byte-identical KRONDOR.EXE
```

### 關鍵技術約束
1. **BCC 2.0 Protected-Mode 限制：**
   - BCC 2.0 使用 A.I. Architects 286 extender，採用 286 任務切換（Task Switch）進入保護模式。
   - QEMU-KVM 無法虛擬化此行為（會觸發 General Protection Fault `#GP`），必須使用 QEMU-TCG 軟體模擬。
2. **TASM under TCG 限制：**
   - TASM 在 QEMU-TCG 下無法正常產出 `.OBJ`，因此 TASM 與 BCC 3.1 必須在 KVM 下執行。
3. **時間戳記（RTC）要求：**
   - Borland TLINK 會在執行檔末端的 `OVRINFO` 區塊寫入系統日期時間。
   - 1.00 需鎖定至 `1993-06-16T12:00:00`，1.02 需鎖定至 `1994-03-21T12:00:00`。

---

## 2. 本機環境盤點 (Host Environment Inventory)

| 元件 / 工具 | 本機現狀 | 版本 / 路徑 | 狀態評估 |
|---|---|---|---|
| **作業系統** | Windows 11 x64 | Windows NT Kernel | Host OS |
| **Git** | 已安裝 | `C:\Users\pmany\AppData\Local\Programs\Git\cmd\git.exe` | 正常 |
| **Python** | 已安裝 | Python 3.12.10 (`C:\Users\pmany\AppData\Local\Programs\Python\Python312\python.exe`) | 正常 |
| **DOSBox-X** | 已安裝 | DOSBox-X 2026.06.02 (`D:\ghidra_re\dosbox\bin\x64\Release\dosbox-x.exe`) | 正常 (可用於 Runtime 測試) |
| **uv** | 未安裝至 PATH | - | 構建自動化依賴 |
| **QEMU (i386)** | 未安裝至 PATH | - | Upstream 預設構建依賴 |
| **mtools** | 未安裝至 PATH | - | Upstream 映像檔讀寫依賴 |
| **WSL2** | 系統支援未啟用 | 需要 `wsl --install` | 建議用於 Linux 原生構建 |

---

## 3. Windows 環境構建分析與落實途徑 (Build Reproduction Options)

上游原生 `cli/src/bakbuild` 使用了 POSIX 專屬的 `fcntl.flock` 以及依賴 Linux `/dev/kvm` 加速。在 Windows 環境下，有以下三種途徑重現與執行編譯：

### 途徑 A：WSL2 (Ubuntu) + KVM 途徑（最完整相容）
- **方式：** 在 Windows 啟用 WSL2，安裝 Ubuntu，啟用巢狀虛擬化（Nested Virtualization / KVM），安裝 `uv`, `qemu-system-x86`, `mtools`。
- **優點：** 100% 走通上游的原生 `uv run bak build` 與 byte-matching 驗證。

### 途徑 B：DOSBox-X 原生 Batch Build 途徑（中文化開發首選）
- **方式：** 將 Borland C++ 3.1 / TASM / TLINK 工具鏈配置於 DOSBox-X 掛載目錄中，使用標準 DOS `MAKE.EXE` 進行批次編譯與連結。
- **優點：** 不需要 Linux/KVM/QEMU，完全在 Windows + DOSBox-X 環境內閉環開發與調試。
- **適用階段：** Phase 4 中文 POC 與 Phase 5 引擎修改的主力工作流。

### 途徑 C：Python CLI 跨平台適配（TCG / 磁碟映像直接操作）
- **方式：** 移除 `fcntl` 依賴，使用 Python `fat16` 模組或 Windows QEMU-TCG 驅動。

---

## 4. 結論

本專案現已完整掌握上游構建邏輯與工具鏈技術細節。現行環境具備完整的 Python 3.12、Git 與 DOSBox-X 執行除錯環境，為後續中文化研發與測試奠定堅實基礎。
