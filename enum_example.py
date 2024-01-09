from enum import Enum


class Kolory(Enum):
    RED = 1
    BLUE = 2


class Kierunki(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


def kolorowy_kierunek_enum(kolor: Kolory, kierunek: Kierunki):
    if kierunek == Kierunki.WEST:
        print(kolor, kierunek)


if __name__ == "__main__":
    kolorowy_kierunek_enum(Kolory.RED, Kierunki.WEST)
