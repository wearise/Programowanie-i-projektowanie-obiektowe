# import pygame
from abc import ABC, abstractmethod
# from MovingObject import MovingObject


class Strategy(ABC):

    def __init__(self, obj: "MovingObject"):
        self.obj = obj

    @abstractmethod
    def next_direction(self):
        pass


class RandomStrategy(Strategy):

    def __init__(self, obj: "MovingObject"):
        super().__init__(obj)
    def next_direction(self):
        pass


class FollowStrategy(Strategy):

    def next_direction(self):
        pass