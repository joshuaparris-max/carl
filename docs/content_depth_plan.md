# Content Depth Plan

## Principle

Content comes after feel. Do not build five floors while movement, combat, audio, and UI still feel rough.

## Tutorial Guild Expansion

Current Tutorial Guild is functional. It needs depth and presentation.

Add:

- Mordecai dialogue expanded to 8-10 escalating lines.
- Donut banter by tile type.
- Donut reaction to shop, chest, hazard, goblin, and no-pants state.
- Tutorial chest cinematic opening.
- A second crawler NPC who gives bad advice.
- System announcements on every quest completion.
- Optional hint prompts if the player stalls.
- A short tutorial-complete state.

Acceptance criteria:

- Player understands controls without reading a wall of text.
- Player sees Carl/Donut/Mordecai personalities immediately.
- Player learns chest -> material -> craft -> explosive -> combat.
- Player sees viewer pressure react to actions.

## Floor 1 Minimum Viable Design

Floor 1 should be the first real content expansion.

Size:

- 4 columns x 3 rows of rooms.
- Each room roughly 12x12 to 16x16 tiles.
- Corridors connect rooms.
- Two saferoom doors.
- One locked door.
- One mini-boss room.

Room types:

- Entry room.
- Combat tutorial room.
- Hazard room.
- Crafting materials room.
- Shop/saferoom.
- Locked saferoom.
- Patrol enemy corridor.
- Optional loot room.
- Mini-boss antechamber.
- Mini-boss room.
- Exit/stairwell.

## Enemy Types

### Training Goblin

- Weak.
- Simple adjacent attack.
- Teaches basic combat.

### Patrol Kobold

- Moves between two or more points.
- Can detect Carl within short range.
- Teaches timing and positioning.

### Sleeping Crawler-Turned-Enemy

- Stationary until disturbed.
- Wakes if player gets close or makes noise.
- Teaches risk/reward and optional combat.

### Mini-Boss

Requirements:

- Named enemy.
- Pre-fight System announcement.
- At least one special attack.
- Environmental interaction or explosive weakness.
- Victory reward and viewer spike.

## Saferooms

Saferoom mechanics:

- Door can be opened/entered.
- Auto-save triggers on entry.
- Enemies cannot enter.
- Shop inventory.
- Rest or partial heal.
- Dialogue NPC or terminal.
- Timer continues or pauses depending on floor rule, but must be explicit.

Two Floor 1 saferooms:

- One open saferoom.
- One locked saferoom requiring key, quest, or rule exploit.

## Crafting Depth

Starter recipes:

1. Crude Blast Charge.
2. Flash Powder.
3. Shrapnel Popper.

Rules:

- Recipes are discovered, not shown upfront.
- Failed craft gives System commentary.
- Explosion radius preview appears before throwing.
- Crafted explosives should have risk: misfire chance, noise, collateral damage, or stamina cost.

## Floor Timer

Tutorial Guild:

- 100 turns for prototype pressure.

Floor 1:

- 200-turn hard deadline.
- Warning thresholds at 100, 50, 20, 10, 5.
- UI grows more urgent as timer drops.
- NPC behavior changes near deadline.
- Some optional rooms become bad choices late.

## Completion State

Floor 1 completion should show:

- Quests completed.
- Enemies defeated.
- Items crafted.
- Viewer score.
- Donut popularity.
- Damage taken.
- Time remaining.
- System commentary.

