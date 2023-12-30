class Bazowa:
    pole = 9
    def __init__(self, x):
        self.x = x

    @staticmethod
    def metoda():
        print("I'm here")

    @classmethod # też, jak metoda statyczna, taka sama dla każdego obiektu w klasie
    #ale metoda statyczna nie wie jakiego jest typu, a metoda w klasie dostaje ten tym jako argument
    def metoda_w_klasie(cls):
        print(f"I'm here in {cls}")

    @staticmethod
    def nowy_obiekt(val):
        return Bazowa(val)

    @classmethod
    def nowy_obiekt_w_klasie(cls,val):
        print(f"Nowy obiekt dla {val}")
        return cls(val)

class Potomna(Bazowa):

    def __init__(self, x):
        self.x = x*x
    # pass
    @staticmethod
    def metoda():
        print("I'm there")

if __name__ == "__main__":
    # # p = Potomna()
    # Potomna.metoda()
    # o = Potomna.nowy_obiekt_w_klasie(3)
    # print(o.x)
    # # Bazowa.metoda_w_klasie()
    # # Potomna.metoda_w_klasie()
    o1 = Potomna.nowy_obiekt_w_klasie(3)
    print(o1.pole)
    Potomna.pole = 8
    print(o1.pole)
    o2 = Potomna.nowy_obiekt_w_klasie(3)
    print(Potomna.pole)