result: In a live comparison of two game versions, early retention and engagement improved across player groups, and the team recommended a full release.

![Lorem ipsum dolor sit amet, consectetur adipiscing elit.](dream-blast-notifications-hero|16:9)

## Overview

After a level, events used to open on their own and interrupt the session. Our research linked those interruptions to churn. I owned the design of a system that moves event updates from pop-ups onto the event badge: a small set of badge states plus rules for about 20 events. Players now see what needs attention without being stopped.

## Outcome and impact

**For players:** event updates arrive on the badge instead of interrupting play, so they can play more levels in a row. In the live comparison, early retention and engagement both improved.

**For the team:** one documented rule set now covers about 20 events, and two old notifications (the checkmark and the Kite Festival counter) were retired as redundant.

**How we measured it:** a true A/B test was not technically possible, so we compared two live versions, one with pop-ups and one with the badge notifications, using A/B analysis. Day 1 retention improved significantly across player groups, including spenders and new players, and returning players completed noticeably more levels. The gains after the first day were not significant over the week, so the effect was strongest early.

**The decisions together:** matching the badge to urgency meant more states to learn, in exchange for signals that mean something. Keeping some interruptions balanced player flow against the need to deliver rewards and free up event slots. And one rule set for very different events meant managing exceptions by documenting them instead of hiding them. Together they let players keep playing, while rewards still get delivered and event slots keep moving.

**What I’d do next:** add a motion cue to the “Open” state, and move the pop-up priority list out of the client so it can be tuned without a release.

## The challenge

Events would open whenever a reward unlocked or an action became available. Research with spenders showed that too many pop-ups was one of the main reasons they churned. For the business, fewer interruptions meant more levels played per session and better retention.

The constraints made it hard:

- About 20 events with very different mechanics (solo, competitive, Season Pass).
- Finished events still had to be resolved so slots opened for new ones.
- Some events needed the player to make a decision.
- The pop-up order lived in the client, so it was hard to tweak.

![Lorem ipsum dolor sit amet, consectetur adipiscing elit.](dream-blast-notifications-challenge|16:9)

## Key decisions

### 1. Match the badge signal to urgency, not to every update.

A single generic alert would have recreated the pop-up problem on the badge. Instead I defined distinct states, each tied to a level of urgency:

- “Join” call to action with a dot: persistent urgency, for opt-in events only.
- “Open” call to action with a dot: temporary urgency.
- A dot alone: non-urgent attention.
- A numerical dot: the count of unclaimed rewards.
- Timer, Completed and Finished: information only.

![Lorem ipsum dolor sit amet, consectetur adipiscing elit.](dream-blast-notifications-decision-1|16:9)

### 2. Decide what still deserves to interrupt.

The goal was fewer pop-ups, not zero. Two rules came first: event pop-ups no longer appear when the game launches, and events no longer open on their own when a reward unlocks or an action becomes available. That update now shows on the event badge instead.

Finished events are different. If they stay unresolved, they keep occupying a slot, and new events can’t start. So they still need the player’s attention:

- **Competitive events:** a results screen opens when the event ends, and the player claims their rewards.
- **Solo events:** they resolve on the player’s next level or when they tap the badge. If too many finished badges pile up, the oldest are cleared automatically (the limit is configurable).

Two exceptions remain: Season Pass still opens when it starts, and events where the player must choose a path still open automatically, because the decision can’t wait.

![Lorem ipsum dolor sit amet, consectetur adipiscing elit.](dream-blast-notifications-decision-2|16:9)

### 3. Make one rule set work across very different events.

With about 20 events that behave very differently, I needed one system that stayed consistent without forcing every event into the same mold.

- **A badge matrix.** I mapped badge behavior for every event across four moments: first appearance, visited with no action, played a level, and resolved.
- **Grouped logic.** Events that share the same notification logic are grouped together, and every exception is documented.
- **Event changes to fit the system.** Chest-opening overlays became a reward icon, and rewards now accumulate across milestones instead of opening the event each time.
- **Passive notifications.** Status markers like leaderboard position and offline status, and short sliders like multiplier updates, stay outside the system because they give feedback without asking the player to act. I designed around them, though. For example, offline status overrides any badge notification until the event is back online.
- **Art direction.** I defined the badge art direction together with the artists: the CTA has to grab the eye, and the badge has to be built so its colors and elements can be adapted for each event.

![Lorem ipsum dolor sit amet, consectetur adipiscing elit.](dream-blast-notifications-decision-3|16:9)
