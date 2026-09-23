"""
Project settings and default configurations for Snake Battle and Prompting Workflow.
"""

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class GameSettings:
    """Settings controlling the grid, speeds, and battle mechanics."""
    grid_width: int = 30
    grid_height: int = 30
    cell_size: int = 20
    default_player_color: str = "#00ff88"
    default_fruit_color: str = "#ff0055"
    default_opponents: int = 3
    max_opponents: int = 4
    min_opponents: int = 1
    
    # Tick rates in milliseconds for different difficulties
    speed_presets: Dict[str, int] = None
    
    # Score rewards
    points_per_fruit: int = 10
    points_per_elimination: int = 50
    initial_snake_length: int = 4
    
    def __post_init__(self):
        if self.speed_presets is None:
            self.speed_presets = {
                "Easy": 150,
                "Normal": 110,
                "Fast": 80,
                "Frenzy": 50
            }


class Settings:
    """Global system configuration."""
    PROJECT_NAME: str = "PROJECT 1 - AI Prompting in 2026"
    PROJECT_SUBTITLE: str = "Iterative Snake Battle Game + Prompting Workflow System"
    VERSION: str = "1.0.0"
    
    # Paths relative to project root
    PROMPTS_DIR: str = "prompts"
    WORKFLOW_DIR: str = "workflow"
    EVIDENCE_DIR: str = "evidence"
    WEB_DIR: str = "web"
    TESTS_DIR: str = "tests"
    ASSETS_DIR: str = "assets"
    
    game: GameSettings = GameSettings()
