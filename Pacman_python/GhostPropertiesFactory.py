from Colors import Colors
from Strategy import *
from GameConstants import GameConstants

class GhostPropertiesFactory:

    __strategies = list([RandomStrategy(), FollowStrategy(), RandomStrategy(), FollowStrategy(), RunAwayStrategy()])
    __colors = Colors.ghost_colors
    __index = 0

    @staticmethod
    def get_ghost_properties() -> "GhostProperties":
        if GhostPropertiesFactory.__index == len(GhostPropertiesFactory.__strategies):
            GhostPropertiesFactory.__index = 0
        GhostPropertiesFactory.__index += 1
        return GhostProperties(GhostPropertiesFactory.__strategies[GhostPropertiesFactory.__index-1],
                               GhostPropertiesFactory.__colors[GhostPropertiesFactory.__index-1],
                               (GhostPropertiesFactory.__index-1)*3*GameConstants.FPS)


class GhostProperties:

    def __init__(self, strategy, color, waiting_time):
        self._strategy = strategy
        self._color = color
        self._waiting = waiting_time

    @property
    def strategy(self):
        return self._strategy

    @property
    def color(self):
        return self._color

    @property
    def waiting(self):
        return self._waiting
