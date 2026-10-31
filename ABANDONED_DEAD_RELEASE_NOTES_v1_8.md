# Abandoned Dead v1.8 — New Recruit weapon visibility and abilities hotfix

**Homebrew playtest.** Target: the published `Varroth/Gaul-Campaign-Renegades` repository and existing Gaul Campaign game-system revision **7** (`0408-b3dc-97f0-53dc`). The Abandoned Dead catalogue revision is **4**. No changes to `Infernal_Warriors.cat` or `Gaul_Campaign_Renegades.gst` are required.

## Problem identified

The v1.7 5-/10-model and 10-/20-model roster implementations nested all weapon slots under individual `model` entries inside size-configuration `upgrade` entries. Minimum-model constraints were defined, but there was no explicit defaulted model group ensuring those mandatory models were instantiated. Depending on roster editor behavior, this can leave a squad showing no selected model weapon profiles until individual model slots are added. Separately, 28 required ammunition/turret groups had no default. Several existing character abilities and selectable mission-kit effects were buried in non-selective freeform notes.

## Changes made

1. Reorganized all **460 model entries** across **49 squad-size configurations** into one-child model selection groups. Each of the **386 mandatory model entries** now belongs to a group with `min=1`, `max=1`, and an explicit `defaultSelectionEntryId`; the **74 optional model entries** remain non-defaulted (they are added only on request). All original model IDs and weapons were retained.
2. Added defaults to **28** required ammunition/vehicle-turret selection groups, without deleting options.
3. Promoted **Vephar's Command** and seven other existing prominent character abilities to standalone, visible rules; did not invent replacements or change their effects.
4. Promoted **39** additional existing abilities and mission-kit effects to standalone named rules or rules attached to the selected kit (including Directorate Breach, Shadow Operative, Field Support, Pallbearer, and Unmarked Scout formations).
5. Added a quick explanation under each affected squad describing exactly where the **per-model weapon choices** live in New Recruit.
6. Preserved **all 59 unit entries**, **1,533 existing weapon profiles** within **1,605 total profiles**, 13 invulnerable-save profiles, original unit costs and upgrade weapon definitions. All existing model option lists and allowed sizes remain in place. Key specialist access remains 1/3 anti-materiel snipers in 5/10-model squads, 1/2 Scout specialist slots in 5/10-model squads, and 2/4 Directorate specialist slots in 10/20-person squads.

## Player acceptance checks — use after GitHub refresh

- **Vephar:** Check that Oathblade and Master-crafted Boltgun are visible, and **Vephar's Command** is separately listed as a unit ability.
- **Blackout Breachers:** Add 5; confirm five models populate with Boarding Boltguns by default; change Operator #2 to a legal Flamer/Meltagun if desired.
- **Pallbearer Veterans:** Add 5; inspect Master-crafted Boltguns and per-model alternate weapons. **Pallbearer Terminators:** add the default 10; inspect ten Storm Bolters and melee weapons.
- **Directorate Breach Cell:** Add 5; confirm combat shotguns and that exactly one chosen Breach/Engineer/Demolition kit displays its rule.
- **Field Support Cell:** Confirm three laspistols and select either the Medicae or Forge ability.
- **Shadow Operative Cell:** Confirm five suppressed carbines, and exactly one of the four special mission kits has a visible selected effect.
- **Unmarked Scout Squad:** Confirm five default boltguns and individual flamer/melta/heavy-weapon choices where eligible; verify Infiltrators versus Scouts 6" choice is exclusive.
- **Veil Stalker snipers:** Confirm 5 models permit at most one anti-materiel sniper and 10 permit at most three. Fixed Longshot ammunition defaults and Ghost-Eye selections must not stack illegally.
- Export the roster as `.ros` or formatted print and verify the selected weapon **profiles**, squad size, and selected ability names actually appear in the export. Pay particular attention to auto-selected model entries, as **live New Recruit import/export was not performed by this offline release process**.

## How to receive updates in New Recruit

**GitHub install:** Open **MySystems > Add from GitHub** and use `Varroth/Gaul-Campaign-Renegades`. New Recruit's official tutorial says GitHub-source updates are picked up automatically afterwards. You may need to reopen/refresh the application for it to retrieve newly published files. No universally documented dedicated Update button is required. Confirm the new catalogue behaves as described above.

**Manual file install:** Manually uploaded `.cat` / `.gst` files do **not** follow GitHub. Back up saved `.ros` armies before removing any old game data. Then install the GitHub source from MySystems, avoiding two copies of the same game.

**Duplicate Abandoned Dead placeholder:** The GitHub repository's old `Abandoned_Dead_FUTURE.cat` was already deleted in v1.7. The repository contains just `Abandoned_Dead.cat` and one `Abandoned Dead Task Force` force entry. If the app still shows two Abandoned Dead choices, it likely has old local data or two system sources installed. Remove *only* the obsolete placeholder/local source from MySystems after backing up saved rosters; do not delete the current live GitHub game data or your saved armies to fix the display.

## Validation scope

Static XML, existing IDs, preserved profiles and points, all required group defaults, root unit counts, and recursively expanded default weapon profiles passed local tests. This is **not** a verified live New Recruit UI acceptance test, exported `.ros` test, end-to-end unit association test, or competitive balance certification. If the app still loses weapons on export, report the exact squad/size and share an uncompressed `.ros` for a targeted correction.