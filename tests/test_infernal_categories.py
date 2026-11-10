"""Regression tests for the ten Infernal Warriors New Recruit sections."""
import unittest
import xml.etree.ElementTree as ET

from scripts.check_repository import ROOT, children

EXPECTED = [
    "Army Configuration", "Characters", "Battleline", "Infantry & Elites",
    "Lost Cohort", "Dreadnoughts", "Vehicles & Artillery", "Aircraft",
    "Daemon Engines", "Auxiliaries & Allies",
]

class InfernalCategoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(ROOT / "Infernal_Warriors.cat").getroot()
        cls.system = ET.parse(ROOT / "Gaul_Campaign_Renegades.gst").getroot()
        cls.force = next(f for f in children(cls.system, "forceEntries")
                         if f.get("id") == "73a9-6482-df85-55c4")
        cls.entries = children(cls.root, "selectionEntries")

    def test_visible_browse_sections_and_root_entries(self):
        links = children(self.force, "categoryLinks")
        shown = [l for l in links if l.get("hidden") != "true"]
        self.assertEqual([l.get("name") for l in shown], EXPECTED)
        self.assertEqual(len(self.entries), 103)
        self.assertEqual(sum(e.get("type") == "unit" for e in self.entries), 74)
        self.assertEqual(sum(e.get("type") == "model" for e in self.entries), 22)
        self.assertEqual(sum(e.get("type") == "upgrade" for e in self.entries), 7)
        visible_targets = {l.get("targetId") for l in shown}
        groups = {l.get("targetId"): l.get("name") for l in shown}
        categories = {}
        for entry in self.entries:
            links = children(entry, "categoryLinks")
            primary = [l for l in links if l.get("primary") == "true"]
            self.assertEqual(len(primary), 1, entry.get("name"))
            self.assertIn(primary[0].get("targetId"), visible_targets, entry.get("name"))
            self.assertEqual(len(links), len({l.get("targetId") for l in links}), entry.get("name"))
            name = groups[primary[0].get("targetId")]
            categories.setdefault(name, []).append(entry.get("name"))
        self.assertEqual(set(categories), set(EXPECTED))

    def test_unique_formation_and_old_rules_tags_remain(self):
        by_name = {e.get("name"): e for e in self.entries}
        section_ids = {l.get("targetId"): l.get("name") for l in children(self.force, "categoryLinks")
                       if l.get("hidden") != "true"}
        samples = {
            "Balan Bannon": "Characters",
            "Infernal Berzerkers": "Battleline",
            "Ashen Chain Terminators": "Infantry & Elites",
            "Lost Cohort — Power Armour": "Lost Cohort",
            "Contemptor Relic Dreadnought": "Dreadnoughts",
            "Rhino Carrier": "Vehicles & Artillery",
            "Thunderhawk Gunship": "Aircraft",
            "Blood Slaughterer": "Daemon Engines",
            "Bloodmarked Thralls": "Auxiliaries & Allies",
            "Bloodletters": "Auxiliaries & Allies",
            "01 — START HERE: Battle Size & Enhancements": "Army Configuration",
        }
        for name, expected in samples.items():
            if name not in by_name and name.startswith("01 — "):
                name = next(n for n in by_name if n.startswith("01 — START HERE"))
            links = children(by_name[name], "categoryLinks")
            primary = next(l for l in links if l.get("primary") == "true")
            self.assertEqual(section_ids[primary.get("targetId")], expected)
        for name, old_tag in [
            ("Bloodletters", "Khorne Allies"),
            ("Lost Cohort — Power Armour", "Lost Cohort"),
            ("DETACHMENT — Iron Reavers", "Detachments"),
        ]:
            self.assertIn(old_tag, {l.get("name") for l in children(by_name[name], "categoryLinks")})
        force_links = children(self.force, "categoryLinks")
        for old_tag in ("Command", "Infantry", "Khorne Allies", "Detachments",
                        "Muster Settings", "Force Dispositions"):
            self.assertFalse(any(l.get("name") == old_tag for l in force_links), old_tag)
        for tag in ("Khorne Allies", "Lost Cohort", "Detachments"):
            matching = [e for e in children(self.system, "categoryEntries") if e.get("name") == tag]
            self.assertTrue(matching, tag)
            self.assertTrue(children(matching[0], "constraints"), tag)

if __name__ == "__main__":
    unittest.main()
