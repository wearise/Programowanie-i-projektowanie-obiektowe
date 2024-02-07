import pygame
from abc import ABC
from Colors import Colors


class Treats(ABC):

    def __init__(self, x: int, y: int, board: "Board"):
        self._board = board
        self._position = (x * board.factor, y * board.factor)
        self._center = (x * board.factor + board.factor / 2, y * board.factor + board.factor / 2)
        self._radius = None
        self._color = Colors.WHITE

    @property
    def position(self):
        return self._position

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._center[0], self._center[1]), self._radius)


class Treat(Treats):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)
        self._radius = int(0.1 * self._board.factor)


class BigTreat(Treats):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)
        self._radius = int(0.25 * self._board.factor)
