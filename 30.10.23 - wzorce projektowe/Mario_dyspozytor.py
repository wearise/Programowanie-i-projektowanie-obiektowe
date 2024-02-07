from abc import ABC, abstractmethod
from math import fabs

class Actor:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Mario(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20)
        self.coins = 0
        self.lifes = 3
        self.speed = 1.0

    def if_crashes_into(self, actor: Actor):
        dx = fabs(actor.x - self.x)
        dy = fabs(actor.y - self.y)
        return dx < (self.width+actor.width)/2.0 and dy < (self.height+actor.height)/2.0

class Coin(Actor):
    def __init__(self, x, y):
        super(Coin, self).__init__(x, y, 10, 10)

class Turtle(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 10)

class Cherry(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10)

class CollisionAction(ABC):
    @abstractmethod
    def dispatch(self, a_mario: Mario): pass

class MarioHitsTurtle(CollisionAction):
    def dispatch(self, a_mario: Mario): a_mario.lifes -= 1


class MarioHitsCoin(CollisionAction):
    def dispatch(self, a_mario: Mario): a_mario.coins += 1

class MarioHitsCherry(CollisionAction):
    def dispatch(self, a_mario: Mario): a_mario.speed *= 1.5

class CollisionDispatch:
    def __init__(self):
        self.__dict = {}

    def __str__(self):
        return str(self.__dict)

    def register(self, cls_name: str, action: CollisionAction):
        self.__dict[cls_name] = action

    def make_action(self, actor_name):
        return self.__dict[actor_name]


if __name__ == "__main__":

    game_actors = [Turtle(20, 5), Coin(24, 8),
                   Coin(26, 8), Cherry(30, 2)]

    # in the main loop of the game you update Mario's position
    mario = Mario(0, 0)
    # register collision action in a dispatch:
    collisions = CollisionDispatch()
    collisions.register(Coin.__name__, MarioHitsCoin())
    collisions.register(Turtle.__name__, MarioHitsTurtle())
    collisions.register(Cherry.__name__, MarioHitsCherry())

    # print(Coin.__name__)
    # print(Turtle.__name__)
    # print(Cherry.__name__)
    # print(collisions)

    # check for collisions:
    for actor in game_actors:
        # dispatch actions accordingly to the actor's type
        if mario.if_crashes_into(actor):
            collisions.make_action(actor.__name__).dispatch(mario)