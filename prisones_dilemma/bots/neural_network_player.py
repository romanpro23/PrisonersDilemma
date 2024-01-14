import random
import torch.nn
import torch.nn as nn

from prisones_dilemma.player import Player


class LinearModel(nn.Module):
    """
    Defines a linear neural network model using PyTorch's nn.Module.
    This model is specifically designed for the "Prisoner's Dilemma" game.

    Parameters:
    - architecture (list): List specifying the architecture of the neural network.
    """

    def __init__(self, architecture: list):
        super(LinearModel, self).__init__()
        self.layers = nn.ModuleList()

        # Construct the layers of the neural network based on the specified architecture
        for input, output in zip(architecture[:-1], architecture[1:]):
            self.layers.append(nn.Linear(input, output))

            # Add ReLU activation for hidden layers, and Sigmoid for the output layer
            if output != architecture[-1]:
                self.layers.append(nn.ReLU())
            else:
                self.layers.append(nn.Sigmoid())

    def forward(self, x):
        """
        Forward pass through the neural network.

        Parameters:
        - x: Input tensor.

        Returns:
        - torch.Tensor: Output tensor.
        """
        # Convert input to float32 if it's of type torch.int64
        if x.dtype == torch.int64:
            x = x.to(dtype=torch.float32)

        # Feed input through the layers of the neural network
        for layer in self.layers:
            x = layer(x)

        return x


class NeuralNetworkPlayer(Player):
    """
    Defines a player in the "Prisoner's Dilemma" game using a neural network.

    Parameters:
    - memory_size (int): Size of the memory used to store past actions.
    - architecture (tuple): Architecture of the neural network.
    - path (str): Optional path to load a pre-trained neural network model.
    - name (str): Optional name for the player.
    """
    brain: LinearModel

    def __init__(self, memory_size=12, architecture=(24, 16, 8, 1), path=None, name="Neural network"):
        super().__init__(memory_size=memory_size, name=name)

        # Initialize the neural network model
        if path is None:
            self.brain = LinearModel(architecture)
        else:
            # Load pre-trained model from the specified path
            self.brain = torch.load(path)

    def action(self):
        """
        Defines the player's action in the "Prisoner's Dilemma" game using the neural network.

        Returns:
        - int: The player's action (0 or 1).
        """
        # Perform forward pass through the neural network
        self.last_action = int(torch.round(self.brain(torch.flatten(torch.tensor(self.memory)))))
        return self.last_action

    def load(self, path):
        """
        Load a pre-trained neural network model from the specified path.

        Parameters:
        - path (str): Path to the pre-trained model.
        """
        self.brain = torch.load(path)