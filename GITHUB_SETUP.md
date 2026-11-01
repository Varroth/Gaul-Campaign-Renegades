# New Recruit publication and maintenance

Repository: https://github.com/Varroth/Gaul-Campaign-Renegades

## Live source

Keep `Gaul_Campaign_Renegades.gst` and the four `.cat` files at the root of `main`. Preserve existing IDs and filenames. Install through **Add from GitHub → Latest Commit (Head)**. Local file imports do not subscribe to this source. Releases and BattleScribe `.bsi` indexes are not required for this installation path.

## Before committing locally

Run from the repository root with Python 3.12 (standard library only):

```sh
python scripts/sync_new_recruit_revisions.py --base HEAD
python scripts/check_repository.py --write-manifest
python scripts/audit_new_recruit.py
python scripts/audit_frozen_cogs_roster.py
python tools/qc_frozen_cogs.py
python -m unittest discover -s tests -v
```

If the changes are already committed, pass the last published/pre-change commit SHA as `--base` instead. The synchronizer refuses invalid baselines, preserves existing revision increases, and is idempotent against the same baseline. Changes to the shared system synchronize catalogue metadata and bump affected catalogue revisions. It never changes unit options, rules, profiles, points, names or IDs.

## GitHub automation

`new-recruit-revisions.yml` runs on every push to `main`, including documentation/script pushes, and can be dispatched manually. It checks out current `main` with full history and compares against the pre-push SHA, so a data change followed by documentation commits is not missed. Manual dispatch uses `HEAD^` as its baseline. It validates the complete dataset and runs regression tests before committing necessary revision/manifest repairs.

There is one publisher, serialized by a concurrency group. A normal fast-forward push refuses to overwrite intervening work. If another author pushes while a job is running, its metadata push can fail safely; the queued run checks the newer head. It never rebases already-tested files onto untested changes. Bot commits do not trigger another workflow run; all checks execute before publication, without `[skip ci]` markers.

Pull requests run `repository-qc.yml` with read-only permissions and check revisions against the PR base. Update `catalogue-manifest.json` with the generator after changing data. CI artifacts retain machine-readable audit evidence.

The two completed, version-pinned Frozen Cogs release workflows and migration scripts were retired; Git history preserves them. Legacy repair/label scripts remain manual utilities, not publication steps. Do not run them as routine release processing.

## Diagnose an apparently stale app

Compare installed catalogue revisions with the generated manifest. For this maintenance release, Abandoned Dead is r14 with 61 root units, including Nullifier Operator and Nullifier Interdiction Team. A fresh list should expose personnel/weapon selections for Unmarked Scout Squad, Blackout Breachers, Directorate Breach Cell and Shadow Operative Cell. Existing saved lists may need their selections refreshed separately.

If the installed revision is older, investigate the installed source, update response and device cache. If the revision is current but a unit/weapon is absent, investigate catalogue parsing and roster selection paths. A successful GitHub commit or Actions run alone cannot certify automatic refresh on a device.
