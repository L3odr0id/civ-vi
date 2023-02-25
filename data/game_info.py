from data.game import Game


class GameInfo:
    def __init__(self, game: Game, player_id: int, leader_id: int, nation_id: int, is_win: bool,
                 score_change: int, place: int ):
        self.game: Game = game # TODO Change type to Game and remove is_played_with_teams
        self.player_id: int = player_id
        self.isWin: bool = is_win
        self.scoreChange: int = score_change
        self.place: int = place
        self.leader_id: int = leader_id
        self.nation_id: int = nation_id
        # self.is_played_by_teams: bool = is_played_by_teams

    def get_serializable(self):
        d = dict()
        d['game_id'] = self.game.id
        d['game_number'] = self.game.game_number
        d['player_id'] = self.player_id
        d['is_win'] = self.isWin
        d['score_change'] = self.scoreChange
        d['place'] = self.place
        d['leader_id'] = self.leader_id
        d['nation_id'] = self.nation_id
        return d
    
    def is_played_by_teams(self) -> bool:
        return self.game.is_played_by_teams()
