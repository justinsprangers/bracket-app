# Bracket App

Bracketing and Queueing System for Railside Rumble Competition

Uses Neon Postgres Database

Deployed on Render

To ensure website remains active and doesn't spin down after 15 minutes of activity this uses uptime robot to ping the website every 5 minutes.

## At events: bad Wi-Fi and lots of viewers

- **Pages ride out dropouts.** Public pages, repair timers and the stream overlays refresh in the background. If the connection drops, they keep showing the last data (with a small "Reconnecting…" badge, hidden on overlays) and catch up when it's back, instead of turning into a browser error page.
- **Server load stays low.** Public pages and overlays are cached for 5-15 seconds, so a room full of phones costs about one page build per refresh instead of one per phone. Changes made in the app show up immediately (the cache is cleared on every change), and admin pages are never cached.
- **Server settings** are in `gunicorn.conf.py` (one worker with 8 threads, 60 s timeout). Render picks it up automatically with the start command `gunicorn app:app`, unless that command sets its own `-w`/`--threads`/`--timeout` flags.
- **Give the scoring/queue laptop its own connection** (phone hotspot or a travel router with a SIM) rather than the venue Wi-Fi.
- **If something still goes down,** check Render's Logs around that time: `WORKER TIMEOUT` means requests were too slow (upgrade the instance or move it to the same region as Neon), `Out of memory` means the instance is too small, and `server closed the connection unexpectedly` is the database dropping.

Start by adding teams. Use the Bulk Add Format Generator Template if its helpful

For streaming, open the Stage 2 bracket's **Streaming Overlay** link or use `/stage2/overlay?class=3lb` as a transparent browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. The overlay refreshes every 20 seconds.

The upcoming match queue also has a standalone **Streaming Overlay** link on the queue control page, or use `/queue/overlay?class=3lb` as a browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. It refreshes every 20 seconds.

The group standings page also has a **Streaming Overlay** link, or use `/standings/overlay?class=3lb` as a browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. It refreshes every 10 seconds.
