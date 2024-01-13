import random
from abc import abstractmethod, ABC
from collections import deque


class Player(ABC):
    last_action: int
    memory: deque
    memory_size: int
    reward: int

    name: str

    def __init__(self, memory_size=1, name=None):
        self.last_action = 1
        self.memory = deque(maxlen=memory_size)
        self.memory_size = memory_size
        self.name = name

        self.clear()

    @abstractmethod
    def action(self):
        pass

    def remember(self, enemy_action):
        self.memory.append((self.last_action, enemy_action))

    def clear(self):
        self.reward = 0
        for _ in range(self.memory_size):
            self.memory.append((-1, -1))
