from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    season = input("Select season [2020-21/2021-22/2022-23/2023-24/2024-25/2025-26/2026-27]: ")
    selector = input("Select view type [nationality/team]: ").strip().lower()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    if selector == "nationality":
        nationality = input("Select nationality: ")
        players = stats.top_scorers_by_nationality(nationality)
        title = f"Top scorers of {nationality} season {season}"
    elif selector == "team":
        team = input("Select team: ")
        players = stats.top_scorers_by_team(team)
        title = f"Top scorers of {team} season {season}"
    else:
        raise ValueError("Invalid selection. Choose either 'nationality' or 'team'.")

    console = Console()
    table = Table(title=title)

    table.add_column("name", style="cyan", justify="left")
    table.add_column("team", style="magenta", justify="left")
    table.add_column("goals", style="green", justify="right")
    table.add_column("assists", style="green", justify="right")
    table.add_column("points", style="green", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console.print(table)

if __name__ == "__main__":
    main()
