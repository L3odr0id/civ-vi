class Team:
    def __init__(self):
        self.players = []

    def print(self):
        print('A team with ' + str(len(self.players)) + ' players:')
        for i in range(1, len(self.players) + 1):
            print(str(i) + ' ' + self.players[i - 1].name)

    def get_average_rating(self):
        sum_of_ratings = 0
        for player in self.players:
            sum_of_ratings += player.rating
        return sum_of_ratings / len(self.players)

    def get_serializable(self):
        res = []
        for player in self.players:
            res.append(player.name)
        return res
