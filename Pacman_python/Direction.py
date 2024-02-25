import pygame  # as pg
import os


class Direction:
    LEFT = (-5, 0)
    RIGHT = (5, 0)
    UP = (0, -5)
    DOWN = (0, 5)

    all_directions = [LEFT, RIGHT, UP, DOWN]

    # LEFT = (-6, 0)
    # RIGHT = (6, 0)
    # UP = (0, -6)
    # DOWN = (0, 6)
    #
    # all_directions = [LEFT, RIGHT, UP, DOWN]


    @staticmethod
    def random_direction(all_or_list_of_directions_to_draw):
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        if all_or_list_of_directions_to_draw == "all" or (isinstance(all_or_list_of_directions_to_draw, list) and len( all_or_list_of_directions_to_draw)==0):#(isinstance(all_or_list_of_directions_to_draw, list):

            if x < 0.25:
                return Direction.LEFT

            elif x < 0.5:
                return Direction.RIGHT

            elif x < 0.75:
                return Direction.UP

            else:
                return Direction.DOWN

        elif (isinstance(all_or_list_of_directions_to_draw, list)
              and sum([isinstance(x, tuple) for x in all_or_list_of_directions_to_draw]) ==
              len(all_or_list_of_directions_to_draw)):
            # sprawdzam czy argument jest listą i czy wszystkie jej elementy są tuplami

            dx = 1 / len(all_or_list_of_directions_to_draw)
            j = 0
            i = dx

            while i <= 1:

                if x < i:
                    return all_or_list_of_directions_to_draw[j]
                j += 1
                i += dx

        else:
            raise Exception("Invalid argument")

    @staticmethod
    def ghost_possible_directions(its_actual_direction: tuple) -> list:
        # duszek nie ma możliwości cofania się
        if its_actual_direction == Direction.LEFT or its_actual_direction == Direction.RIGHT:
            return [Direction.UP, Direction.DOWN, its_actual_direction]
        if its_actual_direction == Direction.UP or its_actual_direction == Direction.DOWN:
            return [Direction.RIGHT, Direction.LEFT, its_actual_direction]

    @staticmethod
    def map_from_event_key(event_key: int) -> tuple:
        if event_key == pygame.K_LEFT:
            return Direction.LEFT
        if event_key == pygame.K_RIGHT:
            return Direction.RIGHT
        if event_key == pygame.K_UP:
            return Direction.UP
        if event_key == pygame.K_DOWN:
            return Direction.DOWN

    # @staticmethod
    # def opposite_direction(direction: tuple) -> tuple:
    #     if direction == Direction.LEFT:
    #         return Direction.RIGHT
    #     if direction == Direction.RIGHT:
    #         return Direction.LEFT
    #     if direction == Direction.UP:
    #         return Direction.DOWN
    #     if direction == Direction.DOWN:
    #         return Direction.UP