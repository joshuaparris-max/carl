from src.announcements import AnnouncementManager
from src.data_repository import DataRepository
from src.engine.actions import ActionProcessor
from src.engine.events import EventQueue
from src.engine.turns import TurnManager
from src.game_state import GameState
from src.quests import QuestLog
from src.ui.terminal import TerminalUI
from src.world import GameWorld


class Game:
    def __init__(self, data_repository=None, ui=None):
        self.data = (data_repository or DataRepository()).load()
        self.events = EventQueue()
        self.world = GameWorld(
            self.data.map_rows,
            self.data.characters,
            objects=self.data.objects,
            hazards=self.data.hazards,
        )
        self.announcements = AnnouncementManager(self.data.announcements)
        self.quests = QuestLog(self.data.quests)
        self.state = GameState(
            data=self.data,
            world=self.world,
            announcements=self.announcements,
            quests=self.quests,
            events=self.events,
        )
        self.action_processor = ActionProcessor(self.state)
        self.turns = TurnManager(self.state, self.action_processor)
        self.ui = ui or TerminalUI()
        self.last_message = self.announcements.emit("welcome", crawler=self.world.carl.name)

    def run(self):
        while True:
            self.display()
            action = input("\nAction: ")
            quit_requested = self.handle_action(action)
            if quit_requested:
                self.display()
                break

    def display(self):
        self.ui.render(self.state, self.last_message)

    def handle_action(self, action):
        quit_requested = self.turns.take_turn(action)
        self.last_message = self.collect_messages()
        return quit_requested

    def collect_messages(self):
        messages = []
        drained = self.events.drain()
        # store last drained events for UI use
        self.state.last_events = drained
        for event in drained:
            if event.message:
                messages.append(event.message)
        return "\n".join(messages)

    # Compatibility wrappers for existing tests and quick scripts.
    def talk(self):
        self.handle_action("t")

    def open_nearby(self):
        self.handle_action("o")

    def show_inventory(self):
        self.handle_action("i")

    def craft(self):
        self.handle_action("c")

    def escalating_donut_complaint(self):
        return self.state.escalating_donut_complaint()
