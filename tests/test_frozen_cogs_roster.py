import unittest
import xml.etree.ElementTree as ET
from tools.qc_frozen_cogs_roster import validate

def roster(unit, leader, troops, weapons):
    models = [f'<selection name="{leader}" type="model" number="1"><selections/></selection>']
    for i in range(troops):
        item = weapons.get(i, "")
        gear = f'<selection name="{item}" type="upgrade" number="1"/>' if item else ""
        models.append(f'<selection name="{("Devastator Marine" if "Devastator" in unit else "Tactical Marine")} {i+1}" type="model" number="1"><selections>{gear}</selections></selection>')
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
    def test_devastator_four_heavies_allowed(self):
        self.assertFalse(validate(roster("Frozen Cogs Devastator Squad", "Devastator Sergeant", 4,
                                         {0:"Heavy bolter",1:"Lascannon",2:"Multi-melta",3:"Grav cannon"}))["errors"])
    def test_devastator_five_heavies_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Devastator Squad", "Devastator Sergeant", 5,
                                        {0:"Heavy bolter",1:"Lascannon",2:"Multi-melta",3:"Grav cannon",4:"Volkite culverin"}))["errors"])
    def test_tactical_four_models_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 3, {}))["errors"])
    def test_tactical_eleven_models_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Tactical Sergeant", 10, {}))["errors"])
    def test_missing_leader_rejected(self):
        self.assertTrue(validate(roster("Frozen Cogs Tactical Squad", "Not a Sergeant", 4, {}))["errors"])
if __name__ == "__main__":
    unittest.main()
