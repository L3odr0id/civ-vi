from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.leaders_storage import LeadersStorage

from data.nation import Nation

# Хранилище наций
class NationsStorage:
    def __init__(self):
        self.nations: List[Nation] = []

    # Всем нациям поставить в соответствие лидеров, а лидерам нации
    def resolve_leaders_and_nations(self, leaders: LeadersStorage):
        for leader in leaders.leaders:
            nation = self.nation(leader.nationName)

            if nation != None:
                nation.add_leader(leader)
                leader.nation = nation
            else:
                self.add_nation(Nation(leader.nationName))
                leader.nation = self.nations[-1]

    # получить нацию по названию
    def nation(self, nation_name: str) -> Nation | None :
        for nation in self.nations:
            if nation.name == nation_name:
                return nation
        return None

    # добавить нацию в список
    def add_nation(self, nation: Nation):
        self.nations.append(nation)

    # получить список наций
    def get_nations(self) -> List[Nation]:
        return self.nations

    def get_serializable(self):
        d = dict()
        for nation in self.nations:
            d[nation.id] = nation.get_serializable()
        return d
