# Betrayal at Krondor — Text Rendering Pipeline & Architecture (Phase 1)

## 1. 綜述 (Executive Summary)

本文件依據 [`Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`](file:///d:/git/betrayal-at-krondor-for-zh/Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md) 第 7 節之規範，針對 `upstream/betrayal-at-krondor/bak/SRC/` 內所有文字呈現相關原始碼進行深度探勘。

本專案確認：
1. **統一字型底層 (Universal Font Core)：** 全遊戲所有文字輸出（包括 DDX 對話、BOK 書籍、UI 元件、物品欄、地圖標籤、謎題與系統訊息）最終均收斂至 [`FONT.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C) 的 `font_render_glyph_or_ctrl` 與 `font_draw_char`。
2. **單字節模型假設證實 (Single-Byte Model Verified)：** 現有引擎全面假設字元為單一字節（`char far *`、`pos++`、`idx = (unsigned char)*str - base_char`），單一 `.FNT` 最大支援 256 個字形。
3. **控制碼與高位元衝突確認 (Control Code Range Verified)：** `0xE0` ~ `0xEF` 與 `0xF0` ~ `0xFF` 被保留為樣式切換、顏色變更與 BOK 格式控制碼，**禁止繁中編碼直接使用這些高位元組**。

---

## 2. 端到端文字渲染管線 (End-to-End Pipeline)

```text
┌────────────────────────────────────────────────────────┐
│ 1. Resource Stage (DDX / BOK / UI String)              │
│    DIAL_Zxx.DDX (DDXRecord + DdxOp + Text Body)        │
│    Autoritative Source: SRC/DIALOG/DIALOG.C:100        │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Parser & Token Expansion                            │
│    - Title parse: '#...#'                              │
│    - Speaker token: '@0'..'5' -> g_pMainScratchBuf     │
│    Autoritative Source: SRC/DIALOG/DIALOG.C:551        │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Line Wrapping (Textwrap)                            │
│    - textwrap_compute_lines                            │
│    - Whitespace breakpoint backtrack                   │
│    - '\n' explicit break                               │
│    Autoritative Source: SRC/UI/TEXTWRAP.C:36           │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Width & Advance Calculation                         │
│    - font_text_pixel_width                             │
│    - font_glyph_metrics (w/h lookup)                   │
│    Autoritative Source: SRC/GFX/FONT/FONT.C:82, 322    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 5. Font Dispatcher & Control Handler                   │
│    - font_draw_text_far                                │
│    - font_render_glyph_or_ctrl (0xE0/0xF0 trap)        │
│    Autoritative Source: SRC/GFX/FONT/FONT.C:207, 302   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 6. Glyph Rasterization & Framebuffer Blit              │
│    - font_draw_char (monochrome / multicolor / clip)   │
│    - g_pfn_blit_glyph_row (ASM fast blit)              │
│    - putpixel / Framebuffer Write                      │
│    Autoritative Source: SRC/GFX/FONT/FONT.C:99, 274    │
└────────────────────────────────────────────────────────┘
```

---

## 3. 關鍵機制 14 項權威證據 (14 Invariant Analyses)

### 3.1 字串結尾判定 (String Termination)
- **原始碼證據：**
  - [`SRC/GFX/FONT/FONT.C:88`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L88)：`while (*str != '\0')`
  - [`SRC/GFX/FONT/FONT.C:306`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L306)：`while (*text != '\0')`
  - [`SRC/UI/TEXTWRAP.C:49`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L49)：`while (count < max_lines && CH(line_start) != '\0')`
- **行為特性：** 標準 C Null-terminated (`0x00`)。在折行繪製時，[`TEXTWRAP.C:138`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L138) 會暫時將 `lines[fl].end` 處寫入 `\0` 傳入 `font_draw_text_far`，繪畢後還原原字元。

### 3.2 字元符號性 (Char Signed/Unsigned Behavior)
- **原始碼證據：**
  - [`SRC/GFX/FONT/FONT.C:89`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L89)：`idx = (unsigned char)*str - g_graphics_context.pFont_base_char[0];`
  - [`SRC/GFX/FONT/FONT.C:216`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L216)：`c = (unsigned char)ch; hi = c & 0xf0;`
- **行為特性：** 在取字元時均顯式轉型為 `(unsigned char)`，避免了 8-bit 大於 127 的字元符號擴展為負數的問題。

### 3.3 字形查找機制 (Glyph Lookup)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:119-131`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L119-L131)
- **格式分類：**
  1. **Format 1 / 3 (Proportional Packed Monochrome):**
     `width = g_font_width_table[0][i];`  
     `glyph_ptr = g_font_bitmap_data[0] + g_font_glyph_offset_table[0][i];`
  2. **Format 2 (Multi-color byte-per-pixel):**
     `glyph_ptr = g_font_bitmap_data[0] + i * width * height;`
  3. **Format 0 (Fixed-width Monochrome):**
     `glyph_ptr = g_font_bitmap_data[0] + i * ((width + 7) >> 3) * height;`

### 3.4 字形度量 (Glyph Metrics)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:322-353`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L322-L353)
- **計算公式：**
  - 字高：`g_graphics_context.pFont_height[0]`
  - 字寬：`g_font_width_table[0][ch]`（比例字型）或 `pFont_glyph_width_bits[0]`（等寬字型）
  - Tab 寬度：`g_nTabWidth`（當 `ch == 9`）

### 3.5 文字像素寬度計算 (Width Computation)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:82-97`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L82-L97)
- **行為特性：** 單字節逐一累加寬度。當遇到控制碼（不在 `[0, glyph_count)` 內）時，回傳寬度為 0 且指針前進 1 位元組。

### 3.6 折行演算法 (Line Wrapping)
- **原始碼證據：** [`SRC/UI/TEXTWRAP.C:14-89`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L14-L89)
- **行為特性：**
  - 折行斷點：以空白 `' '` 或省略號 `...` 後接字母為合法斷行處。
  - 當行累加像素超過 `max_width` 時，回溯至前一個空白斷點；若該行無任何斷點則強制切斷單詞。
  - 下一行自動跳過前導空白：`while (CH(line_start) == ' ') line_start++;`。

### 3.7 對齊邏輯 (Alignment)
- **原始碼證據：** [`SRC/UI/TEXTWRAP.C:127-144`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L127-L144)
- **對齊標記：**
  - 水平置中：`flags & 2`，`hoff = (max_width - line_width) / 2`
  - 水平靠右：`flags & 4`，`hoff = max_width - line_width`
  - 垂直置中：`flags & 0x10`，`voff = (max_height - total_height) / 2`
  - 垂直靠底：`flags & 0x20`，`voff = max_height - total_height`

### 3.8 控制碼語法與範圍 (Control Codes)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:217-257`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L217-L257)
- **觸發範圍：** `(c & 0xF0) == 0xE0 || (c & 0xF0) == 0xF0`（即 `0xE0..0xEF` 與 `0xF0..0xFF`）。
- **指令功能：**
  - `0xF0` / `0xE0`: 重設文字樣式與前景色至預設值。
  - `0xF1` / `0xE1` / `0xF2` / `0xE2`: 切換斜體/高亮（`bText_style_flags = 5`）。
  - `0xF4` / `0xF5`: 切換特定調色盤顏色索引。
- **空白重設機制：** [`FONT.C:307`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L307) 在繪製每個空白字元 `' '` 時，會自動調用 `font_render_glyph_or_ctrl(-0x10, 0, 0)`（即 `0xF0` 重設樣式）。

### 3.9 樣式與色彩系統 (Style & Colors)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:146-198`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L146-L198)
- **`bText_style_flags` 位元定義：**
  - `& 1`: 關閉底線/描邊（0 為描繪底線）
  - `& 2`: 粗體（Bold，在 `x+1` 重複繪製，字寬 +1）
  - `& 4`: 斜體（Italic，每 3 列遞減 x）
  - `& 8`: 底線（Underline，在 `underline_offset + 2` 畫線）
  - `& 0x10`: 網點/半透明（Dither，棋盤格繪製）

### 3.10 裁剪與邊界保護 (Clipping)
- **原始碼證據：** [`SRC/GFX/FONT/FONT.C:133-140`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L133-L140)
- **機制：** 當字形超出 `clip.xmin..clip.xmax, clip.ymin..clip.ymax` 時，切換至帶有邊界判定的通用 `putpixel`；若在視窗內且符合條件，則調用快速組合語言 `g_pfn_blit_glyph_row`。

### 3.11 記憶體模型約束 (Memory Model & Far Pointers)
- **編譯器模型：** Borland C++ Medium Model（Code 為 Far，Data 預設為 Near，跨 Segment 資料顯式標記 `far` / `huge`）。
- **跨段指標：** 文字緩衝區與資產指標均為 `char far *` 或 `char huge *`，偏移計算時必須注意 16 位元 Segment 溢位保護。

### 3.12 緩衝區容量限制 (Buffer Sizes)
- **行數上限：** [`SRC/UI/TEXTWRAP.C:97`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L97) `struct textline lines[90];`，單次折行最多支援 90 行。
- **對話標題暫存區：** `char buf[50];`
- **發話者名稱長度：** `char g_speaker_names[6][32];`

### 3.13 DDX 對話調用鏈 (DDX Call Path)
```text
dialog_play_record (SRC/DIALOG/DIALOG.C:840)
  │
  ├─► dialog_load_record_by_key (DIALOG.C:100) -> 讀取 DIAL_Zxx.DDX
  │
  └─► dialog_render_text_with_tokens (DIALOG.C:551)
        │
        ├─► 展開 @0..@5 發話者名稱至 g_pMainScratchBuf
        ├─► textwrap_draw_aligned (TEXTWRAP.C:95)
        │     ├─► textwrap_compute_lines (TEXTWRAP.C:36)
        │     └─► font_draw_text_far (FONT.C:302)
        │           └─► font_render_glyph_or_ctrl (FONT.C:207)
```

### 3.14 BOK 書籍系統渲染共用性 (BOK System Integration)
- **原始碼證據：**
  - [`SRC/SCREENS/BOOKTEXT.C:177`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/BOOKTEXT.C#L177)：`font_render_glyph_or_ctrl(ch, x, y + g_pBookViewer->nBaselineYOff);`
  - [`SRC/SCREENS/BOOKTEXT.C:178`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/BOOKTEXT.C#L178)：`font_glyph_metrics(ch, &width, &height);`
  - [`SRC/SCREENS/BOOKTEXT.C:53`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/SCREENS/BOOKTEXT.C#L53)：`font_activate(g_pBookViewer->pFontSlots[slot]);`
- **結論：** BOK 書籍系統具備獨立的段落兩端對齊（Justify）與圖片繞排佈局計算，**但在字形繪製與寬度度量底層，100% 共用 `FONT.C`**。

---

## 4. 中文化架構設計關鍵發現 (Implications for Chinese Localization)

1. **不可直接套用 Big5 原碼：**
   - Big5 首字節範圍為 `0x81` ~ `0xFE`，尾字節為 `0x40` ~ `0x7E` 及 `0xA1` ~ `0xFE`。
   - 當中文字節落入 `0xE0` ~ `0xFF` 時，會直接被 [`FONT.C:218`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C#L218) 誤判為顏色或樣式控制碼，導致文字消失、調色盤亂跳或死鎖。
2. **折行機制必須支援中文字無空白斷行 (Char Wrapping)：**
   - 原版 [`TEXTWRAP.C:19`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C#L19) 只在遇到 `' '` 空白時斷行。中文連續排版無空格，若不擴充斷行規則，整句中文會被視為單一巨大單詞而被截斷。
3. **寬度計算與字串疊代器必須感知雙字節 (Double-byte Awareness)：**
   - `font_text_pixel_width` 與 `font_draw_text_far` 必須在遇到中文引導字節（Lead byte）時一次前進 2 位元組，並依據中文字型度量回傳正確像素寬度（如 12px 或 16px）。
4. **修改範圍高度集中：**
   - 核心修改點僅需聚焦於 [`FONT.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/GFX/FONT/FONT.C) 與 [`TEXTWRAP.C`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/SRC/UI/TEXTWRAP.C)，即可同時賦予 DDX 對話、BOK 書籍、UI 元件與遊戲全系統完整的繁中支援能力。
