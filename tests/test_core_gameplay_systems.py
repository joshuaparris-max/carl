import unittest

from src.game import Game
from src.save_system import SAVE_PATH


class CoreGameplaySystemTests(unittest.TestCase):
    def tearDown(self):
        if SAVE_PATH.exists():
            SAVE_PATH.unlink()

    def test_attack_damages_adjacent_enemy(self):
        game = Game()
        game.world.carl.x = 7
        game.world.carl.y = 8
        enemy = game.world.entities["training_goblin"]
        start = enemy.resources.health

        game.handle_action("x")

        self.assertLess(enemy.resources.health, start)
        self.assertIn("hits", game.last_message)

    def test_explosive_item_interacts_with_combat_and_is_consumed(self):
        game = Game()
        game.world.carl.inventory.append("crude_blast_charge")
        game.world.carl.x = 7
        game.world.carl.y = 8

        game.handle_action("u")

        self.assertNotIn("crude_blast_charge", game.world.carl.inventory)
        self.assertIn("explosive problem solving", game.state.viewer.timeline[-1])

    def test_pickup_and_equip_pants(self):
        game = Game()
        game.world.carl.x = 2
        game.world.carl.y = 7

        game.handle_action("p")
        self.assertIn("threadbare_pants", game.world.carl.inventory)

        game.handle_action("e")
        self.assertEqual(game.world.carl.equipment["legs"], "threadbare_pants")
        self.assertGreaterEqual(game.world.carl.resources.armor, 2)

    def test_shop_purchase_adds_item(self):
        game = Game()
        game.world.carl.x = 9
        game.world.carl.y = 8

        game.handle_action("b")

        self.assertIn("stale_healing_bar", game.world.carl.inventory)

    def test_hazard_applies_damage(self):
        game = Game()
        game.world.carl.x = 5
        game.world.carl.y = 8
        start = game.world.carl.resources.health

        game.handle_action("d")

        self.assertLess(game.world.carl.resources.health, start)
        self.assertTrue(game.quests.quests["bad_flooring"]["completed"])

    def test_companion_mode_changes(self):
        game = Game()

        game.handle_action("h")

        self.assertEqual(game.world.donut.state["mode"], "hide")

    def test_save_load_restores_timer_viewer_and_equipment(self):
        game = Game()
        game.world.carl.inventory.append("threadbare_pants")
        game.handle_action("e")
        game.state.viewer.change(8, "test")
        game.handle_action("v")

        game.state.floor_timer = 1
        game.state.viewer.popularity = 0
        game.world.carl.equipment.pop("legs")
        game.handle_action("l")

        self.assertGreater(game.state.floor_timer, 1)
        self.assertEqual(game.state.viewer.popularity, 8)
        self.assertEqual(game.world.carl.equipment["legs"], "threadbare_pants")

    def test_checkpoint_restart_restores_saved_run_state(self):
        game = Game()
        game.handle_action("v")
        old_x = game.world.carl.x
        game.handle_action("d")

        game.handle_action("k")

        self.assertEqual(game.world.carl.x, old_x)


if __name__ == "__main__":
    unittest.main()
