import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

# --- Testit search-metodille ---
    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.stats.search("Selänne")
        self.assertIsNone(pelaaja)

    # --- Testit team-metodille ---
    def test_team_palauttaa_oikean_maaran_joukkueen_pelaajia(self):
        edm_pelaajat = self.stats.team("EDM")
        # Stubissa on kolme EDM-pelaajaa: Semenko, Kurri ja Gretzky
        self.assertEqual(len(edm_pelaajat), 3)
        self.assertEqual(edm_pelaajat[0].name, "Semenko")

    # --- Testit top-metodille ---
    def test_top_palauttaa_oikean_maaran_parhaita_pelaajia(self):
        # Metodin sisällä on while i <= how_many, joten arvolla 2 se hakee indeksit 0, 1 ja 2 (yhteensä 3 pelaajaa)
        top_pelaajat = self.stats.top(2)

        self.assertEqual(len(top_pelaajat), 3)
        # Gretzkyn (124 pistettä) tulisi olla listan ykkösenä
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
        # Lemieux'n (99 pistettä) tulisi olla listan kakkosena
        self.assertEqual(top_pelaajat[1].name, "Lemieux")


    def test_top_palauttaa_parhaat_maalintekijat(self):
        # Stubissa eniten maaleja on Lemieux'lla (45), toisena Yzerman (42)
        top_pelaajat = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_pelaajat[0].name, "Lemieux")
        self.assertEqual(top_pelaajat[1].name, "Yzerman")

    def test_top_palauttaa_parhaat_syottajat(self):
        # Stubissa eniten syöttöjä on Gretzkyllä (89), toisena Yzerman (56)
        top_pelaajat = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
        self.assertEqual(top_pelaajat[1].name, "Yzerman")
