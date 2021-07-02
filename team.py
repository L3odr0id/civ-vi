from leader import Leader
from player import Player


class _MetaPlayer:
    def __init__(self, p: Player, leader: Leader):
        self.player = p
        self.leader = leader

    def get_serializable(self):
        d = dict()
        d['player_id'] = self.player.index
        d['leader_id'] = self.leader.index
        return d


class Team:
    def __init__(self):
        self.__players = []  # list of __MetaPlayer

    def print(self):
        print('A team with ' + str(len(self.__players)) + ' players:')
        for i in range(len(self.__players)):
            print(str(i + 1) + ' ' + self.__players[i].player.name + ' ' + self.__players[i].leader.name + '(' +
                  self.__players[i].leader.nationName + ')')

    def add_player(self, p: Player, n: Leader):
        self.__players.append(_MetaPlayer(p, n))

    def get_average_rating(self):
        sum_of_ratings = 0
        for player in self.__players:
            sum_of_ratings += player.player.rating
        return sum_of_ratings / len(self.__players)

    def get_serializable(self):
        res = []
        for meta in self.__players:
            res.append(meta.get_serializable())
        return res

    def get_players(self):
        return self.__players
