#!/usr/bin/env python3
"""Validate the reviewed Abandoned Dead unit-placement and keyword matrix."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def children(node, tag):
    return [e for group in node if group.tag.rsplit('}', 1)[-1] == tag for e in group]

def inspect_keywords(root, system, matrix_path=None):
    matrix = json.loads((matrix_path or ROOT/'data/abandoned-dead-keywords.json').read_text())
    expected = {u['id']: u for u in matrix['units']}
    units = {u.get('id'): u for u in children(root, 'selectionEntries') if u.get('type') == 'unit'}
    errors = []
    if set(units) != set(expected):
        errors.append('Abandoned Dead root units differ from reviewed keyword matrix')
    categories = {e.get('id'): e.get('name') for r in (root, system) for e in children(r, 'categoryEntries')}
    force = next(e for e in children(system, 'forceEntries') if e.get('id') == 'ada1-e202-6a1d-ecad')
    sections = {e.get('targetId') for e in children(force, 'categoryLinks')}
    ids = matrix['category_ids']
    for keyword, cid in ids.items():
        if categories.get(cid, '').upper() != keyword:
            errors.append(f'Keyword definition absent or mismatched: {keyword}')
    for uid, u in units.items():
        if uid not in expected:
            continue
        spec = expected[uid]
        prefix = u.get('name')
        links = children(u, 'categoryLinks')
        primary = [l for l in links if l.get('primary') == 'true']
        if len(primary) != 1 or primary[0].get('name') != spec['section'] or primary[0].get('targetId') not in sections:
            errors.append(f'{prefix}: wrong or inaccessible roster section')
        targets = [l.get('targetId') for l in links]
        if len(targets) != len(set(targets)):
            errors.append(f'{prefix}: duplicate category links')
        actual = {categories.get(t, '').upper() for t in targets}
        # Primary sections are navigation labels, except Battleline, which is also a keyword.
        actual -= {spec['section'].upper()} - {'BATTLELINE'}
        if actual != set(spec['keywords']):
            errors.append(f'{prefix}: keyword mismatch; missing={sorted(set(spec["keywords"])-actual)}, extra={sorted(actual-set(spec["keywords"]))}')
        if len(actual & {'INFANTRY','MOUNTED','VEHICLE'}) != 1:
            errors.append(f'{prefix}: conflicting or missing unit type')
        if actual & {'CHAOS','IMPERIUM','PSYKER','DAEMON'}:
            errors.append(f'{prefix}: unsupported allegiance or psychic/daemon keyword')
        if 'ASTARTES' in actual and actual & {'DIRECTORATE','CULTISTS','MORTAL'}:
            errors.append(f'{prefix}: conflicting branch keywords')
        if 'EPIC HERO' in actual and 'CHARACTER' not in actual:
            errors.append(f'{prefix}: Epic Hero without Character')
        if 'AIRCRAFT' in actual and not {'VEHICLE','FLY'} <= actual:
            errors.append(f'{prefix}: aircraft missing Vehicle/Fly')
        if 'TERMINATOR' in actual and 'POWER ARMOUR' in actual:
            errors.append(f'{prefix}: incompatible armour keywords')
        want = {(c['option_id'], ids[k]) for c in spec['conditional'] for k in c['keywords']}
        found = set()
        descendant_ids = {e.get('id') for e in u.iter() if e.get('id')}
        for modifier in children(u, 'modifiers'):
            if modifier.get('field') != 'category':
                continue
            conds = children(modifier, 'conditions')
            if modifier.get('type') != 'add' or len(conds) != 1:
                errors.append(f'{prefix}: unexpected category modifier')
                continue
            cond = conds[0]
            if (cond.get('type'),cond.get('value'),cond.get('scope'),cond.get('field'),cond.get('includeChildSelections'),cond.get('includeChildForces')) != ('atLeast','1','parent','selections','true','false'):
                errors.append(f'{prefix}: keyword condition must apply to this unit only')
            if cond.get('childId') not in descendant_ids:
                errors.append(f'{prefix}: keyword condition references another unit')
            found.add((cond.get('childId'), modifier.get('value')))
        if found != want:
            errors.append(f'{prefix}: equipment-dependent keywords differ from reviewed matrix')
        summary = next((e for e in children(u,'rules') if e.get('name') in {'Keywords', 'Faction and unit keywords'}), None)
        if summary is None or not all(k in ''.join(summary.itertext()) for k in spec['keywords']):
            errors.append(f'{prefix}: missing exported keyword summary')
    return errors

if __name__ == '__main__':
    errors = inspect_keywords(ET.parse(ROOT/'Abandoned_Dead.cat').getroot(), ET.parse(ROOT/'Gaul_Campaign_Renegades.gst').getroot())
    print(json.dumps({'status': 'FAIL' if errors else 'PASS', 'errors': errors}, indent=2))
    raise SystemExit(bool(errors))
