"""
AI opponents with distinct tactical behaviors: Balanced, Aggressive, and Cautious.
"""

from enum import Enum
from typing import List, Set, Optional, Dict
from .snake import Snake, Position, Direction
from .fruit import Fruit


class AIBehavior(Enum):
    BALANCED = "Balanced"
    AGGRESSIVE = "Aggressive"
    CAUTIOUS = "Cautious"


class AISnake(Snake):
    """
    Computer-controlled snake that analyzes arena obstacles, targets fruit,
    and moves tactically according to its assigned personality.
    """

    def __init__(
        self,
        snake_id: str,
        name: str,
        color: str,
        behavior: AIBehavior,
        initial_positions: List[Position],
        initial_direction: Direction = Direction.RIGHT
    ):
        super().__init__(
            snake_id=snake_id,
            name=name,
            color=color,
            initial_positions=initial_positions,
            initial_direction=initial_direction,
            is_ai=True
        )
        self.behavior = behavior

    def decide_next_direction(
        self,
        grid_width: int,
        grid_height: int,
        fruits: List[Fruit],
        all_snakes: List[Snake]
    ) -> Direction:
        """
        Evaluates surrounding grid cells and chooses the best safe direction based on AI personality.
        """
        if not self.is_alive:
            return self.direction

        # Build set of dangerous cells (walls + all alive snake bodies)
        dangerous_cells: Set[Position] = set()

        for s in all_snakes:
            if s.is_alive:
                # Include body
                for seg in s.segments:
                    dangerous_cells.add(seg)
                # If opposing snake is alive and not self, candidate head moves should be treated with caution
                if s.snake_id != self.snake_id:
                    for d in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
                        dangerous_cells.add(s.head.translate(d))

        # Do not treat self current head as an obstacle for future steps, but own body is
        dangerous_cells.difference_update({self.head})

        # Check candidate moves
        candidate_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        valid_moves: List[Direction] = []

        for d in candidate_directions:
            # Cannot reverse direction
            if self.direction.is_opposite(d):
                continue
            
            target_pos = self.head.translate(d)

            # Check arena boundaries
            if not (0 <= target_pos.x < grid_width and 0 <= target_pos.y < grid_height):
                continue

            # Check dangerous cells (other snakes + own body)
            if target_pos in self.body:
                continue

            # For other snakes, their body is hard death
            other_bodies = set()
            for s in all_snakes:
                if s.is_alive and s.snake_id != self.snake_id:
                    other_bodies.update(s.segments)
            
            if target_pos in other_bodies:
                continue

            valid_moves.append(d)

        if not valid_moves:
            # Desperation: try any move that doesn't hit a wall
            for d in candidate_directions:
                if not self.direction.is_opposite(d):
                    target_pos = self.head.translate(d)
                    if 0 <= target_pos.x < grid_width and 0 <= target_pos.y < grid_height:
                        self.set_direction(d)
                        return d
            return self.direction

        # Score valid moves
        best_direction = valid_moves[0]
        best_score = -float('inf')

        # Identify nearest fruit
        nearest_fruit: Optional[Fruit] = None
        min_fruit_dist = float('inf')
        for f in fruits:
            dist = self.head.manhattan_distance(f.position)
            if dist < min_fruit_dist:
                min_fruit_dist = dist
                nearest_fruit = f

        # Identify player snake
        player_snake = next((s for s in all_snakes if not s.is_ai and s.is_alive), None)

        for d in valid_moves:
            next_pos = self.head.translate(d)
            score = 0.0

            # 1. Base Fruit Seeking
            if nearest_fruit:
                dist_to_fruit = next_pos.manhattan_distance(nearest_fruit.position)
                score += (100.0 - dist_to_fruit * 2.5)

            # 2. Wall Proximity
            dist_to_wall_x = min(next_pos.x, grid_width - 1 - next_pos.x)
            dist_to_wall_y = min(next_pos.y, grid_height - 1 - next_pos.y)
            wall_margin = min(dist_to_wall_x, dist_to_wall_y)

            # 3. Personality Adjustments
            if self.behavior == AIBehavior.CAUTIOUS:
                # Heavy penalty for low wall margins or near other snakes
                if wall_margin < 2:
                    score -= 50.0
                if any(next_pos.manhattan_distance(s.head) <= 2 for s in all_snakes if s.snake_id != self.snake_id and s.is_alive):
                    score -= 80.0

            elif self.behavior == AIBehavior.AGGRESSIVE:
                # Seek to intercept player or cut off paths
                if player_snake:
                    dist_to_player = next_pos.manhattan_distance(player_snake.head)
                    if self.length >= player_snake.length:
                        # Hunt player
                        score += (60.0 - dist_to_player * 2.0)
                    else:
                        # Avoid if smaller
                        score -= (30.0 - dist_to_player)
                # Prioritize high value corpse fruits
                if nearest_fruit and nearest_fruit.points > 10:
                    score += 40.0

            elif self.behavior == AIBehavior.BALANCED:
                # Moderate avoidance of edges
                if wall_margin < 1:
                    score -= 20.0
                # Focus primarily on nearest fruit efficiently
                score += 10.0

            # 4. Open-space lookahead (1-step forward mobility)
            open_exits = 0
            for test_d in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
                p = next_pos.translate(test_d)
                if (0 <= p.x < grid_width and 0 <= p.y < grid_height) and (p not in self.body):
                    open_exits += 1
            score += open_exits * 15.0

            # Prefer maintaining momentum slightly to avoid jitter
            if d == self.direction:
                score += 5.0

            if score > best_score:
                best_score = score
                best_direction = d

        self.set_direction(best_direction)
        return best_direction
