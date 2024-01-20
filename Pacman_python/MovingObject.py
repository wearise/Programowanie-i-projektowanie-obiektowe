import pygame
from abc import ABC, abstractmethod
from Strategy import Strategy
from Direction import Direction
from Colors import Colors
from copy import copy


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


class MovingObject(ABC):
    def __init__(self, x: int, y: int, board: "Board"):
        self._board = board
        self._position = (x * board.factor, y * board.factor)
        # self._position = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._center = (x * board.factor + board.factor//2, y * board.factor + board.factor//2)
        self._color = None
        self._direction = (0, 0)
        self._current_tile = (x * board.factor, y * board.factor)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direct: "Direction"):
        self._direction = direct

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos

    @property
    def color(self):
        return self._color

    # @color.setter
    # def color(self, col: "Colors"):
    #     self._color = col

    @property
    def current_tile(self):
        return self._current_tile

    @current_tile.setter
    def current_tile(self, tile: tuple):
        self._current_tile = tile
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self, screen: "pygame.surface.Surface"):
        pass



class Pacman(MovingObject):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)
        self._color = Colors.YELLOW
        self._new_direction = copy(self._direction)

    @property
    def new_direction(self):
        return self._new_direction

    @new_direction.setter
    def new_direction(self, new_direction: "Direction"):
        self._new_direction = new_direction

    def onKeyPressed(self, event_key: int):

        # self._new_direction = Direction.map_from_event_key(event_key)

        new_direction = Direction.map_from_event_key(event_key)

        tupla1 = (self._current_tile[0] + sign(new_direction[0]) * self._board.factor,
            self._current_tile[1] + sign(new_direction[1]) * self._board.factor)

        tupla2 = (tupla1[0] + sign(self._direction[0]) * self._board.factor,
            tupla1[1] + sign(self._direction[1]) * self._board.factor)

        tupla3 = (tupla1[0] + 2 * sign(self._direction[0]) * self._board.factor,
            tupla1[1] + 2 * sign(self._direction[1]) * self._board.factor)


        if tupla1 not in self._board.walls_xy or tupla2 not in self._board.walls_xy or tupla3 not in self._board.walls_xy:
            self._new_direction = new_direction

        # for ghost in ghosts:
        #     if pacman.position != ghost.position:
        #         do it
        #
        #
        #
        # Collisions = Dispatch{(Pacman,Ghost): function}
        #
        # if pacman.position in list(slownik.keys):
        #     #slownik[pacman.position] -> Ghost
        #     Collisions[(Pacman,slownik[pacman.position])]


    def move(self):

        new_direction = self._new_direction

        if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
            self._current_tile = self._position

            if (self._position[0] + sign(new_direction[0]) * self._board.factor,
            self._position[1] + sign(new_direction[1]) * self._board.factor) not in self._board.walls_xy:
                self._direction = new_direction

        if (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor) not in self._board.walls_xy:
            self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._position[0] + self._board.factor / 2, self._position[1] + self._board.factor / 2),
                           self._board.factor / 2)
        # pygame.draw.circle(screen, self._color,
        #                    (self._position[0], self._position[1]), self._board.factor / 2)


class Ghost(MovingObject):

    def __init__(self, x: int, y: int, board: "Board"):#, strategy: "Strategy"):
        super().__init__(x, y, board)
        # self._strategy = strategy
        self._color = Colors.random_RGB()
        self._direction = Direction.random_direction()

    def move(self):
        if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
            self._current_tile = self._position
            # self._direction = self._strategy.next_direction()

        if (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor) not in self._board.walls_xy:
            self._position = (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor)
            # self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._position[0] + self._board.factor / 2, self._position[1] + self._board.factor / 2),
                           self._board.factor / 2)
        # pygame.draw.circle(screen, self._color,
        #                    (self._position[0], self._position[1]), self._board.factor / 2)

