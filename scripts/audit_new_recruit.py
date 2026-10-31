#!/usr/bin/env python3
"""Read-only, conservative BattleScribe/New Recruit repository QC."""
import argparse
import json
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = "{http://www.battlescribe.net/schema/"
REF_ATTRS = ("targetId", "typeId", "defaultSelectionEntryId")
COST_TAGS = {"cost", "costLimit"}
PROFILE_TAGS = {"profile", "profileType", "characteristic", "characteristicType"}
def local(tag):
    return tag.rsplit("}", 1)[-1]

def inspect():
    errors, warnings, inventory = [], [], []
    paths = [ROOT / "Gaul_Campaign_Renegades.gst"] + sorted(ROOT.glob("*.cat"))
    if len(paths) < 2:
        errors.append("Expected game system and at least one catalogue")
    roots = {}
    for path in paths:
        try:
            roots[path.name] = ET.parse(path).getroot()
        except (ET.ParseError, OSError, UnicodeError) as exc:
            errors.append(f"{path.name}: cannot parse XML: {exc}")
    system = roots.get("Gaul_Campaign_Renegades.gst")
    if system is None:
        return errors, warnings, inventory
    sid, srev = system.get("id"), system.get("revision")
    if local(system.tag) != "gameSystem" or not sid or not (srev or "").isdigit():
        errors.append("Game-system root missing valid ID or revision")
    all_ids = set()
    per_file = {}
    for name, root in roots.items():
        ids = [e.get("id") for e in root.iter() if e.get("id")]
        counts = Counter(ids)
        repeated = [k for k, n in counts.items() if n > 1]
        if repeated:
            warnings.append(f"{name}: {len(repeated)} IDs repeated within file (inspect before changing)")
        per_file[name] = set(ids)
        all_ids.update(ids)
        if name.endswith(".cat"):
            if local(root.tag) != "catalogue":
                errors.append(f"{name}: not a catalogue root")
            if root.get("gameSystemId") != sid or root.get("gameSystemRevision") != srev:
                errors.append(f"{name}: shared game-system ID/revision mismatch")
            if not (root.get("revision") or "").isdigit():
                errors.append(f"{name}: missing numeric catalogue revision")
        broken_costs = []
        for e in root.iter():
            if local(e.tag) in COST_TAGS and e.get("value") is not None:
                try:
                    float(e.get("value"))
                except ValueError:
                    broken_costs.append(e.get("id") or local(e.tag))
        if broken_costs:
            errors.append(f"{name}: {len(broken_costs)} nonnumeric cost values")
        inventory.append({"file": name, "root_id": root.get("id"),
                          "revision": root.get("revision"),
                          "elements": sum(1 for _ in root.iter()),
                          "unique_ids": len(per_file[name]),
                          "selection_entries": sum(local(e.tag) == "selectionEntry" for e in root.iter())})
    # Many BattleScribe references intentionally point to shared or imported libraries.
    # Report unknown targets for review, never automatically rewrite them.
    for name, root in roots.items():
        unknown = Counter()
        for e in root.iter():
            for attr in REF_ATTRS:
                target = e.get(attr)
                if target and target not in all_ids:
                    unknown[attr] += 1
        if unknown:
            warnings.append(f"{name}: unresolved reference candidates {dict(unknown)} (may be external/built-in)")
    return errors, warnings, inventory

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="new-recruit-qc.json")
    args = parser.parse_args()
    errors, warnings, inventory = inspect()
    report = {"status": "FAIL" if errors else "PASS_WITH_WARNINGS" if warnings else "PASS",
              "errors": errors, "warnings": warnings, "inventory": inventory,
              "scope": "XML structure, system metadata, duplicate-ID candidates, numeric costs, reference candidates. Not gameplay or New Recruit UI validation."}
    Path(args.report).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if errors else 0)
if __name__ == "__main__":
    main()
