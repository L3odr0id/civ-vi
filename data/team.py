from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.leader import Leader
    from data.player import Player

from data.meta_player import MetaPlayer

class Team:
    def __init__(self):
        self.players: List[MetaPlayer] = []

    def print(self):
        print('A team with ' + str(len(self.players)) + ' players:')
        for i in range(len(self.players)):
            print(str(i + 1) + ' ' + self.players[i].player.name + ' ' + self.players[i].leader.name + '(' +
                  self.players[i].leader.nationName + ')')

    def add_player(self, p: Player, n: Leader):
        self.players.append(MetaPlayer(p, n))

    def get_average_rating(self):
        sum_of_ratings = 0
        for player in self.players:
            sum_of_ratings += player.player.rating
        return sum_of_ratings / len(self.players)

    def get_serializable(self):
        res = []
        for meta in self.players:
            res.append(meta.get_serializable())
        return res

    def get_players(self):
        return self.players
