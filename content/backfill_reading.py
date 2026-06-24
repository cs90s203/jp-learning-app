#!/usr/bin/env python3
"""
Backfill `reading` field into existing content pack vocab entries.

Priority:
1. Pure kana key → reading = key itself
2. Token with surface_form == basic_form == key → reading = token.reading (base appeared in text)
3. Reconstruct base reading from inflected token reading
4. Otherwise → empty string (app fallback)
"""
import json, os, glob, re

KANA_RE = re.compile(r'^[ぁ-ヿ・ー]+$')
CONTENT_DIR = os.path.dirname(os.path.abspath(__file__))

# い-row → base vowel (五段連用形 to base)
I_TO_BASE = {'き':'く','ぎ':'ぐ','し':'す','じ':'ず','ち':'つ','に':'ぬ','び':'ぶ','み':'む','り':'る','い':'う'}
A_TO_BASE = {'わ':'う','か':'く','が':'ぐ','さ':'す','た':'つ','な':'ぬ','ば':'ぶ','ま':'む','ら':'る','あ':'う'}
# え-row endings indicate 一段 verb (stem + key_end)
E_ROW = set('えけげせてねべめれ')
# Special irregular verbs
IRREGULAR_BASE = {'来る':'くる','為る':'する','する':'する'}

def strip_suru_suffix(reading):
    """For compound する verbs: extract noun prefix from inflected reading."""
    suru_suffixes = [
        'しています','させること','させる','できます','できる','すること',
        'しやすく','しにくく','しました','しません','している','していた',
        'してきた','してきます','します','して','した','し',
    ]
    for sfx in suru_suffixes:
        if reading.endswith(sfx):
            prefix = reading[:-len(sfx)]
            if prefix:
                return prefix + 'する'
    # さ row (passive/causative of する)
    idx = reading.rfind('さ')
    if idx > 0:
        return reading[:idx] + 'する'
    return None


def reconstruct_verb(reading, key_end, basic_form=''):
    """
    Try to reconstruct base form reading.
    key_end: last hiragana of the vocab key (e.g. 'く' from 行く)
    Returns base reading string or None.
    """
    # Compound する verbs (key ends in する)
    if basic_form.endswith('する'):
        result = strip_suru_suffix(reading)
        if result:
            return result

    # 促音便 っ at end: strip っ → root + key_end
    if reading.endswith('っ'):
        root = reading[:-1]
        if root:
            return root + key_end

    # 撥音便 ん at end: strip ん → root + key_end
    if reading.endswith('ん'):
        root = reading[:-1]
        if root:
            return root + key_end

    # Strip suffixes iteratively (loop until no more match)
    compound = [
        'ませんでした','ていません','ていなかった','ていない',
        'ていました','ていた','ている','でいない','でいなかった',
        'でいます','でいた','でいる',
        'とする','とした','ことができる','ことができた',
        'させられる','させること','させる','られる','される',
        'ません','ました','たい','ます',
        'なかった','ない','ければ',
        'ようとする','ようとした','おうとする','おうとした',
        'えば','よう','おう',
        'いて','いで',
        'て','で','た','だ','ば',
    ]

    r = reading
    for _ in range(3):  # max 3 rounds of stripping
        matched = False
        for sfx in compound:
            if r.endswith(sfx):
                candidate = r[:-len(sfx)]
                if candidate:
                    r = candidate
                    matched = True
                break
        if not matched:
            break

    stem = r
    if not stem:
        return None

    # Resolve stem to base reading
    if stem.endswith('っ'):
        root = stem[:-1]
        return (root + key_end) if root else None
    if stem.endswith('ん'):
        root = stem[:-1]
        return (root + key_end) if root else None

    last = stem[-1]
    if last in E_ROW:
        return stem + key_end
    if last in I_TO_BASE:
        if key_end == 'る' and last == 'り':
            return stem[:-1] + 'る'
        elif key_end in I_TO_BASE.values():
            return stem[:-1] + key_end
        else:
            return stem + key_end
    # あ行 未然形: とわ→とう, いわ→いう, しら→しる, つか→つかう
    if last in A_TO_BASE and key_end == A_TO_BASE.get(last):
        return stem[:-1] + key_end
    # 意向形: stem ends in お行+う (ぼう/こう/もう/ろう etc) → strip → root + key_end
    O_ROW = set('おこごそとのほぼもろよを')
    if last == 'う' and len(stem) >= 2 and stem[-2] in O_ROW:
        return stem[:-2] + key_end
    # bare root: just append key_end
    return stem + key_end


def reconstruct_base_reading(reading, pos, basic_form):
    """Reconstruct the base form reading from an inflected reading."""

    # ─── い形容詞 ───
    if pos == '形容詞' and basic_form.endswith('い'):
        for sfx in ['くなかった','くなければ','くなって','かった','くない','くて','ければ','く']:
            if reading.endswith(sfx):
                return reading[:-len(sfx)] + 'い'
        # Already base form? (ends in い)
        if reading.endswith('い'):
            return reading

    # ─── な形容詞・名詞 (not ending in verb vowel) ───
    if pos in ('形容詞','名詞','副詞') and not basic_form[-1] in 'うくぐすぬむぶつる':
        for sfx in ['ではない','ではなかった','でした','じゃない','だった','な','に','さ','で','だ','と']:
            if reading.endswith(sfx):
                stem = reading[:-len(sfx)]
                if stem:
                    return stem
        return reading  # bare noun/adj

    # ─── 動詞 ───
    if pos == '動詞':
        # Irregular
        if basic_form in IRREGULAR_BASE:
            return IRREGULAR_BASE[basic_form]
        key_end = basic_form[-1]
        return reconstruct_verb(reading, key_end, basic_form)

    return None


def backfill_pack(path):
    with open(path, encoding='utf-8') as f:
        pack = json.load(f)

    vocab = pack.get('vocab', {})
    tokens = pack.get('tokens', [])

    # index: basic_form → list of tokens
    tok_map: dict = {}
    for tok in tokens:
        bf = tok.get('basic_form', '')
        if bf:
            tok_map.setdefault(bf, []).append(tok)

    # base-form token reading (surface == basic == key)
    base_reading = {
        bf: next((t['reading'] for t in tl if t.get('surface_form') == bf and t.get('reading')), None)
        for bf, tl in tok_map.items()
    }

    changed = 0
    failed = []
    for key, entry in vocab.items():
        if entry.get('reading'):
            continue

        # 1. Pure kana
        if KANA_RE.match(key):
            entry['reading'] = key
            changed += 1
            continue

        # 2. Base form appeared in text
        if base_reading.get(key):
            entry['reading'] = base_reading[key]
            changed += 1
            continue

        # 3. Reconstruct from inflected tokens
        reconstructed = None
        for tok in tok_map.get(key, []):
            rd = tok.get('reading', '')
            pos = tok.get('pos', '')
            if rd:
                reconstructed = reconstruct_base_reading(rd, pos, key)
                if reconstructed:
                    break

        if reconstructed:
            entry['reading'] = reconstructed
            changed += 1
        else:
            entry['reading'] = ''
            failed.append(key)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)

    rel = os.path.relpath(path, CONTENT_DIR)
    if failed:
        print(f'{rel}: +{changed}, {len(failed)} empty: {failed[:6]}')
    else:
        print(f'{rel}: +{changed} ✓')


# Reset all readings first, then re-run
packs = sorted(glob.glob(os.path.join(CONTENT_DIR, '*', '*.json')))
for path in packs:
    if 'index' in path: continue
    with open(path, encoding='utf-8') as f: pack = json.load(f)
    for v in pack.get('vocab', {}).values():
        v.pop('reading', None)  # clear to re-derive cleanly
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)

print('=== Backfilling readings ===')
for path in packs:
    if 'index' in path: continue
    backfill_pack(path)

total_empty = sum(
    1 for path in packs if 'index' not in path
    for v in json.load(open(path)).get('vocab', {}).values()
    if not v.get('reading')
)
print(f'\nRemaining empty: {total_empty}')
