"""Verify immutable manual captures and every reproducible quiz-safe variant."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=Path, required=True, help='Manual root containing lecture folders')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'data/source-manifest.json').read_text())
q = json.loads((root / 'data/question-bank.json').read_text())
verified_variants = set()

for s in m['sources']:
    p = args.source / s['relative_path']
    assert p.is_file(), p
    assert hashlib.sha256(p.read_bytes()).hexdigest() == s['sha256'], p
    assert hashlib.sha256((root / s['original_asset']).read_bytes()).hexdigest() == s['sha256']
    if s['status'] != 'USABLE':
        continue
    original = Image.open(p).convert('RGB')
    variants = s.get('variants') or [{
        'variant_id': s['variant_id'], 'image': s['image'],
        'zoom_image': s['zoom_image'], 'transform': s['transform'],
    }]
    for v in variants:
        crop = v['transform'].get('crop')
        if crop is not None:
            assert len(crop) == 4
            x0, y0, x1, y1 = crop
            assert all(isinstance(n, int) for n in crop)
            assert 0 <= x0 < x1 <= s['width'] and 0 <= y0 < y1 <= s['height']
            expected = original.crop(tuple(crop))
        else:
            expected = original
        final = Image.open(root / v['zoom_image']).convert('RGB')
        assert expected.size == final.size
        delta = ImageChops.difference(expected, final)
        d = ImageDraw.Draw(delta)
        for x0, y0, x1, y1 in v['transform']['masks']:
            assert 0 <= x0 < x1 <= expected.width and 0 <= y0 < y1 <= expected.height
            d.rectangle((x0, y0, x1 - 1, y1 - 1), fill=(0, 0, 0))
        assert delta.getbbox() is None, ('Pixels changed outside declared mask', s['relative_path'], v['variant_id'])
        for key, fmt in [('image', 'WEBP'), ('zoom_image', 'PNG')]:
            assert re.fullmatch(r'assets/[a-f0-9]{24}\.(png|webp)', v[key])
            with Image.open(root / v[key]) as im:
                assert im.format == fmt and im.size == expected.size
                im.verify()
        assert v['variant_id'] not in verified_variants
        verified_variants.add(v['variant_id'])
        assert s['variant_review_complete'], (s['relative_path'], v['variant_id'])

for question in q['questions']:
    assert question['variant_id'] in verified_variants, question['question_id']
    for key in ('image', 'zoom_image', 'original_image'):
        assert (root / question[key]).is_file(), (question['question_id'], key)

assert len(m['sources']) == m['source_count_physical'] == 62
assert len(q['questions']) == 95
for lecture, sources, questions in [('R5', 6, 11), ('R6', 15, 15), ('R7', 14, 11), ('R8', 3, 13), ('R9', 4, 4)]:
    assert sum(s['lecture_id'] == lecture for s in m['sources']) == sources
    assert sum(question['collection'] == lecture for question in q['questions']) == questions
print(f"PASS: {len(m['sources'])} immutable captures, {len(verified_variants)} verified variants, {len(q['questions'])} scored questions")
