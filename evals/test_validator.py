#!/usr/bin/env python3
"""Inject packaging defects into new temporary copies, never the source package."""

from pathlib import Path
import argparse
import json
import runpy
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True


def run(root: Path, scratch: Path | None) -> list[dict]:
    check = runpy.run_path(str(root / 'scripts' / 'validate_package.py'))['inspect']
    errors, _ = check(root)
    if errors:
        raise AssertionError(f'Baseline package fails: {errors}')
    if scratch:
        scratch.mkdir(parents=True, exist_ok=True)
    public_trial = Path(tempfile.mkdtemp(prefix='art-validator-url-', dir=scratch)) / root.name
    shutil.copytree(root, public_trial, ignore=shutil.ignore_patterns('desktop.ini', '__pycache__', '.git'))
    public_readme = public_trial / 'README.md'
    public_readme.write_text(public_readme.read_text(encoding='utf-8') + '\n[Public guide](https://example.org/home/resources/guide/)\n', encoding='utf-8')
    public_errors, _ = check(public_trial)
    if public_errors:
        raise AssertionError(f'Public HTTPS path was rejected: {public_errors}')
    results = []
    for kind in ('broken_link', 'private_path', 'private_unix_path', 'invalid_pin', 'fixture_mismatch', 'private_binary', 'populated_worksheet'):
        # Retain isolated fixtures for inspection; no recursive cleanup/deletion.
        trial = Path(tempfile.mkdtemp(prefix='art-validator-', dir=scratch)) / root.name
        shutil.copytree(root, trial, ignore=shutil.ignore_patterns('desktop.ini', '__pycache__', '.git'))
        if kind == 'broken_link':
            file = trial / 'README.md'
            file.write_text(file.read_text(encoding='utf-8') + '\n[broken](missing-source.md)\n', encoding='utf-8')
            expected = 'Broken/outside relative link'
        elif kind == 'private_path':
            file = trial / 'README.md'
            file.write_text(file.read_text(encoding='utf-8') + '\nZ:' + chr(92) + 'fictional-private' + chr(92) + 'source.txt\n', encoding='utf-8')
            expected = 'Absolute private source path'
        elif kind == 'private_unix_path':
            file = trial / 'README.md'
            file.write_text(file.read_text(encoding='utf-8') + '\n/home/fictional-person/private-notes.txt\n', encoding='utf-8')
            expected = 'Absolute private source path'
        elif kind == 'invalid_pin':
            file = trial / 'UPSTREAM.json'
            data = json.loads(file.read_text(encoding='utf-8-sig'))
            data['commit'] = 'invalid'
            file.write_text(json.dumps(data), encoding='utf-8')
            expected = 'Invalid upstream commit'
        elif kind == 'fixture_mismatch':
            file = trial / 'evals' / 'prompts.json'
            data = json.loads(file.read_text(encoding='utf-8'))
            data['cases'].pop()
            file.write_text(json.dumps(data), encoding='utf-8')
            expected = 'Behavior prompt IDs'
        elif kind == 'private_binary':
            (trial / 'private-source.pdf').write_bytes(b'fictional-check-only')
            expected = 'Unapproved binary/private artifact'
        else:
            with (trial / 'templates' / 'revision-log.csv').open('a', encoding='utf-8') as stream:
                stream.write('test,test,test,test,test,test,test,test\n')
            expected = 'Blank worksheet unexpectedly contains data'
        found, _ = check(trial)
        if not any(expected in message for message in found):
            raise AssertionError(f'{kind}: intended defect not rejected: {found}')
        results.append({'case': kind, 'rejected_as_expected': True})
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scratch', type=Path, help='Temporary-copy parent outside the package; copies are retained for inspection')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    scratch = args.scratch.resolve() if args.scratch else None
    if scratch and scratch.is_relative_to(root):
        raise SystemExit('Choose a scratch directory outside the package to avoid copying into itself.')
    print(json.dumps({'negative_tests': run(root, scratch)}, indent=2))
