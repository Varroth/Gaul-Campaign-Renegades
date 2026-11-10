"""Regression tests for Infernal Warriors New Recruit browsing and detachment access."""
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
        self.assertEqual(len(self.entries), 100)
        self.assertEqual(sum(e.get("type") == "unit" for e in self.entries), 74)
        self.assertEqual(sum(e.get("type") == "model" for e in self.entries), 22)
        self.assertEqual(sum(e.get("type") == "upgrade" for e in self.entries), 4)
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
        self.assertEqual(len(categories["Army Configuration"]), 4)
        self.assertNotIn("Detachments", categories)
        self.assertEqual(len([n for n in categories["Army Configuration"] if n.startswith("02 — DETACHMENTS:")]), 1)
        self.assertTrue(categories["Army Configuration"][0].startswith("01 — START HERE:"))
        self.assertEqual(categories["Army Configuration"][1],
                         "02 — DETACHMENTS: Choose Detachments")
        self.assertTrue(categories["Army Configuration"][2].startswith("03 — MISSION:"))
        self.assertTrue(categories["Army Configuration"][3].startswith("04 — RULES:"))
        self.assertEqual(len(categories["Characters"]), 22)
        self.assertEqual(len([l for l in children(self.force, "categoryLinks") if l.get("hidden") == "true"]), 0)

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
            "02 — DETACHMENTS: Choose Detachments": "Army Configuration",
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
        ]:
            self.assertIn(old_tag, {l.get("name") for l in children(by_name[name], "categoryLinks")})
        force_links = children(self.force, "categoryLinks")
        selector = by_name["02 — DETACHMENTS: Choose Detachments"]
        groups = children(selector, "selectionEntryGroups")
        self.assertEqual(len(groups), 1)
        group = groups[0]
        self.assertIn("Select Detachments", group.get("name"))
        group_rules = {c.get("type"): c.get("value")
                       for c in children(group, "constraints")}
        self.assertEqual(group_rules, {"min": "1", "max": "4"})
        options = children(group, "selectionEntries")
        self.assertEqual([o.get("name") for o in options], [
            "Breach and Ruin", "Crimson Onslaught", "Iron Reavers", "War Hounds’ Legacy"])
        self.assertEqual(
            {o.get("id") for o in options},
            {"b7ad-18e3-9d4d-57e1", "d6ca-9cbf-e275-5803",
             "5856-87a6-b30e-596e", "8eb0-8d1d-a832-5447"})
        self.assertFalse(any(n.startswith("02 — DETACHMENT: ") for n in by_name))
        dp = {"Breach and Ruin": 1, "Crimson Onslaught": 1,
              "Iron Reavers": 1, "War Hounds’ Legacy": 2}
        for option in options:
            links = children(option, "categoryLinks")
            categories = {l.get("name") for l in links}
            self.assertIn("Detachments", categories)
            self.assertIn("Army Configuration", categories)
            self.assertEqual(sum(l.get("primary") == "true" for l in links), 1)
            costs = children(option, "costs")
            self.assertEqual(
                float(next(c.get("value") for c in costs if c.get("name") == "DP")),
                dp[option.get("name")])
            self.assertTrue(children(option, "profiles"))
            self.assertTrue(children(option, "constraints"))
        for old_tag in ("Command", "Infantry", "Khorne Allies", "Detachments",
                        "Muster Settings", "Force Dispositions"):
            self.assertFalse(any(l.get("name") == old_tag for l in force_links), old_tag)
        for tag in ("Khorne Allies", "Lost Cohort", "Detachments"):
            matching = [e for e in children(self.system, "categoryEntries") if e.get("name") == tag]
            self.assertTrue(matching, tag)
            self.assertTrue(children(matching[0], "constraints"), tag)

if __name__ == "__main__":
    unittest.main()
