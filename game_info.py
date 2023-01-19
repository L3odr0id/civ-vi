class GameInfo:
    def __init__(self, game_id: int, player_id: int, leader_id: int, nation_id: int, is_win: bool,
                 score_change: int, place: int, ):
        self.game_id = game_id
        self.player_id = player_id
        self.isWin = is_win
        self.scoreChange = score_change
        self.place = place
        self.leader_id = leader_id
        self.nation_id = nation_id

    def get_serializable(self):
        d = dict()
        d['game_id'] = self.game_id
        d['player_id'] = self.player_id
        d['is_win'] = self.isWin
        d['score_change'] = self.scoreChange
        d['place'] = self.place
        d['leader_id'] = self.leader_id
        d['nation_id'] = self.nation_id
        return d
