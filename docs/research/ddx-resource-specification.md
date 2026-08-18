# DDX & BOK Dialog/Book Resource Specification (Phase 2)

## 1. DDX 對話資源二進位結構 (DDX File Binary Specification)

`DIAL_Zxx.DDX` 檔案儲存於 `KRONDOR.001` 內部，其命名規則對應各章節：`chapter = node_id / 100000`，如第一章為 `DIAL_Z01.DDX`，主章節對話庫為 `DIAL_Z00.DDX`。

### 1.1 檔案佈局總覽 (File Layout)
```text
┌────────────────────────────────────────────────────────┐
│ Header: record_count (u16, 2 bytes)                    │
├────────────────────────────────────────────────────────┤
│ Directory Table: record_count * 8 bytes                │
│   ├─ [Entry 0]: node_id (u32), file_offset (u32)       │
│   ├─ [Entry 1]: node_id (u32), file_offset (u32)       │
│   └─ ...                                               │
├────────────────────────────────────────────────────────┤
│ Packed Record Sequence:                                │
│   ├─ [Record 0]: Keyed Record at file_offset 0         │
│   ├─ [Record 1]: Sub-Record / Child at file_offset 1   │
│   ├─ [Record 2]: Keyed Record at file_offset 2         │
│   └─ ... (Tightly packed, zero padding)                │
└────────────────────────────────────────────────────────┘
```

### 1.2 紀錄標頭 (Record Header, 9 Bytes)
對應 C 語言 [`struct DDXRecord`](file:///d:/git/betrayal-at-krondor-for-zh/upstream/betrayal-at-krondor/bak/INCLUDE/structs.h#L616)：
```c
struct DDXRecord {
    unsigned char bStyle;        // 0x00: 樣式 (對話框風格/邊框類型 0..6)
    unsigned short wSpeaker_id;  // 0x01: 發話者 ID (0..6 隊員, 0xFD NPC, 0xFE/0xFF 劇情事件)
    unsigned short wFlags;       // 0x03: 行為標記 (0x200 自動滾動, 0x400 分支話題, 0x100 清螢幕)
    unsigned char bCnt1;         // 0x05: DdxChoice 選項數量 (每個 10 bytes)
    unsigned char bCnt2;         // 0x06: DdxOp 指令數量 (每個 10 bytes)
    unsigned short wBody_len;    // 0x07: 純文字本文長度 (bytes)
};
```

### 1.3 選項與指令陣列 (Choices & Opcodes)
- **`DdxChoice` (10 Bytes):**
  `wCond (u16), nA1 (u16), nA2 (u16), nA3 (u16), nA4 (u16)`
  - `wCond`: 觸發條件 (如話題 ID、技能判定或事件標記)。
  - `nA3`: **關鍵子紀錄檔案偏移 (Sub-record File Offset)**。當玩家選取該選項時，引擎調用 `dialog_load_record_by_key(nA3, 1)` 直接載入該偏移處的子紀錄。
- **`DdxOp` (10 Bytes):**
  `wOp (u16), nA1 (u16), nA2 (u16), nA3 (u16), nA4 (u16)`
  - `wOp`: 指令代碼 (如 `0x01` 分配戰鬥員名稱、`0x04` 設置發話者、`0x0C` 播放音效/音樂)。

### 1.4 本文區塊 (Text Body)
- 長度由 `wBody_len` 嚴格指定。
- 格式特徵：
  - `#標題#`: 定義發話者或場景標題。
  - `@0`..`@5`: 發話者名稱變數替換標記。
  - `\t`: 首行縮排。
  - `\n`: 強制斷行。

---

## 2. BOK 書籍資源二進位結構 (BOK Specification)

BOK 檔案（如 `C11.BOK`）儲存章節小說與劇情插圖頁面。

### 2.1 頁面目錄結構 (PageDirectory)
- **Header:** `size (u32, 4 bytes)`
- **目錄主體:**
  - `nCount (u16)`: 頁面總數
  - `pPages[nCount]`: 各頁面相對於目錄起始點的偏移位址

### 2.2 頁面結構 (`BookPage`, 50 Bytes)
```c
struct BookPage {
    Rect rect;                      // 頁面外框座標與尺寸 (x, y, w, h)
    unsigned short wDisplayNumber;  // 顯示羅馬頁碼數值
    unsigned short wPageNumber;     // 內部邏輯頁碼
    unsigned short wPrevPageNumber; // 前一頁
    unsigned short wNextPageNumber; // 下一頁
    unsigned short wPagePointer;    // 跨章節頁面連結
    unsigned short w_pad12;         // 背景重繪旗標
    unsigned short wImageCount;     // 插圖數量
    unsigned short wReservedCount;  // 繞排文字排除區域數量
    unsigned short wShowPageNumber; // 是否顯示頁碼
    unsigned char pReserved[30];    // 樣式保留狀態 (字型/邊界/文字指針)
};
```

---

## 3. Round-Trip 驗證結論 (Verification Conclusion)

本專案實作之 [`tools/text/ddx_extract.py`](file:///d:/git/betrayal-at-krondor-for-zh/tools/text/ddx_extract.py) 與 [`tools/text/ddx_pack.py`](file:///d:/git/betrayal-at-krondor-for-zh/tools/text/ddx_pack.py)：
1. 完整辨識 Directory 頂層索引紀錄與深層 Sub-records。
2. 自動在 Pack 階段動態計算新長度並重對齊 `nA3` 內部跳轉指標與 Directory 表。
3. 在未修改文字的情境下，針對全遊戲 29 個 DDX 檔案進行解包與重封裝，**100% 達成 SHA-256 Byte-Identical Match**！
