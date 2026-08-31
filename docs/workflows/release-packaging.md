# 發布「免安裝整合包」流程

把翻譯／引擎異動組成 `dist/release_v100_zh/`（可直接發布的整合包資料夾＋對應 `.zip`）。所有指令從 repo 根目錄執行。

## 什麼時候要重新出包

- **翻譯或 `dist/test_v100_zh/` 資源檔有更動**（DDX/BOK/DAT/字型…）→ 只要重跑 `package_release.py`。
- **`krondor.exe` 重編過**（引擎原始碼改動、`bak build` 產生新 exe）→ 先重跑 `build_exe_patch.py`，再跑 `package_release.py`。
- **`tools/release/starter_save_base/` 底下的基準存檔有換**（金幣基準檔、玩家自己新的遊玩進度）→ 先重跑 `build_starter_save.py`，再跑 `package_release.py`。
- **DOSBox-X／可嵌入版 Python 的固定版本要升級** → 改 `vendor_dosboxx.py`／`vendor_python_embed.py` 裡的版本號＋雜湊常數，重跑對應腳本，再跑 `package_release.py`。這兩支腳本的輸出有快取（`dist/_vendor_cache/`），版本沒變的話不用重跑。

**只有 `package_release.py` 是每次出包都一定要跑的**；其餘幾支只在對應的來源真的變了才需要重跑，因為它們的輸出（`exe_patch/`、`dosbox-x/`、`python-embed/`、`starter_save/`）都是 `package_release.py` 直接讀取、不會自己重算。

## 標準流程

```powershell
# 只有 krondor.exe 重編過才需要這行
python .\tools\release\build_exe_patch.py

# 只有 starter_save_base/ 換了基準存檔才需要這行
python .\tools\release\build_starter_save.py

# 第一次設定環境，或要升級固定版本才需要這兩行（有快取，重跑很快）
python .\tools\release\vendor_dosboxx.py
python .\tools\release\vendor_python_embed.py

# 每次出包都要跑
python .\tools\release\package_release.py
```

`package_release.py` 會依序：

1. 依 `dist/test_v100_zh/` 的各個 `*_BUILD_MANIFEST.json` 收錄已翻譯資源檔到 `resources/`，逐檔核對雜湊，過期或缺檔直接中止。
2. 從 `localization/generated/zh_mapping.json` 產生 `STARTUP.GAM` 隊伍姓名 patch data（`gam_patch/character_names.json`）。
3. 複製 `installer.py`／`bspatch_apply.py`，並用 CRLF 重新寫出兩個 `.bat` 啟動器（`cmd.exe` 對 LF 換行很敏感，見下方「已知地雷」）。
4. 建立空的 `game_data/`（附說明檔）＋複製 `starter_save/GAMES/Plus.G01/` 整包存檔點進去。
5. 確認 `dosbox-x/`／`python-embed/` 都在，並把 `dosbox_krondor.conf.template` 重新寫進 `dosbox-x/zh_krondor.conf`（這支設定檔沒有快取，每次都是新的，不會有改了 template 卻沒生效的問題）。
6. 寫 `README_安裝說明.txt`。
7. **安全檢查**：確認 `game_data/` 除了說明檔跟 `Plus.G01/` 存檔點以外沒有別的檔案——防止本機測試時不小心把真的遊戲資料留在裡面、被一起打包發布出去。檢查沒過會直接中止、不出 zip。
8. 打包成 `dist/release_v100_zh.zip`。

## 驗證

```powershell
python -m unittest discover -s tests/unit -v
```

**手動端到端測試**（強烈建議每次出包後至少跑一次）：複製一份 `dist/release_v100_zh/` 到別的資料夾（不要污染 repo 裡這份），把一份乾淨的原版 v1.00 遊戲資料複製到那份複本的 `game_data/`，跑「安裝中文化.bat」，確認：

- 裝出來的 `krondor.exe` 雜湊跟 `dist/test_v100_zh/krondor.exe` 一致。
- 「玩遊戲.bat」能正常叫出 DOSBox-X、沒有設定值警告。
- `--uninstall` 能正確還原。

## 已知地雷（都已經修過，但改動這一帶時要留意）

- `.bat` 檔一定要是 CRLF，純 LF 會被 `cmd.exe` 解析器打散成奇怪的指令片段。
- 批次檔裡呼叫執行檔要用明確路徑（例如 `.\dosbox-x.exe`），不要靠「目前目錄」隱含搜尋——有些 Windows 機器會關掉這個行為（`NoDefaultCurrentDirectoryInExePath`）。
- `vendor_dosboxx.py`／`vendor_python_embed.py` 的輸出有快取，改了 `dosbox_krondor.conf.template` 之後**不會**自動反映到已快取的 `dosbox-x/` 輸出——這就是為什麼 `zh_krondor.conf` 改成由 `package_release.py` 每次重寫，而不是放在 `vendor_dosboxx.py` 裡。
- `game_data/` 的安全檢查白名單目前認得「說明檔」＋整個 `GAMES/Plus.G01/` 資料夾；之後如果 starter save 的路徑結構再變，記得同步改 `package_release.py` 的 `check_game_data_is_empty()`。
