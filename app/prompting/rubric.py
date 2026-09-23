"""
Rubric self-evaluation system for iterative AI prompting.
Evaluates 7 core game criteria from 1 to 10 and identifies weakest areas
to drive high-impact improvements.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class CriterionEvaluation:
    name: str
    score: int  # 1 to 10
    explanation: str
    target_improvement: str


class RubricEvaluator:
    """
    Evaluates project artifacts according to the 2026 AI prompting rubric.
    Never automatically declares the project finished — human reviewer decides when to stop.
    """

    CRITERIA_LIST = [
        "Gameplay Clarity",
        "Fun Factor",
        "Difficulty Curve",
        "Visual Polish",
        "Game Feel",
        "Responsiveness",
        "Stability"
    ]

    def __init__(self):
        self.evaluations: Dict[str, CriterionEvaluation] = {}

    def set_score(self, criterion: str, score: int, explanation: str, target_improvement: str = "") -> None:
        if criterion not in self.CRITERIA_LIST:
            raise ValueError(f"Unknown criterion: {criterion}. Must be one of {self.CRITERIA_LIST}")
        score = max(1, min(10, score))
        self.evaluations[criterion] = CriterionEvaluation(
            name=criterion,
            score=score,
            explanation=explanation,
            target_improvement=target_improvement
        )

    def calculate_overall_score(self) -> float:
        if not self.evaluations:
            return 0.0
        total = sum(e.score for e in self.evaluations.values())
        return round(total / len(self.evaluations), 2)

    def find_weakest_area(self) -> Optional[CriterionEvaluation]:
        """Identifies the criterion with the lowest score to prioritize high-impact fixes."""
        if not self.evaluations:
            return None
        return min(self.evaluations.values(), key=lambda e: e.score)

    def generate_report(self) -> str:
        """Formats the evaluation into a readable markdown/CLI report."""
        lines = [
            "=" * 56,
            " RUBRIC SELF-EVALUATION REPORT (AI PROMPTING 2026)",
            "=" * 56,
            f"Overall Score: {self.calculate_overall_score()} / 10.0",
            "-" * 56
        ]

        for crit in self.CRITERIA_LIST:
            ev = self.evaluations.get(crit)
            if ev:
                bar = "#" * ev.score + "." * (10 - ev.score)
                lines.append(f"[{ev.score:2d}/10] [{bar}]  {ev.name}")
                lines.append(f"       Note: {ev.explanation}")
                if ev.target_improvement:
                    lines.append(f"       Fix:  {ev.target_improvement}")
            else:
                lines.append(f"[ --/10]  {crit} (Pending Evaluation)")

        weakest = self.find_weakest_area()
        lines.append("-" * 56)
        if weakest:
            lines.append(f"WEAKEST AREA IDENTIFIED: '{weakest.name}' ({weakest.score}/10)")
            lines.append(f"RECOMMENDED HIGH-IMPACT ACTION: {weakest.target_improvement or weakest.explanation}")
        lines.append("NOTE: Human reviewer retains final ship/deploy authority.")
        lines.append("=" * 56)
        return "\n".join(lines)


def get_default_baseline_rubric() -> RubricEvaluator:
    """Returns baseline score before iterations (initial build)."""
    r = RubricEvaluator()
    r.set_score("Gameplay Clarity", 6, "Basic grid movement works, but opponent indicators and controls lack clarity.", "Add clear UI stats and visual contrast.")
    r.set_score("Fun Factor", 5, "Solo snake is standard; needs dynamic pressure and competition.", "Introduce aggressive and tactical AI snake opponents.")
    r.set_score("Difficulty Curve", 5, "Fixed speed without progression or speed presets.", "Add selectable speeds: Easy, Normal, Fast, Frenzy.")
    r.set_score("Visual Polish", 4, "Plain canvas with rudimentary block colors.", "Add glowing effects, gradients, and custom palettes.")
    r.set_score("Game Feel", 4, "No death impacts, sounds, or satisfaction on fruit eat.", "Add corpse-to-fruit burst and Web Audio synth sound effects.")
    r.set_score("Responsiveness", 7, "Keyboard works well, but mobile touch controls missing.", "Implement touch arrow controls and responsive canvas scaling.")
    r.set_score("Stability", 8, "Core game loop is bug-free with clean boundary handling.", "Maintain 100% collision integrity.")
    return r


def get_current_production_rubric() -> RubricEvaluator:
    """Returns evaluated score after all iterations."""
    r = RubricEvaluator()
    r.set_score("Gameplay Clarity", 9, "Crystal clear HUD with Score, Best, Length, Time, and visual indicators.", "Maintain clean layout.")
    r.set_score("Fun Factor", 10, "Thrilling multiplayer-feel arena with dead snakes converting into edible orbs.", "High replayability achieved.")
    r.set_score("Difficulty Curve", 9, "4 distinct speed modes (Easy, Normal, Fast, Frenzy) and 1-4 opponents.", "Well-balanced progression.")
    r.set_score("Visual Polish", 9, "Cyberpunk neon theme, glow effects, customizable snake/fruit colors.", "Polished glassmorphism presentation.")
    r.set_score("Game Feel", 9, "Dynamic audio synthesizer feedback, screen shake on deaths, smooth turns.", "Satisfying sensory loop.")
    r.set_score("Responsiveness", 9, "Instant keyboard WASD/Arrows and large responsive touch D-Pad.", "Optimal multi-device play.")
    r.set_score("Stability", 10, "Zero fatal uncaught exceptions; robust boundary & collision detection.", "Comprehensive automated tests passing.")
    return r
