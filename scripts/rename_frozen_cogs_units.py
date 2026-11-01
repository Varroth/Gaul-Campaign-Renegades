#!/usr/bin/env python3
"""Frozen Cogs unit-name cleanup: remove redundant catalogue prefix from entry labels."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

path = Path("Frozen_Cogs.cat")
before = path.read_text(encoding="utf-8")
pattern = re.compile(r'(<selectionEntry\b[^>]*\bname=")Frozen Cogs (?=[^"]+)')
after, count = pattern.subn(r'\1', before)
old = ET.fromstring(before)
new = ET.fromstring(after)
ns = {"b": "http://www.battlescribe.net/schema/catalogueSchema"}
old_entries = old.findall(".//b:selectionEntry", ns)
new_entries = new.findall(".//b:selectionEntry", ns)
assert len(old_entries) == len(new_entries)
changes = []
for a, b in zip(old_entries, new_entries):
    assert a.attrib["id"] == b.attrib["id"], "Entry ID changed"
    if a.attrib["name"] != b.attrib["name"]:
        assert a.attrib["name"] == "Frozen Cogs " + b.attrib["name"], "Unexpected rename"
        changes.append((a.attrib["name"], b.attrib["name"]))
assert len(changes) == count, "Rename count mismatch"
# All changes must be limited to the selectionEntry name attributes.
assert old.attrib["id"] == new.attrib["id"]
if after != before:
    path.write_text(after, encoding="utf-8")
print(f"Renamed {count} Frozen Cogs unit/model entries; IDs, wargear, rules and points preserved.")
