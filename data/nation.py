from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.leader import Leader
    from data.game_info import GameInfo


class Nation:
    def __init__(self, id: int, name: str):
        self.id: int = id
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
