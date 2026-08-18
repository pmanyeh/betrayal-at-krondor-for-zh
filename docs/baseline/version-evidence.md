# Betrayal at Krondor — Version & Asset Evidence (Phase 0)

## 1. 概述 (Overview)

本文件依據 [`Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md`](file:///d:/git/betrayal-at-krondor-for-zh/Betrayal_at_Krondor_Traditional_Chinese_PROJECT_PLAN.md) 第 6 節與第 25 節要求，對本機現有遊戲資料檔案與上游 Recompilation 專案所定義之版本特徵進行雜湊比對與版本鑑定。

---

## 2. 本機遊戲檔案完整雜湊清單 (Local Asset Hash Inventory)

目錄路徑：`betrayal-at-krondor/`（未納入 Git 版控，符合資產分離與版權保護規範）

| 檔案名稱 | 檔案大小 (Bytes) | MD5 雜湊值 | SHA-256 雜湊值 | 檔案說明 |
|---|---|---|---|---|
| `adl.drv` | 107 | `e156febd28f92706b4ffe6fa8d541d25` | `577910f0380aef1d8f592dc03101a78764265708c29045f0124c98e56a5dea6d` | AdLib 音效驅動設定 |
| `antara.bmp` | 525,368 | `c131e4c84cc173558d3dfeb10bfec1fd` | `30c5418c83b1ebdac45fc7938b6bf4c95724e315e7fd39a9ecbc7a31f9ec0318` | 宣傳/啟動點陣圖 |
| `bakplay.wri` | 1,791,744 | `a85e869ba53ca003702b6ea2d1ad3531` | `cce399d26b9d99c882aa2db04b5d4a7b14664db1a0bf0f5bd2acf31917ef3b6b` | 遊戲手冊文字檔 |
| `bakts.wri` | 652,928 | `e7954d118848b7bb2335698f26826e29` | `6dab5af071552696005a54ffe0833220f236a4535df467e1c6ef394d10a4a9de` | 技術支援說明檔 |
| `frp.sx` | 1,486,774 | `16990eba5e4c00fc459f46b25f4e7844` | `2861d2487079a8e0ed6e933a45721e5ed8b0a4d42498497497ab8cd05c90fab8` | 遊戲音效/音樂資料包 |
| `genmidi.drv` | 116 | `b8525cf2809e165c0812b594496ecdde` | `0e7623a0f0a47e5ebfcb026093494354608bc641c11fd36306dc0380740cd8e3` | General MIDI 驅動設定 |
| `install.exe` | 76,230 | `02b412c30a9db2565dd9e56537dc390d` | `473b22c5b9bea5767279259e86270ea3677b8e3fda5c6278b7bad330ce47abf1` | 安裝程式 |
| `install.hlp` | 17,555 | `6f7f08c4e82a98338b56345c6750b45f` | `617793cbbb1df6809b04d66cdaf5789283d34064abfbcc7b1dd984e73501726f` | 安裝說明檔 |
| `install.scr` | 3,536 | `08e6c1cc6fa7437dc1ee31b14eca6cba` | `665c2a248cf1fd24be469287880c4cd2d402dd2fe2845e3b22a8a42c550aadd5` | 安裝腳本 |
| `install.txt` | 9,436 | `22e161e732063961ea9ed4329502400f` | `7cb0f4bf5f66c237c53d8aba41aef1c587d066508da84d11d5022e9d0d08b8ef` | 安裝文字說明 |
| `intro` | 296 | `3df83690800c499e1cd297cfc9a72ede` | `9e19a1e1e2dcd7fc42fa8c14af42de7ba38d9e821ee5f8a923fba42b163325f0` | 開頭設定檔 |
| **`krondor.001`** | **11,562,208** | `eea645b06fd72d9765735a612a061b56` | `3bae0b808423ecc3423c8edfc1482f93dd1ac2d5d09b77f8df6c53dc42445d66` | **核心資產庫 (Primary Resource Archive)** |
| **`krondor.exe`** | **453,904** | `5d6e96204fe9c850838a92e2ec509f86` | `c943fd895a570224813c767d47acf44299c0aff972f1ea5f743aef303ebdd7fe` | **主執行檔 (Main Executable)** |
| **`krondor.rmf`** | **14,149** | `f8ec565df6ec5ccf1edff586a06c450b` | `0d5c5655f991d4c392ddc2226c8cbd8f892cc5829f9734293e20adefb3444e2a` | **資源目錄清單 (Resource Master File)** |
| `language.inf` | 2,518 | `976b41a506e6dc9791870849bdd23bd6` | `8f00da1a5ff7c108bceeebd233e865314c7caa5d540965b54442d7b815f54a98` | 語言定義資訊 |
| `mem.dat` | 4 | `79c905fc9df57630eac93078bcc781c0` | `5f1c92189aa148bcbec742dce5a46818c7d1e2949337aa85970c5c4f251c8eff` | 記憶體設定檔 |
| `mt32.drv` | 109 | `a1e032df550dc32c10476a477ff08510` | `7d1cfa4e4a676b148d761d89a37dff64fb9c28193d1082051f7595724c4e1b21` | Roland MT-32 驅動設定 |
| `readme` | 8,846 | `f74e57b8578eb58e1eb94e90ab3258c1` | `6c98f263e81721f8a0c280359556b60a8b13d041dfd74c4b536060be9468b573` | 讀我檔案 |
| `readme.bat` | 19 | `854ad148e3ecd1cf0856ac34ba0c4012` | `f0324fe23bf0d7daf67c6c915b43160910601544af4477a72473c31849f16f48` | 讀我批次檔 |
| `readme.wri` | 532,992 | `ee48e705a0cee84a1ad4511083ee1483` | `58784cc9e10a3f2ec15a8dbe2bb7242787551415845eb012dd8d310c51f168df` | 讀我文件檔 |
| `resource.cfg` | 139 | `e4821e8ce7847ecdc3d3247ce6a4f6cf` | `fe820f527c047108e013242171a11f9990414dd825fe1f0a636607ec97cfcd29` | 引擎資源設定檔 |
| `setup.exe` | 32,592 | `a2cb3c91bb846de643871fb897b0ad3a` | `51f3ea06024d54734eef19344a2b79b89db78e73b68fc951fb3643b04a921e1c` | 設定程式 |
| `setup.gid` | 8,628 | `da4c915b6383c250c5eda39db9c093af` | `0178fdf932fa4149ae948edebcb872acab2aa246f7224e5114d3cbd76d527520` | 設定索引快取 |
| `setup.hlp` | 213,005 | `8a568fe0c2f92383c77bb8311086194f` | `49120dd2f7743ecc830914218482a6e8b02f34c4d2414e687125ad215065a100` | 設定說明檔 |
| `setup.sol` | 981,603 | `82e7b63d5aee7b2083420b8037d44f33` | `31e04f4ce86ae09156cce0933ed6b92c797ba1a809506c5b6ac93d0e88079751` | 設定資料檔 |
| `sierra.inf` | 2,693 | `703f3134be24bfdd12a6dfe1315de029` | `c2ad50c652e16274c9c222396158b66113d81c702f763eccae295fcb5fc43d8b` | Sierra 發行資訊 |
| `sndblast.drv` | 97 | `33fd2158eebc211b91ccbc4b68d4cab4` | `35385c10d597b217c992fd2b9872ba0cc811c48e43409602511c66d149e3bea7` | Sound Blaster 驅動設定 |
| **`startup.gam`** | **334,605** | `0bf05915f21a413fad59a1ebfa5af64c` | `b587c74b8a9f00a8b5bf5a382287319120c1958f26282dbc547bb199157bf8c2` | **初始遊戲存檔/狀態檔** |
| `std.drv` | 118 | `72b63c9f75ed156abf5f6fcf417d1a57` | `5cfac6b002a2fe086aceac380fa26161d39a774dcf169255255fd034ec1030e7` | 標準揚聲器驅動設定 |
| **`sx.ovl`** | **40,742** | `e0a222c89cdcae54838faf6670d77bd8` | `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb` | **音訊驅動覆蓋模組 (Sound Driver Overlay)** |
| `unbkron.com` | 1,004 | `b5d3deb9b45fd666cb1cab7b922ba818` | `0d543cecbbf13f334043a433af5eeb8d648654d3ad1a8ccc3f68f172b6df934f` | 解壓縮/輔助工具 |
| **`vmcode.ovl`** | **44,582** | `58a0bcdca22e36902b89506b661583a5` | `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0` | **視訊驅動覆蓋模組 (Video Driver Overlay)** |

---

## 3. 上游 Target 與版本精確比對 (Version Comparison)

上游 Recompilation 專案（`canassa/betrayal-at-krondor`）定義之驗證基準如下：

### 3.1 版本 1.00 (Floppy — June 16, 1993)
- `KRONDOR.EXE`: 大小 `453,904` Bytes | SHA-256 `c943fd895a570224813c767d47acf44299c0aff972f1ea5f743aef303ebdd7fe`
- `VMCODE.OVL`: 大小 `44,582` Bytes | SHA-256 `cd0cf73df9b11b7f70aa2036c813a64a8178ba60d24f9bbe548155c3e56237e0`
- `SX.OVL`: 大小 `40,742` Bytes | SHA-256 `d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb`

### 3.2 版本 1.02 (CD-ROM — March 21, 1994)
- `KRONDOR.EXE`: 大小 `456,048` Bytes | SHA-256 `e254770143e003dbac55b739e9efddfe84a70cbc5a8186f1bf79f38386056a59`
- `VMCODE.OVL`: 大小 `44,582` Bytes | 與 1.00 完全相同（Byte-Identical）
- `SX.OVL`: 大小 `40,742` Bytes | 與 1.00 完全相同（Byte-Identical）

---

## 4. 比對結論與發現 (Findings & Conclusion)

1. **二進位吻合度：**
   - 本機現有 `betrayal-at-krondor/krondor.exe` 的 SHA-256 為 `c943fd895a570224813c767d47acf44299c0aff972f1ea5f743aef303ebdd7fe`，**100% 吻合原版 1.00 Floppy release**。
   - 本機現有 `sx.ovl` 與 `vmcode.ovl` 雜湊值與 upstream 預期 **完全吻合**。
2. **版本架構說明：**
   - 上游 recompilation 專案同一套 source tree 透過 `#ifdef V102CD` 同時支援 1.00 與 1.02。
   - 1.02 CD-ROM 主程式相較於 1.00，僅為 30 個 C 翻譯單元重新帶入 `-DV102CD` 編譯並連結全新常駐 MSCDEX CD-Audio 驅動（`CDAUDIO.ASM`）。
   - 外部資料庫 `KRONDOR.001`、`KRONDOR.RMF` 以及驅動覆蓋模組 `VMCODE.OVL` / `SX.OVL` 在 1.00 與 1.02 間完全相容與共用。
