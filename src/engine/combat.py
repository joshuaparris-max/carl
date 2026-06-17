class CombatSystem:
    def __init__(self, state):
        self.state = state

    def attack(self, attacker_id, target_id, item_id=None):
        attacker = self.state.world.entities[attacker_id]
        target = self.state.world.entities[target_id]
        if target.resources.health <= 0:
            return f"{target.name} is already down."

        weapon = self.state.items.get(item_id, {}) if item_id else {}
        accuracy = weapon.get("accuracy", 80) + attacker.stats.get("dexterity", 0) * 2
        roll = self.state.next_roll(100)
        if roll > accuracy:
            return f"{attacker.name} misses {target.name}."

        base_damage = weapon.get("damage", 1 + attacker.stats.get("strength", 1) // 2)
        if item_id and "consumable" in weapon.get("tags", []):
            self.state.consume_item(attacker_id, item_id)
        damage = max(0, base_damage - target.resources.armor)
        target.resources.health = max(0, target.resources.health - damage)

        self.state.events.push(
            "combat_hit",
            f"{attacker.name} hits {target.name} for {damage} damage.",
            attacker=attacker_id,
            target=target_id,
            damage=damage,
        )
        if target.resources.health <= 0:
            self.state.events.push("entity_defeated", f"{target.name} is defeated.", target=target_id)
            completed_messages = self.state.quests.record_event("defeated_enemy")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
            self.state.viewer.change(5, "creative violence remains a marketable asset")
        return ""

    def nearest_enemy(self, origin_id="carl", distance=1):
        origin = self.state.world.entities[origin_id]
        living = [
            enemy
            for enemy in self.state.world.entities_by_type("monster")
            if enemy.resources.health > 0
            and abs(origin.x - enemy.x) <= distance
            and abs(origin.y - enemy.y) <= distance
        ]
        return living[0] if living else None

    def enemy_turns(self):
        for enemy in self.state.world.entities_by_type("monster"):
            if enemy.resources.health <= 0:
                continue
            target = self._enemy_target(enemy)
            if not target:
                continue
            damage = max(0, 2 - target.resources.armor)
            target.resources.health = max(0, target.resources.health - damage)
            self.state.events.push(
                "enemy_attack",
                f"{enemy.name} claws {target.name} for {damage} damage.",
                attacker=enemy.entity_id,
                target=target.entity_id,
                damage=damage,
            )
            if target.resources.health <= 0:
                self.state.events.push("party_member_down", f"{target.name} goes down.", target=target.entity_id)

    def donut_support(self):
        donut = self.state.world.donut
        if donut.resources.health <= 0:
            return
        enemy = self.nearest_enemy("donut", distance=2)
        if not enemy:
            return
        if donut.state.get("mode") == "hide":
            self.state.events.push("companion_action", "Donut stays hidden and complains silently, which is frankly impressive.")
            return
        damage = 1
        enemy.resources.health = max(0, enemy.resources.health - damage)
        self.state.events.push("companion_action", f"Donut swipes at {enemy.name} for {damage} damage.", target=enemy.entity_id)
        if enemy.resources.health <= 0:
            self.state.events.push("entity_defeated", f"{enemy.name} is defeated.", target=enemy.entity_id)
            completed_messages = self.state.quests.record_event("defeated_enemy")
            for msg in completed_messages:
                self.state.events.push("quest_completed", msg)
            self.state.viewer.change(8, "Donut did something adorable and violent")

    def _enemy_target(self, enemy):
        targets = [self.state.world.carl, self.state.world.donut]
        adjacent = [
            target
            for target in targets
            if target.resources.health > 0
            and abs(enemy.x - target.x) <= 1
            and abs(enemy.y - target.y) <= 1
        ]
        if not adjacent:
            return None
        return min(adjacent, key=lambda entity: entity.resources.health)
