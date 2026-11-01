#!/usr/bin/env python3
"""Read-only structural, reference and publication checks for every catalogue.

This is not a New Recruit runtime or gameplay-balance certification.
"""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    'rules', 'selectionEntries', 'selectionEntryGroups', 'profiles', 'constraints',
    'modifiers', 'modifierGroups', 'costs', 'categoryLinks', 'entryLinks', 'infoLinks',
    'categoryEntries', 'forceEntries', 'catalogueLinks', 'sharedSelectionEntries',
    'sharedSelectionEntryGroups', 'sharedProfiles', 'sharedRules', 'characteristics',
    'characteristicTypes', 'profileTypes', 'costTypes', 'publications', 'conditions',
    'conditionGroups', 'repeats', 'associations',
}
AFFECTED = ('Unmarked Scout Squad', 'Blackout Breachers', 'Directorate Breach Cell',
            'Shadow Operative Cell', 'Pallbearer Terminators', 'Field Support Cell')
NULLIFIERS = {'ad26-null-op-2026', 'ad26-null-team-2026'}

def local(tag):
    return tag.rsplit('}', 1)[-1]

def children(node, container):
    return [e for group in node if local(group.tag) == container for e in group]

def validate_root(root, visible_ids):
    errors = []
    ids = [e.get('id') for e in root.iter() if e.get('id')]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate IDs within file')
    top = children(root, 'selectionEntries') + children(root, 'sharedSelectionEntries')
    for e in root.iter():
        label = e.get('name') or e.get('id') or local(e.tag)
        counts = Counter(local(c.tag) for c in e)
        for tag, count in counts.items():
            if tag in COLLECTIONS and count > 1:
                errors.append(f'{label}: duplicate {tag} containers ({count})')
        if local(e.tag) == 'selectionEntry' and e.get('type') == 'unit' and e not in top:
            errors.append(f'{label}: unit nested inside another selection; expected root unit')
        if e in children(root, 'selectionEntries') and e.get('type') == 'unit' and e.get('import') != 'true':
            errors.append(f'{label}: root unit is not importable')
        for attr in ('targetId', 'typeId'):
            if e.get(attr) and e.get(attr) not in visible_ids:
                errors.append(f'{label}: unresolved {attr} {e.get(attr)}')
        default = e.get('defaultSelectionEntryId')
        if default and default not in {x.get('id') for x in children(e, 'selectionEntries') + children(e, 'entryLinks')}:
            errors.append(f'{label}: default is not a direct choice')
        if local(e.tag) in ('cost', 'costLimit', 'constraint'):
            try:
                value = float(e.get('value', 'nan'))
                if not math.isfinite(value):
                    raise ValueError()
            except ValueError:
                errors.append(f'{label}: invalid numeric value')
    return errors

def inspect(directory=ROOT):
    errors, warnings, inventory = [], [], []
    paths = sorted(list(directory.glob('*.gst')) + list(directory.glob('*.cat')))
    roots = {}
    for path in paths:
        try:
            roots[path.name] = ET.parse(path).getroot()
        except (ET.ParseError, OSError) as exc:
            errors.append(f'{path.name}: {exc}')
    systems = [r for name, r in roots.items() if name.endswith('.gst')]
    if len(systems) != 1:
        return ['Expected exactly one root game system'] + errors, warnings, inventory
    system = systems[0]
    root_ids = [r.get('id') for r in roots.values()]
    if len(root_ids) != len(set(root_ids)):
        errors.append('Duplicate catalogue/system root IDs')
    for name, root in roots.items():
        visible = {e.get('id') for e in system.iter() if e.get('id')}
        pending = [root]
        visited = set()
        while pending:
            current = pending.pop()
            if id(current) in visited:
                continue
            visited.add(id(current))
            visible.update(e.get('id') for e in current.iter() if e.get('id'))
            for link in children(current, 'catalogueLinks'):
                target = next((r for r in roots.values() if r.get('id') == link.get('targetId')), None)
                if target is None:
                    errors.append(f'{name}: missing imported catalogue {link.get("targetId")}')
                else:
                    pending.append(target)
        errors.extend(f'{name}: {e}' for e in validate_root(root, visible))
        try:
            if int(root.get('revision', '0')) < 1:
                raise ValueError()
        except ValueError:
            errors.append(f'{name}: invalid revision')
        if name.endswith('.cat'):
            if root.get('gameSystemId') != system.get('id') or root.get('gameSystemRevision') != system.get('revision'):
                errors.append(f'{name}: game-system ID/revision mismatch')
        units = [e for e in children(root, 'selectionEntries') if e.get('type') == 'unit']
        if name == 'Abandoned_Dead.cat':
            by_name = {e.get('name'): e for e in units}
            for unit_name in AFFECTED:
                unit = by_name.get(unit_name)
                if unit is None:
                    errors.append(f'{name}: missing {unit_name}')
                    continue
                groups = children(unit, 'selectionEntryGroups')
                if not any(g.get('name') == 'Squad Size / Personnel' for g in groups):
                    errors.append(f'{name}: {unit_name} missing personnel group')
                for model in unit.iter():
                    if local(model.tag) != 'selectionEntry' or model.get('type') != 'model':
                        continue
                    primary = next((g for g in children(model, 'selectionEntryGroups') if g.get('name') == 'Primary Weapon (choose one)'), None)
                    if primary is None or not primary.get('defaultSelectionEntryId'):
                        errors.append(f'{name}: {unit_name}/{model.get("name")} missing primary weapon default')
                    elif not any(local(p.tag) == 'profile' and p.get('typeName') == 'Weapon' for p in primary.iter()):
                        errors.append(f'{name}: {unit_name}/{model.get("name")} missing weapon profiles')
            if not NULLIFIERS.issubset({u.get('id') for u in units}):
                errors.append(f'{name}: Nullifier units missing from root army list')
            for u in units:
                if not any(local(p.tag) == 'profile' and p.get('typeName') == 'Weapon' for p in u.iter()):
                    if u.get('id') in NULLIFIERS:
                        warnings.append(f'{u.get("name")}: approved loadout has no approved numeric weapon profiles; attachment/Psychic weapon interactions remain manual')
                    else:
                        errors.append(f'{name}: {u.get("name")} has no weapon profiles')
        inventory.append({'file': name, 'id': root.get('id'), 'revision': int(root.get('revision', '0')),
                          'root_units': len(units), 'sha256': hashlib.sha256((directory/name).read_bytes()).hexdigest()})
    return errors, warnings, inventory

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--write-manifest', action='store_true')
    p.add_argument('--check-manifest', action='store_true')
    p.add_argument('--report')
    args = p.parse_args()
    errors, warnings, inventory = inspect()
    manifest = json.dumps({'files': inventory}, indent=2) + '\n'
    path = ROOT/'catalogue-manifest.json'
    if args.write_manifest and not errors:
        path.write_text(manifest, encoding='utf-8')
    if args.check_manifest and (not path.exists() or path.read_text(encoding='utf-8') != manifest):
        errors.append('catalogue-manifest.json is stale; regenerate after data changes')
    report = {'status': 'FAIL' if errors else 'PASS_WITH_LIMITATIONS' if warnings else 'PASS',
              'errors': errors, 'warnings': warnings, 'inventory': inventory,
              'scope': 'Repository structure and references, not New Recruit runtime or balance.'}
    if args.report:
        Path(args.report).write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(errors))

if __name__ == '__main__':
    main()
