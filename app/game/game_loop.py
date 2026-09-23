"""
Headless game loop simulation for testing, validation, and CLI demonstrations.
"""

from typing import Dict, Any, List
from .game_state import GameState, GameStatus


class GameLoop:
    """Provides stepped or continuous simulation of the Snake Battle arena."""

    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def run_ticks(self, max_ticks: int = 100) -> Dict[str, Any]:
        """Runs the game for max_ticks or until game over / victory."""
        history: List[Dict[str, Any]] = []

        for tick in range(max_ticks):
            if self.game_state.status not in (GameStatus.PLAYING, GameStatus.MENU):
                break
            tick_result = self.game_state.step()
            history.append({
                "tick": tick + 1,
                "result": tick_result
            })

        return {
            "total_ticks": len(history),
            "final_status": self.game_state.status.value,
            "final_score": self.game_state.score_tracker.to_dict(),
            "history": history
        }
