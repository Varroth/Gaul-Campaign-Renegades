# Frozen Cogs Phase 1 — QC baseline (2026-11-01)

Status: **technical audit in progress; no lore, rules, points, IDs or faction choices changed.**

## Verified from published GitHub source
- Frozen_Cogs.cat: catalogue revision **17**, catalogue ID `9a0b2133-696e-5c99`.
- Gaul_Campaign_Renegades.gst: system revision **10**, system ID `0408-b3dc-97f0-53dc`.
- Catalogue references system revision 10 correctly.
- 164 top-level units; 6,816 selection entries; 1,629 selection groups; 4,650 constraints; 6,485 profiles.
- No duplicate `id` attributes detected by initial structural scan.
- v2.3 release notes (system rev 8, catalogue rev 13) are **historical**, not the current deployed revisions.

## Automated QC added in this branch
- XML parsing, duplicate ID detection, matching system IDs and revisions, top-level unit count and basic constraint checks.
- GitHub Actions execution on relevant changes and manual dispatch.

## Outstanding acceptance tests (not claimed as passed)
1. Import/refresh the GitHub source in New Recruit; verify revision 17 is displayed.
2. For every squad, test minimum/maximum model counts, compulsory champions and per-five/per-ten weapon caps.
3. Test replacement exclusivity, free and paid option totals, invalid loadouts and exported weapon profiles.
4. Test Leader associations, transport capacities and cross-unit restrictions; some may require manual enforcement.
5. Compare exported roster totals to the independent offline editors, including Wintergrave 5- and 10-model presets.
6. Verify automatic refresh after a future incremented revision on the published default branch.

## Pending design approval — NOT IMPLEMENTED
- Any changed weapon profiles, option costs, quotas, model roles or rules.
- Consolidation of shared weapon definitions if it would change exported profiles or available options.
- Any modification to established lore or faction-specific army identity.

This branch intentionally avoids rewriting the 5.9 MB catalogue without exhaustive option-by-option comparison.

## Evolving Arsenal sample — inspected in published revision 17

| Squad | Individual model entries | Equipment groups | Constraint scopes |
| --- | ---: | ---: | --- |
| Wintergrave Siege Terminators | 10 | 49 | parent, roster |
| Frostglass Interdictors | 10 | 39 | parent, roster |
| IceBreaker Breachers | 10 | 40 | parent, roster |
| IceBreaker Terminators | 10 | 40 | parent, roster |
| Frozen Cogs Tactical Squad | 10 | 40 | parent, roster |
| Frozen Cogs Devastator Squad | 10 | 30 | parent, roster |

**Confirmed gap:** Each sampled unit offers native per-model equipment choices, but its constraint elements only use `parent` and `roster` scopes; no modifier elements were found in the catalogue. This does **not** demonstrate enforcement of cross-model quotas such as Tactical special-per-five, heavy-per-ten, or Devastator heavy-per-squad. The datasheet text explicitly calls for manual verification. These are existing-rule enforcement gaps, not proposed gameplay revisions.

**Next implementation gate:** Build native cross-model aggregate checks (or an accurate external validator where BattleScribe semantics cannot enforce them) and test representative legal/illegal loadouts before modifying the large catalogue. Preserve all current option names, IDs, point values, profiles and squad rules. Do not conflate a per-model `parent` max with a unit-wide quota.

**Caution:** This is a structural inspection, not a successful New Recruit import or an executed GitHub Actions run.
