import random

from prisones_dilemma.player import Player


class GraaskampPlayer(Player):
    counter_play_false: int

    def __init__(self, memory_size=2, name="Graaskamp"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        self.counter_play_false += 1
        if self.counter_play_false == 50:
            self.last_action = 0
        elif self.counter_play_false > 50 and self.memory[-1][1] == self.memory[-2][1] == 1:
            self.last_action = 0
        else:
            self.last_action = abs(self.memory[-1][1])
        return self.last_action

    def clear(self):
        super(GraaskampPlayer, self).clear()
        self.counter_play_false = 0
