# 中文化引擎補丁

此目錄把本專案對 [`canassa/betrayal-at-krondor`](https://github.com/canassa/betrayal-at-krondor) 還原引擎所做的中文化修改，保存成可在目前主專案中追蹤、推送及重建的補丁。

## 固定版本

- 上游基準提交：`1fc2a69e306af1623cd22f3390a5569302059f4d`
- 本專案最終本機引擎提交：`65c7985569e82ce7913dd9c1d93a07638f02704d`
- 套用後預期 Git tree：`dd11fd90088e3cb67ae0146a94233e7473f445dc`
- 補丁 SHA-256：`8e4c7fc29ab215a7878b3bada0d96a674fa81ee609d097aea2407bacfbd76f91`

`betrayal-at-krondor-zh.patch` 是由上述兩個提交之間的已提交內容，以 `git diff --binary --full-index` 產生的合併補丁。它涵蓋 28 個原始碼檔；不包含遊戲資產、編譯產物，也不包含本機工作樹尚未提交的 VESA／EVG 實驗。

`commits.txt` 依時間順序記錄這段範圍的 79 個本機提交，方便回查每項修改的目的。合併補丁本身不會在目標 clone 重建這 79 筆提交歷史，只會重建相同的最終檔案內容。

## 套用

在乾淨的上游 clone 執行：

```console
git checkout --detach 1fc2a69e306af1623cd22f3390a5569302059f4d
git apply --check /path/to/betrayal-at-krondor-zh.patch
git apply --index /path/to/betrayal-at-krondor-zh.patch
git diff --cached --check
git write-tree
```

最後一行應輸出：

```text
dd11fd90088e3cb67ae0146a94233e7473f445dc
```

這代表套用結果與本專案最終引擎提交的 tree 完全一致。之後可自行建立本地提交，再依 [`HANDOFF.md`](../HANDOFF.md) 的 Borland／WSL 流程編譯。

## 更新補丁

只有在新的引擎修改已提交、實機驗收完成，且確定不含其他工作樹實驗時才更新。從本專案根目錄執行：

```console
git -C upstream/betrayal-at-krondor diff --binary --full-index --no-ext-diff 1fc2a69e306af1623cd22f3390a5569302059f4d..NEW_HEAD --output=engine-patches/betrayal-at-krondor-zh.patch
git -C upstream/betrayal-at-krondor log --reverse --format="%H %s" --output=engine-patches/commits.txt 1fc2a69e306af1623cd22f3390a5569302059f4d..NEW_HEAD
```

更新後必須同步修改本文件的最終提交、tree hash 與補丁 SHA-256，並重新在乾淨基準 worktree 執行一次套用驗證。

## 上游規則

**不得向 `canassa/betrayal-at-krondor` push，也不要嘗試 push。** 該倉庫只作為還原引擎來源與比對基準。中文化引擎修改透過此目錄保存在本專案；若日後要保存完整引擎提交歷史，必須使用使用者明確指定的個人 fork 或其他遠端。
