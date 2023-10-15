from constants import Guaranteed_score, STOP_BONUS_GAME_NUM
from data.player import Player

class GameBonus:
    """
    Расчёт безусловного бонуса
    """
    def __init__(self, p: Player) -> None:
        self.p : Player = p

    def get_value(self) -> float:
        forever_bonus = float(Guaranteed_score / 4)
        games_played = self.p.games_amount

        if games_played >= STOP_BONUS_GAME_NUM:
            return forever_bonus
        else:
            percent = games_played*100 / STOP_BONUS_GAME_NUM
            bonus_mul = (100 - percent) / 100
            res = Guaranteed_score * bonus_mul
            return max(res, forever_bonus)

