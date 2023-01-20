from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.player import Player

class PlayersStorage:
    def __init__(self, players: List[Player] = []):
        self.players: List[Player] = players

    def player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def sort(self):
        self.players.sort()

    def print(self):
        for i in range(len(self.players)):
            print(str(i + 1) + ' ' + str(self.players[i].get_serializable()))

    def get_serializable(self):
        d = dict()
        for player in self.players:
            d[player.id] = player.get_serializable()
        return d
