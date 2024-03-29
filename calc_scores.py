from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.game import Game
from constants import K, WIN_AWARD

from data.game_info import GameInfo
from data.player import RatingChange
from calculations.game_bonus import GameBonus


def get_elo_change(rating1: int, rating2: int, win: bool):
    ea = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    return K * (int(win) - ea)


def calc_scores(game: Game):
    WIN = True
    LOSE = False
    # Для каждой команды рассчитываем средний рейтинг
    # Затем её выигрыш или проигрыш по отношению ко всем другим и суммируем результат
    # Каждому участнику команды добавляем очки результата

    # Рассчитаем изменения рейтингов для всех игроков
    avgs = []
    for i in range(len(game.teams)):
        our_rating = game.teams[i].get_average_rating()
        sum = 0
        for j in range(len(game.teams)):
            if i > j:
                # мы проигрываем этой команде
                their_rating = game.teams[j].get_average_rating()
                sum += get_elo_change(int(our_rating), int(their_rating), LOSE)
            if i < j:
                # мы выигрываем у этой команды
                their_rating = game.teams[j].get_average_rating()
                sum += get_elo_change(int(our_rating), int(their_rating), WIN)
        avg = sum / (len(game.teams)-1)
        avgs.append(avg)

    # Применим изменения
    for i in range(len(game.teams)):
        for meta in game.teams[i].get_players():
            player = meta.player
            leader = meta.leader

            # Подсчёт статистики
            player.games_amount += 1
            if i == 0:
                # Выигрыш партии
                if len(game.teams[0].get_players()) == 1:
                    player.solo_wins_amount += 1
                else:
                    player.team_wins_amount += 1

            win_award = WIN_AWARD if i == 0 else 0 # Надбавка за победу
            # game_bonus = Guaranteed_score # Безусловный бонус за участие в партии
            game_bonus = GameBonus(p=player).get_value()

            change = round(avgs[i] + game_bonus + win_award)  # Изменение рейтинга

            if player.is_bot and player.games_info and player.games_info[-1].game.id == game.id:
                # Если player - это бот и таких ботов участвовало несколько в партии,
                # тогда не нужно лишний раз начислять ему баллы за участие
                change -= game_bonus

            if player.highest_rating_take[0] < change:
                player.highest_rating_take = (change, game.id)
            if player.lowest_rating_take[0] > change:
                player.lowest_rating_take = (change, game.id)

            # Изменить рейтинг
            player.rating += change
            player.rating = round(player.rating)

            # Статистика пикового значения очков
            player.peak_rating = max(player.rating, player.peak_rating)

            # история изменений
            player.rating_changes.append(RatingChange(game.id, change))

            # для лидера и нации добавляем запись об игре
            game_info = GameInfo(game, player.id, leader.id,
                                 leader.nation.id, i == 0, change, i + 1,
                                 )
            player.games_info.append(game_info)
            leader.games_info.append(game_info)
            leader.nation.games_info.append(game_info)
