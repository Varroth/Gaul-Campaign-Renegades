#!/usr/bin/env python3
"""Synchronize only root revision metadata against an explicit Git baseline.

Local/pre-commit use: --base HEAD. CI uses the pre-push SHA, covering every
commit in a push. No unit, weapon, rule, label or import changes happen here.
"""
import argparse
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def root_tag(source, kind):
    match = re.search(r'<' + kind + r'\b[^>]*>', source)
    if not match:
        raise ValueError(f'Missing {kind} root')
    return match.group()

def attr(tag, name):
    match = re.search(r'\b' + name + r'="([^"]*)"', tag)
    if not match:
        raise ValueError(f'Missing {name}')
    return match.group(1)

def replace_attr(tag, name, value):
    attr(tag, name)
    return re.sub(r'\b' + name + r'="[^"]*"', f'{name}="{value}"', tag, count=1)

def previous(directory, base, name):
    # A valid baseline with a new file is different from a missing Git baseline.
    found = subprocess.run(['git', 'cat-file', '-e', f'{base}:{name}'], cwd=directory,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if found.returncode:
        return None
    return subprocess.check_output(['git', 'show', f'{base}:{name}'], cwd=directory).decode('utf-8')

def normalize(directory=ROOT, base='HEAD', check=False):
    if not re.fullmatch('0{40,64}', base):
        subprocess.run(['git', 'rev-parse', '--verify', f'{base}^{{commit}}'], cwd=directory,
                       stdout=subprocess.DEVNULL, check=True)
    paths = [directory/'Gaul_Campaign_Renegades.gst'] + sorted(directory.glob('*.cat'))
    if len(paths) < 2:
        raise ValueError('Expected a game system and catalogues')
    updates = {}
    system_id = system_revision = None
    for path in paths:
        kind = 'gameSystem' if path.suffix == '.gst' else 'catalogue'
        source = path.read_text(encoding='utf-8')
        old = None if re.fullmatch('0{40,64}', base) else previous(directory, base, path.name)
        tag = root_tag(source, kind)
        new_tag = tag
        if kind == 'catalogue':
            if attr(tag, 'gameSystemId') != system_id:
                raise ValueError(f'{path.name}: wrong gameSystemId')
            new_tag = replace_attr(new_tag, 'gameSystemRevision', system_revision)
        revision = int(attr(tag, 'revision'))
        candidate = source.replace(tag, new_tag, 1)
        if old is not None and candidate != old:
            old_revision = int(attr(root_tag(old, kind), 'revision'))
            revision = max(revision, old_revision + 1)
        elif candidate != source:
            revision += 1
        if revision < 1:
            raise ValueError(f'{path.name}: revision must be positive')
        new_tag = replace_attr(new_tag, 'revision', revision)
        updated = source.replace(tag, new_tag, 1)
        if kind == 'gameSystem':
            system_id, system_revision = attr(new_tag, 'id'), revision
        if updated != source:
            updates[path] = updated
    if not check:
        for path, updated in updates.items():
            path.write_text(updated, encoding='utf-8')
    return [p.name for p in updates]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='HEAD', help='Pre-change commit; CI passes pre-push SHA')
    parser.add_argument('--check', action='store_true', help='Fail instead of writing needed repairs')
    args = parser.parse_args()
    changed = normalize(base=args.base, check=args.check)
    print(('Revision repairs required: ' if args.check else 'Revisions updated: ') + ', '.join(changed) if changed else 'Revision metadata is current')
    raise SystemExit(bool(changed) if args.check else 0)

if __name__ == '__main__':
    main()
