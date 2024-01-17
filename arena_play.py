import os

from genetic_algorithm.population import Population
from prisones_dilemma.arena import Arena
from prisones_dilemma.bots.friedman_player import FriedmanPlayer
from prisones_dilemma.bots.graaskamp_player import GraaskampPlayer
from prisones_dilemma.bots.joss_player import JossPlayer
from prisones_dilemma.bots.noisy_tit_for_tat_player import NoisyTitForTatPlayer
from prisones_dilemma.bots.random_player import RandomPlayer
from prisones_dilemma.bots.tester_player import TesterPlayer
from prisones_dilemma.bots.tit_for_2tat_player import TitFor2TatPlayer
from prisones_dilemma.bots.tit_for_tat_player import TitForTatPlayer
from prisones_dilemma.stage import Stage

import matplotlib.pyplot as plt

# Create instances of different players
player1 = RandomPlayer()
player2 = TitForTatPlayer()
player3 = FriedmanPlayer()
player4 = TitFor2TatPlayer()
player5 = TesterPlayer()
player6 = NoisyTitForTatPlayer()
player7 = GraaskampPlayer()
player8 = JossPlayer()

# Create a population with a neural network architecture
population = Population(56, 12, [24, 1], mutation_rate=0.1, parents_probability=0.0)

# Create a stage for battles
stage = Stage(200)
arena = Arena(stage)

# Set the number of epochs for the genetic algorithm
count_epoch = 128

# Initial list of players
players = [player1, player2, player3, player4, player5, player6, player7, player8]

# Run the genetic algorithm for a specified number of epochs
for epoch in range(count_epoch):
    # Combine the initial players and the current population players
    players = [player1, player2, player3, player4, player5, player6, player7, player8]
    players.extend(population.players)

    # Evaluate the performance of players in the arena
    result = arena.evaluate(players, number_repetitions=1)

    # Extract scores for the population players
    population_result = {}
    for name, score in result.items():
        if name.startswith("GA"):
            population_result[name] = score

    # Save the neural network models for the population players
    population.save(f"brains/epoch_{epoch}", population_result)

    # Perform crossover operation in the genetic algorithm
    population.crossover(population_result)

    # Extract names and scores for the top players (excluding population players)
    names = []
    scores = []
    print(f"\nEpoch {epoch} ", end="")
    for name, score in sorted(result.items(), key=lambda item: -item[1])[:15]:
        names.append(name)
        scores.append(score)
        print(f"{name}: {score}", end=" ")

    # Plot a horizontal bar chart for the top players
    plt.barh(names[::-1], scores[::-1], color='lightblue')

    # Set plot details
    plt.title(f'Top players in the epoch {epoch + 1}')
    plt.xlabel('Names')
    plt.ylabel('Scores')

    # Save the bar chart as an image
    if not os.path.exists("diagrams"):
        os.makedirs("diagrams")
    plt.savefig(f"diagrams/Scores_epoch_{epoch + 1}")

    # Clear the plot for the next iteration
    plt.clf()
