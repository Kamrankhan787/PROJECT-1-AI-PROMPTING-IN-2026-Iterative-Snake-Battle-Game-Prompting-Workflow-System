"""
Unit tests for collision detector (wall, self, and inter-snake combat fatal collisions).
"""

import unittest
from app.game.collision import CollisionDetector
from app.game.snake import Snake, Position, Direction


class TestCollision(unittest.TestCase):

    def setUp(self):
        self.detector = CollisionDetector(width=20, height=20)

    def test_wall_collision_in_bounds(self):
        self.assertFalse(self.detector.is_wall_collision(Position(0, 0)))
        self.assertFalse(self.detector.is_wall_collision(Position(19, 19)))
        self.assertFalse(self.detector.is_wall_collision(Position(10, 10)))

    def test_wall_collision_out_of_bounds(self):
        self.assertTrue(self.detector.is_wall_collision(Position(-1, 5)))
        self.assertTrue(self.detector.is_wall_collision(Position(20, 5)))
        self.assertTrue(self.detector.is_wall_collision(Position(5, -1)))
        self.assertTrue(self.detector.is_wall_collision(Position(5, 20)))

    def test_self_collision_negative(self):
        snake = Snake(
            "s1", "Snake 1", "#00ff88",
            [Position(5, 5), Position(4, 5), Position(3, 5)]
        )
        self.assertFalse(self.detector.is_self_collision(snake))

    def test_self_collision_positive(self):
        # Snake whose head is on one of its own body segments
        snake = Snake(
            "s1", "Snake 1", "#00ff88",
            [Position(4, 5), Position(5, 5), Position(5, 6), Position(4, 6), Position(4, 5)]
        )
        self.assertTrue(self.detector.is_self_collision(snake))

    def test_snake_to_snake_body_collision(self):
        # Snake A runs head-first into Snake B body
        snake_a = Snake("a", "Snake A", "#00ff88", [Position(5, 5), Position(5, 6)])
        snake_b = Snake("b", "Snake B", "#ff0055", [Position(6, 5), Position(5, 5), Position(4, 5)])

        dead = self.detector.evaluate_collisions([snake_a, snake_b])
        # Snake A head is at (5,5) which is in Snake B's body
        self.assertIn(snake_a, dead)
        self.assertEqual(snake_b.kills, 1)

    def test_head_to_head_collision(self):
        # Both snakes hit each other head-to-head
        snake_a = Snake("a", "Snake A", "#00ff88", [Position(5, 5), Position(4, 5)])
        snake_b = Snake("b", "Snake B", "#ff0055", [Position(5, 5), Position(6, 5)])

        dead = self.detector.evaluate_collisions([snake_a, snake_b])
        self.assertIn(snake_a, dead)
        self.assertIn(snake_b, dead)


if __name__ == "__main__":
    unittest.main()
