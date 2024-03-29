import random

from prisones_dilemma.player import Player


class RandomPlayer(Player):

    def __init__(self, memory_size=1, name="Random"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = random.randint(0, 1)
        return self.last_action
