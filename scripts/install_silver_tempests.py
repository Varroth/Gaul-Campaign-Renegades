#!/usr/bin/env python3
"""Idempotently install Silver Tempests as a dedicated Frozen Cogs category."""
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

PATH = Path(__file__).resolve().parents[1] / "Frozen_Cogs.cat"
NS = "http://www.battlescribe.net/schema/catalogueSchema"
ET.register_namespace("", NS)
def q(tag): return "{%s}%s" % (NS, tag)
def add(parent, tag, **attrs): return ET.SubElement(parent, q(tag), attrs)
def uid(key): return str(uuid.uuid5(uuid.NAMESPACE_URL, "gaul-silver-tempests-v1/" + key))
def el(parent, tag, key, **attrs): return add(parent, tag, id=uid(key), **attrs)
def characteristic(parent, name, typeid, value): add(parent, "characteristic", name=name, typeId=typeid).text=str(value)

CAT = uid("category")
KW = {"ASTARTES":"adbd-c48e-4b21-a001", "CHAOS":"f3a9-cba5-9153-4501",
      "PSYKER":"24cb-d5b2-6056-59d1", "Infantry":"d640-7a85-a199-c350",
      "VEHICLE":"e9b8-90bf-98a0-69e0", "WALKER":"75e8-ab1d-0a0f-89f1",
      "DREADNOUGHT":"61bb-d5dd-f5e7-e5d5", "LEADER":"962b-fca8-d881-0729",
      "JUMP PACK":"625d-1d06-b00a-9f58"}
STATS = {"M":"8ffa-8367-2184-5557","T":"c2bc-ad63-c63b-5cea",
         "Sv":"f078-5176-43c6-5f6a","W":"ecdc-11e1-15d1-5780",
         "Ld":"2bb6-cceb-9d3f-5f47","OC":"6bb9-f7e0-3ec4-5517",
         "Invulnerable":"fcc9-7d25-7e12-9146"}
WEAPON = {"Range":"8aa7-21a6-b6c1-50e6","A":"1df3-e803-7074-57ce",
          "BS/WS":"a16c-0b6c-2681-5f8f","S":"846d-1dce-303c-5c75",
          "AP":"91f2-51a2-9429-5a60","D":"14cd-2ade-2ccc-5c11",
          "Traits":"0f05-4353-204c-511f"}
POWERS = [
 ("Stormspark", "The Sergeant gains Stormspark, a Psychic ranged weapon."),
 ("Warding Current", "Once per battle round, when targeted by ranged attacks, this unit gains a 5+ invulnerable save until the end of the phase."),
 ("Hunter's Premonition", "Once per turn, re-roll one Hit roll when this unit shoots or fights."),
 ("Veil of the Tempest", "Once per battle round, at the start of the enemy Shooting phase, this unit gains Stealth until the end of the phase."),
 ("Omen of the Hunt", "Once per battle round, re-roll this unit's Advance roll.")]
DISCIPLINES = [
 ("Thunderous Hand", "The Stormseer gains Tempest Lance."),
 ("Unbroken Shoal", "The attached unit has a 5+ invulnerable save, unless it has a better save."),
 ("Veiled Current", "The attached unit has Stealth."),
 ("Hunter's Foresight", "Once per turn, the attached unit can re-roll one Hit roll and one Wound roll."),
 ("Eye Beyond the Storm", "Once per battle, the attached unit can re-roll a Charge roll after arriving using Deep Strike.")]
UNITS = [
 ("Stormseer",90,("6\"",4,"3+",4,"6+",1,"—"),["Infantry","ASTARTES","CHAOS","PSYKER","LEADER"],1,
  [("Psychic discipline",DISCIPLINES),("Armour",[("Power armour","3+ save."),("Terminator armour","2+ save, 4+ invulnerable save; may lead Silver Fang Terminators.")]),("Force weapon",[("Force staff","Melee, A4, WS3+, S6, AP-2, D2."),("Force sword","Melee, A4, WS3+, S6, AP-2, D2.")])]),
 ("Tidebound Intervention Squad",105,("6\"",4,"3+",2,"6+",2,"—"),["Infantry","ASTARTES","CHAOS","PSYKER"],3,
  [("Squad size",[("5 models","Five models total."),("10 models","Ten models total; +100 pts.")]),("Stormbound Sergeant manifestation",POWERS),("Special weapon",[("Bolters only","Standard boltguns."),("Plasma gun","One special weapon per five models."),("Meltagun","One special weapon per five models.")])]),
 ("Silver Fang Terminators",195,("5\"",5,"2+",3,"6+",1,"4+"),["Infantry","ASTARTES","CHAOS","PSYKER"],3,
  [("Squad size",[("5 models","Five models total."),("10 models","Ten models total; +190 pts.")]),("Stormbound Sergeant manifestation",POWERS),("Melee armament",[("Power fists","Power fists."),("Chainfists","Chainfists.")]),("Heavy weapon",[("Storm bolters","Storm bolters."),("Heavy flamer","One per five models."),("Reaper autocannon","One per five models.")])]),
 ("Tempest Talons",115,("12\"",4,"3+",2,"6+",1,"—"),["Infantry","ASTARTES","CHAOS","PSYKER","JUMP PACK"],3,
  [("Squad size",[("5 models","Five models total."),("10 models","Ten models total; +110 pts.")]),("Stormbound Sergeant manifestation",POWERS),("Sergeant weapon",[("Chainsword","Astartes chainsword."),("Power weapon","Power weapon.")])]),
 ("Stormheart Dreadnought",195,("8\"",9,"2+",10,"6+",3,"5+"),["VEHICLE","WALKER","DREADNOUGHT","ASTARTES","CHAOS","PSYKER"],1,
  [("Stormheart conduit",[("Tempest Lance","Gain the Tempest Lance psychic ranged weapon."),("Aegis of Iron","Once per battle round, gain a 5+ invulnerable save when targeted until the end of the phase."),("Ancient Foresight","Once per battle round, one friendly Silver Tempests unit within 6 inches may re-roll one Hit roll.")]),("Primary weapon",[("Assault cannon","Dreadnought assault cannon."),("Multi-melta","Multi-melta."),("Twin lascannon","Twin lascannon.")])])]
def ability(parent, key, name, description):
    p=el(parent,"profile",key,name=name,typeId="9e35-1f3d-c6b7-3ec0",typeName="Abilities",hidden="false")
    characteristic(add(p,"characteristics"),"Description","6fdd-8f47-abc3-6d08",description)
def weapon(parent, key, name, vals):
    p=el(parent,"profile",key,name=name,typeId="a4f5-4674-06d7-5496",typeName="Weapon",hidden="false")
    ch=add(p,"characteristics")
    for (k,v) in zip(WEAPON,vals): characteristic(ch,k,WEAPON[k],v)
def build():
    tree=ET.parse(PATH); root=tree.getroot()
    cats=root.find(q("categoryEntries"))
    if cats is None: cats=add(root,"categoryEntries")
    if not any(c.get("name")=="Silver Tempests" for c in cats):
        el(cats,"categoryEntry","category",name="Silver Tempests",hidden="false")
    entries=root.find(q("selectionEntries"))
    if entries is None: raise RuntimeError("Missing root selectionEntries")
    existing={e.get("name") for e in entries}
    for name,pts,stats,keys,max_units,options in UNITS:
        if name in existing: continue
        e=el(entries,"selectionEntry","unit/"+name,name=name,type="unit",hidden="false",**{"import":"true"})
        constraints=add(e,"constraints")
        el(constraints,"constraint",name+"/limit",type="max",field="selections",scope="roster",value=str(max_units),shared="true")
        links=add(e,"categoryLinks")
        el(links,"categoryLink",name+"/category",name="Silver Tempests",targetId=CAT,hidden="false",primary="true")
        for k in keys:
            el(links,"categoryLink",name+"/kw/"+k,name=k,targetId=KW[k],hidden="false",primary="false")
        profiles=add(e,"profiles")
        p=el(profiles,"profile",name+"/stats",name=name,typeId="0cb1-7394-fb88-5322",typeName="Unit",hidden="false")
        ch=add(p,"characteristics")
        for k,v in zip(STATS,stats): characteristic(ch,k,STATS[k],v)
        ability(profiles,name+"/covenant","Iron Covenant","This unit is a subordinate Silver Tempests contingent. It does not gain the Frozen Cogs faction keyword.")
        if name!="Stormheart Dreadnought":
            ability(profiles,name+"/arrival","The Silver Intervention","Deep Strike. Once per battle, re-roll one Hit roll in the turn this unit arrives using Deep Strike.")
        if name=="Stormseer":
            ability(profiles,name+"/leader","Leader","May lead Tidebound Intervention Squad; may lead Silver Fang Terminators if equipped with Terminator armour.")
        if name=="Stormheart Dreadnought":
            ability(profiles,name+"/sarcophagus","Warded Sarcophagus","Psychically warded interment and stable Stormheart conduit.")
        costs=add(e,"costs")
        add(costs,"cost",name="pts",typeId="0246-3343-a75c-5ffa",value=str(pts))
        groups=add(e,"selectionEntryGroups")
        for label,choices in options:
            g=el(groups,"selectionEntryGroup",name+"/group/"+label,name=label,hidden="false")
            c=add(g,"constraints")
            el(c,"constraint",name+"/"+label+"/min",type="min",field="selections",scope="parent",value="1",shared="true")
            el(c,"constraint",name+"/"+label+"/max",type="max",field="selections",scope="parent",value="1",shared="true")
            choices_el=add(g,"selectionEntries")
            for title,desc in choices:
                u=el(choices_el,"selectionEntry",name+"/"+label+"/"+title,name=title,type="upgrade",hidden="false",**{"import":"true"})
                up=add(u,"profiles")
                ability(up,name+"/"+label+"/"+title+"/rule",title,desc)
                if title=="10 models":
                    extra={"Tidebound Intervention Squad":100,"Silver Fang Terminators":190,"Tempest Talons":110}[name]
                    add(add(u,"costs"),"cost",name="pts",typeId="0246-3343-a75c-5ffa",value=str(extra))
                if title=="Stormspark":
                    weapon(up,name+"/stormspark","Stormspark",('12\"',"D3","3+","5","-1","1","Psychic"))
                if title=="Tempest Lance" or (name=="Stormseer" and title=="Thunderous Hand"):
                    weapon(up,name+"/"+title+"/lance","Tempest Lance",('18\"',"D3+1","3+","7","-2","2","Psychic"))
    # ElementTree preserves the existing XML structure, but normalizes formatting.
    tree.write(PATH,encoding="utf-8",xml_declaration=True)
    print("Silver Tempests category and five units installed")
if __name__=="__main__": build()
