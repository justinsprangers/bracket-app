# Bracket App: session notes

Club repo (railsiderobotics/bracket-app).

## Status
- 2026-11-17: 21 bug fixes on `fix/general-bugfixes`, see `FIX_REPORT.md`. Tested on SQLite only (not Neon).
- `feature/local-testing` (built on main, independent): README "Running locally", `.env.example`, `seed_demo.py`.
- `feature/admin-overrides` (built on the fix branch): Overrides page (`/admin/overrides`): withdraw/reinstate, edit any match (Stage 2 changes carry into the next round and the bronze match), add/delete Stage 1 matches, roll back rounds, set repair time, change class, override log (`OverrideLog` table); queue "Move to Top".
- Kept separate from `arena-controller` for now; they're meant to talk later (arena prints `state: N` / `time: N` over serial at 9600).

## Next steps
- Decide the open items in `FIX_REPORT.md` ("Not changed"): queue showing unlocked pairings, bulk-add hyphen split, ProxyFix for the login rate limit, delete unused `templates/bracket.html`.

## Decisions & gotchas
- Branching: `fix/...` for bug fixes, `feature/...` for each new feature, each its own pull request. A feature that needs the fixes is built on the fix branch; merge the fix PR first.
- Results forms send `orig_*` hidden inputs; the server only saves matches whose value changed (`form_value_changed`). Any new results form must include them or it falls back to "save everything".
- `queue_status` values: queued, in_progress, awaiting_results, completed (set when a winner is saved).

## Log
- 2026-11-17: admin overrides feature (72/72 end-to-end checks incl. 33 override checks).
- 2026-11-17: bug sweep (stale-form data loss, queue order, re-queue, byes, Stage 2 guards, timers, standings cache, confirms).
