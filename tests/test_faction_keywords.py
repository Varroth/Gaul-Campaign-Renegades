"""Check the playable entries, their exported keywords and equipment-specific tags."""
import unittest
import xml.etree.ElementTree as ET

from scripts.check_repository import ROOT, children


def read_entries(filename):
    root = ET.parse(ROOT / filename).getroot()
    system = ET.parse(ROOT / 'Gaul_Campaign_Renegades.gst').getroot()
    categories = {c.get('id'): c.get('name').upper() for doc in (system, root)
                  for c in children(doc, 'categoryEntries')}
    units = {u.get('name'): u for u in children(root, 'selectionEntries')
             if u.get('type') in ('unit', 'model')}
    return units, categories


def fixed(unit, categories):
    return {categories[c.get('targetId')] for c in children(unit, 'categoryLinks')}


def option_changes(unit, categories, option_prefix):
    ids = {e.get('targetId') or e.get('id') for e in unit.iter()
           if e.tag.rsplit('}', 1)[-1] in ('entryLink', 'selectionEntry')
           and e.get('name', '').startswith(option_prefix)}
    changes = set()
    for mod in children(unit, 'modifiers'):
        if mod.get('field') != 'category':
            continue
        for cond in mod.findall('.//{*}condition'):
            if cond.get('scope') == 'self' and cond.get('childId') in ids:
                changes.add((mod.get('type'), categories[mod.get('value')]))
    return changes


class FactionKeywords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iw, cls.ik = read_entries('Infernal_Warriors.cat')
        cls.fc, cls.fk = read_entries('Frozen_Cogs.cat')

    def test_every_playable_entry_has_an_exported_keyword_set(self):
        for units, cats, size in [(self.iw, self.ik, 96), (self.fc, self.fk, 169)]:
            self.assertEqual(len(units), size)
            for name, unit in units.items():
                with self.subTest(unit=name):
                    links = children(unit, 'categoryLinks')
                    self.assertEqual(sum(c.get('primary') == 'true' for c in links), 1)
                    self.assertEqual(len(links), len({c.get('targetId') for c in links}))
                    summaries = [s for tag in ('rules', 'profiles') for s in children(unit, tag)
                                 if s.get('name') == 'Keywords']
                    self.assertEqual(len(summaries), 1)
                    keys = set(''.join(summaries[0].itertext()).strip().split('.')[0].split(', '))
                    self.assertTrue(keys <= fixed(unit, cats), keys - fixed(unit, cats))
                    ally = name in ('Bloodletters', 'Flesh Hounds', 'Bloodcrushers',
                                    'Herald of Khorne', 'Bloodthirster')
                    if ally:
                        self.assertTrue({'DAEMON', 'KHORNE'} <= keys)
                        self.assertNotIn('INFERNAL WARRIORS', fixed(unit, cats))
                    elif units is self.fc and name in {
                        'Stormseer', 'Tidebound Intervention Squad', 'Silver Fang Terminators',
                        'Tempest Talons', 'Stormheart Dreadnought'
                    }:
                        self.assertTrue({'SILVER TEMPESTS', 'TZEENTCH', 'CHAOS', 'ASTARTES'} <= keys)
                        self.assertNotIn('FROZEN COGS', keys)
                    else:
                        self.assertIn('INFERNAL WARRIORS' if units is self.iw else 'FROZEN COGS', keys)

    def test_infernal_roles_and_exclusions(self):
        for name in ('Bike Recon Squadron', 'Outrider Assault Squadron', 'Attack Bike Flanking Section'):
            keys = fixed(self.iw[name], self.ik)
            self.assertTrue({'MOUNTED', 'ASTARTES'} <= keys)
            self.assertNotIn('INFANTRY', keys)
        for name in ('Tenth Company Scouts', 'Bloodmarked Thralls', 'Chainbound Reavers',
                     'Contemptor Relic Dreadnought', 'Defiler'):
            self.assertNotIn('ASTARTES', fixed(self.iw[name], self.ik))
        self.assertIn('CHAPLAIN', fixed(self.iw['Orvath Krail'], self.ik))
        self.assertNotIn('CHAPLAIN', fixed(self.iw['Balan Bannon'], self.ik))
        self.assertIn('VOXMASTER', fixed(self.iw['Karnus Vehl'], self.ik))

    def test_equipment_changes_keywords_only_on_the_equipped_unit(self):
        fly = {('add', 'JUMP PACK'), ('add', 'FLY')}
        for unit, cats, option in [
            (self.iw['Infernal Chaplain'], self.ik, 'Equip jump pack'),
            (self.fc['Assault Squad'], self.fk, 'Certified jump packs'),
            (self.fc['Vanguard Veterans'], self.fk, 'Certified jump packs'),
        ]:
            self.assertFalse(fixed(unit, cats) & {'JUMP PACK', 'FLY'})
            self.assertEqual(option_changes(unit, cats, option), fly)
        for size in range(5, 11):
            self.assertEqual(option_changes(self.iw['Lost Cohort — Power Armour'], self.ik,
                                            f'{size} afflicted + attached jump-pack'), fly)
        self.assertEqual(option_changes(self.iw['Infernal Legionaries'], self.ik, 'Vox of the Unforgotten'),
                         {('add', 'VOXMASTER')})
        stormraven = self.iw['Stormraven Assault Gunship']
        self.assertTrue({'AIRCRAFT', 'FLY', 'TRANSPORT'} <= fixed(stormraven, self.ik))
        self.assertEqual(option_changes(stormraven, self.ik, 'Low-Altitude Assault Skimmer'),
                         {('remove', 'AIRCRAFT'), ('set-primary', 'VEHICLES')})

    def test_frozen_cogs_mixed_roles(self):
        cases = [
            ('Glacierfall Artillery Cadres', {'ARTILLERY', 'ASTARTES', 'INFANTRY'}, {'VEHICLE'}),
            ('Verglas the Venerated', {'WALKER', 'DREADNOUGHT', 'CHARACTER', 'EPIC HERO'}, {'INFANTRY'}),
            ('Rimeguard Automata', {'AUTOMATA', 'WALKER'}, {'ASTARTES', 'DAEMON'}),
            ('Frostvein Interceptor Engine', {'DAEMON ENGINE', 'VEHICLE', 'SLAANESH'}, {'AIRCRAFT', 'FLY'}),
            ('Frostbound Armored Carrier', {'FROSTBOUND AUXILIA', 'VEHICLE', 'TRANSPORT'}, {'ASTARTES'}),
        ]
        for name, required, excluded in cases:
            with self.subTest(unit=name):
                keys = fixed(self.fc[name], self.fk)
                self.assertTrue(required <= keys)
                self.assertFalse(keys & excluded)
