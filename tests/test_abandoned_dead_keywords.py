import copy
import json
import unittest
import xml.etree.ElementTree as ET
from scripts.audit_abandoned_dead import ROOT, children, inspect_keywords

class KeywordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(ROOT/'Abandoned_Dead.cat').getroot()
        cls.system = ET.parse(ROOT/'Gaul_Campaign_Renegades.gst').getroot()
        cls.matrix = json.loads((ROOT/'data/abandoned-dead-keywords.json').read_text())
        cls.ids = cls.matrix['category_ids']
        cls.ns = cls.root.tag.split('}')[0]+'}'

    def unit(self, name, root=None):
        return next(u for u in children(self.root if root is None else root,'selectionEntries') if u.get('name')==name)

    def keywords(self, name, options=()):
        # Evaluate the catalogue's narrow equipment-category modifier subset.
        # This is not a simulation of the complete New Recruit engine.
        u=self.unit(name)
        cats={c.get('targetId') for c in children(u,'categoryLinks')}
        selected={e.get('id') for e in u.iter() if e.get('name') in options and e.tag==self.ns+'selectionEntry'}
        for mod in children(u,'modifiers'):
            if mod.get('field')=='category' and all(c.get('childId') in selected for c in children(mod,'conditions')):
                cats.add(mod.get('value'))
        return {k for k,v in self.ids.items() if v in cats}

    def test_all_61_units_reviewed(self):
        self.assertEqual(len(self.matrix['units']),61)
        self.assertEqual(inspect_keywords(self.root,self.system),[])

    def test_missing_faction_rejected(self):
        r=copy.deepcopy(self.root);u=self.unit('Ghostline Squad',r)
        links=u.find(self.ns+'categoryLinks')
        links.remove(next(l for l in links if l.get('targetId')==self.ids['ABANDONED DEAD']))
        self.assertTrue(any('keyword mismatch' in e for e in inspect_keywords(r,self.system)))

    def test_wrong_section_rejected(self):
        r=copy.deepcopy(self.root);u=self.unit('Nullifier Operator',r)
        next(l for l in children(u,'categoryLinks') if l.get('primary')=='true').set('targetId','missing')
        self.assertTrue(any('roster section' in e for e in inspect_keywords(r,self.system)))

    def test_mounted_and_vehicle_not_infantry(self):
        for name in ['Phantom Lancers','Darek Soln, Ghost Spear','Shroud Dreadnought','Spectre Scout Walker','Nullfire Interceptor']:
            with self.subTest(name=name):self.assertNotIn('INFANTRY',self.keywords(name))
        self.assertNotIn('FLY',self.keywords('Nullfire Interceptor'))
        self.assertNotIn('AIRCRAFT',self.keywords('Nullfire Interceptor'))

    def test_support_people_are_infantry(self):
        for name in ['Heavy Weapons Cell','Field Support Cell','Nullifier Operator','Nullifier Interdiction Team']:
            kw=self.keywords(name)
            self.assertTrue({'ABANDONED DEAD','DIRECTORATE','MORTAL','INFANTRY'} <= kw)
            self.assertFalse(kw & {'ASTARTES','VEHICLE','CHARACTER','PSYKER'})

    def test_jump_pack_only_with_selected_equipment(self):
        foot=self.keywords('Abandoned Dead Strike Commander', ['Standard power armour'])
        jump=self.keywords('Abandoned Dead Strike Commander', ['Jump Pack'])
        self.assertFalse(foot & {'JUMP PACK','FLY'})
        self.assertTrue({'INFANTRY','JUMP PACK','FLY'}<=jump)

    def test_transport_fits(self):
        for name, yes, no in [
            ('Ghost Carrier',['Covered Transport','Recon Fit','Fire Support Fit'],['Recovery Fit']),
            ('Ghostwing Assault Gunship',['Insertion Fit'],['Strike Fit']),
            ('Shadow Gunship',['Extraction/Airlift'],['Strike Sortie']),
        ]:
            for fit in yes:self.assertIn('TRANSPORT',self.keywords(name,[fit]))
            for fit in no:self.assertNotIn('TRANSPORT',self.keywords(name,[fit]))

    def test_keyword_condition_cannot_count_other_units(self):
        r=copy.deepcopy(self.root);u=self.unit('Abandoned Dead Strike Commander',r)
        mod=next(m for m in children(u,'modifiers') if m.get('field')=='category')
        children(mod,'conditions')[0].set('scope','roster')
        self.assertTrue(any('this unit only' in e for e in inspect_keywords(r,self.system)))

if __name__=='__main__':unittest.main()
