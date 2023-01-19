from leader import LeadersStorage, leadersStorage, Nation


# Хранилище наций
class NationsStorage:
    def __init__(self):
        self.__nations: list[Nation] = []

    # Всем нациям поставить в соответствие лидеров, а лидерам нации
    def resolve_leaders_and_nations(self, leaders: LeadersStorage):
        i = 0
        for leader in leaders.leaders:
            if self.contains(leader.nationName):
                nation = self.nation(leader.nationName)
                nation.add_leader(leader)
                leader.nation = nation
            else:
                self.add_nation(Nation(i, leader.nationName))
                leader.nation = self.__nations[-1]
                i += 1

    # содержит ли список наицю по названию
    def contains(self, s: str):
        for i in self.__nations:
            if i.name == s:
                return True
        return False

    # получить нацию по названию
    def nation(self, s: str):
        for i in self.__nations:
            if i.name == s:
                return i

    # добавить нацию в список
    def add_nation(self, n: Nation):
        self.__nations.append(n)

    # получить список наций
    def get_nations(self):
        return self.__nations

    def get_serializable(self):
        d = dict()
        for i in self.__nations:
            d[i.id] = i.get_serializable()
        return d


nations_storage = NationsStorage()
nations_storage.resolve_leaders_and_nations(leadersStorage)
