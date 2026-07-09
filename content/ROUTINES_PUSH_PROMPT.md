# Routines: Daily Content Validation & Push

你是在使用者本機自動執行的排程，負責驗證今日日語學習文章品質並推上 GitHub。
全程用繁體中文。這是獨立 session，無記憶，每次重新讀取所需資訊。

---

## 步驟 0：冪等檢查

確認今天本地日期 TODAY（YYYY-MM-DD，用 `date +%Y-%m-%d` 取得）。

```bash
cd /Users/mick/Documents/Projects/Language
```

- 若 `content/TODAY/.pushed` 已存在 → 今天已成功 push，直接結束，輸出「✅ 今天已 push，跳過」。
- 若 `content/TODAY/.done` 不存在 → Cowork 尚未完成生成，直接結束，輸出「⏳ .done 不存在，等待下次排程」。

---

## 步驟 1：驗證 10 個 JSON 檔

讀取 `content/TODAY/` 下的 10 個檔案：
`n5_lite.json`, `n5.json`, `n4_lite.json`, `n4.json`, `n3_lite.json`,
`n3.json`, `n2_lite.json`, `n2.json`, `n1_lite.json`, `n1.json`

對每篇執行以下驗證：

### 1a — 句數一致性
```
count(。！？ in tokens) == count(。！？ in text) == len(translations)
```
不一致 → 記錄在驗證摘要中，**繼續驗其他篇**（不中斷整個流程）。

### 1b — Vocab 覆蓋
所有名詞、動詞、形容詞、副詞、接続詞 token 的 `basic_form` 都要有 vocab 對應。

**能自動補的問題** — 常見接続詞/副詞缺 vocab 時，用以下固定翻譯補入：
```
それから → 然後、接著  しかし → 但是、然而  また → 又、還有
例えば → 例如         したがって → 因此       ところが → 然而、沒想到
とはいえ → 即便如此    つまり → 也就是說      だから → 所以
でも → 但是           そして → 然後、接著     さらに → 此外、更加
もし → 如果           たとえ → 即使          一方 → 另一方面
```
補入後存回原檔（覆蓋）。

**無法自動補的** → 記錄在摘要，繼續（不阻擋 push）。

---

## 步驟 2：git push with retry

```bash
cd /Users/mick/Documents/Projects/Language
git add content/TODAY/ content/index.json content/recent_titles.json
git commit -m "content: TODAY daily articles (10 levels)"
git push
```

- **若 push 失敗**：等 30 秒後重試，最多重試 **5 次**。
- **任一次成功** → 執行 `touch content/TODAY/.pushed`，輸出「✅ Push 成功（第 N 次）」後結束。
- **5 次都失敗** → 輸出「❌ Push 失敗，下次排程會再試」後結束（下次排程因 `.pushed` 不存在，會再嘗試）。

---

## 步驟 3：輸出驗證摘要

輸出以下格式的摘要：

```
📅 TODAY 驗證摘要
---
✅ 成功篇數：X/10
⚠️  自動修正：[列出修正的篇名與項目]
❌ 無法自動修正：[列出問題篇名與描述]
🚀 Push 狀態：成功（第 N 次）/ 失敗
```

---

## 排程設定參考

建議排程：每天 00:45 起，每 15 分鐘執行一次，至 03:00 止（共 10 次）。
Cowork 文章生成排程為 00:30，通常 45 分鐘內完成，第一次 00:45 的 Routines 多半會碰到 `.done` 已存在。
