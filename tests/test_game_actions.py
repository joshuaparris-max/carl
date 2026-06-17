import unittest

from src.game import Game


class GameActionTests(unittest.TestCase):
    def test_inventory_completes_inventory_quest(self):
        game = Game()
        game.handle_action("i")
        self.assertTrue(game.quests.quests["inspect_inventory"]["completed"])

    def test_open_chest_adds_material(self):
        game = Game()
        game.world.carl.x = 7
        game.world.carl.y = 3
        game.handle_action("o")
        self.assertIn("unstable_powder", game.world.carl.inventory)
        self.assertTrue(game.quests.quests["open_tutorial_chest"]["completed"])

    def test_craft_first_explosive(self):
        game = Game()
        game.world.carl.inventory.append("unstable_powder")
        game.handle_action("c")
        self.assertIn("crude_blast_charge", game.world.carl.inventory)
        self.assertTrue(game.quests.quests["craft_first_explosive"]["completed"])


if __name__ == "__main__":
    unittest.main()
