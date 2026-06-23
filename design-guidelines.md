# 日語學習 App — 設計準則

版本：1.0 · 2026-06-21  
適用檔案：`Released/jp_learning_mvp.html`

---

## 設計原則

1. **溫暖專注**：米色暖調底色，減少藍光刺激，適合長時間閱讀。
2. **極簡層次**：三層文字濃度（主文字 / 次要 / 說明），卡片不超過兩層嵌套。
3. **一致圓角**：所有元件都由三個 token 組成，不出現隨意數值。
4. **拇指友好**：最小可點區域 44×44px，底部操作優先（iOS HIG 原則）。
5. **漸進揭示**：次要資訊預設收合（中文備注、刪除按鈕），互動後才展開。

---

## 設計 Token

### 圓角（Border Radius）

| Token | 值 | 適用 |
|---|---|---|
| `--r-card` | `16px` | 卡片、面板、底部 sheet |
| `--r-btn` | `10px` | 標準按鈕、輸入框 |
| `--r-pill` | `999px` | Badge、Tag、Toggle、膠囊按鈕 |

> Word Panel 頂部圓角為 `20px`（底部 sheet 規格，保留獨立值）

### 字型尺寸

| 用途 | 大小 | 字重 |
|---|---|---|
| 頁面標題（top-bar h1） | 24px | 500 |
| 卡片標題 / 文章文字 | 16px | 400–500 |
| 單字大字（vocab display） | 36–40px | 500 |
| 正文 / 按鈕文字 | 15px | 400 |
| 說明 / 標籤 / badge | 12px | 400 |
| 微型標注（furigana, hint） | 11px | 400 |

### 間距

| 名稱 | 值 | 用途 |
|---|---|---|
| 頁面水平邊距 | 16px | `.sec` padding |
| 元件間距 | 12px | 卡片之間 |
| 卡片內邊距 | 16px | `.card` padding |
| 列高（list row） | min 44px | 符合觸控最小高度 |
| 分隔線 | 0.5px | `var(--wa-bg2)` |

---

## 色彩系統

### 日間模式（Light Mode）

```css
:root {
  /* Primary Amber */
  --wa:    #C4783A;   /* 主強調色：可點按元素、進度、選中狀態 */
  --wa-l:  #F0D9BE;   /* 淡橘：hover 背景、輕量高亮 */
  --wa-ll: #FDF8F3;   /* 頁面底色（幾乎白） */
  --wa-bg: #F5EDE0;   /* 區塊底色（米黃） */
  --wa-bg2:#E8DDD0;   /* 分隔線、邊框 */

  /* Text */
  --wt:    #2A1A08;   /* 主文字（深棕） */
  --wt2:   #5A3A1A;   /* 次要文字 */
  --wt3:   #9A7A5A;   /* 說明文字、disabled */

  /* Semantic */
  --wg:    #3A6B47;   /* 成功 / 熟悉 / 完成 */
  --wg-bg: #D4EDDA;
  --wy:    #8B6200;   /* 警告 / 普通熟悉度 */
  --wy-bg: #FFF0CC;
  --wr:    #9B2617;   /* 錯誤 / 危險 / 刪除 */
  --wr-bg: #FDDDD9;
}
```

**用途對照表**

| 情境 | 使用色 |
|---|---|
| 主按鈕、進度條、選取點 | `--wa` |
| 頁面背景 | `--wa-ll` |
| 卡片底色 | `#FFFFFF`（白）|
| 區塊 / top-bar 底色 | `--wa-bg` |
| 邊框 / 分隔線 | `--wa-bg2` |
| 主文字 | `--wt` |
| 次要文字（副標、標籤） | `--wt2` |
| 說明 / placeholder | `--wt3` |
| 完成 / 熟悉 badge | `--wg` on `--wg-bg` |
| 普通 badge | `--wy` on `--wy-bg` |
| 刪除 / 危險 | `--wr` on `--wr-bg` |

---

### 夜晚模式（Dark Mode）

```css
[data-theme="dark"] {
  /* Primary Amber（深色背景上略提亮） */
  --wa:    #D4884A;
  --wa-l:  #3D2410;
  --wa-ll: #120C04;   /* 頁面底色（極深暖黑） */
  --wa-bg: #1C1208;   /* 區塊底色 */
  --wa-bg2:#2E1E0C;   /* 分隔線、邊框 */

  /* Text */
  --wt:    #F0E4D0;   /* 主文字（暖白） */
  --wt2:   #B89070;   /* 次要文字 */
  --wt3:   #7A5A3C;   /* 說明 / disabled */

  /* Semantic */
  --wg:    #5BAB6A;
  --wg-bg: #0E2A18;
  --wy:    #C8A020;
  --wy-bg: #2A2000;
  --wr:    #D05050;
  --wr-bg: #3A1515;
}
```

**日 / 夜對照**

| 角色 | Light | Dark |
|---|---|---|
| 頁面底色 | `#FDF8F3` | `#120C04` |
| 卡片 | `#FFFFFF` | `#1C1208` |
| 區塊底 | `#F5EDE0` | `#1C1208` |
| 邊框 | `#E8DDD0` | `#2E1E0C` |
| 主文字 | `#2A1A08` | `#F0E4D0` |
| 次要文字 | `#5A3A1A` | `#B89070` |
| 說明文字 | `#9A7A5A` | `#7A5A3C` |
| 主強調 | `#C4783A` | `#D4884A` |

> 切換方式：在 `<html>` 或 `.app` 加 `data-theme="dark"`，CSS 變數自動覆寫。

---

## 元件規範

### 按鈕（Button）

| 類型 | 背景 | 文字 | 邊框 | 圓角 |
|---|---|---|---|---|
| Primary | `--wa` | `#FFF` | 無 | `--r-btn` |
| Secondary | 透明 | `--wa` | 1px `--wa` | `--r-btn` |
| Ghost | 透明 | `--wt2` | 1px `--wa-bg2` | `--r-btn` |
| Danger | `--wr` | `#FFF` | 無 | `--r-btn` |
| Icon btn（圓形） | `--wa-bg` | `--wt` | 無 | `--r-pill` |
| Disabled | 任意 × 0.4 opacity | — | — | 繼承 |

最小高度：44px（行動端）。

### 卡片（Card）

```
背景：#FFFFFF（Light）/ #1C1208（Dark）
邊框：0.5px solid var(--wa-bg2)
圓角：var(--r-card)  → 16px
內距：16px
下距：12px
```

### Badge / Tag

```
圓角：var(--r-pill)
字號：12px
內距：3px 8px
```

| 類型 | 背景 | 文字 |
|---|---|---|
| 生（raw） | `--wr-bg` | `--wr` |
| 普（mid） | `--wy-bg` | `--wy` |
| 熟（ripe） | `--wg-bg` | `--wg` |
| Level tag (N5…) | `--wa-bg` | `--wt2` |

### Toggle

```
圓角：var(--r-pill)
尺寸：44×26px
開：背景 var(--wa)，圓鈕右移
關：背景 var(--wa-bg2)，圓鈕左移
```

### 工具列（av-bar）

```
背景：var(--wa-ll)
上邊框：0.5px solid var(--wa-bg2)
內距：12px 16px
高度：朗讀 ~52px／跟讀 ~80px
圓角：無（全寬貼邊）
```

### 底部面板（Word Panel / Sheet）

```
背景：var(--wa-ll)
頂部圓角：20px（固定，非 token）
Handle：4×36px，var(--wa-bg2)，圓角 2px
z-index：200
```

### 分隔線

```
高度：0.5px
顏色：var(--wa-bg2)
```

---

## 深色模式實作指引

1. 在 CSS `:root` 之後加入 `[data-theme="dark"] { ... }` 覆寫所有變數。
2. 在 `<html>` 加 `data-theme` 屬性控制切換：
   ```js
   document.documentElement.dataset.theme = 'dark'; // 開啟
   delete document.documentElement.dataset.theme;   // 還原
   ```
3. 偵測系統偏好（選用）：
   ```js
   if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
     document.documentElement.dataset.theme = 'dark';
   }
   ```
4. 使用者偏好存 localStorage：`localStorage.setItem('theme', 'dark')`。
5. 所有顏色都已用 CSS 變數，切換後**不需要改任何元件的 class**。
6. 圖示（SVG）用 `stroke="currentColor"` 或 `fill="currentColor"`，會自動繼承文字色。

---

## 待辦（尚未套用）

- [ ] 設定頁加入「夜晚模式」開關
- [ ] `[data-theme="dark"]` CSS block 加入主 HTML
- [ ] 全 app `.card` border-radius 統一為 `var(--r-card)`（目前部分為 18px）
- [ ] 全 app button border-radius 統一為 `var(--r-btn)`
- [ ] 首頁任務環 SVG 在深色模式下調整底色
