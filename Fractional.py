from Polynomial import Polynomial
class Fractional():

    def __init__(self,num,den): #numerator, denomiantor; bez anotacji typów, bo mogą być różne
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num.copy()

    @property
    def den(self):
        return self.__den.copy()

    def __str__(self):
        return str(self.__num) + '/' + str(self.__den)

    def __add__(self, f : "Fractional") -> "Fractional":
        new_num = self.__num * f.__den + f.__num * self.__den
        new_den = self.__den * f.__den
        return Fractional(new_num,new_den)

    def __sub__(self, f : "Fractional") -> "Fractional":
        new_num = self.__num * f.__den - f.__num * self.__den
        new_den = self.__den * f.__den
        return Fractional(new_num,new_den)

    def __mul__(self, f : "Fractional") -> "Fractional":
        return Fractional(self.__num * f.__num, self.__den * f.__den)

if __name__ == '__main__':
    # f1 = Fractional(3,4)
    # f2 = Fractional(1,2)
    # print(f1)
    # f3 = f1 + f2
    # print(f3)
    # f4 = f1 - f2
    # print(f4)
    # f5 = f1 * f2
    # print(f5)

    # f1 = Fractional(2, 5)
    # f2 = Fractional(1, 3)
    #
    # f3 = f1 * f2
    # print(f3)  # Drukuje na ekran: 2/15
    # f3 += f1   # 2/15 + 2/5 = (10+30)/(15*5)
    # print(f3)
    # f4 = f3 - f2

    w1 = Polynomial(1, 2, 5)
    w2 = Polynomial(1, 3)
    print(str(w2)+'/'+str(w1))
    f1 = Fractional(w1, w2)   # 1*x^2 + 2*x + 5/1*x + 3
    f2 = Fractional(w2, w1)   # 1*x + 3/1*x^2 + 2*x + 5
    print(f1 + f2)            # 1*x^4 + 4*x^3 + 15*x^2 + 26*x + 34/1*x^3 + 5*x^2 + 11*x + 15