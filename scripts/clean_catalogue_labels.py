#!/usr/bin/env python3
"""Remove player-facing status labels from catalogues without changing IDs or rules."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LABEL_RE = re.compile(r'\b(?:provisional|draft|playtest|in[ -]development)\b', re.I)

def clean_catalogue(source):
    original = source
    names = {
        "Draft / compatibility notice": "Equipment and compatibility",
        "Provisional roster design": "Roster guidance",
        "Draft development notice": "Equipment guidance",
        "Draft notice": "Roster guidance",
        "Draft status": "Roster guidance",
    }
    for before, after in names.items():
        source = source.replace('name="' + before + '"', 'name="' + after + '"')
    source = re.sub(r'\(\s*(?:draft|provisional(?: test effect)?)\s*\)', '', source, flags=re.I)
    source = re.sub(r'\bDRAFT\s+HOME\s*BREW\b', 'Homebrew', source, flags=re.I)
    source = re.sub(r'\bAll stats and points draft\b', 'Use the listed homebrew statistics and points', source, flags=re.I)
    source = re.sub(r'\bAll stats provisional\b', 'Use the listed homebrew statistics', source, flags=re.I)
    source = re.sub(r'\bProvisional:\s*', '', source, flags=re.I)
    source = re.sub(r'\bprovisional\b', 'homebrew', source, flags=re.I)
    source = re.sub(r'\bdraft\b', 'homebrew', source, flags=re.I)
    source = re.sub(r'\bplaytest\b', 'homebrew', source, flags=re.I)
    source = re.sub(r'\bin[ -]development\b', 'not yet selectable', source, flags=re.I)
    source = re.sub(r'\bunverified\b', 'requires an in-app check', source, flags=re.I)
    if LABEL_RE.search(source):
        raise ValueError('Status wording survived cleanup')
    def signatures(data):
        root = ET.fromstring(data)
        return root.get('id'), [e.get('id') for e in root.iter() if e.get('id')]
    if signatures(source) != signatures(original):
        raise ValueError('Catalogue IDs were changed')
    return source

def main():
    for path in sorted(ROOT.glob('*.cat')):
        original = path.read_text(encoding='utf-8')
        cleaned = clean_catalogue(original)
        if cleaned != original:
            path.write_text(cleaned, encoding='utf-8')
            print(f'Cleaned labels: {path.name}')
        else:
            print(f'No status labels: {path.name}')

if __name__ == '__main__':
    main()
