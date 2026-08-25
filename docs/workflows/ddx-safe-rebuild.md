# DDX 安全全量重建流程

此流程把 DDX 的指標錯誤提前到建置階段攔下，避免錯誤的 choice 目標位址在遊戲內演變成 `MEM:34 (Heap Corrupt!)`。

## 一次性準備原始檔

從同一份遊戲安裝的 `krondor.rmf` / `krondor.001` 擷取全部原始 `DIAL_*.DDX`：

```powershell
python .\tools\text\ddx_extract_pristine.py
```

檔案會放到 `scratchpad/pristine/`，不會修改遊戲安裝目錄。若既有同名檔案和封存檔內容不同，工具會拒絕混用不同版本的遊戲資料。

## 每次翻譯批次完成後

```powershell
python .\tools\text\ddx_rebuild_all.py `
  --manifest .\dist\test_v100_zh\DDX_BUILD_MANIFEST.json
```

此指令會：

1. 確認每個 `localization/translated/DIAL_*.json` 都有對應的原始 DDX；少一個就停止，絕不做部分重建。
2. 驗證原始 DDX 的目錄位址與 choice 子記錄位址都指向合法記錄邊界。
3. 在暫存目錄全數建立本地化 DDX，逐一再次驗證。
4. 全部成功後才把輸出更新到 `dist/test_v100_zh/`，並寫出 SHA-256 manifest。

單一檔案的舊指令 `ddx_translate.py build` 也已自動執行輸入與輸出結構驗證；但日常測試或發佈請優先使用全量指令。

## 只檢查結構

```powershell
python .\tools\text\ddx_validate.py .\dist\test_v100_zh\DIAL_Z00.DDX
```

驗證器檢查 DDX 解析完整性、directory entry，以及每個 bit 31 未設的本檔 choice target。bit 31 已設的值是合法的全域／鍵值目標（例如 `0x800000c4`），不是本檔位址。它也不會把 `DdxOp.nA3` 當作位址，因為該欄位是一般 opcode operand。
