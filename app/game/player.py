"""
Player-controlled snake representation.
"""

from typing import List
from .snake import Snake, Position, Direction


class PlayerSnake(Snake):
    """The main snake controlled by the human user."""

    def __init__(
        self,
        snake_id: str = "player",
        name: str = "Player",
        color: str = "#00ff88",
        initial_positions: List[Position] = None,
        initial_direction: Direction = Direction.RIGHT
    ):
        if initial_positions is None:
            initial_positions = [
                Position(5, 5),
                Position(4, 5),
                Position(3, 5),
                Position(2, 5)
            ]
        super().__init__(
            snake_id=snake_id,
            name=name,
            color=color,
            initial_positions=initial_positions,
            initial_direction=initial_direction,
            is_ai=False
        )

    def handle_input(self, action: str) -> bool:
        """Processes player directional command ('UP', 'DOWN', 'LEFT', 'RIGHT')."""
        direction_map = {
            "UP": Direction.UP,
            "DOWN": Direction.DOWN,
            "LEFT": Direction.LEFT,
            "RIGHT": Direction.RIGHT,
            "w": Direction.UP,
            "s": Direction.DOWN,
            "a": Direction.LEFT,
            "d": Direction.RIGHT
        }
        target_dir = direction_map.get(action.upper() if len(action) > 1 else action.lower())
        if target_dir:
            return self.set_direction(target_dir)
        return False
