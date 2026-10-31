# Gaul Campaign: Renegades — New Recruit GitHub updates

**Published repository:** https://github.com/Varroth/Gaul-Campaign-Renegades

Install using New Recruit > MySystems > Add from GitHub, with `Varroth/Gaul-Campaign-Renegades`. Do not import individual files if you want repository-linked updates.

## How updates are published

The game system (`Gaul_Campaign_Renegades.gst`) and four catalogues (`*.cat`) live in the repository root on `main`. The catalogue's own `revision` must increase whenever that catalogue changes; the `gameSystemRevision` must match the shared game system's revision. Preserve all existing system, catalogue, unit and option IDs to protect saved rosters.

The workflow `.github/workflows/new-recruit-revisions.yml` runs `scripts/sync_new_recruit_revisions.py` on relevant pushes. It detects catalogue changes that lack a revision increase, repairs stale game-system revision references, validates XML, and commits metadata repairs. The workflow requires **GitHub Actions enabled** and permission to write repository contents (Settings > Actions > General > Workflow permissions). If Actions are disabled or blocked, the workflow will not execute; run it manually from the Actions tab or run the Python script locally before publishing.

A GitHub commit alone does not prove that New Recruit has refreshed its local cache. Check New Recruit's installed source, refresh/reopen while online, and verify the displayed catalogue revision. Back up rosters before troubleshooting; do not delete saved rosters.

## Compatibility and limitations

The maintenance script only edits root-tag version metadata, not unit profiles, points, options, IDs or rules. It does not prove in-app New Recruit refresh behavior, which requires a real-device test. No `.bsi` index is required for the New Recruit Add from GitHub installation path.
