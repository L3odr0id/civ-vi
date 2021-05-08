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
        res = []
        for p in self.players:
            res.append(p.get_serializable())
        return res
