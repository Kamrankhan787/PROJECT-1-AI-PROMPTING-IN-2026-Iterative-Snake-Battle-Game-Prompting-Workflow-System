"""
Snake game engine core logic, state management, and AI behaviors.
"""

from .snake import Snake, Direction, Position
from .fruit import Fruit, FruitType
from .collision import CollisionDetector
from .scoring import ScoreTracker
from .player import PlayerSnake
from .ai_snake import AISnake, AIBehavior
from .game_state import GameState
from .game_loop import GameLoop

__all__ = [
    "Snake",
    "Direction",
    "Position",
    "Fruit",
    "FruitType",
    "CollisionDetector",
    "ScoreTracker",
    "PlayerSnake",
    "AISnake",
    "AIBehavior",
    "GameState",
    "GameLoop"
]
