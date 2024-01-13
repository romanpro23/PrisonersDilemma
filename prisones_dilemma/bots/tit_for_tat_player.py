import random

from prisones_dilemma.player import Player


class TitForTatPlayer(Player):

    def __init__(self, memory_size=1, name="TitForTat"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = abs(self.memory[-1][1])
        return self.last_action
