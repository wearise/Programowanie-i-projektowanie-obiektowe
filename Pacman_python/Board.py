from MovingObject import Pacman, Ghost
from Wall import Wall
from Treats import SmallTreat, BigTreat


class Board:
    def __init__(self, board_file_txt, factor):
        self.__board_file = board_file_txt
        self.__factor = factor  # factor musi być podzielny na 5 (bo o 5 pikseli porzusza się w jednej klatce pacman)
        self.__length = None
        self.__width = None
        self.__walls = []
        self.__walls_xy = []
        self._ghosts = []
        self.__treats = []
        self._pacman = None
        self.grid = dict()

        with open(self.__board_file) as board_txt:

            line_number = 0
            for line in board_txt:
                n = 0
                for element in line:

                    if element == ' ':
                        self.__treats.append(SmallTreat(n, line_number, self))
                    elif element == 't':
                        self.__treats.append(BigTreat(n, line_number, self))
                    elif element == '#':
                        self.__walls.append(Wall(n, line_number, self))
                    elif element == 'g':
                        self._ghosts.append(Ghost(n, line_number, self))
                    elif element == 'p':
                        self._pacman = Pacman(n, line_number, self)
                    n += 1
                line_number += 1

            self.__length = (len(line) * self.__factor)
            self.__width = (line_number * self.__factor)
            self.__walls_xy = [wall.position for wall in self.__walls]

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
        return self._ghosts

    @property
    def pacman(self) -> "Pacman":
        return self._pacman

    @property
    def treats(self) -> list:
        return self.__treats

    def usun_smaczek(self, treat: "Treat"):
        self.__treats.remove(treat)

    def is_wall_there(self, position: tuple) -> bool:
        return self.__walls_xy.__contains__(position)

    def are_all_treats_eaten(self) -> bool:
        # if sum([treat.is_eaten() for treat in self.__treats])/len(self.__treats) == 1
        #
        for treat in self.__treats:
            if not treat.is_eaten:
                return False
        return True

    def ghost_pacman_are_too_close(self, ghost: "Ghost") -> bool:
        if (abs(ghost.center[0] - self._pacman.center[0]) < ghost.radius + self._pacman.radius and
                abs(ghost.center[1] - self._pacman.center[1]) < ghost.radius + self._pacman.radius):
            return True

    def ghosts_no_able_to_be_eaten(self):
        for ghost in self._ghosts:
            ghost.how_long_it_can_be_eaten = 0

    def ghosts_restart_waiting(self):
        for ghost in self._ghosts:
            ghost.restart_waiting()

    def reset_objects_positions(self):
        self._pacman.reset_position()
        self._pacman.reset_directions()
        for ghost in self._ghosts:
            ghost.reset_position()
