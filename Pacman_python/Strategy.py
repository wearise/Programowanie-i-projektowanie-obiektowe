# import pygame
from abc import ABC, abstractmethod
# from MovingObject import MovingObject


class Strategy(ABC):

    def __init__(self, obj: "MovingObject"):
        self._obj = obj

    @abstractmethod
    def next_direction(self):#, objects_position: tuple, list_of_walls: list):
        pass


class RandomStrategy(Strategy):

    def __init__(self, obj: "MovingObject"):
        super().__init__(obj)

    def next_direction(self):# w domyśle: , objects_position: tuple, list_of_walls: list):

        if self._obj.position == self._obj:
            pass


class FollowStrategy(Strategy):

    def next_direction(self):
        pass