#!/usr/bin/env python3
"""Validate exported uncompressed New Recruit/BattleScribe .ros squad loadouts.

This is a supplementary external checker, NOT a substitute for native editor rules.
Uses existing published Frozen Cogs squad descriptions; no gameplay rules changed.
"""
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

HEAVY_TACTICAL = {"Heavy bolter", "Missile launcher (frag)", "Lascannon"}
SPECIAL_TACTICAL = {"Volkite charger", "Flamer", "Meltagun", "Plasma gun — standard"}
HEAVY_DEVASTATOR = {"Heavy bolter", "Reaper-style autocannon", "Lascannon",
                    "Missile launcher (frag)", "Plasma cannon — standard",
                    "Multi-melta", "Grav cannon", "Volkite culverin"}
SQUADS = {
    "Frozen Cogs Tactical Squad": ("Tactical Sergeant", "Tactical Marine"),
    "Frozen Cogs Devastator Squad": ("Devastator Sergeant", "Devastator Marine"),
    "Wintergrave Siege Terminators": ("Wintergrave Siege-Master", "Wintergrave Terminator"),
    "Frostglass Interdictors": ("Frostglass Sightmaster", "Frostglass Interdictor"),
    "IceBreaker Breachers": ("IceBreaker Breach-Sergeant", "IceBreaker Breacher"),
    "IceBreaker Terminators": ("IceBreaker Siege-Sergeant", "IceBreaker Terminator"),
}
def lname(el):
    return el.tag.rsplit("}", 1)[-1]
def direct_children(el):
    for child in el:
        if lname(child) == "selections":
            yield from (x for x in child if lname(x) == "selection")
def descendants(el):
    for child in el.iter():
        if child is not el and lname(child) == "selection":
            yield child
def validate(root):
    problems, checked = [], []
    for unit in root.iter():
        if lname(unit) != "selection" or unit.get("name") not in SQUADS:
            continue
        name = unit.get("name")
        leader, troop = SQUADS[name]
        models = [x for x in direct_children(unit) if x.get("type") == "model"]
        if not models:
            problems.append(f"{name}: no individual model selections found (unsupported export structure)")
            continue
        count = sum(int(x.get("number", "1")) for x in models)
        leaders = sum(int(x.get("number", "1")) for x in models if x.get("name") == leader)
        if not 5 <= count <= 10:
            problems.append(f"{name}: {count} models; permitted 5–10")
        if leaders != 1:
            problems.append(f"{name}: requires exactly one {leader}; found {leaders}")
        if any(not (x.get("name") == leader or x.get("name", "").startswith(troop)) for x in models):
            problems.append(f"{name}: unexpected model entry")
        selected = [(model, [e.get("name", "") for e in descendants(model)])
                    for model in models]
        if name == "Frozen Cogs Tactical Squad":
            specials = sum(any(w in SPECIAL_TACTICAL for w in opts) for _, opts in selected)
            heavies = sum(any(w in HEAVY_TACTICAL for w in opts) for _, opts in selected)
            if specials > count // 5:
                problems.append(f"{name}: {specials} special weapons; maximum {count // 5}")
            if heavies > count // 10:
                problems.append(f"{name}: {heavies} heavy weapons; maximum {count // 10}")
            for model, opts in selected:
                if model.get("name") == leader and any(w in SPECIAL_TACTICAL | HEAVY_TACTICAL for w in opts):
                    problems.append(f"{name}: sergeant may not take special/heavy weapon")
        if name == "Frozen Cogs Devastator Squad":
            heavies = sum(any(w in HEAVY_DEVASTATOR for w in opts) for _, opts in selected)
            if heavies > 4:
                problems.append(f"{name}: {heavies} heavy weapons; maximum 4")
            for model, opts in selected:
                if model.get("name") == leader and any(w in HEAVY_DEVASTATOR for w in opts):
                    problems.append(f"{name}: sergeant may not take heavy weapon")
        checked.append({"unit": name, "models": count, "leader_count": leaders})
    return {"checked": checked, "errors": problems,
            "limitations": ["Other specialist equipment quotas require per-unit rules mapping",
                            "Leader attachments, transport passenger limits and game timing not checked",
                            "Native New Recruit behavior not verified"]}
def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("roster", type=Path, help="Uncompressed .ros XML file")
    args = p.parse_args()
    try:
        result = validate(ET.parse(args.roster).getroot())
    except (OSError, ET.ParseError) as exc:
        print(f"Invalid roster XML: {exc}")
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result["errors"] else 0
if __name__ == "__main__":
    raise SystemExit(main())
