import pygame
import os
from copy import deepcopy, copy
from abc import ABC, abstractmethod
from Dispatch import Dispatch
from Direction import Direction
from Strategy import RandomStrategy#, FollowStrategy
from Collisions import BigTreatCollision, GhostCollision
from MovingObject import Pacman, Ghost
from Wall import Wall
from Treats import Treat, BigTreat
from Colors import Colors


class Board:
    def __init__(self, board_file_txt, factor):
        self.__board_file = board_file_txt
        self.__factor = factor  # factor musi być podzielny na 5 (bo o 5 pikseli porzusza się w jednej klatce pacman)
        self.__length = None
        self.__width = None
        self.__walls = []
        self.__walls_xy = []
        self.__ghosts = []
        self.__treats = []
        self.__pacman = None
        self.grid = dict()

        with open(self.__board_file) as board_txt:

            line_number = 0
            for line in board_txt:
                n = 0
                for element in line:
                    # print(element)
                    if element == ' ':
                        self.__treats.append(Treat(n, line_number, self))
                    elif element == 't':
                        self.__treats.append(BigTreat(n, line_number, self))
                    elif element == '#':
                        self.__walls.append(Wall(n, line_number, self))
                        self.__walls_xy.append((n * self.__factor, line_number * self.__factor))
                        # self.__walls_xy.append((n * self.__factor + self.__factor // 2, line_number * self.__factor + self.__factor // 2))
                    elif element == 'g':
                        self.__ghosts.append(Ghost(n, line_number, self))
                    elif element == 'p':
                        self.__pacman = Pacman(n, line_number, self)
                    n += 1
                line_number += 1
            self.__length = (len(line) * self.__factor)
            self.__width = (line_number * self.__factor)

    @property
    def factor(self) -> int:
        return self.__factor

    @property
    def length(self) -> int:
        return self.__length

    @property
    def width(self) -> int:
        return self.__width

    @property
    def walls(self) -> list:
        return self.__walls

    @property
    def walls_xy(self) -> list:
        return self.__walls_xy

    @property
    def ghosts(self) -> list:
        return self.__ghosts

    def delete_ghost(self, ghost: "Ghost"):
        self.__ghosts.remove(ghost)

    @property
    def pacman(self) -> "Pacman":
        return self.__pacman

    @property
    def treats(self) -> list:
        return self.__treats

    def usun_smaczek(self, treat: "Treat"):
        self.__treats.remove(treat)

    def is_wall_there(self, position: tuple) -> bool:
        return self.__walls_xy.__contains__(position)