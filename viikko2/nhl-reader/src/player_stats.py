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
