# Gaul Campaign: Renegades — Infernal Warriors, Abandoned Dead & Frozen Cogs

**Homebrew Warhammer 40,000 army-builder data** for New Recruit / BattleScribe. Contains playable Infernal Warriors, Abandoned Dead and Frozen Cogs catalogues. Silver Tempest has no selectable units.

## Installation from downloaded ZIP

1. Extract this ZIP.
2. Back up any existing `.ros` rosters from the previous version.
3. Open [New Recruit](https://www.newrecruit.eu/app) > **MySystems**.
4. Import `Gaul_Campaign_Renegades.gst` and the four `.cat` files from the extracted directory. Replace or refresh the earlier local dataset as needed.
5. Select **Gaul Campaign: Renegades > Infernal Warriors** to verify your existing army, or **Abandoned Dead Task Force** to build an Abandoned Dead army.

## GitHub-based updates

The five importable files are also in the **root** of this repository-ready package. If you publish them in the root of a GitHub repository, New Recruit can import that repository via **MySystems > Add from GitHub**, specifying `owner/repository` or the repository URL. Updates committed to that same repository are picked up automatically by New Recruit. You do not need to publish GitHub Releases or manually assemble a `.bsi` index for this New Recruit workflow.

**This repository is published.** New Recruit retrieves catalogue updates from this GitHub source when it refreshes. Avoid installing duplicate local copies of the same game system.

## How to use this patch

- To declare a Leader, select the desired **individual** bodyguard squad's **LEADER — select attached character for THIS squad** menu. Also purchase the Leader unit separately and use New Recruit's native association if available.
- To plan Bloodletter summoning, buy Bloodletters, declare legal Reserves on them, then optionally choose **Plan Invocation with this Thralls squad**. The rule remains once per army during the battle.
- New four preset loadouts remain editable and have no extra surcharge.
- The existing distinct Enhancement authorization system remains in place (separate approval in **01 — START HERE** followed by buying the upgrade on the unit).
- To run additional offline warnings and get an organized printable roster, export uncompressed `.ros` XML and open `ROSTER_FIELD_CHECK.html` in your browser, then choose the `.ros` file. No data is uploaded.


## Abandoned Dead — catalogue revision 12 (homebrew)

Abandoned Dead is a playable 59-unit catalogue with integrated Astartes, Directorate, covert, and cultist forces under one Abandoned Dead faction. The current catalogue is **revision 12** and references **game-system revision 10**. Vephar's v1.9 update remains documented in [the earlier release notes](ABANDONED_DEAD_RELEASE_NOTES_v1_9.md); those notes are historical and their revision 7 reference is superseded. Approved strategic doctrines 28–30 are now included as non-mechanical reference rules. See the [2026-11-01 strategic synchronization and outstanding QA report](ABANDONED_DEAD_STRATEGIC_SYNC_2026_11_01.md). **New Recruit import/export, automatic refresh, all 30 doctrine implementations, and competitive points balance have not been fully verified.**

## Known limitations

Real native Leader joins, cross-vehicle passenger accounting, and board timing cannot be fully enforced with the existing XML selections. In-app testing remains necessary. Review `QC_REPORT_v2_5_2.md` for details, including manual validation cases.

## Receiving updates and avoiding duplicate game entries

GitHub-installed games under **MySystems > Add from GitHub** receive updates automatically as New Recruit refreshes the source. On mobile, use **Menu > Manage Games** to inspect your sources; if old data persists, restart/reopen New Recruit while online. Manually uploaded `.cat`/`.gst` files are not linked to GitHub updates. If you see duplicate Abandoned Dead choices, the repository contains only the current catalogue: back up rosters, then remove only the old manually installed game/source from MySystems. Do not delete saved lists or the current GitHub source to force an update.

### Vephar, the Uncrowned Sovereign — Chapter Master (v1.9 homebrew)

Vephar's canonical epithet is **the Uncrowned Sovereign**; his formal rank remains Chapter Master. His selectable unit and profile names in `Abandoned_Dead.cat` now use **Vephar, the Uncrowned Sovereign**. Vephar has five activated battle abilities, his signature halberd, two mutually exclusive ranged choices, and a homebrew 220-point cost. The shared game-system and Infernal Warriors are unchanged. Read [v1.9 notes](ABANDONED_DEAD_RELEASE_NOTES_v1_9.md) for limitations.

## Frozen Cogs v2.3

**Frozen Cogs Expeditionary Force** contains 164 roster entries. See [Frozen Cogs release notes](FROZEN_COGS_RELEASE_NOTES_v2_3.md). Points remain homebrew. Native New Recruit import and certain cross-unit weapon, Leader and transport restrictions require additional acceptance testing.
