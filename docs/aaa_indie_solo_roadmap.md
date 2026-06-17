# From Python Prototype to AAA-Indie Solo Demo

## Purpose

This roadmap turns the current Python and browser prototypes into a practical solo-dev production path. The goal is not to build everything at once. The goal is to ship a polished demo by sequencing the work so each milestone is playable, visible, and useful.

Target outcome:

- A premium-feeling 2D browser/desktop demo.
- Tutorial Guild plus Floor 1 loop.
- Polished movement, combat, System announcements, quests, inventory, crafting, and viewer pressure.
- A build suitable for itch.io-style feedback after roughly 12-14 weeks of consistent work.

## The Hard Truth

Trying to improve engine, art, game feel, content, UX, audio, and polish all at once is how solo projects stall. These pillars must be built in order:

1. **Engine choice and port.**
2. **Game feel and juice.**
3. **Visual art.**
4. **Content depth.**
5. **UX and polish.**
6. **Release packaging.**

Each stage should leave the game playable.

## What Already Exists

The project already has a strong foundation:

- Data-driven content in JSON.
- Separated systems for world, state, combat, quests, turns, validation, and UI.
- Working save/load and checkpoint behavior.
- Unit and integration tests.
- Seven tutorial quests driving the opening loop.
- A playable Python terminal prototype.
- A single-file browser prototype in `index.html`.
- Early combat, inventory, crafting, viewer pressure, hazards, NPCs, shops, and companion behavior.

This matters because the future visual game is not starting from zero. The design and logic spine already exists.

## What Blocks AAA-Indie Feel

The biggest missing quality signals are:

- No engine-level visual renderer with sprites, tilemaps, particles, and camera.
- No audio.
- No "juice": screen shake, hit flash, floating damage, transitions, particle bursts, UI animation.
- No full UI scene stack: title, pause, game over, floor transition, victory.
- No floor-scale content beyond the tutorial room.
- No custom art pass.
- No content pipeline for maps and assets.

The key leverage point is to port the Python logic to JavaScript/Phaser first, then build presentation on top. The JSON content, quest structure, combat math, and map concept can survive the port.

## Recommended Engine Direction

Recommended path: **Phaser 3 + web-first build**, later packaged with **Electron** or **Tauri** for desktop.

Why this fits this project:

- The browser prototype already proves the game works in JavaScript.
- Existing JSON content can load directly.
- Phaser has built-in tilemaps, scenes, tweens, particles, camera shake, and Web Audio support.
- The project is grid/tile-based, which Phaser handles well.
- A web build is easy to share for playtesting.
- Desktop packaging can happen late without changing game code.

Rejected or lower-priority options:

- **Continue Python terminal:** best for system tests, not final presentation.
- **Pygame:** good learning path, weaker web/desktop sharing path and less UI polish leverage.
- **Godot:** strong option, but introduces a new scripting and project model after the JS browser prototype already exists.
- **Unity:** powerful but heavier than needed for this 2D solo-dev scope.
- **Unreal:** wrong scale for this project at this stage.

## Visual Identity

The visual identity should be dark, grimy dungeon fantasy with absurd bright interruptions.

Core palette:

- Deep stone grays and near-black backgrounds.
- Amber for System announcements, rewards, fire, and dungeon UI.
- Teal for Donut and companion-affection moments.
- Red for danger, HP loss, debuffs, and System threat states.
- Occasional garish reward colors to make the show layer feel alien and tacky.

Recommended art style:

- 16x16 pixel art.
- Tile-based environments.
- 4-direction walk cycles.
- Small sprites with expressive animation and strong silhouette.
- UI painted with dark panels, amber borders, and high readability.

Why 16x16:

- Achievable for one developer.
- Works with a 12x12 tutorial grid.
- Scales beautifully to browser and desktop windows.
- Lets animation and UI carry much of the premium feel.
- Compatible with free placeholder tilesets while custom art is built.

## Game Feel Priority

Game feel should come before more content.

Players judge quality quickly from:

- Movement response.
- Hit feedback.
- Sound.
- UI transitions.
- Quest completion feedback.
- Whether the game reacts to their actions.

The first "juice pass" should include:

- Smooth tile movement tween, 80-100 ms.
- Donut follows one beat after Carl with ease-out.
- Player landing bounce, scale 1.0 -> 1.05 -> 1.0.
- Screen shake on hit.
- Enemy hit flash.
- Floating damage numbers.
- Death pop/fade animation.
- System typewriter text.
- Quest complete banner.
- Chest glow and open shimmer.
- Explosion particle burst.
- Footstep, hit, explosion, chest, and System jingle sounds.

## Content Depth

Content depth comes after game feel.

The first real content target should be:

- Tutorial Guild polished.
- Floor 1 as a 4x3 room layout.
- 3 enemy types.
- 1 mini-boss.
- 2 saferoom doors.
- 3 starter crafting recipes.
- A real collapse timer.
- One complete flow: tutorial -> Floor 1 -> death or completion.

Do not expand to many floors until Floor 1 feels good.

## UX and Polish

Polish is information design, not decoration.

Required screens before demo release:

- Title screen.
- New game / Continue / Options.
- Tutorial intro.
- Pause screen.
- Game over screen.
- Floor transition screen.
- Victory / tutorial-complete screen.
- Full inventory screen.
- Dialogue box with speaker portrait.
- Quest summary screen.

Required UX improvements:

- Contextual controls bar instead of a wall of shortcuts.
- Collapsible quest log.
- Item hover stats.
- Speaker portraits in dialogue.
- Auto-save on saferoom entry.
- Visible no-pants indicator on Carl's sprite.
- Pause on focus loss.

Required accessibility:

- Colorblind mode with icons/shapes, not color only.
- Reduced motion toggle.
- Text scaling via browser settings.
- Keyboard-only support.
- Audio volume sliders.

## Final Demo Definition

The demo is ready when:

- It opens to a title screen.
- New game enters a polished Tutorial Guild.
- Player can learn movement, talk, open chest, inspect inventory, craft, fight, equip, buy, and use items.
- System announcements are animated and audible.
- Quests complete with clear feedback.
- Floor 1 has a beginning, middle, and end.
- Combat feels responsive even with placeholder content.
- Save/continue works.
- Game over and victory states exist.
- No obvious debug/developer UI remains.
- The game can be shared as a browser build.

