#!/usr/bin/env python3
"""Read-only New Recruit QC for the Frozen Cogs catalogue and shared system."""
from collections import Counter
from pathlib import Path
import argparse, json, math
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS="{http://www.battlescribe.net/schema/catalogueSchema}"
GNS="{http://www.battlescribe.net/schema/gameSystemSchema}"
MODE_NAMES={
 "Plasma gun — standard":"Plasma gun — supercharge",
 "Plasma cannon — standard":"Plasma cannon — supercharge",
 "plasma cannon":"plasma cannon — supercharge",
 "Missile launcher (frag)":"Missile launcher (krak)",
 "combi-flamer":"combi-flamer — bolt mode",
 "combi-plasma":"combi-plasma — bolt mode",
 "combi-melta":"combi-melta — bolt mode",
}
CHAR_FIELDS={"Range","A","BS/WS","S","AP","D","Traits"}

def inspect():
    cat=ET.parse(ROOT/"Frozen_Cogs.cat").getroot()
    gs=ET.parse(ROOT/"Gaul_Campaign_Renegades.gst").getroot()
    errors=[];warning=[];checks={}
    roots=cat.find(NS+"selectionEntries").findall(NS+"selectionEntry")
    checks["root_units"]=len(roots)
    if len(roots)!=164:errors.append(f"Expected 164 root units, found {len(roots)}")
    if any(u.get("type")!="unit" or u.get("import")!="true" for u in roots):
        errors.append("Root-unit type or import flags invalid")
    ids=[node.get("id") for node in cat.iter() if node.get("id")]
    if len(ids)!=len(set(ids)):errors.append(f"{len(ids)-len(set(ids))} duplicate IDs")
    checks["catalogue_ids"]=len(ids)
    if cat.get("gameSystemId")!=gs.get("id") or cat.get("gameSystemRevision")!=gs.get("revision"):
        errors.append("Game system ID/revision mismatch")
    gcats={e.get("id"):e.get("name") for e in gs.findall("./"+GNS+"categoryEntries/"+GNS+"categoryEntry")}
    for e in cat.iter():
        if (e.get("name") or "").startswith("FC · "):
            errors.append(f"Abbreviated category label remains: {e.get('name')}")
        if e.tag==NS+"categoryLink" and e.get("targetId") in gcats and e.get("name")!=gcats[e.get("targetId")]:
            errors.append(f"Category label mismatch {e.get('targetId')}")
    for name in gcats.values():
        if name.startswith("FC · "):errors.append(f"Abbreviated system category remains: {name}")
    for i,u in enumerate(roots[:16]):
        caps=[e for e in u.findall("./"+NS+"constraints/"+NS+"constraint")
              if e.get("scope")=="roster" and e.get("type")=="max"]
        target="6" if u.get("name")=="Tactical Squad" else "3"
        if len(caps)!=1 or caps[0].get("value")!=target:
            errors.append(f"{u.get('name')}: missing/wrong roster-copy cap")
    for e in cat.iter():
        if e.tag==NS+"selectionEntryGroup":
            selections=e.findall("./"+NS+"selectionEntries/"+NS+"selectionEntry")
            choices=e.findall("./"+NS+"selectionEntryLinks/"+NS+"selectionEntryLink")
            default=e.get("defaultSelectionEntryId")
            if default and default not in {x.get("id") for x in selections+choices}:
                errors.append(f"Invalid selection default: {e.get('name')}")
            bounds={c.get("type"):float(c.get("value")) for c in e.findall("./"+NS+"constraints/"+NS+"constraint") if c.get("type") in ("min","max")}
            if "min" in bounds and "max" in bounds and bounds["min"]>bounds["max"]:
                errors.append(f"Invalid group min/max: {e.get('name')}")
        if e.tag==NS+"profile" and e.get("typeName")=="Weapon":
            fields={x.get("name") for x in e.findall("./"+NS+"characteristics/"+NS+"characteristic")}
            if not CHAR_FIELDS.issubset(fields):
                errors.append(f"Weapon {e.get('name')} missing fields {CHAR_FIELDS-fields}")
        if e.tag==NS+"cost":
            try:
                val=float(e.get("value"))
                if not math.isfinite(val) or val<0: errors.append(f"Invalid cost {e.get('value')}")
            except (TypeError, ValueError):
                errors.append(f"Nonnumeric cost {e.get('value')}")
    mode_entries=Counter()
    for e in cat.iter():
        if e.tag!=NS+"selectionEntry" or e.get("name") not in MODE_NAMES:continue
        name=e.get("name")
        wp=[p.get("name") for p in e.findall("./"+NS+"profiles/"+NS+"profile")
            if p.get("typeName")=="Weapon"]
        if MODE_NAMES[name] not in wp:errors.append(f"Missing second mode: {name}/{e.get('id')}")
        else:mode_entries[name]+=1
    checks["dual_mode_options"]=sum(mode_entries.values())
    checks["weapon_profiles"]=sum(e.tag==NS+"profile" and e.get("typeName")=="Weapon" for e in cat.iter())
    checks["choice_groups"]=sum(e.tag==NS+"selectionEntryGroup" for e in cat.iter())
    checks["mode_counts"]=dict(mode_entries)
    if checks["dual_mode_options"]!=59:
        errors.append(f"Expected 59 dual-profile options; got {checks['dual_mode_options']}")
    warning.append("Native per-five/per-ten specialist quotas, cross-model coordination, Leader joins and passenger assignments require in-app/manual verification.")
    return {"status":"FAIL" if errors else "PASS_WITH_LIMITATIONS","errors":errors,"limitations":warning,"checks":checks}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--report",default="frozen-cogs-qc.json")
    args=p.parse_args()
    data=inspect()
    (ROOT/args.report).write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(data,indent=2))
    raise SystemExit(bool(data["errors"]))
