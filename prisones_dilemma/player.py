import random
from abc import abstractmethod, ABC
from collections import deque


class Player(ABC):
    """
    Abstract base class for defining the structure of a player in the "Prisoner's Dilemma" game.
    """

    last_action: int
    memory: deque
    memory_size: int
    reward: int

    name: str

    def __init__(self, memory_size=1, name=None):
        """
        Initializes a player in the "Prisoner's Dilemma" game.

        Parameters:
        - memory_size (int): Size of the memory used to store past actions.
        - name (str): Optional name for the player.
        """
        self.last_action = 1  # Default initial action
        self.memory = deque(maxlen=memory_size)
        self.memory_size = memory_size
        self.name = name

        self.clear()

    @abstractmethod
    def action(self):
        """
        Abstract method representing the player's action in the "Prisoner's Dilemma" game.
        This method should be implemented by subclasses.

        Returns:
        - int: The player's action (0 or 1).
        """
        pass

    def remember(self, enemy_action):
        """
        Records the player's and the enemy's actions in the memory.

        Parameters:
        - enemy_action (int): The action taken by the opponent.
        """
        self.memory.append((self.last_action, enemy_action))

    def clear(self):
        """
        Clears the player's reward and initializes memory with default values.
        """
        self.reward = 0
        for _ in range(self.memory_size):
            self.memory.append((-1, -1))  # Default memory values for uninitialized actions
