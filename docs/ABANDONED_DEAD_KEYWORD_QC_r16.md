# Abandoned Dead placement and keyword QC — revision 16

All 61 units were checked against their existing catalogue role text, profiles, equipment, attachment and transport restrictions. The 61 root-unit placements and their established primary sections are retained. No units remain nested in equipment choices. Heavy Weapons Cell and Field Support Cell correctly remain in the combined Vehicles & Support section, but are tagged INFANTRY rather than VEHICLE.

Every unit now has an explicit ABANDONED DEAD faction category and an exported keyword summary. Existing ASTARTES, DIRECTORATE and CULTISTS category IDs are retained. New classifications are catalogue-local; the shared system and other factions are unchanged. Secondary keyword links do not replace the primary roster section.

## Classification decisions

- Foot units: INFANTRY; human infantry also MORTAL. Existing branch assignments are retained, including Liberation Partisans under DIRECTORATE.
- Phantom Lancers and Darek Soln: MOUNTED, BIKER, not INFANTRY. Darek's fixed command-bike rule and the Lancers' existing mounted squad configuration support this assignment.
- Kaedran and Pallbearer Terminators: TERMINATOR; no POWER ARMOUR keyword. Scout squads have SCOUT and are not labelled POWER ARMOUR. Other Astartes personnel retain their power-armour classification.
- Command entries: CHARACTER. Named command entries already restricted to one per roster are also EPIC HERO; no copy limits are changed. The Nullifier Operator is an ATTACHED SPECIALIST, not automatically a CHARACTER or Leader.
- Jump units: JUMP PACK and FLY. The generic Strike Commander's two tags apply only when its Jump Pack option is selected.
- Vehicles: VEHICLE; walkers also WALKER, the Dreadnought also DREADNOUGHT. Ghostwing and Shadow Gunships are AIRCRAFT/FLY. Spectre Recon Skimmer has FLY. Nullfire Interceptor is treated as a ground vehicle: its M10/T10 turret chassis and existing anti-air role do not establish aircraft status.
- Transport: fixed on the two Astartes ground carriers, conditional on transport-capable Ghost Carrier/Ghostwing/Shadow Gunship fits. Recovery and strike-only fits do not gain TRANSPORT.
- Battleline retains the existing primary category (no duplicate category). Null Battery is ARTILLERY. Rule-specific OATHBOUND CULTISTS, LIBERATION PARTISANS, SHADOW OPERATIVE and PATHFINDER identifiers are included on the applicable units.
- No IMPERIUM, CHAOS, DAEMON or PSYKER keywords are added. A SCOUT keyword identifies a scout unit; it does not grant the Scouts movement ability. Keywords do not grant new stealth, deployment, nullification or transport-capacity rules.

## Validation

The reviewed matrix in `data/abandoned-dead-keywords.json` covers every root unit by stable ID. Repository CI checks the matrix, section accessibility, faction/branch consistency, exclusive infantry/mounted/vehicle types, keyword summaries and unit-local equipment conditions. Regression tests cover missing faction tags, wrong sections, mortal support teams, mounted exclusions, jump-pack choices and transport fits.

Existing profiles, weapons, costs, constraints, rules and IDs are preserved. Only category definitions/links, conditional category modifiers and a keyword-summary rule are added; catalogue revision advances to 16. There are 32 regression tests in total. Static checks do not establish live New Recruit category propagation/export behavior; equipment-dependent tags still need an in-app check. Existing manual attachment and psychic-interaction limitations are unchanged.

## Complete unit review

| Unit | Roster section | Fixed faction/keywords | Conditional keywords |
| --- | --- | --- | --- |
| Vephar, the Uncrowned Sovereign | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Chief Apothecary Buer | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Abandoned Dead Strike Commander | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER | Jump Pack: JUMP PACK, FLY |
| Kaedran Morvane, the Pale Warden | Command | ABANDONED DEAD, ASTARTES, INFANTRY, CHARACTER, EPIC HERO, TERMINATOR | — |
| Abandoned Dead Shadow Lieutenant | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER | — |
| Abandoned Dead Forge-Wright | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER | — |
| Ghostline Squad | Battleline | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, BATTLELINE | — |
| Veil Stalker Hunter-Killer Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Veil Stalker Sniper Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Unmarked Scout Squad | Battleline | ABANDONED DEAD, ASTARTES, INFANTRY, BATTLELINE, SCOUT | — |
| Unmarked Scout Sniper Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, SCOUT | — |
| Blackout Breachers | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Pallbearer Veterans | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Pallbearer Terminators | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, TERMINATOR | — |
| Grave Seeker Recovery Team | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Veiled Circuit Signal Cell | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Phantom Lancers | Specialists | ABANDONED DEAD, ASTARTES, MOUNTED, BIKER, POWER ARMOUR | — |
| Falling Shroud Jump Assault | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, JUMP PACK, FLY | — |
| Last Echo Heavy-Support Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Shroud Dreadnought | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE, WALKER, DREADNOUGHT | — |
| Shroud Armoured Carrier | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE, TRANSPORT | — |
| Shroud Battle Tank | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE | — |
| Ghostwing Assault Gunship | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE, AIRCRAFT, FLY | Insertion Fit: TRANSPORT |
| Abandoned Dead Truthwarden | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER | — |
| Abandoned Dead Ciphermaster | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER | — |
| Void Wraith Boarding Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Silent Knell Shock Squad | Specialists | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR | — |
| Spectre Recon Skimmer | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE, FLY | — |
| Nullfire Interceptor | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE | — |
| Pallbearer Heavy Assault Carrier | Vehicles & Support | ABANDONED DEAD, ASTARTES, VEHICLE, TRANSPORT | — |
| Elias Veyr, Shadow Director | Command | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, CHARACTER, EPIC HERO | — |
| Directorate Field Liaison | Command | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, CHARACTER | — |
| Shadow Handler | Command | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, CHARACTER | — |
| Cult Agitator | Command | ABANDONED DEAD, CULTISTS, INFANTRY, MORTAL, CHARACTER | — |
| Directorate Line Infantry | Battleline | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, BATTLELINE | — |
| Directorate Veteran Cell | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL | — |
| Directorate Breach Cell | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL | — |
| Shadow Operative Cell | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, SHADOW OPERATIVE | — |
| Pathfinder Recon Team | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, PATHFINDER | — |
| Longwatch Marksmen | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL | — |
| Heavy Weapons Cell | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL | — |
| Field Support Cell | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL | — |
| Oathbound Cultists | Battleline | ABANDONED DEAD, CULTISTS, INFANTRY, MORTAL, BATTLELINE, OATHBOUND CULTISTS | — |
| Shroud-Knife Cultists | Specialists | ABANDONED DEAD, CULTISTS, INFANTRY, MORTAL | — |
| Liberation Partisans | Battleline | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, BATTLELINE, LIBERATION PARTISANS | — |
| Ghost Carrier | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, VEHICLE | Covered Transport: TRANSPORT; Recon Fit: TRANSPORT; Fire Support Fit: TRANSPORT |
| Spectre Scout Walker | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, VEHICLE, WALKER | — |
| Reclaimed Battle Tank | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, VEHICLE | — |
| Null Battery | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, VEHICLE, ARTILLERY | — |
| Shadow Gunship | Vehicles & Support | ABANDONED DEAD, DIRECTORATE, VEHICLE, AIRCRAFT, FLY | Extraction/Airlift: TRANSPORT |
| Serik Valech, Hollow Fox | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Odran Khelt, Dead Channel | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Threx Halvorn, Gravesight | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Malach Vorn, Black Bell | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Cyren Mordax, False Signal | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Darek Soln, Ghost Spear | Command | ABANDONED DEAD, ASTARTES, MOUNTED, BIKER, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Maelor Vexis, Nightfall | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO, JUMP PACK, FLY | — |
| Hadrien Ossar, Last Report | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Amon Veyth, Null | Command | ABANDONED DEAD, ASTARTES, INFANTRY, POWER ARMOUR, CHARACTER, EPIC HERO | — |
| Nullifier Operator | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, ATTACHED SPECIALIST, NULLIFIER | — |
| Nullifier Interdiction Team | Specialists | ABANDONED DEAD, DIRECTORATE, INFANTRY, MORTAL, NULLIFIER | — |
