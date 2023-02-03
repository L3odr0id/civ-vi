from data.game import Game
from data.team import Team

from storage.games_storage import GamesStorage

import values.players as players
import values.leaders as leaders


def get_game_1():
    game = Game(1, 144, 'Суп ушёл варить пельмени', start_date='02.05.2020', finish_date='02.05.2020', seconds_per_move=-1)

    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Friedrich_Barbarossa)
    team0.add_player(players._Leodroid, leaders._Trayan)
    team0.add_player(players._Veldy, leaders._Peter_the_Great)

    team1 = Team()
    team1.add_player(players._Neodim, leaders._Mansa_Musa)
    team1.add_player(players._SaltySoup, leaders._Hojo_Tokimune)
    team1.add_player(players._The_Losst, leaders._Rusvelt_Progressive)

    game.teams = [team0, team1]
    return game


def get_game_2():
    game = Game(2, 148, 'Культурная', start_date='14.11.2020', finish_date='15.11.2020', seconds_per_move=-1)
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Pedru_II)
    team1 = Team()
    team1.add_player(players._Neodim, leaders._Peter_the_Great)
    team2 = Team()
    team2.add_player(players._Leodroid, leaders._Chaka)
    team3 = Team()
    team3.add_player(players._MaxBelol, leaders._Yadviga)

    game.teams = [team0, team1, team2, team3]
    return game


def get_game_3():
    game = Game(3, 236, 'Дипломатическая', start_date='28.12.2020', finish_date='30.12.2020', seconds_per_move=-1)
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
    game = Game(4, 215, 'Религиозная', start_date='01.02.2021', finish_date='03.02.2021', seconds_per_move=-1)
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
    game = Game(5, 192, 'Религиозная', start_date='28.02.2021', finish_date='14.02.2021', seconds_per_move=-1)
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Yadviga)
    team0.add_player(players._MaxBelol, leaders._Robert_Brus)
    team0.add_player(players._Neodim, leaders._Peter_the_Great)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Ambiotriks)
    team1.add_player(players._TinyClayMan, leaders._Hubilai_Mongol)

    game.teams = [team0, team1]
    return game


def get_game_6():
    game = Game(6, 182, 'Дипломатическая', start_date='04.04.2021', finish_date='18.04.2021', seconds_per_move=-1)
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

    game.teams = [team0, team1]
    return game


def get_game_7():
    game = Game(7, 241, 'Дипломатическая', start_date='25.04.2021', finish_date='09.05.2021', seconds_per_move=-1)
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
    game = Game(8, 220, 'Дипломатическая', start_date='16.05.2021', finish_date='27.06.2021', seconds_per_move=-1)
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Tin_Huan)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Chieu_Vietnam)
    team2 = Team()
    team2.add_player(players._Losyashboi, leaders._Hojo_Tokimune)
    team3 = Team()
    team3.add_player(players._TinyClayMan, leaders._Juan_III)

    game.teams = [team0, team1, team2, team3]
    return game


def get_game_9():
    game = Game(9, 148, 'Религиозная', start_date='13.3.2022', finish_date='13.3.2022', seconds_per_move=69)
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Javarman)
    team1 = Team()
    team1.add_player(players._George_Best_7, leaders._Kupe)
    team2 = Team()
    team2.add_player(players._TinyClayMan, leaders._PoundMaker)
    team3 = Team()
    team3.add_player(players._Kris, leaders._Hojo_Tokimune)

    game.teams = [team0, team1, team2, team3]
    return game

def get_game_10():
    game = Game(10, 72, 'Военная', start_date='24.04.2022', finish_date='24.04.2022', seconds_per_move=-1)
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Kir)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Menelik2)

    game.teams = [team0, team1]
    return game

def get_game_11():
    game = Game(11, 232, 'Научная', start_date='18.09.2022', finish_date='16.10.2022', seconds_per_move=-1)
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

    game.teams = [team0, team1, team2, team3, team4]
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
