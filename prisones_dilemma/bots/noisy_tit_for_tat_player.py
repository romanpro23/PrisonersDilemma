import random

from prisones_dilemma.player import Player


class NoisyTitForTatPlayer(Player):

    def __init__(self, memory_size=1, name="NoisyTitForTat"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = random.randint(0, 1) if random.random() < 0.1 else abs(self.memory[-1][1])
        return self.last_action
