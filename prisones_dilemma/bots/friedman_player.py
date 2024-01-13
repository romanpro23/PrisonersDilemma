from prisones_dilemma.player import Player


class FriedmanPlayer(Player):
    play_false: bool

    def __init__(self, memory_size=2, name="Friedman"):
        super().__init__(memory_size=memory_size, name=name)

    def action(self):
        if not self.play_false and self.memory[-1][1] == 0:
            self.play_false = True
        self.last_action = 0 if self.play_false else 1
        return self.last_action

    def clear(self):
        super(FriedmanPlayer, self).clear()
        self.play_false = False
