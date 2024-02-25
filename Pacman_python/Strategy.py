# import pygame
from abc import ABC, abstractmethod
from Direction import Direction
from sign import *


# from MovingObject import MovingObject

# funkcja sign jest potrzebna, bo pacman w jednej klatce
# przesówa się o 5 pikseli, a my chcemy tylko wyłapać kierunek
def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


class Strategy(ABC):

    def _possible_directions(self, object_position: tuple, object_direction: tuple, board: "Board") -> list:
        directions = [x for x in Direction.ghost_possible_directions(object_direction)
                      if not board.is_wall_there((object_position[0] + sign(x[0]) * board.factor,
                                                  object_position[1] + sign(x[1]) * board.factor))]
        # if not board.is_wall_there((object_position[0] + sign(object_direction[0]) * board.factor,
        #                             object_position[1] + sign(object_direction[1]) * board.factor)):
        #     directions.append(object_direction)
        return directions

    @abstractmethod
    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board") -> tuple:
        pass


class RandomStrategy(Strategy):

    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
        possible_directions = self._possible_directions(object_position, object_direction, board)
        return Direction.random_direction(possible_directions)
        # return Direction.random_direction(Strategy._possible_directions(self, object_position, object_direction, board))


class RunAwayStrategy(Strategy):

    def _possible_directions(self, object_position: tuple, object_direction: tuple, board: "Board") -> list:
        directions = [x for x in Direction.ghost_possible_directions(
            (sign(object_direction[0]) * 5, sign(object_direction[1]) * 5))
                      if not board.is_wall_there((object_position[0] + sign(x[0]) * board.factor,
                                                  object_position[1] + sign(x[1]) * board.factor))]
        # if not board.is_wall_there((object_position[0] + sign(object_direction[0]) * board.factor,
        #                             object_position[1] + sign(object_direction[1]) * board.factor)):
        #     directions.append(object_direction)
        return directions

    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
        possible_directions = self._possible_directions(object_position, object_direction, board)
        direction = Direction.random_direction(possible_directions)
        return (sign(direction[0]) * 3, sign(direction[1]) * 3)
        # return Direction.random_direction(Strategy._possible_directions(self, object_position, object_direction, board))

# class FollowStrategy(Strategy):
#
#     def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
#
#         pacman_position = board.pacman.position
#         possible_directions = self._possible_directions(object_position, object_direction, board)
#
#         if object_position
#         return Direction.random_direction(possible_directions)
