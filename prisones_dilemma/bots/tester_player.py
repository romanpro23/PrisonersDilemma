import random

from prisones_dilemma.player import Player


class TesterPlayer(Player):
    attack: bool
    apologize: bool

    def __init__(self, memory_size=2, name="Tester"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        if not self.apologize and self.memory[-2][0] == self.memory[-1][1] == 0:
            self.apologize = True

        if self.memory[-2][0] == 0 and self.memory[-1][1] == 1:
            self.attack = True

        self.last_action = 0 if self.attack else 1 if self.apologize else abs(self.memory[-1][1])
        self.attack = False

        return self.last_action

    def clear(self):
        super(TesterPlayer, self).clear()
        self.attack = True
        self.apologize = False
