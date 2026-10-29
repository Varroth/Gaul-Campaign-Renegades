# v2.5.2 — Verification report

## Results

- **39,069/39,069** structural and regression checks passed against the v2.5.1 baseline.
- **8/8** Chromium browser tests passed for the offline roster validator (synthetic .ros fixtures).
- **5/5** game-system and faction XML files parse successfully; all `.gst` / `.cat` file identities were preserved.
- **19** named Leader selection tokens and **15** bodyguard-side choice groups encode **59** legal Leader/bodyguard pairings. This is a *per-squad roster declaration*, not proof of a native New Recruit Leader association.
- **4** additional editable presets for Bloodmarked Thralls and Chainbound Reavers; all are price-neutral.
- **1** optional, zero-point, once-per-roster Bloodletter Invocation planning declaration.
- No existing unit, wargear, enhancement, cost or rule IDs were removed; original selection and point values were preserved.
- The catalogue is saved as compact XML to reduce uncompressed size from 6,742,337 bytes to 5,155,760 bytes (same parsed data).

## Chromium scenario coverage

| Scenario | Expected validation | Result |
|---|---|---|
| Valid Bloodmarked Thralls + purchased Reserve Bloodletters | No errors | PASS |
| Thralls Invocation plan without paid Reserve Bloodletters | Warning | PASS |
| Three Lost Cohort units | Error | PASS |
| Varroth declared attached but not purchased | Error | PASS |
| Khorne Daemons over 25% budget | Error | PASS |
| The Measured Strike without authorization | Error | PASS |
| Authorized The Measured Strike | No authorization error | PASS |
| Two planned Bloodletter invokers | Error | PASS |

## Disclosed limitations

1. **New Recruit live import and runtime rules remain untested**. Automated XML checking cannot establish what the client displays or enforces. Open the imported roster and verify an actual bodyguard assignment, points, and transport choices.
2. **Native Leader attachments not implemented**. Only bodyguard-instance declarations and references are available in this BattleScribe 2.03 XML. They do not physically connect Character and Bodyguard entries; match each selection to the separately purchased Leader.
3. **Core two-step Enhancement authorization is retained** for distinct-name counting, preserving v2.5.1 logic; no new single-step automatic behavior is claimed.
4. **Transport passenger totals, duplicate squads across changing missions, and some shared unit restrictions require manual or offline review**. The HTML tool flags more cases but is not New Recruit's validation engine.
5. **Browser helper depends on recognizable `.ros` XML names** and does not handle compressed `.rosz`; parse failures and unusual export formats may require manual review. No user files are sent to a server.
6. **The invocation is only an optional pregame plan**. Only *already purchased* Bloodletters in legal Reserves can be summoned; battlefield movement, timing and placement must be judged during play. The optional invoker declaration must not be misinterpreted as locking which surviving Thralls squad can legally use the ability.
7. **No live GitHub publishing occurred**. The repository-ready directory places `.gst` and `.cat` files in the repository root; a real destination repository and enabled write-capable action are required to publish it.

## Test provenance

- Source: `Gaul_Campaign_Renegades_v2_5_1_New_Units_QC.zip` extracted baseline, with the v2.5.1 unit data.
- 39,069 checks compare previous IDs, profiles, costs, constraints, links, selection-entry names and unchanged placeholder files; also validate new references and defaults.
- Browser tests loaded the HTML content in headless Chromium and uploaded synthetic `.ros` files through its ordinary input control.
- Tests **do not simulate real tabletop play** or claim officially validated Warhammer 40,000 point values.
