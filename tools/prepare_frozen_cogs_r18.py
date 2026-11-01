#!/usr/bin/env python3
"""Prepare Frozen Cogs New Recruit release 18 from the existing catalogue.

No undocumented gameplay rules are introduced. This release preserves every
selection ID and weapon profile and clarifies which quotas remain manual.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

PATH = Path("Frozen_Cogs.cat")
old = PATH.read_text(encoding="utf-8")
if 'name="Frozen Cogs" revision="18"' in old:
    print("Frozen Cogs is already revision 18; no update necessary.")
    raise SystemExit(0)
assert 'name="Frozen Cogs" revision="17"' in old, "Expected release 17"
new = old.replace('name="Frozen Cogs" revision="17"',
                  'name="Frozen Cogs" revision="18"', 1)
old_note = "native cross-model constraints pending actual New Recruit import/verification."
new_note = ("New Recruit r18: individual weapons are selectable; cross-model "
            "special/heavy quotas remain manual pending native validation. "
            "Use the stated squad allowances when building a roster.")
new = new.replace(old_note, new_note)
assert new != old
ET.fromstring(new)
PATH.write_text(new, encoding="utf-8")
print(f"Updated Frozen Cogs to revision 18; {old.count(old_note)} roster notes clarified.")
