from leader import leadersStorage
from players_storage import playerStorage
from team import Team


def get_history():
    games = [
        get_game_1(),
        get_game_2(),
        get_game_3(),
        get_game_4(),
        get_game_5(),
        get_game_6(),
        get_game_7(),
        get_game_8(),
    ]
    return games


def get_games_serializable(games: list):
    d = dict()
    for game in games:
        d[game.index] = game.get_serializable()
    return d


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


# Игроки
_George_Best_7 = playerStorage.player('George_Best_7')
_Leodroid = playerStorage.player('Leodroid')
_Veldy = playerStorage.player('Veldy')
_Neodim = playerStorage.player('Neodim')
_SaltySoup = playerStorage.player('SaltySoup')
_The_Losst = playerStorage.player('The_Losst')
_MaxBelol = playerStorage.player('MaxBelol')
_TinyClayMan = playerStorage.player('TinyClayMan')
_TheDavidGame = playerStorage.player('TheDavidGame')
_Ortreke = playerStorage.player('Ortreke')
_Cvytik = playerStorage.player('Cvytik')
_StillWiseOut = playerStorage.player('StillWiseOut')
_Kris = playerStorage.player('Kris')
_Losyashboi = playerStorage.player('Losyashboi')

# Лидеры
_Friedrich_Barbarossa = leadersStorage.leader(46)
_Trayan = leadersStorage.leader(42)
_Peter_the_Great = leadersStorage.leader(28)
_Mansa_Musa = leadersStorage.leader(23)  # Мали
_Hojo_Tokimune = leadersStorage.leader(49)
_Rusvelt_Progressive = leadersStorage.leader(39)
_Pedru_II = leadersStorage.leader(31)  # Бразилия
_Chaka = leadersStorage.leader(53)  # Зулусы
_Yadviga = leadersStorage.leader(57)  # Польша
_Cleopatra = leadersStorage.leader(18)
_Rusvelt_Vsadnik = leadersStorage.leader(40)
_Amanitore = leadersStorage.leader(3)  # Нубия
_Alieanora_England = leadersStorage.leader(1)
_Gilgamesh = leadersStorage.leader(9)  # Шумеры
_Vasilii_II = leadersStorage.leader(5)
_Chingishan = leadersStorage.leader(55)  # Монголия
_Pochatok = leadersStorage.leader(30)  # Инки
_Perikl = leadersStorage.leader(32)  # Греция
_Saladin = leadersStorage.leader(34)  # Аравия
_Ekatetina_Medichi_Velikolepnaya = leadersStorage.leader(14)  # Франция
_Robert_Brus = leadersStorage.leader(33)  # Шотландия
_Ambiotriks = leadersStorage.leader(4)  # Галлия
_Hubilai_Mongol = leadersStorage.leader(50)  # Монголия
_Vilgelmina = leadersStorage.leader(7)  # Нидерланды
_Wilfried_Lorie = leadersStorage.leader(44)
_Simon_Bolivar = leadersStorage.leader(35)
_viktoria = leadersStorage.leader(6)
_Montesuma = leadersStorage.leader(27)
_Didona = leadersStorage.leader(13)
_Ish_vak = leadersStorage.leader(16)
_Hammurapi = leadersStorage.leader(47)
_Matiash_I = leadersStorage.leader(24)
_Kristina_I = leadersStorage.leader(20)
_Tamara = leadersStorage.leader(38)
_Tin_Huan = leadersStorage.leader(52)
_Chieu_Vietnam = leadersStorage.leader(56)
_Juan_III = leadersStorage.leader(15)


def get_game_1():
    game = Game(index=1, turns=144, end='Суп ушёл варить пельмени')

    team1 = Team()
    team1.add_player(_George_Best_7, _Friedrich_Barbarossa)
    team1.add_player(_Leodroid, _Trayan)
    team1.add_player(_Veldy, _Peter_the_Great)

    team2 = Team()
    team2.add_player(_Neodim, _Mansa_Musa)
    team2.add_player(_SaltySoup, _Hojo_Tokimune)
    team2.add_player(_The_Losst, _Rusvelt_Progressive)

    game.teams.append(team1)
    game.teams.append(team2)

    return game


def get_game_2():
    game = Game(index=2, turns=148, end='Культурная')
    team1 = Team()
    team1.add_player(_George_Best_7, _Pedru_II)
    team2 = Team()
    team2.add_player(_Neodim, _Peter_the_Great)
    team3 = Team()
    team3.add_player(_Leodroid, _Chaka)
    team4 = Team()
    team4.add_player(_MaxBelol, _Yadviga)

    game.teams.append(team1)
    game.teams.append(team2)
    game.teams.append(team3)
    game.teams.append(team4)

    return game


def get_game_3():
    game = Game(index=3, turns=236, end='Дипломатическая')
    team0 = Team()
    team0.add_player(_George_Best_7, _Rusvelt_Vsadnik)
    team1 = Team()
    team1.add_player(_Leodroid, _Cleopatra)
    team2 = Team()
    team2.add_player(_TheDavidGame, _Amanitore)
    team3 = Team()
    team3.add_player(_TinyClayMan, _Alieanora_England)
    team4 = Team()
    team4.add_player(_Neodim, _Peter_the_Great)
    team5 = Team()
    team5.add_player(_The_Losst, _Gilgamesh)

    game.teams = [team0, team1, team2, team3, team4, team5]
    return game


def get_game_4():
    game = Game(index=4, turns=215, end='Религиозная')
    team0 = Team()
    team0.add_player(_Ortreke, _Pochatok)
    team1 = Team()
    team1.add_player(_Neodim, _Vasilii_II)
    team2 = Team()
    team2.add_player(_Leodroid, _Chingishan)
    team3 = Team()
    team3.add_player(_Cvytik, _Perikl)
    team4 = Team()
    team4.add_player(_TinyClayMan, _Saladin)
    team5 = Team()
    team5.add_player(_George_Best_7, _Ekatetina_Medichi_Velikolepnaya)

    game.teams = [team0, team1, team2, team3, team4, team5]
    return game


def get_game_5():
    game = Game(index=5, turns=192, end='Религиозная')
    team0 = Team()
    team0.add_player(_George_Best_7, _Yadviga)
    team0.add_player(_MaxBelol, _Robert_Brus)
    team0.add_player(_Neodim, _Peter_the_Great)

    team1 = Team()
    team1.add_player(_Leodroid, _Ambiotriks)
    team1.add_player(_TinyClayMan, _Hubilai_Mongol)

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_game_6():
    game = Game(index=6, turns=182, end='Дипломатическая')
    team0 = Team()
    team0.add_player(_Neodim, _Peter_the_Great)
    team0.add_player(_Ortreke, _Montesuma)
    team0.add_player(_SaltySoup, _Friedrich_Barbarossa)
    team0.add_player(_StillWiseOut, _Didona)
    team0.add_player(_The_Losst, _Ish_vak)

    team1 = Team()
    team1.add_player(_Cvytik, _Vilgelmina)
    team1.add_player(_George_Best_7, _Wilfried_Lorie)
    team1.add_player(_Leodroid, _Hojo_Tokimune)
    team1.add_player(_MaxBelol, _Simon_Bolivar)
    team1.add_player(_TinyClayMan, _viktoria)

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_game_7():
    game = Game(index=7, turns=241, end='Дипломатическая')
    team0 = Team()
    team0.add_player(_George_Best_7, _Hammurapi)
    team1 = Team()
    team1.add_player(_Neodim, _Peter_the_Great)
    team2 = Team()
    team2.add_player(_TinyClayMan, _Matiash_I)
    team3 = Team()
    team3.add_player(_MaxBelol, _Kristina_I)
    team4 = Team()
    team4.add_player(_Leodroid, _Tamara)
    team5 = Team()
    team5.add_player(_Kris, _Friedrich_Barbarossa)
    team6 = Team()
    team6.add_player(_Losyashboi, _Ish_vak)

    game.teams = [team0, team1, team2, team3, team4, team5, team6]
    return game


def get_game_8():
    game = Game(index=8, turns=220, end='Дипломатическая')
    team0 = Team()
    team0.add_player(_George_Best_7, _Tin_Huan)
    team1 = Team()
    team1.add_player(_Leodroid, _Chieu_Vietnam)
    team2 = Team()
    team2.add_player(_Losyashboi, _Hojo_Tokimune)
    team3 = Team()
    team3.add_player(_TinyClayMan, _Juan_III)

    game.teams = [team0, team1, team2, team3, ]
    return game
