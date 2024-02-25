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
        return directions

    @abstractmethod
    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board") -> tuple:
        pass


class RandomStrategy(Strategy):

    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
        possible_directions = self._possible_directions(object_position, object_direction, board)
        return Direction.random_direction(possible_directions)


class FollowStrategy(Strategy):

    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
        pacman = board.pacman

        possible_directions = self._possible_directions(object_position, object_direction, board)

        x_axis_diff = pacman.position[0] - object_position[0]
        y_axis_diff = pacman.position[1] - object_position[1]

        new_directions_priority = [(sign(x_axis_diff), 0), (0, sign(y_axis_diff))]

        if abs(x_axis_diff) <= abs(y_axis_diff):
            new_directions_priority.reverse()

        for direction in new_directions_priority:
            if direction in possible_directions:
                return direction

        return Direction.random_direction(possible_directions)


class RunAwayStrategy(Strategy):
    def next_direction(self, object_position: tuple, object_direction: tuple, board: "Board"):
        pacman = board.pacman

        possible_directions = self._possible_directions(object_position, object_direction, board)

        x_axis_diff = pacman.position[0] - object_position[0]
        y_axis_diff = pacman.position[1] - object_position[1]

        new_directions_priority = [(sign(x_axis_diff), 0), (0, sign(y_axis_diff))]

        if abs(x_axis_diff) <= abs(y_axis_diff):
            new_directions_priority.reverse()

        for direction in new_directions_priority:
            if Direction.opposite_direction(direction) in possible_directions:
                return Direction.opposite_direction(direction)

        return Direction.random_direction(possible_directions)

