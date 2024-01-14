from prisones_dilemma.bots.friedman_player import FriedmanPlayer
from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer
from prisones_dilemma.bots.tester_player import TesterPlayer
from prisones_dilemma.bots.tit_for_tat_player import TitForTatPlayer
from prisones_dilemma.bots.tit_for_2tat_player import TitFor2TatPlayer
from prisones_dilemma.bots.true_player import TruePlayer
from prisones_dilemma.stage import Stage

player1 = NeuralNetworkPlayer(6, path="brains/epoch_7/264_GA #169")
player2 = TitForTatPlayer()
player3 = FriedmanPlayer()
player4 = TitFor2TatPlayer()
player5 = TesterPlayer()
player6 = TruePlayer()

stage = Stage(200)

print(stage.battle(player3, player1))
print(stage.battle(player3, player4))
print(stage.battle(player1, player2))
print(stage.log_action)

print(stage.battle(player5, player6))
print(stage.log_action)

print(stage.battle(player5, player2))
print(stage.log_action)


