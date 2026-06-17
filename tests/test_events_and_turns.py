import unittest

from src.engine.events import EventQueue
from src.game import Game


class EventQueueTests(unittest.TestCase):
    def test_event_queue_drains_in_order(self):
        events = EventQueue()
        events.push("first", "One")
        events.push("second", "Two")
        drained = events.drain()
        self.assertEqual([event.event_type for event in drained], ["first", "second"])
        self.assertEqual(events.peek_all(), [])


class TurnManagerTests(unittest.TestCase):
    def test_turn_decrements_timer(self):
        game = Game()
        start = game.state.floor_timer
        game.handle_action("i")
        self.assertEqual(game.state.floor_timer, start - 1)

    def test_floor_collapse_requests_quit(self):
        game = Game()
        game.state.floor_timer = 1
        should_quit = game.handle_action("i")
        self.assertTrue(should_quit)
        self.assertIn("floor timer hit zero", game.last_message)


if __name__ == "__main__":
    unittest.main()
