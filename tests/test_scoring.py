"""
Unit tests for ScoreTracker, eliminations, high score tracking, and time elapsed.
"""

import unittest
from app.game.scoring import ScoreTracker


class TestScoring(unittest.TestCase):

    def setUp(self):
        self.tracker = ScoreTracker(high_score=100)

    def test_initial_state(self):
        self.assertEqual(self.tracker.stats.current_score, 0)
        self.assertEqual(self.tracker.stats.high_score, 100)
        self.assertEqual(self.tracker.stats.fruits_eaten, 0)
        self.assertEqual(self.tracker.stats.opponents_eliminated, 0)

    def test_fruit_points(self):
        new_score = self.tracker.add_fruit_points(10)
        self.assertEqual(new_score, 10)
        self.assertEqual(self.tracker.stats.fruits_eaten, 1)
        self.assertEqual(self.tracker.stats.current_score, 10)
        # High score remains 100 since current < high
        self.assertEqual(self.tracker.stats.high_score, 100)

    def test_high_score_surpassed(self):
        self.tracker.add_fruit_points(120)
        self.assertEqual(self.tracker.stats.current_score, 120)
        self.assertEqual(self.tracker.stats.high_score, 120)

    def test_elimination_points(self):
        self.tracker.add_elimination_points(50)
        self.assertEqual(self.tracker.stats.current_score, 50)
        self.assertEqual(self.tracker.stats.opponents_eliminated, 1)

    def test_reset(self):
        self.tracker.add_fruit_points(150)
        self.tracker.reset()
        self.assertEqual(self.tracker.stats.current_score, 0)
        self.assertEqual(self.tracker.stats.high_score, 150)
        self.assertEqual(self.tracker.stats.fruits_eaten, 0)

    def test_to_dict(self):
        self.tracker.add_fruit_points(20)
        d = self.tracker.to_dict()
        self.assertEqual(d["score"], 20)
        self.assertIn("elapsed_seconds", d)
        self.assertEqual(d["fruits_eaten"], 1)


if __name__ == "__main__":
    unittest.main()
