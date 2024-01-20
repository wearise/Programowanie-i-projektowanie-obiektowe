from abc import ABC, abstractmethod
import pygame


class Object(ABC):

    def __init__(self, x: int, y: int, board: "Board"):
        self._board = board
        self._position = (x * board.factor, y * board.factor)
        # self._position = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._center = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._color = None

    @property
    def position(self):
        return self._position

    @abstractmethod
    def draw(self, screen: "pygame.surface.Surface"):
        pass
