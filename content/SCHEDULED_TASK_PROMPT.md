# Daily Article Generation Prompt

## Schedule
- Time: 00:30 daily (Taiwan time)
- Runner: Cowork Scheduled Task

---

## Task

Today is {{TODAY}} (format: YYYY-MM-DD).

Generate 10 Japanese learning articles, one per level. Complete and save each article before starting the next.

Save path: `/Users/mick/Documents/Projects/Language/content/{{TODAY}}/`

Files: `n5_lite.json` `n5.json` `n4_lite.json` `n4.json` `n3_lite.json` `n3.json` `n2_lite.json` `n2.json` `n1_lite.json` `n1.json`

---

## Avoid Recent Topics

Read `/Users/mick/Documents/Projects/Language/content/recent_titles.json` — it lists the last 7 days of titles per level. **Do not repeat any title in today's 10 articles.**

---

## Per-Article Steps (in order, no skipping)

**① Write the article** (output `text` field content only)

**② Silent quality check** (no output — check internally and fix directly)
- Natural and fluent? No contradictions?
- Vocabulary matches the level?
- Any more colloquial/natural word choices? (e.g. うち over いえ, ちょっと over 少し, てる over ている)
- Fix issues silently and continue.

**③ Write full JSON and save**

---

## Level Specs

| File | Display | Length | Grammar Features |
|------|---------|--------|-----------------|
| n5_lite | N5⁻ | 40–60 chars | High-freq nouns + です/います, no verb conjugation |
| n5 | N5 | 80–120 chars | て-form/た-form, common particles |
| n4_lite | N4⁻ | 100–140 chars | N5 grammar + N4 vocab |
| n4 | N4 | 140–180 chars | ～たり～たり, ～ので/のに, ～ことができる |
| n3_lite | N3⁻ | 160–200 chars | N4 grammar + N3 vocab |
| n3 | N3 | 200–250 chars | Contrast, quotation, compound expressions |
| n2_lite | N2⁻ | 220–270 chars | N3 grammar + N2 vocab |
| n2 | N2 | 270–330 chars | Written style, complex conjunctions |
| n1_lite | N1⁻ | 300–360 chars | N2 grammar + N1 vocab |
| n1 | N1 | 360+ chars | Written/formal style, abstract discourse |

_lite: grammar one tier below same level, sentences 20–30% shorter, topic is free.

**Tone principle**: N4 and below → prefer colloquial vocab (うち, ちょっと, てる-form etc.); N2 and above may use written style. Overall tone: Japanese diary or casual conversation — avoid textbook stiffness.

---

## JSON Format

```json
{
  "date": "{{TODAY}}",
  "level": "n4_lite",
  "title": "Article title",
  "text": "Full Japanese article text",
  "tokens": [
    { "surface_form": "inflected form", "basic_form": "dictionary form", "reading": "hiragana", "pos": "part of speech" }
  ],
  "vocab": {
    "dictionary_form": { "meaning": "Traditional Chinese meaning" }
  },
  "particles": {
    "は": "topic marker — marks the sentence topic",
    "と": "marks a companion or quoted content"
  },
  "translations": [
    [ { "text": "Full Chinese for sentence 1", "word": "corresponding vocab basic_form" } ],
    [ { "text": "First part,", "word": "wordA" }, { "text": "second part.", "word": "wordB" } ]
  ]
}
```

---

## Rules

1. **tokens**: Cover all words. **Punctuation `。！？、` MUST each be its own token** — `{ "surface_form": "。", "basic_form": "。", "reading": "。", "pos": "記号" }` (same for `！？、`). **This is critical, not optional**: the app splits the article into sentences and inserts Chinese translations by scanning `tokens` for a `surface_form` of exactly `。`/`！`/`？` — omitting these tokens breaks sentence segmentation and hides all Chinese translations, even though `translations` itself is correct. **Verb and adjective inflections are ONE token** — `basic_form` = dictionary form, `reading` = full hiragana of the inflected form. Do NOT split into stem + auxiliary. Examples:
   - `行きました` → one token `{ surface:"行きました", basic:"行く", reading:"いきました", pos:"動詞" }`
   - `減っている` → `{ surface:"減っている", basic:"減る", reading:"へっている", pos:"動詞" }`
   - Exception: standalone particles (は・を・に・へ・と・で・が…) and sentence-final auxiliaries (です・だ・ます etc.) are each their own token — same as punctuation, never merged into a neighboring word.
   - **Self-check before saving**: concatenating every token's `surface_form` in order must reproduce `text` exactly, character for character (including all `。！？、`). If it doesn't, punctuation tokens are missing — this is the #1 cause of broken articles.

2. **vocab**: Include all nouns, verbs, adjectives, adverbs, conjunctions, interjections. **Exclude** particles and auxiliaries. Key must exactly match the token's `basic_form`. Value must include `meaning` (Traditional Chinese). Do NOT include `romaji` (computed locally by the app). After generating, self-check: every content-word token's `basic_form` must have a vocab entry. **Missing entries cause "尚無中文翻譯" errors.**

3. **particles**: Object — key = particle/auxiliary in the article, value = one-sentence Traditional Chinese usage note. App merges this with its built-in table.

4. **translations**: Nested array — each outer element = one sentence; each sentence = array of `{ "text": "...", "word": "..." }`. `text` = Chinese fragment, `word` = corresponding Japanese `basic_form`. One segment per sentence is fine. **Must be nested array, not plain strings.**

5. Topics: different each day, everyday life/culture/current events. All Chinese output in **Traditional Chinese**.

6. `level` = filename; `difficulty` field is **not needed** (hardcoded in app by level).

7. **Sentence-count consistency (CRITICAL — verify before saving each file).** The app splits sentences from `tokens` on 。！？ and pairs each with `translations` by index, so all three must be exactly equal:
   **count(。！？ in tokens) == count(。！？ in text) == length(translations)** — one sentence ↔ one translations element, strict order.
   Common mistakes that break alignment (fix until equal):
   - (a) A sentence-final `。` written as `、` in tokens (tokens punctuation must match text) → one missing boundary shifts every later translation.
   - (b) Missing one sentence's translation (often the last) → last sentence has no Chinese, or shift.
   - (c) A `？` inside quotes (e.g. 「…ですか？」) splits `text` into two sentences but `translations` only has one → split the translation into two matching segments.

---

## After All 10 Articles: Update Files & Mark Done

### Step 1 — Update recent_titles.json

Path: `/Users/mick/Documents/Projects/Language/content/recent_titles.json`

Prepend today's entry and keep only the latest 7 entries:
```json
{
  "date": "{{TODAY}}",
  "n5_lite": "<title>", "n5": "<title>", "n4_lite": "<title>", "n4": "<title>",
  "n3_lite": "<title>", "n3": "<title>", "n2_lite": "<title>", "n2": "<title>",
  "n1_lite": "<title>", "n1": "<title>"
}
```

### Step 2 — Update index.json

Path: `/Users/mick/Documents/Projects/Language/content/index.json`

Prepend to `dates` array:
```json
{
  "date": "{{TODAY}}",
  "levels": ["n5_lite", "n5", "n4_lite", "n4", "n3_lite", "n3", "n2_lite", "n2", "n1_lite", "n1"],
  "generated_at": "{{TODAY}}T00:30:00Z"
}
```

### Step 3 — Write .done marker

```bash
cd /Users/mick/Documents/Projects/Language && touch content/{{TODAY}}/.done
```

---

## After .done: Validate, Push, and Verify (no manual intervention required)

**Important — avoid permission hangs**: do not use command substitution `$(...)` or shell variables like `$TODAY` inside a single bash command. Resolve `{{TODAY}}` to the literal date string (e.g. `2026-07-15`) once, then hardcode that literal string into every command below.

### Step 4 — Validate the 10 JSON files

For each of the 10 files (`n5_lite.json` … `n1.json`):

**4a — Token/punctuation reconstruction (CRITICAL — this is what broke articles on 2026-07-14/15)**
Concatenate every token's `surface_form` in order and compare to `text`, character for character. **They must be identical.** If tokens are missing punctuation (`。！？、`), the article renders as one unbroken block with no sentence breaks and no Chinese — even though `translations` itself may be fine.
If they don't match, fix by re-inserting a punctuation token (`{ "surface_form": "。", "basic_form": "。", "reading": "。", "pos": "記号" }`, same pattern for `！？、`) at every point where `text` has a punctuation character not present in the token stream. Re-check after fixing.

**4b — Sentence-count consistency (CRITICAL)**
```
count(。！？ in tokens) == count(。！？ in text) == length(translations)
```
If mismatched, fix directly in the file (common causes: a sentence-final `。` mis-tokenized as `、`; a missing last-sentence translation; a `？` inside quotes splitting `text` but not `translations`). Re-check after fixing. Do not stop the whole run for one bad file — fix what you can, note what you can't, and continue.

**4c — Vocab coverage**
Every noun/verb/adjective/adverb/conjunction token's `basic_form` must have a `vocab` entry. For common missing conjunctions/adverbs, backfill with:
```
それから → 然後、接著  しかし → 但是、然而  また → 又、還有
例えば → 例如         したがって → 因此       ところが → 然而、沒想到
とはいえ → 即便如此    つまり → 也就是說      だから → 所以
でも → 但是           そして → 然後、接著     さらに → 此外、更加
もし → 如果           たとえ → 即使          一方 → 另一方面
```
Save fixes back to the file (overwrite). Anything you can't auto-fix — note it, don't block the push.

### Step 5 — git push with retry (ensures nothing needs manual handling)

Replace `{{TODAY}}` below with the **literal resolved date string** (e.g. `2026-07-15`) — never a shell variable:

```bash
cd /Users/mick/Documents/Projects/Language
git add content/{{TODAY}}/ content/index.json content/recent_titles.json
git commit -m "content: {{TODAY}} daily articles (10 levels)"
git push
```

- **If push fails**: wait 30 seconds, retry. Retry up to **5 times total**.
- **On any success** → run `touch content/{{TODAY}}/.pushed` (literal date), output "✅ Push 成功（第 N 次）", done.
- **If all 5 attempts fail** → output "❌ Push 失敗，已重試 5 次，將由備援 routine（jp-content-git-push，每 15 分鐘檢查 `.pushed`）自動接手重試". Do not treat this as a fatal error — the backup routine will pick it up automatically because `.pushed` was never created. No manual step is needed from the user in either case.

### Step 6 — Output summary

```
📅 {{TODAY}} 生成＋驗證＋Push 摘要
---
✅ 成功篇數：X/10
⚠️  自動修正：[列出修正的篇名與項目]
❌ 無法自動修正：[列出問題篇名與描述]
🚀 Push 狀態：成功（第 N 次）/ 失敗（備援 routine 將接手）
```
