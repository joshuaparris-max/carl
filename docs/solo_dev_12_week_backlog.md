# Solo Dev 12-Week Backlog

## Rule

Do not work on all pillars at once. Each week must leave the game playable.

## Weeks 1-2: Engine Port

Goal: Phaser Tutorial Guild playable with placeholder art.

Tasks:

- Create `phaser-client/` Vite project.
- Install Phaser.
- Copy JSON data into Phaser client.
- Port `GameState`.
- Port `World`.
- Port movement.
- Port quests.
- Port inventory.
- Port crafting.
- Port combat.
- Port announcements.
- Load Tutorial Guild map.
- Render map with placeholder tiles.
- Render Carl, Donut, Mordecai, shopkeeper, enemy, chest, pickup, hazards.
- Implement keyboard controls.
- Implement basic HUD.

Acceptance criteria:

- Tutorial Guild is playable in browser through Phaser.
- Player can complete the seven tutorial quests.
- Placeholder art is acceptable.
- No Python runtime required.

## Weeks 3-4: Juice Pass

Goal: the game feels good before adding content.

Tasks:

- Smooth tile movement tweens.
- Donut delayed follow tween.
- Blocked movement bump.
- Hit flash.
- Floating damage numbers.
- Enemy death animation.
- Camera shake.
- Quest complete banner.
- System typewriter effect.
- Chest open animation.
- Explosion particle effect.
- Footstep sounds.
- Swing/hit sounds.
- Explosion sound.
- Ambient loop.

Acceptance criteria:

- A new player says the game feels responsive.
- Combat hits are readable without checking logs.
- Quest completion is satisfying.
- Movement no longer feels like a terminal port.

## Weeks 5-7: Art Pass

Goal: screenshots look like a real game.

Tasks:

- Carl sprite.
- Donut sprite.
- Mordecai sprite.
- Training goblin sprite.
- Shopkeeper sprite.
- Chest sprite.
- Hazard tiles.
- Desk tile.
- Wall/floor tiles.
- UI frame art.
- Item icons.
- Attack animations.
- Idle animations.
- Walk cycles.

Acceptance criteria:

- A still screenshot communicates genre and tone.
- Carl's jacket/no-pants state is readable.
- Donut is instantly identifiable.
- UI has dark/amber identity.

## Weeks 8-10: Floor 1 Content

Goal: a complete play loop beyond the Tutorial Guild.

Tasks:

- Build Floor 1 map, 4x3 rooms.
- Add corridors.
- Add open saferoom.
- Add locked saferoom.
- Add three enemy types.
- Add patrol behavior.
- Add sleeping enemy trigger.
- Add mini-boss.
- Add pre-fight System announcement.
- Add collapse timer, 200 turns.
- Add 3 crafting recipes.
- Add crafting UI.
- Add explosion radius preview.
- Add floor transition screen.
- Add victory/death condition.

Acceptance criteria:

- Player can go tutorial -> Floor 1 -> death or completion.
- Floor timer matters.
- Crafting feels like Carl's identity.
- Mini-boss requires more than basic attacking.

## Weeks 11-12: Polish and Screens

Goal: demo release candidate.

Tasks:

- Title screen.
- Main menu.
- Continue.
- Options.
- Pause.
- Game over.
- Victory summary.
- Floor transition polish.
- Auto-save on saferoom entry.
- Contextual controls bar.
- Inventory screen.
- Dialogue portraits.
- Colorblind mode.
- Reduced motion.
- Volume settings.
- Browser focus pause.
- Credits/legal screen.

Acceptance criteria:

- Demo can be given to another person without explanation.
- No debug-only UI is required to play.
- Restart/continue works.
- Accessibility basics exist.
- Build is ready for itch.io upload.

## Weeks 13-14: Buffer and Release

Use these weeks for reality.

Likely tasks:

- Bug fixes.
- Balancing.
- Audio polish.
- Map readability.
- UI clarity.
- Performance pass.
- Credits and attribution.
- Itch page assets.
- Trailer/gif capture.
- First public playtest.

Acceptance criteria:

- The demo can survive external playtesting.
- Known issues are documented.
- Feedback collection is ready.

