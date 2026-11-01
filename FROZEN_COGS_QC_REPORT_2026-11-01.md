# Frozen Cogs roster QC and New Recruit integration — 1 November 2026

## Published fix

- Replaced all `FC ·` category headings and unit category links with descriptive names, without changing category IDs.
- Preserved all **164** Frozen Cogs root units and their catalogue identity.
- Added **59 fully defined alternate weapon profiles**: plasma supercharge (38), missile-launcher krak (18), and combi-weapon bolt modes (3). These are alternate firing profiles for a single selected weapon, not extra weapons to shoot simultaneously.
- Added standard roster-copy maximums for 16 earlier formations, including 6 copies of the Tactical Squad and 3 copies of each of the other fifteen.
- Verified IceBreaker Breachers retain boltguns, combi-bolters, bolt pistols, and Frostforged Breaching Shotguns with mandatory shields; IceBreaker Terminators retain bolter/shotgun/heavy firearm choices and mandatory shields; Frosthammer Terminators remain melee-and-shield focused.

## Automated QC — PASS WITH LIMITATIONS

The GitHub Actions `Validate and synchronize New Recruit revisions` workflow completed successfully.

- **164** selectable root unit entries, all marked for import.
- **4,135** weapon profiles with Range, Attacks, BS/WS, Strength, AP, Damage and Traits fields.
- **1,629** selectable equipment groups.
- **59** specific dual-mode weapon selections audited.
- XML schema structure, ID uniqueness, mandatory option defaults, cost values, category links, shared game-system metadata, and first-sixteen roster caps passed local automated checks.
- Existing Infernal Warriors and Abandoned Dead units were not modified by the Frozen Cogs wargear repair. Their catalogue revision metadata was synchronized with the shared game system.

## What this QC does **not** certify

The catalogue has **not** been tested inside a signed-in user's New Recruit session. These still require native client acceptance tests and/or careful player enforcement:

- Squad-wide per-five/per-ten weapon quotas when choices occur independently on different models.
- Special weapon combination restrictions across models.
- Leader-to-bodyguard associations, shared transport passenger assignment, and game-turn timing.
- Actual exported roster presentation, client cache/update behavior, and tabletop rules balance.

These limitations are not hidden by a passing static QC result. A user can still select an equipment combination that is prohibited by a squad-wide rule if that particular combination is not enforced natively.

**Next acceptance checks:** refresh the GitHub-installed Gaul Campaign system in New Recruit; open Frozen Cogs; add IceBreaker Breachers and a full 10-model Wintergrave unit; switch bolter/shotgun and alternate weapon modes; confirm points/export profiles; then attempt deliberately illegal specialist limits to identify which caps still need native support.
