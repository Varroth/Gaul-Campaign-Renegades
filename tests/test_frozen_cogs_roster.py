import unittest
import xml.etree.ElementTree as ET
from tools.qc_frozen_cogs_roster import validate

def roster(unit, leader, troops, weapons):
    models = [f'<selection name="{leader}" type="model" number="1"><selections/></selection>']
    for i in range(troops):
        item = weapons.get(i, "")
        gear = f'<selection name="{item}" type="upgrade" number="1"/>' if item else ""
        models.append(f'<selection name="Tactical Marine {i+1}" type="model" number="1"><selections>{gear}</selections></selection>')
    return ET.fromstring('<roster><selections><selection name="'+unit+'" type="unit"><selections>'+''.join(models)+'</selections></selection></selections></roster>')
class RosterTests(unittest.TestCase):
    def test_tactical_five_one_special(self):
        self.assertFalse(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 4, {0:"Flamer"}))["errors"])
    def test_tactical_five_two_specials_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 4, {0:"Flamer",1:"Meltagun"}))["errors"])
    def test_tactical_five_heavy_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 4, {0:"Lascannon"}))["errors"])
    def test_tactical_ten_one_heavy_allowed(self):
        self.assertFalse(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 9, {0:"Lascannon",1:"Flamer",2:"Meltagun"}))["errors"])
    def test_tactical_ten_two_heavy_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 9, {0:"Lascannon",1:"Heavy bolter"}))["errors"])
if __name__ == "__main__":
    unittest.main()
