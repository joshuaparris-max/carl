# Architecture

## Current Shape

The prototype is now split into four layers:

- `src/engine/`: engine-level action processing, events, turn updates, and data validation.
- `src/`: game-specific state, entities, world model, quests, announcements, saves, and data loading.
- `src/ui/`: terminal rendering and player-facing display.
- `data/`: authored game content.

The goal is to keep game rules testable without requiring terminal input/output.

## Entry Point

`crawler.py` creates and runs `src.game.Game`.

`Game` is now an orchestrator:

- Loads and validates all data through `DataRepository`.
- Creates `GameWorld`.
- Creates `GameState`.
- Connects `ActionProcessor`, `TurnManager`, `EventQueue`, and `TerminalUI`.
- Collects event messages for display.

## Data Flow

```text
data/*.json + map txt
        |
DataRepository
        |
DataValidator
        |
GameData
        |
GameWorld + GameState
        |
ActionProcessor -> EventQueue -> TurnManager updates -> TerminalUI
```

## Data-Driven Files

- `characters.json`: player, companion, NPC, and future monster definitions.
- `items.json`: gear, materials, combat items, and future consumables.
- `quests.json`: objective-based quest definitions.
- `announcements.json`: System notification templates.
- `dialogue.json`: NPC dialogue.
- `objects.json`: chests, doors, terminals, and future interactables.
- `hazards.json`: map hazards and triggered environmental effects.
- `recipes.json`: crafting recipes.
- `lore_bible.json`: canon status and legal-risk tracking.
- `tutorial_guild_map.txt`: authored tile map.

## Validation

`src/engine/validation.py` defines lightweight schemas without external dependencies.

Validation currently covers:

- Characters.
- Items.
- Dialogue.
- Quests and quest objectives.
- Announcements.
- Recipes and item references.
- Objects.
- Hazards.
- Map width consistency.

Invalid data raises `DataValidationError` before the game starts.

## Entity Model

`Entity` now supports:

- `entity_type`: player, companion, NPC, monster.
- Position.
- Stats.
- Inventory.
- Buffs.
- Debuffs.
- Status effects.
- Resource block: health, max health, stamina, max stamina, armor.
- Free-form state for mode, previous position, dialogue state, and later AI state.

`WorldObject` supports:

- Position.
- Object type.
- Blocking.
- State such as opened/closed and contained items.

`Hazard` supports:

- Position.
- Effect.
- Severity.
- Tags.

## Game Loop

The turn loop lives in `src/engine/turns.py`.

Each turn:

1. Emits `turn_started`.
2. Processes player action.
3. Updates companions.
4. Updates enemies.
5. Updates environment.
6. Decrements floor timer.
7. Emits `turn_finished`.

The current loop is simple but ready for combat, enemy AI, floor timers, hazards, and companion behavior.

## Action Processing

`src/engine/actions.py` handles:

- Movement.
- Talking.
- Opening objects.
- Inventory viewing.
- Crafting.
- Save/load.
- Quit.
- Invalid commands.

Actions emit events rather than printing directly. This keeps the UI replaceable later.

Current player actions include:

- Movement.
- Attack.
- Use combat item.
- Talk.
- Open.
- Inventory.
- Craft.
- Equip.
- Pick up.
- Buy.
- Donut behavior mode changes.
- Save/load.
- Checkpoint restore.
- Quit.

## Gameplay Systems

The current playable systems include:

- Tile collision and entity blocking.
- Companion follow pathing with collision fallback.
- Hazards and terrain effects.
- Enemy stats, health, armor, hit/miss, and damage resolution.
- Donut support combat.
- Consumable explosive item use.
- Stack-aware inventory display.
- Equipment slots and armor recalculation.
- Pickups, chests, and a simple shop object.
- Objective-based quests.
- Multiple NPC dialogue targets.
- Viewer pressure and sponsor-ready announcements.
- Floor timer and collapse failure.
- Checkpoint restore from last save.

## Testing

Current tests cover:

- World movement.
- Collision.
- Object blocking.
- Hazard lookup.
- Quest completion.
- Item handling.
- Announcements.
- Lore-bible labels.
- Data validation.
- Event queue behavior.
- Turn timer updates.
- Floor-collapse quit condition.
- Integration scenario from inventory to chest to crafting.
- Integration dialogue scenario with Mordecai.

Run tests:

```powershell
python -m unittest discover -s tests
```

## Next Architecture Targets

- Add combat resolution.
- Add richer enemy data and spawn placement.
- Add richer companion command modes.
- Add floor definitions and timer data.
- Add data-driven banter.
- Add schema documentation per JSON file.
- Move save path into configurable settings.
- Add more integration tests for save/load and hazards.
