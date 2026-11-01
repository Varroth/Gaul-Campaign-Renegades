# Repository maintenance — November 1, 2026

## Confirmed defects and corrections

1. **Abandoned Dead duplicate XML collections:** 49 parents had repeated `rules` containers and six had repeated `selectionEntryGroups` containers. A total of 120 extra containers were merged into their first sibling without discarding their contents. XML being well-formed did not make this structure safe for collection-based importers; the previous audit did not check it.
2. **Affected personnel and weapons:** Unmarked Scout Squad, Blackout Breachers, Directorate Breach Cell, Shadow Operative Cell, Pallbearer Terminators and Field Support Cell had separate deployment and personnel group containers. Both groups now reside in one container per unit. The four reported squads pass static default traversal for five- and ten-model options, with weapons and costs present.
3. **Misplaced Nullifier units:** Operator and Interdiction Team were nested in the Shadow Gunship's Mission Kit / Deployment Protocol equipment choices. They are now direct catalogue units, raising the root unit count from 59 to 61. Existing IDs and selection details are retained.
4. **Revision baseline gap:** automation previously compared only `HEAD^`. A multi-commit push ending in documentation could hide an earlier unversioned catalogue edit. The new publisher compares against the pre-push SHA with full history. Tests reproduce that failure and confirm idempotent repair.
5. **Unsafe release handoff:** the old publisher could rebase validated data onto intervening, untested changes. The new publisher uses a normal fast-forward push and fails safely on concurrent changes; queued runs inspect the new head.
6. **Overlapping historical release jobs:** completed Frozen Cogs r18/r19 publishers and their one-off scripts were retired. The separate Frozen Cogs CI job is consolidated into full-repository validation; its checks and tests still run.
7. **Misleading file organization:** old revision-specific reports, manifests and reference tables now live in `docs/archive/`. Root README/install instructions describe the active source and current limitations. A deterministic manifest records revision, root ID, root unit count and SHA-256 for all five live files.
8. **Missing regression protection:** strict checks now reject duplicate collection containers, nested units, invalid direct defaults, duplicate IDs, unresolved references outside the system/imported catalogue scope, nonfinite numeric values and inconsistent shared-system metadata. Both push and pull-request workflows cover every catalogue.

## Validation evidence

- All five live XML files parse and pass repository structural/reference checks.
- All 23 tests pass: 10 existing Frozen Cogs roster tests and 13 repository/revision/default-selection tests.
- Every one of the 9,024 original Abandoned Dead IDs is preserved. Existing element attributes are unchanged except the catalogue revision; all existing profiles, rules, costs, constraints, modifiers and conditions are semantically identical.
- Abandoned Dead is revision **14**, shared system revision **10**, with **61** root units.
- Other four live data files are byte-identical to pre-maintenance commit `49c373bd5c1d5bc1d9ca574646c7fe205871a16f`.
- The manifest matches actual file hashes. Workflow YAML parses; Git whitespace checks pass.
- Default traversal is a narrow static regression check, not an implementation of the New Recruit roster engine.

## Remaining gameplay and application acceptance work

- Nullifier fixed equipment was approved, but no numeric weapon profiles were supplied in the earlier design conversation. The existing loadout, model costs and field rules are preserved. Each Nullifier entry now explicitly identifies the missing profile definitions. Supplying numeric profiles requires a rules-design decision, not an inferred maintenance correction.
- Nullifier attachments (maximum one eligible Attached Specialist, no Terminators/vehicles/Dreadnoughts) remain manual. Psychic weapon interactions remain undefined in the existing rules.
- Frozen Cogs cross-model quotas, native character joins, transport accounting, and other in-game restrictions still need New Recruit acceptance. Existing structural and exported-roster checks do not certify those runtime behaviors.
- This pass does not certify completion of all 30 Abandoned Dead strategic decisions or competitive points balance. The preserved strategic synchronization report records that separate scope.
- Automatic refresh on the user's device has not been observed. These findings explain missing catalogue content independently of caching; they do not establish the sole cause of any app update failure.

## Device acceptance checklist

1. Update the existing GitHub-installed system from Latest Commit (Head); confirm Abandoned Dead revision 14 against the manifest.
2. In a fresh army, verify Nullifier Operator and Nullifier Interdiction Team appear as independent root units, not Shadow Gunship equipment.
3. Add each of the four reported squads. Confirm both Mission Kit / Deployment Protocol and Squad Size / Personnel are available; open required models and Primary Weapon choices.
4. Check five- and ten-model configurations, alternate weapons, costs and exported profiles. Existing saved lists may need their selections refreshed separately.
5. If the revision is older, record the source and update response. If r14 is installed but choices still fail, capture the affected unit and exported roster for a runtime-specific fix. Do not delete saved armies to force a refresh.
