from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from data.leader import Leader

class LeadersStorage:
    def __init__(self, leaders: List[Leader]):
        self.leaders: List[Leader] = leaders

    def leader(self, id: int):
        for leader in self.leaders:
            if leader.id == id:
                return leader
        return None

    def get_serializable(self):
        d = dict()
        for leader in self.leaders:
            d[leader.id] = leader.get_serializable()
        return d
