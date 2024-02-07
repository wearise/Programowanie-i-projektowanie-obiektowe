import pygame
from abc import ABC, abstractmethod


class Collision(ABC):

    @staticmethod
    @abstractmethod
    def execute_collision(list_of_ghosts: list, pacman_position: tuple):
        pass


class BigTreatCollision(Collision):

    @staticmethod
    def execute_collision(list_of_ghosts: list, pacman_position: tuple):
        for ghost in list_of_ghosts:
            ghost.able_to_be_eaten = True
            ghost.how_long_it_can_be_eaten += 10*20  # FPS = 20


class GhostCollision(Collision):

    # trzeba sprawdzać czy jest flaga able_to_be_eaten
    @staticmethod
    def execute_collision(list_of_ghosts: list, pacman_position: tuple):
        # for ghost in list_of_ghosts:
        #     gost.position
        pass

