from genetic_algorithm.population import Population
from prisones_dilemma.stage import Stage


class Environment:
    population: Population
    stage: Stage

    def __init__(self, population: Population, stage: Stage):
        self.population = population
        self.stage = stage

    def survival(self, count_epoch):
        for _ in range(count_epoch):
            for i in range(self.population.size):
                print('.', end="")
                for j in range(self.population.size):
                    reward1, reward2 = self.stage.battle(self.population.players[i], self.population.players[j])

                    self.population.fitness_players[i] += reward1
                    self.population.fitness_players[j] += reward2

            print()
            self.population.crossover()
