from enum import Enum

import pygame
import os
from copy import deepcopy, copy
from abc import ABC, abstractmethod
from Dispatch import Dispatch
from Direction import Direction
from Strategy import RandomStrategy, FollowStrategy
from MovingObject import Pacman, Ghost
from Wall import Wall
from Colors import Colors


class Board:
    def __init__(self, board_file_txt, factor):
        self.__board_file = board_file_txt
        self.__factor = factor
        self.__length = None
        self.__width = None
        self.__walls = []
        self.__walls_xy = []
        self.__ghosts = []
        self.__ghosts_xy = []
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
                        self.__walls.append(Wall(n * self.__factor, line_number * self.__factor, self))
                        self.__walls_xy.append((n * self.__factor, line_number * self.__factor))
                    if element == 'g':
                        self.__ghosts.append(Ghost(n * self.__factor, line_number * self.__factor, self))
                        self.__ghosts_xy.append((n * self.__factor, line_number * self.__factor))
                    if element == 'p':
                        self.__pacman = Pacman(n * self.__factor, line_number * self.__factor, self)
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
    def ghosts(self):
        return self.__ghosts

    @property
    def ghosts_xy(self):
        return self.__ghosts_xy

    @property
    def pacman(self):
        return self.__pacman

    @property
    def smaczki(self):
        return self.__smaczki

    def usun_smaczek(self, value):
        self.__smaczki.remove(value)


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':

    board = Board("board1.txt", 30)
    # with open("easy_board.txt") as board:
    screen = pygame.display.set_mode((board.length, board.width))
    clock = pygame.time.Clock()
    FPS = 20  # Frames per second.

    factor = board.factor
    pacman = board.pacman
    walls_xy = [wall.position for wall in board.walls]
    # a = []
    # print(type(a))
    # print(type(Direction.UP))
    # print(type(board.pacman))
    print(type(screen))

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
                # print(type(event.key))
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pacman.onKeyPressed(event.key)

        screen.fill(Colors.BLACK)
        pacman.move()

        for wall in board.walls:
            wall.draw(screen)

        for ghost in board.ghosts:
            ghost.draw(screen)

        # for j in range(len(board.ghosts_xy)):
        #     ghost = board.ghosts_xy[j]
        #     ghost_color = ghosts_colors[j]
        #
        #     pygame.draw.circle(screen, ghost_color, (ghost[0] + board.factor / 2, ghost[1] + board.factor / 2),
        #                        board.factor / 2)  # surface, color, center, radius

        for smaczek in board.smaczki:
            if smaczek == pacman.position:
                board.usun_smaczek(smaczek)
            pygame.draw.circle(screen, Colors.WHITE,
                               (smaczek[0] + factor / 2, smaczek[1] + factor / 2),
                               5)

        pacman.draw(screen)
        pygame.display.update()  # Or pygame.display.flip()

    pygame.quit()
