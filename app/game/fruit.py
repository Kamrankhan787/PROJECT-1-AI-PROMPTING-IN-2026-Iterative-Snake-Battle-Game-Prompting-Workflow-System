"""
Fruit entities and spawning mechanics.
"""

import random
from dataclasses import dataclass
from enum import Enum
from typing import List, Set, Optional
from .snake import Position


class FruitType(Enum):
    REGULAR = "regular"
    SNAKE_CORPSE = "snake_corpse"
    GOLDEN = "golden"


@dataclass
class Fruit:
    position: Position
    fruit_type: FruitType = FruitType.REGULAR
    points: int = 10
    color: str = "#ff0055"

    @classmethod
    def create_regular(cls, pos: Position, color: str = "#ff0055") -> 'Fruit':
        return cls(position=pos, fruit_type=FruitType.REGULAR, points=10, color=color)

    @classmethod
    def create_corpse_fruit(cls, pos: Position, original_color: str = "#ffd700") -> 'Fruit':
        return cls(position=pos, fruit_type=FruitType.SNAKE_CORPSE, points=15, color=original_color)

    @classmethod
    def create_golden(cls, pos: Position) -> 'Fruit':
        return cls(position=pos, fruit_type=FruitType.GOLDEN, points=30, color="#ffd700")


class FruitSpawner:
    """Manages fruit population on the grid ensuring no overlap with active snakes."""

    def __init__(self, width: int = 30, height: int = 30, default_color: str = "#ff0055"):
        self.width = width
        self.height = height
        self.default_color = default_color
        self.fruits: List[Fruit] = []

    def clear(self) -> None:
        self.fruits.clear()

    def get_fruit_at(self, position: Position) -> Optional[Fruit]:
        for fruit in self.fruits:
            if fruit.position == position:
                return fruit
        return None

    def remove_fruit(self, fruit: Fruit) -> None:
        if fruit in self.fruits:
            self.fruits.remove(fruit)

    def add_fruit(self, fruit: Fruit) -> None:
        self.fruits.append(fruit)

    def spawn_corpse_fruits(self, positions: List[Position], color: str = "#ffd700") -> int:
        """Spawns corpse fruits when a snake dies (Rule 5)."""
        count = 0
        existing_positions = {f.position for f in self.fruits}
        for pos in positions:
            if pos not in existing_positions and 0 <= pos.x < self.width and 0 <= pos.y < self.height:
                self.fruits.append(Fruit.create_corpse_fruit(pos, color))
                existing_positions.add(pos)
                count += 1
        return count

    def spawn_random_fruit(self, occupied_positions: Set[Position], target_count: int = 3) -> Optional[Fruit]:
        """Spawns fruit if current fruit count is below target_count."""
        if len(self.fruits) >= target_count:
            return None

        all_occupied = occupied_positions.union({f.position for f in self.fruits})
        available = []
        for x in range(self.width):
            for y in range(self.height):
                pos = Position(x, y)
                if pos not in all_occupied:
                    available.append(pos)

        if not available:
            return None

        chosen_pos = random.choice(available)
        new_fruit = Fruit.create_regular(chosen_pos, self.default_color)
        self.fruits.append(new_fruit)
        return new_fruit
