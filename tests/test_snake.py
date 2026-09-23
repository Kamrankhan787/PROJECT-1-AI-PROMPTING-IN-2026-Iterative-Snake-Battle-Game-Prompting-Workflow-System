"""
Unit tests for Snake movement, direction handling, growth, and dead-snake fruit conversion (Rule 5).
"""

import unittest
from app.game.snake import Snake, Direction, Position
from app.game.player import PlayerSnake
from app.game.ai_snake import AISnake, AIBehavior
from app.game.fruit import Fruit


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.initial_positions = [
            Position(5, 5),
            Position(4, 5),
            Position(3, 5),
            Position(2, 5)
        ]
        self.snake = Snake(
            snake_id="test_snake",
            name="Tester",
            color="#00ff88",
            initial_positions=self.initial_positions,
            initial_direction=Direction.RIGHT
        )

    def test_snake_initialization(self):
        self.assertEqual(self.snake.head, Position(5, 5))
        self.assertEqual(self.snake.length, 4)
        self.assertTrue(self.snake.is_alive)
        self.assertEqual(len(self.snake.body), 3)

    def test_snake_movement(self):
        new_head = self.snake.move()
        self.assertEqual(new_head, Position(6, 5))
        self.assertEqual(self.snake.head, Position(6, 5))
        self.assertEqual(self.snake.length, 4)
        self.assertEqual(self.snake.segments[1], Position(5, 5))
        self.assertEqual(self.snake.segments[-1], Position(3, 5))

    def test_snake_growth(self):
        self.snake.grow(1)
        self.assertEqual(self.snake.pending_growth, 1)
        self.snake.move()
        self.assertEqual(self.snake.length, 5)
        self.assertEqual(self.snake.pending_growth, 0)
        # Next move without growth should maintain length 5
        self.snake.move()
        self.assertEqual(self.snake.length, 5)

    def test_direction_change_valid(self):
        self.assertTrue(self.snake.set_direction(Direction.UP))
        self.snake.move()
        self.assertEqual(self.snake.head, Position(5, 4))

    def test_direction_change_prevent_opposite(self):
        # Snake is moving RIGHT; moving LEFT should be rejected
        self.assertFalse(self.snake.set_direction(Direction.LEFT))
        self.snake.move()
        self.assertEqual(self.snake.head, Position(6, 5))

    def test_rule_5_dead_snake_converts_to_fruit(self):
        """Rule 5: When a snake dies, its body segments convert into fruit."""
        self.snake.die()
        self.assertFalse(self.snake.is_alive)
        fruit_positions = self.snake.convert_to_fruits()
        self.assertEqual(len(fruit_positions), 4)
        self.assertIn(Position(5, 5), fruit_positions)
        self.assertIn(Position(4, 5), fruit_positions)
        self.assertIn(Position(3, 5), fruit_positions)
        self.assertIn(Position(2, 5), fruit_positions)
        # Snake segments should be emptied after conversion
        self.assertEqual(len(self.snake.segments), 0)

    def test_player_snake_input(self):
        player = PlayerSnake()
        self.assertTrue(player.handle_input("UP"))
        player.move()
        self.assertEqual(player.direction, Direction.UP)

    def test_ai_snake_decision_making(self):
        ai = AISnake(
            snake_id="ai_test",
            name="Viper",
            color="#ff0055",
            behavior=AIBehavior.BALANCED,
            initial_positions=[Position(10, 10), Position(9, 10), Position(8, 10)],
            initial_direction=Direction.RIGHT
        )
        fruits = [Fruit.create_regular(Position(12, 10))]
        next_dir = ai.decide_next_direction(30, 30, fruits, [ai])
        self.assertIn(next_dir, [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])
        # Since fruit is directly to the right, balanced AI should favor continuing RIGHT
        self.assertEqual(next_dir, Direction.RIGHT)


if __name__ == "__main__":
    unittest.main()
