# Betrayal at Krondor 繁體中文化專案計畫
## Agent-Driven DOS Localization Project Plan

**文件狀態：** Initial Project Plan  
**目標平台：** 原版 DOS《Betrayal at Krondor》（優先 1.02 CD-ROM）  
**主要策略：** byte-perfect recompilation + 原版遊戲資料 + 自訂繁中文字型/文字編碼  
**輔助策略：** bak-translation-tools + DOSBox-X / DOSBox-X MCP Debugger  
**替代研究線：** BaKGL / xBaK（僅作格式、行為與現代引擎參考）  
**語言：** 繁體中文（Traditional Chinese）  
**工作方式：** VS Code + AI Agents，Phase-gated，evidence-first

---

# 0. 專案使命

本專案的目標是製作可在原始 DOS《Betrayal at Krondor》遊戲引擎上執行的繁體中文化版本。

專案優先保持：

1. 原 DOS 遊戲邏輯與體驗。
2. 原遊戲資料檔相容性。
3. 最小化對 reconstructed engine source 的侵入。
4. 中文文字資料與原始遊戲資產分離。
5. 可重現、可測試、可由 AI Agents 持續執行的工程流程。
6. 不散布原版遊戲資產；使用者必須自行提供合法取得的遊戲資料。

第一個成功標準不是「完成整款遊戲翻譯」，而是：

> **使用 rebuilt KRONDOR.EXE，在 DOSBox-X 中讓遊戲真正顯示一小句繁體中文，且英文原始文字仍可正常顯示。**

在此 POC 完成以前，禁止開始大規模翻譯。

---

# 1. 已知技術基礎

## 1.1 Byte-perfect recompilation

主要研究基底：

- `canassa/betrayal-at-krondor`
- https://github.com/canassa/betrayal-at-krondor

該專案目前聲明：

- 已由 DOS binaries 逆向重建原始程式。
- 可 byte-identically build 原始遊戲 binary。
- 同一 source tree 支援：
  - 1.00 floppy
  - 1.02 CD-ROM
- 包含 browser-based asset viewer。
- reconstructed source 位於 `bak/SRC/`。
- 專案本身以 preservation / reverse-engineering 為目標，不以 modding 為目標。

**本專案不得直接把中文修改混入上游 preservation branch。**

應建立獨立 fork / branch，將：

- preservation baseline
- Traditional Chinese modifications

清楚分離。

---

## 1.2 Translation tools

輔助工具：

- `old-games/bak-translation-tools`
- https://github.com/old-games/bak-translation-tools

目前可見工具能力包括：

- `krondor.001` / `krondor.rmf` resource extract/archive
- `.FNT` font operations
- Font Editor
- `.BOK` book operations
- `.PAL` / `.SCX` / `.BMX` image operations

目前 README 的 TODO/Status 顯示：

- BOK text extract / pack 已列入文字工具範圍
- DDX dialog extract / pack 尚需確認實作狀態，不可假設已完成

**Agent 必須檢查目前實際 source tree 與測試，不得只依 README 推測。**

---

## 1.3 BaKGL

參考專案：

- `xavieran/BaKGL`
- https://github.com/xavieran/BaKGL

用途：

- 參考資源解析方式。
- 參考遊戲系統語意。
- 參考 graphics override / modding。
- 研究現代 renderer 的可能性。

目前不將 BaKGL 當成主要中文化 runtime，因為其 README 仍將 Combat 列為待完成項目。

---

## 1.4 xBaK

歷史參考：

- xBaK 是較早期的開源重製／逆向成果。
- BaKGL 與目前 recompilation 專案皆承認其研究貢獻。

用途限於：

- 格式比對
- 行為比對
- 命名／結構參考

不得在存在 byte-perfect reconstructed source 時，優先以 xBaK 猜測原版行為。

---

# 2. 核心工程假設

目前最重要的假設：

> 原版文字 renderer 主要採 single-byte character model；完整繁中不可能只靠替換既有 256 字元 `.FNT` 完成。

因此預期需要：

1. 定義繁中編碼。
2. 定義中文字型資料格式。
3. 修改字串 iterator。
4. 修改 width calculation。
5. 修改 wrapping。
6. 修改 glyph rendering。
7. 保留原 ASCII / control codes 行為。
8. 處理 DDX/BOK 等文字資源。

但這些都必須由 Agent 以 source evidence 驗證。

**禁止把上述假設直接當成實作事實。**

---

# 3. 建議 repo 架構

建議建立新的中文化工作 repo，而不是直接污染 upstream clone。

```text
bak-zh-tw/
├─ README.md
├─ PROJECT_PLAN.md
├─ AGENTS.md
├─ docs/
│  ├─ baseline/
│  ├─ research/
│  ├─ encoding/
│  ├─ font/
│  ├─ ddx/
│  ├─ bok/
│  ├─ testing/
│  └─ decisions/
├─ upstream/
│  └─ betrayal-at-krondor/        # fork/submodule/working copy
├─ tools/
│  ├─ text/
│  ├─ font/
│  ├─ validation/
│  └─ build/
├─ localization/
│  ├─ glossary/
│  ├─ extracted/
│  ├─ translated/
│  └─ generated/
├─ testdata/
│  └─ synthetic/                  # 不放原版 copyrighted assets
└─ tests/
   ├─ unit/
   ├─ integration/
   └─ acceptance/
```

若使用者偏好直接 fork `canassa/betrayal-at-krondor`，則至少建立：

```text
docs/zh-tw/
tools/zh-tw/
tests/zh-tw/
```

並將中文化變更放在獨立 branch。

---

# 4. Agent 全域操作規則

所有 AI Agents 均必須遵守。

## 4.1 Evidence-first

任何修改前，先提出 evidence：

- source path
- function name
- data structure
- call chain
- sample behavior
- build/test result

不得因名稱看起來合理就直接修改。

---

## 4.2 Frozen baseline

建立 verified baseline 後：

- 不得修改 baseline evidence。
- 不得修改原版 binary。
- 不得覆寫使用者的原始 game data。
- 測試輸出必須寫到獨立 working directory。

---

## 4.3 No scope explosion

在 Phase 4 POC 完成以前，禁止：

- 翻譯大量劇情。
- 製作完整中文字庫。
- 重畫 UI。
- 研究 HD graphics。
- 改寫整個 text engine。
- 移植 SDL / FreeType。
- 將 BaKGL 改成主要 runtime。
- 建立完整 GUI localization editor。

---

## 4.4 Stop on blocker

若發現以下任一情況，Agent 必須停止修改並回報：

1. baseline 無法重現 build。
2. 使用的遊戲版本與 source target 不一致。
3. reconstructed source 行為與原 binary 不一致。
4. 文字格式理解存在兩種以上合理解釋。
5. pack 後 resource 無法 round-trip。
6. control code 與中文 encoding 衝突且尚無決策。
7. 需要修改 undocumented binary blob。
8. 必須散布 copyrighted original assets 才能繼續。
9. 測試無法證明修改沒有破壞英文。
10. Agent 需要大幅重構 preservation source 才能完成小型 POC。

遇 blocker：

> **STOP — do not “try something” silently.**

建立 blocker report，列出：

- Observation
- Evidence
- Impact
- Options
- Recommended next action

---

## 4.5 No silent fallback

Agent 不得：

- build 失敗後偷偷改用另一版本。
- DDX 工具不存在後直接以 regex 猜格式。
- 中文顯示失敗後改用圖片文字假裝成功。
- DOS runtime 失敗後改用 BaKGL 宣稱 POC 通過。

---

## 4.6 Commit discipline

每個 Phase：

1. 先完成 evidence。
2. 再修改。
3. 跑 acceptance。
4. PASS 後 commit。

推薦 commit：

```text
phase0: establish verified 1.02 baseline
phase1: document text rendering pipeline
phase2: document dialog and book resource pipeline
phase3: freeze zh-tw encoding and font format
phase4: render first traditional chinese sentence
...
```

Phase FAIL 時不得標記完成。

---

# 5. 版本選擇

## Primary target

**Betrayal at Krondor 1.02 CD-ROM**

理由：

- recompilation upstream 明確支援。
- 較適合作為最終玩家版本。
- 後續聲音／CD 發行內容相對完整。

## Secondary target

1.00 floppy 僅用於：

- 比對 reconstructed source。
- 檢查版本差異。
- 測試修改是否能容易 backport。

**第一輪 POC 只做 1.02。**

---

# 6. Phase 0 — Reproducible Baseline

## Goal

建立完全沒有中文修改的可重現基準。

## Tasks

Agent 必須：

1. clone/fork recompilation project。
2. 記錄 upstream commit hash。
3. 閱讀：
   - README
   - BUILDING
   - CONTRIBUTING
   - version/build scripts
4. 確認 Windows build requirements。
5. 使用合法取得的 1.02 game data。
6. build 原版 target。
7. 比對 upstream 定義的 byte-match / hashes。
8. 在 DOSBox-X 啟動 rebuilt game。
9. 進入至少一個具有英文對話的遊戲畫面。
10. 保存 build log 與驗證結果。

## Deliverables

```text
docs/baseline/phase0-baseline.md
docs/baseline/build-environment.md
docs/baseline/version-evidence.md
```

## Acceptance

必須全部 PASS：

- [ ] 1.02 build 成功
- [ ] expected binary match 通過
- [ ] rebuilt executable 可在 DOSBox-X 執行
- [ ] 英文原版畫面可正常顯示
- [ ] 沒有任何中文化 source modification
- [ ] upstream commit hash 已記錄
- [ ] 原始 game data 未被修改

## Gate

**Phase 0 不 PASS，不得進 Phase 1。**

---

# 7. Phase 1 — Text Rendering Reconnaissance

## Goal

用 source evidence 建立完整文字繪製 call chain。

## Required investigation

至少研究：

```text
FONT.C
TEXTWRAP.C
DIALOG.C
```

以及相關 headers / callers。

Agent 需確認：

1. 字串 termination。
2. char signed/unsigned behavior。
3. glyph lookup。
4. glyph metrics。
5. width computation。
6. line wrapping。
7. alignment。
8. control codes。
9. style/color changes。
10. clipping。
11. far pointer / memory model constraints。
12. buffer size限制。
13. 對話文字進入 renderer 的 call path。
14. BOK 文字是否走同一 renderer。

## Required deliverable

```text
docs/research/text-rendering-pipeline.md
```

內容必須包含：

```text
resource
→ parser
→ token expansion
→ wrap
→ width
→ renderer
→ glyph
→ framebuffer
```

每一箭頭都要有：

- source file
- function
- evidence

## Required tests

建立不改功能的 instrumentation 或 test harness（若 upstream build constraints 不允許 instrumentation，可使用 isolated test implementation）。

需證明：

- ASCII width 計算。
- 空白。
- newline/wrap。
- 一個 control code。
- 一段正常英文對話。

## Acceptance

- [ ] text iterator 已確認
- [ ] control byte range 已確認
- [ ] glyph index rule 已確認
- [ ] wrap rule 已確認
- [ ] DIALOG → renderer call chain 已確認
- [ ] 文件含 source references
- [ ] 尚未加入中文功能

---

# 8. Phase 2 — Text Resource Reconnaissance

## Goal

理解需要翻譯的文字資源，以及 extract/pack 可行性。

## 2A — Translation tools audit

檢查 `bak-translation-tools`：

- resource commands
- font commands
- book commands
- image commands
- DDX 實際 source 是否存在
- tests
- round-trip behavior

禁止只看 README。

建立：

```text
docs/research/bak-translation-tools-audit.md
```

---

## 2B — BOK

確認：

- BOK record/layout
- encoding
- text extraction
- text insertion
- length/offset update
- compression（若有）
- round-trip

Acceptance：

```text
original BOK
→ extract
→ no text change
→ pack
→ semantic/binary validation
```

---

## 2C — DDX

使用 reconstructed `DIALOG.C` 作 authoritative evidence。

確認：

- DDX directory structure
- record key
- record headers
- body layout
- token/control syntax
- pointers/offsets
- record length
- chapter mapping
- compression（若有）

若現成 DDX tool 不存在：

建立最小工具：

```text
tools/text/ddx_extract.py
tools/text/ddx_pack.py
```

先只要求：

```text
DDX → structured JSON
structured JSON → DDX
```

JSON 必須保留：

- record key/id
- untranslated raw bytes（必要時）
- text
- tokens
- metadata

## Critical requirement

必須先做 unchanged round-trip。

## Acceptance

- [ ] 至少一個 DDX 可 extract
- [ ] 可辨識一段實際遊戲對話
- [ ] unchanged pack 可重新被遊戲讀取
- [ ] tokens 不被破壞
- [ ] offsets/lengths 正確
- [ ] 原始檔保留不覆寫

---

# 9. Phase 3 — Chinese Encoding & Font Architecture

## Goal

在寫 renderer 前，先凍結最小中文方案。

## Candidate designs

Agent 必須比較至少：

### Option A — Big5-like two-byte

優點：

- 現成繁中字碼。
- 翻譯工具容易處理。

風險：

- 原遊戲 high-byte control codes。
- 需要 escape/conflict handling。
- Big5 lead/trail byte 可能撞現有語意。

### Option B — Custom escape + glyph ID

示例：

```text
ASCII:          00-7F
Control:        preserve original
Chinese escape: ESC <hi> <lo>
```

優點：

- 與原遊戲 control codes 可明確隔離。
- glyph ID 可達 65536。
- 與 Unicode mapping 可分離。

缺點：

- 文本不是標準 Big5。
- extractor/packer 必須轉碼。

### Option C — Runtime mapping table

translation file 使用 UTF-8，pack 時轉成 compact game encoding。

此方案可與 Option B 結合。

---

## Required decision document

```text
docs/decisions/ADR-001-chinese-text-encoding.md
```

必須包含：

- chosen encoding
- rejected alternatives
- byte grammar
- ASCII compatibility
- control compatibility
- malformed sequence behavior
- max glyph count
- tool conversion rule
- test vectors

---

## Font architecture

第一版禁止把數千中文字塞進原 `.FNT`。

建議建立獨立格式，例如：

```text
ZH16.FNT
```

或：

```text
ZH16.DAT
```

最小 header 建議：

```text
magic
version
glyph width
glyph height
glyph count
offset table
bitmap data
```

**實際格式由 Agent 根據 DOS memory constraints 決定。**

第一個 POC 字型只需包含 10–50 個中文字。

例如：

```text
歐
文
我
們
在
哪
裡
克
朗
多
```

## Required decision document

```text
docs/decisions/ADR-002-chinese-font-format.md
```

## Acceptance

- [ ] encoding 無 control collision
- [ ] ASCII 保持原樣
- [ ] font format 可被 DOS memory model 讀取
- [ ] mapping 可 deterministic generate
- [ ] synthetic unit tests PASS
- [ ] 尚未進行大量翻譯

---

# 10. Phase 4 — First Chinese Rendering POC

## Goal

**讓原 DOS engine 真正顯示第一句繁中。**

這是專案最重要的 Gate。

## Scope

只允許：

- 一個 DDX record 或其他非常容易觸發的文字來源
- 10–50 個中文字
- 單一字型大小
- monochrome / 原色彩系統
- 不要求漂亮
- 不要求所有 UI

## Target example

例如：

```text
歐文：我們在哪裡？
```

實際句子可依最容易穩定觸發的遊戲場景選擇。

---

## Required renderer changes

Agent 必須以 Phase 1 evidence 決定確切修改點。

預期可能涉及：

```text
font_draw_text_far()
font_text_pixel_width()
font_glyph_metrics()
textwrap_compute_lines()
```

但：

> **不得因本計畫列出函式名就假設全部必須修改。**

只改 evidence 證明必要的部分。

---

## Required invariants

修改後：

1. 原 ASCII glyph renderer 保留。
2. 原 control codes 保留。
3. 英文 UI 不變。
4. 中文 glyph 走獨立 code path。
5. 不改遊戲 logic。
6. 不改 save format。
7. 不依賴 Windows/host Unicode runtime。
8. 不使用圖片覆蓋文字冒充中文 renderer。

---

## Acceptance scenario

Agent 必須提供：

### Test A — English regression

顯示原英文：

```text
Inventory
Options
```

或其他已固定 baseline。

PASS：

- glyph 正常
- spacing 正常
- wrap 正常

### Test B — Chinese render

顯示指定繁中句。

PASS：

- 每個中文字正確
- 無 byte 被當成錯誤 control code
- 無 crash
- 無 memory corruption

### Test C — Mixed text

例如：

```text
Owyn / 歐文
```

PASS：

- ASCII + Chinese 可共存

### Test D — Width

中文句子的：

```text
computed width
```

必須與實際 glyph advance 相符。

### Test E — Wrap

至少一個中文 wrap case 必須通過。

---

## Phase 4 PASS 定義

只有以下條件同時成立才 PASS：

> rebuilt 1.02 KRONDOR.EXE + 原版 game data + 新中文字型/文字資料，在 DOSBox-X 中可實際顯示繁中句子。

**BaKGL 顯示成功不算 Phase 4 PASS。**

---

# 11. Phase 5 — Robust Chinese Text Engine

## Goal

把 POC 擴展成可靠文字層。

## Features

- safe iterator
- codepoint/glyph decoding
- width
- wrapping
- clipping
- alignment
- punctuation handling
- mixed ASCII/Chinese
- malformed sequence handling
- token boundary handling
- buffer length validation

---

## Chinese wrapping policy

至少評估：

- 不允許行首標點
- 不允許行尾開括號
- 中文可逐字換行
- ASCII word 保持 word wrapping
- 中文 + ASCII 混排

先做 minimal policy，再視需要改善。

不得在此 Phase 引入完整 Unicode line-breaking algorithm。

---

## Acceptance

建立 deterministic tests：

```text
ASCII only
Chinese only
mixed
punctuation
long line
token insertion
max line
malformed bytes
```

全部 PASS。

---

# 12. Phase 6 — DDX Localization Pipeline

## Goal

建立可重現的 DDX 翻譯工作流。

## Desired pipeline

```text
original DDX
→ extractor
→ canonical localization file
→ translator/editor
→ encoder
→ packer
→ localized DDX
→ game
```

## Canonical file

建議 UTF-8 JSON / YAML / CSV。

優先 JSON，例如：

```json
{
  "id": "...",
  "source": "Where are we?",
  "translation": "我們在哪裡？",
  "tokens": [],
  "notes": "",
  "status": "translated"
}
```

Agent 必須保留 record identity，不得靠文字本身當 key。

---

## Validation

每次 build translation pack：

- untranslated entries fallback to source
- token count/identity validation
- illegal byte detection
- buffer size validation
- deterministic output
- report changed records

---

## Acceptance

至少：

- [ ] 20 個 DDX entries 可 round-trip
- [ ] 10 個 entries 有繁中
- [ ] tokens 正常
- [ ] 遊戲實際可播放對話
- [ ] 不需手工 hex edit

---

# 13. Phase 7 — BOK Localization

## Goal

讓書籍/章節文字完整支援繁中。

## Tasks

1. 驗證現有 BOK exporter/importer。
2. 導入統一 encoding pipeline。
3. 更新 width/wrap。
4. 建立至少一頁繁中 BOK 測試。
5. 驗證翻頁與 layout。

## Acceptance

- [ ] 原英文 BOK regression PASS
- [ ] 繁中 BOK 可顯示
- [ ] 多行 wrap 正常
- [ ] 翻頁正常
- [ ] 無 buffer corruption

---

# 14. Phase 8 — Text Surface Inventory

## Goal

盤點遊戲內所有可見文字來源。

分類至少：

- DDX dialog
- BOK books
- UI labels
- inventory
- item names/descriptions
- spell names/descriptions
- character names
- location names
- combat messages
- system messages
- save/load UI
- chapter titles
- image-embedded text

輸出：

```text
docs/research/text-surface-inventory.md
```

每一類標記：

```text
SOURCE
FORMAT
EXTRACTABLE
PACKABLE
RUNTIME PATH
CHINESE READY
STATUS
```

## 現況（已完成盤點）

[`docs/research/text-surface-inventory.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/research/text-surface-inventory.md) 已產出，涵蓋全部四條文字路徑：

1. DDX 對話系統（Phase 6 既有基礎設施，615 筆已翻譯）。
2. BOK 書籍系統（Phase 7 前置調查已完成，新格式＋需改 `BOOKTEXT.C` 支援雙位元組）。
3. MenuPage / NamedTable / DialogWidget 資源系統（新發現，主選單/存讀檔/法術選單/戰鬥選單等數十個 `.dat` 檔，需要新 parser/packer）。
4. 話題詢問選單 `KEYWORD.DAT`（新發現，對話畫面下方的關鍵字按鈕格，**不屬於 DDX**，是獨立第四條路徑）。

另加：話題詢問選單 `KEYWORD.DAT`（§4a）、大地圖城鎮標籤 `fmap_twn.dat`（§4b）、大量硬編碼 C 字串常數（可直接改原始碼，無需新工具，`g_abStatNames` 優先度最高）、密碼盤謎題（需要設計決策而非翻譯）、隊伍角色名字（存檔二進位欄位，暫不處理）。詳見該文件 §1–§11。盤點已涵蓋全部類別，唯一剩餘開放項目（`MENULBL.C` 捲動貼圖被哪支 `.TTM` 腳本呼叫，§9）屬於資料檔調查，不影響盤點完整性。

## Gate

在 inventory 未完成前，不得宣稱「完整中文化工具鏈完成」。**Inventory 本身已完成，但這只代表「已知道要做什麼」——§3/§4/§4a 列出的新資源格式尚未開發對應 parser/packer，翻譯/工程工作尚未開始，不得因為 inventory 完成就宣稱這些子系統已可翻譯。**

---

# 15. Phase 9 — Translation Production Tooling

## Goal

開始支援真正翻譯工作，而不是 renderer research。

## Features

- UTF-8 translation source
- stable IDs
- source text hash
- status
- translator notes
- terminology glossary
- token validation
- character limit hints
- build report
- untranslated report
- changed-source report

---

## Glossary

建立：

```text
localization/glossary/terms.csv
```

至少包含：

```text
English
Traditional Chinese
Category
Context
Notes
Approved
```

人名、地名、魔法、物品等需保持一致。

---

# 16. Phase 10 — Full Translation Campaign

## Goal

才在此 Phase 開始大規模翻譯。

建議順序：

1. Main UI
2. Character/location names
3. Items
4. Spells
5. System/combat messages
6. Chapter 1 dialogs
7. Chapter 1 books
8. 逐章擴展

每章獨立 acceptance。

---

# 17. Phase 11 — Full Game QA

## Goal

完整 playthrough 驗證。

## QA categories

### Rendering

- missing glyph
- wrong glyph
- clipped text
- overlap
- bad wrap
- control byte leak

### Content

- mistranslation
- terminology inconsistency
- token grammar
- character gender/name
- context mismatch

### Runtime

- crash
- corruption
- invalid resource
- save/load regression
- chapter progression regression

---

## Automated diagnostics

建議遊戲啟動／resource build 前產生：

```text
missing-glyphs.txt
untranslated.txt
invalid-encoding.txt
token-errors.txt
overlong-lines.txt
resource-build-report.txt
```

---

# 18. DOSBox-X MCP Debugger 的角色

DOSBox-X MCP Debugger 不應成為本專案的必要 build dependency。

它定位為：

**runtime verification / diagnostics tool**

可用於：

1. DDX record load trace。
2. 文字 buffer memory inspection。
3. token expansion 前後比較。
4. 中文 decoder breakpoint。
5. glyph lookup。
6. width/wrap bug。
7. crash root-cause。
8. memory corruption inspection。
9. 英文與中文 code path 比對。

---

## 建議新增 MCP 能力後的測試

若 MCP Debugger 已支援 real-mode memory watch：

```text
watch dialog buffer
watch glyph data
watch renderer state
```

若已支援 keyboard/mouse injection：

```text
launch
navigate
trigger target dialog
capture state
```

可進一步建立半自動 acceptance。

但：

> 中文化專案不得等待 MCP Debugger 新功能完成才前進。

---

# 19. Phase 12 — Optional Agent-Driven Runtime Acceptance

這是進階 Phase。

## Goal

讓 fresh Agent：

1. 啟動測試遊戲。
2. 透過 DOSBox-X MCP 控制。
3. 進入指定畫面。
4. 讀取 runtime state。
5. 驗證指定中文 glyph code 被 consume。
6. 驗證 text engine 沒有異常。
7. 回報 PASS/FAIL。

此 Phase 模式可沿用 DOSBox-X MCP Debugger 專案的：

- deterministic tests
- fresh-agent acceptance
- bounded session
- evidence adapter
- tool-call budget

---

# 20. Test Strategy

## Tier 1 — Unit

不啟動 DOS 遊戲：

- encoding
- decoder
- glyph lookup
- font parsing
- width
- wrapping
- DDX parser
- DDX packer
- BOK pipeline

## Tier 2 — Binary/resource integration

- unchanged round-trip
- known fixture
- deterministic build
- invalid input rejection

## Tier 3 — DOS runtime

- game boot
- text display
- dialog
- BOK
- mixed text
- chapter scenario

## Tier 4 — Agent acceptance

optional，於核心功能穩定後加入。

---

# 21. Synthetic Test Data Rule

Git repo 內禁止放原版遊戲 copyrighted assets。

tests 應優先使用：

- synthetic DDX-like fixtures
- synthetic font fixtures
- handcrafted minimal records
- hash/evidence descriptions

需要真實 game data 的 integration tests：

```text
SKIP if game data not configured
```

並由環境變數或 local config 指向使用者自己的合法 copy。

---

# 22. Legal / Distribution Boundary

專案公開發布時：

可以發布：

- 自己撰寫的 translation tools
- encoding/font loader modifications（依 base project license/legal條件審慎處理）
- translation text（需另外考慮衍生著作權問題）
- patch files
- synthetic test data
- documentation

不得直接發布：

- KRONDOR.001
- KRONDOR.RMF
- 原版 graphics
- 原版音訊
- 原版完整 game data
- 未經允許的 proprietary compiler/toolchain binaries

**Agent 不得自行決定可再散布何種第三方內容。**

若要公開 GitHub，先做 publication audit。

---

# 23. Publication Audit Gate

GitHub push 前：

1. 掃描絕對本機路徑。
2. 掃描 secrets。
3. 掃描 original game assets。
4. 掃描 generated binaries。
5. 掃描 third-party compiler files。
6. 檢查 license。
7. 檢查 submodule/fork provenance。
8. 確認 README 不聲稱官方授權。
9. 確認 build instructions 要求使用者自行提供合法遊戲資料。

若有 blocker：

> **STOP BEFORE PUSH.**

---

# 24. Agent Required Reporting Format

每個 Phase 完成時回報：

```markdown
# Phase X Report

## Result
PASS / FAIL / BLOCKED

## Baseline
- upstream commit:
- game version:
- environment:

## Work Performed

## Files Added

## Files Modified

## Evidence

## Tests
| Test | Result | Evidence |
|---|---|---|

## Regressions

## Blockers

## Deviations From Plan

## Next Recommended Phase

## Git Status
- working tree:
- commit:
- pushed: yes/no
```

禁止只回：

> “Done.”

---

# 25. Agent First Task

將本段直接交給第一個 Agent。

---

## TASK — Phase 0 Only

You are working on a Traditional Chinese localization research project for the DOS game **Betrayal at Krondor**.

Your current task is **Phase 0 only: establish a verified, reproducible upstream baseline**.

### Objectives

1. Inspect the current project directory.
2. Identify whether `canassa/betrayal-at-krondor` is already present.
3. If present, record its current commit and working-tree state.
4. Read the upstream README, BUILDING documentation, CONTRIBUTING documentation, and build scripts relevant to version 1.02.
5. Determine the exact prerequisites needed on this Windows environment.
6. Attempt to reproduce the **unmodified 1.02 CD-ROM build** using the user's legally obtained game data if it is already configured and accessible.
7. Verify the upstream byte-match/hash mechanism.
8. If possible, run the rebuilt game in the existing DOSBox-X environment and verify that a normal English text screen is displayed.
9. Create the Phase 0 documentation defined in `PROJECT_PLAN.md`.

### Hard boundaries

Do **not**:

- implement Chinese rendering;
- modify FONT.C;
- modify TEXTWRAP.C;
- modify DIALOG.C;
- modify game resources;
- translate any text;
- build DDX tooling;
- copy original game assets into Git;
- change upstream source just to make a failing baseline pass;
- silently switch from 1.02 to 1.00;
- start Phase 1.

### Stop conditions

Stop and report BLOCKED if:

- the required legally obtained game files cannot be located;
- the game-data version cannot be established;
- required build tooling is unavailable;
- the unmodified upstream build fails;
- expected byte-match verification fails;
- completing the build would require modifying upstream source.

### Required output

Create:

```text
docs/baseline/phase0-baseline.md
docs/baseline/build-environment.md
docs/baseline/version-evidence.md
```

Then produce a Phase 0 Report using the format defined in this plan.

Do not proceed to Phase 1 unless Phase 0 is PASS.

---

# 26. Milestone Summary

| Milestone | Meaning |
|---|---|
| M0 | 原版 1.02 reconstructed build 可重現 |
| M1 | 文字 renderer / DDX call chain 已證實 |
| M2 | DDX/BOK extract-pack 路徑已證實 |
| M3 | 中文 encoding + font architecture 凍結 |
| **M4** | **原 DOS Krondor 顯示第一句繁體中文** |
| M5 | 中文 wrap / mixed text 穩定 |
| M6 | DDX translation pipeline 可用 |
| M7 | BOK translation pipeline 可用 |
| M8 | 全文字來源 inventory 完成 |
| M9 | Translation production tooling 完成 |
| M10 | 全遊戲翻譯 |
| M11 | Complete QA |
| M12 | Optional AI-agent runtime acceptance |

---

# 27. Success Definition

## Technical success

最低技術成功：

> 原版 1.02 reconstructed DOS engine 能讀取外部中文字型，解析自訂繁中編碼，並在正常遊戲對話中顯示繁體中文字，同時保持原英文文字與遊戲功能正常。

## Project success

完整成功：

> 玩家以自己合法取得的 Betrayal at Krondor 遊戲資料，加上本專案提供的 patch/tools/localization package，即可完成可玩的繁體中文版，不需要散布原版遊戲資產。

---

# 28. Current Recommended Priority

```text
Phase 0
  ↓
Verified 1.02 baseline
  ↓
Phase 1
  ↓
Renderer + wrap + dialog evidence
  ↓
Phase 2
  ↓
DDX/BOK pipeline
  ↓
Phase 3
  ↓
Encoding + font ADR
  ↓
Phase 4
  ↓
★ FIRST TRADITIONAL CHINESE SENTENCE ★
```

在 ★ M4 ★ 以前：

> **所有工作都應服務於證明「原 DOS engine 可以可靠顯示繁中」這一件事。**

不要提前優化，不要提前全翻譯，不要提前做 HD remake。

---

# 29. Reference Repositories

## Primary

Betrayal at Krondor byte-perfect recompilation  
https://github.com/canassa/betrayal-at-krondor

## Localization tooling

Betrayal at Krondor Translation Tools  
https://github.com/old-games/bak-translation-tools

## Modern remake/reference

BaKGL  
https://github.com/xavieran/BaKGL

## Historical reference

xBaK / related historical reverse-engineering work  
Use only as secondary evidence where the reconstructed original source does not answer the question.

---

# 30. Final Instruction to All Agents

The project is intentionally phased.

**Do not maximize code output. Maximize verified progress.**

The preferred behavior is:

```text
observe
→ document
→ test
→ make the smallest change
→ test again
→ preserve evidence
→ stop at the phase gate
```

A small PASS with strong evidence is more valuable than a large unverified implementation.
