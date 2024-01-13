from prisones_dilemma.player import Player


class Stage:
    number_battles: int
    log_action: list

    def __init__(self, number_battles):
        self.number_battles = number_battles
        self.log_action = []

    def battle(self, player1: Player, player2: Player):
        player1.reward = 0
        player2.reward = 0

        for _ in range(self.number_battles):
            action1 = player1.action()
            action2 = player2.action()

            player1.remember(action2)
            player2.remember(action1)

            # print(action1, action2)

            self.log_action.append((action1, action2))

            if action1 == action2:
                reward = 3 if action1 == 1 else 1

                player1.reward += reward
                player2.reward += reward
            elif action1 == 0:
                player1.reward += 5
            else:
                player2.reward += 5

        # print(f"Reward player №1: {player1.reward}")
        # print(f"Reward player №2: {player2.reward}")

        return player1.reward, player2.reward
