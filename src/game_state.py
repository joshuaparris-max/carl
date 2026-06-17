from src.viewer import ViewerState
import copy


class GameState:
    def __init__(self, data, world, announcements, quests, events):
        self.data = data
        self.world = world
        self.items = data.items
        self.dialogue = data.dialogue
        self.announcements = announcements
        self.quests = quests
        self.events = events
        self.dialogue_index = {"mordecai": 0}
        self.floor_timer = 100
        self.viewer = ViewerState()
        self.checkpoint = None
        self.rolls = []

    def next_roll(self, sides):
        if self.rolls:
            return self.rolls.pop(0)
        return 50 if sides >= 50 else 1

    def inventory_lines(self, entity_id):
        entity = self.world.entities[entity_id]
        counts = {}
        for item_id in entity.inventory:
            counts[item_id] = counts.get(item_id, 0) + 1
        lines = []
        for item_id, count in counts.items():
            item = self.items[item_id]
            bits = []
            if "armor" in item:
                bits.append(f"armor {item['armor']}")
            if "durability" in item:
                bits.append(f"durability {item['durability']}")
            if "crafting_power" in item:
                bits.append(f"crafting power {item['crafting_power']}")
            if "damage" in item:
                bits.append(f"damage {item['damage']}")
            if item_id in entity.equipment.values():
                bits.append("equipped")
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"{item['name']}{qty}: {', '.join(bits) or 'utility item'}")
        return lines

    def consume_item(self, entity_id, item_id):
        inventory = self.world.entities[entity_id].inventory
        if item_id in inventory:
            inventory.remove(item_id)
            return True
        return False

    def make_checkpoint(self):
        self.checkpoint = {
            "entities": copy.deepcopy(self.world.entities),
            "objects": copy.deepcopy(self.world.objects),
            "quests": copy.deepcopy(self.quests.quests),
            "floor_timer": self.floor_timer,
            "viewer": copy.deepcopy(self.viewer),
        }

    def restore_checkpoint(self):
        if not self.checkpoint:
            self.events.push("checkpoint_missing", "No checkpoint exists yet.")
            return False
        self.world.entities = copy.deepcopy(self.checkpoint["entities"])
        self.world.objects = copy.deepcopy(self.checkpoint["objects"])
        self.quests.quests = copy.deepcopy(self.checkpoint["quests"])
        self.floor_timer = self.checkpoint["floor_timer"]
        self.viewer = copy.deepcopy(self.checkpoint["viewer"])
        return True

    def find_available_recipe(self, entity_id):
        inventory = self.world.entities[entity_id].inventory
        inventory_counts = {item_id: inventory.count(item_id) for item_id in set(inventory)}
        for recipe in self.data.recipes.values():
            if all(inventory_counts.get(item_id, 0) >= recipe["ingredients"].count(item_id) for item_id in set(recipe["ingredients"])):
                return recipe
        return None

    def equip_first_available(self, entity_id):
        entity = self.world.entities[entity_id]
        equipped_items = set(entity.equipment.values())
        for item_id in entity.inventory:
            if item_id in equipped_items:
                continue
            item = self.items[item_id]
            slot = item.get("slot")
            if slot in {"torso", "legs", "weapon"}:
                previous = entity.equipment.get(slot)
                entity.equipment[slot] = item_id
                self.recalculate_armor(entity_id)
                return f"Equipped {item['name']}."
        return "No equippable item available."

    def recalculate_armor(self, entity_id):
        entity = self.world.entities[entity_id]
        armor = 0
        for item_id in entity.equipment.values():
            armor += self.items.get(item_id, {}).get("armor", 0)
        entity.resources.armor = armor

    def escalating_donut_complaint(self):
        steps = [
            "Donut: Carl, this floor is unspeakably filthy.",
            "Donut: I can feel the grime between my toes. This is a hate crime against grooming.",
            "Donut: My fans must never see me like this. Walk softer.",
        ]
        index = min(self.dialogue_index["mordecai"], len(steps) - 1)
        return steps[index]
