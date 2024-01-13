from genetic_algorithm.population import Population
from genetic_algorithm.population_environment import Environment
from prisones_dilemma.arena import Arena
from prisones_dilemma.bots.friedman_player import FriedmanPlayer
from prisones_dilemma.bots.graaskamp_player import GraaskampPlayer
from prisones_dilemma.bots.joss_player import JossPlayer
from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer
from prisones_dilemma.bots.noisy_tit_for_tat_player import NoisyTitForTatPlayer
from prisones_dilemma.bots.random_player import RandomPlayer
from prisones_dilemma.bots.tester_player import TesterPlayer
from prisones_dilemma.bots.tit_for_2tat_player import TitFor2TatPlayer
from prisones_dilemma.bots.tit_for_tat_player import TitForTatPlayer
from prisones_dilemma.bots.true_player import TruePlayer
from prisones_dilemma.stage import Stage

player1 = RandomPlayer()
player2 = TitForTatPlayer()
player3 = FriedmanPlayer()
player4 = TitFor2TatPlayer()
player5 = TesterPlayer()
player6 = NoisyTitForTatPlayer()
player7 = GraaskampPlayer()
player8 = JossPlayer()

players = [player1, player2, player3, player4, player5, player6, player7, player8]

stage = Stage(200)
arena = Arena(stage)

result = arena.evaluate(players, number_repetitions=5)

for name, score in sorted(result.items(), key=lambda item: -item[1]):
    print(f"{name}: {score}")
