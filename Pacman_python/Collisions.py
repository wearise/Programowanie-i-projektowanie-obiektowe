# import pygame
# from abc import ABC, abstractmethod
#
from GameConstants import GameConstants
from Strategy import RunAwayStrategy


# class Collision(ABC):
#
#     @staticmethod
#     @abstractmethod
#     def execute_collision(board: "Board"):  # list_of_ghosts: list, pacman_position: tuple):
#         pass


class BigTreatCollision():

    @staticmethod
    def execute_collision(list_of_ghosts: list):

        for ghost in list_of_ghosts:
            ghost.strategy = RunAwayStrategy()
            ghost.how_long_it_can_be_eaten += 10 * GameConstants.FPS
            ghost.speed.register_new_speed(ghost.speed.speed//2 + 1)


class GhostCollision():

    @staticmethod
    def execute_collision(board: "Board", ghost: "Ghost"):

        # pacman = board.pacman
        #
        # if ghost.how_long_it_can_be_eaten > 0:
        #     ghost.how_long_it_can_be_eaten = 0
        #     ghost.reset_position()
        #     ghost.waiting = 5 * GameConstants.FPS
        # else:
        #     pacman.life_lost()
        #     board.ghosts_no_able_to_be_eaten()
        #     board.ghosts_restart_waiting()
        #
        #     if pacman.lives == 0:
        #         game_finished = 1
        #         # board.draw_ghosts(screen)
        #         screen.blit(przegranko_text, textRect)
        #     else:
        #         board.reset_objects_positions()
        #         break

            pass

