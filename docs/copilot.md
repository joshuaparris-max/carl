Looking at the current state and the roadmap, here's the highest-value, lowest-effort wins:

## 1. **Add terminal colors & formatting** (~30 min, huge visual impact)
Your terminal output is plain text. Add ANSI color codes to:
- Quest completion messages in **amber** (matches the System voice)
- Enemy damage in **red**
- Friendly actions in **green**
- NPC dialogue in **cyan**

This is a single paint pass on the event rendering—no logic changes, instant polish.

## 2. **Show last 5 events instead of just 1** (~30 min, fixes feedback loop)
Currently `last_message` is a single line. Change it to display the last 5 events stacked vertically. Players will know what just happened without guessing.

## 3. **Expand dialogue and banter** (~1 hour, costs nothing)
The JSON files are the game. Add:
- 3–5 more dialogue lines for Mordecai (escalating stress)
- 5–6 Donut complaints per tile type (water, shop, hazard, etc.)
- System announcements for quest completion, enemy defeat, hazard trigger

All in data, no code changes.

## 4. **Better terminal HUD layout** (~30 min, readability win)
Reorganize the render to show:
- Map at top
- Carl/Donut status + timer in middle
- Quest lines below
- Event log at bottom

Current layout is cramped. Vertical space costs nothing, improves scannability.

---

## Why these first?

- **Colors + better layout** = the game looks intentional instead of sloppy, costs almost nothing
- **Event log** = players understand what's happening, core to feeling polished
- **More dialogue** = the game has personality, already have the infrastructure
- **Together** = 2–3 hours of work, transforms how the game *feels* to play

The roadmap says "game feel is the highest ROI work in game dev." These are terminal-era game feel wins.

Which of these sounds best to start with?