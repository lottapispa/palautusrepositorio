import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        # 16, 99, 90, 98, 124
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

    def test_search(self):
        self.assertIsNotNone(self.stats.search("Kurri"))
        self.assertEqual(self.stats.search("Kurri"), self.stats._players[2])

    def test_search_no_return(self):
        self.assertEqual(self.stats.search("Kuri"), None)
    
    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(self.stats.team("EDM"), [self.stats._players[0], self.stats._players[2], self.stats._players[4]])

    def test_top(self):
        self.assertEqual(self.stats.top(1), [self.stats._players[4]])
        self.assertEqual(self.stats.top(1), [self.stats._players[4]])
        self.assertEqual(self.stats.top(2, SortBy.POINTS), [self.stats._players[4], self.stats._players[1]])
        self.assertEqual(self.stats.top(1, SortBy.GOALS), [self.stats._players[1]])
        self.assertEqual(self.stats.top(1, SortBy.ASSISTS), [self.stats._players[4]])
        

