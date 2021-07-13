from game_info import GameInfo
from games import Game

K = 20
Guaranteed_score = round(K / 2.5)


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
                sum += get_elo_change(our_rating, their_rating, LOSE)
            if i < j:
                # мы выигрываем у этой команды
                their_rating = game.teams[j].get_average_rating()
                sum += get_elo_change(our_rating, their_rating, WIN)
        avg = sum / len(game.teams)
        avgs.append(avg)

    # Применим изменения
    for i in range(len(avgs)):
        for meta in game.teams[i].get_players():
            player = meta.player
            leader = meta.leader

            # Подсчёт статистики
            player.games_count += 1
            if i == 0:
                # Выигрыш партии
                if len(game.teams[0].get_players()) == 1:
                    player.personal_wins += 1
                else:
                    player.team_wins += 1
            change = round(avgs[i] + Guaranteed_score)  # Изменение рейтинга

            if player.highest_score_take[0] < change:
                player.highest_score_take = [change, game.index]
            if player.highest_score_loss[0] > change:
                player.highest_score_loss = [change, game.index]

            # Изменить рейтинг
            player.rating += change
            player.rating = round(player.rating)

            # Статистика пикового значения очков
            player.peak_score = max(player.rating, player.peak_score)

            # история изменений
            player.changes_history.append({'game_index': game.index,
                                           'rating_change': change})

            # для лидера и нации добавляем запись об игре
            game_info = GameInfo(game.index, player.index, leader.index, leader.nation.index, i == 0, change, i + 1)
            player.games_info.append(game_info)
            leader.games_info.append(game_info)
            leader.nation.games_info.append(game_info)
