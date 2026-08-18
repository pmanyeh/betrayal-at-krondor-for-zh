# ADR-001: 繁體中文文字編碼方案決策 (Chinese Text Encoding Scheme)

## 1. 決策背景 (Context)

在《Betrayal at Krondor》原版引擎中，文字處理全面採用單字節模型（`char far *`）。根據 [`docs/research/text-rendering-pipeline.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/research/text-rendering-pipeline.md) 之研究結論：
1. **控制碼保留區間：** [`FONT.C:218`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L218) 明確定義 `(c & 0xF0) == 0xE0 || (c & 0xF0) == 0xF0`（即 `0xE0..0xFF`）為字型樣式、前景色切換與 BOK 格式控制碼。
2. **字串結尾：** `0x00` 為 Null 結尾字元。
3. **語法標記：** `@`（發話者變數）、`#`（標題框標記）、`\n`（換行）、`\t`（縮排）。

繁體中文需支援數千漢字，必須引入雙字節編碼方案，同時**絕對不得與上述控制碼或既有語法發生位元組碰撞**。

---

## 2. 評估方案比較 (Options Evaluated)

### 方案 A：標準 Big5 編碼 (Standard Big5)
- **結構：** Lead byte `0x81..0xFE`，Trail byte `0x40..0x7E` / `0xA1..0xFE`。
- **缺點：** Lead byte `0xE0..0xFE` 與原版控制碼區間（`0xE0..0xFF`）產生**嚴重衝突**。引擎在遍歷字串時會將漢字首字節誤判為樣式重設或變色指令，造成文字繪製中斷或畫面混亂。
- **結論：** ❌ **否決 (REJECTED)**。

### 方案 B：自訂轉義碼 (Custom Escape Prefix)
- **結構：** `ESC (0x1B) <Glyph_ID_Hi> <Glyph_ID_Lo>`（3 bytes / 字）。
- **優點：** 與 ASCII 區間明確隔離。
- **缺點：** 每個中文字佔用 3 位元組，增加 50% 記憶體負擔與暫存區長度。
- **結論：** ❌ **否決 (REJECTED)**。

### 方案 C：緊湊雙字節遊戲編碼 (Compact 2-Byte Game Encoding) ★ 獲選方案
- **結構：**
  - **原始翻譯來源：** 標準 UTF-8 JSON（翻譯工具、編輯器與 Git 最佳體驗）。
  - **運行時遊戲編碼 (BAK-ZH Compact)：**
    - `0x00`: Null Terminator
    - `0x01`..`0x7F`: 原始 ASCII 字元（保留 `@`、`#`、`\n`、`\t` 等語法）
    - `0x80`..`0xDF`: **中文引導字節 (Lead Byte)**（共 96 個區段）
    - `0x20`..`0x7E` / `0x80`..`0xDF`: **中文跟隨字節 (Trail Byte)**（共 160 個有效值）
    - `0xE0`..`0xFF`: **原版控制碼保留區**（零衝突！）
- **容量上限：** 96 * 160 = **15,360 個字形**，遠超過繁中常用字庫需求（~6,000 字）。
- **結論：** ✅ **採納 (ACCEPTED)**。

---

## 3. 編碼位元組語法規格 (Byte Grammar Specification)

```text
[Byte Stream]
  ├── 0x00           -> String Terminator
  ├── 0x01 .. 0x7F   -> Single-byte ASCII (Width calculated from FNT:Slot 0)
  ├── 0x80 .. 0xDF   -> Chinese Lead Byte (Consume next byte as Trail Byte)
  │    └── Trail Byte:
  │         ├── 0x20 .. 0x7E -> Glyph ID = (Lead - 0x80) * 160 + (Trail - 0x20)
  │         └── 0x80 .. 0xDF -> Glyph ID = (Lead - 0x80) * 160 + 95 + (Trail - 0x80)
  └── 0xE0 .. 0xFF   -> Original Engine Control Code (Reset, Style, Color)
```

### 3.1 畸形位元組序列容錯 (Malformed Byte Handling)
- 若遇到 Lead Byte（`0x80..0xDF`）後緊接 `0x00`（結尾）或 `0xE0..0xFF`（控制碼）：
  - 判定為畸形序列，單獨略過或繪製空白，指針不跨越合法控制碼。

---

## 4. 測試向量 (Test Vectors)

| 測試類型 | 輸入字串 (UTF-8) | 編碼後位元組序列 (Hex) | 解碼 Glyph ID | 預期像素寬度 |
|---|---|---|---|---|
| 純英文 | `"Owyn"` | `4F 77 79 6E` | - (ASCII) | ~24 px |
| 單一漢字 | `"歐"` | `80 20` | Glyph #0 | 16 px |
| 混合文字 | `"Owyn: 歐文"` | `4F 77 79 6E 3A 20 80 20 80 21` | ASCII + #0, #1 | 24 + 4 + 16 + 16 px |
| 帶樣式控制碼 | `"\xF0\x01歐\xF0\x00"` | `F0 01 80 20 F0 00` | Ctrl + #0 + Ctrl | 16 px |
| 發話者 Token | `"@0: 我們"` | `40 30 3A 20 80 22 80 23` | Token + #2, #3 | Token 展開後計算 |
