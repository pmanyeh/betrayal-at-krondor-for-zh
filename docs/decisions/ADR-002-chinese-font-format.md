# ADR-002: 繁體中文字型架構與檔案格式 (Chinese Font Format: `ZH16.DAT`)

## 1. 決策背景 (Context)

原版《Betrayal at Krondor》使用 `.FNT` 格式字型，內部以 1 個 byte 的 `pFont_glyph_count` 儲存字形數量（最大 256 個）。

由於繁體中文常用字需約 3,000 至 6,000 個字形，若將其強行寫入原版 `.FNT`，將面臨：
1. 8 位元計數器溢位。
2. 破壞原版 20 個字型 Slot 的資料結構佈局。
3. 破壞原版 ASCII 字型樣式與 UI 比例。

因此，本專案決定設計**獨立外掛中文字型格式 `ZH16.DAT`**。

---

## 2. `ZH16.DAT` 二進位結構規格 (Binary Specification)

### 2.1 檔案標頭 (Header, 16 Bytes)
```c
struct ZhFontHeader {
    char szMagic[4];             // 0x00: "ZHFN" (固定識別魔術字元)
    unsigned short wVersion;     // 0x04: 1 (格式版本)
    unsigned char bGlyphWidth;   // 0x06: 16 (點陣字寬，像素)
    unsigned char bGlyphHeight;  // 0x07: 16 (點陣字高，像素)
    unsigned short wGlyphCount;  // 0x08: 總收錄漢字數量 (N)
    unsigned char bBaseLead;     // 0x0A: 0x80 (引導字節起始碼)
    unsigned char bPad[5];       // 0x0B: 保留對齊位元組 (填 0)
};
```

### 2.2 點陣資料區 (Bitmap Data Array)
- 每個字形採用 **16x16 單色 1-bit 點陣**（Monochrome Bitmap）：
  - 每列 16 像素 = 2 位元組（16 bits，MSB 在左）。
  - 16 列 = 32 位元組 / 字形。
- 資料區總長度：`wGlyphCount * 32` 位元組。
- 字形記憶體偏移計算公式：
  `glyph_offset = 16 + (glyph_id * 32)`

---

## 3. DOS 記憶體管理與載入策略 (DOS Memory Allocation)

### 3.1 記憶體佔用評估
| 字庫階段 | 收錄字數 | 檔案與記憶體大小 | 評估 |
|---|---|---|---|
| **Phase 4 POC** | 50 字 | 16 B + 1,600 B ≈ **1.6 KB** | 極小，任何模式均無壓力 |
| **章節小說版** | 1,500 字 | 16 B + 48,000 B ≈ **48 KB** | 遠小於單一 64KB 段 |
| **全遊戲完整版** | 6,000 字 | 16 B + 192,000 B ≈ **192 KB** | 透過 `alloc_far` 分配 Far Heap |

### 3.2 載入方式
- 在遊戲啟動階段（[`BOOT.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SYS/BOOT.C) 或 `font_init`）由 `res_fopen("ZH16.DAT", "rb")` 讀取。
- 調用 `alloc_far(file_size, 0)` 分配常駐 Far Pointer `unsigned char far *g_pZhFontBitmap;`。
- 若 `ZH16.DAT` 不存在，引擎優雅降級為純英文模式。

---

## 4. Phase 4 POC 最小測試字表 (POC Minimal Glyph Set)

POC 階段精選 50 個代表性漢字：

```text
歐 文 我 們 在 哪 裡 克 朗 多 洛 爾 戈 拉 斯 塔
主 選 單 開 始 繼 續 設 定 離 庫 存 裝 備 觀 察
金 幣 隊 伍 戰 鬥 攻 擊 防 禦 魔 法 逃 跑 投 降
道 具 說 明 是 否
```

此 50 字覆蓋：
- 主要主角名稱（歐文、洛克爾、戈拉斯、克朗多）。
- 基礎系統詞彙（主選單、開始、存檔、金幣、戰鬥、是/否）。
- POC 驗證對話句（`歐文：我們在哪裡？`）。
