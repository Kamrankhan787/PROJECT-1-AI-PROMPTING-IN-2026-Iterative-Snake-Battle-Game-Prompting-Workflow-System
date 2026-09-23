"""
Scoring and stats tracking for player and AI snakes.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
import time


@dataclass
class ScoreStats:
    current_score: int = 0
    high_score: int = 0
    fruits_eaten: int = 0
    opponents_eliminated: int = 0
    start_time: float = 0.0
    elapsed_seconds: float = 0.0


class ScoreTracker:
    """Manages score calculations, streaks, and best scores."""

    def __init__(self, high_score: int = 0):
        self.stats = ScoreStats(high_score=high_score)
        self.stats.start_time = time.time()

    def reset(self) -> None:
        high = max(self.stats.high_score, self.stats.current_score)
        self.stats = ScoreStats(high_score=high)
        self.stats.start_time = time.time()

    def add_fruit_points(self, points: int = 10) -> int:
        self.stats.current_score += points
        self.stats.fruits_eaten += 1
        if self.stats.current_score > self.stats.high_score:
            self.stats.high_score = self.stats.current_score
        return self.stats.current_score

    def add_elimination_points(self, points: int = 50) -> int:
        self.stats.current_score += points
        self.stats.opponents_eliminated += 1
        if self.stats.current_score > self.stats.high_score:
            self.stats.high_score = self.stats.current_score
        return self.stats.current_score

    def update_time(self) -> float:
        self.stats.elapsed_seconds = round(time.time() - self.stats.start_time, 1)
        return self.stats.elapsed_seconds

    def to_dict(self) -> Dict[str, any]:
        return {
            "score": self.stats.current_score,
            "high_score": self.stats.high_score,
            "fruits_eaten": self.stats.fruits_eaten,
            "eliminations": self.stats.opponents_eliminated,
            "elapsed_seconds": self.update_time()
        }
