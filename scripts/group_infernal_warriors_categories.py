#!/usr/bin/env python3
"""Keep ten Infernal Warriors sections; show numbered detachment choices in Army Configuration.

Retain every old unit category as a secondary link (especially rules-bearing
Khorne Allies, Detachments, Lost Cohort and muster-setting categories).
Remove old force-category browse links (hidden links can suppress units in NR).
Relocate the Detachments force limits onto the original category entry.
Does not change costs, weapons, units, keywords or selectable equipment.
"""
from collections import Counter
import copy
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CAT_PATH = ROOT / "Infernal_Warriors.cat"
SYS_PATH = ROOT / "Gaul_Campaign_Renegades.gst"
CNS = "http://www.battlescribe.net/schema/catalogueSchema"
SNS = "http://www.battlescribe.net/schema/gameSystemSchema"
GROUPS = (
    "Army Configuration", "Characters", "Battleline",
    "Infantry & Elites", "Lost Cohort", "Dreadnoughts",
    "Vehicles & Artillery", "Aircraft", "Daemon Engines",
    "Auxiliaries & Allies",
)
# Existing system category IDs are reused where possible. The Characters
# category is already shared by Frozen Cogs; it is force-scoped in New Recruit.
EXISTING = {
    "Detachments": "3c17-c261-4038-5fcc",
    "Characters": "c1bd73c6-6a54-5bc3-ad26-514cbbbf90f6",
    "Battleline": "ec2c-68bb-bfbc-5ee3",
    "Lost Cohort": "2962-6989-212f-598d",
    "Dreadnoughts": "930f-f4e6-1451-52ba",
    "Aircraft": "6be8-bd06-032f-5209",
    "Daemon Engines": "b703-ed42-a968-5cce",
}
OLD_TO_NEW = {
    "Muster Settings": "Army Configuration",
    "Force Dispositions": "Army Configuration",
    "Detachments": "Army Configuration",
    "Enhancements": "Army Configuration",
    "Configuration Tools": "Army Configuration",
    "Command": "Characters",
    "Battleline": "Battleline",
    "Infantry": "Infantry & Elites",
    "Elites": "Infantry & Elites",
    "Terminators": "Infantry & Elites",
    "Jump Infantry": "Infantry & Elites",
    "Mounted": "Infantry & Elites",
    "Lost Cohort": "Lost Cohort",
    "Dreadnoughts": "Dreadnoughts",
    "Vehicles": "Vehicles & Artillery",
    "Transports": "Vehicles & Artillery",
    "Artillery": "Vehicles & Artillery",
    "Aircraft": "Aircraft",
    "Daemon Engines": "Daemon Engines",
    "Mortal Auxilia": "Auxiliaries & Allies",
    "Khorne Allies": "Auxiliaries & Allies",
}
FORCE_ID = "73a9-6482-df85-55c4"

def uid(key):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "gaul-infernal-categories-v1/" + key))

def q(ns, name):
    return "{" + ns + "}" + name

def direct(parent, container, element, ns):
    wrapper = parent.find(q(ns, container))
    if wrapper is None:
        return []
    return wrapper.findall(q(ns, element))

def run():
    cat_tree = ET.parse(CAT_PATH)
    sys_tree = ET.parse(SYS_PATH)
    cat, system = cat_tree.getroot(), sys_tree.getroot()
    system_categories = system.find(q(SNS, "categoryEntries"))
    force = next((f for f in direct(system, "forceEntries", "forceEntry", SNS)
                  if f.get("id") == FORCE_ID), None)
    if system_categories is None or force is None:
        raise ValueError("Missing shared categories or Infernal Warriors muster")
    force_links = force.find(q(SNS, "categoryLinks"))
    selections = cat.find(q(CNS, "selectionEntries"))
    if force_links is None or selections is None:
        raise ValueError("Missing force category links or root selections")

    by_id = {c.get("id"): c for c in system_categories}
    targets = dict(EXISTING)
    for name, cat_id in EXISTING.items():
        if cat_id not in by_id or by_id[cat_id].get("name") != name:
            raise ValueError("Shared category mismatch: " + name)
    for group in GROUPS:
        if group not in targets:
            cat_id = uid("category/" + group)
            matches = [c for c in system_categories if c.get("id") == cat_id]
            if matches and matches[0].get("name") != group:
                raise ValueError("Conflicting category definition " + group)
            if not matches:
                ET.SubElement(system_categories, q(SNS, "categoryEntry"),
                              {"id": cat_id, "name": group, "hidden": "false"})
            targets[group] = cat_id

    root_entries = list(selections)
    if len(root_entries) < 103 or any(e.tag != q(CNS, "selectionEntry") for e in root_entries):
        raise ValueError("Unexpected root entry layout; refusing to remove or regroup units")
    original_ids = [(u.get("id"), u.get("type")) for u in root_entries]
    counts = Counter()
    for entry in root_entries:
        links = entry.find(q(CNS, "categoryLinks"))
        if links is None:
            raise ValueError("Missing category links: " + str(entry.get("name")))
        all_links = links.findall(q(CNS, "categoryLink"))
        primary = [link for link in all_links if link.get("primary") == "true"]
        if len(primary) != 1:
            raise ValueError("Expected one primary category: " + str(entry.get("name")))
        previous = primary[0].get("name")
        # Detachments remain independently selectable at the roster root,
        # but their primary browse category is Army Configuration. Their
        # legacy Detachments category tag stays secondary for force limits
        # and rules that reference the unchanged IDs.
        is_detachment = any(link.get("targetId") == targets["Detachments"]
                            for link in all_links)
        new = ("Army Configuration" if is_detachment
               else previous if previous in GROUPS
               else OLD_TO_NEW.get(previous))
        if new not in GROUPS:
            raise ValueError("Unmapped primary category: " + str(previous))
        target = targets[new]
        matches = [link for link in all_links if link.get("targetId") == target]
        if len(matches) > 1:
            raise ValueError("Duplicate target category: " + str(entry.get("name")))
        if matches:
            chosen = matches[0]
        else:
            chosen = ET.SubElement(links, q(CNS, "categoryLink"), {
                "id": uid("unit/" + str(entry.get("id")) + "/" + new),
                "name": new, "targetId": target,
                "hidden": "false", "primary": "false",
            })
        # All previously assigned categories remain, including the original
        # primary. They continue to provide keywords and rule-scoped tags.
        for link in all_links:
            link.set("primary", "false")
        if is_detachment:
            old_name = entry.get("name", "")
            # Use conspicuous names and numerical ordering inside the
            # existing configuration tab; do not add a new category or move
            # the detachment's ID (other rules target it directly).
            if old_name.startswith("DETACHMENT — "):
                label = old_name.removeprefix("DETACHMENT — ")
            elif old_name.startswith("02 — DETACHMENT: "):
                label = old_name.removeprefix("02 — DETACHMENT: ")
            else:
                raise ValueError("Unknown detachment entry name: " + old_name)
            entry.set("name", "02 — DETACHMENT: " + label)
        elif entry.get("id") == "8d559da4-63be-49c6":
            entry.set("name", "03 — MISSION: Select One Disposition")
        elif entry.get("id") == "f1d2-4a82-72d7-5b2d":
            entry.set("name", "04 — RULES: Infernal Warriors Quick Reference")
        chosen.set("primary", "true")
        chosen.set("hidden", "false")
        counts[new] += 1

    # The underlying catalogue's order matches New Recruit's browse order.
    rank = {name: i for i, name in enumerate(GROUPS)}
    def sort_key(entry):
        main = next(l for l in direct(entry, "categoryLinks", "categoryLink", CNS)
                    if l.get("primary") == "true")
        return rank[main.get("name")], entry.get("name", "").casefold()
    selections[:] = sorted(root_entries, key=sort_key)

    original_force_links = list(force_links)
    visible = []
    for group in GROUPS:
        target = targets[group]
        matches = [l for l in original_force_links if l.get("targetId") == target]
        if len(matches) > 1:
            raise ValueError("Duplicate force link for " + group)
        if matches:
            link = matches[0]
        else:
            link = ET.Element(q(SNS, "categoryLink"), {
                "id": uid("force/" + group), "name": group,
                "targetId": target, "hidden": "false", "primary": "false",
            })
        link.set("hidden", "false")
        visible.append(link)
    legacy = [link for link in original_force_links if link not in visible]
    # New Recruit may treat a hidden force category as hiding any unit that
    # carries the matching secondary category tag. Never retain old browse
    # links with hidden=true; remove them from this force altogether.
    # Preserve the original 1-4 Detachments selection rule on its category.
    detachment = next(c for c in system_categories
                      if c.get("name") == "Detachments" and c.get("id") == "3c17-c261-4038-5fcc")
    for old_link in legacy:
        if old_link.get("name") == "Detachments":
            old_constraints = direct(old_link, "constraints", "constraint", SNS)
            if old_constraints:
                destination = detachment.find(q(SNS, "constraints"))
                if destination is None:
                    destination = ET.SubElement(detachment, q(SNS, "constraints"))
                known = {c.get("id") for c in destination}
                for rule in old_constraints:
                    if rule.get("id") not in known:
                        destination.append(copy.deepcopy(rule))
                        known.add(rule.get("id"))
    # Khorne Allies, Lost Cohort and muster limits live on the original
    # shared category entries; these category tags remain on every unit.
    force_links[:] = visible

    resulting = [(u.get("id"), u.get("type")) for u in selections]
    if sorted(resulting) != sorted(original_ids):
        raise ValueError("Root entries were changed during reorganization")
    if {l.get("name") for l in visible} != set(GROUPS) or len(visible) != 10:
        raise ValueError("Did not create exactly ten visible sections")
    if counts["Army Configuration"] != 7 or counts["Characters"] != 22:
        raise ValueError("Configuration or character entries missing")
    det_entries = [e for e in selections if e.get("name", "").startswith("02 — DETACHMENT: ")]
    if len(det_entries) != 4:
        raise ValueError("Expected four directly selectable detachment entries")
    config_entries = [e.get("name", "") for e in selections
                      if any(l.get("primary") == "true" and
                             l.get("targetId") == targets["Army Configuration"]
                             for l in direct(e, "categoryLinks", "categoryLink", CNS))]
    if (not config_entries[0].startswith("01 — START HERE:")
            or not all(n.startswith("02 — DETACHMENT: ") for n in config_entries[1:5])
            or not config_entries[5].startswith("03 — MISSION:")
            or not config_entries[6].startswith("04 — RULES:")):
        raise ValueError("Army Configuration order is not easy to browse")
    if sum(counts.values()) != len(root_entries):
        raise ValueError("Category assignment did not cover every entry")
    ET.register_namespace("", CNS)
    cat_tree.write(CAT_PATH, encoding="utf-8", xml_declaration=True)
    ET.register_namespace("", SNS)
    sys_tree.write(SYS_PATH, encoding="utf-8", xml_declaration=True)
    print("Infernal Warriors 10 browse categories, detachments inside Army Configuration:", dict(counts))

if __name__ == "__main__":
    run()
