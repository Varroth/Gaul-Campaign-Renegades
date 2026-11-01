# Gaul Campaign: Renegades

Homebrew Warhammer 40,000 data for **New Recruit**: Infernal Warriors, Frozen Cogs and Abandoned Dead. Silver Tempest is an empty reserved catalogue.

## Install and receive updates

[Install from GitHub in New Recruit](https://www.newrecruit.eu/app/MySystems?addSystem=Varroth%2FGaul-Campaign-Renegades&ref=HEAD), or use **MySystems → Add from GitHub**, enter `Varroth/Gaul-Campaign-Renegades`, and select **Latest Commit (Head)**.

The five `.gst`/`.cat` files at the repository root on `main` are the live dataset. GitHub installations are eligible for New Recruit's automatic updates. Local file imports are not GitHub subscriptions. The install link does not force a refresh of an already installed copy.

Use the app's update/refresh action, then reopen it online. Compare the installed catalogue revision with [catalogue-manifest.json](catalogue-manifest.json). Avoid duplicate local installations; back up saved rosters before removing any source. Do not delete lists to troubleshoot an update.

## Current maintenance release — November 1, 2026

| File | Revision | Root units |
| --- | ---: | ---: |
| `Gaul_Campaign_Renegades.gst` | 10 | — |
| `Abandoned_Dead.cat` | **16** | **61** |
| `Frozen_Cogs.cat` | 19 | 164 |
| `Infernal_Warriors.cat` | 15 | 74 |
| `Silver_Tempest.cat` | 7 | 0 |

This table describes the maintenance release. The generated manifest is authoritative after later updates.

Abandoned Dead r14 merges duplicate XML equipment/rule containers and moves the two Nullifier units out of the Shadow Gunship equipment menu into the army list. All pre-existing IDs, points, profiles, weapon choices and rule text are retained. The four reported squads have complete default model/weapon paths in static tests, including both five- and ten-model configurations. See [the audit and remaining limitations](docs/MAINTENANCE_2026-11-01.md).

**Nullifier armament (r15):** fixed carbines, sidearms and the approved models’ combat knives now have selectable, default-equipped weapon profiles. Weapon costs are included in the existing model prices. See [weapon statistics and validation](docs/NULLIFIER_WEAPONS_r15.md). Attachment restrictions and Psychic weapon interactions remain manual.

**Keyword QC (r16):** all 61 units now list ABANDONED DEAD, their branch and appropriate unit-type keywords. Equipment-dependent Jump Pack/Fly and Transport tags are conditional. See the [complete unit review](docs/ABANDONED_DEAD_KEYWORD_QC_r16.md).

## Repository layout

- Root `.gst` and `.cat`: live New Recruit source, with stable filenames and IDs.
- `catalogue-manifest.json`: generated revisions, unit counts and SHA-256 hashes; diagnostic metadata, not a New Recruit update index.
- `scripts/`: repository audits and revision maintenance.
- `tools/`: Frozen Cogs structural/exported-roster checks.
- `tests/`: regression tests, including the Abandoned Dead visibility defects.
- `docs/`: current maintenance findings; `docs/archive/` preserves earlier release notes, reports and reference tables. Archived versions are historical, not current release claims.
- `ROSTER_FIELD_CHECK.html`: optional offline Infernal Warriors exported-roster helper; not a New Recruit integration test.

## Maintainers

See [publishing and validation](GITHUB_SETUP.md). Every push to `main` validates all catalogues; pull requests run read-only checks. Revision maintenance changes metadata only. Completed one-off r18/r19 release publishers have been retired.

GitHub validation does not prove that a particular device has refreshed, that every native attachment/quota works, or that homebrew points are balanced. New Recruit acceptance remains a separate real-app test. Unified Forces remains the shared standing alliance option; this maintenance does not alter lore or army rules.
