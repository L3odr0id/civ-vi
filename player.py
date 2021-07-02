INITIAL_RATING = 228


class Player:
    def __init__(self, index: int, name: str):
        self.index = index  # ID игрока
        self.name = name    # Никнейм
        self.rating = INITIAL_RATING  # Рейтинг
        self.games_count = 0    # Кол-во игр
        self.personal_wins = 0  # Личных побед
        self.team_wins = 0      # Командных побед
        self.highest_score_take = [-INITIAL_RATING, -1]  # Наибольшее кол-во очков за партию
        self.highest_score_loss = [INITIAL_RATING, -1]  # Наименьшее кол-во очков за игру
        self.peak_score = INITIAL_RATING  # Пиковый рейтинг
        self.changes_history = []   # История изменения рейтинга [индекс игры, изменение]
        self.top_position = 228     # Наивысшая позиция
        self.lowest_position = -1   # Низшая позиция
        self.previous_position = 0  # Позиция в результате прошлой партии
        self.change_position = 0    # Позиция в результате прошлой партии

    def __lt__(self, other):
        return self.rating > other.rating

    def get_serializable(self):
        d = dict()
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
        # d['peak_score'] = self.peak_score
        d['changes'] = self.changes_history
        d['top_position'] = self.top_position
        d['lowest_position'] = self.lowest_position
        d['average'] = self.get_average()
        d['win_rate'] = self.get_win_rate()
        d['change_position'] = self.change_position
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
            res += i[1]
        return round(res / self.games_count, 2)
