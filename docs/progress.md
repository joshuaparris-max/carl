## What’s Done So Far

### Core Architecture
- crawler.py launches the game by creating `src.game.Game` and calling `run()`.
- game.py defines the main loop:
  - loads data
  - constructs `GameWorld`, `GameState`, `QuestLog`, `EventQueue`, `ActionProcessor`, `TurnManager`, `TerminalUI`
  - reads player input, processes a turn, collects event messages, renders output

### Data-Driven Content
- Uses JSON assets in data for:
  - characters
  - items
  - dialogue
  - announcements
  - quests
  - recipes
  - objects
  - hazards
- Map layout loaded from tutorial_guild_map.txt

### Gameplay Systems Implemented
- Movement with blocking and companion follow
- Talk action for nearby NPCs
- Open action for chests
- Inventory viewing
- Crafting from recipe materials
- Attack and item-use combat
- Equip and pickup actions
- Shop purchase action
- Companion mode commands (`f`, `h`, `r`)
- Save / load / checkpoint restore
- Quit command

### World & State Management
- world.py handles entity positions, map rendering, objects, hazards
- game_state.py tracks:
  - inventory, equipment, armor
  - dialogue progress
  - floor timer
  - viewer pressure
  - checkpoint state
- events.py queues game events/messages

### Quest & Feedback System
- quests.py tracks quest objectives and completion
- Quest progress is driven by event recording
- terminal.py renders:
  - map
  - player/companion status
  - timer
  - viewer pressure
  - active quest lines
  - last event message(s)

### Combat & Enemy Behavior
- combat.py resolves attacks, hit/miss, damage, armor
- Consumable explosives can be used in combat
- Companion Donut supports combat and can act differently based on mode
- Enemies take turns and can attack the party

### Save / Checkpoint Support
- save_system.py saves to and loads from `savegame.json`
- Checkpoint system in `GameState` can snapshot and restore current run state

### Recent Improvements
- Quest completion messages now fire immediately when objectives finish
- Fixed duplicate `player_moved` quest recording in movement handling
- Added quest-completion event pushes for:
  - inventory inspection
  - chest opening
  - crafting
  - talking to Mordecai
  - hazard triggering
  - defeating enemies
  - item pickup

### Validation
- The codebase has unit/integration tests under tests
- Running `unittest discover tests` currently passes

### Current Playtest State
- The app is a playable terminal prototype with a tutorial loop:
  - move around
  - open the tutorial chest
  - inspect inventory
  - craft the first explosive
  - talk to Mordecai
  - fight enemies
  - see quest status and event messages

If you want, I can next summarize what is still missing vs. a minimal playable demo.

## Minimal Playable Demo Status

### What is already playable
- crawler.py launches the terminal game.
- game.py runs a turn loop, renders state, and collects event messages.
- Movement, blocking, and companion following are working.
- Core actions work:
  - `T` talk
  - `O` open chest
  - `I` inventory
  - `C` craft
  - `X` attack
  - `U` use explosive
  - `E` equip
  - `P` pickup
  - `B` buy
  - `F/H/R` companion modes
  - `V/L/K` save/load/checkpoint
- Quest progression is tracked via quests.py.
- Quest completion messages now display immediately in the terminal.
- Combat and enemy turns are active in combat.py.
- World, objects, hazards, and map render are active via world.py.
- Save/load and checkpoint snapshot restore are implemented.

### What makes it a playable demo now
- Tutorial loop exists.
- You can open the tutorial chest and craft the first explosive.
- Quest objectives update and complete.
- Status and quest info show in the terminal HUD.
- Tests are passing under `unittest discover tests`.

---

## What is still missing for a stronger demo

### UI / feedback
- No dedicated inventory menu or multiple-screen UI
- Only one `last_message` display stream, no event log/history
- Limited rendering polish

### World/content depth
- Only tutorial floor / map content exists
- No multi-floor progression or floor-specific rules
- Few enemy/NPC types and only one quest chain

### Systems not fully expanded
- No branching dialogue or richer NPC interaction
- No advanced item equipment / slot rules beyond basic equip
- No procedural or authored floor generation pipeline
- No formal combat abilities beyond attacks/use item
- No explicit reward system for quests or loot beyond simple inventory

### Game structure
- Prototype is still a terminal proof-of-concept, not a full game shell
- Data validation, schema design, and modular content pipelines can improve
- More polish needed around companion AI, hazards, and rules presentation

---

## Next best step
- Keep the current prototype playable and expand one vertical slice:
  1. polish tutorial flow
  2. add one more floor or room
  3. add a small new quest/objective
  4. improve terminal feedback for quest/event updates

If you want, I can now turn this into a concrete “next milestone” list and start implementing the next playable feature.

> Note: the current prototype status has also been added to `docs/todo.md` and `docs/dcc_aaa_indie_roadmap.html` for tracking.