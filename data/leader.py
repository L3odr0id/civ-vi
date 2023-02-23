from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.game_info import GameInfo

from data.nation import Nation

import itertools

class Leader:

    id_iter = itertools.count()

    def __init__(self, name: str, nation_name: str, is_banned: bool=False):
        self.id: int = next(self.id_iter)
        self.name: str = name
        self.nationName: str = nation_name # TODO: убрать после переработки соединения нации и лидера
        self.nation: Nation | None = None
        self.games_info: List[GameInfo] = []
        self.is_banned = is_banned

    def get_serializable(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        d['nation_name'] = self.nationName
        d['nation_id'] = self.nation.id if self.nation != None else None
        games_info = []
        for game_info in self.games_info:
            games_info.append(game_info.get_serializable())
        d['games_info'] = games_info
        d['games_amount'] = len(self.games_info)
        d['total_wins_amount'] = self.get_wins_count()
        d['solo_wins_amount'] = self.get_solo_wins()
        d['team_wins_amount'] = self.get_team_wins()
        d['win_rate'] = self.get_win_rate()
        d['is_played'] = len(self.games_info) > 0
        d['is_banned'] = self.is_banned
        return d

    def get_team_wins(self):
        return sum(map(lambda x : x.isWin and x.is_played_by_teams, self.games_info))
    
    def get_solo_wins(self):
        return sum(map(lambda x : x.isWin and not x.is_played_by_teams, self.games_info))
    
    def get_wins_count(self):
        return self.get_team_wins() + self.get_solo_wins()
    
    def get_win_rate(self):
        if len(self.games_info) == 0:
            return 0
        return round(self.get_wins_count() / len(self.games_info), 2)
