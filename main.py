import json

INITIAL_RATING = 228
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
]

K = 20


class Player:
    def __init__(self, name: str):
        self.name = name
        self.rating = INITIAL_RATING

    def __lt__(self, other):
        return self.rating > other.rating

    def get_serializable(self):
        d = dict()
        d['name'] = self.name
        d['rating'] = self.rating
        return d


class Team:
    def __init__(self):
        self.players = []

    def print(self):
        print('A team with ' + str(len(self.players)) + ' players:')
        for i in range(1, len(self.players) + 1):
            print(str(i) + ' ' + self.players[i - 1].name)

    def get_average_rating(self):
        sum = 0
        for player in self.players:
            sum += player.rating
        return sum / len(self.players)

    def get_serializable(self):
        res = []
        for player in self.players:
            res.append(player.name)
        return res


class Game:
    def __init__(self, turns:int, end:str):
        self.teams = []
        self.turns = turns
        self.end = end

    def print(self):
        print('A game with ' + str(len(self.teams)) + ' teams')
        for team in self.teams:
            team.print()
        print()

    def get_serializable(self):
        teams = []
        for team in self.teams:
            teams.append(team.get_serializable())
        res = dict()
        res['teams'] = teams
        res['turns'] = self.turns
        res['reason'] = self.end
        return res


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
            print(str(i + 1) + ' ' + self.players[i].name + ' ' + str(self.players[i].rating))

    def get_serializable(self):
        res = []
        for p in self.players:
            res.append(p.get_serializable())
        return res


def get_players():
    res = PlayersStorage()
    for nick in NICKNAMES:
        res.players.append(Player(nick))
    return res


def get_first_game(ps: PlayersStorage):
    game = Game(turns=144, end='Суп ушёл варить пельмени')

    team1 = Team()
    team1.players.append(ps.player('George_Best_7'))
    team1.players.append(ps.player('Leodroid'))
    team1.players.append(ps.player('Veldy'))

    team2 = Team()
    team2.players.append(ps.player('Neodim'))
    team2.players.append(ps.player('SaltySoup'))
    team2.players.append(ps.player('The_Losst'))

    game.teams.append(team1)
    game.teams.append(team2)

    return game


def get_second_game(ps: PlayersStorage):
    game = Game(turns=148, end='Культурная')
    team1 = Team()
    team1.players.append(ps.player('George_Best_7'))
    team2 = Team()
    team2.players.append(ps.player('Neodim'))
    team3 = Team()
    team3.players.append(ps.player('Leodroid'))
    team4 = Team()
    team4.players.append(ps.player('MaxBelol'))

    game.teams.append(team1)
    game.teams.append(team2)
    game.teams.append(team3)
    game.teams.append(team4)

    return game


def get_third_game(ps: PlayersStorage):
    game = Game(turns=236, end='Дипломатическая')
    team0 = Team()
    team0.players.append(ps.player('George_Best_7'))
    team1 = Team()
    team1.players.append(ps.player('Leodroid'))
    team2 = Team()
    team2.players.append(ps.player('TheDavidGame'))
    team3 = Team()
    team3.players.append(ps.player('TinyClayMan'))
    team4 = Team()
    team4.players.append(ps.player('Neodim'))
    team5 = Team()
    team5.players.append(ps.player('The_Losst'))

    game.teams.append(team0)
    game.teams.append(team1)
    game.teams.append(team2)
    game.teams.append(team3)
    game.teams.append(team4)
    game.teams.append(team5)

    return game


def get_fourth_game(ps: PlayersStorage):
    game = Game(turns=215, end='Религиозная')
    team0 = Team()
    team0.players.append(ps.player('Ortreke'))
    team1 = Team()
    team1.players.append(ps.player('Neodim'))
    team2 = Team()
    team2.players.append(ps.player('Leodroid'))
    team3 = Team()
    team3.players.append(ps.player('Cvytik'))
    team4 = Team()
    team4.players.append(ps.player('TinyClayMan'))
    team5 = Team()
    team5.players.append(ps.player('George_Best_7'))

    game.teams.append(team0)
    game.teams.append(team1)
    game.teams.append(team2)
    game.teams.append(team3)
    game.teams.append(team4)
    game.teams.append(team5)

    return game


def get_fifth_game(ps: PlayersStorage):
    game = Game(turns=192, end='Религиозная')
    team0 = Team()
    team0.players.append(ps.player('George_Best_7'))
    team0.players.append(ps.player('MaxBelol'))
    team0.players.append(ps.player('Neodim'))
    team1 = Team()
    team1.players.append(ps.player('Leodroid'))
    team1.players.append(ps.player('TinyClayMan'))

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_sixth_game(ps: PlayersStorage):
    game = Game(turns=182, end='Дипломатическая')
    team0 = Team()
    team0.players.append(ps.player('Neodim'))
    team0.players.append(ps.player('Ortreke'))
    team0.players.append(ps.player('SaltySoup'))
    team0.players.append(ps.player('StillWiseOut'))
    team0.players.append(ps.player('The_Losst'))
    team1 = Team()
    team1.players.append(ps.player('Cvytik'))
    team1.players.append(ps.player('George_Best_7'))
    team1.players.append(ps.player('Leodroid'))
    team1.players.append(ps.player('MaxBelol'))
    team1.players.append(ps.player('TinyClayMan'))

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_history(ps: PlayersStorage):
    games = [
        get_first_game(ps),
        get_second_game(ps),
        get_third_game(ps),
        get_fourth_game(ps),
        get_fifth_game(ps),
        get_sixth_game(ps),
    ]
    return games


def get_elo_change(rating1: int, rating2: int, win: bool):
    ea = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    return K * (int(win) - ea)


def calc_scores(game: Game):
    WIN = True
    LOSE = False
    # Для каждой команды рассчитываем средний рейтинг
    # Затем её выигрыш или проигрыш по отношению ко всем другим и суммируем результат
    # Каждому участнику команды добавляем очки результата

    # Рассчитаем изменения рейтингов для всех игроков
    avgs = []
    for i in range(len(game.teams)):
        our_rating = game.teams[i].get_average_rating()
        sum = 0
        for j in range(len(game.teams)):
            if i > j:
                # мы проигрываем этой команде
                their_rating = game.teams[j].get_average_rating()
                sum += get_elo_change(our_rating, their_rating, LOSE)
            if i < j:
                # мы выигрываем у этой команды
                their_rating = game.teams[j].get_average_rating()
                sum += get_elo_change(our_rating, their_rating, WIN)
        avg = sum / len(game.teams)
        avgs.append(avg)

    # Применим изменения
    for i in range(len(avgs)):
        for player in game.teams[i].players:
            player.rating += avgs[i]
            player.rating = round(player.rating)

    # Немного поднять рейтинг всем
    for i in range(len(avgs)):
        for player in game.teams[i].players:
            player.rating += round(K / 2.5)


def get_games_serializable(games: list):
    res = []
    for game in games:
        res.append(game.get_serializable())
    return res


def main():
    ps = get_players()
    games = get_history(ps)

    ps.print()
    print()

    for i in range(len(games)):
        calc_scores(games[i])
        print('Результаты партии ' + str(i + 1))
        ps.sort()
        ps.print()
        print()

    res_json = dict()
    res_json['users'] = ps.get_serializable()
    res_json['games'] = get_games_serializable(games)
    # data = json.dumps(res_json) - хуйня
    # print(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)
    # for game in games:
    #     game.print()

    # ps.sort()
    # ps.print()


if __name__ == "__main__":
    main()
