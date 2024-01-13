from genetic_algorithm.population import Population
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

population = Population(16, 12, [24, 16, 8, 1], mutation_rate=0.1)

stage = Stage(200)
arena = Arena(stage)

count_epoch = 128

players = [player1, player2, player3, player4, player5, player6, player7, player8]

for epoch in range(count_epoch):
    players = [player1, player2, player3, player4, player5, player6, player7, player8]
    players.extend(population.players)

    result = arena.evaluate(players, number_repetitions=1)

    population_result = {}
    for name, score in result.items():
        if name.startswith("GA"):
            population_result[name] = score

    population.save(f"brains/epoch_{epoch}", population_result)
    population.crossover(population_result)

    for name, score in sorted(result.items(), key=lambda item: -item[1]):
        print(f"{name}: {score}", end="  ")
    print()
