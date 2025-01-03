from data.game import Game
from data.team import Team

from storage.games_storage import GamesStorage

import values.players as players
import values.leaders as leaders


def get_game_1():
    game = Game(1, 144, 'Суп ушёл варить пельмени', start_date='2020-02-05', finish_date='2020-02-05')

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
    game = Game(2, 148, 'Культурная', start_date='2020-11-14', finish_date='2020-11-15')
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
    game = Game(3, 236, 'Дипломатическая', start_date='2020-12-28', finish_date='2020-12-30')
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
    game = Game(4, 215, 'Религиозная', start_date='2021-02-01', finish_date='2021-02-03')
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
    game = Game(5, 192, 'Религиозная', start_date='2021-02-14', finish_date='2021-02-28')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Yadviga)
    team0.add_player(players._MaxBelol, leaders._Robert_Brus)
    team0.add_player(players._Neodim, leaders._Peter_the_Great)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Ambiotriks)
    team1.add_player(players._TinyClayMan, leaders._Hubilai_Mongol)
    team1.add_player(players._Bot_4_civ6, leaders._Alexandr_Makedonia)

    game.teams = [team0, team1]
    return game


def get_game_6():
    game = Game(6, 182, 'Дипломатическая', start_date='2021-04-04', finish_date='2021-04-18')
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
    game = Game(7, 241, 'Дипломатическая', start_date='2021-04-25', finish_date='2021-05-09')
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
    game = Game(8 , 220, 'Дипломатическая', start_date='2021-05-16', finish_date='2021-06-27')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Tin_Huan)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Chieu_Vietnam)
    team4 = Team()
    team4.add_player(players._Bot_4_civ6, leaders._Trayan)
    team2 = Team()
    team2.add_player(players._Losyashboi, leaders._Hojo_Tokimune)
    team5 = Team()
    team5.add_player(players._Bot_4_civ6, leaders._Peter_the_Great)
    team3 = Team()
    team3.add_player(players._TinyClayMan, leaders._Juan_III)

    game.teams = [team0, team1, team4, team2, team5, team3]
    return game


def get_game_9():
    game = Game(9, 148, 'Религиозная', start_date='2022-03-13', finish_date='2022-03-13', seconds_per_move='69')
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
    game = Game(10, 72, 'Военная', start_date='2022-04-24', finish_date='2022-04-24')
    team0 = Team()
    team0.add_player(players._George_Best_7, leaders._Kir)
    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Menelik2)

    game.teams = [team0, team1]
    return game

def get_game_11():
    game = Game(11, 232, 'Научная', start_date='2022-09-18', finish_date='2022-10-16')
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
    team5 = Team()
    team5.add_player(players._Bot_4_civ6, leaders._Trayan)

    game.teams = [team0, team1, team2, team3, team4, team5]
    return game

def get_game_12():
    game = Game(12, 181, 'Военная', start_date='2023-02-04', finish_date='2023-02-11', seconds_per_move='169')
    team0 = Team()
    team0.add_player(players._MaxBelol, leaders._Filipp_2)
    team0.add_player(players._TinyClayMan, leaders._Wu_Zeitian)
    team0.add_player(players._George_Best_7, leaders._Tokugawa)
    team0.add_player(players._Cvytik, leaders._Friedrich_Barbarossa)

    team1 = Team()
    team1.add_player(players._Neodim, leaders._Peter_the_Great)
    team1.add_player(players._MixKage, leaders._Trayan)
    team1.add_player(players._Leodroid, leaders._Ekaterina_Medichi_Black_Queen)
    team1.add_player(players._Bot_4_civ6, leaders._Gorgo_Grece)

    game.teams = [team0, team1]
    return game

def get_game_13():
    game = Game(13, 198, 'Научная', start_date='2023-02-18', finish_date='2023-02-25', seconds_per_move='169')
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Hubilau_China)

    team1 = Team()
    team1.add_player(players._TinyClayMan, leaders._Gandi)

    team2 = Team()
    team2.add_player(players._MaxBelol, leaders._Suleiman_muhtesem)

    team3 = Team()
    team3.add_player(players._Bot_5_civ6, leaders._Peter_the_Great)

    team4 = Team()
    team4.add_player(players._George_Best_7, leaders._Tribuhvana)

    game.teams = [team0, team1, team2, team3, team4]
    return game

def get_game_14():
    game = Game(14, 175, 'Дипломатическая', start_date='2023-03-04', finish_date='2023-03-04', seconds_per_move='148')
    team0 = Team()
    team0.add_player(players._TinyClayMan, leaders._Saladin_sultan)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Tin_Huan_unifier)

    team2 = Team()
    team2.add_player(players._George_Best_7, leaders._Nader_shah)

    team3 = Team()
    team3.add_player(players._Bot_5_civ6, leaders._Alieanora_France)

    game.teams = [team0, team1, team2, team3]
    return game

def get_game_15():
    game = Game(15, 125, 'Военная', start_date='2023-04-22', finish_date='2023-04-22', seconds_per_move='148')
    team0 = Team()
    team0.add_player(players._TinyClayMan, leaders._Victoria)
    team0.add_player(players._Leodroid, leaders._Chandaragupta)

    team1 = Team()
    team1.add_player(players._Neodim, leaders._Peter_the_Great)
    team1.add_player(players._George_Best_7, leaders._Yongle)

    game.teams = [team0, team1]
    return game

def get_game_16():
    game = Game(16, 161, 'Религиозная', start_date='2023-10-08', finish_date='2023-10-15', seconds_per_move='Flatter Dynamic Turn Timer')
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Cleopatra_Ptolematic)

    team1 = Team()
    team1.add_player(players._MaxBelol, leaders._Teodora)

    team2 = Team()
    team2.add_player(players._George_Best_7, leaders._Mvembda)

    team3 = Team()
    team3.add_player(players._TinyClayMan, leaders._Harald)

    team4 = Team()
    team4.add_player(players._Debil, leaders._Mansa_Musa)

    team5 = Team()
    team5.add_player(players._MixKage, leaders._Trayan)

    team6 = Team()
    team6.add_player(players._Neodim, leaders._Peter_the_Great)

    game.teams = [team0, team1, team2, team3, team4, team5, team6]
    return game

def get_game_17():
    game = Game(17, 214, 'Религиозная', start_date='2023-11-12', finish_date='2023-12-10', seconds_per_move='115')
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Nzinga_Mbandi)

    team1 = Team()
    team1.add_player(players._TinyClayMan, leaders._Ramses)

    team2 = Team()
    team2.add_player(players._MaxBelol, leaders._Ludwig)

    team3 = Team()
    team3.add_player(players._Przemyslaw_Wojciechowski, leaders._Harald_Varangian)

    team4 = Team()
    team4.add_player(players._V4kodin, leaders._Rusvelt_Vsadnik)

    game.teams = [team0, team1, team2, team3, team4]
    return game

def get_game_18():
    game = Game(18, 171, 'Религиозная', start_date='2024-02-25', finish_date='2024-03-03', seconds_per_move='https://github.com/L3odr0id/civ_vi_timer_mod/commit/98ec76e60fd0ac5f19843891242b95847bec02e4')
    
    team0 = Team()
    team0.add_player(players._TinyClayMan, leaders._Sundiata_Keita)

    team1 = Team()
    team1.add_player(players._MaxBelol, leaders._Montesuma)

    team2 = Team()
    team2.add_player(players._Leodroid, leaders._Ramses)

    team3 = Team()
    team3.add_player(players._George_Best_7, leaders._Rusvelt_Progressive)

    game.teams = [team0, team1, team2, team3]
    return game

def get_game_19():
    game = Game(19, 181, 'Культурная', start_date='2024-03-17', finish_date='2024-04-07', seconds_per_move='https://github.com/L3odr0id/civ_vi_timer_mod/commit/98ec76e60fd0ac5f19843891242b95847bec02e4')
    
    team0 = Team()
    team0.add_player(players._MaxBelol, leaders._Hojo_Tokimune)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Robert_Brus)

    team2 = Team()
    team2.add_player(players._MixKage, leaders._Trayan)

    team3 = Team()
    team3.add_player(players._George_Best_7, leaders._Vasilii_II)

    team4 = Team()
    team4.add_player(players._TinyClayMan, leaders._Alexandr_Makedonia)

    game.teams = [team0, team1, team2, team3, team4]
    return game

def get_game_20():
    game = Game(20, 151, 'Религиозная', start_date='2024-04-28', finish_date='2024-05-05', seconds_per_move='https://github.com/L3odr0id/civ_vi_timer_mod/commit/98ec76e60fd0ac5f19843891242b95847bec02e4')
    
    team0 = Team()
    team0.add_player(players._Leodroid, leaders._Hammurapi)

    team1 = Team()
    team1.add_player(players._TinyClayMan, leaders._Peter_the_Great)

    team2 = Team()
    team2.add_player(players._MaxBelol, leaders._Mvembda)

    game.teams = [team0, team1, team2]
    return game

def get_game_21():
    game = Game(21, 155, 'Культурная', start_date='2024-12-15', finish_date='2024-12-22', seconds_per_move='дефолтный дин. таймер')
    
    team0 = Team()
    team0.add_player(players._MaxBelol, leaders._Vilgelmina)

    team1 = Team()
    team1.add_player(players._Leodroid, leaders._Wilfried_Lorie)

    team2 = Team()
    team2.add_player(players._TinyClayMan, leaders._Kupe)

    team3 = Team()
    team3.add_player(players._George_Best_7, leaders._Matiash_I)

    game.teams = [team0, team1, team2, team3]
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
    get_game_11(),
    get_game_12(),
    get_game_13(),
    get_game_14(),
    get_game_15(),
    get_game_16(),
    get_game_17(),
    get_game_18(),
    get_game_19(),
    get_game_20(),
    get_game_21()
])
