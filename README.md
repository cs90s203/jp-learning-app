# Bird Hide Learning｜靜靜地，學會日語

日語閱讀練習 App，給繁體中文使用者用的。核心是每天一篇分級文章，帶 furigana 標音、長按查單字、中文對照、跟讀錄音，JLPT 分十個等級（N5⁻ 到 N1），從完全新手到高階都有對應難度的內容可以讀。

正式站：https://cs90s203.github.io/jp-learning-app/

## 技術棧

單一 HTML 檔案（`Released/jp_learning_mvp.html`），不用任何框架，vanilla JS/CSS/HTML。資料用 localStorage 存單字卡、學習紀錄；IndexedDB 存跟讀錄音。可選登入 Firebase 做跨裝置同步，不登入純本機也能完整使用。

## 內容怎麼來的

每天的 10 篇文章（10 個等級各一篇）是排程自動生成的，生成後跑一輪格式/品質檢查再上線，不是手動寫的。

## 目錄

- `Released/jp_learning_mvp.html` — App 本體，目前正式在跑的版本
- `Released/CHANGELOG.md` — 版本記錄
- `content/` — 每日文章資料（依日期分資料夾），JSON 格式
- `index.html` — 網站首頁（連到 App 本體）
