import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_team(self):
        self.assertEqual(self.stats.team("EDM"), [Player("Semenko", "EDM", 4, 12), Player("Kurri", "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)])

    def test_top(self):
        self.assertEqual(self.stats.top(1), [Player("Gretzky", "EDM", 35, 89)])
        self.assertEqual(self.stats.top(2), [Player("Gretzky", "EDM", 35, 89), Player("Lemieux", "PIT", 45, 54)])
