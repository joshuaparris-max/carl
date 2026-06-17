"""Project scope and roadmap definitions for Dungeon Crawler Carl."""

PROJECT_PATH = "fan/internal prototype"

CANON_REFERENCE_POLICY = {
    "allowed": [
        "high-level book themes",
        "game systems inspired by the books",
        "character roles and relationships",
        "dungeon structure and floor rules",
        "viewer/sponsor pressure mechanics",
    ],
    "replaced": [
        "exact book dialogue and prose",
        "copyrighted names, titles, and branding unless licensed",
        "protected plot text and dialogue beats",
        "official audiobook performance or quotations",
        "any trademarked or branded elements",
    ],
}

TARGET_RELEASE = {
    "name": "vertical slice",
    "scope": [
        "opening survival and registration sequence",
        "Floor 1 tutorial guild segment",
        "Floor 2 escalation and training floor",
        "early hub transformation or first major transition",
    ],
    "success_criteria": [
        "player can move, interact, and navigate a first floor",
        "companion behavior and proximity dialogue are present",
        "basic quest flow completes through tutorial objectives",
        "inventory, opening actions, and simple item feedback work",
        "system announcements and show-style flavor are active",
        "the first playable build feels like a coherent dungeon crawl",
    ],
}

ROADMAP_PHASES = [
    {
        "phase": "Phase 1",
        "goal": "Systems prototype",
        "description": "Validate core mechanics in a data-driven Python prototype; keep text and map rendering simple."
    },
    {
        "phase": "Phase 2",
        "goal": "Polished 2D release",
        "description": "Move to a visual tile-based interface, improve UX, add more floors, and polish content."
    },
    {
        "phase": "Phase 3",
        "goal": "Expanded content or 3D conversion",
        "description": "Add larger dungeon scope, advanced companion systems, and consider a 3D or more cinematic presentation."
    }
]

PLATFORM_ENGINE_DECISION = {
    "platform": "PC-first",
    "prototype_engine": "Python text prototype for fast iteration",
    "target_engine": "Godot for 2D/top-down tile-based release",
    "alternative_engine": "Unity if the team chooses a commercial asset pipeline or stronger cross-platform support",
    "rationale": [
        "PC-first keeps development focused and avoids early console overhead",
        "Python prototype lets the team lock down rules before committing to art/engine work",
        "Godot is a strong fit for 2D grid/isometric tactics and rapid iteration",
        "Unity is viable later for larger scope, but it adds overhead earlier",
    ],
}


def get_project_plan():
    return {
        "project_path": PROJECT_PATH,
        "canon_reference_policy": CANON_REFERENCE_POLICY,
        "target_release": TARGET_RELEASE,
        "roadmap_phases": ROADMAP_PHASES,
        "platform_engine_decision": PLATFORM_ENGINE_DECISION,
    }
