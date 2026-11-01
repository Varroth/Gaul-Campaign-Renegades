#!/usr/bin/env python3
"""Add New Recruit-native squad quota categories to Frozen Cogs r18.

Shared category constraints count matching equipment across the parent squad.
This is a candidate implementation; New Recruit runtime validation is owner-led.
"""
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

PATH=Path("Frozen_Cogs.cat")
NS="http://www.battlescribe.net/schema/catalogueSchema"
ET.register_namespace("",NS)
q=lambda x:f"{{{NS}}}{x}"
def uid(label):
    return str(uuid.uuid5(uuid.NAMESPACE_URL,"gaul/frozen-cogs/r19/"+label))[:18].replace("-","")[:4]+"-"+str(uuid.uuid5(uuid.NAMESPACE_URL,"gaul/frozen-cogs/r19/"+label)).replace("-","")[4:8]+"-"+str(uuid.uuid5(uuid.NAMESPACE_URL,"gaul/frozen-cogs/r19/"+label)).replace("-","")[8:12]+"-"+str(uuid.uuid5(uuid.NAMESPACE_URL,"gaul/frozen-cogs/r19/"+label)).replace("-","")[12:16]
def child(parent,name):
    found=parent.find(q(name))
    if found is None: found=ET.SubElement(parent,q(name))
    return found
root=ET.parse(PATH).getroot()
if root.get("revision")=="19":
    print("Already r19");raise SystemExit(0)
assert root.get("revision")=="18",root.get("revision")
units={x.get("name"):x for x in root.find(q("selectionEntries")) if x.get("type")=="unit"}
category_defs=child(root,"categoryEntries")
rules=[
 ("Frozen Cogs Tactical Squad","Special weapons",{"Volkite charger","Flamer","Meltagun","Plasma gun — standard"},1),
 ("Frozen Cogs Tactical Squad","Heavy weapons",{"Heavy bolter","Missile launcher (frag)","Lascannon"},1),
 ("Frozen Cogs Devastator Squad","Heavy weapons",{"Heavy bolter","Reaper-style autocannon","Lascannon","Missile launcher (frag)","Plasma cannon — standard","Multi-melta","Grav cannon","Volkite culverin"},4)
]
counts={}
for unit_name,label,options,limit in rules:
    unit=units[unit_name]
    cat_id=uid(unit_name+"/"+label)
    category=ET.SubElement(category_defs,q("categoryEntry"),{"id":cat_id,"name":unit_name+" — "+label,"hidden":"true"})
    # Each matching weapon is tagged with the same category, allowing the category
    # limit to aggregate across the unit's independently selectable Marine models.
    con=child(category,"constraints")
    cid=uid(unit_name+"/"+label+"/max")
    ET.SubElement(con,q("constraint"),{"id":cid,"type":"max","field":"selections","scope":unit.get("id"),"value":str(limit),"shared":"true","includeChildSelections":"true","includeChildForces":"false"})
    if unit_name=="Frozen Cogs Tactical Squad":
        # The second special weapon and first heavy weapon are only legal
        # when Marine 9 is present (10 models including Sergeant).
        marine9=next(x for x in unit.iter(q("selectionEntry")) if x.get("name")=="Tactical Marine 9" and x.get("type")=="model")
        mods=child(category,"modifiers")
        if label=="Special weapons":
            mod=ET.SubElement(mods,q("modifier"),{"type":"set","field":cid,"value":"2"})
            cond_type="atLeast"; val="1"
        else:
            # At 5–9 models the heavy allowance is zero.
            mod=ET.SubElement(mods,q("modifier"),{"type":"set","field":cid,"value":"0"})
            cond_type="lessThan"; val="1"
        conds=child(mod,"conditions")
        ET.SubElement(conds,q("condition"),{"type":cond_type,"value":val,"field":"selections","scope":unit.get("id"),"childId":marine9.get("id"),"shared":"true","includeChildSelections":"true","includeChildForces":"false"})
    found=0
    for model in unit.iter(q("selectionEntry")):
        if model.get("type")!="model":continue
        for weapon in model.iter(q("selectionEntry")):
            if weapon.get("type")!="upgrade" or weapon.get("name") not in options:continue
            links=child(weapon,"categoryLinks")
            ET.SubElement(links,q("categoryLink"),{"id":uid(unit_name+"/"+label+"/"+weapon.get("id")),"name":category.get("name"),"targetId":cat_id,"hidden":"false","primary":"false"})
            found+=1
    assert found>0,(unit_name,label)
    counts[unit_name+"/"+label]=found
root.set("revision","19")
ET.ElementTree(root).write(PATH,encoding="utf-8",xml_declaration=True)
ET.parse(PATH)
print("Native category quota constraints added:",counts)
