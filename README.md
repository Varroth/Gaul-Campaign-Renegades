# Gaul Campaign: Renegades

Homebrew Warhammer 40,000 army catalogues for New Recruit.

[Install Gaul Campaign: Renegades in New Recruit](https://www.newrecruit.eu/app/MySystems?addSystem=Varroth%2FGaul-Campaign-Renegades&ref=HEAD)

## Build your first roster

1. Open the install link. For manual installation, open **MySystems → Add from GitHub**, enter `Varroth/Gaul-Campaign-Renegades`, and choose **Latest Commit (Head)**.
2. Create a roster using **Gaul Campaign: Renegades**, choose your faction and set the points limit for your battle.
3. Add units from the faction’s army list. Open each unit to choose its size, weapons and wargear. Check the roster warnings before exporting your list.

| Catalogue | Army list |
| --- | --- |
| Infernal Warriors | 74 units, including Despoiler Cadre, Void Breachers and Ashen Chain Terminators. |
| Frozen Cogs | 164 units. Look for units by their individual names in the faction list. |
| Abandoned Dead | 61 units, including Astartes, Liberation Directorate forces and Nullifier specialists. |
| Silver Tempest | Reserved for a future army. No units are available. |

For Infernal Warriors, open **Army Configuration**, add **02 — DETACHMENTS: Choose Detachments**, and select your detachments inside its menu (War Hounds’ Legacy, Crimson Onslaught, Iron Reavers or Breach and Ruin). The menu supports one to four different detachments subject to your DP budget. Set battle size first, then select the mission disposition and consult the rules reference. Pay for each declared Leader separately. Each Lost Cohort unit requires its own qualifying Chaplain. For a Unified Forces battle, agree the coalition with your opponents and muster each contingent from its own catalogue.

## Update an existing installation

Open New Recruit online, use its update or refresh action, then reopen the system. Compare the installed faction revision with the [current catalogue manifest](catalogue-manifest.json). A GitHub installation can receive updates. Importing a local file creates a separate copy.

If a selection is missing, check it in a fresh roster of the same faction. This helps distinguish an older saved selection from a catalogue problem. Keep your saved lists and back them up before removing an installation.

## Repository reference

The root game system and faction catalogues are the live files. The [publication guide](GITHUB_SETUP.md) covers validation and updates. [Maintenance reports](docs/) record individual changes, and the [archive](docs/archive/) preserves earlier releases. The [offline field checker](ROSTER_FIELD_CHECK.html) is a helper for exported Infernal Warriors rosters.

## Battle Simulator (alpha playtest)

The [Gaul Campaign tactical simulator](docs/simulator/index.html) is a separate browser game with editable armies, movement, ranged and melee combat, objectives, computer turns and a ten-match Battle Lab. It covers Infernal Warriors, Frozen Cogs, Abandoned Dead and Silver Tempests using **illustrative, provisional** unit profiles rather than imported New Recruit points.

- [Open the website source](docs/simulator/index.html) or [review editable code and instructions](simulator/).
- To host the site publicly, enable **Settings → Pages → Deploy from a branch → main → /docs**. The planned website path is `/Gaul-Campaign-Renegades/simulator/`.
- New Recruit catalogues remain independent and untouched by simulator logic.
