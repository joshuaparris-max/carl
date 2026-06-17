# Playable Feature Specifications

## Floor Generation and Authoring

### Current State

The Tutorial Guild is authored as a plain text map in `data/tutorial_guild_map.txt`.

### Near-Term Requirement

Keep authored maps for story-critical spaces. Add structured metadata beside each map.

Minimum map metadata:

- Map ID.
- Display name.
- Floor ID.
- Canon status.
- Legal risk.
- Entry positions.
- Exit positions.
- Interactable tiles.
- Spawn points.
- Safe room flag.

### Future Requirement

Use procedural generation only for repeatable corridors, optional rooms, and combat spaces. Use authored maps for:

- Tutorial Guild.
- Saferooms.
- Major quest rooms.
- Boss arenas.
- Character-specific story beats.

## Encounters and Hazards

### Encounter Types

- Tutorial encounter.
- Ambush.
- Environmental puzzle.
- Timed escape.
- Boss puzzle.
- Social encounter.
- Shop/economy encounter.

### Hazard Types

- Damage tile.
- Trap tile.
- Noise lure.
- Timed collapse.
- Locked route.
- Visibility blocker.
- Dirty/smelly tile for Donut reactions.

### First Implementation Target

Add one harmless tutorial hazard tile that triggers:

- System warning.
- Donut complaint.
- Future damage hook.

## Loot and Crafting

### Current State

The game has:

- Carl's Leather Jacket.
- Unstable Dungeon Powder.
- Crude Blast Charge.
- Threadbare Tutorial Pants.
- Stale Healing Bar.

### Crafting Rules

Crafting should eventually support:

- Ingredients.
- Tools.
- Risk score.
- Yield score.
- Discovery state.
- Combat-use restrictions.
- System commentary.

### First Implementation Target

Replace the hard-coded `C` craft command with a data-driven recipe file:

```json
{
  "id": "crude_blast_charge",
  "ingredients": ["unstable_powder"],
  "result": "crude_blast_charge",
  "discovery": "tutorial_chest_opened"
}
```

Status: complete. `data/recipes.json` now defines the crude blast charge recipe, and crafting consumes ingredients and creates the result.

## Dialogue and Banter

### Dialogue Types

- NPC dialogue.
- Companion banter.
- System announcements.
- Quest text.
- Item descriptions.
- Combat barks.
- Floor timer warnings.

### Rules

- Keep dialogue in data files.
- Tag dialogue by speaker, trigger, tone, and canon status.
- Do not copy book dialogue unless licensed.
- Use original lines that preserve character function and tone.

### First Implementation Target

Add `data/banter.json` for Donut reactions:

- Movement complaints.
- Chest opening.
- Crafting explosive.
- Standing near Mordecai.
- Wall bump.

## Quest Systems

### Current State

The quest system can complete simple quests.

It now supports objective arrays, progress tracking, completed/open display, and event-driven progression.

### Needed Features

- Objective lists.
- Partial progress.
- Rewards.
- Hidden objectives.
- Failure conditions.
- Time-limited quests.
- Quest-triggered announcements.

### Quest Data Shape

Future quests should include:

- ID.
- Title.
- Description.
- Canon source.
- Canon status.
- Legal risk.
- Objectives.
- Rewards.
- Failure rules.
- Trigger events.

### First Implementation Target

Upgrade `data/quests.json` from simple descriptions to objective arrays while preserving current behavior.

Status: complete. The current quest file tracks tutorial dialogue, inventory inspection, chest opening, crafting, item pickup, hazard triggering, and first combat success.

## Combat and Encounters

### Current State

The game now includes:

- A tutorial enemy.
- Enemy health, armor, stamina, stats, and entity type.
- Carl basic attack.
- Explosive combat item use.
- Donut support attack.
- Enemy attack updates.
- Defeat events.
- Combat-linked quest progression.
- Viewer pressure increases from violent or explosive actions.

### Next Target

Add:

- Enemy movement toward Carl/Donut.
- Multiple enemy attack profiles.
- Status effects such as bleeding, stunned, burning, frightened.
- Combat log filtering in the UI.

## Movement, Navigation, and Hazards

### Current State

The game now includes:

- Tile collision.
- Entity blocking.
- Object blocking.
- Donut follow behavior with fallback pathing.
- Nonlethal grime hazard.
- Rough terrain stamina effect.
- Trap damage effect.

### Next Target

Add:

- Hazard disarming.
- Hidden traps.
- Line of sight.
- Doors and locked routes.

## Inventory, Equipment, and Shops

### Current State

The game now includes:

- Stack-aware inventory display.
- Equipment slots.
- Armor recalculation.
- Pickups.
- Chest loot.
- Simple shop purchase.
- Consumable explosive use.

### Next Target

Add:

- Currency.
- Shop prices.
- Unequip command.
- Consumable healing action.
- Loot tables.
