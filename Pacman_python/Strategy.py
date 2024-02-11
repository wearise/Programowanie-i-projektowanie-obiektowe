# import pygame
from abc import ABC, abstractmethod
from Direction import Direction
from sign import *
# from MovingObject import MovingObject


class Strategy(ABC):

    def __init__(self, obj: "MovingObject"):
        self._obj = obj

    @abstractmethod
    def next_direction(self):#, objects_position: tuple, list_of_walls: list):
        # possible_directions = [x for x in Direction.ghost_possible_directions(self._direction)
        # if not self._obj.board.is_wall_there((self._obj.position[0] + sign(x[0]) * self._obj._board.factor,
        # self._position[1] + sign(x[1]) * self._board.factor))]
        # if not self._board.is_wall_there((self._position[0] + sign(self._direction[0]) * self._board.factor,
        #                                   self._position[1] + sign(self._direction[1]) * self._board.factor)):
        #     possible_directions.append(self._direction)
        # self._new_direction = Direction.random_direction(possible_directions)
        pass


class RandomStrategy(Strategy):

    def __init__(self, obj: "MovingObject"):
        super().__init__(obj)

    def next_direction(self):  # w domyśle: , objects_position: tuple, list_of_walls: list):

        if self._obj.position == self._obj:
            pass


class FollowStrategy(Strategy):

    def next_direction(self):
        pass