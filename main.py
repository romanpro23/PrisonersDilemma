from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer
from prisones_dilemma.bots.random_player import RandomPlayer
from prisones_dilemma.bots.tit_for_tat_player import TitForTatPlayer
from prisones_dilemma.stage import Stage

player1 = NeuralNetworkPlayer()
player2 = TitForTatPlayer()

stage = Stage(200)

stage.battle(player1, player2)
