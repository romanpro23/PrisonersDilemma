import math
import os
import random
import torch

from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer

class Population:
    """
    Represents a population of NeuralNetworkPlayer instances evolving over generations.
    Implements genetic algorithm operations such as crossover, mutation, and selection.
    """

    architecture: list
    input: int

    counter_population: int

    parents: list
    players: list

    mutation_rate: float

    parents_fitness: dict

    def __init__(self, size: int, input: int, architecture: list, mutation_rate=0.025):
        """
        Initializes a population of NeuralNetworkPlayers.

        Parameters:
        - size (int): Size of the population.
        - input (int): Number of input nodes for the neural network.
        - architecture (list): List specifying the architecture of the neural network.
        - mutation_rate (float): Rate of mutation for genetic algorithm operations.
        """
        # Initialize the Population
        self.size = size
        self.input = input
        self.architecture = architecture

        # Create a list of NeuralNetworkPlayer instances as the population
        self.players = [NeuralNetworkPlayer(input, architecture=architecture, name=f"GA #{i}") for i in range(size)]
        self.mutation_rate = mutation_rate

        # Counter to keep track of the population
        self.counter_population = size

    def crossover(self, players_fitness: dict):
        """
        Performs crossover operation to create a new generation of NeuralNetworkPlayers.

        Parameters:
        - players_fitness (dict): Dictionary containing the fitness scores of players in the current generation.
        """
        sample = self.selection(players_fitness)

        new_players = []
        for _ in range(self.size):
            mother_name = random.choice(sample)
            father_name = random.choice(sample)

            # Select mother and father based on their names
            mother = next((player for player in self.players if player.name == mother_name))
            father = next((player for player in self.players if player.name == father_name))

            # Create a child using recombination of mother and father
            child = self.__recombination(mother, father)
            new_players.append(child)

        # Update the current generation's parents and players
        self.parents = self.players
        self.players = new_players

    def get_player(self, name):
        """
        Retrieves a player from the population based on their name.

        Parameters:
        - name (str): Name of the player to retrieve.

        Returns:
        - NeuralNetworkPlayer: The requested player.
        """
        for player in self.players:
            if player.name == name:
                return player

    def __recombination(self, mother, father):
        """
        Recombines the parameters of mother and father to create a new NeuralNetworkPlayer.

        Parameters:
        - mother (NeuralNetworkPlayer): Mother player.
        - father (NeuralNetworkPlayer): Father player.

        Returns:
        - NeuralNetworkPlayer: The child player created through recombination.
        """
        child = NeuralNetworkPlayer(self.input, architecture=self.architecture, name=f"GA #{self.counter_population}")
        for child_param, mother_param, father_param \
                in zip(child.brain.parameters(), mother.brain.parameters(), father.brain.parameters()):
            self.__crossover(child_param, mother_param, father_param)
            self.__mutation(child_param)

        # Increment the population counter
        self.counter_population += 1
        return child

    def __crossover(self, child_param, mother_param, father_param):
        """
        Performs crossover operation on the parameters of mother and father.

        Parameters:
        - child_param (torch.Tensor): Parameters of the child player.
        - mother_param (torch.Tensor): Parameters of the mother player.
        - father_param (torch.Tensor): Parameters of the father player.
        """
        with torch.no_grad():
            mask = torch.rand_like(child_param) < 0.5
            child_param[mask] = mother_param[mask]
            child_param[~mask] = father_param[~mask]

    def __mutation(self, child_param):
        """
        Introduces mutation to the parameters.

        Parameters:
        - child_param (torch.Tensor): Parameters of the child player.
        """
        with torch.no_grad():
            mask = torch.rand_like(child_param) < self.mutation_rate
            max_value = torch.max(child_param)
            min_value = torch.min(child_param)
            range_value = max_value - min_value
            random_param = range_value * torch.rand_like(child_param) + min_value
            child_param[mask] = random_param[mask]

    def selection(self, fitness_players: dict):
        """
        Performs selection of players based on their fitness.

        Parameters:
        - fitness_players (dict): Dictionary containing the fitness scores of players.

        Returns:
        - list: A sample of player names based on their fitness for use in crossover.
        """
        avg_fitness = sum(fitness for fitness in fitness_players.values()) / len(self.players)

        # Create a selection sample based on fitness
        selection_sample = [name for name, fitness in fitness_players.items()
                            for _ in range(math.ceil(fitness * 10 / avg_fitness))]
        return selection_sample

    def save(self, path, players_fitness: dict):
        """
        Saves the NeuralNetworkPlayer instances to files.

        Parameters:
        - path (str): Directory path to save the players.
        - players_fitness (dict): Dictionary containing the fitness scores of players.
        """
        if not os.path.exists(path):
            os.makedirs(path)
        for name, fitness in players_fitness.items():
            player = next((player for player in self.players if player.name == name))
            torch.save(player.brain, f"{path}/{fitness}_{name}")