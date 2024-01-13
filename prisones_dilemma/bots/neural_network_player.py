import random
import torch.nn
import torch.nn as nn

from prisones_dilemma.player import Player


class LinearModel(nn.Module):
    def __init__(self, architecture: list):
        super(LinearModel, self).__init__()
        self.layers = nn.ModuleList()

        for input, output in zip(architecture[:-1], architecture[1:]):
            self.layers.append(nn.Linear(input, output))
            if output != architecture[-1]:
                self.layers.append(nn.ReLU())
            else:
                self.layers.append(nn.Sigmoid())

    def forward(self, x):
        if x.dtype == torch.int64:
            x = x.to(dtype=torch.float32)
        for layer in self.layers:
            x = layer(x)
        return x


class NeuralNetworkPlayer(Player):
    brain: LinearModel

    def __init__(self, memory_size=12, architecture=(24, 16, 8, 1), path=None, name="Neural network"):
        super().__init__(memory_size=memory_size, name=name)

        if path is None:
            self.brain = LinearModel(architecture)
        else:
            self.brain = torch.load(path)

    def action(self):
        self.last_action = int(torch.round(self.brain(torch.flatten(torch.tensor(self.memory)))))
        return self.last_action

    def load(self, path):
        self.brain = torch.load(path)
