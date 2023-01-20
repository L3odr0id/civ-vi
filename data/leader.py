from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.game_info import GameInfo

from data.nation import Nation


class Leader:
    def __init__(self, name: str, nation_name: str, id: int):
        self.name: str = name
        self.nationName: str = nation_name
        self.id: int = id
        self.nation: Nation = Nation(0, '')  # плесйхолдер
        self.games_info: List[GameInfo] = []

    def get_serializable(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        d['nation_name'] = self.nationName
        d['nation_id'] = self.nation.id
        games_info = []
        for game_info in self.games_info:
            games_info.append(game_info.get_serializable())
        d['games_info'] = games_info
        return d
