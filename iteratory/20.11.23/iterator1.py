class Parzyste:
    def __init__(self, start, stop):
        self.__start = start
        self.__stop = stop
        self.__current = start

    def __next__(self) -> int:
        wynik = self.__current
        if wynik >= self.__stop:
            raise StopIteration()
        self.__current += 2
        return wynik

    def __iter__(self): #sprawia że obiekt jest iterable
        return self


# for i in range(10):
#     print(i)

for i in Parzyste(100, 120):
    print(i)
