"""
Unit tests for prompting workflow, rubric evaluation, iteration history, and prompt manager.
"""

import unittest
from pathlib import Path
from app.prompting.rubric import RubricEvaluator, get_default_baseline_rubric, get_current_production_rubric
from app.prompting.iteration import IterationHistory
from app.prompting.feedback import FeedbackCollector
from app.prompting.prompt_manager import PromptManager
from app.game.game_state import GameState, GameStatus


class TestPromptingWorkflow(unittest.TestCase):

    def setUp(self):
        self.rubric = RubricEvaluator()

    def test_rubric_evaluation_calculation(self):
        self.rubric.set_score("Gameplay Clarity", 8, "Very clear")
        self.rubric.set_score("Fun Factor", 6, "Good")
        self.rubric.set_score("Visual Polish", 4, "Needs glow")
        
        overall = self.rubric.calculate_overall_score()
        self.assertEqual(overall, 6.0)

        weakest = self.rubric.find_weakest_area()
        self.assertIsNotNone(weakest)
        self.assertEqual(weakest.name, "Visual Polish")
        self.assertEqual(weakest.score, 4)

    def test_baseline_and_production_rubrics(self):
        baseline = get_default_baseline_rubric()
        production = get_current_production_rubric()
        
        self.assertGreater(production.calculate_overall_score(), baseline.calculate_overall_score())
        self.assertEqual(len(production.evaluations), 7)
        self.assertEqual(len(baseline.evaluations), 7)

    def test_iteration_history(self):
        history = IterationHistory()
        self.assertGreaterEqual(len(history.iterations), 4)
        summary = history.get_summary()
        self.assertIn("Iteration #1", summary)
        self.assertIn("Iteration #4", summary)

    def test_feedback_collector(self):
        collector = FeedbackCollector()
        self.assertGreaterEqual(len(collector.items), 4)
        self.assertTrue(all(item.resolved for item in collector.items))

    def test_prompt_manager_loads_all_six_prompts(self):
        pm = PromptManager()
        prompts = pm.list_prompts()
        self.assertEqual(len(prompts), 6)
        
        # Verify each prompt file actually exists and contains content
        for p in prompts:
            self.assertTrue(p["exists"], f"Prompt file {p['filename']} missing!")
            content = pm.get_prompt_content(p["filename"])
            self.assertGreater(len(content.strip()), 20)

        # Check prompt 1 phrase
        p1 = pm.get_prompt_content("01_initial_prompt.md")
        self.assertIn("Let's build and play a game where a snake eats fruit balls to grow", p1)

        # Check prompt 3 phrase
        p3 = pm.get_prompt_content("03_battle_prompt.md")
        self.assertIn("Now make it a battle", p3)
        self.assertIn("when a snake dies its body turns into fruit", p3)

    def test_game_state_headless_step(self):
        gs = GameState(width=20, height=20, opponent_count=2)
        self.assertEqual(gs.status, GameStatus.PLAYING)
        self.assertEqual(len(gs.opponents), 2)
        self.assertIsNotNone(gs.player)
        
        # Advance 10 ticks
        for _ in range(10):
            res = gs.step()
            self.assertIn(res["status"], ["playing", "game_over", "victory"])


if __name__ == "__main__":
    unittest.main()
