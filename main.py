import json
from calc_scores import calc_scores
# from firebase import pushToFirebase

from values.players import player_storage
from values.leaders import leadersStorage
from values.nations import nations_storage
from values.games import games_storage


def main():

    for game in games_storage.games:
        calc_scores(game)
        # print('Результаты партии ' + str(i + 1))
        player_storage.sort()
        # Наивысшую/Низшую и изменение позиции
        for j in range(len(player_storage.players)):
            player_storage.players[j].top_position = min(player_storage.players[j].top_position, j + 1)
            player_storage.players[j].lowest_position = max(player_storage.players[j].lowest_position, j + 1)
            player_storage.players[j].change_position = player_storage.players[j].previous_position - j - 1
            player_storage.players[j].previous_position = j + 1
        # playerStorage.print()
        # print()

    res_json = dict()
    res_json['players'] = player_storage.get_serializable()
    res_json['games'] = games_storage.get_serializable()
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
