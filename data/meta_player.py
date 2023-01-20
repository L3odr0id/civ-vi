from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.player import Player
    from data.leader import Leader


class MetaPlayer:
    def __init__(self, player: Player, leader: Leader):
        self.player: Player = player
        self.leader: Leader = leader

    def get_serializable(self):
        d = dict()
        d['player_id'] = self.player.id
        d['leader_id'] = self.leader.id
        return d
