import os


class TerminalUI:
    CONTROLS = "Controls: W/A/S/D move | X attack | U use | T talk | O open | I inventory | C craft | E equip | P pickup | B buy | F/H/R Donut | V/L/K save/load/checkpoint | Q quit"

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def render(self, state, last_message=""):
        self.clear()
        print("=== DUNGEON CRAWLER CARL: TUTORIAL GUILD ===")
        print(self.CONTROLS + "\n")
        print(state.world.render())
        print("\n" + "=" * 62)
        self.print_status(state)
        print("=" * 62)
        if last_message:
            print(last_message)

    def print_status(self, state):
        carl = state.world.carl
        donut = state.world.donut
        jacket = state.items[carl.inventory[0]]["name"] if carl.inventory else "None"
        print(
            f"Carl | Level {carl.level} | HP {carl.resources.health}/{carl.resources.max_health} "
            f"| Armor {carl.resources.armor} | Gear: {jacket} | Debuffs: {', '.join(carl.debuffs)}"
        )
        print(
            f"Donut | Level {donut.level} | HP {donut.resources.health}/{donut.resources.max_health} "
            f"| Title: Grand Champion | Mode: {donut.state.get('mode', 'follow')}"
        )
        print(f"Timer: {state.floor_timer} turns")
        print(
            f"Viewer pressure: party {state.viewer.popularity} | Carl {state.viewer.carl_popularity} "
            f"| Donut {state.viewer.donut_popularity}"
        )
        enemies = [enemy for enemy in state.world.entities_by_type("monster") if enemy.resources.health > 0]
        if enemies:
            print("Enemies: " + " | ".join(f"{enemy.name} HP {enemy.resources.health}/{enemy.resources.max_health}" for enemy in enemies))
        statuses = []
        if carl.buffs:
            statuses.append("Buffs: " + ", ".join(carl.buffs))
        if carl.status_effects:
            statuses.append("Statuses: " + ", ".join(carl.status_effects))
        if statuses:
            print(" | ".join(statuses))
        print("Quests: " + " | ".join(state.quests.active_lines()))
