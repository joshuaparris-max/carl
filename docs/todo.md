Inspecting the existing project plan and core code structure so the task list matches the current implementation.

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/Dungeon_Crawler_Carl_Game_Build_Plan.md#1-1), lines 1 to 260

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/crawler.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/world.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/game.py)

Reviewing the actual implementation and data files to make the task list tightly aligned with the current prototype.

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/entity.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/data_loader.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/announcements.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/src/quests.py)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/tests/test_world.py)

Gathering current data and content files to ensure the to-do list reflects actual scope and prototype state.

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/data/characters.json)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/data/dialogue.json)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/data/items.json)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/data/quests.json)

Read [](file:///c%3A/Users/Josh/OneDrive%20-%20Dubbo%20Christian%20School/Documents/Dungeon%20Crawler%20Carl/data/announcements.json)

## Detailed To-Do List for Making This Project Happen

### 1. Define Scope, Vision, and Release Plan
- Decide project path
  - Official/licensed adaptation versus fan/internal prototype
  - If unlicensed, define which book elements can be referenced and which must be replaced with original analogues
- Set target release
  - Minimum vertical slice: opening survival, Floor 1 tutorial, Floor 2 escalation, early hub transformation
  - Define success criteria for first playable version
- Create a production roadmap
  - Phase 1: systems prototype
  - Phase 2: polished 2D release
  - Phase 3: expanded content or 3D conversion
- Establish platform and engine choice
  - PC-first recommendation
  - Evaluate Godot vs Unity vs text prototype continuation

### 2. Research, Lore, and Design Foundations
- Build a Lore Bible
  - Canon source references for characters, rules, floor identity, item types, factions
  - Track source, canon status, gameplay translation, legal risk
- Define core tone and pillars
  - Absurd televised dungeon, cruel rules, risk vs reward, Carl/Donut partnership
- Design primary systems before implementation
  - Character progression
  - Floor rules and mechanics
  - Companion behavior
  - Viewer/sponsor pressure and announcements
- Document playable features
  - Floor generation/authoring
  - Encounters and hazards
  - Loot and crafting
  - Dialogue and banter
  - Quest systems

### 3. Architecture and Codebase Improvements
- Refactor current prototype into modular architecture
  - Separate engine, game logic, UI, and data
  - Move from hard-coded behavior to data-driven systems
- Improve core data loading and validation
  - Define schemas for characters, items, dialogue, quests, announcements, maps
  - Add validation and error handling for JSON content
- Expand entity and world models
  - Add entity types for monsters, NPCs, objects, hazards
  - Add full position/state handling for companions, enemies, items
  - Add status effects, buffs/debuffs, health, stamina, armor
- Implement a proper game loop
  - event queue or turn system
  - update cycles for player, companion, enemies, environment
- Add test coverage
  - Unit tests for world movement, collision, quest completion, announcements, item handling
  - Integration tests for key scenario flows
  - Expand beyond current test_world.py

### 4. Core Gameplay Systems
- Movement and navigation
  - Validate tile collisions and entity blocking for all entity types
  - Add companion pathing and collision avoidance
  - Add tile effects like hazards, traps, and terrain
- Combat and encounters
  - Create enemy stats, attack resolution, hit/miss, damage, armor
  - Add companion combat actions
  - Allow player abilities and items to interact with combat
- Inventory, equipment, and items
  - Expand inventory system with slots, stackable items, consumables
  - Add equip/unequip actions and item stats
  - Implement item pickups, chest opening, shops or loot pools
- Quest and objective systems
  - Add quest state progression, objectives, rewards
  - Support active and completed quest display
  - Add tasks beyond tutorial: exploration, rescue, item retrieval, rule exploits
- Dialogue and NPC interaction
  - Add talk actions for more NPCs
  - Add branching or context-sensitive dialogue
  - Add companion banter and world text responses
- Announcement and show system
  - Expand event types: floor start/end, dawn bells, sponsor messages, viewer polls
  - Tie announcements to game events and failure states
- HUD and status display
  - Show health, armor, statuses, objectives, timeline, viewer pressure
  - Add feedback for companion and system state
- Save/load
  - Implement save state and restore functionality
  - Support restart from checkpoint or dungeon entry

### 5. Map, Level, and Content Pipeline
- Design and author dungeon and hub maps
  - Tutorial guild room
  - Early floors with themed hazards and rules
  - Saferooms and stairwells
- Create floor rule definitions
  - Floor-specific mechanics, timers, monster tables, loot tables
- Build a content editor or pipeline
  - Map format improvements beyond plain text if needed
  - Data-driven spawn tables and event triggers
- Populate game content
  - Enemies and hazard definitions
  - Items, crafting materials, and gear
  - NPCs with roles, relationships, and dialogue
  - Quests, tasks, and achievements
- Add narrative and flavor content
  - Original game dialogue, announcements, and lore text
  - Donut banter and player commentary
  - In-world rules explanations without copying book text

### 6. UI/UX, Presentation, and Controls
- Replace text-only renderer with proper visual interface
  - Tile-based display, map, and entity symbols
  - Option for ASCII plus more graphical representation later
- Add input handling improvements
  - More commands than W/A/S/D/T/O/I/Q
  - Support keyboard, mouse, and later controller
- Create menus
  - Main menu, settings, inventory screen, character sheet
- Add feedback and polish
  - Clear messages for invalid actions, attack results, quest updates
  - Smooth companion movement and animation placeholder
- Plan art direction
  - Decide on 2D pixel/tile art or simple UI styling
  - Placeholder art and icons for prototype

### 7. Companion and NPC Systems
- Upgrade Donut behavior
  - Avoid hazards, react to enemy threats, follow intelligently
  - Add commands and behavior modes (stay, follow, attack, retreat)
  - Add relationship/trust state and morale effects
- Improve NPC roles
  - Mordecai as guide, quest giver, crafting advisor
  - Add other NPCs with unique duties and interactions
- Add companion vulnerability
  - Donut can be hurt, targeted, and require protection
  - Create consequences for separation or injury

### 8. Polishing Production Requirements
- Add audio
  - UI sounds, environmental effects, combat sounds, announcements
- Add save and replayability features
  - Randomized elements, procedural encounters or authored variety
- Add accessibility
  - Text scaling, color contrast, control remapping
- Add analytics for playtesting
  - Track progress, failure points, time spent in floors
- Localize or prepare for localization
  - Keep all text in data assets

### 9. Testing, Validation, and Iteration
- Create a playtesting plan
  - Early internal tests for core mechanics
  - Iterate on difficulty, flow, and system clarity
- Establish bug tracking and task management
  - Turn this to-do list into issue backlog
- Validate legal / IP safety
  - Review all text, names, and art for unlicensed compliance if not licensed

### 10. Release and Post-Release Plan
- Prepare a demo or vertical slice
  - Publish a playable early version to collect feedback
- Plan expansions
  - Next floors, more show mechanics, additional companions
- Document decisions
  - Keep design notes, system specs, lore bible, and implementation notes updated

---

## Immediate Next Work Items
- Choose project path: licensed vs unlicensed prototype
- Define MVP content and playable scope
- Refactor current prototype into modular game and data systems
- Expand world/entity models and add proper content schemas
- Implement interactive inventory, combat, and dialogue systems beyond tutorial

## Prioritized Issue Tracker

| Priority | Task | Notes |
|---|---|---|
| Now | Decide project path and legal approach | Confirm fan/internal prototype stance and unlicensed content rules |
| Now | Define vertical slice scope and success criteria | Lock down MVP goals and acceptance criteria |
| Now | Create a modular Python prototype structure | Separate game logic, data, and UI paths |
| Now | Add data validation for JSON assets | Validate characters, items, dialogue, quests, announcements |
| Now | Expand core world/entity model | Support companions, NPC interactions, and entity states |
| Next | Implement a turn-based game loop | Add player, companion, and environment update cycles |
| Next | Add quest state progression and display | Track objectives, completion, and quest lines |
| Next | Add basic interaction actions | Talk, open, inventory, inspect |
| Next | Improve map rendering and collision handling | Support multiple entity types and tile blocks |
| Next | Create floor definitions and tutorial rules | Data-drive floor behavior and tutorial objectives |
| Later | Add item equipment and inventory slot handling | Chest/loot interactions and equipment state |
| Later | Add status effects, health, armor, combat | Implement simple resolution mechanics |
| Later | Add companion behavior modes | Stay, follow, combat, and Donut safety systems |
| Later | Create announcement/event system | Tie system messages to game state and failure events |
| Later | Build UI/UX flow for menu and status | Inventory screen, main menu, player feedback |
| Backlog | Add audio and visual polish | 2D presentation and asset improvements |
| Backlog | Build content pipeline | Maps, spawn tables, event triggers |
| Backlog | Design additional floors and hub areas | Narrative content and expanded dungeon design |
| Backlog | Add save/load and checkpoint systems | Persist game progress and restore points |
| Backlog | Add playtesting instrumentation and accessibility | Track play patterns and support options |

### Milestones
1. **Prototype Foundation:** path decision, roadmap, modular codebase, data validation, world/entity model
2. **Playable Core:** turn loop, interactions, quests, map rules, tutorial scenario
3. **Gameplay Polishing:** combat, companion systems, announcements, UI flow
4. **Content Expansion:** more floors, narrative, loot, polish, audio/visual enhancements

### Dependencies
- Project path decision before finalizing lore/legal constraints
- Data schemas before adding complex content or UI
- Modular game loop before companion AI and combat systems
- Floor definitions before quest and event progression

### Current Prototype Status
- `crawler.py` launches the playable terminal demo with `src/game.py` driving the turn loop.
- Active game systems include movement, talk, open chest, inventory, craft, attack, use item, equip, pickup, shop, companion modes, save/load/checkpoint, and quit.
- Quest progression now updates in real time and quest completion messages display immediately.
- The world renders the tutorial map, entities, objects, hazards, and enemy turns.
- Unit/integration tests are passing with `unittest discover tests`.