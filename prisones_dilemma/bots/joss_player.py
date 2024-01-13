import random

from prisones_dilemma.player import Player


class JossPlayer(Player):

    def __init__(self, memory_size=1, name="Joss"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = 0 if random.random() < 0.1 else abs(self.memory[-1][1])
        return self.last_action
