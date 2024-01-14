from prisones_dilemma.player import Player

class Stage:
    """
    Represents a stage of battles in the "Prisoner's Dilemma" game between two players.
    """

    number_battles: int
    log_action: list

    def __init__(self, number_battles):
        """
        Initializes a stage with a specified number of battles.

        Parameters:
        - number_battles (int): Number of battles in the stage.
        """
        self.number_battles = number_battles
        self.log_action = []

    def battle(self, player1: Player, player2: Player):
        """
        Conducts a series of battles between two players and records the actions and rewards.

        Parameters:
        - player1 (Player): The first player.
        - player2 (Player): The second player.

        Returns:
        - tuple: A tuple containing the rewards for player1 and player2.
        """
        # Clear the log of actions and reset players' rewards and memories
        self.log_action.clear()
        player1.clear()
        player2.clear()

        # Conduct battles
        for _ in range(self.number_battles):
            action1 = player1.action()
            action2 = player2.action()

            # Remember each player's action for the next round
            player1.remember(action2)
            player2.remember(action1)

            # Log the actions for analysis or visualization purposes
            self.log_action.append((action1, action2))

            # Determine rewards based on the actions
            if action1 == action2:
                reward = 3 if action1 == 1 else 1
                player1.reward += reward
                player2.reward += reward
            elif action1 == 0:
                player1.reward += 5
            else:
                player2.reward += 5

        # Return the rewards for each player after the battles
        return player1.reward, player2.reward