#!/usr/bin/env python3
"""Consolidate Frozen Cogs roster browsing into nine categories.

Only primary categoryLink flags/targets and new category definitions are changed.
All original category links remain as secondary links to preserve unit keywords.
"""
from collections import Counter
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

PATH=Path(__file__).resolve().parents[1]/"Frozen_Cogs.cat"
NS="{http://www.battlescribe.net/schema/catalogueSchema}"
ET.register_namespace("", NS[1:-1])
GROUPS=("Characters","Battleline","Infantry","Dreadnoughts & Automata",
        "Vehicles","Aircraft","Daemon Engines","Auxiliaries","Silver Tempests")
SPECIAL={"Silver Tempests","Frostbound Auxilia"}
VEHICLE_GROUPS={"Armored Transports","Battle Tanks","Siege Armor",
                "Relic Super-heavy Vehicles","Drop Assault","Speeders & Reconnaissance"}
INFANTRY_GROUPS={"Elite Siege Infantry","Heavy Support","Siege Assault","Melee Shock",
                 "Elite Wardens","Siege Artillery","Assault Infantry","Scouts & Recon",
                 "Combat Engineers","Veterans","Tactical Support","Bikes & Jetbikes"}
def child(node,name):return node.find(NS+name)
def children(node,name):return node.findall(NS+name)
def new_id(key):return str(uuid.uuid5(uuid.NAMESPACE_URL,"gaul-frozen-cogs-categories-v1/"+key))
def select_group(unit,old,keywords):
    name=unit.get("name")
    if old=="Silver Tempests":return "Silver Tempests"
    if old=="Frostbound Auxilia":return "Auxiliaries"
    if old=="Contained Daemon Engines" or "DAEMON ENGINE" in keywords:return "Daemon Engines"
    if old in {"Dreadnoughts & Living Masters","Sacred Forge Walkers","Automata"} or "DREADNOUGHT" in keywords or "AUTOMATA" in keywords:
        return "Dreadnoughts & Automata"
    if old in {"Aircraft & Gunships","Aerial Aces"} or "AIRCRAFT" in keywords:return "Aircraft"
    if old in {"Chapter Command","Named Characters"} or "CHARACTER" in keywords or "LEADER" in keywords:return "Characters"
    if old=="Battleline":return "Battleline"
    if old in VEHICLE_GROUPS or "VEHICLE" in keywords:return "Vehicles"
    if name in {"Iron Firewall Relay Node","Coldforge Field Fabricator","Canticle Relay Spire"}:
        return "Vehicles"
    if old in INFANTRY_GROUPS or old in {"Sacred Forge Support","Harmonic Conclave"} or "INFANTRY" in keywords or "MOUNTED" in keywords:
        return "Infantry"
    # Uncrewed relay nodes and field fabricators are equipment/vehicle support.
    raise ValueError(f"Unclassified unit: {name} / {old} / {sorted(keywords)}")
def run():
    tree=ET.parse(PATH);root=tree.getroot()
    cats=child(root,"categoryEntries")
    entries=child(root,"selectionEntries")
    if cats is None or entries is None:raise ValueError("Missing catalogue category/selection containers")
    by_name={e.get("name"):e for e in children(cats,"categoryEntry")}
    by_id={e.get("id"):e.get("name") for e in children(cats,"categoryEntry")}
    for group in GROUPS:
        if group not in by_name:
            c=ET.SubElement(cats,NS+"categoryEntry",{"id":new_id(group),"name":group,"hidden":"false"})
            by_name[group]=c;by_id[c.get("id")]=group
    counts=Counter()
    units=[u for u in children(entries,"selectionEntry") if u.get("type")=="unit"]
    if len(units)!=169:raise ValueError(f"Expected 169 root units, found {len(units)}")
    for unit in units:
        links=child(unit,"categoryLinks")
        if links is None:raise ValueError(f"Missing category links: {unit.get('name')}")
        all_links=children(links,"categoryLink")
        primary=[l for l in all_links if l.get("primary")=="true"]
        if len(primary)!=1:raise ValueError(f"Expected one primary category for {unit.get('name')}")
        old=primary[0].get("name")
        keys={l.get("name","").upper() for l in all_links}
        group=select_group(unit,old,keys)
        target=by_name[group].get("id")
        matches=[l for l in all_links if l.get("targetId")==target]
        if matches:
            chosen=matches[0]
        else:
            chosen=ET.SubElement(links,NS+"categoryLink",{
                "id":new_id(unit.get("id")+"/"+group),
                "name":group,"targetId":target,"hidden":"false","primary":"false"})
        for l in all_links:l.set("primary","false")
        chosen.set("primary","true")
        counts[group]+=1
    if len(counts)!=len(GROUPS) or sum(counts.values())!=169:
        raise ValueError(f"Unexpected grouping counts: {counts}")
    if counts["Silver Tempests"]!=5:raise ValueError("Silver Tempests must contain five units")
    tree.write(PATH,encoding="utf-8",xml_declaration=True)
    print("Nine primary roster categories:",dict(counts))
if __name__=="__main__":run()
