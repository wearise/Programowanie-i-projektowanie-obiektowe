import pygame
from abc import ABC, abstractmethod
from Colors import Colors


class Treats(ABC):

    def __init__(self, x: int, y: int, board: "Board"):
        self._board = board
        self._position = (x * board.factor, y * board.factor)
        # self._position = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._center = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._color = Colors.WHITE

    @property
    def position(self):
        return self._position

    @abstractmethod
    def draw(self, screen: "pygame.surface.Surface"):
        pass


class Treat(Treats):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._position[0] + self._board.factor / 2, self._position[1] + self._board.factor / 2),
                           int(0.1*self._board.factor))
        # pygame.draw.circle(screen, self._color,
        #                    (self._position[0], self._position[1]), int(0.1*self._board.factor))



class BigTreat(Treats):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._position[0] + self._board.factor / 2, self._position[1] + self._board.factor / 2),
                           int(0.25*self._board.factor))
        # pygame.draw.circle(screen, self._color,
        #                    (self._position[0], self._position[1]), int(0.25*self._board.factor))
