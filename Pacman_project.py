from enum import Enum

import pygame  # as pg
import os
from copy import deepcopy, copy
from abc import ABC, abstractmethod


class Board:
    def __init__(self, board_file_txt, factor):
        self.__board_file = board_file_txt
        self.__factor = factor
        self.__length = None
        self.__width = None
        self.__walls = []
        self.__walls_xy = []
        self.__ghosts_xy = []
        self.__pacman_xy = None
        self.__smaczki = []
        self.__pacman = None

        with open(self.__board_file) as board_txt:

            line_number = 0
            for line in board_txt:
                n = 0
                for element in line:
                    # print(element)
                    if element == ' ':
                        self.__smaczki.append((n * self.__factor, line_number * self.__factor))
                    if element == '#':
                        self.__walls.append(pygame.Rect(n * self.__factor, line_number * self.__factor, self.__factor, self.__factor))
                        self.__walls_xy.append((n * self.__factor, line_number * self.__factor))
                    if element == 'g':
                        self.__ghosts_xy.append((n * self.__factor, line_number * self.__factor))
                    if element == 'p':
                        self.__pacman_xy = (n * self.__factor, line_number * self.__factor)
                        self.__pacman = Pacman()
                    n += 1
                line_number += 1
            self.__length = (len(line) * self.__factor)
            self.__width = (line_number * self.__factor)

    @property
    def factor(self):
        return self.__factor

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def walls(self):
        return self.__walls

    @property
    def walls_xy(self):
        return self.__walls_xy

    @property
    def ghosts_xy(self):
        return self.__ghosts_xy

    @property
    def pacman_xy(self):
        return self.__pacman_xy

    @pacman_xy.setter
    def pacman_xy(self, value: tuple):
        self.__pacman_xy = value

    @property
    def pacman(self):
        return self.__pacman

    def pacman_move(self):
        # a = self.__pacman.direction[0]
        if (self.__pacman_xy[0] + sign(self.__pacman.direction[0])*self.__factor, self.__pacman_xy[1] + sign(self.__pacman.direction[1])*self.__factor) not in self.__walls_xy:
            self.__pacman_xy = (self.__pacman_xy[0] + sign(self.__pacman.direction[0])*self.__factor, self.__pacman_xy[1] + sign(self.__pacman.direction[1])*self.__factor)

    @property
    def smaczki(self):
        return self.__smaczki

    def usun_smaczek(self, value):
        self.__smaczki.remove(value)
class Direction:
    LEFT = (-5, 0)  # (-board.factor, 0)
    RIGHT = (5, 0)
    UP = (0, -5)
    DOWN = (0, 5)

    @staticmethod
    def random_direction():
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        if x < 0.25:
            return Direction.LEFT

        elif x < 0.5:
            return Direction.RIGHT

        elif x < 0.75:
            return Direction.UP

        else:
            return Direction.DOWN


class MovingObject(ABC):
    # def __init__(self, x: int, y: int):
    #     self.__position = (y, x)
    def __init__(self):
        self.__color = None
        self.__direction = (0, 0)

    @property
    def direction(self):
        return self.__direction

    # @abstractmethod
    # def change_direction(self, key_of_event):
    #     pass

    @direction.setter
    def direction(self, direction: "Direction"):
        self.__direction = direction


class Pacman(MovingObject):

    def __init__(self):  # , x: int, y: int):
        super().__init__()  # x, y)
        self.__color = Colors.YELLOW


class Ghost(MovingObject):

    def __init__(self):  # , x: int, y: int):
        super().__init__()  # x, y)
        self.__color = Colors.random_RGB()
        self.__direction = Direction.random_direction()

# # def change_direction(self, key_of_event):


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MINT = (int(0.667 * 255), int(0.941 * 255), int(0.82 * 255))

    @staticmethod
    def random_RGB() -> (int, int, int):
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        if x < 0.33:
            return Colors.RED

        elif x < 0.66:
            return Colors.GREEN

        else:
            return Colors.MINT
def sign(n):
    if n<0: return -1
    elif n>0: return 1
    else: return 0

if __name__ == '__main__':

    board = Board("board1.txt", 30)
    # with open("easy_board.txt") as board:
    screen = pygame.display.set_mode((board.length, board.width))
    clock = pygame.time.Clock()
    FPS = 10  # Frames per second.
    factor = board.factor

    # a = []
    # print(type(a))
    # print(type(Direction.UP))
    # print(type(board.pacman))

    hh = True

    Game = True
    while Game:
        clock.tick(FPS)

        # while hh:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             hh = False
        #
        #         if event.type == pygame.KEYDOWN:
        #
        #             if event.key == pygame.K_LEFT:
        #                 board.pacman.direction = Direction.LEFT
        #                 hh = False
        #
        #             if event.key == pygame.K_RIGHT:
        #                 board.pacman.direction = Direction.RIGHT
        #                 hh = False
        #
        #             if event.key == pygame.K_UP:
        #                 board.pacman.direction = Direction.UP
        #                 hh = False
        #
        #             if event.key == pygame.K_DOWN:
        #                 board.pacman.direction = Direction.DOWN
        #                 hh = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    direction = Direction.LEFT
                    if (board.pacman_xy[0] + sign(direction[0]) * factor,
                        board.pacman_xy[1] + sign(direction[1]) * factor) not in board.walls_xy:
                        board.pacman.direction = direction

                if event.key == pygame.K_RIGHT:
                    direction = Direction.RIGHT
                    if (board.pacman_xy[0] + sign(direction[0]) * factor,
                        board.pacman_xy[1] + sign(direction[1]) * factor) not in board.walls_xy:
                        board.pacman.direction = direction

                if event.key == pygame.K_UP:
                    direction = Direction.UP
                    if (board.pacman_xy[0] + sign(direction[0]) * factor,
                        board.pacman_xy[1] + sign(direction[1]) * factor) not in board.walls_xy:
                        board.pacman.direction = direction

                if event.key == pygame.K_DOWN:
                    direction = Direction.DOWN
                    if (board.pacman_xy[0] + sign(direction[0]) * factor,
                        board.pacman_xy[1] + sign(direction[1]) * factor) not in board.walls_xy:
                        board.pacman.direction = direction

        screen.fill(Colors.BLACK)
        board.pacman_move()


        for wall in board.walls:
            # rect = pygame.Rect(wall[0], wall[1], board.factor, board.factor)
            pygame.draw.rect(screen, Colors.BLUE, wall)

        # for j in range(len(board.ghosts_xy)):
        #     ghost = board.ghosts_xy[j]
        #     ghost_color = ghosts_colors[j]
        #
        #     pygame.draw.circle(screen, ghost_color, (ghost[0] + board.factor / 2, ghost[1] + board.factor / 2),
        #                        board.factor / 2)  # surface, color, center, radius

        for smaczek in board.smaczki:
            if smaczek == board.pacman_xy:
                board.usun_smaczek(smaczek)
            pygame.draw.circle(screen, Colors.WHITE,
                               (smaczek[0] + factor / 2, smaczek[1] + factor / 2),
                               5)

        pygame.draw.circle(screen, Colors.YELLOW,
                           (board.pacman_xy[0] + board.factor / 2, board.pacman_xy[1] + board.factor / 2),
                           board.factor / 2)

        pygame.display.update()  # Or pygame.display.flip()

    pygame.quit()
