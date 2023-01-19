from typing import Tuple, List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.game_info import GameInfo

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
    def __init__(self, id: int, name: str):
        self.id: int = id  # ID игрока
        self.name: str = name    # Никнейм
        self.rating: int = INITIAL_RATING  # Рейтинг
        self.games_count: int = 0    # Кол-во игр
        self.personal_wins: int = 0  # Личных побед
        self.team_wins: int = 0      # Командных побед
        self.highest_score_take: Tuple[int, int] = (-INITIAL_RATING, -1)  # Наибольшее кол-во очков за партию
        self.highest_score_loss: Tuple[int, int] = (INITIAL_RATING, -1)  # Наименьшее кол-во очков за игру
        self.peak_score: int = INITIAL_RATING  # Пиковый рейтинг
        self.changes_history: List[RatingChange] = []   # История изменения рейтинга [индекс игры, изменение]
        self.top_position: int = 228     # Наивысшая позиция
        self.lowest_position: int = -1   # Низшая позиция
        self.previous_position: int = 0  # Позиция в результате прошлой партии
        self.change_position: int = 0    # Позиция в результате прошлой партии
        self.games_info: List[GameInfo] = []

    def __lt__(self, other):
        return self.rating > other.rating

    def get_serializable(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        d['rating'] = self.rating
        d['count'] = self.games_count
        d['personal_wins'] = self.personal_wins
        d['team_wins'] = self.team_wins
        d['total_wins'] = self.get_wins_count()
        d['highest_score_take'] = self.highest_score_take[0]
        d['highest_score_game'] = self.highest_score_take[1]
        d['lowest_score_take'] = self.highest_score_loss[0]
        d['lowest_score_game'] = self.highest_score_loss[1]
        d['peak_score'] = self.peak_score
        changes_history = []
        for change in self.changes_history:
            changes_history.append(change.get_serializable())
        d['changes'] = changes_history
        d['top_position'] = self.top_position
        d['lowest_position'] = self.lowest_position
        d['average'] = self.get_average()
        d['win_rate'] = self.get_win_rate()
        d['change_position'] = self.change_position
        games_info = []
        for game_info in self.games_info:
            games_info.append(game_info.get_serializable())
        d['games_info'] = games_info
        return d

    def get_wins_count(self):
        return self.team_wins + self.personal_wins

    def get_win_rate(self):
        if self.games_count == 0:
            return 0
        return round(self.get_wins_count() / self.games_count, 2)

    def get_average(self):
        if self.games_count == 0:
            return 0
        res = 0
        for i in self.changes_history:
            res += i.rating_change
        return round(res / self.games_count, 2)
