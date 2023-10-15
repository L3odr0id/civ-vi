from constants import Guaranteed_score, STOP_BONUS_GAME_NUM
from data.player import Player

class GameBonus:
    """
    Расчёт безусловного бонуса
    """
    def __init__(self, p: Player) -> None:
        self.p : Player = p

    def get_value(self) -> float:
        games_played = self.p.games_amount
        if games_played >= STOP_BONUS_GAME_NUM:
            return 0.0
        else:
            percent = games_played*100 / STOP_BONUS_GAME_NUM
            bonus_mul = (100 - percent) / 100
            res = Guaranteed_score * bonus_mul
            return res

