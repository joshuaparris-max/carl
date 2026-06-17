# Lore Bible

## Purpose

This lore bible is the project's accuracy checkpoint. Every character, rule, floor identity, item type, faction, quest, and major system should be traceable here before it becomes final game content.

Use this bible to answer four questions:

- What is the canon source?
- How confirmed is it?
- How does it become gameplay?
- What is the legal/IP risk if this is distributed without a license?

## Canon Status Labels

- `confirmed`: Directly supported by the books or official material.
- `inferred`: Reasonable from canon, but not directly stated.
- `gameplay_adaptation`: Added to make canon work as an interactive game.
- `placeholder`: Temporary prototype content.
- `requires_verification`: Must be checked against the books before final use.

## Legal Risk Labels

- `low`: General game mechanic or original implementation.
- `medium`: Canon-inspired structure, name, or situation that needs review.
- `high`: Specific protected character, setting, dialogue, title, art, or scene detail.
- `licensed_only`: Use only in an official/licensed build.

## Source Reference Format

Use compact source references rather than copied prose.

Recommended format:

```text
Book 1, opening chapters, Tutorial Guild sequence
Book 1, Floor 1 entry sequence
Book 2, early floor rules explanation
Official author site, books listing, checked 2026-06-17
```

Do not paste long book passages into this project. Store short paraphrases and scene references only.

## Character References

| Entry | Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Carl | Book 1 opening | confirmed | Main player character with classless start, improvised combat, under-equipped gear state | licensed_only |
| Princess Donut | Book 1 opening | confirmed | Co-protagonist companion with separate stats, Level 0 civilian start, social/viewer strengths | licensed_only |
| Mordecai | Book 1 Tutorial Guild | confirmed | Guide/manager NPC, rules explainer, stressed advisor, dialogue escalation | licensed_only |
| System AI | Book 1 onward | confirmed | Personality-driven announcement engine and reward/punishment interface | licensed_only |

## Rule References

| Entry | Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Classless start | Book 1 early crawl | confirmed | Carl begins without class and gains build choices later | medium |
| Donut civilian start | Book 1 early crawl | confirmed | Donut has low combat readiness and must be protected before progression | medium |
| Floor timers | Book 1 onward | confirmed | Visible countdown that prevents grinding and creates forced pacing | medium |
| Achievements/rewards | Book 1 onward | confirmed | Event-triggered announcements and mechanical rewards | medium |
| Saferooms | Book 1 onward | confirmed | Safe areas with shops, rest, NPC dialogue, lockable rules | medium |

## Item Type References

| Entry | Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Carl's leather jacket | Book 1 opening | confirmed | Named torso item with armor and durability | licensed_only |
| No-pants equipment state | Book 1 opening | confirmed | Named debuff affecting armor coverage and System commentary | medium |
| Explosive materials | Book 1 onward | confirmed | Crafting category for Carl's improvised combat identity | medium |
| Tutorial chest content | Prototype design | gameplay_adaptation | Early controlled loot and crafting tutorial | low |

## Floor Identity References

| Entry | Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Tutorial Guild | Book 1 early sequence | confirmed | Opening controlled room for movement, dialogue, inventory, and System UI | licensed_only |
| Floor 1 | Book 1 | requires_verification | First real dungeon floor with timer, saferooms, first combat, loot and crafting | high |
| Floor 2 | Book 2 | requires_verification | Escalated navigation, stronger NPC/faction pressure, deeper system rules | high |
| Floor 3 | Book 3 | requires_verification | Hub/social/class identity escalation | high |

## Faction References

| Entry | Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Alien viewers | Book 1 onward | confirmed | Audience factions with preferences, popularity, and sponsor drops | medium |
| Sponsors | Book 1 onward | confirmed | Real-time rewards based on popularity and behavior | medium |
| Saferoom commerce groups | Book 1 onward | requires_verification | Economy and NPC pressure inside safe zones | high |

## Current Prototype Lore Entries

| Prototype Feature | Canon Source | Canon Status | Gameplay Translation | Legal Risk |
|---|---|---|---|---|
| Carl entity | Book 1 opening | confirmed | Player character, Level 1, classless, low charisma, starting jacket | licensed_only |
| Donut entity | Book 1 opening | confirmed | Companion, Level 0, high charisma/fame, civilian debuff | licensed_only |
| Mordecai entity | Book 1 Tutorial Guild | requires_verification | Guide NPC behind desk with rising stress | licensed_only |
| Tutorial Guild 12x12 room | Prototype | placeholder | Test map for movement, interaction, chest, and quest flow | low |
| Unstable Dungeon Powder | Prototype | gameplay_adaptation | Starter explosive material for crafting tutorial | low |
| Crude Blast Charge | Prototype | gameplay_adaptation | First crafted explosive item | low |
| Original System messages | Project writing | gameplay_adaptation | Placeholder tone for announcement engine | low |

## Verification Backlog

- Verify Mordecai's exact form, role, and constraints in the Tutorial Guild sequence.
- Verify Carl's starting equipment and wording around the jacket, socks, underwear, and lack of pants.
- Verify Donut's initial level, title presentation, and when combat progression begins.
- Verify Floor 1 environment identity before locking biome art.
- Verify class-selection timing and available options before implementing final class trees.
- Verify saferoom economy details before writing faction-specific commerce.

