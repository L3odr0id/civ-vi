# CIVILIZATION VI Stats

## Инфа
Вся информация разделена на блоки players, games, leaders и nations. Каждая из них представляет собой словарь, где каждому index соответствует конкретный объект. Объекты из разных отделов могут сслыться друг на друга по этим индексам.

### Описание ключей:
**Players**

player_id = уникальный id игрока <br>
name = Ник игрока <br>
rating = Рейтинг <br>
count = Кол-во сыграных партий <br>
personal_wins = Кол-во одиночных побед <br>
team_wins = Кол-во командных побед <br>
total_wins = Общее кол-во побед. total_wins = personal_wins + team_wins <br>
highest_score_take = Максимальное кол-во очков за партию <br>
highest_score_game = Номер игры, где получено наибольшее кол-во очков <br>
lowest_score_take = Наименьшее кол-во очков за партию <br>
lowest_score_game= Номер игры, где получено наименьшее кол-во очков за партию <br>
changes = История изменений очков в формате {'game_id' : id игры из **Games**, 'rating_change' : изменение рейтинга} <br>
top_position = Наивысшая позиция, которую игрок занимал в таблице <br>
lowest_position = Низшая позиция, которую игрок занимал в таблице <br>
average = Среднее кол-во очков за партию <br>
win_rate = Процент побед <br>
change_position = Изменение позиции в таблице, относительно прошлой игры <br>
peak_score = наибольшее значение рейтинга за всё время <br>
games_info = массив объектов **GameInfo** <br>

**Games**

game_id = уникальный id игры <br>
teams = массив объектов **Team** <br>
turns = кол-во ходов <br>
reason = название победы <br>

**Team**

player_id = индекс из словаря **Players** <br>
leader_id = индекс из словаря **Leaders** <br>

**Leaders**

leader_id = уникальный id лидера <br>
name = имя лидера <br>
nation_name = название нации <br>
nation_id = index нации из словая **Nations** <br>
games_info = массив объектов **GameInfo** <br>

**Nations**

nation_id = уникальный id нации <br>
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
