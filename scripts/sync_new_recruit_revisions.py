#!/usr/bin/env python3
"""Normalize BattleScribe/New Recruit revision metadata without changing catalogue IDs or rules."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
GST = ROOT / "Gaul_Campaign_Renegades.gst"
CATS = sorted(ROOT.glob("*.cat"))

def previous(path):
    try:
        return subprocess.check_output(
            ["git", "show", f"HEAD^:{path.name}"], cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode("utf-8")
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        return None

def root_tag(s, kind):
    m = re.search(r"<" + kind + r"\b[^>]*>", s)
    if not m:
        raise ValueError(f"Missing {kind} root")
    return m.group()

def attr(tag, name):
    m = re.search(r"\b" + name + r'="([^"]*)"', tag)
    if not m:
        raise ValueError(f"Missing {name}")
    return m.group(1)

def replace_attr(tag, name, value):
    if not re.search(r"\b" + name + r'="[^"]*"', tag):
        raise ValueError(f"Missing {name}")
    return re.sub(r"\b" + name + r'="[^"]*"', name + '="' + str(value) + '"', tag, count=1)

def update(path, kind, target_system_rev=None):
    source = path.read_text(encoding="utf-8")
    tag = root_tag(source, kind)
    old_source = previous(path)
    old_tag = root_tag(old_source, kind) if old_source else None
    revision = int(attr(tag, "revision"))
    new_tag = tag
    # When file content changes without a revision increase, increase it once.
    if old_source is not None and source != old_source and old_tag:
        old_revision = int(attr(old_tag, "revision"))
        if revision <= old_revision:
            new_tag = replace_attr(new_tag, "revision", old_revision + 1)
    if target_system_rev is not None and attr(new_tag, "gameSystemRevision") != str(target_system_rev):
        # A metadata-only change also needs a catalogue revision bump to be discoverable.
        if new_tag == tag:
            new_tag = replace_attr(new_tag, "revision", revision + 1)
        new_tag = replace_attr(new_tag, "gameSystemRevision", target_system_rev)
    if new_tag != tag:
        path.write_text(source.replace(tag, new_tag, 1), encoding="utf-8")
        print(f"Updated {path.name}: {attr(tag, 'revision')} -> {attr(new_tag, 'revision')}")
        return True
    print(f"Already current: {path.name}")
    return False

def main():
    if not GST.exists():
        raise SystemExit("Missing game system")
    update(GST, "gameSystem")
    system_source = GST.read_text(encoding="utf-8")
    system_tag = root_tag(system_source, "gameSystem")
    system_id = attr(system_tag, "id")
    system_rev = int(attr(system_tag, "revision"))
    if not CATS:
        raise SystemExit("No catalogues found")
    for cat in CATS:
        tag = root_tag(cat.read_text(encoding="utf-8"), "catalogue")
        if attr(tag, "gameSystemId") != system_id:
            raise SystemExit(f"Wrong gameSystemId in {cat.name}")
        update(cat, "catalogue", system_rev)

if __name__ == "__main__":
    main()
