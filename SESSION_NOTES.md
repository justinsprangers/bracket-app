# Bracket App: session notes

Club repo (railsiderobotics/bracket-app). No push access: work is pushed to the fork `justinsprangers/bracket-app` (git remote `fork`) and merged via PRs.

## Status
- 2026-11-17: 21 bug fixes on `fix/general-bugfixes`, see `FIX_REPORT.md`. Tested on SQLite only (not Neon). PR open.
- `feature/local-testing` (built on main, independent): README "Running locally", `.env.example`, `seed_demo.py`. PR open.
- `feature/admin-overrides` (built on the fix branch): Overrides page (matchup swap, match editor, add/delete, rollback, repair time, class move, log) + queue arrows. Withdraw option removed at user's request. PR link given.
- `fix/connection-resilience` (built on the fix branch): after crashes at an event (blamed on venue Wi-Fi). Background refresh (`templates/_live_refresh.html`) replaces `location.reload()`/meta refresh on public pages, timers and overlays; `public_cache()` 5-15 s on public pages/overlays (40 phones + 3 overlays: 626 -> 41 DB queries); `pool_pre_ping`/`pool_recycle`; `gunicorn.conf.py` (1 worker, gthread x8, timeout 60). PR link given.
- Kept separate from `arena-controller` for now; they're meant to talk later (arena prints `state: N` / `time: N` over serial at 9600).

## Next steps
- Ask the club to check Render logs (WORKER TIMEOUT / OOM / "server closed the connection"), Render plan (free = 0.1 CPU) and Render vs Neon region.
- Decide the open items in `FIX_REPORT.md` ("Not changed"): queue showing unlocked pairings, bulk-add hyphen split, ProxyFix for the login rate limit, delete unused `templates/bracket.html`.

## Decisions & gotchas
- Branching: `fix/...` for bug fixes, `feature/...` for each new feature, each its own pull request. A feature that needs the fixes is built on the fix branch; merge the fix PR first.
- Results forms send `orig_*` hidden inputs; the server only saves matches whose value changed (`form_value_changed`). Any new results form must include them or it falls back to "save everything".
- `queue_status` values: queued, in_progress, awaiting_results, completed (set when a winner is saved).
- Public pages issue 5-22 DB queries each; one viewer with every public page open is ~6.6 queries/s. Before the resilience fix, pages refreshed with `location.reload()`/meta refresh, so one failed refresh left a dead error page. Countdowns now use `data-ends-at` (absolute ms) so cached pages stay accurate.
- PRs are opened from prefilled compare URLs (`compare/main...justinsprangers:bracket-app:<branch>?expand=1&title=..&body=..`); a Chrome extension blocks automated clicks on GitHub.

## Log
- 2026-11-17: crash investigation; fix/connection-resilience built (39/39 checks, browser dropout simulation passed).
- 2026-11-17: admin overrides feature; withdraw dropped, matchup swap + queue arrows added (76/76 end-to-end checks).
- 2026-11-17: bug sweep (stale-form data loss, queue order, re-queue, byes, Stage 2 guards, timers, standings cache, confirms).
