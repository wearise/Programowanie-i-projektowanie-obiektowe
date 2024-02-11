# funkcja sign jest potrzebna, bo pacman w jednej klatce
# przesówa się o 5 pikseli, a my chcemy tylko wyłapać kierunek
def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0