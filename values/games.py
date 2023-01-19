from data.game import Game
from data.team import Team

from storage.games_storage import GamesStorage

import values.players as players
import values.leaders as leaders


def get_game_1():
    game = Game(id=1, turns=144, end='Суп ушёл варить пельмени')

    team1 = Team()
    team1.add_player(players._George_Best_7, leaders._Friedrich_Barbarossa)
    team1.add_player(players._Leodroid, leaders._Trayan)
    team1.add_player(players._Veldy, leaders._Peter_the_Great)

    team2 = Team()
    team2.add_player(players._Neodim, leaders._Mansa_Musa)
    team2.add_player(players._SaltySoup, leaders._Hojo_Tokimune)
    team2.add_player(players._The_Losst, leaders._Rusvelt_Progressive)

    game.teams.append(team1)
    game.teams.append(team2)

    return game


def get_game_2():
    game = Game(id=2, turns=148, end='Культурная')
    team1 = Team()
    team1.add_player(players._George_Best_7, leaders._Pedru_II)
    team2 = Team()
    team2.add_player(players._Neodim, leaders._Peter_the_Great)
    team3 = Team()
    team3.add_player(players._Leodroid, leaders._Chaka)
    team4 = Team()
    team4.add_player(players._MaxBelol, leaders._Yadviga)

    game.teams.append(team1)
    game.teams.append(team2)
    game.teams.append(team3)
    game.teams.append(team4)

    return game


def get_game_3():
    game = Game(id=3, turns=236, end='Дипломатическая')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Rusvelt_Vsadnik)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Cleopatra)
    team2 = Team()
    team2.add_player(players._TheDavidGame, leaders._Amanitore)
    team3 = Team()
    team3.add_player(players._TinyClayMan, leaders._Alieanora_England)
    team4 = Team()
    team4.add_player(players._Neodim, leaders._Peter_the_Great)
    team5 = Team()
    team5.add_player(players._The_Losst, leaders._Gilgamesh)

    game.teams = [team0, team1, team2, team3, team4, team5]
    return game


def get_game_4():
    game = Game(id=4, turns=215, end='Религиозная')
    team0 = Team()
    team0.add_player(players._Ortreke, leaders._Pochatok)
    team1 = Team()
    team1.add_player(players._Neodim, leaders._Vasilii_II)
    team2 = Team()
    team2.add_player(players._Leodroid, leaders._Chingishan)
    team3 = Team()
    team3.add_player(players._Cvytik, leaders._Perikl)
    team4 = Team()
    team4.add_player(players._TinyClayMan, leaders._Saladin)
    team5 = Team()
    team5.add_player(players._George_Best_7, leaders._Ekatetina_Medichi_Velikolepnaya)

    game.teams = [team0, team1, team2, team3, team4, team5]
    return game


def get_game_5():
    game = Game(id=5, turns=192, end='Религиозная')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Yadviga)
    team0.add_player(players._MaxBelol, leaders._Robert_Brus)
    team0.add_player(players._Neodim, leaders._Peter_the_Great)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Ambiotriks)
    team1.add_player(players._TinyClayMan, leaders._Hubilai_Mongol)

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_game_6():
    game = Game(id=6, turns=182, end='Дипломатическая')
    team0 = Team()
    team0.add_player(players._Neodim, leaders._Peter_the_Great)
    team0.add_player(players._Ortreke, leaders._Montesuma)
    team0.add_player(players._SaltySoup, leaders._Friedrich_Barbarossa)
    team0.add_player(players._StillWiseOut, leaders._Didona)
    team0.add_player(players._The_Losst, leaders._Ish_vak)

    team1 = Team()
    team1.add_player(players._Cvytik, leaders._Vilgelmina)
    team1.add_player(players._George_Best_7, leaders._Wilfried_Lorie)
    team1.add_player(players._Leodroid, leaders._Hojo_Tokimune)
    team1.add_player(players._MaxBelol, leaders._Simon_Bolivar)
    team1.add_player(players._TinyClayMan, leaders._viktoria)

    game.teams.append(team0)
    game.teams.append(team1)

    return game


def get_game_7():
    game = Game(id=7, turns=241, end='Дипломатическая')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Hammurapi)
    team1 = Team()
    team1.add_player(players._Neodim, leaders._Peter_the_Great)
    team2 = Team()
    team2.add_player(players._TinyClayMan, leaders._Matiash_I)
    team3 = Team()
    team3.add_player(players._MaxBelol, leaders._Kristina_I)
    team4 = Team()
    team4.add_player(players._Leodroid, leaders._Tamara)
    team5 = Team()
    team5.add_player(players._Kris, leaders._Friedrich_Barbarossa)
    team6 = Team()
    team6.add_player(players._Losyashboi, leaders._Ish_vak)

    game.teams = [team0, team1, team2, team3, team4, team5, team6]
    return game


def get_game_8():
    game = Game(id=8, turns=220, end='Дипломатическая')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Tin_Huan)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Chieu_Vietnam)
    team2 = Team()
    team2.add_player(players._Losyashboi, leaders._Hojo_Tokimune)
    team3 = Team()
    team3.add_player(players._TinyClayMan, leaders._Juan_III)

    game.teams = [team0, team1, team2, team3, ]
    return game


def get_game_9():
    game = Game(id=9, turns=148, end='Религиозная')
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Javarman)
    team1 = Team()
    team1.add_player(players._George_Best_7, leaders._Kupe)
    team2 = Team()
    team2.add_player(players._TinyClayMan, leaders._PoundMaker)
    team3 = Team()
    team3.add_player(players._Kris, leaders._Hojo_Tokimune)

    game.teams = [team0, team1, team2, team3, ]
    return game

def get_game_10():
    game = Game(id=10, turns=72, end='Военная')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Kir)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Menelik2)

    game.teams = [team0, team1, ]
    return game

def get_game_11():
    game = Game(id=11, turns=232, end='Научная')
    team0 = Team()
    team0.add_player(players._The_Losst, leaders._Friedrich_Barbarossa)
    team1 = Team()
    team1.add_player(players._TinyClayMan, leaders._Lautaro)
    team2 = Team()
    team2.add_player(players._Neodim, leaders._Peter_the_Great)
    team3 = Team()
    team3.add_player(players._Leodroid, leaders._Tomiris)
    team4 = Team()
    team4.add_player(players._George_Best_7, leaders._Suleiman)

    game.teams = [team0, team1, team2, team3, team4, ]
    return game


games_storage = GamesStorage([
    get_game_1(),
    get_game_2(),
    get_game_3(),
    get_game_4(),
    get_game_5(),
    get_game_6(),
    get_game_7(),
    get_game_8(),
    get_game_9(),
    get_game_10(),
    get_game_11()
])
