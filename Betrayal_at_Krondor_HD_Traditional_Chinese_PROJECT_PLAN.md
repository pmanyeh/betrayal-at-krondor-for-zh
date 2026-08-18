# Betrayal at Krondor HD Traditional Chinese Project
## Original DOS Engine + Host-Side HD Text Rendering

**文件狀態：** Revised Master Project Plan — HD Text Overlay First  
**目標遊戲：** Betrayal at Krondor（叛變克朗多）  
**主要版本：** DOS 1.02 CD-ROM  
**主要策略：** 保留原 DOS 遊戲引擎與遊戲邏輯，在 DOSBox-X / host presentation layer 加入高清繁體中文字層  
**主要研究基底：** `canassa/betrayal-at-krondor` byte-perfect recompilation  
**輔助工具：** `old-games/bak-translation-tools`、DOSBox-X、DOSBox-X MCP Debugger  
**次要參考：** BaKGL、xBaK  
**工作方式：** VS Code + AI Agents + Phase Gates + Evidence-First  
**Canonical translation：** UTF-8 `zh-TW`

---

# 0. Project Mission

本專案**不重製 Betrayal at Krondor 遊戲引擎**。

保留：

- 原 DOS 遊戲邏輯
- 原戰鬥、AI、任務與事件
- 原資源與存檔格式
- 原遊戲輸入與 timing
- 原 DOS framebuffer

新增：

> **Host-side HD Presentation Layer**

第一階段只做：

> **HD Traditional Chinese Text Overlay**

後續才考慮：

- HD books
- HD UI labels
- HD portraits
- HD icons
- shaders / scaling
- optional image replacement

第一個重大成功標準：

> **原版 KRONDOR.EXE 正常執行時，指定對話能在 DOSBox-X 最終輸出畫面上，由 host 以真正高解析度 TrueType/OpenType 字型顯示繁體中文。**

在此以前禁止大規模翻譯。

---

# 1. Architecture Change

舊計畫：

```text
UTF-8 translation
→ custom DOS encoding
→ DDX/BOK repack
→ modified TEXTWRAP.C
→ modified FONT.C
→ DOS Chinese bitmap font
```

新計畫：

```text
Original KRONDOR.EXE
        │
        ├─ original game logic
        ├─ original resource handling
        ├─ original English renderer
        │
        └─ minimal TextEvent instrumentation
                     │
                     ▼
              DOSBox-X bridge
                     │
                     ▼
              Presentation Event Queue
                     │
                     ▼
              Localization Lookup
                     │
                     ▼
                 UTF-8 zh-TW
                     │
                     ▼
          Host HD Text Renderer
                     │
                     ▼
             Final SDL output
```

核心原則：

> DOS engine 決定「現在顯示什麼」。

> Host presentation layer 決定「玩家最後看到什麼文字」。

---

# 2. Why HD Text First

此路線第一階段可避開：

- Big5/custom DOS encoding
- double-byte DOS parser
- 256 glyph `.FNT` 限制
- DOS 中文 bitmap font
- conventional memory 字型壓力
- far-pointer 中文字庫
- DOS 中文換行
- DDX 中文重新 pack
- Unicode → DOS encoding conversion

Host 端直接：

```text
UTF-8
→ Unicode
→ TrueType/OpenType
→ high-resolution rasterization
→ SDL
```

原生 DOS 中文 renderer 保留為未來 fallback，不是主線。

---

# 3. Non-Goals Before First HD POC

Phase 7 PASS 前禁止：

- 完成 BaKGL
- 完成 xBaK
- 重寫 Krondor engine
- 重寫 combat/world renderer
- 3D HD material replacement
- FreeType 移植進 DOS guest
- 完整 Unicode DOS engine
- 大量翻譯
- OCR-based translation
- AI screenshot recognition pipeline
- full HD UI remake

---

# 4. Primary Sources

## 4.1 Original-engine authority

```text
https://github.com/canassa/betrayal-at-krondor
```

用途：

- reconstructed original DOS source
- source-level call graph
- 1.02 build baseline
- minimal instrumentation

若 reconstructed source 與 remake 推測不同，優先採 reconstructed source evidence。

## 4.2 Translation tools

```text
https://github.com/old-games/bak-translation-tools
```

用途：

- resource research
- BOK
- FNT
- extraction workflow
- image/resource formats

Agent 必須 audit source tree，不可只依 README 推測 DDX support。

## 4.3 BaKGL

```text
https://github.com/xavieran/BaKGL
```

僅作：

- resource reference
- graphics override reference
- modern renderer reference

不作為本專案 runtime target。

---

# 5. High-Level Components

## A — Original DOS Guest

`KRONDOR.EXE`

負責：

- game state
- resource load
- DDX/BOK logic
- token substitution
- original rendering
- emit minimal presentation metadata

不得負責：

- UTF-8
- translation database
- TrueType
- HD layout
- host DPI

## B — Guest Text Event Instrumentation

當遊戲準備顯示某段文字時產生：

```text
TextEvent
```

例：

```json
{
  "event": "text_show",
  "surface": "dialog",
  "record_id": 12345,
  "speaker_id": 7,
  "x": 40,
  "y": 132,
  "w": 240,
  "h": 54,
  "style": 2
}
```

第一版優先送 stable ID 與 layout metadata，不送 UTF-8。

## C — DOSBox-X Presentation Bridge

```text
guest event
→ host event
```

要求：

- deterministic
- bounded
- non-blocking
- safe to ignore
- HD disabled 時不影響遊戲

## D — Host HD Text Renderer

負責：

- UTF-8
- font loading
- zh-TW glyph rendering
- wrap
- clipping
- coordinate transform
- resize/fullscreen
- optional original-English masking

## E — Localization Store

Canonical source：

```text
UTF-8 JSON
```

不得綁定 DOS encoding。

---

# 6. Suggested Repository Layout

```text
bak-hd-zh-tw/
├─ README.md
├─ PROJECT_PLAN.md
├─ AGENTS.md
├─ docs/
│  ├─ baseline/
│  ├─ research/
│  ├─ architecture/
│  ├─ protocol/
│  ├─ renderer/
│  ├─ localization/
│  ├─ testing/
│  ├─ decisions/
│  └─ reports/
├─ upstream/
│  ├─ betrayal-at-krondor/
│  └─ dosbox-x/
├─ guest/
│  ├─ instrumentation/
│  └─ protocol/
├─ host/
│  ├─ bridge/
│  ├─ hd_text/
│  └─ presentation/
├─ localization/
│  ├─ zh-TW/
│  │  ├─ dialog/
│  │  ├─ books/
│  │  ├─ ui/
│  │  ├─ items/
│  │  └─ glossary/
│  └─ schema/
├─ tools/
│  ├─ extract/
│  ├─ validate/
│  └─ diagnostics/
├─ tests/
│  ├─ unit/
│  ├─ protocol/
│  ├─ integration/
│  ├─ runtime/
│  └─ acceptance/
└─ testdata/
   └─ synthetic/
```

若整合既有 DOSBox-X MCP Debugger repo，HD presentation 與 AI debugger 必須邏輯分離。

---

# 7. Global Agent Rules

## 7.1 Evidence First

修改前必須記錄：

- source file
- function
- call path
- runtime evidence
- expected behavior
- minimal proposed change

禁止猜測後直接改。

## 7.2 Minimal Guest Mutation

KRONDOR guest 修改只做：

```text
detect
→ identify
→ emit
```

不在 guest 做翻譯、UTF-8、HD rendering。

## 7.3 Fail-Open

若：

- bridge disabled
- localization missing
- font missing
- renderer unavailable

則：

> 原版英文遊戲仍須正常工作。

## 7.4 Original Engine Is Authority

HD layer 不可改：

- dialog choices
- RNG
- combat
- movement
- saves
- game state
- chapter progression

## 7.5 No OCR

禁止：

```text
framebuffer screenshot
→ OCR
→ translation
→ overlay
```

我們有 source 與 record identity。

## 7.6 No Pixel Identity

不得以畫面 hash / pixel pattern 作主要文字 identity。

優先：

- DDX record ID
- BOK record ID
- resource key
- UI string ID
- explicit message type

## 7.7 No Silent Fallback

Agent 不得：

- 1.02 build fail 後偷換 1.00
- transport fail 後改 OCR
- overlay fail 後改 BaKGL 宣稱成功
- HD render fail 後用低解析中文字放大冒充

---

# 8. Stop Conditions

以下任一成立，Agent 必須停止並回報 BLOCKED：

1. baseline 無法重現
2. game version 不明
3. stable text identity 找不到
4. instrumentation 需要大幅改 gameplay code
5. event transport 阻塞 emulation thread
6. coordinate semantics 無法證實
7. host overlay 必須改 game state
8. masking 原英文無可靠方案且無法閱讀
9. licensing/distribution blocker
10. existing MCP/debugger regression
11. 必須修改 frozen baseline 才能 PASS

Blocker report：

```markdown
# Blocker Report
## Observation
## Evidence
## Impact
## Options
## Recommended Action
## Files Touched
## Git Status
```

---

# 9. Frozen Baselines

建立兩個 baseline。

## Krondor baseline

記錄：

- upstream commit
- 1.02 target
- build procedure
- binary verification
- game-data location（local only）
- runtime startup

## DOSBox-X baseline

記錄：

- branch
- commit
- AI bridge state
- MCP state
- test counts
- executable path
- normal video path

HD 改動不得破壞現有 debugger/MCP 功能。

---

# 10. Phase 0 — Verified Dual Baseline

## Goal

在沒有 HD code 時確認：

1. Krondor 1.02 reconstructed build 可重現
2. DOSBox-X current project 可重現
3. rebuilt Krondor 可在此 DOSBox-X 正常運行

## Tasks

### Krondor

- inspect repo
- record commit/tree
- read README/BUILDING
- identify exact 1.02 build
- build
- verify expected binary
- run

### DOSBox-X

- record branch/commit/tree
- build existing target
- run existing deterministic regressions
- verify bridge/debugger baseline

### Integration

- launch Krondor
- reach English dialog
- verify input
- verify normal rendering

## Deliverables

```text
docs/baseline/phase0-krondor.md
docs/baseline/phase0-dosboxx.md
docs/baseline/phase0-integration.md
```

## Acceptance

- [ ] Krondor 1.02 build PASS
- [ ] upstream binary verification PASS
- [ ] DOSBox-X build PASS
- [ ] existing regressions PASS
- [ ] rebuilt game boots
- [ ] English dialog visible
- [ ] no HD code added

**Gate:** Phase 0 fail → STOP.

---

# 11. Phase 1 — Text Surface Reconnaissance

## Goal

找出「文字內容與 identity 已確定、但還沒拆成 glyph」的最佳 hook。

至少研究：

```text
DIALOG.C
TEXTWRAP.C
FONT.C
```

以及 caller/callee。

## Questions

1. DDX record ID 在哪裡？
2. body 何時讀入？
3. token substitution 在哪裡？
4. final text buffer 在哪裡？
5. speaker identity 是否存在？
6. target rectangle 何時確定？
7. style/color 何時確定？
8. dialog clear/close lifecycle？
9. 下一頁/下一句如何切換？
10. BOK 是否不同 path？
11. UI static text 哪裡來？
12. compiled-in strings 有哪些？

## Preferred Hook

最佳 hook 應：

- 一個 text surface 只產生少量 event
- 不在 glyph renderer 每字送 event
- 有 stable identity
- 有 layout rectangle
- 不需改 game logic

## Deliverable

```text
docs/research/text-surface-callgraph.md
```

必須包含：

```text
resource/key
→ record load
→ token expansion
→ final text
→ layout region
→ original renderer
```

並列：

- preferred hook
- alternative hooks
- rejected hooks

## Acceptance

- [ ] stable dialog identity found
- [ ] final text stage found
- [ ] rectangle source found
- [ ] lifecycle understood
- [ ] one Chapter 1 dialog traced
- [ ] no functional code change

---

# 12. Phase 2 — Presentation Protocol v1

## Goal

設計 guest → host protocol。

此 Phase 只設計。

## Requirements

- versioned
- bounded
- deterministic
- endian explicit
- no raw pointers
- non-blocking
- ignorable
- fail-open

## Minimum Events

```text
PRESENTATION_HELLO
TEXT_SHOW
TEXT_CLEAR
RESET/CLEAR_ALL
```

## Candidate TextEvent

```c
struct TextEventV1 {
    uint16_t version;
    uint16_t event_type;
    uint32_t surface_id;
    uint32_t record_id;
    int16_t x;
    int16_t y;
    int16_t w;
    int16_t h;
    uint16_t style;
    uint16_t flags;
    uint16_t speaker_id;
    uint16_t reserved;
};
```

此結構只是 proposal，Agent 必須依 compiler/alignment/transport evidence 決定。

## Coordinate Rule

guest 只送 logical DOS coordinates。

guest 不知道：

- 1080p
- 4K
- DPI
- window size

## Deliverable

```text
docs/protocol/ADR-001-presentation-protocol-v1.md
```

## Acceptance

- [ ] packet frozen
- [ ] identity defined
- [ ] coordinate semantics defined
- [ ] lifetime defined
- [ ] version mismatch behavior
- [ ] renderer-disabled behavior
- [ ] guest 不含 Unicode

---

# 13. Phase 3 — Guest Event POC

## Goal

讓一個指定對話發出可靠 TextEvent。

原流程：

```text
dialog
→ original renderer
```

新流程：

```text
dialog
├→ emit TextEvent
└→ original renderer
```

## Scope

只支援一個 approved dialog path。

## Critical Invariant

event failure：

```text
must not affect original render
```

## Acceptance

- [ ] target dialog event appears
- [ ] record ID correct
- [ ] region correct
- [ ] lifetime/clear correct
- [ ] wrong dialog does not share identity
- [ ] no bridge → game works
- [ ] original English remains
- [ ] gameplay unchanged
- [ ] modification minimal

---

# 14. Phase 4 — DOSBox-X Event Reception

## Goal

Host 能收到並記錄 event。

此 Phase**不畫中文**。

```text
KRONDOR.EXE
→ presentation transport
→ DOSBox-X
→ bounded event queue
→ structured capture/log
```

## Hard Boundaries

禁止：

- localization lookup
- font loading
- SDL text rendering

## Acceptance

- [ ] payload exact
- [ ] ordering correct
- [ ] clear event correct
- [ ] no blocking
- [ ] queue bounded
- [ ] existing MCP/debugger regressions PASS
- [ ] non-Krondor DOS software unaffected

---

# 15. Phase 5 — Offline HD Text Renderer

## Goal

不啟動 Krondor，先完成 host renderer harness。

## Required v1

- UTF-8 input
- Traditional Chinese glyphs
- TrueType/OpenType font
- logical rectangle
- coordinate scaling
- wrap
- clip
- left alignment
- resize
- fullscreen transform

## Font Policy

repo 不得自行 commit 未確認授權的 font binary。

使用設定：

```json
{
  "font_path": "local/font/path",
  "font_size": 28
}
```

## Test Texts

```text
我們在哪裡？
Owyn / 歐文
「你確定嗎？」
```

另測：

- long line
- empty
- missing glyph
- malformed UTF-8
- resize

## Deliverables

```text
host/hd_text/
tests/unit/hd_text/
docs/renderer/hd-text-layout.md
```

## Acceptance

- [ ] UTF-8 PASS
- [ ] zh-TW glyph PASS
- [ ] wrap PASS
- [ ] logical→drawable PASS
- [ ] resize PASS
- [ ] missing font clean fail
- [ ] no Krondor dependency

---

# 16. Phase 6 — Canonical Localization Store

## Goal

建立 engine-independent UTF-8 translation source。

## Recommended Schema

```json
{
  "schema": 1,
  "entries": [
    {
      "key": "dialog:chapter1:000001",
      "record_id": 1,
      "surface": "dialog",
      "speaker_id": 7,
      "source": "Where are we?",
      "zh_TW": "我們在哪裡？",
      "status": "translated",
      "notes": ""
    }
  ]
}
```

## Stable ID Rule

不得使用 source/translation 文字本身當 key。

## Validation

- duplicate ID
- invalid UTF-8
- missing source
- unknown record
- schema version
- placeholder/token preservation

## Acceptance

- [ ] deterministic lookup
- [ ] UTF-8 round-trip
- [ ] malformed DB rejected
- [ ] missing translation fallback
- [ ] 只放 Phase 7 所需少量資料

---

# 17. Phase 7 — ★ First Live HD Traditional Chinese Dialog ★

## Goal

重大 Gate：

> 原版 KRONDOR.EXE 正常執行時，host 在正確位置顯示第一句真正高清繁中。

Pipeline：

```text
KRONDOR.EXE
→ dialog record
→ TextEvent
→ DOSBox-X
→ localization lookup
→ UTF-8 zh-TW
→ HD layout
→ SDL draw
→ final screen
```

## Original English Handling

優先順序：

### A

若 dialog background 適合，host mask original text rectangle。

### B

保存/重畫原背景區域，再畫中文。

### C

只有 A/B 不可行才考慮 guest suppress original glyph draw。

**第一版不優先修改 FONT.C。**

## Required Tests

### T1 Identity

指定 dialog → 正確繁中。

### T2 Wrong Dialog

其他 dialog 不得顯示同一翻譯。

### T3 True HD

必須由 host 直接以 high-resolution font rasterization 繪製。

禁止低解析中文 upscale。

### T4 Resize

resize 後 region 正確。

### T5 Fullscreen

fullscreen 正確。

### T6 Disable

HD renderer disabled → 原英文正常。

### T7 Missing Translation

無翻譯 → 原英文 fallback。

### T8 Regression

existing DOSBox-X MCP/debugger regressions PASS。

## PASS Definition

- [ ] original game logic authoritative
- [ ] original game playable
- [ ] correct event
- [ ] correct UTF-8 lookup
- [ ] correct HD Chinese
- [ ] correct location
- [ ] disable fallback
- [ ] missing translation fallback
- [ ] no OCR
- [ ] no remake engine

---

# 18. Phase 8 — Dialog Lifecycle Robustness

## Goal

由單句 POC 擴展成正常對話。

Host state machine：

```text
IDLE
↓ TEXT_SHOW
ACTIVE
↓ TEXT_SHOW
REPLACE
↓ TEXT_CLEAR
IDLE
```

需處理：

- repeated record
- fast advance
- speaker change
- scene clear
- pause
- resize
- stale event

## Acceptance

至少 20 個連續 dialog events：

不得有：

- ghost text
- stale text
- wrong translation
- duplicate overlay
- late clear

---

# 19. Phase 9 — Chinese Layout

## Goal

建立可用的繁中排版。

v1 支援：

- 中文逐字斷行
- ASCII word wrapping
- 中英混排
- basic punctuation constraints
- line height
- padding
- clipping

不要求完整 Unicode UAX #14。

Config 可 per-surface：

```json
{
  "dialog": {
    "font_size": 28,
    "line_height": 34,
    "padding": 8
  }
}
```

---

# 20. Phase 10 — DDX Extraction Pipeline

## Goal

抽取 translation metadata，不把中文塞回 DDX。

新架構：

```text
original DDX
→ extract IDs + English
→ UTF-8 localization JSON
→ host lookup
```

第一階段不需要：

```text
zh-TW → DDX pack
```

若現成 DDX tool 不完整，可建立 read-only：

```text
tools/extract/ddx_extract.py
```

## Acceptance

- [ ] target chapter records extractable
- [ ] stable IDs
- [ ] source English preserved
- [ ] original DDX unmodified
- [ ] deterministic output

---

# 21. Phase 11 — HD BOK / Book Text

## Goal

書本頁面改用 HD overlay。

研究：

- BOK page ID
- text region
- page lifecycle
- headings
- body
- illustrations

新增 event 類型：

```text
BOOK_TEXT_SHOW
BOOK_TEXT_CLEAR
```

## Acceptance

- [ ] one translated page
- [ ] page turn replacement
- [ ] multiline wrap
- [ ] resize/fullscreen
- [ ] original book logic untouched

---

# 22. Phase 12 — Full Text Surface Inventory

盤點：

- DDX dialog
- BOK
- main menu
- inventory
- character sheet
- items
- spells
- combat
- shops
- save/load
- chapter titles
- map labels
- system messages
- button labels
- image-embedded text

輸出：

```text
docs/research/text-surface-inventory.md
```

欄位：

```text
Surface
Source
Stable Identity
Hook
Region
Translation Ready
HD Ready
Priority
Notes
```

---

# 23. Phase 13 — Static UI Text

處理：

- menu
- labels
- buttons
- inventory UI

可能新增：

```text
UI_TEXT_SHOW
UI_TEXT_HIDE
```

禁止 glyph-level event spam。

---

# 24. Phase 14 — Dynamic / Combat Text

若動態訊息沒有 stable resource ID，研究：

```text
message_type + arguments
```

例：

```json
{
  "message": "combat.damage",
  "actor": 3,
  "target": 5,
  "amount": 12
}
```

只有 source evidence 支援時才採用。

---

# 25. Phase 15 — Translation Production Tooling

開始真正翻譯前建立：

- source hash
- translation status
- glossary
- notes
- token validation
- missing translation report
- changed source report

Status：

```text
untranslated
draft
review
approved
blocked
```

---

# 26. Phase 16 — Glossary

```text
localization/zh-TW/glossary/terms.csv
```

欄位：

```text
English
Traditional Chinese
Category
Context
Notes
Status
```

---

# 27. Phase 17 — Full Translation Campaign

只有此 Phase 才大量翻譯。

順序：

1. Main UI
2. Names
3. Locations
4. Items
5. Spells
6. Chapter 1
7. Chapter 2...
8. Books
9. Edge surfaces

每章獨立 acceptance。

---

# 28. Phase 18 — HD Portrait / UI Extension

HD text 穩定後才做：

- portraits
- inventory icons
- book art
- dialog frames
- static UI panels

可新增：

```text
IMAGE_SHOW
```

但 guest 不重寫 graphics logic。

---

# 29. Phase 19 — Scaling / Shader

可加入：

- integer scaling
- aspect correction
- CRT shaders
- sharp scaling
- configurable filtering

與 localization 邏輯分離。

---

# 30. 3D HD Material Replacement — Deferred

原 world renderer 到 SDL 時通常只剩 framebuffer。

host 不自然知道：

- texture ID
- UV
- polygon
- depth

真正 3D HD texture replacement 可能需要 render metadata 與 partial host re-render。

因此：

> **不屬於第一階段。**

只建立未來研究文件：

```text
docs/future/3d-hd-rendering.md
```

---

# 31. DOSBox-X MCP Debugger Role

MCP Debugger 是：

> diagnostics tool

不是玩家 runtime dependency。

用途：

- break dialog load
- inspect record ID
- inspect text buffer
- verify region
- diagnose stale event
- check bridge state

玩家使用 HD 中文版不應需要啟動 MCP server。

---

# 32. Presentation Bridge vs AI Bridge

可共用底層 transport ideas，但邏輯分離：

```text
DOSBox-X
├─ Debug / AI Bridge
│  └─ MCP
└─ Presentation Bridge
   └─ HD Renderer
```

HD text 不得依賴每句文字經 MCP JSON-RPC round trip。

---

# 33. Performance

要求：

- no emulation frame stalls
- no synchronous network wait
- bounded queue
- stale-event handling
- near-zero overhead when disabled

Queue full：

presentation event 可安全 drop / replace，但不得 block emulation thread。

實際 policy 由 Agent 依 thread model設計。

---

# 34. Threading

Agent 必須確認：

- emulation thread
- render thread
- SDL call thread
- bridge callback thread

建立：

```text
docs/architecture/threading-model.md
```

禁止在未知 thread 直接 SDL draw。

---

# 35. Original Text Masking Strategy

優先：

1. solid dialog background mask
2. saved background rectangle restore
3. presentation-aware background redraw
4. guest suppress original text（最後手段）

POC 不優先改 FONT.C。

---

# 36. Runtime State

Overlay 是 derived presentation state。

- emulator pause → overlay 可保留
- reset → clear all
- game load → 等新 events
- scene change → clear stale overlay

不得寫入 Krondor save。

---

# 37. Localization Fallback

Lookup zh-TW fail：

```text
show original English
```

不得：

- blank
- crash
- key text
- raw JSON

---

# 38. Configuration

建議：

```json
{
  "hd_presentation": {
    "enabled": true,
    "language": "zh-TW",
    "text": {
      "enabled": true,
      "font_path": "...",
      "font_size": 28,
      "mask_original": true
    }
  }
}
```

---

# 39. Test Strategy

## Tier 1 — Unit

- UTF-8
- localization lookup
- layout
- coordinate transform
- event serialization

## Tier 2 — Protocol

- encode/decode
- version mismatch
- malformed packet
- queue

## Tier 3 — Renderer Harness

- Chinese draw
- wrap
- resize
- fullscreen

## Tier 4 — Runtime

- dialog
- BOK
- UI

## Tier 5 — Fresh Agent Acceptance

核心穩定後才做。

---

# 40. Deterministic Test Suites

至少：

```text
presentation_event_tests
localization_tests
layout_tests
coordinate_tests
fallback_tests
```

Phase report 必須記錄 exact pass counts。

---

# 41. Synthetic Test Data

公開 repo 禁止原版 game data。

tests 使用：

- synthetic events
- synthetic localization
- synthetic images

真實 integration 透過 local-only：

```text
BAK_DATA_DIR
```

---

# 42. Copyright / Distribution Boundary

不得 commit：

- KRONDOR.001
- KRONDOR.RMF
- original graphics/audio
- proprietary compiler binaries
- 未確認可散布的 fonts
- secrets

公開前另做 legal/provenance audit。

---

# 43. Publication Audit

push 前掃描：

- absolute local paths
- secrets
- original assets
- generated binaries
- compiler tools
- font licenses
- third-party DLLs
- source provenance
- README claims

有 blocker：

> **STOP BEFORE PUSH.**

---

# 44. Branch / Commit Discipline

推薦：

```text
main
baseline/krondor-102
feature/presentation-protocol
feature/guest-dialog-events
feature/host-hd-text
feature/zh-tw-localization
```

推薦 commits：

```text
phase0: verify dual baseline
phase1: document dialog text lifecycle
phase2: define presentation protocol v1
phase3: emit first dialog event
phase4: receive presentation event in host
phase5: add offline HD text renderer
phase6: add canonical zh-TW store
phase7: render first live HD Chinese dialog
```

Phase FAIL 不標完成。

---

# 45. Agent Phase Report Template

```markdown
# Phase N Report

## Result
PASS / FAIL / BLOCKED

## Goal

## Baselines
- Krondor commit:
- DOSBox-X commit:
- Game version:

## Evidence

## Work Performed

## Files Added

## Files Modified

## Tests
| Test | Result | Evidence |
|---|---|---|

## Runtime Verification

## Regressions

## Blockers

## Deviations From Plan

## Git Status
- branch:
- commit:
- working tree:
- pushed:

## Recommendation
```

禁止只回：

```text
Done.
```

---

# 46. Fresh-Agent Review

建議 fresh review：

- Phase 1 callgraph
- Phase 2 protocol
- Phase 7 POC
- publication audit

Reviewer 只拿 requirements + code + evidence。

---

# 47. Phase Gates

| Phase | Gate |
|---|---|
| P0 | Krondor + DOSBox-X dual baseline |
| P1 | Text identity/region/lifecycle proven |
| P2 | Presentation Protocol v1 frozen |
| P3 | Guest emits approved event |
| P4 | Host receives exact event |
| P5 | Offline HD UTF-8 renderer PASS |
| P6 | Canonical zh-TW lookup PASS |
| **P7** | **First live HD Traditional Chinese dialog** |
| P8 | Dialog lifecycle stable |
| P9 | Chinese layout stable |
| P10 | DDX extraction |
| P11 | HD books |
| P12 | Text inventory |
| P13 | Static UI |
| P14 | Dynamic/combat |
| P15+ | Production localization |
| P18+ | HD visual extensions |

---

# 48. Phase 7 Go / No-Go

## GO

若：

- instrumentation small
- identity stable
- masking visually clean
- resize/fullscreen correct
- game unaffected

則繼續 HD overlay。

## RE-EVALUATE

若：

- stable identity 不成立
- overlay rectangle 不可靠
- original text masking impossible
- instrumentation extremely invasive
- DOSBox-X render pipeline無法安全 overlay

再考慮：

1. guest suppress original text
2. DOS-native Chinese renderer
3. alternative presentation hook
4. BaKGL

不得 Phase 7 前自行改成 remake。

---

# 49. FIRST AGENT TASK — PHASE 0 ONLY

將以下 Task 直接交給第一個 Agent。

---

## TASK: Establish Dual Baseline

You are working on **Betrayal at Krondor HD Traditional Chinese**, an original-DOS-engine localization project.

Read this entire `PROJECT_PLAN.md`.

Execute **PHASE 0 ONLY**.

### Goal

Establish verified, reproducible baselines for:

1. Betrayal at Krondor 1.02 reconstructed source.
2. The current DOSBox-X / DOSBox-X MCP Debugger source tree.
3. Running the unmodified rebuilt Krondor 1.02 inside that DOSBox-X build.

### A. Inspect Workspace

Identify:

- relevant repositories
- branches
- commits
- dirty working trees
- existing documentation

Do not clean/reset anything automatically.

### B. Krondor Baseline

For `canassa/betrayal-at-krondor`:

1. record commit hash
2. read README
3. read BUILDING instructions
4. identify exact 1.02 build command
5. identify legally obtained game-data requirement
6. build unmodified 1.02 if local data is already available
7. run upstream binary verification
8. record results

### C. DOSBox-X Baseline

For the existing DOSBox-X MCP Debugger project:

1. record branch
2. record commit
3. record working tree
4. identify current build executable
5. run existing deterministic regression tests relevant to bridge/MCP/debugger
6. do not modify frozen tests

### D. Runtime Integration

If both baselines are available:

1. run rebuilt Krondor 1.02
2. verify normal English text
3. verify normal input
4. verify no HD presentation modification exists
5. document reproducible launch procedure

### Required Documents

```text
docs/baseline/phase0-krondor.md
docs/baseline/phase0-dosboxx.md
docs/baseline/phase0-integration.md
```

### Do NOT

- implement HD renderer
- modify SDL rendering
- modify KRONDOR text functions
- design or implement presentation protocol
- emit guest events
- translate text
- modify DDX/BOK
- add font libraries
- modify MCP behavior
- push GitHub
- start Phase 1

### STOP Conditions

Stop and report BLOCKED if:

- Krondor 1.02 data cannot be identified
- reconstructed build fails
- binary verification fails
- DOSBox-X baseline cannot build
- existing debugger regression fails
- baseline success requires source modification
- game data would need to be copied into Git

### Required Final Report

Use the `Agent Phase Report Template`.

Do not proceed to Phase 1 even if Phase 0 passes.

---

# 50. Phase 1 Task Skeleton

**Do not execute until Phase 0 is reviewed.**

```text
Map the complete Chapter 1 dialog text lifecycle from resource identity through
token expansion, layout/rectangle selection, and original rendering.

Do not modify source.

Identify the best minimal event hook and at least one alternative.
Return evidence and stop.
```

---

# 51. Phase 2 Task Skeleton

```text
Design Presentation Protocol v1 based strictly on approved Phase 1 evidence.

No HD renderer.
No translation implementation.
Produce ADR-001 and stop.
```

---

# 52. Phase 3 Task Skeleton

```text
Implement the smallest guest instrumentation for one approved dialog.

Original English rendering must remain unchanged.
Failure to emit an event must not affect gameplay.

Do not implement host rendering.
```

---

# 53. Phase 4 Task Skeleton

```text
Receive and capture the approved Presentation Protocol event in DOSBox-X.

Do not render text.

Prove identity, coordinates, lifetime, ordering, and non-blocking behavior.
```

---

# 54. Phase 5 Task Skeleton

```text
Build a standalone host HD text rendering harness.

Input:
- logical game rectangle
- UTF-8 text
- configured font

Output:
- high-resolution text

Do not integrate with Krondor.
```

---

# 55. Phase 6 Task Skeleton

```text
Create canonical UTF-8 zh-TW localization storage and deterministic lookup.

Populate only enough data for the single Phase 7 POC.

Do not bulk translate.
```

---

# 56. Phase 7 Task Skeleton

```text
Integrate:
- approved guest event
- DOSBox-X presentation receiver
- localization lookup
- HD text renderer

Render exactly one approved Traditional Chinese dialog in live
Betrayal at Krondor 1.02.

Verify:
- original game works
- renderer disable fallback
- missing translation fallback
- resize
- fullscreen
- MCP/debugger regressions

Stop after report.
```

---

# 57. Architectural Invariants

## I1

```text
Original DOS game is the gameplay authority.
```

## I2

```text
HD layer is presentation-only.
```

## I3

```text
HD layer can be disabled.
```

## I4

```text
Missing translation never blocks gameplay.
```

## I5

```text
Canonical translation is UTF-8.
```

## I6

```text
No OCR identity path.
```

## I7

```text
No remake engine dependency.
```

## I8

```text
Existing DOSBox-X debugger remains independent.
```

---

# 58. Technical Success Definition

第一階段技術成功：

> Betrayal at Krondor 1.02 original reconstructed DOS engine runs normally, emits presentation metadata for a dialog, and DOSBox-X renders the matching UTF-8 Traditional Chinese translation at native host resolution while preserving original gameplay behavior.

---

# 59. User Experience Goal

最終：

```text
1993 original gameplay
+
original logic and saves
+
modern scaling
+
true HD Traditional Chinese text
+
optional HD portraits/UI
```

玩家感受到：

> **原版 Betrayal at Krondor 的 HD 中文 Remaster Presentation**

而不是另一套 remake engine。

---

# 60. Long-Term Roadmap

核心中文完成後：

```text
HD Dialog Text
→ HD Books
→ HD UI
→ HD Portraits
→ HD Icons
→ Shaders
→ Optional Graphics Replacement
→ Experimental 3D Presentation
```

每一項維持：

```text
original engine authority
```

---

# 61. Final Instruction to All Agents

Do not maximize code output.

Maximize verified, reversible progress.

Always prefer:

```text
observe
→ prove
→ document
→ design
→ make the smallest change
→ test
→ preserve fallback
→ stop at the phase gate
```

The project succeeds when the original game remains the game,
and the host presentation layer makes it readable and beautiful on modern displays.

**Phase 7 — the first live HD Traditional Chinese dialog — is the first major success gate.**
