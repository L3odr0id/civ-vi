# CIVILIZATION VI Stats

## Инфа

Вся информация разделена на блоки players, games, leaders и nations. Каждая из них представляет собой словарь, где каждому id соответствует конкретный объект. Объекты из разных блоков могут сслыться друг на друга по этим id.

## Описание сущностей:

### Player

- id = Уникальный id игрока
- name = Ник игрока
- rating = Рейтинг
- games_amount = Кол-во сыграных партий
- solo_wins_amount = Кол-во одиночных побед
- team_wins_amount = Кол-во командных побед
- total_wins_amount = Общее кол-во побед
- highest_rating_take = Наибольшее кол-во рейтинга за партию
- highest_rating_take_game = Номер игры, где получено наибольшее кол-во рейтинга
- lowest_rating_take = Наименьшее кол-во рейтинга за партию
- lowest_rating_take_game = Номер игры, где получено наименьшее кол-во рейтинга за партию
- rating_changes = История изменений рейтинга, см. RatingChange
- top_position = Наивысшая позиция, которую игрок занимал в таблице
- lowest_position = Низшая позиция, которую игрок занимал в таблице
- average_rating = Среднее кол-во очков за партию
- win_rate = Процент побед
- change_position = Изменение позиции в таблице, относительно прошлой игры
- peak_rating = Наибольшее значение рейтинга за всё время
- games_info = Краткая информация о играх, в которых принимал участие игрок, см. GameInfo

### RatingChange

- game_id = id игры
- rating_change = Изменение рейтинга

### Game

- id = Уникальный id игры
- teams = Команды, участвующие в игре, см. Team
- turns = Кол-во ходов
- reason = Причина победы

### Team

- player_id = id игрока, см. Player
- leader_id = id лидера нации, см. Leader

### Leader

- id = Уникальный id лидера
- name = Имя лидера
- nation_name = Название нации
- nation_id = id нации, см Nation
- games_info = Краткая информация о играх, в которых принимал участие этот лидер, см. GameInfo

### Nation

- id = Уникальный id нации
- name = Название нации
- games_info = Краткая информация о играх, в которых принимала участие эта нация, см. GameInfo

### GameInfo

- game_id = id игры, см. Game
- player_id = id игрока, см. Player
- leader_id= id лидера, см. Leaders
- nation_id = id нации, см. Nation
- is_win = Победа или нет
- score_change = Изменение очков для этого игрока в этой игре
- place = Место занятое в общем зачёте в данной партии
