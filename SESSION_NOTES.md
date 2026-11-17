# Bracket App: session notes

Club repo (railsiderobotics/bracket-app). No push access: work is pushed to the fork `justinsprangers/bracket-app` (git remote `fork`) and merged via PRs.

## Status
- 2026-11-17: 21 bug fixes on `fix/general-bugfixes`, see `FIX_REPORT.md`. Tested on SQLite only (not Neon). PR open.
- `feature/local-testing` (built on main, independent): README "Running locally", `.env.example`, `seed_demo.py`. PR open.
- `feature/admin-overrides` (built on the fix branch): Overrides page (matchup swap, match editor, add/delete, rollback, repair time, class move, log) + queue arrows. Withdraw option removed at user's request. PR link given.
- IN PROGRESS `fix/connection-resilience` (built on the fix branch): after crashes at an event (blamed on venue Wi-Fi). Done so far, uncommitted: `pool_pre_ping`/`pool_recycle` engine options, `public_cache()` decorator on the auto-refreshing public pages and overlays.
- Kept separate from `arena-controller` for now; they're meant to talk later (arena prints `state: N` / `time: N` over serial at 9600).

## Next steps
- Finish `fix/connection-resilience`: `gunicorn.conf.py` (1 worker, gthread, 8 threads, timeout 60); background refresh (fetch + swap content, keep old data on failure, retry, "reconnecting" badge, pause when tab hidden) replacing `location.reload()` / meta refresh on competitor pages, timers and overlays; test (e2e, load probe, browser dropout sim); README; push + PR link.
- Ask the club to check Render logs (WORKER TIMEOUT / OOM / "server closed the connection"), Render plan (free = 0.1 CPU) and Render vs Neon region.
- Decide the open items in `FIX_REPORT.md` ("Not changed"): queue showing unlocked pairings, bulk-add hyphen split, ProxyFix for the login rate limit, delete unused `templates/bracket.html`.

## Decisions & gotchas
- Branching: `fix/...` for bug fixes, `feature/...` for each new feature, each its own pull request. A feature that needs the fixes is built on the fix branch; merge the fix PR first.
- Results forms send `orig_*` hidden inputs; the server only saves matches whose value changed (`form_value_changed`). Any new results form must include them or it falls back to "save everything".
- `queue_status` values: queued, in_progress, awaiting_results, completed (set when a winner is saved).
- Public pages issue 5-22 DB queries each; one viewer with every public page open is ~6.6 queries/s. Old pages refreshed with `location.reload()`/meta refresh, so one failed refresh left a dead error page.
- PRs are opened from prefilled compare URLs (`compare/main...justinsprangers:bracket-app:<branch>?expand=1&title=..&body=..`); a Chrome extension blocks automated clicks on GitHub.

## Log
- 2026-11-17: crash investigation; started fix/connection-resilience.
- 2026-11-17: admin overrides feature; withdraw dropped, matchup swap + queue arrows added (76/76 end-to-end checks).
- 2026-11-17: bug sweep (stale-form data loss, queue order, re-queue, byes, Stage 2 guards, timers, standings cache, confirms).
