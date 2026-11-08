from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    # Injektoidaan riippuvuudet ketjussa: URL -> Reader -> Stats
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    # Pyydetään tilastopalvelulta valmis lista
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
