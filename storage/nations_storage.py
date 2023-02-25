from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.leaders_storage import LeadersStorage

from data.nation import Nation

# Хранилище наций
class NationsStorage:
    def __init__(self, nations: List[Nation]):
        self.nations: List[Nation] = []

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
