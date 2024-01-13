import math
import random
import torch

from prisones_dilemma.bots.neural_network_player import NeuralNetworkPlayer


class Population:
    size: int
    old_population: list
    players: list
    mutation_rate: float

    fitness_players: list

    def __init__(self, size: int, mutation_rate=0.01):
        self.size = size
        self.players = [NeuralNetworkPlayer(5, input=10, hidden=[16, 8], output=1) for _ in range(size)]
        self.mutation_rate = mutation_rate

        self.fitness_players = [0] * self.size

    def crossover(self):
        sample = self.selection()
        new_population = []
        for _ in range(self.size):
            child = self.__recombination(self.players[random.choice(sample)], self.players[random.choice(sample)])
            new_population.append(child)

        self.old_population = self.players
        self.players = new_population
        self.fitness_players = [0] * self.size

    def __recombination(self, mother, father):
        child = NeuralNetworkPlayer(5, input=10, hidden=[16, 8], output=1)
        brain = child.brain
        for child_param, mother_param, father_param \
                in zip(brain.parameters(), mother.brain.parameters(), mother.brain.parameters()):
            self.__crossover(child_param, mother_param, father_param)
            self.__mutation(child_param)

        return child

    def __crossover(self, child_param, mother_param, father_param):
        with torch.no_grad():
            mask = torch.rand_like(child_param) < 0.5
            child_param[mask] = mother_param[mask]
            child_param[~mask] = father_param[~mask]

    def __crossover_onpnt(self, c, m, f):
        with torch.no_grad():
            rand_p = torch.randint(0, m.shape[0], (1,))
            mask = torch.cat([i < rand_p for i in range(m.shape[0])])
            c[mask] = m[mask]
            c[~mask] = f[~mask]

    def _crossover_avg(self, c, m, f):
        with torch.no_grad():
            c[...] = (m + f) / 2

    def __mutation(self, child_param):
        with torch.no_grad():
            mask = torch.rand_like(child_param) < self.mutation_rate
            max_value = torch.max(child_param)
            min_value = torch.min(child_param)
            range_value = max_value - min_value
            random_param = range_value * torch.rand_like(child_param) + min_value
            child_param[mask] = random_param[mask]

    def selection(self):
        avg_fitness = sum(self.fitness_players) / self.size
        selection_sample = [i for i, fitness in enumerate(self.fitness_players)
                            for _ in range(math.ceil(fitness / avg_fitness))]

        print(max(self.fitness_players) / self.size, min(self.fitness_players) / self.size)
        return selection_sample
