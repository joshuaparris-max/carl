# Game Feel and Audio Spec

## Purpose

This document defines the "juice" pass that will make the game feel premium before the content is large.

## Movement Feel

### Carl Movement

- Movement is grid-based but visually tweened.
- Tile-to-tile movement duration: 80-100 ms.
- Use ease-out.
- Player sprite does a small landing bounce after each move.
- Movement input should buffer lightly so rapid key taps feel responsive.
- If movement is blocked, Carl should bump 2-3 pixels toward the obstacle and snap back.

Acceptance criteria:

- Carl never teleports visually from tile to tile.
- Blocked movement gives immediate feedback.
- Movement feels crisp at keyboard repeat speed.

### Donut Movement

- Donut follows one beat after Carl.
- Delay: 60-90 ms after Carl begins moving.
- Use a softer ease-out than Carl.
- If blocked, Donut pathfinds one tile around when possible.
- Donut has a small tail/fur bounce on movement.

Acceptance criteria:

- Donut feels like a companion, not a glued-on cursor.
- Donut never overlaps enemies or walls.
- Donut visibly reacts when unable to follow.

## Combat Feel

### Basic Hit

On a successful hit:

- Freeze for 35-50 ms.
- Camera shake: tiny, 80 ms.
- Target flashes white for 80 ms.
- Damage number floats upward and fades over 450-600 ms.
- Hit sound plays after swing sound.

### Miss

On a miss:

- Attacker does a short lunge.
- Target does not flash.
- Small "MISS" text pops briefly.
- System may occasionally mock repeated misses.

### Death

On enemy death:

- Target scales to 1.25 over 70 ms.
- Flash red or white.
- Collapse/fade out over 220 ms.
- Drop particles or small loot sparkle if loot exists.
- Quest update and viewer update happen after death animation starts.

### Explosions

Explosion is Carl's signature feedback.

Explosion event should include:

- Radius preview before use.
- Bright amber/white flash.
- Particle burst.
- Camera shake stronger than normal hit.
- Low boom sound.
- Smoke puff.
- Damage numbers for each target.
- System line if it is the first explosion or a creative kill.

## UI Feel

### System Announcements

- Typewriter text.
- Blinking cursor.
- Slight amber glow.
- New message slides in from right.
- Important messages briefly pulse the panel border.

Message timing:

- Short line: 0.6-1.0 seconds.
- Long line: allow skip/fast-forward by pressing the action key.

### Quest Complete

- Amber banner slides from top.
- Holds for 2 seconds.
- Fades out.
- Plays a short reward sound.
- Quest card changes state at the same time.

### Inventory

- Inventory panel slides in from right.
- Selected item row glows.
- Hover/focus shows stats.
- Equip action animates the item moving to slot.

### Level Up

- 20% amber full-screen flash.
- Brief triumphant sound.
- Stat change numbers animate upward.
- System line plays after the flash.

## Audio Priorities

Build audio in this order:

1. Footsteps.
2. UI select/confirm.
3. Attack swing.
4. Hit impact.
5. Explosion.
6. Chest open.
7. Quest complete.
8. System announcement jingle.
9. Ambient dungeon loop.
10. Shop/menu sounds.

## Audio Direction

Carl:

- Heavy footstep.
- Short gritty attack swing.
- Improvised metal/cloth movement.

Donut:

- Light pawstep.
- Tiny hop or soft tap.
- Occasional expressive chirp-like UI cue, not realistic meow spam.

System:

- Alien broadcast chirp.
- Low digital sting.
- Amber UI pulse.

Dungeon:

- Distant drips.
- Low rumble.
- Occasional metallic groan.
- Floor-specific ambient loops later.

## Reduced Motion Mode

When reduced motion is enabled:

- Disable camera shake.
- Replace large flashes with subtle border pulses.
- Keep damage numbers but remove large movement arcs.
- Keep typewriter optional.
- Disable particle bursts or reduce them heavily.

