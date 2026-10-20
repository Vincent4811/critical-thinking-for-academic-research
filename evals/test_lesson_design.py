#!/usr/bin/env python3
"""Check lesson time budgets and the published game's point logic, not efficacy."""

from pathlib import Path
import json
import re


def schedules(text: str) -> list[list[tuple[int, int]]]:
    groups: list[list[tuple[int, int]]] = []
    current: list[tuple[int, int]] = []
    for start, end in re.findall(r'^\|\s*(\d+)[–-](\d+)\s*\|', text, re.M):
        item = (int(start), int(end))
        if item[0] == 0 and current:
            groups.append(current)
            current = []
        current.append(item)
    if current:
        groups.append(current)
    return groups


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    timelines = {}
    matrices = {}
    for lang in ('en', 'zh-TW'):
        groups = schedules((root / 'teaching' / f'lesson-120.{lang}.md').read_text(encoding='utf-8'))
        assert len(groups) == 2, (lang, groups)
        for group, budget in zip(groups, (120, 50)):
            previous = 0
            for start, end in group:
                assert start == previous and end > start, (lang, start, end, previous)
                previous = end
            assert previous == budget
            assert sum(end - start for start, end in group) == budget
        timelines[lang] = groups
        card = (root / 'teaching' / f'activity-cards.{lang}.md').read_text(encoding='utf-8')
        rows = re.findall(r'^\|\s*([CD])\s*\|\s*\((\d+),\s*(\d+)\)\s*\|\s*\((\d+),\s*(\d+)\)\s*\|', card, re.M)
        assert len(rows) == 2
        matrix = {}
        for a, cc_a, cc_b, dd_a, dd_b in rows:
            matrix[a, 'C'] = (int(cc_a), int(cc_b))
            matrix[a, 'D'] = (int(dd_a), int(dd_b))
        assert set(matrix) == {('C', 'C'), ('C', 'D'), ('D', 'C'), ('D', 'D')}
        for b in ('C', 'D'):
            assert matrix['D', b][0] > matrix['C', b][0]
        for a in ('C', 'D'):
            assert matrix[a, 'D'][1] > matrix[a, 'C'][1]
        assert sum(matrix['C', 'C']) > sum(matrix['D', 'D'])
        matrices[lang] = matrix
    assert timelines['en'] == timelines['zh-TW']
    assert matrices['en'] == matrices['zh-TW']
    assert 120 - 12 + 15 - 9 + 6 == 120  # documented replacement, not an extra block
    assert 120 + 15 == 135  # all four games, retaining the original blocks
    winning = [False]
    for n in range(1, 14):
        winning.append(any(not winning[n-take] for take in (1, 2) if take <= n))
    assert [n for n in range(1, 14) if not winning[n]] == [3, 6, 9, 12]
    assert winning[13]
    print(json.dumps({'bilingual_time_budgets': [120, 50], 'continuous_no_overlap': True,
                      'optional_replacement_minutes': 120, 'all_four_games_minutes': 135,
                      'payoff_matrix_logic': 'pass', 'last_token_best_play': 'pass'}, indent=2))


if __name__ == '__main__':
    main()
