#!/usr/bin/env python3
"""Frozen Cogs non-mutating catalogue integrity audit (Python standard library)."""
from collections import Counter
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "Frozen_Cogs.cat"
GST = ROOT / "Gaul_Campaign_Renegades.gst"
NS = {"b": "http://www.battlescribe.net/schema/catalogueSchema"}
def local(tag):
    return tag.rsplit("}", 1)[-1]
def main():
    errors, warnings = [], []
    try:
        cat, gst = ET.parse(CAT).getroot(), ET.parse(GST).getroot()
    except (OSError, ET.ParseError) as exc:
        print("FAIL: XML unreadable:", exc)
        return 1
    for label, root in (("catalogue", cat), ("game system", gst)):
        ids = [e.attrib["id"] for e in root.iter() if "id" in e.attrib]
        duplicates = [key for key, n in Counter(ids).items() if n > 1]
        if duplicates:
            errors.append(f"{label}: {len(duplicates)} duplicate IDs: {duplicates[:8]}")
    if cat.get("gameSystemId") != gst.get("id"):
        errors.append("Frozen Cogs gameSystemId does not match game-system id")
    if cat.get("gameSystemRevision") != gst.get("revision"):
        errors.append("Frozen Cogs gameSystemRevision does not match current .gst revision")
    entries = [e for e in cat.iter() if local(e.tag) == "selectionEntry"]
    # Count only entries directly beneath the root's selectionEntries collection.
    root_entries = next((e for e in cat if local(e.tag) == "selectionEntries"), None)
    units = [e for e in root_entries if local(e.tag) == "selectionEntry" and e.get("type") == "unit"] if root_entries is not None else []
    if len(units) != 164:
        warnings.append(f"Top-level unit count is {len(units)}; release baseline is 164")
    for e in cat.iter():
        if local(e.tag) != "constraint":
            continue
        try:
            value = float(e.get("value", "nan"))
            if value < 0:
                warnings.append(f"Negative constraint value: {e.get('id')}")
        except ValueError:
            errors.append(f"Invalid numeric constraint: {e.get('id')}")
    # Inspect representative Evolving Arsenal squads without changing their rules.
    representative = [
        "Wintergrave Siege Terminators", "Frostglass Interdictors",
        "IceBreaker Breachers", "IceBreaker Terminators",
        "Frozen Cogs Tactical Squad", "Frozen Cogs Devastator Squad",
    ]
    arsenal = []
    for name in representative:
        unit = next((u for u in units if u.get("name") == name), None)
        if unit is None:
            errors.append(f"Missing baseline squad: {name}")
            continue
        models = [e for e in unit.iter() if local(e.tag) == "selectionEntry"
                  and e.get("type") == "model"]
        groups = [e for e in unit.iter() if local(e.tag) == "selectionEntryGroup"]
        scopes = Counter(e.get("scope", "") for e in unit.iter()
                         if local(e.tag) == "constraint")
        if len(models) != 10:
            warnings.append(f"{name}: {len(models)} model slots, expected 10")
        if not groups:
            warnings.append(f"{name}: no native selectable equipment groups")
        # Parent-scope limits alone do not prove a cross-model per-five cap.
        if scopes.get("parent", 0) and not any(
            key not in ("parent", "roster") for key in scopes
        ):
            warnings.append(f"{name}: only parent/roster constraint scopes; "
                            "cross-model weapon quotas require manual validation")
        arsenal.append({"unit": name, "model_slots": len(models),
                        "equipment_groups": len(groups),
                        "constraint_scopes": dict(scopes)})
    result = {"catalogue_revision": cat.get("revision"),
              "system_revision": gst.get("revision"), "top_level_units": len(units),
              "selection_entries": len(entries),
              "selection_groups": sum(local(e.tag) == "selectionEntryGroup" for e in cat.iter()),
              "constraints": sum(local(e.tag) == "constraint" for e in cat.iter()),
              "arsenal_sample": arsenal, "errors": errors, "warnings": warnings[:50]}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0
if __name__ == "__main__":
    sys.exit(main())
