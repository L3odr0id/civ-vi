class Leader:
    def __init__(self, name: str, nation: str, index: int):
        self.name = name
        self.nationName = nation
        self.index = index
        self.nation = Nation(0, '')  # плесйхолдер
        self.games_info = []

    def get_serializable(self):
        d = dict()
        d['leader_id'] = self.index
        d['name'] = self.name
        d['nation_name'] = self.nationName
        d['nation_id'] = self.nation.index
        arr = []
        for i in self.games_info:
            arr.append(i.get_serializable())
        d['games_info'] = arr
        return d


class LeadersStorage:
    def __init__(self, leaders: list):
        self.leaders = leaders

    def leader(self, index: int):
        for i in self.leaders:
            if i.index == index:
                return i

    def get_serializable(self):
        d = dict()
        for i in self.leaders:
            d[i.index] = i.get_serializable()
        return d


class Nation:
    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        self.games_info = []
        self.__leaders = []

    def add_leader(self, leader: Leader):
        self.__leaders.append(leader)

    def get_serializable(self):
        d = dict()
        d['nation_id'] = self.index
        d['name'] = self.name
        arr = []
        for i in self.games_info:
            arr.append(i.get_serializable())
        d['games_info'] = arr
        return d


Leaders_list = [
    Leader('Александр', 'Македония', 0),
    Leader('Алиенора Аквитанская (Англия)', 'Англия', 1),
    Leader('Алиенора Аквитанская (Франция)', 'Франция', 2),
    Leader('Аманиторе', 'Нубия', 3),
    Leader('Амбиорикс', 'Галлия', 4),
    Leader('Василий II', 'Византия (Россия 2)', 5),
    Leader('Виктория', 'Англия', 6),
    Leader('Вильгельмина', 'Нидерланды', 7),
    Leader('Ганди', 'Индия', 8),
    Leader('Гильгамеш', 'Шумер', 9),
    Leader('Горго', 'Греция', 10),
    Leader('Джайаварман VII', 'Кхмеры', 11),
    Leader('Джон Кэртин', 'Австралия', 12),
    Leader('Дидона', 'Финикия', 13),
    Leader('Екатерина Медичи (Великолепная)', 'Франция', 14),
    Leader('Жуан III', 'Португалия', 15),
    Leader('Иш-Вак-Чан-Ахав', 'Майя', 16),
    Leader('Кир II', 'Персия', 17),
    Leader('Клеопатра', 'Египет', 18),
    Leader('Константин Острожский', 'Волынь', 19),
    Leader('Кристина', 'Швеция', 20),
    Leader('Купе', 'Маори', 21),
    Leader('Лаутаро', 'Мапуче', 22),
    Leader('Манса Муса', 'Мали', 23),
    Leader('Матьяш I', 'Венгрия', 24),
    Leader('Мвемба а Нзинга', 'Конго', 25),
    Leader('Менелик II', 'Эфиопия', 26),
    Leader('Монтесума', 'Ацтеки', 27),
    Leader('Пётр Великий', 'Россия', 28),
    Leader('Паундмейкер', 'Кри', 29),
    Leader('Пачакутек', 'Инки', 30),
    Leader('Педру II', 'Бразилия', 31),
    Leader('Перикл', 'Греция', 32),
    Leader('Роберт Брюс', 'Шотландия', 33),
    Leader('Саладин', 'Аравия', 34),
    Leader('Симон Боливар', 'Колумбия', 35),
    Leader('Сондок', 'Корея', 36),
    Leader('Сулейман', 'Османы', 37),
    Leader('Тамара', 'Грузия', 38),
    Leader('Теодор Рузвельт (Прогрессивист)', 'США', 39),
    Leader('Теодор Рузвельт (Мужественный всадник)', 'США', 40),
    Leader('Томирис', 'Скифия', 41),
    Leader('Траян', 'Рим', 42),
    Leader('Трибхувана', 'Индонезия', 43),
    Leader('Уилфрид Лорье', 'Канада', 44),
    Leader('Филипп II', 'Испания', 45),
    Leader('Фридрих Барбаросса', 'Германия', 46),
    Leader('Хаммурапи', 'Вавилон', 47),
    Leader('Харальд Суровый', 'Норвегия', 48),
    Leader('Ходзё Токимунэ', 'Япония', 49),
    Leader('Хубилай (Монголия)', 'Монголия', 50),
    Leader('Хубилай (Китай)', 'Китай', 51),
    Leader('Цинь Шихуанди', 'Китай', 52),
    Leader('Чака', 'Зулусы', 53),
    Leader('Чандрагупта', 'Индия', 54),
    Leader('Чингисхан', 'Монголия', 55),
    Leader('Чьеу Тхи Чинь', 'Вьетнам', 56),
    Leader('Ядвига', 'Польша', 57),
    Leader('Екатерина Медичи (Чёрная королева)', 'Франция', 58),
]

leadersStorage = LeadersStorage(Leaders_list)
