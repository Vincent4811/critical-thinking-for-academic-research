#!/usr/bin/env python3
"""Offline release checks. No model calls or scientific-validity claims."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED = (
    'SKILL.md', 'README.md', 'README.zh-TW.md', 'LICENSE',
    'THIRD_PARTY_NOTICES.md', 'UPSTREAM.json', 'agents/openai.yaml',
    'docs/method.en.md', 'docs/method.zh-TW.md',
    'references/workflow.md', 'references/evidence-and-maps.md',
    'references/thinking-tools.md', 'references/course-activities.md',
    'references/source-map.md', 'references/lesson-design.md', 'evals/prompts.json', 'evals/expectations.json',
    'evals/rubric.md', 'evals/README.md', 'evals/validation-report.md', 'evals/test_validator.py', 'evals/test_lesson_design.py',
    'templates/evidence-ledger.csv', 'templates/revision-log.csv',
)
PAIRS = (
    'templates/analysis', 'templates/mindmap', 'templates/coach-session',
    'examples/serving-bowl', 'examples/light-response', 'examples/nutrition',
    'teaching/lesson-120', 'teaching/activity-cards',
    'templates/lesson-plan', 'templates/classroom-worksheet',
)
PRIVATE_PATH = re.compile(r'(?i)(?:\b[a-z]:[\\/]|/(?:Users|home)/[a-z0-9_.-]+/|file://(?:localhost|[a-z]))')
SECRET_VALUE = re.compile(r'\b(?:sk-proj-|ghp_|github_pat_)[A-Za-z0-9_\-]{15,}')
MARKDOWN_LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\n)]+)\)')
MERMAID_BLOCK = re.compile(r'^```mermaid\s*\n(.*?)^```', re.M | re.S)


def inspect(root: Path) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    root = root.resolve()
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f'Missing release file: {rel}')
    for prefix in PAIRS:
        for lang in ('en', 'zh-TW'):
            if not (root / f'{prefix}.{lang}.md').is_file():
                errors.append(f'Missing language pair: {prefix}.{lang}.md')

    # Windows shell metadata is ignored by .gitignore and by the release archive.
    files = [p for p in root.rglob('*') if p.is_file() and p.name.lower() != 'desktop.ini']
    diagrams = 0
    links = 0
    for item in root.rglob('*'):
        if item.is_symlink():
            errors.append(f'Symlink is not a self-contained release asset: {item.relative_to(root)}')
    for path in files:
        rel = path.relative_to(root)
        if any(part in {'.git', 'node_modules', '__pycache__', '.venv', 'private', 'work'} for part in rel.parts):
            errors.append(f'Private/runtime directory in release: {rel}')
        if path.name.startswith('.env') or path.suffix.lower() in {'.pdf', '.pptx', '.docx', '.xlsx', '.jpg', '.jpeg', '.png', '.zip', '.pyc'}:
            errors.append(f'Unapproved binary/private artifact in release: {rel}')
            continue
        try:
            text = path.read_text(encoding='utf-8-sig')
        except (UnicodeError, OSError) as exc:
            errors.append(f'Unreadable UTF-8 release file: {rel}: {exc}')
            continue
        if PRIVATE_PATH.search(text):
            errors.append(f'Absolute private source path in release: {rel}')
        if SECRET_VALUE.search(text):
            errors.append(f'Credential-like value in release: {rel}')
        if path.suffix == '.json':
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f'Invalid JSON: {rel}: {exc}')
        if path.suffix == '.md':
            for target in MARKDOWN_LINK.findall(text):
                target = target.strip().strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith('#'):
                    continue
                links += 1
                local = (path.parent / unquote(parsed.path)).resolve()
                if not local.is_relative_to(root) or not local.is_file():
                    errors.append(f'Broken/outside relative link: {rel} -> {target}')
            for block in MERMAID_BLOCK.findall(text):
                diagrams += 1
                if not block.lstrip().startswith(('mindmap\n', 'flowchart ')):
                    errors.append(f'Unexpected diagram type in {rel}')
            # Unclosed fences catch accidental truncation, not Mermaid semantics.
            if len(re.findall(r'^```', text, re.M)) % 2:
                errors.append(f'Unbalanced Markdown fences: {rel}')

    skill_path = root / 'SKILL.md'
    if skill_path.is_file():
        text = skill_path.read_text(encoding='utf-8-sig')
        match = re.match(r'^---\n(.*?)\n---\n', text.replace('\r\n', '\n'), re.S)
        if not match:
            errors.append('Missing skill frontmatter')
        else:
            header = match.group(1)
            name = re.search(r'^name:\s*(\S+)\s*$', header, re.M)
            description = re.search(r'^description:\s*(.+)$', header, re.M)
            if not name or name.group(1) != root.name:
                errors.append('Skill name must equal package directory name')
            if not description or len(description.group(1)) > 1024:
                errors.append('Skill description missing or too long')
            if len(text.splitlines()) > 250:
                errors.append('Skill entry exceeds the release limit of 250 lines')

    try:
        upstream = json.loads((root / 'UPSTREAM.json').read_text(encoding='utf-8-sig'))
        if not re.fullmatch(r'[0-9a-f]{40}', upstream['commit']):
            errors.append('Invalid upstream commit')
        records = upstream['files']
        if len(records) != 9 or len({r['path'] for r in records}) != 9:
            errors.append('Expected nine distinct upstream source records')
        for record in records:
            if upstream['commit'] not in record['url'] or not re.fullmatch(r'[0-9a-f]{64}', record['sha256']):
                errors.append(f'Invalid upstream pin/hash: {record["path"]}')
        notices = (root / 'THIRD_PARTY_NOTICES.md').read_text(encoding='utf-8')
        retained = re.search(r'```text\n(.*?)\n```', notices, re.S)
        if not retained:
            errors.append('Full upstream license block missing')
        else:
            # Source cache line endings can differ; compare normalized license words.
            license_hash_text = '\n'.join(line.rstrip() for line in retained.group(1).splitlines()).strip()
            if 'Copyright (c) 2025 TJ Boudreaux' not in license_hash_text or 'permission notice shall be included' not in license_hash_text:
                errors.append('Upstream copyright/permission notice incomplete')
    except (OSError, KeyError, ValueError) as exc:
        errors.append(f'Invalid upstream provenance: {exc}')

    try:
        prompts = json.loads((root / 'evals/prompts.json').read_text(encoding='utf-8'))['cases']
        expected = json.loads((root / 'evals/expectations.json').read_text(encoding='utf-8'))['cases']
        ids = [case['id'] for case in prompts]
        if len(set(ids)) != len(ids) or set(ids) != set(expected):
            errors.append('Behavior prompt IDs and expectation IDs differ or repeat')
        if not all(case.get('prompt', '').strip() for case in prompts):
            errors.append('Empty behavioral prompt')
    except (OSError, KeyError, ValueError) as exc:
        errors.append(f'Invalid evaluation fixtures: {exc}')

    for name, required_columns in (
        ('evidence-ledger.csv', {'id', 'label', 'source_id', 'locator', 'checking_scope', 'publication_status'}),
        ('revision-log.csv', {'decision_owner', 'feedback_status', 'reason', 'next_evidence'}),
    ):
        try:
            with (root / 'templates' / name).open(encoding='utf-8', newline='') as stream:
                reader = csv.DictReader(stream)
                if not required_columns.issubset(reader.fieldnames or []):
                    errors.append(f'Missing worksheet headers: {name}')
                if list(reader):
                    errors.append(f'Blank worksheet unexpectedly contains data: {name}')
        except OSError as exc:
            errors.append(f'Unreadable worksheet {name}: {exc}')
    return errors, {'files': len(files), 'relative_links': links, 'mermaid_blocks': diagrams}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, counts = inspect(args.root)
    print(json.dumps({'ok': not errors, **counts, 'errors': errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
