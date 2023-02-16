from data.player import Player


class Winstreak:
    def set_values(self, player: Player):
        max_streak = 0
        current_streak = 0
        for game in player.games_info:
            if game.isWin:
                current_streak += 1
                max_streak = max(current_streak, max_streak)
            else:
                current_streak = 0
        player.max_win_streak = max_streak
        player.current_win_streak = current_streak
