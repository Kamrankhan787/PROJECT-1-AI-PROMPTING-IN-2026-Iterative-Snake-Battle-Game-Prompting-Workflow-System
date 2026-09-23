"""
Feedback loop processing and playtesting observation tracker.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict


class FeedbackCategory(Enum):
    MECHANICS = "Gameplay Mechanics"
    VISUALS = "Visual Polish"
    AUDIO = "Audio & Game Feel"
    CONTROLS = "Controls & Responsiveness"
    BALANCE = "Difficulty & Balance"


@dataclass
class FeedbackItem:
    feedback_id: str
    category: FeedbackCategory
    observation: str
    proposed_solution: str
    impact_level: str  # High, Medium, Low
    resolved: bool = False


class FeedbackCollector:
    """Collects and prioritizes human tester feedback during playtesting loops."""

    def __init__(self):
        self.items: List[FeedbackItem] = []
        self._seed_default_feedback()

    def add_feedback(self, item: FeedbackItem) -> None:
        self.items.append(item)

    def _seed_default_feedback(self) -> None:
        self.items = [
            FeedbackItem(
                feedback_id="FB-01",
                category=FeedbackCategory.VISUALS,
                observation="Opponent snakes blend into the background or look too similar to player.",
                proposed_solution="Assign distinct high-contrast neon colors and visible name badges to AI snakes.",
                impact_level="High",
                resolved=True
            ),
            FeedbackItem(
                feedback_id="FB-02",
                category=FeedbackCategory.MECHANICS,
                observation="Grid starts with zero or one fruit, creating dull initial 10 seconds.",
                proposed_solution="Instantly pre-populate arena with 5 fruit orbs upon battle start.",
                impact_level="Medium",
                resolved=True
            ),
            FeedbackItem(
                feedback_id="FB-03",
                category=FeedbackCategory.AUDIO,
                observation="Collisions feel abrupt without sensory cues or death animations.",
                proposed_solution="Add particle explosion, screen shake, and synthesized audio frequencies for fatal crashes.",
                impact_level="High",
                resolved=True
            ),
            FeedbackItem(
                feedback_id="FB-04",
                category=FeedbackCategory.CONTROLS,
                observation="Mobile users cannot steer the snake effectively.",
                proposed_solution="Provide large virtual touch directional controls beneath the arena.",
                impact_level="High",
                resolved=True
            )
        ]

    def get_summary(self) -> str:
        lines = [
            "=" * 60,
            " PLAYTESTING FEEDBACK REGISTER",
            "=" * 60
        ]
        for fb in self.items:
            status = "[RESOLVED]" if fb.resolved else "[PENDING]"
            lines.append(f"{fb.feedback_id} {status} ({fb.category.value}) - Impact: {fb.impact_level}")
            lines.append(f"  Observed: {fb.observation}")
            lines.append(f"  Action:   {fb.proposed_solution}")
            lines.append("-" * 60)
        return "\n".join(lines)
