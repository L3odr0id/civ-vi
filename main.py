import json

from games import get_history, Game
from player import Player
from players_storage import PlayersStorage

NICKNAMES = [
    'Neodim',
    'George_Best_7',
    'Leodroid',
    'Ortreke',
    'The_Losst',
    'TinyClayMan',
    'SaltySoup',
    'MaxBelol',
    'StillWiseOut',
    'Cvytik',
    'Veldy',
    'TheDavidGame',
]

K = 20
Guaranteed_score = round(K / 2.5)


def get_players():
    res = PlayersStorage()
    for nick in NICKNAMES:
        res.players.append(Player(nick))
    return res


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
        for player in game.teams[i].players:
            # Подсчёт статистики
            player.games_count += 1
            if i == 0:
                # Выигрыш партии
                if len(game.teams[0].players) == 1:
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
            player.changes_history.append([game.index, change])


def get_games_serializable(games: list):
    res = []
    for game in games:
        res.append(game.get_serializable())
    return res


def main():
    ps = get_players()
    games = get_history(ps)

    ps.print()
    print()

    for i in range(len(games)):
        calc_scores(games[i])
        print('Результаты партии ' + str(i + 1))
        ps.sort()
        # Наивысшую/Низшую и изменение позиции
        for j in range(len(ps.players)):
            ps.players[j].top_position = min(ps.players[j].top_position, j + 1)
            ps.players[j].lowest_position = max(ps.players[j].lowest_position, j + 1)
            ps.players[j].change_position = ps.players[j].previous_position - j - 1
            ps.players[j].previous_position = j + 1
        ps.print()
        print()

    res_json = dict()
    res_json['users'] = ps.get_serializable()
    # res_json['games'] = get_games_serializable(games)
    # data = json.dumps(res_json) - хуйня
    # print(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)
    # for game in games:
    #     game.print()

    # ps.sort()
    # ps.print()


if __name__ == "__main__":
    main()
