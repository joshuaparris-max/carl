class TurnManager:
    def __init__(self, state, action_processor):
        self.state = state
        self.action_processor = action_processor
        self.turn_number = 0
        self.quit_requested = False

    def take_turn(self, action):
        self.turn_number += 1
        self.state.events.push("turn_started", turn=self.turn_number)
        self.quit_requested = self.action_processor.handle(action)
        self.update_companions()
        self.update_enemies()
        self.update_environment()
        self.state.events.push("turn_finished", turn=self.turn_number)
        return self.quit_requested

    def update_companions(self):
        donut = self.state.world.entities.get("donut")
        if not donut:
            return
        if donut.state.get("mode") == "follow":
            self.state.events.push("companion_updated", companion="donut", mode="follow")
        self.action_processor.combat.donut_support()

    def update_enemies(self):
        self.action_processor.combat.enemy_turns()
        for enemy in self.state.world.entities_by_type("monster"):
            if enemy.resources.health > 0:
                self.state.events.push("enemy_updated", enemy=enemy.entity_id)

    def update_environment(self):
        self.state.floor_timer -= 1
        if self.state.floor_timer in {30, 10, 5}:
            self.state.events.push("timer_warning", f"System timer warning: {self.state.floor_timer} turns remain.")
        if self.state.floor_timer <= 0:
            self.state.events.push("floor_collapsed", "The floor timer hit zero. This run is over.")
            self.quit_requested = True
        if self.state.viewer.sponsor_ready():
            self.state.events.push("sponsor_ready", self.state.announcements.emit("sponsor_ready"))
            self.state.viewer.popularity = 0
