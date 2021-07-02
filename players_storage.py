from player import Player

NICKNAMES = [
    'Neodim',
    'George_Best_7',
    'Leodroid',
    'Ortreke',
    'The_Losst',
    'TinyClayMan',
    'SaltySoup',
    'MaxBelol',
    'StillWiseOut',
    'Cvytik',
    'Veldy',
    'TheDavidGame',
    'Kris',
    'Losyashboi'
]


class PlayersStorage:
    def __init__(self):
        self.players = []

    def player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    def sort(self):
        self.players.sort()

    def print(self):
        for i in range(len(self.players)):
            print(str(i + 1) + ' ' + str(self.players[i].get_serializable()))

    def get_serializable(self):
        d = dict()
        for p in self.players:
            d[p.index] = p.get_serializable()
        return d


def _get_players():
    res = PlayersStorage()
    i = 0
    for nick in NICKNAMES:
        res.players.append(Player(i, nick))
        i += 1
    return res


playerStorage = _get_players()
