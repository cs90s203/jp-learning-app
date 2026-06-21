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

語言偏好: 回應用繁體中文，程式碼用英文