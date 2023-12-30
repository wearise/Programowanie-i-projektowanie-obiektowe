from abc import ABC, abstractmethod


class Action(ABC):
    @abstractmethod
    def action(self):
        pass


class Actor(ABC):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @abstractmethod
    def name(self):
        pass


class Coin(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)

    def name(self):
        return "Coin"


class Cherry(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)

    def name(self):
        return "Cherry"


class Dragon(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)

    def name(self):
        return "Dragon"


# class AbstractHit(ABC):
#     @abstractmethod
#     def collision(self):
#         pass


class HitCoin(Action):
    def action(self):
        self.money += 1


class HitCherry(Action):
    def action(self):
        print("SUPERPOWER")


class Dispatch:
    def __init__(self):
        self.__a = {}

    def register_action(self, key: str, action: Action):
        self.__a[key] = action

    def action(self, key):
        if key in self.__a:
            self.__a[key].action()
        else:
            raise NotImplemented


class Maker(ABC):
    @abstractmethod
    def make_actor(self):
        pass


class MakeCoin(Maker):
    def make_actor(self, x, y):
        print(f"Making a new coin at {x} {y}")
        return Coin(x, y)


class MakeDragon(Maker):
    def make_actor(self, x, y):
        print(f"Making a new dragon at {x} {y}")
        return Dragon(x, y)


cfg = '''
Coin 14 24
Coin 15 24
Coin 16 24
Dragon 20 20
'''

if __name__ == "__main__":
    dispatch = Dispatch()  # - dyspozytor
    dispatch.register_action("Coin", HitCoin())
    dispatch.register_action("Cherry", HitCherry())

    factory = {"Coin": MakeCoin(), "Dragon": MakeDragon()}

    # print(factory)
    # print("-------------------------------------")

    for line in cfg.split('\n'):
        # print(line)
        tokens = line.split()
        # print(tokens,line)
        if len(tokens) != 3: continue
        factory[tokens[0]].make_actor(int(tokens[1]), int(tokens[2]))

    # print("-------------------------------------")
    # print(factory)


    # c1 = Coin()
    # c2 = Coin()
    # d = Dragon()
    # obstacles = [c1, c2, d]
    #
    # for o in obstacles:
    #     # print(o.__class__.__name__) # to działa tylko w pythonie
    #     print(o.name()) # to też w innych jezykach

    # a = Coin()
    # print(type(a))
    # print(a.__class__.__name__)
    # # print(dir(dispatch))
    # # print(dir(Dispatch))
    # # dispatch.action(a.name())
