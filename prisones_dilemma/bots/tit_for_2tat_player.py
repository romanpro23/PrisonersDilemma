import random

from prisones_dilemma.player import Player


class TitFor2TatPlayer(Player):

    def __init__(self, memory_size=2, name="TitFor2Tat"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = 0 if self.memory[-1][1] == self.memory[-2][1] == 0 else 1
        return self.last_action
