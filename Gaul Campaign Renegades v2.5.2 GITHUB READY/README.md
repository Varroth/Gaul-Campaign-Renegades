# Gaul Campaign: Renegades — v2.5.2

**Homebrew Warhammer 40,000 army-builder data** for New Recruit / BattleScribe. Contains the Infernal Warriors, plus clearly marked future placeholders for Frozen Cogs, Abandoned Dead and Silver Tempest.

## Installation from downloaded ZIP

1. Extract this ZIP.
2. Back up any existing `.ros` rosters from the previous version.
3. Open [New Recruit](https://www.newrecruit.eu/app) > **MySystems**.
4. Import `Gaul_Campaign_Renegades.gst` and the four `.cat` files from the extracted directory. Replace or refresh the earlier local dataset as needed.
5. Select **Gaul Campaign: Renegades > Infernal Warriors** and verify your existing army.

## GitHub-based updates

The five importable files are also in the **root** of this repository-ready package. If you publish them in the root of a GitHub repository, New Recruit can import that repository via **MySystems > Add from GitHub**, specifying `owner/repository` or the repository URL. Updates committed to that same repository are picked up automatically by New Recruit. You do not need to publish GitHub Releases or manually assemble a `.bsi` index for this New Recruit workflow.

**This package is not proof that any repository is already published.** Publishing requires a repository destination and authorized GitHub write access. Any future catalogue version requires editing, testing, and committing new files to the repository before New Recruit can download the change.

## How to use this patch

- To declare a Leader, select the desired **individual** bodyguard squad's **LEADER — select attached character for THIS squad** menu. Also purchase the Leader unit separately and use New Recruit's native association if available.
- To plan Bloodletter summoning, buy Bloodletters, declare legal Reserves on them, then optionally choose **Plan Invocation with this Thralls squad**. The rule remains once per army during the battle.
- New four preset loadouts remain editable and have no extra surcharge.
- The existing distinct Enhancement authorization system remains in place (separate approval in **01 — START HERE** followed by buying the upgrade on the unit).
- To run additional offline warnings and get an organized printable roster, export uncompressed `.ros` XML and open `ROSTER_FIELD_CHECK.html` in your browser, then choose the `.ros` file. No data is uploaded.

## Known limitations

Real native Leader joins, cross-vehicle passenger accounting, and board timing cannot be fully enforced with the existing XML selections. In-app testing remains necessary. Review `QC_REPORT_v2_5_2.md` for details, including manual validation cases.
