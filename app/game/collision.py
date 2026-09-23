"""
Collision detection for walls, self-body, and opponent snakes.
"""

from typing import List, Tuple, Set, Optional
from .snake import Snake, Position


class CollisionDetector:
    """Handles all collision queries within the game arena."""

    def __init__(self, width: int = 30, height: int = 30):
        self.width = width
        self.height = height

    def is_wall_collision(self, position: Position) -> bool:
        """Returns True if position is out of grid bounds."""
        return not (0 <= position.x < self.width and 0 <= position.y < self.height)

    def is_self_collision(self, snake: Snake) -> bool:
        """Returns True if snake head collides with any part of its own body."""
        if not snake.is_alive or len(snake.segments) <= 1:
            return False
        return snake.head in snake.body

    def check_snake_body_collision(self, head: Position, target_snake: Snake) -> bool:
        """Checks if a head position collides with target_snake's body or alive head."""
        if not target_snake.is_alive:
            return False
        return head in target_snake.segments

    def evaluate_collisions(self, snakes: List[Snake]) -> List[Snake]:
        """
        Evaluates all active snakes and returns the list of snakes that suffered
        fatal collisions in this tick.
        """
        dead_this_tick: List[Snake] = []
        alive_snakes = [s for s in snakes if s.is_alive]

        # 1. Wall collisions and self collisions
        for snake in alive_snakes:
            if self.is_wall_collision(snake.head) or self.is_self_collision(snake):
                if snake not in dead_this_tick:
                    dead_this_tick.append(snake)

        # 2. Inter-snake collisions
        for i, snake_a in enumerate(alive_snakes):
            for j, snake_b in enumerate(alive_snakes):
                if i == j:
                    continue

                # Snake A head hits Snake B body
                if snake_a.head in snake_b.body:
                    if snake_a not in dead_this_tick:
                        dead_this_tick.append(snake_a)
                        snake_b.kills += 1

                # Head to Head collision
                elif snake_a.head == snake_b.head:
                    if snake_a not in dead_this_tick:
                        dead_this_tick.append(snake_a)
                    if snake_b not in dead_this_tick:
                        dead_this_tick.append(snake_b)

        return dead_this_tick
