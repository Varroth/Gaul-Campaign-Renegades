#!/usr/bin/env python3
"""Idempotent Frozen Cogs category, weapon-mode and roster limit repair."""
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape
import re, uuid
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "Frozen_Cogs.cat"
GST = ROOT / "Gaul_Campaign_Renegades.gst"
NS = "{http://www.battlescribe.net/schema/catalogueSchema}"
CHAR = (
    ("Range","8aa7-21a6-b6c1-50e6"), ("A","1df3-e803-7074-57ce"),
    ("BS/WS","a16c-0b6c-2681-5f8f"), ("S","846d-1dce-303c-5c75"),
    ("AP","91f2-51a2-9429-5a60"), ("D","14cd-2ade-2ccc-5c11"),
    ("Traits","0f05-4353-204c-511f")
)
MODES = {
 "Plasma gun — standard": ("Plasma gun — supercharge", ('24"','2','3+','8','-3','2','Hazardous; choose one firing mode')),
 "Plasma cannon — standard": ("Plasma cannon — supercharge", ('36"','D3','3+','8','-3','2','Blast; Heavy; Hazardous; choose one firing mode')),
 "plasma cannon": ("plasma cannon — supercharge", ('36"','D3','3+','8','-3','2','Blast; Hazardous; choose one firing mode')),
 "Missile launcher (frag)": ("Missile launcher (krak)", ('48"','1','3+','9','-2','3','Heavy; choose frag OR krak')),
 "combi-flamer": ("combi-flamer — bolt mode", ('24"','2','3+','4','0','1','Choose bolt OR flamer mode')),
 "combi-plasma": ("combi-plasma — bolt mode", ('24"','2','3+','4','0','1','Choose bolt OR plasma mode')),
 "combi-melta": ("combi-melta — bolt mode", ('24"','2','3+','4','0','1','Choose bolt OR melta mode')),
}
UNIT = re.compile(r'<selectionEntry\b(?=[^>]*\btype="unit")[^>]*>')
OPTION = re.compile(
 r'(<selectionEntry\b(?=[^>]*\btype="upgrade")(?=[^>]*\bname="(?:Plasma gun — standard|Plasma cannon — standard|plasma cannon|Missile launcher \(frag\)|combi-flamer|combi-plasma|combi-melta)")[^>]*>)(.*?)(</selectionEntry>)',re.S)

def stable_id(value, salt):
    h=uuid.uuid5(uuid.NAMESPACE_URL, "Gaul-Campaign/Renegades/"+salt+"/"+value).hex[:16]
    return "-".join(h[i:i+4] for i in range(0,16,4))

def profile(entry_id, name, stats):
    opening=(f'<profile id="{stable_id(entry_id,"alt-weapon")}" name="{escape(name)}" '
             'hidden="false" typeId="a4f5-4674-06d7-5496" typeName="Weapon"><characteristics>')
    chars="".join(f'<characteristic name="{n}" typeId="{cid}">{escape(v)}</characteristic>'
                  for (n,cid),v in zip(CHAR,stats))
    return opening+chars+"</characteristics></profile>"

def fix_copy_limits(source):
    root=ET.fromstring(source)
    roots=root.find(NS+"selectionEntries").findall(NS+"selectionEntry")
    if len(roots)!=164: raise ValueError(f"Expected 164 units, got {len(roots)}")
    missing=[e.get("id") for e in roots[:16]
             if not any(c.get("scope")=="roster" and c.get("type")=="max"
                 for c in e.findall("./"+NS+"constraints/"+NS+"constraint"))]
    if missing and len(missing)!=16:
        raise ValueError(f"Partially patched legacy roster copy limits: {len(missing)}")
    if not missing:return source,0
    seen=[0]
    def add(m):
        seen[0]+=1
        tag=m.group()
        if seen[0]>16:return tag
        entry_id=re.search(r'\bid="([^"]+)"',tag).group(1)
        limit=6 if 'name="Frozen Cogs Tactical Squad"' in tag else 3
        cid=stable_id(entry_id,"max-copies")
        return (tag+f'<constraints><constraint id="{cid}" type="max" field="selections" scope="roster" '
                f'value="{limit}" percentValue="false" shared="true" '
                'includeChildSelections="false" includeChildForces="true"/></constraints>')
    source=UNIT.sub(add,source)
    if seen[0]!=164:raise ValueError("Unit matching failed")
    return source,16

def fix_weapon_modes(source):
    counts=Counter()
    def add(m):
        head,body,tail=m.groups()
        name=re.search(r'\bname="([^"]+)"',head).group(1)
        entry_id=re.search(r'\bid="([^"]+)"',head).group(1)
        extra,stats=MODES[name]
        if 'name="'+extra+'"' in body:return m.group(0)
        if "</profiles>" not in body:raise ValueError(f"Profiles absent in {entry_id}")
        if name=="plasma cannon":
            for old,new in (
              (">7/8</characteristic>",">7</characteristic>"),
              (">-2/-3</characteristic>",">-2</characteristic>"),
              (">1/2</characteristic>",">1</characteristic>"),
              ("Standard/Supercharge: Blast; Supercharge also Hazardous","Blast; choose one firing mode")
            ):
                if old not in body:raise ValueError(f"Malformed plasma cannon {entry_id}: {old}")
                body=body.replace(old,new,1)
        body=body.replace("</profiles>",profile(entry_id,extra,stats)+"</profiles>",1)
        counts[name]+=1
        return head+body+tail
    source=OPTION.sub(add,source)
    if counts and sum(counts.values())!=59:raise ValueError(f"Incomplete modes: {dict(counts)}")
    return source,dict(counts)

def main():
    for path in (CAT,GST):
        original=path.read_text(encoding="utf-8")
        corrected=original.replace('name="FC · ', 'name="')
        if path==CAT:
            corrected,caps=fix_copy_limits(corrected)
            corrected,modes=fix_weapon_modes(corrected)
            print(f"Frozen Cogs: added {caps} copy limits, firing-mode profiles {modes}")
        ET.fromstring(corrected)
        if corrected!=original:
            path.write_text(corrected,encoding="utf-8")
            print(f"Updated {path.name}, removed {original.count('name=')-corrected.count('name=')+0} naming artifacts")
        else: print(f"No change in {path.name}")
if __name__=="__main__":main()
