# UX, Polish, Accessibility, and Release Plan

## Screens Needed

### Title Screen

Requirements:

- Dark atmospheric background.
- Carl and Donut visible.
- Donut judging from the corner.
- New Game.
- Continue.
- Options.
- Credits / Legal note.

### Tutorial Intro

Requirements:

- System announcement before control is given.
- Short, animated, skippable.
- Establishes tone and objective.

### Pause Screen

Requirements:

- Freezes turn progression.
- Resume.
- Options.
- Save.
- Quit to title.
- System makes a comment about stopping.

### Game Over

Requirements:

- Cause of death.
- Turn count.
- Quests completed.
- System commentary.
- Restart from checkpoint.
- Return to title.

### Floor Transition

Requirements:

- "Entering Floor X" animation.
- Timer reset/change shown clearly.
- System commentary.
- Loading state if needed.

### Victory / Tutorial Complete

Requirements:

- Viewer count reveal.
- Quest summary.
- Items found.
- Crafting discovered.
- Continue to Floor 1.
- Return to title.

### Full Inventory

Requirements:

- Equipment slots.
- Item list.
- Item details on hover/focus.
- Use/equip/drop actions.
- Keyboard navigation.

## Contextual Controls

Replace the permanent shortcut wall with contextual controls.

Examples:

- Near chest: `O Open`.
- On pickup: `P Pick up`.
- Near enemy: `X Attack`, `U Use item`.
- Near NPC: `T Talk`.
- Near shop: `B Buy`.
- Always: movement, inventory, pause.

## Accessibility

Minimum viable accessibility:

- Keyboard-only support.
- Colorblind mode with icon/shape indicators.
- Reduced motion toggle.
- Text size respects browser scaling.
- Sound volume controls.
- Pause on focus loss.
- No time-critical UI that cannot be paused unless the floor rule demands it and is clearly explained.

## Save UX

Manual save should remain for debugging, but player-facing saves should happen automatically:

- On saferoom entry.
- On floor transition.
- On tutorial completion.
- Before mini-boss encounter.

Save slots can wait. One continue slot is enough for the first demo.

## Release Checklist

Before itch.io demo:

- Title screen works.
- Continue works.
- Options screen has audio/reduced motion.
- Tutorial Guild complete.
- Floor 1 complete.
- Game over works.
- Victory summary works.
- Audio pass complete.
- All placeholder assets either replaced or clearly acceptable.
- Browser build tested in Chrome, Edge, and Firefox.
- Keyboard-only playthrough tested.
- Reduced motion tested.
- No console errors.
- Credits list asset/audio sources.
- Legal note describes fan/internal status if applicable.

