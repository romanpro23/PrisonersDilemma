from genetic_algorithm.population import Population
from genetic_algorithm.population_environment import Environment
from prisones_dilemma.bots.friedman_player import FriedmanPlayer
from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer
from prisones_dilemma.bots.random_player import RandomPlayer
from prisones_dilemma.bots.tester_player import TesterPlayer
from prisones_dilemma.bots.tit_for_tat_player import TitForTatPlayer
from prisones_dilemma.bots.tit_for_2tat_player import TitFor2TatPlayer
from prisones_dilemma.bots.true_player import TruePlayer
from prisones_dilemma.stage import Stage

player1 = NeuralNetworkPlayer(6, path="brains/epoch_3/nn_297.90625")
player2 = TitForTatPlayer()
player3 = FriedmanPlayer()
player4 = TitFor2TatPlayer()
player5 = TesterPlayer()
player6 = TruePlayer()
# player5 = NeuralNetworkPlayer(6, path="brains/epoch_1/nn_498.5")
# player6 = NeuralNetworkPlayer(6, path="brains/epoch_2/nn_354.6875")
# player7 = NeuralNetworkPlayer(6, path="brains/epoch_3/nn_254.6875")

stage = Stage(200)

print(stage.battle(player3, player1))
# print(stage.battle(player1, player5))
# print(stage.battle(player5, player6))
# print(stage.battle(player6, player7))
print(stage.battle(player3, player4))
print(stage.battle(player1, player2))
print(stage.log_action)

print(stage.battle(player5, player6))
print(stage.log_action)

print(stage.battle(player5, player2))
print(stage.log_action)


