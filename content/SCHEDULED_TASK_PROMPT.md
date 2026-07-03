# Daily Article Generation Prompt

## Schedule
- Time: 00:30 daily (Taiwan time)
- Runner: Cowork Scheduled Task

---

## Task

Today is {{TODAY}} (format: YYYY-MM-DD).

Generate 10 Japanese learning articles, one per level. Complete and save each article before starting the next.

Save path: `/Users/mick/Documents/Language/content/{{TODAY}}/`

Files: `n5_lite.json` `n5.json` `n4_lite.json` `n4.json` `n3_lite.json` `n3.json` `n2_lite.json` `n2.json` `n1_lite.json` `n1.json`

---

## Avoid Recent Topics

Read `/Users/mick/Documents/Language/content/recent_titles.json` — it lists the last 7 days of titles per level. **Do not repeat any title in today's 10 articles.**

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

1. **tokens**: Cover all words. **Skip punctuation** (。、！？ etc. need no token). **Verb and adjective inflections are ONE token** — `basic_form` = dictionary form, `reading` = full hiragana of the inflected form. Do NOT split into stem + auxiliary. Examples:
   - `行きました` → one token `{ surface:"行きました", basic:"行く", reading:"いきました", pos:"動詞" }`
   - `減っている` → `{ surface:"減っている", basic:"減る", reading:"へっている", pos:"動詞" }`
   - Exception: standalone particles (は・を・に・へ・と・で・が…) and sentence-final auxiliaries (です・だ・ます etc.) are each their own token.

2. **vocab**: Include all nouns, verbs, adjectives, adverbs, conjunctions, interjections. **Exclude** particles and auxiliaries. Key must exactly match the token's `basic_form`. Value must include `meaning` (Traditional Chinese). Do NOT include `romaji` (computed locally by the app). After generating, self-check: every content-word token's `basic_form` must have a vocab entry. **Missing entries cause "尚無中文翻譯" errors.**

3. **particles**: Object — key = particle/auxiliary in the article, value = one-sentence Traditional Chinese usage note. App merges this with its built-in table.

4. **translations**: Nested array — each outer element = one sentence; each sentence = array of `{ "text": "...", "word": "..." }`. `text` = Chinese fragment, `word` = corresponding Japanese `basic_form`. One segment per sentence is fine. **Must be nested array, not plain strings.**

5. Topics: different each day, everyday life/culture/current events. All Chinese output in **Traditional Chinese**.

6. `level` = filename; `difficulty` field is **not needed** (hardcoded in app by level).

---

## After All 10 Articles: Update Files & Push

### Step 1 — Update recent_titles.json

Path: `/Users/mick/Documents/Language/content/recent_titles.json`

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

Path: `/Users/mick/Documents/Language/content/index.json`

Prepend to `dates` array:
```json
{
  "date": "{{TODAY}}",
  "levels": ["n5_lite", "n5", "n4_lite", "n4", "n3_lite", "n3", "n2_lite", "n2", "n1_lite", "n1"],
  "generated_at": "{{TODAY}}T00:30:00Z"
}
```

### Step 3 — git commit & push

```bash
cd /Users/mick/Documents/Language
git add content/{{TODAY}}/ content/index.json content/recent_titles.json
git commit -m "content: {{TODAY}} daily articles (10 levels)"
git push
```
