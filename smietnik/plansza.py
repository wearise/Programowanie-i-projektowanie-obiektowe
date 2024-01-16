import pygame  # as pg
import os
from copy import deepcopy, copy
from abc import ABC, abstractmethod

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


class Board:
    def __init__(self, factor):
        self.__factor = factor
        self.__length = None
        self.__width = None
        self.__walls = []
        self.__ghosts_xy = []
        self.__pacman_xy = None

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, value):
        self.__factor = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def walls(self):
        return self.__walls

    def add_wall(self, x: int, y: int):
        self.__walls.append((y,x))

    @property
    def ghosts_xy(self):
        return self.__ghosts_xy

    def add_ghost_xy(self, x: int, y: int):
        self.__ghosts_xy.append((y,x))

    @property
    def pacman_xy(self):
        return self.__pacman_xy

    @pacman_xy.setter
    def pacman_xy(self, value: tuple):
        self.__pacman_xy = value


# class Strategy:
#     def __init__(self):

class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MINT = (int(0.667*255), int(0.941*255), int(0.82*255))

    @staticmethod
    def random_RGB() -> (int, int, int):
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        if x < 0.33:
            return Colors.RED

        elif x < 0.66:
            return Colors.GREEN

        else:
            return Colors.MINT


if __name__ == '__main__':

    board = Board(30)
    # with open("easy_board.txt") as board:
    with open("../Pacman_python/board1.txt") as board_txt:
        # print(board.read())

        line_number = 0
        for line in board_txt:
            n = 0
            for element in line:
                # print(element)
                if element == '#':
                    board.add_wall(line_number * board.factor, n * board.factor)
                elif element == 'g':
                    board.add_ghost_xy(line_number * board.factor, n * board.factor)
                elif element == 'p':
                    board.pacman_xy = (line_number * board.factor, n * board.factor)
                n += 1
            line_number += 1
            # tokens = line.split()
        board.length = (len(line) * board.factor)
        board.width = (line_number * board.factor)

    # Board.walls = Board.walls[:2]
    print(board.walls)
    print(board.ghosts_xy)
    print(board.pacman_xy)
    print((board.length, board.width))

    screen = pygame.display.set_mode((board.length, board.width))
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.

    ghosts_colors = []
    for ghost in board.ghosts_xy:
        ghosts_colors.append(Colors.random_RGB())

    print(ghosts_colors)

    # set the pygame window name
    pygame.display.set_caption('Show Text')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('GeeksForGeeks', True, Colors.GREEN, Colors.MINT)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (board.length//2, board.width//2)

    Game = True
    while Game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if (board.pacman_xy[0] - board.factor, board.pacman_xy[1]) not in board.walls:
                        board.pacman_xy = (board.pacman_xy[0] - board.factor, board.pacman_xy[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if (board.pacman_xy[0] + board.factor, board.pacman_xy[1]) not in board.walls:
                        board.pacman_xy = (board.pacman_xy[0] + board.factor, board.pacman_xy[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if (board.pacman_xy[0], board.pacman_xy[1] - board.factor) not in board.walls:
                        board.pacman_xy = (board.pacman_xy[0], board.pacman_xy[1] - board.factor)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if (board.pacman_xy[0], board.pacman_xy[1] + board.factor) not in board.walls:
                        board.pacman_xy = (board.pacman_xy[0], board.pacman_xy[1] + board.factor)

        screen.fill(Colors.BLACK)
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.


        for wall in board.walls:
            rect = pygame.Rect(wall[0], wall[1], board.factor, board.factor)
            pygame.draw.rect(screen, Colors.BLUE, rect)

        for j in range(len(board.ghosts_xy)):
            ghost = board.ghosts_xy[j]
            ghost_color = ghosts_colors[j]

            pygame.draw.circle(screen, ghost_color, (ghost[0] + board.factor / 2, ghost[1] + board.factor / 2),
                               board.factor / 2)  # surface, color, center, radius

        pygame.draw.circle(screen, Colors.YELLOW,
                           (board.pacman_xy[0] + board.factor / 2, board.pacman_xy[1] + board.factor / 2),
                           board.factor / 2)
        screen.blit(text, textRect)
        pygame.display.update()  # Or pygame.display.flip()

    pygame.quit()
