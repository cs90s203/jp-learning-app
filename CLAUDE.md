這是一個日語學習 PWA 專案（單一 HTML 架構）。

主檔案: Released/jp_learning_mvp.html（約 2000 行，單一 HTML/CSS/JS，無 build system）
測試 URL: https://cs90s203.github.io/jp-learning-app/Released/jp_learning_mvp.html
CHANGELOG: Released/CHANGELOG.md

技術限制:
- 不使用任何框架或 npm — 所有程式碼必須是 vanilla JS/HTML/CSS
- localStorage 儲存 SRS 資料（addedWords map，familiarity 0–20）
- IndexedDB 儲存錄音（shadowing recorder）
- 相容 iOS Safari + Chrome

目前完成: 文章頁（furigana/CN gloss/TTS）、長按詞彙面板、首頁任務環、跟讀錄音
尚未完成: 內容套件系統（文章資料仍 hardcoded）、單字卡/測驗頁尚未接真實資料

Deploy 流程: 開發完成後請提醒我執行 deploy.sh，再由我 git push。
版本規則: bug fix = 末位數；新功能完成 = 中位數；每次 deploy 同步更新設定頁版本號文字。

語言偏好: 回應用繁體中文，程式碼用英文

---

## 對話模板（加快溝通，節省 token）

使用者用以下格式提需求時，Claude 直接照格式理解並執行，不需要再追問。

### 【UI調整】
```
【UI調整】頁面 > 元件
問題：___
目標：___
參考值：___（可選，例如 r=4→3）
```

### 【文案】
```
【文案】頁面/區塊
舊：___
新：___
備註：___（可選）
```

### 【Bug】
```
【Bug】功能名稱
裝置：___
步驟：___
預期：___
實際：___
截圖/alert：___
```

### 【功能】
```
【功能】名稱
目的：___
入口：___
行為：___
資料：___（localStorage key 或 Firestore）
版本類型：patch / minor
```

### Claude 每次完成後輸出
- CHANGELOG 草稿（已寫入檔案）
- `bash deploy.sh VERSION "description"` 供使用者複製執行