"""
Snake representation and core movement mechanics.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Optional


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def dx(self) -> int:
        return self.value[0]

    @property
    def dy(self) -> int:
        return self.value[1]

    def is_opposite(self, other: 'Direction') -> bool:
        return (self.dx + other.dx == 0) and (self.dy + other.dy == 0)


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def translate(self, direction: Direction) -> 'Position':
        return Position(self.x + direction.dx, self.y + direction.dy)

    def manhattan_distance(self, other: 'Position') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def as_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)


class Snake:
    """Base Snake class handling positions, movement, growth, and body conversion."""
    
    def __init__(
        self,
        snake_id: str,
        name: str,
        color: str,
        initial_positions: List[Position],
        initial_direction: Direction = Direction.RIGHT,
        is_ai: bool = False
    ):
        self.snake_id = snake_id
        self.name = name
        self.color = color
        self.segments: List[Position] = list(initial_positions)
        self.direction = initial_direction
        self.next_direction = initial_direction
        self.pending_growth = 0
        self.is_alive = True
        self.is_ai = is_ai
        self.kills = 0
        self.fruits_eaten = 0

    @property
    def head(self) -> Position:
        if not self.segments:
            raise ValueError(f"Snake {self.name} has no segments.")
        return self.segments[0]

    @property
    def body(self) -> List[Position]:
        return self.segments[1:]

    @property
    def length(self) -> int:
        return len(self.segments)

    def set_direction(self, new_direction: Direction) -> bool:
        """Sets next direction if not directly opposite to current moving direction."""
        if not self.direction.is_opposite(new_direction):
            self.next_direction = new_direction
            return True
        return False

    def grow(self, amount: int = 1) -> None:
        """Queue growth segments for upcoming steps."""
        self.pending_growth += amount
        self.fruits_eaten += 1

    def move(self) -> Position:
        """
        Advances the snake one cell forward according to its next_direction.
        Returns the new head position.
        """
        if not self.is_alive:
            return self.head

        self.direction = self.next_direction
        new_head = self.head.translate(self.direction)
        self.segments.insert(0, new_head)

        if self.pending_growth > 0:
            self.pending_growth -= 1
        else:
            self.segments.pop()

        return new_head

    def die(self) -> None:
        """Marks the snake as dead."""
        self.is_alive = False

    def convert_to_fruits(self) -> List[Position]:
        """
        Rule 5: When a snake dies, its body segments convert into fruit
        so other snakes can eat them.
        """
        if self.is_alive:
            return []
        
        # Return all segment positions as fruit locations
        converted_positions = list(self.segments)
        self.segments = []
        return converted_positions
