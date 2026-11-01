# Frozen Cogs r20 and Infernal Warriors refresh

Frozen Cogs r20 polishes 1,148 ability profile instances and removes 121 profiles containing development notices only. This includes repeated equipment/ability copies. Unit composition and weapon quotas are written as prose instead of Python/JSON data; gameplay text no longer includes editor implementation notes or release history. Selected Wintergrave and Frostglass rules use complete datasheet sentences. This remains a homebrew catalogue.

All selectable entries, equipment options, constraints, costs, weapon profiles and unit characteristics are unchanged. A structural comparison excluding ability profiles and the catalogue revision verified that the remaining XML was identical. No undefined range, timing, or rule effect has been invented to fill a gap.

The Abandoned Dead editorial pass renamed its exported keyword summaries to `Keywords`. The validator required the former heading, `Faction and unit keywords`, and failed publication checks for all 61 units. The validator now accepts either heading while continuing to check keyword contents. Abandoned Dead data is unchanged.

Infernal Warriors retains its catalogue ID and all 74 importable, visible root units. Every unit's primary category is reachable through `Infernal Warriors Muster`. Revision 16 republishes the same content to offer an update to installed clients. No units, weapons, points, IDs or force settings were changed. This does not establish that an existing device's empty roster menu is repaired. Check that the roster uses Infernal Warriors and Infernal Warriors Muster; a different faction's force has different category links.

Validation: all 34 regression tests pass; strict repository and reference checks pass; Frozen Cogs structural/roster checks pass with their existing limitations. New tests guard Infernal Warriors unit visibility/category reachability and the absence of development notices in Frozen Cogs ability text.

Native cross-model quotas, Leader attachments, passenger assignments and automatic refresh on the user's device still require in-app verification. These implementation caveats belong here, outside the printed abilities. Back up existing saved rosters before any installation removal; do not delete lists as a refresh step.
