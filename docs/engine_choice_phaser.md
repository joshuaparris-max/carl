# Engine Choice: Phaser 3 Web-First

## Decision

Use **Phaser 3** as the next serious game engine target.

Keep the Python version as a systems prototype and test reference. Keep `index.html` as a visual proof-of-concept. Build the production demo in a proper Phaser project.

## Why Phaser

Phaser fits this project because:

- The game is tile-based.
- The browser prototype is already JavaScript.
- Existing JSON data files can be loaded directly.
- Phaser supports scenes, tilemaps, sprites, tweens, particles, camera effects, input, and audio.
- Web builds are easy to playtest.
- Desktop packaging can be deferred to Electron or Tauri.

## Project Structure

Recommended future Phaser structure:

```text
phaser-client/
  package.json
  index.html
  src/
    main.js
    scenes/
      BootScene.js
      PreloadScene.js
      TitleScene.js
      TutorialGuildScene.js
      FloorOneScene.js
      PauseScene.js
      GameOverScene.js
      VictoryScene.js
    systems/
      GameState.js
      World.js
      Combat.js
      Quests.js
      Inventory.js
      Crafting.js
      ViewerPressure.js
      Announcements.js
      SaveSystem.js
    ui/
      Hud.js
      QuestLog.js
      InventoryPanel.js
      DialogueBox.js
      ControlsBar.js
    data/
      characters.json
      items.json
      quests.json
      dialogue.json
      recipes.json
      announcements.json
      maps/
  public/
    assets/
      sprites/
      tilesets/
      audio/
      ui/
```

## Porting Strategy

Port systems in this order:

1. Data loading.
2. Game state.
3. World grid.
4. Movement.
5. Quest system.
6. Inventory.
7. Crafting.
8. Combat.
9. Announcements.
10. Save/load.
11. Viewer pressure.
12. UI panels.

Do not start with art. Use colored placeholder rectangles or Kenney tiles first.

## Phaser Scene Plan

### BootScene

- Configure resolution.
- Read saved settings.
- Prepare global constants.

### PreloadScene

- Load JSON data.
- Load placeholder tiles.
- Load placeholder sprites.
- Load audio.
- Show loading progress.

### TitleScene

- New Game.
- Continue.
- Options.
- Credits/legal note if needed.

### TutorialGuildScene

- Tutorial map.
- Carl, Donut, Mordecai, shopkeeper, training enemy.
- First quests.
- First chest.
- First craft.
- First combat.

### FloorOneScene

- First larger floor.
- Collapse timer.
- Saferooms.
- Enemy variety.
- Mini-boss.

### PauseScene

- Resume.
- Options.
- Save.
- Quit to title.

### GameOverScene

- Cause of death.
- System commentary.
- Restart from checkpoint.
- Return to title.

### VictoryScene

- Floor summary.
- Viewer count.
- Quests completed.
- Continue or quit.

## Vite Setup

Use Vite for the development server because it is fast and simple.

Commands once the Phaser client exists:

```powershell
cd phaser-client
npm install
npm run dev
```

Keep build output separate from the current Python prototype until the Phaser version is stable.

## Packaging

Do not package early.

Packaging should wait until:

- Title screen exists.
- Save/continue works.
- Floor 1 loop works.
- Options screen exists.
- Audio settings exist.

Desktop packaging options:

- **Electron:** easiest and most common.
- **Tauri:** lighter, more setup work, better final app footprint.

Use Electron first unless app size becomes a real problem.

## Success Criteria

The Phaser port is successful when:

- Tutorial Guild is playable in Phaser.
- JSON data loads unchanged or with only small schema additions.
- Movement, quests, inventory, combat, crafting, and announcements behave like the Python/browser prototypes.
- The game can run with placeholder art.
- Tests or scripted smoke checks can verify core flow.

