from Strategy import Strategy


class Dispatch:
    def __init__(self):
        self.__a = {}

    def register_strategy(self, key: str, action: "Strategy"):
        self.__a[key] = action

    def make_restrain(self, key, tokens):
        if key in self.__a:
            return self.__a[key].make_object(tokens)
        else:
            raise NotImplemented

