# CIVILIZATION VI Stats

## Инфа
Вся информация разделена на блоки players, games, leaders и nations. Каждая из них представляет собой словарь, где каждому id соответствует конкретный объект. Объекты из разных блоков могут сслыться друг на друга по этим id.

## Описание сущностей:

### Players

- id = уникальный id игрока
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
- peak_rating = наибольшее значение рейтинга за всё время
- games_info = Краткая информация о играх, в которых принимал участие игрок, см. GameInfo

### RatingChange

- game_id = id игры
- rating_change = изменение рейтинга

### Game

- id = уникальный id игры
- teams = команды, участвующие в игре, см. Team
- turns = кол-во ходов
- reason = Причина победы

**Team**

player_id = индекс из словаря **Players** <br>
leader_id = индекс из словаря **Leaders** <br>

**Leaders**

id = уникальный id лидера <br>
name = имя лидера <br>
nation_name = название нации <br>
nation_id = index нации из словая **Nations** <br>
games_info = массив объектов **GameInfo** <br>

**Nations**

id = уникальный id нации <br>
name = имя нации <br>
games_info = массив объектов **GameInfo** <br>

**GameInfo**

game_id = id игры из **Games** <br>
player_id = id игрока из **Players** <br>
leader_id= id лидера из **Leaders** <br>
nation_id = id нации из **Nations** <br>
is_win = победа или нет <br>
score_change = изменение очков для этого игрока в этой игре <br>
place = место занятое в общем зачёте в данной партии <br>
