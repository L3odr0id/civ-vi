class GameInfo:
    def __init__(self, game_id: int, player_id: int, leader_id: int, nation_id: int, is_win: bool,
                 score_change: int, place: int, ):
        self.game_id: int = game_id
        self.player_id: int = player_id
        self.isWin: bool = is_win
        self.scoreChange: int = score_change
        self.place: int = place
        self.leader_id: int = leader_id
        self.nation_id: int = nation_id

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
