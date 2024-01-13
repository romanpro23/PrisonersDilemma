import random
from abc import abstractmethod, ABC
from collections import deque


class Player(ABC):
    last_action: int
    memory: deque
    memory_size: int
    reward: int

    def __init__(self, memory_size=1):
        self.last_action = 1
        self.memory = deque(maxlen=memory_size)
        self.memory_size = memory_size
        self.reward = 0

    @abstractmethod
    def action(self):
        pass

    def remember(self, enemy_action):
        self.memory.append((self.last_action, enemy_action))
