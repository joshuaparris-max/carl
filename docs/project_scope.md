# Project Scope, Vision, and Release Plan

## Project Path
- Chosen path: **fan/internal prototype**
- Allowed source material:
  - high-level book themes
  - character roles and relationships
  - dungeon mechanics and floor rules
  - viewer/sponsor-style pressure systems
- Replaced content:
  - exact book dialogue and prose
  - copyrighted names, titles, and branding unless licensed
  - protected plot text and quotes
  - official audiobook or media assets

## Target Release
- Name: **Vertical Slice**
- Scope:
  - opening survival and registration sequence
  - Floor 1 tutorial guild segment
  - Floor 2 escalation and training floor
  - early hub transformation or first major transition
- Success criteria:
  - player movement and floor navigation work
  - companion behavior and proximity dialogue exist
  - basic quest flow completes tutorial objectives
  - inventory, open/interact actions, and item feedback work
  - system announcements and show-style flavor are active
  - first playable build feels like a coherent dungeon crawl

## Production Roadmap
- Phase 1: **Systems prototype**
  - tighten rules using a data-driven Python build
  - keep presentation simple
  - validate movement, interaction, companion AI, and quests
- Phase 2: **Polished 2D release**
  - add visual tile rendering
  - improve UI, menus, and controls
  - expand content beyond the tutorial
- Phase 3: **Expanded content or 3D conversion**
  - add deeper floors, more mechanics, and polish
  - evaluate a 3D or higher-fidelity presentation later

## Platform & Engine Choice
- Platform: **PC-first**
- Prototype approach: **Python text prototype** for fast iteration
- Recommended target engine: **Godot** for 2D/top-down tile-based release
- Alternative engine: **Unity** if the team prioritizes commercial pipeline or multi-platform release
- Rationale:
  - PC-first avoids early console certification and input complexity
  - Python prototype lets core game rules be locked down before art or engine work
  - Godot is well-suited to 2D tile-based tactics and rapid iteration
  - Unity is viable later but adds overhead for a small prototype
