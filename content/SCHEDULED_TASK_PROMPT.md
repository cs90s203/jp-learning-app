# 每日文章生成排程 Prompt

## 排程設定
- 執行時間：每天 00:30（台灣時間）
- 執行方式：Cowork Scheduled Task

---

## 任務

今天的日期是 {{TODAY}}（格式：YYYY-MM-DD）。

生成今日日語學習文章，共 10 個等級。每篇獨立完成後立即寫檔，再進行下一篇。

存檔路徑：`/Users/mick/Documents/Language/content/{{TODAY}}/`

檔名：`n5_lite.json` `n5.json` `n4_lite.json` `n4.json` `n3_lite.json` `n3.json` `n2_lite.json` `n2.json` `n1_lite.json` `n1.json`

---

## 近期已用主題（避免重複）

執行前先讀取以下檔案，取得近 7 天各等級的標題，**今天 10 篇的主題不得與清單重複**：

```
/Users/mick/Documents/Language/content/index.json
```

從 `dates` 陣列取最近 7 筆，對每筆讀取對應目錄下各等級 JSON 的 `title` 欄位，列出已用標題後再開始生成。

---

## 每篇執行步驟（依序，不可跳過）

**① 撰寫文章**（只輸出 `text` 欄位內容）

**② 靜默品質自查**（不輸出任何審閱文字，直接在心中確認）
- 句子通順自然？無語意矛盾？
- 詞彙難度符合等級？
- 有沒有更口語/自然的詞可以替換？（例：うち＞いえ、ちょっと＞少し、てる＞ている）
- 若有問題：直接修正，繼續，不說明

**③ 寫出完整 JSON 並存檔**

---

## 各等級規格

| 檔名 | 顯示 | 字數 | 文法特徵 |
|------|------|------|---------|
| n5_lite | N5⁻ | 40–60 | 高頻名詞＋です/います，無動詞變化 |
| n5 | N5 | 80–120 | 基本て形/た形、常見助詞 |
| n4_lite | N4⁻ | 100–140 | N5文法骨幹＋N4詞彙 |
| n4 | N4 | 140–180 | ～たり～たり、～ので/のに、～ことができる |
| n3_lite | N3⁻ | 160–200 | N4文法骨幹＋N3詞彙 |
| n3 | N3 | 200–250 | 逆接・引用・複合表現 |
| n2_lite | N2⁻ | 220–270 | N3文法骨幹＋N2詞彙 |
| n2 | N2 | 270–330 | 書面語、複雜接續詞 |
| n1_lite | N1⁻ | 300–360 | N2文法骨幹＋N1詞彙 |
| n1 | N1 | 360+ | 書面語、抽象論述 |

_lite 版：文法比同等級低一階，句子短 20–30%，主題可自由選擇。

**語感原則**：N4 以下優先使用口語常用詞（うち、ちょっと、てる形等）；N2 以上可引入書面語。整體語感貼近「日本人日記或朋友對話」，避免教科書腔。

---

## JSON 格式

> ⚠️ 以下為**實際可運作格式**（app 就是這樣讀的）。重點：`translations` 是「巢狀陣列 + {text, word}」（不是純字串）、有 `particles` 欄位、`tokens` 的動詞/形容詞活用**整體一個 token 不拆**。欄位齊全且照此順序。

```json
{
  "date": "{{TODAY}}",
  "level": "n4_lite",
  "title": "文章標題",
  "text": "完整日文文章",
  "tokens": [
    { "surface_form": "表層形（含活用）", "basic_form": "辭書形", "reading": "平假名", "pos": "詞性" }
  ],
  "vocab": {
    "basic_form": { "meaning": "繁體中文", "romaji": "羅馬拼音" }
  },
  "particles": {
    "は": "主題助詞，標示話題",
    "と": "表示一起行動的對象（和…一起）"
  },
  "translations": [
    [ { "text": "第一句的完整中文（可整句一段）", "word": "該段對應的 vocab basic_form" } ],
    [ { "text": "第二句前半中文，", "word": "詞A" }, { "text": "後半中文。", "word": "詞B" } ]
  ],
  "difficulty": {
    "target_vocab_rate": 0.08,
    "jlpt_level": "N4-"
  }
}
```

---

## 規則

1. **tokens**：覆蓋全文所有詞語，**略過標點符號**（。、！？等不需要 token）。**動詞・形容詞的活用形整體當「一個」token**，`basic_form` 填辭書形、`reading` 填該活用形的完整平假名。**不要拆成語幹＋助動詞**。例：
   - `行きました` → 一個 token `{ surface:"行きました", basic:"行く", reading:"いきました", pos:"動詞" }`
   - `減っている` → `{ surface:"減っている", basic:"減る", reading:"へっている", pos:"動詞" }`
   - `伝えたい` → basic `伝える`；`おいしかった` → basic `おいしい`（pos 形容詞）
   - 例外：**獨立**的助詞（は・を・に・へ・と・で・が…）與**句末單獨出現**的助動詞（です・だ・だろう・ます）各自一個 token。
2. **vocab**：收所有名詞・動詞・形容詞・副詞・接続詞・感動詞（**不收**助詞/助動詞）。key 必須與 token 的 basic_form 完全一致，value 至少含 `meaning`（繁中）與 `romaji`；`reading` 可省略（token 已有讀音）。生成後自查：掃描所有 token，確認每個名詞/動詞/形容詞/副詞的 basic_form 都有對應 vocab key。**若 content word 不在 vocab 中，App 會顯示「尚無中文翻譯」，這是錯誤。**
3. **particles**：物件，key = 文章中出現的助詞/常見助動詞（は・を・に・へ・と・で・が・から・まで・ています…），value = 該助詞的繁中用法說明。App 會把它合併進內建說明。
4. **translations**：**巢狀陣列**——最外層每個元素對應「一句」；每句是一個 `[{ "text": ..., "word": ... }]` 陣列。`text` = 該片段完整中文，`word` = 該片段要對應/高亮的日文詞 basic_form（整句可只切一段，也可切多段）。**絕不是純字串陣列。**（app 的句子測驗直接讀這個結構，格式錯會壞掉。）
5. 每天主題不同，貼近日常/文化/時事；10 篇不必同主題；所有中文說明用**繁體中文**。
6. `level` 填檔名；`difficulty.jlpt_level` 填顯示名稱（如 `N4-`）。

---

## 完成後：更新 index.json 並推上 GitHub

### 步驟一：更新 index.json

路徑：`/Users/mick/Documents/Language/content/index.json`

在 `dates` 陣列**最前面**新增：
```json
{
  "date": "{{TODAY}}",
  "levels": ["n5_lite", "n5", "n4_lite", "n4", "n3_lite", "n3", "n2_lite", "n2", "n1_lite", "n1"],
  "generated_at": "{{TODAY}}T00:30:00Z"
}
```

### 步驟二：git commit & push

```bash
cd /Users/mick/Documents/Language
git add content/{{TODAY}}/ content/index.json
git commit -m "content: {{TODAY}} 日語學習文章（10篇）"
git push
```
