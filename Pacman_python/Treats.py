import pygame
from abc import ABC, abstractmethod
from Colors import Colors


class Treat(ABC):

    def __init__(self, x: int, y: int, board: "Board"):
        self._board = board
        self._position = (x * board.factor, y * board.factor)
        self._center = (x * board.factor + board.factor / 2, y * board.factor + board.factor / 2)
        self._radius = int(self.get_radius_factor() * self._board.factor)
        self._color = Colors.WHITE
        self._is_eaten = False

    @property
    def position(self):
        return self._position

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @property
    def is_eaten(self) -> bool:
        return self._is_eaten

    @abstractmethod
    def get_radius_factor(self) -> float:
        pass

    def eat(self):
        self._is_eaten = True

    def draw(self, screen: "pygame.surface.Surface"):
        if not self._is_eaten:
            pygame.draw.circle(screen, self._color,
                           (self._center[0], self._center[1]), self._radius)


class SmallTreat(Treat):

    def get_radius_factor(self) -> float:
        return 0.1


class BigTreat(Treat):

    def get_radius_factor(self) -> float:
        return 0.25
