import json
from calc_scores import calc_scores
from games import get_history, get_games_serializable
from leader import leadersStorage
from nations import nations_storage
from players_storage import playerStorage


def main():
    games = get_history()

    for i in range(len(games)):
        calc_scores(games[i])
        # print('Результаты партии ' + str(i + 1))
        playerStorage.sort()
        # Наивысшую/Низшую и изменение позиции
        for j in range(len(playerStorage.players)):
            playerStorage.players[j].top_position = min(playerStorage.players[j].top_position, j + 1)
            playerStorage.players[j].lowest_position = max(playerStorage.players[j].lowest_position, j + 1)
            playerStorage.players[j].change_position = playerStorage.players[j].previous_position - j - 1
            playerStorage.players[j].previous_position = j + 1
        # playerStorage.print()
        # print()

    res_json = dict()
    res_json['users'] = playerStorage.get_serializable()
    res_json['games'] = get_games_serializable(games)
    res_json['leaders'] = leadersStorage.get_serializable()
    res_json['nations'] = nations_storage.get_serializable()

    # pushToFirebase(res_json)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)
    # for game in games:
    #     game.print()

    # ps.sort()
    # ps.print()


if __name__ == "__main__":
    main()
