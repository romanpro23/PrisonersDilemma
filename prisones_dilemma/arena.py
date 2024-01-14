from prisones_dilemma.stage import Stage

class Arena:
    """
    Represents an arena where players compete against each other in the "Prisoner's Dilemma" game.
    """

    players: list
    stage: Stage

    def __init__(self, stage):
        """
        Initializes an arena with a specified stage.

        Parameters:
        - stage (Stage): The stage where battles between players will take place.
        """
        self.stage = stage

    def evaluate(self, players: list, number_repetitions: int = 1):
        """
        Evaluates the performance of players in the arena through repeated battles.

        Parameters:
        - players (list): List of players participating in the arena.
        - number_repetitions (int): Number of repetitions for the evaluation.

        Returns:
        - dict: A dictionary containing the average scores of each player based on the evaluations.
        """
        # Initialize player scores
        players_score = {}
        for player in players:
            players_score[player.name] = 0

        # Repeat battles and update scores
        for _ in range(number_repetitions):
            for i in range(len(players)):
                for j in range(i, len(players)):
                    reward1, reward2 = self.stage.battle(players[i], players[j])

                    players_score[players[i].name] += reward1
                    players_score[players[j].name] += reward2

        # Calculate average scores for each player
        for player in players:
            players_score[player.name] = int(players_score[player.name] / (len(players) * number_repetitions))

        return players_score