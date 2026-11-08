from player_reader import PlayerReader
from player_stats import PlayerStats

url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
stats = PlayerStats(PlayerReader(url))

# Oletetaan, että agentti nimesi metodin top_scorers_by_team
for p in stats.top_scorers_by_team("DAL"):
    print(p)
