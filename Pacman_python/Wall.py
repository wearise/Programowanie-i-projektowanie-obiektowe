import pygame
from Colors import Colors


class Wall:
    def __init__(self, x: int, y: int, board: "Board"):
        # self._board = board
        self._position = (x * board.factor, y * board.factor)
        self._color = Colors.BLUE
        self._rect = pygame.Rect(x * board.factor, y * board.factor, board.factor, board.factor)

    @property
    def position(self):
        return self._position

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.rect(screen, self._color, self._rect)