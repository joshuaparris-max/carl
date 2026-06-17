from src.save_system import load_game, save_game
from src.engine.combat import CombatSystem


MOVES = {
    "w": (0, -1),
    "s": (0, 1),
    "a": (-1, 0),
    "d": (1, 0),
}


class ActionProcessor:
    def __init__(self, state):
        self.state = state
        self.combat = CombatSystem(state)

    def handle(self, action):
        action = action.strip().lower()
        if action in MOVES:
            return self._move(action)
        if action == "t":
            return self._talk()
        if action == "o":
            return self._open()
        if action == "i":
            return self._inventory()
        if action == "c":
            return self._craft()
        if action == "x":
            return self._attack()
        if action == "u":
            return self._use_item()
        if action == "e":
            return self._equip()
        if action == "p":
            return self._pickup()
        if action == "b":
            return self._buy()
        if action in {"f", "h", "r"}:
            return self._companion_mode(action)
        if action == "k":
            restored = self.state.restore_checkpoint()
            if restored:
                self.state.events.push("checkpoint_loaded", "Checkpoint restored.")
            return False
        if action == "v":
            path = save_game(self.state.world, self.state.quests, self.state)
            self.state.make_checkpoint()
            self.state.events.push("game_saved", f"Game saved: {path.name}")
            return False
        if action == "l":
            loaded = load_game(self.state.world, self.state.quests, self.state)
            message = "Game loaded." if loaded else "No save file exists yet."
            self.state.events.push("game_loaded", message, loaded=loaded)
            return False
        if action == "q":
            message = self.state.announcements.emit("quit")
            self.state.events.push("quit", message)
            return True

        self.state.events.push("invalid_action", "Invalid command. Use W/A/S/D, T, O, I, C, X, U, E, P, B, F/H/R, V, L, K, or Q.")
        return False

    def _move(self, action):
        dx, dy = MOVES[action]
        moved = self.state.world.move_entity("carl", dx, dy)
        if not moved:
            message = self.state.announcements.emit("bump")
            self.state.events.push("movement_blocked", message, actor="carl")
            self.state.quests.record_event("movement_blocked")
            return False

        self.state.world.follow_entity("donut", "carl")
        completed_messages = self.state.quests.record_event("player_moved")
        self.state.events.push("player_moved", actor="carl", dx=dx, dy=dy)
        for msg in completed_messages:
            self.state.events.push("quest_completed", msg)

        hazard = self.state.world.hazard_at(self.state.world.carl.x, self.state.world.carl.y)
        if hazard:
            self._apply_hazard(hazard)

        if self.state.world.near("mordecai"):
            self.state.events.push("near_npc", "Mordecai is close enough to talk. Press T.", npc="mordecai")
        else:
            self.state.events.push("companion_banter", self.state.escalating_donut_complaint())
        return False

    def _talk(self):
        npc = self.state.world.near_entity(entity_type="npc")
        if not npc:
            self.state.events.push("talk_failed", "There is nobody close enough to talk to.")
            return False

        lines = self.state.dialogue[npc.entity_id]
        index = self.state.dialogue_index.get(npc.entity_id, 0)
        message = lines[index]["text"]
        self.state.dialogue_index[npc.entity_id] = min(index + 1, len(lines) - 1)
        self.state.events.push("dialogue", message, speaker=npc.entity_id)
        if npc.entity_id == "mordecai" and index >= 1:
            completed_messages = self.state.quests.record_event("spoke_to_mordecai")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
        return False

    def _open(self):
        obj = self.state.world.near_object(object_type="chest")
        if not obj:
            self.state.events.push("open_failed", "Nothing nearby opens. The desk definitely does not count.")
            return False
        if obj.state.get("opened"):
            self.state.events.push("open_failed", "The tutorial chest is already open. Donut is still disappointed by its presentation.")
            return False

        obj.state["opened"] = True
        obj.blocks_movement = False
        obj.symbol = "."
        for item_id in obj.state.get("contains", []):
            self.state.world.carl.inventory.append(item_id)
        message = self.state.announcements.emit("chest_opened")
        self.state.events.push("object_opened", message, object_id=obj.object_id)
        completed_messages = self.state.quests.record_event("opened_tutorial_chest")
        for msg in completed_messages:
            self.state.events.push("quest_completed", msg)
        return False

    def _inventory(self):
        lines = self.state.inventory_lines("carl")
        completed_messages = self.state.quests.record_event("inspected_inventory")
        self.state.events.push("inventory_viewed", "\n".join(lines) if lines else "Inventory empty.")
        for msg in completed_messages:
            self.state.events.push("quest_completed", msg)
        return False

    def _craft(self):
        recipe = self.state.find_available_recipe("carl")
        if not recipe:
            self.state.events.push("craft_failed", "Carl needs something unstable before he can make something worse.")
            return False
        actor = self.state.world.carl
        for ingredient in recipe["ingredients"]:
            actor.inventory.remove(ingredient)
        actor.inventory.append(recipe["result"])
        message = self.state.announcements.emit(recipe.get("announcement", "crafted_explosive"))
        self.state.events.push("item_crafted", message, recipe_id=recipe["id"], item_id=recipe["result"])
        completed_messages = self.state.quests.record_event("crafted_first_explosive")
        for msg in completed_messages:
            self.state.events.push("quest_completed", msg)
        return False

    def _attack(self):
        target = self.combat.nearest_enemy("carl", distance=1)
        if not target:
            self.state.events.push("attack_failed", "Carl swings at the concept of danger. Nothing happens.")
            return False
        message = self.combat.attack("carl", target.entity_id)
        if message:
            self.state.events.push("combat_result", message)
        self.state.viewer.change(1, "basic violence", target="carl")
        return False

    def _use_item(self):
        actor = self.state.world.carl
        explosive = next((item_id for item_id in actor.inventory if "explosive" in self.state.items[item_id].get("tags", [])), None)
        if not explosive:
            self.state.events.push("use_failed", "Carl has nothing explosively useful ready.")
            return False
        target = self.combat.nearest_enemy("carl", distance=3)
        if not target:
            self.state.events.push("use_failed", "No enemy is close enough to make this a responsible bad idea.")
            return False
        message = self.combat.attack("carl", target.entity_id, item_id=explosive)
        if message:
            self.state.events.push("combat_result", message)
        self.state.viewer.change(6, "explosive problem solving", target="carl")
        return False

    def _equip(self):
        message = self.state.equip_first_available("carl")
        self.state.events.push("equipment_changed", message)
        return False

    def _pickup(self):
        obj = self.state.world.near_object(object_type="pickup", distance=0)
        if not obj:
            self.state.events.push("pickup_failed", "There is nothing here to pick up.")
            return False
        item_id = obj.state.get("item_id")
        if not item_id:
            self.state.events.push("pickup_failed", "That pickup is suspiciously empty.")
            return False
        self.state.world.carl.inventory.append(item_id)
        obj.state["picked_up"] = True
        obj.symbol = "."
        obj.x = -1
        obj.y = -1
        completed_messages = self.state.quests.record_event("picked_up_item")
        self.state.events.push("item_picked_up", f"Picked up {self.state.items[item_id]['name']}.", item_id=item_id)
        for msg in completed_messages:
            self.state.events.push("quest_completed", msg)
        return False

    def _buy(self):
        shop = self.state.world.near_object(object_type="shop")
        if not shop:
            self.state.events.push("shop_failed", "No shop is close enough to overcharge you.")
            return False
        if not shop.shop_inventory:
            self.state.events.push("shop_failed", "The shop has nothing useful, which feels personal.")
            return False
        item_id = shop.shop_inventory[0]
        self.state.world.carl.inventory.append(item_id)
        self.state.events.push("shop_purchase", f"Bought {self.state.items[item_id]['name']} from {shop.name}.")
        return False

    def _companion_mode(self, action):
        modes = {"f": "follow", "h": "hide", "r": "retreat"}
        mode = modes[action]
        self.state.world.donut.state["mode"] = mode
        self.state.events.push("companion_mode", f"Donut mode set to {mode}.", mode=mode)
        return False

    def _apply_hazard(self, hazard):
        carl = self.state.world.carl
        if hazard.effect == "trap":
            damage = max(1, hazard.severity - carl.resources.armor)
            carl.resources.health = max(0, carl.resources.health - damage)
            self.state.events.push("hazard_triggered", f"Trap triggered: Carl takes {damage} damage.", hazard=hazard.hazard_id)
            completed_messages = self.state.quests.record_event("triggered_hazard")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
        elif hazard.effect == "rough":
            carl.resources.stamina = max(0, carl.resources.stamina - 1)
            self.state.events.push("hazard_triggered", "Rough terrain costs Carl 1 stamina.", hazard=hazard.hazard_id)
            completed_messages = self.state.quests.record_event("triggered_hazard")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
        else:
            self.state.events.push("hazard_triggered", "Donut: Carl, I do not like that tile.", hazard=hazard.hazard_id)
            completed_messages = self.state.quests.record_event("triggered_hazard")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
