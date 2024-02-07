class InnerClass:

    def my_method(self):
        return "metoda wewnętrzna"

class SimpleDelegation(InnerClass):

    def __init__(self):#, inner):
        # self.__inner = inner
        pass

    def my_method(self):
        # return "nadpisana " + InnerClass.my_method(self)
        return "nadpisana " + super().my_method()


if __name__ == "__main__" :

    ic = InnerClass()
    sd = SimpleDelegation()
    for obct in [ic, sd]:
        print(obct.my_method())
