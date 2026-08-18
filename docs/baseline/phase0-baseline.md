# Phase 0 Baseline Report — Reproducible Baseline

## 1. 專案基準總覽 (Baseline Summary)

- **專案名稱：** Betrayal at Krondor 繁體中文化研究專案 (Traditional Chinese Localization)
- **上游 Recompilation Repo：** `https://github.com/canassa/betrayal-at-krondor`
- **上游分支：** `master`
- **上游 Commit Hash：** `1fc2a69e306af1623cd22f3390a5569302059f4d`
- **上游提交資訊：** `🏗️ rewrite gstate_hourly_tick without the goto` (Author: Cesar Canassa, 2026-08-03)
- **上游狀態：** Working Tree Clean, 零修改

---

## 2. 目錄架構配置 (Directory Architecture)

依據 [`Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`](file:///d:/git/betrayal-at-krondor-for-zh/Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md) 第 3 節建立之獨立中文化工作庫結構：

```text
d:\git\betrayal-at-krondor-for-zh\
├─ .gitignore                                      # 版權與資產隔離規則
├─ Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md # 總體專案計畫
├─ docs/
│  ├─ baseline/
│  │  ├─ phase0-baseline.md                        # 本 Master 基準報告
│  │  ├─ build-environment.md                      # 構建工具鏈與環境分析
│  │  └─ version-evidence.md                       # 遊戲資產雜湊與版本分析
│  ├─ research/                                    # Phase 1/2 研究輸出
│  └─ decisions/                                   # Phase 3 ADR 決策記錄
├─ upstream/
│  └─ betrayal-at-krondor/                         # Byte-perfect recompilation 官方庫
├─ tools/                                          # 中文化工具鏈 (DDX/Font/BOK)
├─ localization/                                   # 翻譯文本與術語表 (Glossary)
├─ testdata/                                       # Synthetic 測試資料庫
└─ tests/                                          # 單元與整合測試
```

---

## 3. 遊戲資產與版本鑑定 (Asset & Version Verification)

- **資產來源路徑：** `betrayal-at-krondor/`
- **主執行檔 (`KRONDOR.EXE`)：**
  - 大小：`453,904` Bytes
  - SHA-256：`c943fd895a570224813c767d47acf44299c0aff972f1ea5f743aef303ebdd7fe`
  - MD5：`5d6e96204fe9c850838a92e2ec509f86`
  - 判定：**完全吻合 1.00 Floppy release 原版二進位。**
- **驅動覆蓋模組 (`VMCODE.OVL` / `SX.OVL`)：**
  - `VMCODE.OVL` (44,582 B): `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0`
  - `SX.OVL` (40,742 B): `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb`
  - 判定：**完全吻合 1.00 / 1.02 通用驅動。**
- **核心資料庫 (`KRONDOR.001` / `KRONDOR.RMF`)：**
  - `KRONDOR.001` (11,562,208 B): `3bae0b808423ecc3423c8edfc1482f93dd1ac2d5d09b77f8df6c53dc42445d66`
  - `KRONDOR.RMF` (14,149 B): `0d5c5655f991d4c392ddc2226c8cbd8f892cc5829f9734293e20adefb3444e2a`

---

## 4. 運行環境與執行驗證 (Runtime Environment Verification)

- **模擬器：** DOSBox-X 2026.06.02 (Visual Studio 64-bit release)
- **路徑：** `D:\ghidra_re\dosbox\bin\x64\Release\dosbox-x.exe`
- **運行狀態：** 原版遊戲資料與二進位可由 DOSBox-X 成功加載與掛載。

---

## 5. Phase 0 驗收清單核對 (Acceptance Checklist)

| 驗收項目 | 狀態 | 說明 / 證據 |
|---|---|---|
| 1. Upstream Recompilation Repo 已克隆並鎖定 Commit | **PASS** | `1fc2a69e306af1623cd22f3390a5569302059f4d` (canassa/betrayal-at-krondor) |
| 2. 本機遊戲資產雜湊比對與版本確立 | **PASS** | 完整 32 檔案雜湊已記錄在 [`version-evidence.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/baseline/version-evidence.md) |
| 3. 編譯環境與工具鏈要求深度解析 | **PASS** | 完整架構分析已記錄在 [`build-environment.md`](file:///d:/git/betrayal-at-krondor-for-zh/docs/baseline/build-environment.md) |
| 4. 嚴格遵守資產隔離與版權規範 | **PASS** | `.gitignore` 已配置，禁止將原版商業遊戲資源提交至 Git |
| 5. 零侵入與無中文化程式碼變更 | **PASS** | 未修改任何 `bak/SRC/` 原始碼，保持 Frozen Baseline |
| 6. Phase 0 三份交付文檔完成 | **PASS** | `phase0-baseline.md`, `build-environment.md`, `version-evidence.md` |

---

## 6. Gate 判定

> **Phase 0: PASS**  
> 基準已完全確立，所有邊界條件與規範均已嚴格遵守，可推進至 Phase 1（Text Rendering Reconnaissance）。
