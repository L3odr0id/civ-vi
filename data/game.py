from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.team import Team

import itertools


class Game:

    id_iter = itertools.count()

    def __init__(self, game_number: int, turns: int, end_reason: str, start_date: str, finish_date: str, seconds_per_move: str | None = None):
        self.id = next(self.id_iter) # ID игры
        self.game_number: int = game_number  # Номер игры
        self.teams: List[Team] = []  # Команды
        self.turns: int = turns  # Кол-во ходов
        self.end_reason: str = end_reason  # Причина окончания игры
        self.start_date: str = start_date    # Дата начала игры в формате YYYY-MM-DD
        self.finish_date: str = finish_date  # Дата окончания игры в формате YYYY-MM-DD
        self.seconds_per_move: str | None = seconds_per_move    # Время на ход в секундах

    def print(self):
        print('A game with ' + str(len(self.teams)) + ' teams')
        for team in self.teams:
            team.print()
        print()

    def get_serializable(self):
        res = dict()
        res['id'] = self.id
        res['game_number'] = self.game_number
        teams = []
        for team in self.teams:
            teams.append(team.get_serializable())
        res['teams'] = teams
        res['turns'] = self.turns
        res['end_reason'] = self.end_reason
        res['start_date'] = self.start_date
        res['finish_date'] = self.finish_date
        res['seconds_per_move'] = self.seconds_per_move
        return res

    def player_took_part(self, name: str):
        for team in self.teams:
            for meta_player in team.players:
                if meta_player.player.name == name:
                    return True
        return False

    def is_played_by_teams(self) -> bool:
        """
        Если хотя бы в одной команде более 1 игрока,
        значит партия игралась по командам
        """
        res = False
        for team in self.teams:
            if len(team.players) > 1:
                res = True
        return res
