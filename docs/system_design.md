# Primary System Design

## Character Progression

### Goals

- Support separate Carl and Donut growth.
- Delay major class identity until the correct narrative stage.
- Make equipment state matter.
- Track achievements and System rewards.

### Data Needed

- Character base stats.
- Level and XP.
- Class state: `classless`, `candidate`, `selected`.
- Skill trees.
- Equipment slots.
- Debuffs and status effects.
- Titles and fame modifiers.

### Carl

Carl progression emphasizes:

- Strength and durability.
- Improvised weapons.
- Explosive crafting.
- Environmental tactics.
- Rule exploitation.

Early game requirements:

- Starts classless.
- Starts with the leather jacket as named gear.
- Starts with `no_pants` as a debuff.
- Gains access to explosive crafting through discovery, not a normal spell list.

### Donut

Donut progression emphasizes:

- Charisma.
- Fame.
- Agility.
- Social unlocks.
- Magic/support growth.
- Companion commands and autonomy.

Early game requirements:

- Starts Level 0 civilian.
- Has separate stat sheet.
- Is vulnerable before combat progression.
- Has stronger viewer appeal than Carl.

## Floor Rules and Mechanics

### Goals

- Every floor has a distinct identity.
- Floor rules create pressure and alter player behavior.
- Timers force movement and prevent grinding.

### Floor Data

Each floor should eventually have:

- `floor_id`
- `display_name`
- `canon_source`
- `canon_status`
- `legal_risk`
- `timer_minutes`
- `biome_tags`
- `safe_room_rules`
- `enemy_tables`
- `loot_tables`
- `hazards`
- `special_rules`
- `exit_conditions`

### First Implementation Target

Add `data/floors.json` with:

- Tutorial Guild.
- Floor 1 placeholder.
- Timer support.
- Safe room flag.
- Entry and exit coordinates.

## Companion Behavior

### Goals

- Donut follows intelligently.
- Donut avoids obvious hazards.
- Donut can be commanded.
- Donut reacts verbally to context.
- Donut can unlock non-combat opportunities.

### Behavior Modes

- `follow`: stay close to Carl.
- `stay`: hold position.
- `hide`: avoid enemies and hazards.
- `assist`: use support/social/combat action when available.
- `retreat`: move toward safe zone or Carl.

### Triggered Reactions

- Dirty/smelly tile.
- Low health.
- Carl opens loot.
- Carl bumps wall.
- Enemy appears.
- Viewer count changes.
- Sponsor drop lands.
- Floor timer warning.

### First Implementation Target

Add a `companion_mode` field and commands:

- `F`: follow.
- `H`: hide.
- `R`: retreat.

## Viewer, Sponsor, and Announcements

### Goals

- Make the show layer mechanically real.
- Tie announcements to game events.
- Track popularity separately for Carl and Donut.
- Reward spectacle but create risk.

### Viewer Data

Track:

- Party popularity.
- Carl popularity.
- Donut popularity.
- Audience faction scores.
- Recent spectacle events.
- Sponsor eligibility.

### Event Examples

- Creative kill.
- First crafted explosive.
- Donut survives danger.
- Carl takes damage due to no-pants state.
- Timer reaches warning threshold.
- Player spends too long in a safe room.

### Sponsor Drops

Sponsor drop data:

- Trigger event.
- Minimum popularity.
- Faction source.
- Drop table.
- Risk modifier.
- System announcement.

### First Implementation Target

Add `viewer_state.json` defaults and update popularity when:

- Inventory inspected.
- Chest opened.
- First explosive crafted.
- Wall bumped.

