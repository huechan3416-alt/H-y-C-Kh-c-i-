"""Validate the normalized project and its explicitly draft subtitles."""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((root / 'scenes.json').read_text(encoding='utf-8'))
scenes = data['scenes']
assert len(scenes) == 16
blocks = (root / 'subtitles.srt').read_text(encoding='utf-8').strip().split('\n\n')
assert len(blocks) == len(scenes)

def parse_time(value):
    h, m, s, ms = map(int, re.split('[:,]', value))
    assert m < 60 and s < 60 and ms < 1000
    return ((h * 60 + m) * 60 + s) * 1000 + ms

cursor = 0
for i, (scene, block) in enumerate(zip(scenes, blocks), 1):
    assert scene['id'] == f'scene-{i:02}' and scene['number'] == i
    for key in ('narration', 'image_description', 'image_prompt'):
        assert scene[key].strip()
    assert (root / scene['image_path']).is_file()
    path = scene['provenance']['narration'].split('#')[0]
    annotation = json.loads((root / path).read_text(encoding='utf-8'))
    assert scene['narration'] == annotation['storyBasis']
    assert scene['id'] == annotation['sceneId']
    lines = block.splitlines()
    assert int(lines[0]) == i and scene['subtitle_cue_ids'] == [i]
    start, end = map(parse_time, lines[1].split(' --> '))
    assert start == cursor and end > start
    assert start == scene['timing']['start_ms'] and end == scene['timing']['end_ms']
    assert end - start == annotation['sceneDurationMs'] == scene['timing']['duration_ms']
    assert '\n'.join(lines[2:]) == scene['narration']
    cursor = end
assert cursor == 144000
print('PASS: 16 scenes, 16 source annotations, 16 images, 16 aligned draft subtitle cues; 144 seconds.')
print('Original full storyboard/SRT still unavailable; this check does not certify alignment to the old SRT or audio.')
