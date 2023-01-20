from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.game import Game

class GamesStorage:
    def __init__(self, games: List[Game]):
        self.games: List[Game] = games

    def game(self, id: int):
        for game in self.games:
            if game.id == id:
                return game
        return None

    def get_serializable(self):
        d = dict()
        for game in self.games:
            d[game.id] = game.get_serializable()
        return d
