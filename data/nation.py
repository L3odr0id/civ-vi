from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.leader import Leader
    from data.game_info import GameInfo

import itertools

class Nation:

    id_iter = itertools.count()

    def __init__(self, name: str):
        self.id: int = next(self.id_iter)
        self.name: str = name
        self.games_info: List[GameInfo] = []
        self.leaders: List[Leader] = []

    def add_leader(self, leader: Leader):
        self.leaders.append(leader)

    def get_serializable(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        games_info = []
        for game_info in self.games_info:
            games_info.append(game_info.get_serializable())
        d['games_info'] = games_info
        return d
    
    def get_team_wins(self):
        return sum(map(lambda x : x.isWin and x.is_played_by_teams(), self.games_info))
    
    def get_solo_wins(self):
        return sum(map(lambda x : x.isWin and not x.is_played_by_teams(), self.games_info))
    
    def get_wins_count(self):
        return self.get_team_wins() + self.get_solo_wins()
