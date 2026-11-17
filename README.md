# Bracket App

Bracketing and Queueing System for Railside Rumble Competition

Uses Neon Postgres Database

Deployed on Render

To ensure website remains active and doesn't spin down after 15 minutes of activity this uses uptime robot to ping the website every 5 minutes.

Start by adding teams. Use the Bulk Add Format Generator Template if its helpful

## Fixing mistakes: the Overrides page

When something goes wrong mid-event, use **🛠️ Overrides** in the admin navbar (`/admin/overrides`). It skips the normal checks, so type a **Reason** at the top first; every change is saved in the override log at the bottom of the page.

| Situation | What to do |
|---|---|
| A bot has to leave / emergency | **Withdraw** it. Its unfinished matches become forfeit (FF) wins for the opponents, and it's left out of later rounds. **Reinstate** undoes the withdrawal for future rounds. |
| Wrong winner, result type, or bots in a match | Edit that match's row and press **Save**. In Stage 2, keep **Fix next round** ticked so the bot that advanced (and the bronze match) is corrected too. |
| Two bots need to switch matches | Edit both match rows. |
| A rematch, or a match that's missing | **Add a match** (Stage 1 and decider). |
| A match shouldn't exist | **Delete** it (Stage 1 and decider). |
| A round was drawn from bad results | **Roll back** that round. It deletes the round and everything after it; fix the earlier results, then generate it again from its normal page. |
| A bot needs more or less repair time | Set its **Repair time left**. |
| Bot entered in the wrong class | **Move to class** (only before it has matches; otherwise withdraw it and add it again). |
| A match has to go next | **Move to Top** on the Match Queue page. |

For streaming, open the Stage 2 bracket's **Streaming Overlay** link or use `/stage2/overlay?class=3lb` as a transparent browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. The overlay refreshes every 20 seconds.

The upcoming match queue also has a standalone **Streaming Overlay** link on the queue control page, or use `/queue/overlay?class=3lb` as a browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. It refreshes every 20 seconds.

The group standings page also has a **Streaming Overlay** link, or use `/standings/overlay?class=3lb` as a browser source. Replace `3lb` with `1lb` or `1lb_plant` to select another bot class. It refreshes every 10 seconds.
