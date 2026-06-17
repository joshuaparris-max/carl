# Tone and Design Pillars

## Project Tone

The game should feel like a survival RPG trapped inside an alien reality show. The player is not simply exploring a dungeon; they are being watched, scored, mocked, rewarded, and manipulated.

The writing should be original placeholder text unless the project becomes licensed, but it should preserve the functional tone:

- Dark comedy.
- Cruel rules.
- Absurd rewards.
- Violent stakes.
- Emotional sincerity beneath ridiculous presentation.
- Carl and Donut surviving because they are together, not because the dungeon is fair.

## Pillar 1: Absurd Televised Dungeon

The dungeon is entertainment for someone else.

Design rules:

- Important actions should generate System feedback.
- Viewer pressure should reward spectacle, not always good strategy.
- The UI should feel like an invasive show interface.
- Sponsor drops should be exciting but suspicious.
- Achievements should sometimes be helpful, sometimes insulting, and sometimes both.

Prototype hooks:

- `src/announcements.py`
- `data/announcements.json`
- Future: `viewer_popularity`, `sponsor_drop`, `audience_faction`

## Pillar 2: Cruel Rules, Real Consequences

Rules are unfair, but consistent enough to exploit.

Design rules:

- Every floor needs explicit constraints.
- Timers must prevent endless grinding.
- Safe zones must be valuable because the rest of the dungeon is unsafe.
- Failure states should be clear and harsh.
- Rule knowledge should be a player advantage.

Prototype hooks:

- Current collision rules.
- Future floor definitions.
- Future floor timer manager.

## Pillar 3: Risk Versus Reward

The safest action should not always be optimal.

Design rules:

- Creative combat increases viewer interest.
- Dangerous crafting can create stronger results.
- Time pressure makes side content costly.
- Donut's popularity can help the party but also attract attention.
- Carl's blunt solutions can solve problems while closing social doors.

Prototype hooks:

- `crude_blast_charge`
- Future crafting recipe graph.
- Future viewer score changes per event.

## Pillar 4: Carl and Donut Partnership

This is a dual-protagonist game.

Design rules:

- Donut is never a cosmetic pet.
- Donut must have separate stats, progression, dialogue, risks, and agency.
- Carl solves physical, tactical, improvised problems.
- Donut solves social, magical, and fame-driven problems.
- Some objectives should require both characters.

Prototype hooks:

- `data/characters.json`
- Donut follow behavior in `src/world.py`
- Future companion command and autonomy system.

## Pillar 5: Improvisation Over Power Fantasy

The player should survive by noticing systems and abusing opportunities.

Design rules:

- Environmental objects matter.
- Crafting should support experimentation.
- Cheap or strange items can become powerful in context.
- Combat encounters should reward positioning and setup.
- Bosses should be puzzles as much as stat checks.

Prototype hooks:

- Tutorial chest.
- First explosive crafting action.
- Future hazards and object interactions.

