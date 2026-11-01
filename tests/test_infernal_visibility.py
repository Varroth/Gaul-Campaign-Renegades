"""Guard the existing Infernal Warriors roster paths during other faction edits."""
import unittest
import xml.etree.ElementTree as ET
from scripts.check_repository import ROOT, children


class InfernalVisibilityTests(unittest.TestCase):
    def test_muster_retains_all_units_and_sections(self):
        root = ET.parse(ROOT/'Infernal_Warriors.cat').getroot()
        system = ET.parse(ROOT/'Gaul_Campaign_Renegades.gst').getroot()
        self.assertEqual(root.get('id'), '9337-a54f-d3db-5126')
        self.assertEqual(root.get('library'), 'false')
        force = next(f for f in children(system, 'forceEntries')
                     if f.get('id') == '73a9-6482-df85-55c4')
        self.assertEqual(force.get('hidden'), 'false')
        sections = {c.get('targetId') for c in children(force, 'categoryLinks')
                    if c.get('hidden') != 'true'}
        units = [u for u in children(root, 'selectionEntries') if u.get('type') == 'unit']
        self.assertEqual(len(units), 74)
        for unit in units:
            with self.subTest(unit=unit.get('name')):
                self.assertEqual(unit.get('import'), 'true')
                self.assertEqual(unit.get('hidden'), 'false')
                primary = [c for c in children(unit, 'categoryLinks') if c.get('primary') == 'true']
                self.assertEqual(len(primary), 1)
                self.assertIn(primary[0].get('targetId'), sections)
                self.assertFalse(any(m.get('field') == 'hidden' for m in children(unit, 'modifiers')))

    def test_frozen_cogs_no_development_notices(self):
        root = ET.parse(ROOT/'Frozen_Cogs.cat').getroot()
        for p in root.iter():
            if p.get('typeName') == 'Ability':
                text = ''.join(p.itertext()).lower()
                self.assertNotIn('new recruit', text)
                self.assertNotIn('offline editor', text)
                self.assertNotIn('preliminary homebrew', text)

if __name__ == '__main__':
    unittest.main()
