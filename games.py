from players_storage import PlayersStorage
from team import Team


def get_history(ps: PlayersStorage):
    games = [
        get_game_1(ps),
        get_game_2(ps),
        get_game_3(ps),
        get_game_4(ps),
        get_game_5(ps),
        get_game_6(ps),
    ]
    return games


class Game:
    def __init__(self, index: int, turns: int, end: str):
        self.teams = []  # Команды
        self.index = index  # Номер партии
        self.turns = turns  # Кол-во ходов
        self.end = end  # Причина окончания игры

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

    def player_took_part(self, name: str):
        for team in self.teams:
            for player in team.players:
                if player.name == name:
                    return True
        return False


def get_game_1(ps: PlayersStorage):
    game = Game(index=1, turns=144, end='Суп ушёл варить пельмени')

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


def get_game_2(ps: PlayersStorage):
    game = Game(index=2, turns=148, end='Культурная')
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


def get_game_3(ps: PlayersStorage):
    game = Game(index=3, turns=236, end='Дипломатическая')
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


def get_game_4(ps: PlayersStorage):
    game = Game(index=4, turns=215, end='Религиозная')
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


def get_game_5(ps: PlayersStorage):
    game = Game(index=5, turns=192, end='Религиозная')
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


def get_game_6(ps: PlayersStorage):
    game = Game(index=6, turns=182, end='Дипломатическая')
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
