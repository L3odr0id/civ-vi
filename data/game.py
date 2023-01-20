from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.team import Team


class Game:
    def __init__(self, id: int, turns: int, end_reason: str):
        self.id: int = id  # Номер партии
        self.teams: List[Team] = []  # Команды
        self.turns: int = turns  # Кол-во ходов
        self.end_reason: str = end_reason  # Причина окончания игры

    def print(self):
        print('A game with ' + str(len(self.teams)) + ' teams')
        for team in self.teams:
            team.print()
        print()

    def get_serializable(self):
        res = dict()
        res['id'] = self.id
        teams = []
        for team in self.teams:
            teams.append(team.get_serializable())
        res['teams'] = teams
        res['turns'] = self.turns
        res['end_reason'] = self.end_reason
        return res

    def player_took_part(self, name: str):
        for team in self.teams:
            for meta_player in team.players:
                if meta_player.player.name == name:
                    return True
        return False
