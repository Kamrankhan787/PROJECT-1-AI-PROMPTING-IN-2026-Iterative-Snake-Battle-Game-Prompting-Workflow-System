"""
Unit tests for Fruit spawner, fruit types, corpse conversion, and board population.
"""

import unittest
from app.game.fruit import Fruit, FruitType, FruitSpawner
from app.game.snake import Position


class TestFruit(unittest.TestCase):

    def setUp(self):
        self.spawner = FruitSpawner(width=10, height=10, default_color="#ff0055")

    def test_create_regular_fruit(self):
        pos = Position(3, 4)
        fruit = Fruit.create_regular(pos, "#ff0055")
        self.assertEqual(fruit.position, pos)
        self.assertEqual(fruit.fruit_type, FruitType.REGULAR)
        self.assertEqual(fruit.points, 10)
        self.assertEqual(fruit.color, "#ff0055")

    def test_create_corpse_fruit(self):
        pos = Position(7, 8)
        fruit = Fruit.create_corpse_fruit(pos, "#00d4ff")
        self.assertEqual(fruit.position, pos)
        self.assertEqual(fruit.fruit_type, FruitType.SNAKE_CORPSE)
        self.assertEqual(fruit.points, 15)
        self.assertEqual(fruit.color, "#00d4ff")

    def test_spawn_random_fruit(self):
        occupied = {Position(0, 0), Position(1, 1)}
        spawned = self.spawner.spawn_random_fruit(occupied, target_count=3)
        self.assertIsNotNone(spawned)
        self.assertEqual(len(self.spawner.fruits), 1)
        self.assertNotIn(spawned.position, occupied)

    def test_spawn_limit(self):
        occupied = set()
        for _ in range(5):
            self.spawner.spawn_random_fruit(occupied, target_count=3)
        # Should not exceed target count of 3
        self.assertEqual(len(self.spawner.fruits), 3)

    def test_spawn_corpse_fruits_rule_5(self):
        """Rule 5: When snake dies, its segments become fruit for others to eat."""
        corpse_positions = [Position(2, 2), Position(2, 3), Position(2, 4)]
        count = self.spawner.spawn_corpse_fruits(corpse_positions, color="#ffd700")
        self.assertEqual(count, 3)
        self.assertEqual(len(self.spawner.fruits), 3)
        for pos in corpse_positions:
            fruit = self.spawner.get_fruit_at(pos)
            self.assertIsNotNone(fruit)
            self.assertEqual(fruit.fruit_type, FruitType.SNAKE_CORPSE)
            self.assertEqual(fruit.points, 15)

    def test_remove_fruit(self):
        fruit = Fruit.create_regular(Position(5, 5))
        self.spawner.add_fruit(fruit)
        self.assertEqual(len(self.spawner.fruits), 1)
        self.spawner.remove_fruit(fruit)
        self.assertEqual(len(self.spawner.fruits), 0)


if __name__ == "__main__":
    unittest.main()
