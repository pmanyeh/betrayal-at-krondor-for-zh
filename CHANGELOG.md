# 更新紀錄

各版本的完整說明見 [`docs/release-notes/`](docs/release-notes/)。

## 未發布

### 新增
- **Mac 支援**：整合包新增 Mac 啟動腳本 `play_mac.sh`，PC／Mac 共用同一個 zip。Mac 玩家需自備 Python 3 與 Mac 版 DOSBox-X，在終端機執行 `python3 installer.py` 後再執行 `./play_mac.sh` 即可開始遊玩。腳本會先進入 `dosbox-x/` 再讀取同一份 `zh_krondor.conf`，與 Windows 的「玩遊戲.bat」共用設定。打包時腳本固定為 LF 換行，並在 zip 內標記為可執行檔。
- 整合包內的 `README_安裝說明.txt` 新增「Mac 使用者」段落；安裝程式完成時會依作業系統顯示對應的啟動方式。
- Mac 啟動方式參考 [@wesley316-Guybrush](https://github.com/wesley316-Guybrush) 在 [#1](https://github.com/pmanyeh/betrayal-at-krondor-for-zh/issues/1) 提供的腳本與說明，特此感謝。（尚待 Mac 實機測試確認。）

### 修正
- 開新遊戲或進入新章節時，自動存檔的「正在存檔…」提示不再閃爍（`1ccb836`）。
- 自動存檔完成後，「正在存檔…」提示會在下一個畫面立即消失，不必等玩家操作才重繪（`c0df3c6`）。

## v1.0.0 — 2026-09-12

首次正式發布。詳見 [`docs/release-notes/v1.0.0.md`](docs/release-notes/v1.0.0.md)。
