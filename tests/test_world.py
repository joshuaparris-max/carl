import unittest

from src.data_loader import load_json, load_map
from src.world import GameWorld


class WorldTests(unittest.TestCase):
    def setUp(self):
        self.world = GameWorld(
            load_map("tutorial_guild_map.txt"),
            load_json("characters.json"),
            objects=load_json("objects.json"),
            hazards=load_json("hazards.json"),
        )

    def test_carl_moves_and_donut_follows(self):
        old_carl = (self.world.carl.x, self.world.carl.y)
        moved = self.world.move_carl(1, 0)
        self.assertTrue(moved)
        self.assertEqual((self.world.donut.x, self.world.donut.y), old_carl)

    def test_wall_blocks_movement(self):
        self.world.carl.x = 1
        self.world.carl.y = 1
        self.assertFalse(self.world.move_carl(-1, 0))

    def test_desk_blocks_movement(self):
        self.world.carl.x = 3
        self.world.carl.y = 5
        self.assertFalse(self.world.move_carl(1, 0))

    def test_near_mordecai(self):
        self.world.carl.x = 6
        self.world.carl.y = 5
        self.assertTrue(self.world.near("mordecai"))

    def test_object_blocks_when_configured(self):
        chest = self.world.objects["tutorial_chest"]
        chest.blocks_movement = True
        self.world.carl.x = 7
        self.world.carl.y = 3
        self.assertFalse(self.world.move_entity("carl", 0, -1))

    def test_hazard_lookup(self):
        hazard = self.world.hazard_at(4, 8)
        self.assertIsNotNone(hazard)
        self.assertEqual(hazard.effect, "donut_complaint")


if __name__ == "__main__":
    unittest.main()
