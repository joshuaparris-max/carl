import json
from pathlib import Path


SAVE_PATH = Path(__file__).resolve().parents[1] / "savegame.json"


def save_game(world, quest_log, state=None):
    data = {
        "entities": {
            entity_id: {
                "x": entity.x,
                "y": entity.y,
                "inventory": entity.inventory,
                "equipment": entity.equipment,
                "debuffs": entity.debuffs,
                "buffs": entity.buffs,
                "status_effects": entity.status_effects,
                "level": entity.level,
                "resources": entity.resources.__dict__,
                "state": entity.state,
            }
            for entity_id, entity in world.entities.items()
        },
        "objects": {
            object_id: {
                "state": obj.state,
                "symbol": obj.symbol,
                "blocks_movement": obj.blocks_movement,
            }
            for object_id, obj in world.objects.items()
        },
        "quests": {
            quest_id: {
                "completed": quest["completed"],
                "objectives": [
                    {
                        "id": objective["id"],
                        "current": objective["current"],
                        "completed": objective["completed"],
                    }
                    for objective in quest["objectives"]
                ],
            }
            for quest_id, quest in quest_log.quests.items()
        },
        "floor_timer": state.floor_timer if state else None,
        "viewer": state.viewer.__dict__ if state else None,
    }
    with SAVE_PATH.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
    return SAVE_PATH


def load_game(world, quest_log, state=None):
    if not SAVE_PATH.exists():
        return False
    with SAVE_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    for entity_id, values in data.get("entities", {}).items():
        entity = world.entities.get(entity_id)
        if not entity:
            continue
        entity.x = values["x"]
        entity.y = values["y"]
        entity.inventory = values.get("inventory", entity.inventory)
        entity.equipment = values.get("equipment", entity.equipment)
        entity.debuffs = values.get("debuffs", entity.debuffs)
        entity.buffs = values.get("buffs", entity.buffs)
        entity.status_effects = values.get("status_effects", entity.status_effects)
        entity.level = values.get("level", entity.level)
        for resource_name, resource_value in values.get("resources", {}).items():
            if hasattr(entity.resources, resource_name):
                setattr(entity.resources, resource_name, resource_value)
        entity.state = values.get("state", entity.state)

    for object_id, values in data.get("objects", {}).items():
        obj = world.objects.get(object_id)
        if not obj:
            continue
        obj.state = values.get("state", obj.state)
        obj.symbol = values.get("symbol", obj.symbol)
        obj.blocks_movement = values.get("blocks_movement", obj.blocks_movement)
    for quest_id, values in data.get("quests", {}).items():
        if quest_id in quest_log.quests:
            quest_log.quests[quest_id]["completed"] = values.get("completed", False)
            by_id = {objective["id"]: objective for objective in quest_log.quests[quest_id]["objectives"]}
            for saved_objective in values.get("objectives", []):
                objective = by_id.get(saved_objective["id"])
                if objective:
                    objective["current"] = saved_objective.get("current", objective["current"])
                    objective["completed"] = saved_objective.get("completed", objective["completed"])
    if state:
        if data.get("floor_timer") is not None:
            state.floor_timer = data["floor_timer"]
        if data.get("viewer"):
            for key, value in data["viewer"].items():
                if hasattr(state.viewer, key):
                    setattr(state.viewer, key, value)
    return True
