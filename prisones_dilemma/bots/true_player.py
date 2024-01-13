import random

from prisones_dilemma.player import Player


class TruePlayer(Player):
    attack: bool

    def __init__(self, memory_size=1, name="True"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.last_action = 1
        return self.last_action
