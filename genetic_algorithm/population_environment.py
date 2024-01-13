import os

import torch

from genetic_algorithm.population import Population
from prisones_dilemma.stage import Stage


class Environment:
    population: Population
    stage: Stage

    def __init__(self, population: Population, stage: Stage):
        self.population = population
        self.stage = stage

    def survival(self, count_epoch):
        for epoch in range(count_epoch):
            for i in range(self.population.size):
                print('.', end="")
                for j in range(i, self.population.size):
                    reward1, reward2 = self.stage.battle(self.population.players[i], self.population.players[j])

                    self.population.fitness_players[i] += reward1
                    self.population.fitness_players[j] += reward2

            print()
            self.__save(epoch)
            self.population.crossover()

    def __save(self, epoch):
        path = f"brains/epoch_{epoch}"
        os.makedirs(path)
        for i, val in enumerate(self.population.fitness_players):
            torch.save(self.population.players[i].brain, f"{path}/nn_{val / self.population.size}")
