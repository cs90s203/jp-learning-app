# Bird Hide Learning — UI 規格書（給設計工具用）

> 用途：把這份貼給 Claude Design / 設計工具，請它在**不違反第 9 節技術限制與第 10 節不變量**的前提下，提出視覺與排版的精緻化建議。任何建議都要能套回「單一 HTML + vanilla JS/CSS」的現況。

---

## 1. 產品與品牌

- **產品**：日語學習 PWA（單一 HTML 檔），名稱 **Bird Hide Learning**，標語「靜靜地，學會日語」。
- **調性**：安靜、溫暖、低壓力（賞鳥屋＝安靜觀察、慢慢累積）。暖琥珀色系。
- **設計原則**：柔性、不喧嘩、不製造焦慮（**避免** Duolingo 式紅色警示、扣血、排行榜、斷連續懲罰）。
- **目標裝置**：手機優先（iOS Safari + Android Chrome），可「加入主畫面」當 App 用。

---

## 2. 資訊架構（5 個主頁 + 覆蓋層）

底部固定導覽列 5 分頁：**今日 / 文章 / 單字卡 / 試題 / 設定**。

覆蓋層（非分頁）：五十音表、單字複習考、難度選擇 sheet、長按詞彙面板、Tutorial 引導、開場 Splash、首次 Onboarding、開發者面板。

---

## 3. 設計 Token — 顏色

以 CSS 變數實作，**深色由 `html[data-theme="dark"]` 覆寫**。語意命名（wa=amber 主色、wt=text、wg/wy/wr=綠/黃/紅 語意色）。

| 變數 | 用途 | 日間 | 夜晚 |
|------|------|------|------|
| `--wa` | 主色（琥珀） | `#C4783A` | `#D4884A` |
| `--wa-l` | 主色淺底 | `#F0D9BE` | `#3D2410` |
| `--wa-ll` | 頁面底/頂列底 | `#FDF8F3` | `#120C04` |
| `--wa-bg` | 溫暖填充/body | `#F5EDE0` | `#1C1208` |
| `--wa-bg2` | 分隔線/邊框 | `#E8DDD0` | `#2E1E0C` |
| `--wt` | 主文字 | `#2A1A08` | `#F0E4D0` |
| `--wt2` | 次文字 | `#5A3A1A` | `#B89070` |
| `--wt3` | 提示文字 | `#9A7A5A` | `#7A5A3C` |
| `--wg / --wg-bg` | 成功/綠 | `#3A6B47` / `#D4EDDA` | `#5BAB6A` / `#0E2A18` |
| `--wy / --wy-bg` | 警告/黃 | `#8B6200` / `#FFF0CC` | `#C8A020` / `#2A2000` |
| `--wr / --wr-bg` | 危險/紅 | `#9B2617` / `#FDDDD9` | `#D05050` / `#3A1515` |

- 卡片深色實心底另用 `#1C1208`（多個元件硬寫）。
- 行動瀏覽器 UI 底色 `<meta name="theme-color">`：日間 `#FDF8F3`、夜晚 `#120C04`（切換時 JS 動態更新）。
- 深色模式同時設 `color-scheme: dark`（影響捲軸/回彈/表單預設色）。

## 3b. 設計 Token — 字體 / 圓角 / 間距 / 尺寸

- **字體**：`'Noto Sans JP', -apple-system, sans-serif`。
- **字重**：主要用 400 / 500（標題 500）。
- **字級（現況）**：頁面大標 `h1` 24px/500；區塊小標 `.section-title`；單字大字 `.vq-word` 44px；中文/意思 18–20px；提示 11–13px；內文 14–15px。
- **圓角 token**：`--r-card: 16px`、`--r-btn: 10px`、`--r-pill: 999px`。
- **版面尺寸**：`--nav-h: 68px`（底部導覽列高）、`--atb-h: 130px`（文章工具列高）、`--safe-bottom: env(safe-area-inset-bottom)`。
- 視窗高用 `100dvh`（隨 Safari 工具列縮放）。

## 4. Z-index 層級地圖（請勿打亂相對順序）

| 層 | z-index | 元件 |
|----|---------|------|
| 內容裝飾 | 0–10 | 卡片內小元素、difficulty-bar |
| 固定文章工具列 | 50 | `#article-toolbar` |
| 浮動面板/FAB | 100–400 | 詞彙面板、底部 sheet、vocab FAB |
| 五十音固定鈕 | 9000 | `#gojuuon-fixed-btn`、各頁 `?` help 鈕 |
| 設定頁 ? 鈕 | 9100 | 需高於 overlay |
| Tutorial overlay | 9200 | 引導遮罩 |
| 五十音/單字考 overlay | ~9997–9998 | 全屏覆蓋 |
| Splash | 9999 | 開場 |
| Scroll debug bar | 99999 | 開發用（標題連點 3 次） |

---

## 5. App Shell 與導覽

- `.app`：`height:100dvh; display:flex; column; overflow:hidden; background: var(--wa-ll)`。
- `.pages`：`flex:1; overflow:hidden; position:relative`。
- `.page`：`position:absolute; inset:0; overflow-y:auto; padding-bottom: nav-h + safe-bottom (+ 文章頁再加 atb-h)`。只有 `.active` 顯示。
- **底部導覽列** `.bottom-nav`：固定，5 顆 `.nav-btn`（圖示 + 文字標籤），當前頁 `.active` 變主色。順序：今日 / 文章 / 單字卡 / 試題 / 設定。
- 每頁右上角 28px 圓形 `?` help 鈕（觸發該頁 Tutorial）。文章/單字/試題頁右上另有「あ」五十音固定鈕（top:50px）。

---

## 6. 各頁面結構

### 今日頁（home）
- 頂列：`<h1>今日學習</h1>` + 日期 + **等級小標**（N5-…N1，可點往設定）。
- 區塊（皆有小標題 `.section-title`）：
  - **學習紀錄**：月曆卡 `#home-calendar-card`，有文章日期顯示圓點、五色進度環；點日期展開當日詳情（文章名、難度等級、任務狀態）。
  - **今日足跡**：`#home-dashboard` 三格數字（新學單字 / 複習單字 / 完成句子）。
  - **今日任務**：`#home-tasks-card` 中央任務環（0/5）+ 右側五項清單（文章/單字卡複習/聽力/填空+句子/跟讀）含完成度。

### 文章頁（article）
- 頂列：標題 + 等級小標（長按可切該日等級）+ 日期 + 「あ」鈕。
- 週曆列 `#article-week-bar`：近 7 天，可切日期、左箭頭回顧上週。
- 工具按鈕列 `.cn-toggle-row`（靠右）：`＋全部` / `中文` / `書寫` 三顆 `.cn-btn`。
- 文章卡：全選列（橘點 + 「全部」）+ 文章本文（furigana ruby、可長按詞彙加入單字卡、句首橘點選句）。每句下方可選擇性顯示 **中文注釋** 與 **書寫練習底線輸入框**。
- 難度量表 `#difficulty-bar`：五星評分（輕鬆←→很難）。
- **固定底部工具列** `#article-toolbar`（fixed, 高 130px）：朗讀列（播放/停止/速度）+ 跟讀列（句選/播放/停止/逐句/錄音）。

### 單字卡頁（vocab）
- 頂列：標題 + 共 N 張。
- 篩選列 `.vocab-filter-bar`：全部 / 生 / 普 / 熟（SRS 熟悉度 0–20）+ 「開始複習」鈕。
- 顯示卡 `.vocab-display-card`：上下滑切換單字，點下半揭曉中文/例句。
- 單字列表 `.vocab-list-area`：依熟悉度列出，點列跳到該卡。
- FAB 群 `.vocab-btn-group`（右下）：「Aa」羅馬拼音切換、「＋」手動新增。

### 試題頁（quiz）
- 頂列：標題 + 等級小標（長按切難度，與文章頁連動）。
- 週曆列 `#quiz-week-bar`。
- 題型 tabs `#quiz-tabs`：單字聽力 / 句子聽力 / 填空 / 句子判斷 / 句子排列。
- 主區 `#quiz-main`：開始作答 → 逐題作答（即時給分）→ 結果頁（分數 + 答錯題目 + 重新作答）。

### 設定頁（settings）
- 區塊：學習模式（輕鬆/標準/專注 = 40/75/100%）、學習強度（熟記定義門檻、單字複習排序）、**顯示**（夜晚模式三態：日間/夜晚/自動；首次說明重顯）、語言（目前等級）、跟讀設定（靜音門檻/持續時間）、帳號（Google 登入同步）、資料、進階功能（Vision API Key）、開發者面板。
- 列型樣式 `.setting-row`（label + sub + 右側控制）。

---

## 7. 覆蓋層

- **五十音表 overlay**：表格（清音/濁音/半濁音/片假名切換 chips），點格發音。右上 ✕ 關閉、? 教學。
- **單字複習考 overlay**：模式選擇（文字/聽力）→ 卡片（遮罩單字/中文，點擊揭曉）+ 進度條 + 「不記得 / 記得」兩鈕（按任一鍵直接下一張）→ 結果。右上 ✕（top:14px）。
- **難度選擇 sheet**：底部滑出，N5–N1 + lite（NX-）chips。
- **長按詞彙面板**：底部滑出，顯示讀音/意思/例句 + 加入單字卡。
- **Tutorial 引導**：見第 8 節。
- **Splash**：2.4s 開場（鳥屋 logo + 名稱 + 標語），深色模式變色，主題重載時可跳過。
- **Onboarding**：首次進入的等級選擇與介紹。

---

## 8. 元件庫（可重用樣式）

- **按鈕**：`.cn-btn`（pill 外框鈕，active 填主色）、`.nav-btn`（導覽）、`.help-btn`（28px 圓 ?）、`.vq-btn`（複習評分）、主行動鈕（開始作答/開始複習，實心主色）。
- **開關/選擇**：`.toggle`（46×28 滑塊）、`.theme-seg`（三態分段控制 pill）。
- **卡片**：`.card`（圓角 16、邊框 hairline、深色實心 `#1C1208`）。
- **標籤**：`.level-tag`（小 pill，等級）、`.badge`（生/普/熟）。
- **進度**：任務環（SVG 圓環）、`.prog-fill`（線性進度）、月曆五色進度環。
- **量表**：`.difficulty-stars`（五星）。
- **書寫行**：`.write-input`（滿版底線輸入，無填色、`border-bottom` only、`border-radius:0`）。
- **遮罩文字**：`.meaning-hidden`（`color:transparent` + 霧化 `text-shadow`；大字 `.vq-word` 用更濃的疊層 shadow）。

---

## 9.（重要）技術限制 — 任何設計都要能套回這些

1. **單一 HTML 檔、純 vanilla JS/CSS、無 build system、無框架、無 npm**。不能引入 React/Tailwind/SCSS 等；產出要能直接寫進 inline `<style>` 與 vanilla DOM。
2. **顏色一律走 CSS 變數**（見第 3 節），新增顏色請同時給日間/夜晚兩組值。
3. **相容 iOS Safari + Android Chrome**；版面用 `dvh`、`env(safe-area-inset-*)`。
4. **狀態存 localStorage / IndexedDB**（錄音）；資料同步用 Firebase。
5. 圖示偏好 inline SVG（無圖示庫）。
6. 字重只用 400 / 500。圓角用既有 token。

---

## 10.（最重要）不可破壞的 Edge Case / 不變量

> 以下都是實測踩坑後修好的；重新設計時**結構與行為必須保留**，只能改視覺表層。

1. **文章頁捲動**：`#page-article.active` 必須 `display:block`（**不可改回 flex column**）。iOS Safari 的 flex column + overflow 會在 touch reflow 時壓縮子元素導致無法捲動。短文章另靠 JS 對 `.sec` 設 `minHeight` 確保有捲動空間。
2. **固定文章工具列**：`#article-toolbar` 是 `position:fixed` 高 130px；文章頁底部 padding 必須讓出 `nav-h + safe-bottom + atb-h`，否則內容被遮。難度量表要能捲到工具列上方。
3. **主題切換（iOS）**：切換主題時直接對 `<html>`/`<body>` 設 inline `backgroundColor`（不能只改 CSS 變數），否則 overscroll 回彈區殘留前一主題色。iOS 上手動切換會**靜默重載並跳過 splash、且跳回原頁**（用 sessionStorage 旗標）。`<head>` 內有「首次繪製前」inline script 預先套主題，避免閃爍——**不可移除**。
4. **Tutorial 幾何規則**（指示框 spotlight + 說明框 tooltip）：
   - 相接的邊永遠平角、外露的邊圓角；說明框在下方/上方時整組上下反轉。
   - 小按鈕用單邊靠齊（左/右）或置中模式；指示框 6px 留白；說明框無投影。
   - tooltip 須先掛 DOM + overlay 顯示才量得到高度（否則上方定位錯位）。
   - 多功能說明用「每功能一段落」（text 支援陣列），順序依畫面排列。
   - 開啟 tutorial 時先把當前頁捲回頂端（第一步常為頂端 noScroll 小標）。
5. **等級標籤**：lite 等級前端一律顯示 `N5-/N4-/N3-/N2-/N1-`，**不可顯示後端 key `NX_LITE`**（用 `levelKeyLabel()`）。
6. **遮罩文字**：`.meaning-hidden` 系列**不可加 transition**（換卡會閃出下一張答案約 0.5 秒）。大字遮罩需夠濃到無法辨識輪廓。
7. **重疊避讓**：複習頁 ✕ 與五十音「あ」鈕都在右上——✕ 在 `top:14px`、あ 在 `top:50px`，不可再重疊。
8. **長按 / 觸控**：文章長按加詞、句首圓點選句、書寫輸入框點擊——三者不可互相誤觸；輸入框是獨立元素。
9. **Pull-to-refresh**：自製 PTR；Tutorial/overlay 開啟時需被擋住。
10. **safe-area**：底部導覽、固定工具列都要含 `env(safe-area-inset-bottom)`，iPhone 瀏海/Home 條不可遮住內容。

---

## 11. 哪些可放心重新設計 vs 結構承重

- **可自由調整（視覺表層）**：配色細節、圓角大小、字級層級、間距節奏、卡片陰影/邊框風格、按鈕造型、圖示、動效（注意第 6/10.6 遮罩例外）、空狀態插畫、月曆/環的視覺、整體精緻度。
- **承重、需保留結構**：5 分頁底部導覽、文章頁 block 佈局與固定工具列、主題三態與 CSS 變數機制、Tutorial overlay 幾何、覆蓋層的 z-index 相對順序、localStorage/Firebase 資料流。

---

## 12. 想優先精緻化的方向（給設計工具的提示）

1. 整體視覺一致性與「安靜溫暖」質感的強化（留白、層次、卡片風格）。
2. 今日頁的儀表感（環、足跡、月曆）更有「每天想打開」的吸引力，但不焦慮。
3. 規劃中的「賞鳥圖鑑」收集系統視覺（inline SVG 鳥、鎖/解鎖卡、稀有度），需與品牌一致。
4. 空狀態 / 首次使用 / 完成時刻的小巧鼓勵（柔性，非獎懲）。
5. 深色模式的精緻度檢查。

> 交付格式期望：請以「可直接轉成 inline CSS 變數 + vanilla HTML/CSS」的方式描述，並對任何新顏色給出日間/夜晚兩組值。
