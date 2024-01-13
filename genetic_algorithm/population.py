import math
import os
import random
import torch

from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer


class Population:
    architecture: list
    input: int

    counter_population: int

    parents: list
    players: list

    mutation_rate: float

    parents_fitness: dict

    def __init__(self, size: int, input: int, architecture: list, mutation_rate=0.025):
        self.size = size
        self.input = input
        self.architecture = architecture

        self.players = [NeuralNetworkPlayer(input, architecture=architecture, name=f"GA #{i}") for i in range(size)]
        self.mutation_rate = mutation_rate

        self.counter_population = size

    def crossover(self, players_fitness: dict):
        sample = self.selection(players_fitness)

        new_players = []
        for _ in range(self.size):
            mother_name = random.choice(sample)
            father_name = random.choice(sample)

            mother = next((player for player in self.players if player.name == mother_name))
            father = next((player for player in self.players if player.name == father_name))

            child = self.__recombination(mother, father)
            new_players.append(child)

        self.parents = self.players
        self.players = new_players

    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __recombination(self, mother, father):
        child = NeuralNetworkPlayer(self.input, architecture=self.architecture, name=f"GA #{self.counter_population}")
        for child_param, mother_param, father_param \
                in zip(child.brain.parameters(), mother.brain.parameters(), father.brain.parameters()):
            self.__crossover(child_param, mother_param, father_param)
            self.__mutation(child_param)

        self.counter_population += 1
        return child

    def __crossover(self, child_param, mother_param, father_param):
        with torch.no_grad():
            mask = torch.rand_like(child_param) < 0.5
            child_param[mask] = mother_param[mask]
            child_param[~mask] = father_param[~mask]

    def __mutation(self, child_param):
        with torch.no_grad():
            mask = torch.rand_like(child_param) < self.mutation_rate
            max_value = torch.max(child_param)
            min_value = torch.min(child_param)
            range_value = max_value - min_value
            random_param = range_value * torch.rand_like(child_param) + min_value
            child_param[mask] = random_param[mask]

    def selection(self, fitness_players: dict):
        avg_fitness = sum(fitness for fitness in fitness_players.values()) / len(self.players)

        selection_sample = [name for name, fitness in fitness_players.items()
                            for _ in range(math.ceil(fitness * len(self.players) / avg_fitness))]
        return selection_sample

    def save(self, path, players_fitness: dict):
        os.makedirs(path)
        for name, fitness in players_fitness.items():
            player = next((player for player in self.players if player.name == name))
            torch.save(player.brain, f"{path}/{fitness}_{name}")
