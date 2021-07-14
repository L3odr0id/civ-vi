class GameInfo:
    def __init__(self, game_index: int, player_index: int, leader_index: int, nation_index: int, is_win: bool,
                 score_change: int, place: int, ):
        self.game_index = game_index
        self.player_index = player_index
        self.isWin = is_win
        self.scoreChange = score_change
        self.place = place
        self.leader_index = leader_index
        self.nation_index = nation_index

    def get_serializable(self):
        d = dict()
        d['game_id'] = self.game_index
        d['player_id'] = self.player_index
        d['is_win'] = self.isWin
        d['score_change'] = self.scoreChange
        d['place'] = self.place
        d['leader_id'] = self.leader_index
        d['nation_id'] = self.nation_index
        return d
