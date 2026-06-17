import unittest

from src.game import Game


class IntegrationScenarioTests(unittest.TestCase):
    def test_tutorial_chest_to_crafting_flow(self):
        game = Game()
        game.handle_action("i")
        self.assertTrue(game.quests.quests["inspect_inventory"]["completed"])

        game.world.carl.x = 7
        game.world.carl.y = 3
        game.handle_action("o")
        self.assertIn("unstable_powder", game.world.carl.inventory)
        self.assertTrue(game.quests.quests["open_tutorial_chest"]["completed"])

        game.handle_action("c")
        self.assertNotIn("unstable_powder", game.world.carl.inventory)
        self.assertIn("crude_blast_charge", game.world.carl.inventory)
        self.assertTrue(game.quests.quests["craft_first_explosive"]["completed"])
        self.assertIn("crude explosive", game.last_message)

    def test_move_near_mordecai_then_talk(self):
        game = Game()
        game.world.carl.x = 6
        game.world.carl.y = 5
        game.handle_action("t")
        self.assertIn("Mordecai:", game.last_message)

        game.handle_action("t")
        self.assertTrue(game.quests.quests["speak_to_mordecai"]["completed"])


if __name__ == "__main__":
    unittest.main()
