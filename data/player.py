from typing import Tuple, List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.game_info import GameInfo

import itertools

from constants import INITIAL_RATING 

class RatingChange:
    def __init__(self, game_id: int, rating_change: int):
        self.game_id: int = game_id
        self.rating_change: int = rating_change

    def get_serializable(self):
        d = dict()
        d['game_id'] = self.game_id
        d['rating_change'] = self.rating_change
        return d

class Player:

    id_iter = itertools.count()

    def __init__(self, name: str):
        self.id: int = next(self.id_iter) # ID игрока
        self.name: str = name    # Никнейм
        self.rating: int = INITIAL_RATING  # Рейтинг
        self.games_amount: int = 0    # Кол-во игр
        self.solo_wins_amount: int = 0  # Личных побед
        self.team_wins_amount: int = 0      # Командных побед
        self.highest_rating_take: Tuple[int, int] = (-INITIAL_RATING, -1)  # Наибольшее кол-во рейтинга за партию
        self.lowest_rating_take: Tuple[int, int] = (INITIAL_RATING, -1)  # Наименьшее кол-во рейтинга за игру
        self.peak_rating: int = INITIAL_RATING  # Пиковый рейтинг
        self.rating_changes: List[RatingChange] = []   # История изменения рейтинга [индекс игры, изменение]
        self.top_position: int = 228     # Наивысшая позиция
        self.lowest_position: int = -1   # Низшая позиция
        self.previous_position: int = 0  # Позиция в результате прошлой партии
        self.change_position: int = 0    # Позиция в результате прошлой партии
        self.games_info: List[GameInfo] = [] # Краткая информация о играх, в которых принимал участие игрок
        self.current_win_streak = 0     # Текущий винстрик
        self.max_win_streak = 0         # Лучший винстрик

    def __lt__(self, other):
        return self.rating > other.rating

    def get_serializable(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        d['rating'] = self.rating
        d['games_amount'] = self.games_amount
        d['solo_wins_amount'] = self.solo_wins_amount
        d['team_wins_amount'] = self.team_wins_amount
        d['total_wins_amount'] = self.get_wins_count()
        d['highest_rating_take'] = self.highest_rating_take[0]
        d['highest_rating_take_game'] = self.highest_rating_take[1]
        d['lowest_rating_take'] = self.lowest_rating_take[0]
        d['lowest_rating_take_game'] = self.lowest_rating_take[1]
        d['peak_rating'] = self.peak_rating
        rating_changes = []
        for change in self.rating_changes:
            rating_changes.append(change.get_serializable())
        d['rating_changes'] = rating_changes
        d['top_position'] = self.top_position
        d['lowest_position'] = self.lowest_position
        d['average_rating'] = self.get_average_rating()
        d['win_rate'] = self.get_win_rate()
        d['change_position'] = self.change_position
        games_info = []
        for game_info in self.games_info:
            games_info.append(game_info.get_serializable())
        d['games_info'] = games_info
        d['current_win_streak'] = self.current_win_streak
        d['max_win_streak'] = self.max_win_streak
        return d

    def get_wins_count(self):
        return self.team_wins_amount + self.solo_wins_amount

    def get_win_rate(self):
        if self.games_amount == 0:
            return 0
        return round(self.get_wins_count() / self.games_amount, 2)

    def get_average_rating(self):
        if self.games_amount == 0:
            return 0
        res = 0
        for i in self.rating_changes:
            res += i.rating_change
        return round(res / self.games_amount, 2)
