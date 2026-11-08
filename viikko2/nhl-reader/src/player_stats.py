class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = filter(
            lambda player: player.nationality == nationality,
            self._players
        )

        return sorted(
            players_of_nationality,
            key=lambda player: player.points,
            reverse=True
        )

    def top_scorers_by_team(self, team):
        players_of_team = filter(
            lambda player: player.team == team,
            self._players
        )

        return sorted(
            players_of_team,
            key=lambda player: player.points,
            reverse=True
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(
            self._players,
            key=lambda player: player.goals,
            reverse=True
        )[:how_many]
