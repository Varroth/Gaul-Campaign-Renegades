#!/usr/bin/env python3
"""One-time Frozen Cogs editorial cleanup. Preserve gameplay mechanics and IDs."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

path = Path("Frozen_Cogs.cat")
original = path.read_text(encoding="utf-8")
updated = original
# Remove purely editorial/testing notices, never gameplay constraints.
for name in ("Homebrew development status", "Roster notice"):
    pattern = r'<profile\b[^>]*name="' + re.escape(name) + r'"[^>]*>[\s\S]*?</profile>'
    updated = re.sub(pattern, "", updated)
# Standardize headings while leaving descriptions and all IDs intact.
headings = {
    "Role and doctrine": "Operational Assignment",
    "Equipment detail": "Wargear Effect",
    "Equipment effect": "Wargear Ability",
    "Selected configuration": "Configuration",
}
for old, new in headings.items():
    updated = updated.replace('name="' + old + '" hidden="false" typeId="bd5c-f804-35b5-510d" typeName="Ability"',
                              'name="' + new + '" hidden="false" typeId="bd5c-f804-35b5-510d" typeName="Ability"')
# Eliminate explicit development caveats embedded in otherwise playable rules.
updated = updated.replace(" (min. 1; homebrew)", " (to a minimum of 1)")
updated = updated.replace(" (min 1; homebrew)", " (to a minimum of 1)")
updated = updated.replace(" (homebrew)", "")
# Correct stray spacing before full stops in rules prose.
updated = re.sub(r'(?<=\w) +\.(?=</characteristic>)', '.', updated)
# XML and reference integrity: all original element IDs must survive except removed profiles.
root_before = ET.fromstring(original)
root_after = ET.fromstring(updated)
ns = {"b": "http://www.battlescribe.net/schema/catalogueSchema"}
removed_ids = {p.attrib["id"] for p in root_before.findall(".//b:profile", ns)
               if p.attrib.get("name") in ("Homebrew development status", "Roster notice")}
before_ids = {e.attrib["id"] for e in root_before.iter() if "id" in e.attrib}
after_ids = {e.attrib["id"] for e in root_after.iter() if "id" in e.attrib}
assert before_ids - after_ids == removed_ids, "Unexpected removal of IDs"
assert not (after_ids - before_ids), "Unexpected new IDs"
assert len(list(root_before.iter())) - len(list(root_after.iter())) == 48 * 3, "Unexpected profile structure change"
assert root_before.attrib["id"] == root_after.attrib["id"]
if updated != original:
    path.write_text(updated, encoding="utf-8")
print("Frozen Cogs editorial cleanup complete; XML parsed and IDs preserved.")
