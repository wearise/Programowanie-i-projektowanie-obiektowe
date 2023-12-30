from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def action(self):
        pass

class Help(Action):
    def action(self):
        print("hlp msg")

class About(Action):
    def action(self):
        print("This is the best program ever!")

class Dispatch:
    def __init__(self):
        self.__a = {}

    def register_action(self, key: str, action:Action):
        self.__a[key] = action

    def action(self, key):
        if key in self.__a:
            self.__a[key].action()
        else:
            raise NotImplemented

if __name__ == "__main__":
    dispatch = Dispatch() # - dyspozytor
    dispatch.register_action("H", Help())
    dispatch.register_action("A", About())

    commds = "HHAAHAHAHHHH"

    for one_cmd in commds:
        dispatch.action(one_cmd)
