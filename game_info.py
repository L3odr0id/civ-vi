class GameInfo:
    def __init__(self, game_index: int, player_index: int, is_win: bool, score_change: int, place: int):
        self.game_index = game_index
        self.player_index = player_index
        self.isWin = is_win
        self.scoreChange = score_change
        self.place = place

    def get_serializable(self):
        d = dict()
        d['game_index'] = self.game_index
        d['player_index'] = self.player_index
        d['is_win'] = self.isWin
        d['score_change'] = self.scoreChange
        d['place'] = self.place
        return d
