# MLG v1：訊息紀錄檔格式規格（凍結版）

日期：2026-09-06（§11 增訂 2026-09-09）。狀態：**MLG 檔格式已凍結**（第 1 階段成果）。
§11 的增量快照寫入路徑與 `MLGTXN.DAT` v2 標記**不改變任何 MLG byte 佈局**——增量長出來的快照與一次性完整快照 byte-for-byte 相同（`MSGPTEST` 的 `EQUIV` 檢查為證）。

配套文件：[功能與技術規劃](message-log-design.md)、[施工清單](message-log-agent-tasks.md)、[施工進度](message-log-progress.md)。

實作：

- DOS 端：`upstream/betrayal-at-krondor/bak/SRC/DIALOG/MSGLOG.C` / `.H`
- 離線端：`tools/text/message_log.py`
- 測試：`tests/unit/test_message_log.py`、`tools/text/mlg_dos_check.py`（DOS 端互讀）
- Golden fixtures：`tests/fixtures/message_log/*.mlg.hex`

> 本檔案是**唯一**的 byte 佈局來源。C 與 Python 兩邊的常數若與本表不符，視為錯誤；
> `tests/unit/test_message_log.py::TestCHeaderConstantsInSync` 會直接比對 `MSGLOG.H`。

---

## 1. 總體約定

| 項目 | 決定 |
|---|---|
| 位元組序 | **一律 little-endian**，逐欄位寫入。**禁止 `fwrite` C struct**（16 位元編譯器 packing／指標大小會外洩到格式） |
| 字串編碼 | BAK-ZH 緊湊二位元組遊戲編碼（見 [ADR-001](../decisions/ADR-001-chinese-text-encoding.md)），**長度前綴、不含結尾 NUL**。執行期不轉 UTF-8 |
| 校驗 | CRC-32/ISO-HDLC：反射多項式 `0xEDB88320`、初值 `0xFFFFFFFF`、輸出 xor `0xFFFFFFFF`（＝ `zlib.crc32`）。DOS 端用 16 項 nibble 表（64 bytes DGROUP），非 1 KiB 表 |
| 檔案上限 | `MSGLOG_MAX_FILE = 0x3FFFFFFF`（1 GiB）。所有 offset／長度加總都在 signed long 內，遇上限回 `MSGLOG_E_FULL` 並停記，**不回捲** |
| 檔名 | DOS 8.3。存檔槽快照 `SAVEnn.MLG`；工作檔 `MSGWORK.MLG`（第 2 階段決定實際路徑） |
| CRC 用途 | 只偵測意外錯配，**不是安全簽章**。玩家手動對調兩份相同 GAM 的 MLG 無法偵測（設計文件第 6 節已接受此限制） |

## 2. 標頭（64 bytes，固定）

| off | size | 欄位 | 說明 |
|---|---|---|---|
| 0 | 4 | `magic` | ASCII `"BKML"`（`42 4B 4D 4C`） |
| 4 | 2 | `format_version` | `1`。**未知值一律拒絕**，不嘗試解讀 |
| 6 | 2 | `header_length` | `64`。v1 只接受 64 |
| 8 | 2 | `flags` | 見 §2.1 |
| 10 | 2 | `encoding_id` | `1` = BAK-ZH v1。其他值 → `MSGLOG_E_ENCODING` |
| 12 | 4 | `mapping_fingerprint` | 字碼映射指紋，見 §6。不符 → `MSGLOG_E_ENCODING` |
| 16 | 4 | `bound_gam_length` | 綁定 `.GAM` 的位元組長度（僅 snapshot；工作檔為 0） |
| 20 | 4 | `bound_gam_crc32` | 綁定 `.GAM` 的 CRC32（僅 snapshot） |
| 24 | 4 | `committed_length` | **已提交尾端**的絕對檔案 offset。此值之後的位元組不屬於歷史 |
| 28 | 4 | `event_count` | 已提交事件數 |
| 32 | 4 | `next_sequence` | 下一個要配發的事件序號（第一筆是 1） |
| 36 | 4 | `last_event_offset` | 最後一筆已提交事件的絕對 offset；無事件時為 0 |
| 40 | 4 | `data_crc32` | `[header_length, committed_length)` 的 CRC32。**只有 `DATA_CRC` flag 設起時有效** |
| 44 | 8 | `created_time` | 時間線建立時刻，MLGTIME（§4） |
| 52 | 4 | `reserved0` | 0 |
| 56 | 4 | `reserved1` | 0 |
| 60 | 4 | `header_crc32` | **位元組 `[0, 60)` 的 CRC32**（不含本欄位） |

### 2.1 標頭 flags

| bit | 值 | 名稱 | 意義 |
|---|---|---|---|
| 0 | `0x0001` | `SNAPSHOT` | 存檔槽快照；清除代表是執行中的工作檔 |
| 1 | `0x0002` | `HAS_GAP` | 時間線含至少一個紀錄缺口（曾寫入失敗） |
| 2 | `0x0004` | `SEALED` | 標頭是正常關閉時寫的 |
| 3 | `0x0008` | `DATA_CRC` | `data_crc32` 有效 |
| 4 | `0x0010` | `GAM_BOUND` | `bound_gam_*` 有效 |

### 2.2 工作檔與 snapshot 的差別（**規格要求項**）

| | 工作檔 `MSGWORK.MLG` | 快照 `SAVEnn.MLG` |
|---|---|---|
| `SNAPSHOT` | 0 | **1** |
| `GAM_BOUND` / `bound_gam_*` | 0 / 0 | **1** / 實際 GAM 長度與 CRC32 |
| `DATA_CRC` / `data_crc32` | **0 / 0** | **1** / 全歷史 CRC32 |
| `SEALED` | 追加期間為 0；正常關閉時為 1 | 永遠 1 |
| 每次追加的成本 | 記錄本身 + 重寫 64-byte 標頭 | 完整快照：一次串流複製；增量快照（§11）：只複製上次存檔後的新記錄 |

> **「不要求每次追加都重算整個歷史 CRC」如何達成**：`data_crc32` **只在做快照時**（`msglog_prepare_snapshot()` 或 `msglog_extend_snapshot()`）
> 算出。完整快照用一次串流掃描；增量快照從既有快照標頭裡的 `data_crc32` **接續**計算（CRC-32/ISO-HDLC 的 final xor 自反，儲存值就是可續算的執行狀態），只掃新增 bytes。
> 工作檔在追加期間 `DATA_CRC` 永遠是 0，追加只付出「寫記錄 + 重寫 64 bytes 標頭」的代價。
> 每筆事件自己的 `event_crc32` 才是追加時的完整性依據。
>
> `msglog_load_candidate()` 是唯一會重算整份歷史 CRC 的路徑，且只在讀檔驗證候選時發生。
> `msglog_validate_snapshot_tail()`（增量存檔後驗證）只重雜湊新增區段。

### 2.3 已提交尾端的判定（正常 close vs. 追加中斷）

`msglog_open_working()` 的判定順序，**沒有猜測**：

1. 讀 64 bytes。magic／version／`header_length`／`encoding_id`／`mapping_fingerprint` 任一不符 → **直接拒絕**（回 `MSGLOG_E_MAGIC` / `_VERSION` / `_HEADER` / `_ENCODING`），不做恢復。
2. `header_crc32` 正確、`committed_length ≤ 檔案長度`、`last_event_offset` 在合法範圍內，且**該筆記錄本身通過自己的 CRC32** → 採信標頭。
3. 否則進入 **rescan**：從 offset 64 開始逐筆往前走，每筆都要
   `MSGLOG_EVENT_MIN_RECORD ≤ record_length ≤ MSGLOG_MAX_RECORD`、
   `offset + record_length ≤ 檔案長度`、三個字串長度都在各自上限內且加總等於 `record_length`、
   `event_crc32` 正確。第一筆失敗處即為已提交尾端。
   `event_count` / `next_sequence` / `last_event_offset` 由掃描結果重建。
4. `committed_length` 之後的殘留位元組在下一次追加時被 `chsize()` 截掉。

因此：**追加中斷最多只損失那一筆半成品，之前的歷史一定保住**（可驗證前綴）。
`SEALED` 只是「上次是正常關閉」的提示，**不是**判定尾端的依據。

## 3. 事件記錄

每筆記錄 = 52 bytes 固定頭 + speaker + location + body + 4 bytes CRC32。**沒有對齊填充**。

```
record_length = 52 + speaker_len + location_len + body_len + 4
```

| off | size | 欄位 | 說明 |
|---|---|---|---|
| 0 | 4 | `record_length` | 本筆總長，含本欄位與結尾 CRC32 |
| 4 | 2 | `kind` | 見 §3.2 |
| 6 | 2 | `flags` | 見 §3.3 |
| 8 | 4 | `sequence` | 全域遞增事件序號（**不以時間戳當唯一 ID**） |
| 12 | 4 | `conversation` | 所屬 conversation 的 id＝其 `CONV_BEGIN` 記錄的 `sequence`；不在對話中為 0 |
| 16 | 4 | `prev_offset` | 前一筆記錄的絕對 offset；第一筆為 0。清單頁反向分頁用 |
| 20 | 8 | `timestamp` | 事件發生時刻，MLGTIME（§4） |
| 28 | 2 | `chapter` | 章節 |
| 30 | 2 | `zone_id` | `g_gameState.nZoneId` |
| 32 | 2 | `scene_id` | 城鎮／室內場景 id；`0xFFFF` = 不在場景中 |
| 34 | 2 | `speaker_id` | `DDXRecord.wSpeaker_id`；0 = 旁白 |
| 36 | 4 | `source_key` | DDX record key |
| 40 | 2 | `source_file` | `record_key / 100000`（DDX 檔號）；`0xFFFF` = 未知 |
| 42 | 2 | `fragment_index` | 同一段本文被切片時的片號，從 0 起 |
| 44 | 2 | `speaker_len` | ≤ `MSGLOG_MAX_SPEAKER`（64） |
| 46 | 2 | `location_len` | ≤ `MSGLOG_MAX_LOCATION`（64） |
| 48 | 2 | `body_len` | ≤ `MSGLOG_MAX_BODY`（512） |
| 50 | 2 | `reserved` | 0 |
| 52 | `speaker_len` | `speaker` | 說話者顯示名**當下快照**（遊戲編碼位元組） |
| … | `location_len` | `location` | 地點顯示名**當下快照** |
| … | `body_len` | `body` | 已展開的本文位元組 |
| `record_length-4` | 4 | `event_crc32` | **本筆 `[0, record_length-4)` 的 CRC32** |

`MSGLOG_MAX_RECORD = 52 + 64 + 64 + 512 + 4 = 696`。讀取端在**任何長度被當成索引之前**先做上下界檢查。

### 3.1 為何 speaker／location 是快照而非 resource ID

`askabout_name_or_keyword_lookup()` 回傳的是 `g_pKeywordTable` 內的 near 指標，
`dialog_play_record()` 在 `DIALOG.C:1675` 呼叫 `askabout_keyword_table_free()` 後即失效
（第 0 階段 0.7 已證）。DDX 本文指標同樣在 `DIALOG.C:1655` 失效。
因此 API 收的是「呼叫者當下擁有的位元組」，`msglog_append_*()` 在返回前就已寫入磁碟，
**模組本身不保留任何暫存指標**。日後翻譯更新也不會改寫歷史原文。

### 3.2 事件 kind

| 值 | 名稱 | 用途 |
|---|---|---|
| 0 | `NONE` | 保留，非法 |
| 1 | `CONV_BEGIN` | 一場交談開始（最外層 `dialog_play_record()`，見第 0 階段 0.8） |
| 2 | `TEXT` | 一段**已顯示**的本文 |
| 3 | `CHOICE` | 玩家**實際確認**的話題／回答（不記候選、不記取消） |
| 4 | `CONV_END` | 交談結束 |
| 5 | `GAP` | 紀錄缺口標記（同時設標頭 `HAS_GAP`） |
| 6 | `SCENE` | 城鎮／室內場景說明條（`townscene_dlg_draw_page()`，第 4 條顯示路徑） |

**未知 kind 依 `record_length` 跳過**（前提是該筆的長度與 CRC32 都合法），不視為錯誤。
未知 `format_version` 則整份拒絕。

### 3.3 事件 flags

| bit | 值 | 名稱 | 意義 |
|---|---|---|---|
| 0 | `0x0001` | `CONTINUED` | 本片接續前一筆的本文 |
| 1 | `0x0002` | `MORE` | 後面還有續片 |
| 2 | `0x0004` | `NARRATION` | 無說話者（旁白／未知） |
| 3 | `0x0008` | `TRUNCATED` | 來源端就已截斷（正常情況不應出現） |

### 3.4 雙位元組安全分片（**規格要求項**）

BAK-ZH 的 lead byte 範圍是 `0x80..0xDF`；trail byte 是 `0x20..0x7E` 與 `0x80..0xDF`。
**trail byte 可以正好是 `#`（0x23）或 `@`（0x40）**——也就是對話層的標題分隔符與 token 標記。
因此切片必須**從片首往前掃描並追蹤 lead 狀態**，絕不能反向搜尋某個 ASCII 字元。

`msglog_split_point(body, len, limit)`：回傳 ≤ `limit` 且不切斷雙位元組字的最長前綴長度。
遇到「單獨 lead byte 後面沒有 trail」時回 0，呼叫端改為送出該 1 byte，避免無限迴圈。

golden 案例（`SCRIPTED_LONG`）：`'A'` + 300 個 `80 23` = 601 bytes。
天真地在 512 切會落在第 511/512 兩個位元組之間、正好切開一個字，
所以第一片必須是 **511** bytes、第二片 90 bytes。

## 4. MLGTIME（8 bytes）

| off | size | 欄位 | 範圍 |
|---|---|---|---|
| 0 | 2 | `year` | 例 2026 |
| 2 | 1 | `month` | 1–12 |
| 3 | 1 | `day` | 1–31 |
| 4 | 1 | `hour` | 0–23 |
| 5 | 1 | `minute` | 0–59 |
| 6 | 1 | `second` | 0–59 |
| 7 | 1 | `hundredth` | 0–99 |

**不用 FAT 的 32 位元 packed datetime**：它只有 2 秒解析度，無法滿足設計文件要求的
`YYYY-MM-DD HH:MM:SS` 顯示。來源是 DOS `getdate()`／`gettime()`
（`getdate()` 已在第 0 階段 0.4 驗證；`gettime()` **尚未實機驗證**，見進度文件 U4）。

同一秒或系統時間倒退時，**以 `sequence` 決定實際發生順序**，時間戳只照實記錄。

## 5. 結果碼（失敗原因必須可區分）

| 值 | C 名稱 | 意義 |
|---|---|---|
| 0 | `MSGLOG_OK` | 成功 |
| -1 | `MSGLOG_E_STATE` | 目前狀態不允許此呼叫（含 recording-failed） |
| -2 | `MSGLOG_E_PARAM` | 參數錯誤 |
| -3 | `MSGLOG_E_NOMEM` | 未安裝 scratch 緩衝或太小 |
| -4 | `MSGLOG_E_OPEN` | `open()` 失敗 |
| -5 | `MSGLOG_E_IO` | read／write／seek／close 失敗 |
| -6 | `MSGLOG_E_MAGIC` | 不是 MLG 檔 |
| -7 | `MSGLOG_E_VERSION` | 不支援的 `format_version` |
| -8 | `MSGLOG_E_HEADER` | `header_length` 或標頭 CRC32 錯；或候選不是 snapshot |
| -9 | `MSGLOG_E_ENCODING` | `encoding_id` 或字碼映射指紋不符 |
| -10 | `MSGLOG_E_CRC` | 資料或事件 CRC32 不符 |
| -11 | `MSGLOG_E_TRUNC` | 檔案短於自己宣告的長度 |
| -12 | `MSGLOG_E_RANGE` | 長度／offset 越界或會溢位 |
| -13 | `MSGLOG_E_BINDING` | 綁定的 GAM 長度／CRC32 與實際存檔不符 |
| -14 | `MSGLOG_E_FULL` | 觸及 `MSGLOG_MAX_FILE`，停記 |
| -15 | `MSGLOG_E_EMPTY` | 沒有事件／沒有下一筆 |
| -16 | `MSGLOG_E_SUPPRESSED` | 刻意忽略（transition／viewer 期間），不是錯誤 |

## 6. 字碼映射指紋

```
canonical = u32(encoding_id = 1)
          + u32(entry_count)
          + 依 glyph_id 由小到大：u32(glyph_id) + u32(unicode_codepoint)
fingerprint = CRC32(canonical)
```

與 JSON 的鍵順序無關，可由建置工具重算：

```
python -m tools.text.message_log fingerprint --c-define
```

目前 `localization/generated/zh_mapping.json`（5695 字）→ **`0x9659C961`**，
已寫死在 `MSGLOG.H` 的 `MSGLOG_MAPPING_FINGERPRINT`。
`tests/unit/test_message_log.py` 會檢查 C 常數、Python 常數與 JSON 三者一致。

映射若改動（重排 glyph id）指紋就會變，舊 `.MLG` 會被 `MSGLOG_E_ENCODING` **明確拒絕**，
而不是渲染成亂碼。要保留舊歷史必須離線轉換。**只比對字型檔名是不夠的**——指紋比對的是實際 glyph id 對應。

## 7. Golden fixtures

存為可審閱的 hex 文字（repo 的 `.gitignore` 排除 `*.bin`／`*.gam` 這類二進位）：
`tests/fixtures/message_log/`。用 `python -m tools.text.message_log hex2bin` 還原。

### 7.1 `fixture_empty.mlg.hex` —— 空時間線（64 bytes，可完全手算）

```
00000000  42 4B 4D 4C 01 00 40 00 04 00 01 00 61 C9 59 96
00000010  00 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00
00000020  01 00 00 00 00 00 00 00 00 00 00 00 EA 07 09 06
00000030  0D 2D 07 19 00 00 00 00 00 00 00 00 4E 9F A6 4A
```

逐欄位手算：

| off | bytes | 欄位 | 值 |
|---|---|---|---|
| 0 | `42 4B 4D 4C` | magic | `"BKML"` |
| 4 | `01 00` | format_version | 1 |
| 6 | `40 00` | header_length | 0x0040 = 64 |
| 8 | `04 00` | flags | `SEALED` |
| 10 | `01 00` | encoding_id | 1 |
| 12 | `61 C9 59 96` | mapping_fingerprint | 0x9659C961 |
| 16 | `00 00 00 00` | bound_gam_length | 0 |
| 20 | `00 00 00 00` | bound_gam_crc32 | 0 |
| 24 | `40 00 00 00` | committed_length | 64（＝沒有事件） |
| 28 | `00 00 00 00` | event_count | 0 |
| 32 | `01 00 00 00` | next_sequence | 1 |
| 36 | `00 00 00 00` | last_event_offset | 0 |
| 40 | `00 00 00 00` | data_crc32 | 0（`DATA_CRC` 未設） |
| 44 | `EA 07` | year | 0x07EA = 2026 |
| 46 | `09 06 0D 2D 07 19` | 月日時分秒百分秒 | 09-06 13:45:07.25 |
| 52 | `00 …` | reserved0/1 | 0 |
| 60 | `4E 9F A6 4A` | header_crc32 | `CRC32(bytes[0..59]) = 0x4AA69F4E` |

### 7.2 `fixture_one_event.mlg.hex` —— 單一事件（137 bytes，可完全手算）

標頭同上，除了 `committed_length = 0x89 = 137`、`event_count = 1`、
`next_sequence = 2`、`last_event_offset = 0x40 = 64`、`header_crc32 = 0x2E868CDB`。

事件記錄（offset 64 起，73 bytes）：

| 記錄內 off | bytes | 欄位 | 值 |
|---|---|---|---|
| 0 | `49 00 00 00` | record_length | 0x49 = 73 = 52+4+7+6+4 |
| 4 | `02 00` | kind | 2 = `TEXT` |
| 6 | `00 00` | flags | 0 |
| 8 | `01 00 00 00` | sequence | 1 |
| 12 | `01 00 00 00` | conversation | 1 |
| 16 | `00 00 00 00` | prev_offset | 0（第一筆） |
| 20 | `EA 07 09 06 0D 2D 08 00` | timestamp | 2026-09-06 13:45:08.00 |
| 28 | `01 00` | chapter | 1 |
| 30 | `09 00` | zone_id | 9 |
| 32 | `FF FF` | scene_id | 0xFFFF（不在場景） |
| 34 | `07 00` | speaker_id | 7（＝ `Navon du Sandau`，見第 0 階段 0.7） |
| 36 | `06 6A 18 00` | source_key | 0x186A06 = 1600006 |
| 40 | `10 00` | source_file | 16（`DIAL_Z16`） |
| 42 | `00 00` | fragment_index | 0 |
| 44 | `04 00` | speaker_len | 4 |
| 46 | `07 00` | location_len | 7 |
| 48 | `06 00` | body_len | 6 |
| 50 | `00 00` | reserved | 0 |
| 52 | `4F 77 79 6E` | speaker | `"Owyn"` |
| 56 | `4B 72 6F 6E 64 6F 72` | location | `"Krondor"` |
| 63 | `48 65 6C 6C 6F 2E` | body | `"Hello."` |
| 69 | `03 E2 35 C1` | event_crc32 | `CRC32(記錄的前 69 bytes) = 0xC135E203` |

### 7.3 `fixture_scripted.mlg.hex` —— 跨語言腳本 fixture（1141 bytes）

`MLGTEST GEN`（DOS、Borland 編譯、連結遊戲自己的 `MSGLOG.C`）產出的**就是這份位元組**；
`tools.text.message_log.build_scripted_fixture()` 獨立重建同一份。兩者相等即證明跨語言一致。

標頭：`flags = HAS_GAP|SEALED = 0x0006`、`committed_length = 1141`、`event_count = 7`、
`next_sequence = 8`、`last_event_offset = 0x43D`、`data_crc32 = 0`。

| seq | offset | len | kind | flags | frag | spk | loc | body |
|---|---|---|---|---|---|---|---|---|
| 1 | 0x040 | 68 | CONV_BEGIN | 0 | 0 | 4 | 8 | 0 |
| 2 | 0x084 | 88 | TEXT | 0 | 0 | 4 | 8 | 20 |
| 3 | 0x0DC | 72 | CHOICE | 0 | 0 | 4 | 8 | 4 |
| 4 | 0x124 | 579 | TEXT | `MORE` | 0 | 4 | 8 | 511 |
| 5 | 0x367 | 158 | TEXT | `CONTINUED` | 1 | 4 | 8 | 90 |
| 6 | 0x405 | 56 | GAP | 0 | 0 | 0 | 0 | 0 |
| 7 | 0x43D | 56 | CONV_END | 0 | 0 | 0 | 0 | 0 |

- speaker = `84 32 96 49`（「納馮」）、location = `85 43 80 24 81 34 99 3D`（「三山當鋪」）
- seq 2 的 body 含 `80 23`（「漫」，trail = `#`）與 `80 40`（「抵」，trail = `@`），
  外加真正的 ASCII `#` 與 `@`，用來證明 trail byte 不會被誤判
- seq 4/5 是 601 bytes 本文的兩片，切點 511 證明雙位元組安全

### 7.4 `fixture_python.mlg.hex` —— Python 產出、供 DOS 端讀回（218 bytes）

含一筆 `SCENE` 與一筆 `NARRATION` 的 `TEXT`，speaker 為空。

## 8. API 責任分工

| API | 責任 |
|---|---|
| `msglog_init()` | 全部狀態歸零；開機呼叫一次 |
| `msglog_set_scratch(buf, size)` | 安裝／拆除呼叫者擁有的區塊緩衝（≥512 bytes）。**模組本身不配置記憶體** |
| `msglog_new_timeline(path, now)` | 建立空的工作時間線 → `ACTIVE` |
| `msglog_open_working(path)` | 重開工作檔並判定已提交尾端（§2.3） |
| `msglog_conv_begin/end(...)` | conversation 範圍；巢狀只加深不重複記錄 |
| `msglog_append_span/choice/scene(...)` | 追加已顯示本文／實際選擇／場景說明；自動雙位元組安全分片 |
| `msglog_append_gap(now)` | 缺口標記 + `HAS_GAP` |
| `msglog_prepare_snapshot(path, gam_len, gam_crc)` | 串流複製成綁定快照（完整寫入路徑） |
| `msglog_snapshot_extends_working(path, out_hdr64)` | 非破壞性判斷：`path` 是不是目前工作時間線的已提交前綴（可增量長出）；順便回傳其現行 64-byte 標頭當回滾點 |
| `msglog_extend_snapshot(path, gam_len, gam_crc)` | 只把上次存檔後新增的記錄 append 到既有快照、續算 `data_crc32`、重封標頭；任何失敗都把快照還原到原狀（§11） |
| `msglog_validate_snapshot_tail(path, tail_from, gam_len, gam_crc, prev_data_crc, prev_last_off, prev_events)` | 增量存檔後的驗證：標頭 + GAM 綁定 + 從 `prev_data_crc` 續算的 CRC + 只走一遍新增記錄 |
| `msglog_load_candidate(path, gam_len, gam_crc)` | **完整驗證候選，且不動現有時間線** |
| `msglog_activate_candidate(work_path)` | 把已驗證候選變成新的工作時間線 |
| `msglog_discard_candidate()` | 丟棄候選 |
| `msglog_first/last/next/prev_offset()`、`msglog_page_start()`、`msglog_read_event()` | 唯讀分頁；**絕不呼叫 `dialog_play_record()`** |
| `msglog_shutdown()` | 寫入 `SEALED` 標頭並關檔 |
| `msglog_crc32_update()`、`msglog_crc32_file()` | 第 2 階段拿去做 `.GAM` 指紋 |
| `msglog_split_point()` | 第 3 階段拿去做擷取端切片 |

## 9. 狀態機

基底狀態 `INACTIVE` / `ACTIVE` / `FAILED`，外加兩個**獨立的抑制計數器**
`transition_depth` 與 `viewer_depth`。

`msglog_state()` 的優先序：**`FAILED` > `VIEWER` > `TRANSITION` > 基底狀態**。

| 值 | 名稱 | 說明 |
|---|---|---|
| 0 | `INACTIVE` | 沒有活動時間線 |
| 1 | `ACTIVE` | 正在記錄 |
| 2 | `TRANSITION` | 讀檔／新遊戲轉場中，停記 |
| 3 | `VIEWER` | 閱讀器開啟中，停記 |
| 4 | `FAILED` | 曾寫入失敗，已停止追加並保留可驗證前綴 |

**關鍵不變式（設計文件明列的要求）**：viewer 與 transition 只能**抑制**收錄。
因為它們是疊在基底狀態之上的計數器、而不是取代基底狀態的值，
`msglog_leave_viewer()` 後基底若是 `FAILED` 就仍然是 `FAILED`，
**絕不會把原先 failed 的時間線誤變回 active**。
`MLGTEST STATE` 在 DOS 端實際驗證了這條（見進度文件）。

## 10. 記憶體佔用

| 項目 | 大小 |
|---|---|
| 常駐 DGROUP（狀態純量 + 64-byte CRC nibble 表） | **+144 bytes**（`_DATA` +128、`_BSS` +16） |
| overlay 呼叫 stub（常駐） | 207 bytes（`MSGLOG_TEXT` STUBSEG = 0xCF） |
| 程式碼（**overlay，非常駐**） | 8157 bytes（2026-09-06 續作重建，`MSGLOG_TEXT` :OVY = 0x1FDD） |
| 常駐映像總增量 | **+544 bytes**（0x220） |
| 執行期配置 | **0**。區塊緩衝由呼叫者提供，只在存／讀檔期間存在 |

模組刻意**不持有**任何常駐 far 緩衝：追加路徑直接把呼叫者的字串串流到檔案 handle，
CRC 邊寫邊算。這是為了 2026-08-31 那次傳統記憶體不足三重錯誤（`czone_subsystem_init()`
需要 62216 bytes 連續傳統記憶體、實測只有 59232）留下的臨界餘裕。
**本模組絕不碰 `g_pMainScratchBuf`**——`savegame_write()` 做快照的當下正在用它搬 `TEMP.GAM`。

續作驗證補註：上述 DGROUP／常駐映像「增量」為前次記錄，續作未重新建置無 MSGLOG 的對照版，不能當成本次重新量測。最新完整 MAP 的 `_DATA` = 0x3DE0、`_BSS` = 0x2A44、`_STACK` = 0x80；stub 仍為 0xCF。核心沒有自行配置，不代表整個功能零記憶體需求：呼叫者仍須提供分塊 scratch，且未來實際場景的連續記憶體餘量尚待驗證。

§11 的三個新函式仍不持有常駐緩衝、仍只用呼叫者的 scratch；新增的是 overlay 程式碼與 `MSGSAVE.C` 端 88-byte 的堆疊 marker 影像，常駐純量無新增。

---

## 11. 增量快照與 `MLGTXN.DAT` v2（2026-09-09）

存檔時不再每次都把整份歷史複製一遍。`MSGSAVE.C` 的 `msgsave_write_pair()` 依 `msglog_snapshot_extends_working()` 的結果二選一：

- **increment（增量）**：既有 `SAVEnn.MLG` 是目前工作時間線的已提交前綴（`created_time` 相同、`committed_length`／`event_count`／`next_sequence`／`last_event_offset` 都不超過現值、檔長等於標頭宣告、最後一筆記錄 CRC 通過）。把 `SAVEnn.MLG` rename 成 `MLGNEW.MLG`，用 `msglog_extend_snapshot()` 只 append `[舊 committed, 新 committed)`、從舊標頭的 `data_crc32` 續算、重寫標頭並綁定新的 GAM 長度／CRC。
- **full（完整）**：首次存到該槽，或既有 `SAVEnn.MLG` 不是前綴（讀了別條時間線後覆蓋、檔案損壞…）。走原本的 `msglog_prepare_snapshot()` 寫 `MLGNEW.MLG`，並照舊把舊檔 rename 成 `MLGOLD.MLG` 備份。

**等價保證**：`extend(snapshot(T[0:k]), T[k:n])` 與 `prepare_snapshot(T[0:n])` 產出的 `SAVEnn.MLG` **byte-for-byte 相同**。記錄是位置無關的複製，`prev_offset`／`last_event_offset` 都是絕對值且工作檔與快照的事件都從 offset 64 起，`data_crc32` 精確續算。`MSGPTEST` 的 `EQUIV` 檢查每次執行都驗這一點。

### 11.1 `MLGTXN.DAT` v2（88 bytes；`MSGSAVE.C` 私有，非 MLG 格式的一部分）

| off | size | 欄位 |
|---|---|---|
| 0 | 4 | magic `"BKTX"` |
| 4 | 1 | version = **2**（v1 = 18 bytes，仍可讀以回收舊版中斷的存檔；只寫 v2） |
| 5 | 1 | 目標槽 id（0–99） |
| 6 | 1 | 存檔前該槽已有 GAM（0/1） |
| 7 | 1 | 存檔前該槽已有 MLG（0/1） |
| 8 | 4 | 新 GAM 長度 |
| 12 | 4 | 新 GAM CRC32 |
| 16 | 1 | MLG 模式：0 = full（回滾靠 `MLGOLD.MLG`），1 = increment（回滾靠截斷 + 還原下面的舊標頭） |
| 17 | 1 | 0 |
| 18 | 64 | increment 模式的**存檔前 `SAVEnn.MLG` 64-byte 標頭**；full 模式全 0 |
| 82 | 4 | 0 |
| 86 | 2 | `[0, 86)` 的 16-bit 校驗（`msgsave_mark_sum`） |

### 11.2 崩潰恢復

`msgsave_recover_inner()` 讀 marker，依模式判斷：

- **已提交**：full → `msgsave_pair_valid()`（GAM 全檔 CRC + MLG 完整載入）；increment → GAM 全檔 CRC 相符 **且** `msglog_validate_snapshot_tail()` 通過（只驗新增段）。成立就清掉備份／暫存／marker，回報成功。
- **未提交**：GAM 端沿用原本的「有備份就還原備份、沒有就刪掉半成品」。MLG 端 increment 模式 = 把 `SAVEnn.MLG`（或還沒 rename 回去的 `MLGNEW.MLG`）截斷到 marker 記的舊長度、寫回 marker 記的舊 64-byte 標頭；full 模式 = 還原 `MLGOLD.MLG`。整個程序可重跑得到同一結果。

同磁碟 rename 不改動 bytes，所以存檔流程的 stage 6／12 驗證對 increment 模式只做「GAM 標頭 + 續算 CRC 的尾段驗證」，不再整份重雜湊——這也是長時間遊玩後存檔仍不變慢的關鍵。

驗證：`tools/text/msgpair_dos_check.py`（`MSGPTEST.C`）的完整故障矩陣在 full 與 increment 兩種模式下、每個 stage 與每個 I/O op 注入失敗，都要求舊的一對檔案完好；另有 `EQUIV`（增量＝完整，byte 相同）與 `FULL9`（full 模式 stage 9 rename 失敗可恢復）兩項專檢。兩個 OVL 維持 byte-identical。
