from abc import ABC, abstractmethod


class Collision(ABC):

    @staticmethod
    @abstractmethod
    def execute_collision(list_of_objects: list):
        pass


class TreatCollision(Collision):

    @staticmethod
    def execute_collision(list_of_treats: list):
        pass


class GhostCollision(Collision):

    @staticmethod
    def execute_collision(list_of_ghosts: list):
        pass
