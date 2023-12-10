from storage.players_storage import PlayersStorage

from data.player import Player


# Игроки
_Neodim = Player('Neodim')
_George_Best_7 = Player('George_Best_7')
_Leodroid = Player('Leodroid')
_Ortreke = Player('Ortreke')
_The_Losst = Player('The_Losst')
_TinyClayMan = Player('TinyClayMan')
_SaltySoup = Player('SaltySoup')
_MaxBelol = Player('MaxBelol')
_StillWiseOut = Player('StillWiseOut')
_Cvytik = Player('Cvytik')
_Veldy = Player('Veldy')
_TheDavidGame = Player('TheDavidGame')
_Kris = Player('Kris')
_Losyashboi = Player('Losyashboi')
_MixKage = Player('MixKage')
_Debil = Player('Debil') # penechek20
_Przemyslaw_Wojciechowski = Player('Przemyslaw Wojciechowski') # spaceaccordeonist
_V4kodin = Player('V4kodin')

# Боты
_Bot_4_civ6 = Player('Бот (князь) CIV VI', is_bot=True)
_Bot_5_civ6 = Player('Бот (король) CIV VI', is_bot=True)


player_storage = PlayersStorage([
    _George_Best_7,
    _Leodroid,
    _Veldy,
    _Neodim,
    _SaltySoup,
    _The_Losst,
    _MaxBelol,
    _TinyClayMan,
    _TheDavidGame,
    _Ortreke,
    _Cvytik,
    _StillWiseOut,
    _Kris,
    _Losyashboi,
    _MixKage,
    _Bot_4_civ6,
    _Bot_5_civ6,
    _Debil,
    _Przemyslaw_Wojciechowski,
    _V4kodin
])
