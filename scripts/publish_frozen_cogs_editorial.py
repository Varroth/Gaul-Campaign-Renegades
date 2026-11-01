#!/usr/bin/env python3
"""Frozen Cogs editorial package 1: remove non-gameplay development notices."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

path = Path("Frozen_Cogs.cat")
before = path.read_text(encoding="utf-8")
# This first package removes ONLY explicit preliminary-development disclaimers.
pattern = r'<profile\b[^>]*name="Homebrew development status"[^>]*>[\s\S]*?</profile>'
after, count = re.subn(pattern, "", before)
old = ET.fromstring(before)
new = ET.fromstring(after)
ns = {"b": "http://www.battlescribe.net/schema/catalogueSchema"}
removed = {p.attrib["id"] for p in old.findall(".//b:profile", ns)
           if p.attrib.get("name") == "Homebrew development status"}
ids = lambda root: {e.attrib["id"] for e in root.iter() if "id" in e.attrib}
assert ids(old) - ids(new) == removed, "Unexpected deleted IDs"
assert not (ids(new) - ids(old)), "Unexpected new IDs"
assert count == len(removed), "Removal count mismatch"
assert old.attrib["id"] == new.attrib["id"]
if after != before:
    path.write_text(after, encoding="utf-8")
print(f"Package 1: removed {count} development notices; all other rules unchanged.")
