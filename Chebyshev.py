from Polynomial import Polynomial


class Chebyshev(Polynomial):

    @staticmethod
    def __chebyshev(k: int):
        if k == 0:
            return [1]
        elif k == 1:
            return [1, 0]
        else:
            T_k_1 = Chebyshev.__chebyshev(k - 1)
            T_k_1 = [2 * x for x in T_k_1]  # mnoze liste *2
            T_k_1.append(0)  # dodaje 0 na koncu - podnosze potege (*x)
            T_k_2 = Chebyshev.__chebyshev(k - 2)
            T_k_2 = [0, 0] + T_k_2  # dodaje dwa zera na poczatku zeby byly zgodne wymiary
            return [T_k_1[i] - T_k_2[i] for i in range(len(T_k_1))]

    def __init__(self, k: int):
        super().__init__(Chebyshev.__chebyshev(k))


if __name__ == "__main__":
    print("-----------------------------------------")
    C0 = Chebyshev(6)
    C1 = Chebyshev(2)  # [2, 0, -1]
    C2 = C0 + C1

    print(C0.coefficients)
    print(C1.coefficients)
    print(C2.coefficients)
    '''
    
    [2,0,-1]          T2 = 2x^2-1
    [4,0,-3,0]        T3 = 4x^3-3x                    = 4x^3-2x-x
    [8,0,-8,0,1]      T4 = 8x^4 - 8x^2 + 1            = 8x^4-6x^2 - 2x^2 +1
    [16,0,-20,0,5,0]  T5 = 16x^5 - 20x^3 + 5x         = 16x^5 - 16x^3 + 2x - 4x^3 + 2x + x
    
    '''
