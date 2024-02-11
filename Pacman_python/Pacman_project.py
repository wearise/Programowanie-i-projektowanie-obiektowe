import pygame
import os
from copy import deepcopy, copy
from abc import ABC, abstractmethod
from Dispatch import Dispatch
from Direction import Direction
from Strategy import RandomStrategy#, FollowStrategy
from Collisions import BigTreatCollision, GhostCollision
# from MovingObject import Pacman, Ghost
# from Wall import Wall
from Treats import Treat, BigTreat
from Colors import Colors
from Board import Board

# def sign(n):
#     if n < 0:
#         return -1
#     elif n > 0:
#         return 1
#     else:
#         return 0


if __name__ == '__main__':

    pygame.init()
    board = Board("board2.txt", 30)
    # with open("easy_board.txt") as board:
    # screen = pygame.display.set_mode((board.length, board.width))
    screen1 = pygame.display.set_mode((board.length, board.width))
    screen2 = pygame.display.set_mode((board.length, board.width))
    clock = pygame.time.Clock()
    FPS = 20  # Frames per second.

    factor = board.factor
    pacman = board.pacman
    walls_xy = board.walls_xy

    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('PRZEGRANKO', True, Colors.BLACK, Colors.MINT)
    text2 = font.render('WYGRANKO', True, Colors.BLACK, Colors.ORANGE)
    textRect = text.get_rect()
    textRect.center = (board.length // 2, board.width // 2)

    screen1.fill(Colors.BLACK)

    for wall in board.walls:
        wall.draw(screen1)

    for ghost in board.ghosts:
        ghost.draw(screen1)

    for treat in board.treats:
        treat.draw(screen1)

    pygame.display.flip()

    Game = True
    i = 0
    while Game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                Game = False

            if event.type == pygame.KEYDOWN:
                # print(type(event.key))
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pacman.onKeyPressed(event.key)

        if i % 2 == 0:
            screen = screen1
            next_screen = screen2
#             print("""screen = screen1
# next_screen = screen2""")
        else:
            screen = screen2
            next_screen = screen1
            # print("odwrotnie")

        screen.fill(Colors.BLACK)
        pacman.move()

        for wall in board.walls:
            wall.draw(next_screen)

        for treat in board.treats:
            treat.draw(next_screen)
            if treat.center == pacman.center:
                if isinstance(treat, BigTreat):
                    BigTreatCollision.execute_collision(board.ghosts, pacman.position)
                # print(treat)
                board.usun_smaczek(treat)

        for ghost in board.ghosts:
            # jeżeli środki są oddalone o sumę promieni
            if abs(ghost.center[0]-pacman.center[0]) < ghost.radius + pacman.radius and abs(ghost.center[1]-pacman.center[1]) < ghost.radius + pacman.radius:
                if ghost._how_long_it_can_be_eaten > 0:
                    board.delete_ghost(ghost)
                else: screen.blit(text, textRect)
            ghost.set_direction()
            # RUSZ DUSZKIEM i znów to samo:
            ghost.move()
            # if abs(ghost.center[0]-pacman.center[0]) < ghost.radius + pacman.radius and abs(ghost.center[1]-pacman.center[1]) < ghost.radius + pacman.radius:
            #     screen.blit(text, textRect)

            # if ghost.able_to_be_eaten == True:
            if ghost.how_long_it_can_be_eaten > 0:
                if i < 4:
                    ghost.draw(next_screen)
                elif i < 9:
                    pass
                else: i = 0
                ghost.how_long_it_can_be_eaten -= 1
            else: ghost.draw(next_screen)


        if not board.treats:
            screen.blit(text2, textRect)

        pacman.draw(next_screen)
        pygame.display.update()  # Or pygame.display.flip()

        i += 1
        # print(i)

    pygame.quit()
