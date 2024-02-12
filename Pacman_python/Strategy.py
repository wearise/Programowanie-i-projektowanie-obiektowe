# import pygame
from abc import ABC, abstractmethod
from Direction import Direction
from sign import *
# from MovingObject import MovingObject


class Strategy(ABC):
    
    def _possible_directions(self, object_position: tuple, object_direction: tuple, board: "Board") -> list:
        directions = [x for x in Direction.ghost_possible_directions(object_direction)
        if not board.is_wall_there((object_position[0] + sign(x[0]) * board.factor,
        object_position[1] + sign(x[1]) * board.factor))]
        if not board.is_wall_there((object_position[0] + sign(object_direction[0]) * board.factor,
                                    object_position[1] + sign(object_direction[1]) * board.factor)):
            directions.append(object_direction)
        return directions
    @abstractmethod
    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board") -> tuple:
        pass


class RandomStrategy(Strategy):

    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):

        possible_directions = self._possible_directions(object_position, object_direction, board)
        return Direction.random_direction(possible_directions)
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