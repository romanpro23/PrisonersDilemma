import random
import torch.nn
import torch.nn as nn

from prisones_dilemma.player import Player


class LinearModel(nn.Module):
    def __init__(self, input, hidden=None, output=1):
        super(LinearModel, self).__init__()
        self.layers = nn.ModuleList()

        if hidden is not None:
            if isinstance(hidden, int):
                self.layers.append(nn.Linear(input, hidden))
                self.layers.append(nn.ReLU())
                self.layers.append(nn.Linear(hidden, output))
            elif isinstance(hidden, list):
                self.layers.append(nn.Linear(input, hidden[0]))
                self.layers.append(nn.ReLU())

                input = hidden[0]

                for count_neurons in hidden[1:]:
                    self.layers.append(nn.Linear(input, count_neurons))
                    self.layers.append(nn.ReLU())

                    input = count_neurons

                self.layers.append(nn.Linear(input, output))
        else:
            self.layers.append(nn.Linear(input, output))

        self.layers.append(nn.Sigmoid())

    def forward(self, x):
        if x.dtype == torch.int64:
            x = x.to(dtype=torch.float32)
        for layer in self.layers:
            x = layer(x)
        return x


class NeuralNetworkPlayer(Player):
    brain: LinearModel

    def __init__(self, memory_size=3, input=3 * 2, hidden=16, output=1):
        super().__init__(memory_size=memory_size)

        for _ in range(memory_size):
            self.memory.append((-1, -1))

        self.brain = LinearModel(input, hidden, output)

    def action(self):
        self.last_action = int(torch.round(self.brain(torch.flatten(torch.tensor(self.memory)))))
        return self.last_action
