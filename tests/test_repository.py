import copy
from pathlib import Path
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from scripts.check_repository import ROOT, children, inspect, local, validate_root
from scripts.sync_new_recruit_revisions import normalize


def minimum(node):
    return max([int(float(c.get('value'))) for c in children(node, 'constraints')
                if c.get('type') == 'min' and c.get('scope') == 'parent'] or [0])


def default_selection(node):
    """Small static default walk, not a substitute for the New Recruit engine."""
    selected = [node]
    for entry in children(node, 'selectionEntries'):
        for _ in range(minimum(entry)):
            selected.extend(default_selection(entry))
    for group in children(node, 'selectionEntryGroups'):
        if minimum(group):
            entries = children(group, 'selectionEntries')
            choice = next((e for e in entries if e.get('id') == group.get('defaultSelectionEntryId')), None)
            if choice is None:
                raise AssertionError(f'Missing required default: {group.get("name")}')
            for _ in range(minimum(group)):
                selected.extend(default_selection(choice))
    return selected


class StructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(ROOT/'Abandoned_Dead.cat').getroot()
        cls.ns = cls.root.tag.split('}')[0] + '}'
        cls.visible = {e.get('id') for path in list(ROOT.glob('*.cat')) + list(ROOT.glob('*.gst'))
                       for e in ET.parse(path).getroot().iter() if e.get('id')}

    def test_all_catalogues(self):
        self.assertEqual(inspect()[0], [])

    def test_duplicate_equipment_container_rejected(self):
        root = copy.deepcopy(self.root)
        unit = children(root, 'selectionEntries')[0]
        ET.SubElement(unit, self.ns+'selectionEntryGroups')
        ET.SubElement(unit, self.ns+'selectionEntryGroups')
        self.assertTrue(any('duplicate selectionEntryGroups' in e for e in validate_root(root, self.visible)))

    def test_nullifier_nested_under_gunship_rejected(self):
        root = copy.deepcopy(self.root)
        units = root.find(self.ns+'selectionEntries')
        operator = next(u for u in units if u.get('id') == 'ad26-null-op-2026')
        gunship = next(u for u in units if u.get('name') == 'Shadow Gunship')
        units.remove(operator)
        ET.SubElement(gunship, self.ns+'selectionEntries').append(operator)
        self.assertTrue(any('unit nested' in e for e in validate_root(root, self.visible)))

    def test_invalid_default_rejected(self):
        root = copy.deepcopy(self.root)
        group = next(e for e in root.iter() if e.get('defaultSelectionEntryId'))
        group.set('defaultSelectionEntryId', root.get('id'))
        self.assertTrue(any('default is not a direct choice' in e for e in validate_root(root, self.visible)))

    def test_nonfinite_cost_rejected(self):
        root = copy.deepcopy(self.root)
        next(e for e in root.iter() if local(e.tag) == 'cost').set('value', 'NaN')
        self.assertTrue(any('invalid numeric' in e for e in validate_root(root, self.visible)))

    def test_four_reported_squads_have_complete_default_weapons(self):
        names = ('Unmarked Scout Squad', 'Blackout Breachers', 'Directorate Breach Cell', 'Shadow Operative Cell')
        for unit in children(self.root, 'selectionEntries'):
            if unit.get('name') not in names:
                continue
            size_group = next(g for g in children(unit, 'selectionEntryGroups') if g.get('name') == 'Squad Size / Personnel')
            self.assertEqual(len([g for g in unit if local(g.tag) == 'selectionEntryGroups']), 1)
            for size in children(size_group, 'selectionEntries'):
                with self.subTest(unit=unit.get('name'), size=size.get('name')):
                    selected = default_selection(size)
                    models = [e for e in selected if e.get('type') == 'model']
                    expected = 10 if size.get('name').startswith('10') else 5
                    self.assertEqual(len(models), expected)
                    for model in models:
                        choices = default_selection(model)
                        weapons = [p for e in choices for p in children(e, 'profiles') if p.get('typeName') == 'Weapon']
                        self.assertTrue(weapons, model.get('name'))
                    cost = sum(float(c.get('value')) for e in selected for c in children(e, 'costs'))
                    self.assertGreater(cost, 0)

    def test_nullifiers_are_root_units_with_preserved_model_costs(self):
        units = {e.get('id'): e for e in children(self.root, 'selectionEntries')}
        for uid, count, cost in [('ad26-null-op-2026', 1, 35), ('ad26-null-team-2026', 3, 50)]:
            selected = default_selection(units[uid])
            self.assertEqual(sum(e.get('type') == 'model' for e in selected), count)
            self.assertEqual(sum(float(c.get('value')) for e in selected for c in children(e, 'costs')), cost)

    def test_nullifier_fixed_loadouts_and_profiles(self):
        expected_stats = {
            'Compact Carbine': ['18"', '2', '4+', '3', '0', '1', 'Assault'],
            'Directorate Carbine': ['18"', '2', '4+', '3', '0', '1', 'Assault'],
            'Sidearm': ['12"', '1', '4+', '3', '0', '1', 'Pistol'],
            'Combat Knife': ['Melee', '2', '4+', '3', '0', '1', ''],
        }
        models_checked = profiles_checked = 0
        for unit in children(self.root, 'selectionEntries'):
            if unit.get('id') not in {'ad26-null-op-2026', 'ad26-null-team-2026'}:
                continue
            for model in children(unit, 'selectionEntries'):
                with self.subTest(model=model.get('name')):
                    primary = 'Compact Carbine' if 'Operator' in model.get('name') else 'Directorate Carbine'
                    expected = {primary, 'Sidearm'}
                    if not model.get('name').startswith('Null-field Technician'):
                        expected.add('Combat Knife')
                    selected = default_selection(model)
                    weapons = [p for e in selected for p in children(e, 'profiles') if p.get('typeName') == 'Weapon']
                    self.assertEqual({p.get('name') for p in weapons}, expected)
                    self.assertEqual(len(weapons), len(expected))
                    for p in weapons:
                        self.assertEqual([c.text or '' for c in children(p, 'characteristics')], expected_stats[p.get('name')])
                    for group in children(model, 'selectionEntryGroups'):
                        self.assertEqual({c.get('type'): c.get('value') for c in children(group, 'constraints')}, {'min': '1', 'max': '1'})
                    base_cost = sum(float(c.get('value')) for c in children(model, 'costs'))
                    selected_cost = sum(float(c.get('value')) for e in selected for c in children(e, 'costs'))
                    self.assertEqual(selected_cost, base_cost)
                    models_checked += 1
                    profiles_checked += len(weapons)
        self.assertEqual(models_checked, 6)
        self.assertEqual(profiles_checked, 16)


class RevisionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Test')
        self.gst = self.path/'Gaul_Campaign_Renegades.gst'
        self.cat = self.path/'Example.cat'
        self.gst.write_text('<gameSystem id="sys" revision="2"/>')
        self.cat.write_text('<catalogue id="cat" revision="3" gameSystemId="sys" gameSystemRevision="2"><rules/></catalogue>')
        self.commit()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.path, stderr=subprocess.DEVNULL).decode().strip()

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'test')

    def test_multicommit_push_detects_earlier_catalogue_change(self):
        base = self.git('rev-parse', 'HEAD')
        self.cat.write_text(self.cat.read_text().replace('<rules/>', '<rules><rule name="new"/></rules>'))
        self.commit()
        (self.path/'README.md').write_text('Documentation commit after data change')
        self.commit()
        self.assertEqual(normalize(self.path, base), ['Example.cat'])
        self.assertEqual(ET.parse(self.cat).getroot().get('revision'), '4')
        self.assertEqual(normalize(self.path, base), [])

    def test_system_change_updates_catalogue_metadata_once(self):
        self.gst.write_text('<gameSystem id="sys" revision="2"><rules/></gameSystem>')
        self.assertEqual(set(normalize(self.path)), {'Example.cat', 'Gaul_Campaign_Renegades.gst'})
        self.assertEqual(ET.parse(self.cat).getroot().get('gameSystemRevision'), '3')
        self.assertEqual(ET.parse(self.cat).getroot().get('revision'), '4')
        self.assertEqual(normalize(self.path), [])

    def test_check_does_not_mutate(self):
        self.cat.write_text(self.cat.read_text().replace('<rules/>', '<rules><rule/></rules>'))
        before = self.cat.read_bytes()
        self.assertEqual(normalize(self.path, check=True), ['Example.cat'])
        self.assertEqual(self.cat.read_bytes(), before)

    def test_invalid_baseline_fails_closed(self):
        with self.assertRaises(subprocess.CalledProcessError):
            normalize(self.path, 'missing-ref')

    def test_existing_revision_increase_is_preserved(self):
        self.cat.write_text(self.cat.read_text().replace('revision="3"', 'revision="8"'))
        self.assertEqual(normalize(self.path), [])

    def test_revision_rollback_is_repaired(self):
        self.cat.write_text(self.cat.read_text().replace('revision="3"', 'revision="1"'))
        normalize(self.path)
        self.assertEqual(ET.parse(self.cat).getroot().get('revision'), '4')

if __name__ == '__main__':
    unittest.main()
