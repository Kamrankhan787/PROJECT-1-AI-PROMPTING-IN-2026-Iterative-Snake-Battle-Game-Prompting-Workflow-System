"""
Central state orchestrator coordinating snakes, fruits, collisions, and scores.
"""

from enum import Enum
from typing import List, Optional, Set, Dict, Any
from .snake import Snake, Position, Direction
from .player import PlayerSnake
from .ai_snake import AISnake, AIBehavior
from .fruit import Fruit, FruitSpawner
from .collision import CollisionDetector
from .scoring import ScoreTracker


class GameStatus(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"


class GameState:
    """Complete arena simulation for Snake Battle."""

    def __init__(
        self,
        width: int = 30,
        height: int = 30,
        player_color: str = "#00ff88",
        fruit_color: str = "#ff0055",
        opponent_count: int = 3,
        speed_mode: str = "Normal"
    ):
        self.width = width
        self.height = height
        self.player_color = player_color
        self.fruit_color = fruit_color
        self.opponent_count = max(1, min(4, opponent_count))
        self.speed_mode = speed_mode
        self.status = GameStatus.MENU

        self.collision_detector = CollisionDetector(width, height)
        self.fruit_spawner = FruitSpawner(width, height, fruit_color)
        self.score_tracker = ScoreTracker()
        
        self.player: PlayerSnake = None
        self.opponents: List[AISnake] = []
        self.ticks_elapsed = 0
        self.init_game()

    @property
    def all_snakes(self) -> List[Snake]:
        snakes = []
        if self.player:
            snakes.append(self.player)
        snakes.extend(self.opponents)
        return snakes

    def init_game(self) -> None:
        """Initializes or resets board, snakes, and fruits."""
        self.ticks_elapsed = 0
        self.fruit_spawner.clear()
        self.score_tracker.reset()

        # Initialize Player Snake at bottom-left quadrant heading Right
        self.player = PlayerSnake(
            color=self.player_color,
            initial_positions=[
                Position(6, self.height - 8),
                Position(5, self.height - 8),
                Position(4, self.height - 8),
                Position(3, self.height - 8)
            ],
            initial_direction=Direction.RIGHT
        )

        # AI Configurations
        ai_configs = [
            ("Cyber Viper", "#ff4444", AIBehavior.AGGRESSIVE, Position(self.width - 6, 6), Direction.LEFT),
            ("Neon Cobra", "#00d4ff", AIBehavior.BALANCED, Position(self.width - 6, self.height - 8), Direction.UP),
            ("Ghost Python", "#e056fd", AIBehavior.CAUTIOUS, Position(6, 6), Direction.DOWN),
            ("Solar Basilisk", "#ffbe76", AIBehavior.BALANCED, Position(self.width // 2, 4), Direction.RIGHT)
        ]

        self.opponents = []
        for i in range(self.opponent_count):
            name, color, behavior, start_pos, start_dir = ai_configs[i % len(ai_configs)]
            # Body extends backward from initial direction
            opp_segments = [start_pos]
            rev_dir = Direction.LEFT if start_dir == Direction.RIGHT else (
                Direction.RIGHT if start_dir == Direction.LEFT else (
                    Direction.UP if start_dir == Direction.DOWN else Direction.DOWN
                )
            )
            for step in range(1, 4):
                opp_segments.append(Position(start_pos.x + rev_dir.dx * step, start_pos.y + rev_dir.dy * step))

            ai = AISnake(
                snake_id=f"ai_{i+1}",
                name=name,
                color=color,
                behavior=behavior,
                initial_positions=opp_segments,
                initial_direction=start_dir
            )
            self.opponents.append(ai)

        # Spawn initial fruits
        occupied = self.get_all_occupied_cells()
        for _ in range(5):
            self.fruit_spawner.spawn_random_fruit(occupied, target_count=5)
            occupied = self.get_all_occupied_cells()

        self.status = GameStatus.PLAYING

    def get_all_occupied_cells(self) -> Set[Position]:
        occupied = set()
        for snake in self.all_snakes:
            if snake.is_alive:
                occupied.update(snake.segments)
        return occupied

    def step(self) -> Dict[str, Any]:
        """
        Executes a single game tick:
        1. AI decisions
        2. Snake movements
        3. Collisions detection
        4. Rule 5 Dead Snake -> Fruit conversion
        5. Fruit eating and growth
        6. Game status updates
        """
        if self.status != GameStatus.PLAYING:
            return {"status": self.status.value, "events": []}

        self.ticks_elapsed += 1
        events = []

        # 1. AI decisions
        for ai in self.opponents:
            if ai.is_alive:
                ai.decide_next_direction(self.width, self.height, self.fruit_spawner.fruits, self.all_snakes)

        # 2. Move alive snakes
        for snake in self.all_snakes:
            if snake.is_alive:
                snake.move()

        # 3. Collision detection
        fatal_snakes = self.collision_detector.evaluate_collisions(self.all_snakes)

        # 4. Handle deaths & Rule 5: Dead snake body -> fruit
        for dead_snake in fatal_snakes:
            if dead_snake.is_alive:
                dead_snake.die()
                corpse_positions = dead_snake.convert_to_fruits()
                spawned_count = self.fruit_spawner.spawn_corpse_fruits(corpse_positions, dead_snake.color)
                events.append({
                    "type": "snake_died",
                    "snake_id": dead_snake.snake_id,
                    "name": dead_snake.name,
                    "fruits_spawned": spawned_count
                })

                if not dead_snake.is_ai:
                    self.status = GameStatus.GAME_OVER
                    events.append({"type": "game_over", "reason": "Player perished"})
                else:
                    self.score_tracker.add_elimination_points(50)

        # Check victory if all opponents dead and player alive
        if self.player.is_alive and all(not ai.is_alive for ai in self.opponents):
            self.status = GameStatus.VICTORY
            events.append({"type": "victory", "reason": "All opponents defeated"})

        # 5. Check Fruit Eating
        for snake in self.all_snakes:
            if snake.is_alive:
                fruit = self.fruit_spawner.get_fruit_at(snake.head)
                if fruit:
                    snake.grow(1)
                    self.fruit_spawner.remove_fruit(fruit)
                    if not snake.is_ai:
                        self.score_tracker.add_fruit_points(fruit.points)
                    events.append({
                        "type": "fruit_eaten",
                        "snake_id": snake.snake_id,
                        "fruit_type": fruit.fruit_type.value,
                        "points": fruit.points
                    })

        # 6. Replenish regular fruits if below threshold
        occupied = self.get_all_occupied_cells()
        self.fruit_spawner.spawn_random_fruit(occupied, target_count=4)

        return {
            "status": self.status.value,
            "events": events,
            "score": self.score_tracker.to_dict(),
            "player_length": self.player.length if self.player else 0
        }
