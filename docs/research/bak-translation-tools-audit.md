# Audit of bak-translation-tools (Phase 2A)

## 1. 概述 (Overview)

`old-games/bak-translation-tools`（https://github.com/old-games/bak-translation-tools，原由 Andrey Fedoseev 開發，後由 Old-Games.RU 社群維護）是社群為進行《Betrayal at Krondor》俄語中文化所開發的 Python 工具集。

本文件旨在審查其架構、各子模組能力與限制，以供繁體中文化專案評估與借鏡。

---

## 2. 模組功能審查矩陣 (Feature Audit Matrix)

| 模組 / 工具 | 支援格式 | 功能說明 | 繁中專案適用性評估 |
|---|---|---|---|
| **Resource Manager** | `KRONDOR.001` / `KRONDOR.RMF` | 解包與打包主遊戲資源庫，支援 CRC/雜湊計算與項目替換。 | **高**。可作為封裝發行 Patch 的資產管理依據。 |
| **Font Editor (GUI)** | `.FNT` | Tkinter 基礎的 256 字元點陣字型編輯器，支援單字節字元繪製與寬度調整。 | **部分適用**。僅支援單一 256 字元 FNT，不支援數千繁中漢字庫（需自訂多字節字型格式）。 |
| **Book Extractor / Packer** | `.BOK` | 解析書籍頁面、排版標記與純文字流，匯出與匯入章節小說文本。 | **高**。可作為 BOK 翻譯管線（Phase 7）之基礎。 |
| **Image Extractor / Packer** | `.BMX`, `.SCX`, `.PAL` | 圖片、立繪、背景圖與調色盤轉換（BMP/PNG 互轉）。 | **中**。可用於後續 UI 圖形中文化（Phase 8）。 |
| **DDX Dialog Tool** | `.DDX` | 原專案早期未提供完整的獨立 CLI 結構化 DDX 工具，或與俄語單字節編碼緊密綁定。 | **已由本專案自主開發**。本專案已實作標準 `ddx_extract.py` 與 `ddx_pack.py`。 |

---

## 3. 關鍵發現與技術邊界 (Key Findings)

1. **單字節語言設計限制 (Single-Byte Encoding Assumption)：**
   - `bak-translation-tools` 主要針對俄語（西里爾字母，CP866 或自訂 256 字元代碼頁）設計。
   - 俄語只需將原版 `.FNT` 中不常用的 ASCII 擴展字元（128-255）替換為西里爾字母即可顯示。
   - **繁體中文需要數千個漢字，不可能透過單純替換 256 字元 FNT 實現**，必須仰賴本專案設計之擴充中文字型架構（`ZH16.DAT`）與雙字節編碼。
2. **DDX 工具之獨立性：**
   - 本專案自主實作之 `tools/text/ddx_extract.py` 與 `tools/text/ddx_pack.py` 已經達成全遊戲 29 個 DDX 檔案 100% Byte-Identical Round-Trip，且完美處理所有子節點（Child records）與分支指針（`nA3`），完全可自給自足，不依賴外部第三方工具。
