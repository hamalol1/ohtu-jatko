import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from player import Player
from player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({"name": "A", "nationality": "FIN", "team": "TBL", "goals": 25, "assists": 40}),
            Player({"name": "B", "nationality": "USA", "team": "TBL", "goals": 30, "assists": 20}),
            Player({"name": "C", "nationality": "FIN", "team": "DAL", "goals": 35, "assists": 10}),
            Player({"name": "D", "nationality": "SWE", "team": "TOR", "goals": 12, "assists": 28}),
        ]
        self.stats = PlayerStats(StubReader(self.players))

    def test_top_scorers_by_nationality_returns_matching_players_sorted_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in result], ["A", "C"])
        self.assertEqual(result[0].points, 65)
        self.assertEqual(result[1].points, 45)

    def test_top_scorers_by_nationality_ignores_other_nationalities(self):
        result = self.stats.top_scorers_by_nationality("USA")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "B")

    def test_top_scorers_by_team_returns_matching_players_sorted_by_points(self):
        result = self.stats.top_scorers_by_team("TBL")

        self.assertEqual([player.name for player in result], ["A", "B"])
        self.assertEqual(result[0].points, 65)
        self.assertEqual(result[1].points, 50)

    def test_top_goal_scorers_returns_requested_number_of_players_sorted_by_goals(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["C", "B"])
        self.assertEqual([player.goals for player in result], [35, 30])


if __name__ == "__main__":
    unittest.main()
