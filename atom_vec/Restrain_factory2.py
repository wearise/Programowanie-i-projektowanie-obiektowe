import sys
from Atom import Atom, atoms_from_pdb
from abc import ABC, abstractmethod

class AbstractRestrainFunction(ABC):

    def __init__(self, i, j):
        self.__i = i
        self.__j = j

    @abstractmethod
    def __call__(self, x):
        raise NotImplemented("to be implemented in by a derived class")

    @property
    def ai(self):
        return self.__i

    @property
    def aj(self):
        return self.__j


class LinearRestrainFunction(AbstractRestrainFunction):

    def __init__(self, i, j, d0, k):
        super().__init__(i, j)
        self.__d0 = d0
        self.__k = k

    def __call__(self, d):
        v = self.__k*(self.__d0-d)           # Calculate the energy for distance d according to the formula
        return v

    def __str__(self):
        return "%3d %3d LINEAR %6.2f %4.2f" % (self.ai, self.aj, self.__d0, self.__k)

class LorentzianRestrainFunction(AbstractRestrainFunction):

    def __init__(self, i, j, d0, gamma):
        super().__init__(i, j)
        self.__d0 = d0
        self.__gamma = gamma

    def __call__(self, d):
        v = (self.__d0-d)*(self.__d0-d)/((self.__d0-d)*(self.__d0-d)+self.__gamma*self.__gamma)           # Calculate the energy for distance d according to the formula
        return v

    def __str__(self):
        return "%3d %3d LORENTZIAN %6.2f %4.2f" % (self.ai, self.aj, self.__d0, self.__gamma)

class HarmonicRestrainFunction(AbstractRestrainFunction):

    def __init__(self, i, j, d0, k):
        super().__init__(i, j)
        self.__d0 = d0
        self.__k = k

    def __call__(self, d):
        v = self.__k*(self.__d0-d)*(self.__d0-d)           # Calculate the energy for distance d according to the formula
        return v

    def __str__(self):
        return "%3d %3d HARMONIC %6.2f %4.2f" % (self.ai, self.aj, self.__d0, self.__k)

class FlatBottomRestrainFunction(AbstractRestrainFunction):

    def __init__(self, i, j, e, a, b):
        super().__init__(i, j)
        self.__e = e
        self.__a = a
        self.__b = b

    def __call__(self, d):  # Calculate the energy for distance d according to the formula

        if(d>=self.__a and d<=self.__b):
            return self.__e
        return 0.0

    def __str__(self):
        return "%3d %3d FLAT_BOTTOM %6.2f %4.2f" % (self.ai, self.aj, self.__e, self.__a, self.__b)

class Maker(ABC):
    @abstractmethod
    def make_object(self):
        pass


class MakeLinear(Maker):
    def make_object(self, tokens):
        return LinearRestrainFunction(int(tokens[0]), int(tokens[1]), float(tokens[3]), float(tokens[4]))


class MakeHarmonic(Maker):
    def make_object(self, tokens):
        return HarmonicRestrainFunction(int(tokens[0]), int(tokens[1]), float(tokens[3]), float(tokens[4]))

class MakeLorentzian(Maker):
    def make_object(self, tokens):
        return LorentzianRestrainFunction(int(tokens[0]), int(tokens[1]), float(tokens[3]), float(tokens[4]))

class MakeFlatBottom(Maker):
    def make_object(self, tokens):
        return FlatBottomRestrainFunction(int(tokens[0]), int(tokens[1]), float(tokens[3]), float(tokens[4]), float(tokens[5]))

class Dispatch:
    def __init__(self):
        self.__a = {}

    def register_action(self, key: str, action: Maker):
        self.__a[key] = action

    def make_restrain(self, key, tokens):
        if key in self.__a:
            return self.__a[key].make_object(tokens)
        else:
            raise NotImplemented

rst_data = """
 2  8 LINEAR 4.934 3.0
 2  9 LORENTZIAN 5.534 3.0
 2 16 LORENTZIAN 9.279 3.0
 3 11 LORENTZIAN 8.755 3.0
10 19 LORENTZIAN 9.850 3.0
12 17 LORENTZIAN 7.358 3.0
14 19 LORENTZIAN 7.560 3.0
 3  2 HARMONIC 3.0 1.0
 5 13 FLAT_BOTTOM 5.0 6.0 -1.0
 6 12 FLAT_BOTTOM 5.0 6.0 -1.0
 8  6 HIGH 8.0 9.0
"""
if __name__ == "__main__":

    # factory = {"LINEAR": MakeLinear(), "HARMONIC": MakeHarmonic(), "LORENTZIAN": MakeLorentzian(), "FLAT_BOTTOM": MakeFlatBottom()}

    factory = Dispatch()  # - dyspozytor
    factory.register_action("LINEAR", MakeLinear())
    factory.register_action("HARMONIC", MakeHarmonic())
    factory.register_action("LORENTZIAN", MakeLorentzian())
    factory.register_action("FLAT_BOTTOM", MakeFlatBottom())


    # ------------------ Here we prepare restraints
    rst = []
    for line in rst_data.split("\n"):
        if len(line) < 5: continue
        if line[0] == '#': continue
        tokens = line.split()

        # rst.append(factory[tokens[2]].make_object(tokens))
        rst.append(factory.make_restrain(tokens[2],tokens))

    atoms = atoms_from_pdb("surpass.pdb") #sys.argv[1]
    print(atoms[0])
    print(rst)

    for r in rst:
        d = atoms[r.ai].distance_to(atoms[r.aj])
        print("E = ",r(d))
    print("Restraints created:")
    # for r in rst: print(r)