import pygame
from abc import ABC, abstractmethod
from Strategy import Strategy
from Direction import Direction
from Colors import Colors
from Speed import Speed
from GhostPropertiesFactory import GhostPropertiesFactory, GhostProperties
from copy import copy


# funkcja sign jest potrzebna, bo pacman w jednej klatce
# przesówa się o 5 pikseli, a my chcemy tylko wyłapać kierunek
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
        self._starting_position = (x * board.factor, y * board.factor)
        self._center = (x * board.factor + board.factor/2, y * board.factor + board.factor/2)
        self._starting_center = (x * board.factor + board.factor/2, y * board.factor + board.factor/2)
        self._radius = board.factor/2
        self._color = None
        self._direction = (0, 0)
        self._new_direction = (0, 0)
        # self._starting_speed = board.factor // 6
        # self._speed = board.factor // 6
        self._speed = Speed(board.factor)
        self._current_tile = (x * board.factor, y * board.factor)
        self._waiting = 0

    @property
    def starting_position(self):
        return self._starting_position

    @property
    def starting_center(self):
        return self._starting_center

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos: tuple):
        self._position = pos

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, cent: tuple):
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

    # @property
    # def starting_speed(self):
    #     return self._starting_speed
    #
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: int):
        self._speed = new_speed

    @property
    def current_tile(self):
        return self._current_tile

    @current_tile.setter
    def current_tile(self, tile: tuple):
        self._current_tile = tile

    def reset_position(self):
        self._position = self._starting_position
        self._center = self.starting_center

    def move(self):

        # if not self._waiting:
        #     # żeby było bardziej przejrzyście
        #     new_direction = self._new_direction
        #
        #     # pacman porusza się cały czas w kierunku self._direction,
        #     # a skręcamy tylko w korytarze o szerokości board.factor -> self._direction = new_direction
        #     # wtedy też zmieniamy aktualny kafelek
        #     if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
        #         self._current_tile = self._position
        #         # to robi że nie staje na brzegach prostokąta (kiedy idziemy w prawo i klikniemy w górę to się zatrzmuje)
        #         if not self._board.is_wall_there((self._position[0] + sign(new_direction[0]) * self._board.factor,
        #         self._position[1] + sign(new_direction[1]) * self._board.factor)):
        #             self._direction = new_direction
        #         # self._direction = new_direction
        #
        #     # kiedy już wszystko posprawdzaliśmy, zmieniamy pozycję jego środka i samego pacmana
        #     if not self._board.is_wall_there((self._position[0] + sign(self._direction[0])*self._board.factor, self._position[1] + sign(self._direction[1])*self._board.factor)):
        #         self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])
        #         self._center = (self._center[0] + self._direction[0], self._center[1] + self._direction[1])
        if not self._waiting:
            # żeby było bardziej przejrzyście
            new_direction = self._new_direction

            # pacman porusza się cały czas w kierunku self._direction,
            # a skręcamy tylko w korytarze o szerokości board.factor -> self._direction = new_direction
            # wtedy też zmieniamy aktualny kafelek
            if self._position[0] % self._board.factor == 0 and self._position[1] % self._board.factor == 0:
                self._current_tile = self._position
                # to robi że nie staje na brzegach prostokąta (kiedy idziemy w prawo i klikniemy w górę to się zatrzmuje)
                if not self._board.is_wall_there((self._position[0] + new_direction[0] * self._board.factor,
                self._position[1] + new_direction[1] * self._board.factor)):
                    self._direction = new_direction
                    self._speed.update_speed()
                # self._direction = new_direction

            # kiedy już wszystko posprawdzaliśmy, zmieniamy pozycję jego środka i samego pacmana
            if not self._board.is_wall_there((self._position[0] + self._direction[0]*self._board.factor, self._position[1] + self._direction[1]*self._board.factor)):
                self._position = (self._position[0] + self._direction[0] * self._speed.speed, self._position[1] + self._direction[1] * self._speed.speed)
                self._center = (self._center[0] + self._direction[0] * self._speed.speed, self._center[1] + self._direction[1] * self._speed.speed)

    def draw(self, screen: "pygame.surface.Surface"):
        pygame.draw.circle(screen, self._color,
                           (self._center[0], self._center[1]), self._radius)


class Pacman(MovingObject):

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__(x, y, board)
        self._color = Colors.YELLOW
        self._lives = 3  # _lives: int = 3

    @property
    def lives(self):
        return self._lives

    def life_lost(self):
        self._lives -= 1

    def reset_directions(self):
        self._direction = (0,0)
        self._new_direction = (0,0)

    def onKeyPressed(self, event_key: int):

        # tutaj ustawiam tylko zapisywanie przyciśniętego klawisza,
        # nie zmienia to od razu kierunku poruszania się pacmana
        new_direction = Direction.map_from_event_key(event_key)

        # zapisuję zmienną lokalną new_direction do pola pacmana tylko wtedy kiedy to ma rzeczywiście sens,
        # czyli kiedy tam gdzi chcemy pójść rzeczywiście nie ma ściany

        # kafelek zmienia się kiedy znajdzie się w nim cały pacman i jest szerokości board.facor,
        # tworzę tuple pomocnicze, tupla1 - sprawdzam czy kafelek w tę stronę gdzie chcemy pójść
        # nie jest "w ścianach"
        tupla1 = (self._current_tile[0] + new_direction[0] * self._board.factor,
            self._current_tile[1] + new_direction[1] * self._board.factor)

        # tak samo jak wyżej, tylko żeby załapało kafelek wcześniej
        tupla2 = (tupla1[0] + self._direction[0] * self._board.factor,
            tupla1[1] + self._direction[1] * self._board.factor)

        # wersja dla gapiów - dwa kafelki wcześniej
        tupla3 = (tupla1[0] + 2 * self._direction[0] * self._board.factor,
            tupla1[1] + 2 * self._direction[1] * self._board.factor)

        # wykorzystuję wcześniej utworzone tuple i sprawdzam czy faktycznie tam gdzie chcę pójśc nie ma ścian
        # if tupla1 not in self._board.walls_xy or tupla2 not in self._board.walls_xy or tupla3 not in self._board.walls_xy:
        if not self._board.is_wall_there(tupla1) or not self._board.is_wall_there(tupla2) or not self._board.is_wall_there(tupla3):
            # print("changed")
            self._new_direction = new_direction


class Ghost(MovingObject):

    def __init__(self, x: int, y: int, board: "Board", strategy: "Strategy"):
        super().__init__(x, y, board)
        ghost_properties = GhostPropertiesFactory.get_ghost_properties()
        self._main_strategy = ghost_properties.strategy
        self._strategy = ghost_properties.strategy
        self._color = ghost_properties.color
        self._initial_waiting = ghost_properties.waiting
        self._waiting = ghost_properties.waiting
        self._direction = Direction.random_direction(
            [x for x in Direction.all_directions
             if not self._board.is_wall_there((self._position[0] + sign(x[0])*self._board.factor, self._position[1] + sign(x[1])*self._board.factor))])
        self._how_long_it_can_be_eaten = 0

    def restart_waiting(self):
        self._waiting = self._initial_waiting

    @property
    def waiting(self) -> int:
        return self._waiting

    @waiting.setter
    def waiting(self, value: int):
        self._waiting = value

    @property
    def main_strategy(self) -> Strategy:
        return self._main_strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strat: Strategy):
        self._strategy = strat

    @property
    def how_long_it_can_be_eaten(self) -> int:
        return self._how_long_it_can_be_eaten

    @how_long_it_can_be_eaten.setter
    def how_long_it_can_be_eaten(self, value: int):
        self._how_long_it_can_be_eaten = value

    def set_direction(self):

        self._new_direction = self._strategy.next_direction(self._position, self._direction, self._board)

