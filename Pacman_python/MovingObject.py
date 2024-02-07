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
        self._center = (x * board.factor + board.factor/2, y * board.factor + board.factor/2)
        self._radius = board.factor/2
        self._color = None
        self._direction = (0, 0)
        self._new_direction = (0, 0)
        self._current_tile = (x * board.factor, y * board.factor)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, cent):
        self._center = cent

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direct: "Direction"):
        self._direction = direct

    @property
    def new_direction(self):
        return self._new_direction

    @new_direction.setter
    def new_direction(self, new_direction: "Direction"):
        self._new_direction = new_direction

    @property
    def current_tile(self):
        return self._current_tile

    @current_tile.setter
    def current_tile(self, tile: tuple):
        self._current_tile = tile
    @abstractmethod
    def move(self):
        pass

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._center[0], self._center[1]), self._radius)


class Pacman(MovingObject):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)
        self._color = Colors.YELLOW

    def onKeyPressed(self, event_key: int):

        new_direction = Direction.map_from_event_key(event_key)

        # do sprawdzania czy tam gdzie chcemy pójść nie ma ściany
        tupla1 = (self._current_tile[0] + sign(new_direction[0]) * self._board.factor,
            self._current_tile[1] + sign(new_direction[1]) * self._board.factor)

        # tak samo jak wyżej, tylko żeby załapało kafelek wcześniej
        tupla2 = (tupla1[0] + sign(self._direction[0]) * self._board.factor,
            tupla1[1] + sign(self._direction[1]) * self._board.factor)

        # żeby łapało jeszcze chwilkę wcześniej
        tupla3 = (tupla1[0] + 2 * sign(self._direction[0]) * self._board.factor,
            tupla1[1] + 2 * sign(self._direction[1]) * self._board.factor)


        if tupla1 not in self._board.walls_xy or tupla2 not in self._board.walls_xy or tupla3 not in self._board.walls_xy:
            # print("changed")
            self._new_direction = new_direction

    def move(self):

        # print(self._position[0] % self._board.factor, self._position[1] % self._board.factor)
        new_direction = self._new_direction

        # skręcamy tylko w korytarze o szerokości board.factor
        if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
            # wtedy też zmienia się aktualny kafelek
            self._current_tile = self._position
            # to robi że nie staje na brzegach prostokąta (kiedy idziemy w prawo i klikniemy w górę to się zatrzmuje)
            if (self._position[0] + sign(new_direction[0]) * self._board.factor,
            self._position[1] + sign(new_direction[1]) * self._board.factor) not in self._board.walls_xy:
                self._direction = new_direction
            # self._direction = new_direction

        # kiedy już wszystko posprawdzaliśmy, zmieniamy pozycję pacmana
        if (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor) not in self._board.walls_xy:
            self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])
            self._center = (self._center[0] + self._direction[0], self._center[1] + self._direction[1])


class Ghost(MovingObject):

    def __init__(self, x: int, y: int, board: "Board"):#, strategy: "Strategy"):
        super().__init__(x, y, board)
        # self._strategy = strategy
        self._color = Colors.random_RGB()
        self._direction = Direction.random_direction("all")
        self._able_to_be_eaten = False
        self._how_long_it_can_be_eaten = 0

    @property
    def able_to_be_eaten(self) -> bool:
        return self._able_to_be_eaten

    @able_to_be_eaten.setter
    def able_to_be_eaten(self, value: bool):
        self._able_to_be_eaten = value

    @property
    def how_long_it_can_be_eaten(self) -> int:
        return self._how_long_it_can_be_eaten

    @how_long_it_can_be_eaten.setter
    def how_long_it_can_be_eaten(self, value: bool):
        self._how_long_it_can_be_eaten = value

    def move(self):
        if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
            self._current_tile = self._position
            # self._direction = self._strategy.next_direction()

        if (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor) not in self._board.walls_xy:
            self._position = (self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor)
            # self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])
