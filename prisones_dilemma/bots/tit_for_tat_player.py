import random

from prisones_dilemma.player import Player


class TitForTatPlayer(Player):

    def __init__(self, memory_size=1):
        super().__init__(memory_size=memory_size)

    def action(self):
        self.last_action = 1 if len(self.memory) == 0 else self.memory[-1][1]
        return self.last_action
