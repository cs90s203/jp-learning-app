# 每日文章生成排程 Prompt

## 排程設定
- 執行時間：每天 00:30（台灣時間）
- 執行方式：Cowork Scheduled Task

---

## Prompt 內容

今天的日期是 {{TODAY}}（格式：YYYY-MM-DD）。

請幫我生成今日的日語學習文章，共 5 個等級，每篇都要符合以下 JSON 格式，並存到：
`/Users/mick/Documents/Language/content/{{TODAY}}/` 資料夾，檔名分別為：
- `n5_below.json`
- `n5.json`
- `n4.json`
- `n3.json`
- `n2n1.json`

---

## 各等級規格

| 等級 | JLPT | 文章長度 | 生字率 | 文法特徵 |
|------|------|---------|--------|---------|
| n5_below | N5以下 | 40–70字 | 約5% | 簡單名詞＋です/います，無複雜文法 |
| n5 | N5 | 80–120字 | 約8% | 基本動詞變化、て形、簡單時態 |
| n4 | N4 | 120–180字 | 約10% | ～たり～たり、～ので、～ことができる |
| n3 | N3 | 180–250字 | 約12% | 逆接、引用、複合表現、やや抽象話題 |
| n2n1 | N2/N1 | 250字以上 | 約15% | 書面語、複雜接續詞、社會/時事議題 |

---

## JSON 格式（每個檔案都要符合）

```json
{
  "date": "{{TODAY}}",
  "level": "n4",
  "title": "文章標題",
  "text": "完整日文文章文字",

  "tokens": [
    { "surface_form": "表層形", "basic_form": "基本形", "reading": "平假名讀音", "pos": "詞性" }
  ],

  "vocab": {
    "基本形": { "meaning": "繁體中文意思", "romaji": "羅馬拼音" }
  },

  "particles": {
    "助詞": "繁體中文文法說明（一句話）"
  },

  "translations": [
    [
      { "text": "中文翻譯片段", "word": "對應日文basic_form或null" }
    ]
  ],

  "difficulty": {
    "target_vocab_rate": 0.10,
    "jlpt_level": "N4"
  }
}
```

---

## 注意事項

1. **tokens** 必須完整覆蓋全文，標點符號也要包含（pos 為「記号」）
2. **vocab** 必須收錄所有 tokens 中 pos 為名詞・動詞・形容詞・副詞的詞（含常見詞，不可遺漏）。助詞和助動詞不收。**若某個 token 不在 vocab 中，App 會無法顯示該詞的說明。**
3. **particles** 收錄文章中出現的所有助詞及助動詞，用繁體中文簡短說明
4. **translations** 按句子分組，每個句子一個陣列，逐詞片段對應（`word` 填 basic_form，無對應填 null）
5. 文章主題每天不同，盡量貼近日常生活、文化或時事
6. 所有中文說明使用**繁體中文**

生成完 5 個 JSON 檔後，請更新 `/Users/mick/Documents/Language/content/index.json`，在 `dates` 陣列中新增今日記錄：
```json
{
  "date": "{{TODAY}}",
  "levels": ["n5_below", "n5", "n4", "n3", "n2n1"],
  "generated_at": "{{TODAY}}T00:30:00Z"
}
```
