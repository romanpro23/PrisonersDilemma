from prisones_dilemma.stage import Stage


class Arena:
    players: list
    stage: Stage

    def __init__(self, stage):
        self.stage = stage

    def evaluate(self, players: list, number_repetitions: int = 1):
        players_score = {}
        for player in players:
            players_score[player.name] = 0

        for _ in range(number_repetitions):
            for i in range(len(players)):
                for j in range(i, len(players)):
                    reward1, reward2 = self.stage.battle(players[i], players[j])

                    players_score[players[i].name] += reward1
                    players_score[players[j].name] += reward2

        for player in players:
            players_score[player.name] = int(players_score[player.name] / (len(players) * number_repetitions))

        return players_score
