# Abandoned Dead — compatible New Recruit playtest catalogue v1.7

**System:** Gaul Campaign: Renegades (GitHub game-system ID `0408-b3dc-97f0-53dc`, revision 7).

## What was added

- Replaced `Abandoned_Dead_FUTURE.cat` placeholder with `Abandoned_Dead.cat` (one selectable faction).
- Added `Abandoned Dead Task Force` to the existing game-system, without deleting Infernal Warriors data or changing `Infernal_Warriors.cat`.
- Imported 59 Abandoned Dead units: 39 Astartes and 20 mortals (including distinct Directorate and cultist branches).
- Translated 1,533 ranged and melee profiles to the **existing** `Weapon` profile format. Preserved 13 invulnerable saves as explicit Ability profiles instead of adding disruptive Unit characteristics to the system.
- Remapped all unit characteristics, weapon characteristics, point costs, and primary categories to the existing GitHub system IDs. The Abandoned Dead-only Specialist and Support categories were added to that system.
- Preserved canonical line infantry profiles, Longshot/Anti-Materiel/Scout rifles, and published rules from the approved design.

## Quality gate

**Pass:** XML tree structure and uniqueness of catalogue IDs, root catalogue/system/revision identifiers, 59 unit entries, 1,533 weapon profiles, 13 invulnerable abilities, existing cost/characteristic type references, categories and root force categories.

**Not established:** a live New Recruit roster editor import, exported `.ros` validation, fully engine-enforced cross-unit Leader attachments or transport passenger counts, or battle-tested points. These are still **homebrew playtest** data; do not present as finalized competitive balance.

## In New Recruit

1. Go to **MySystems > Add from GitHub** and enter `Varroth/Gaul-Campaign-Renegades`; update/refresh if already installed.
2. Choose **Gaul Campaign: Renegades**, then **Abandoned Dead Task Force**.
3. Validate Ghostline 5/10, ten Pallbearer Terminators, 5-model snipers (one anti-materiel max), 10-model snipers (three max), advanced Ghost-Eye only when selected, mixed Directorate infantry and distinct cultists.
4. If a validation or export fails, share the exact warning and exported `.ros`, rather than assuming the static tests guarantee in-app compatibility.

**Safety:** The Infernal Warriors and Frozen Cogs catalogue files have not been changed by this update. As a backup, use an earlier Git commit to revert the `.gst` and Abandoned Dead changes if needed.
