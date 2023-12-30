from math import sqrt


class Vec3:
    __slots__ = ['__x', '__y', '__z']

    def __init__(self, *args):

        if args is None or len(args) == 0:
            self.__x, self.__y, self.__z = 0.0, 0.0, 0.0  # Default constructor
        elif len(args) == 3:  # support for Vec3(1.2,3.8,0.1)
            self.__x, self.__y, self.__z = args[0], args[1], args[2]
        elif len(args) == 1:
            if isinstance(args[0], Vec3):  # support for Vec3(v)
                self.__x, self.__y, self.__z = args[0].__x, args[0].__y, args[0].__z
            elif isinstance(args[0], list):  # support for Vec3( [1.2,3.8,0.1] )
                self.__x, self.__y, self.__z = args[0][0], args[0][1], args[0][2]
            else:  # support for Vec3(0)
                self.__x, self.__y, self.__z = args[0], args[0], args[0]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z

    def __str__(self):
        return "%.3f, %.3f, %.3f" % (self.__x, self.__y, self.__z)

    def distance_square_to(self, vj):
        d2 = (self.__x - vj.__x) * (self.__x - vj.__x)
        d2 += (self.__y - vj.__y) * (self.__y - vj.__y)
        return d2 + (self.__z - vj.__z) * (self.__z - vj.__z)

    def distance_to(self, vj):
        return sqrt(self.distance_square_to(vj))

    def __isub__(self, v):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        return self

    def __iadd__(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
        return self

    def __add__(self, rhs):
        v = Vec3(self)
        v += rhs
        return v

    def __sub__(self, rhs):
        v = Vec3(self)
        v -= rhs
        return v

    def __imul__(self, rhs):
        self.x *= rhs
        self.y *= rhs
        self.z *= rhs
        return self


if __name__ == "__main__":
    v0 = Vec3()
    v1 = Vec3(1.2, 3.4, 2.6)
    v1.z = 8.2
    print(v1.x)
    print(v1.y)
    print(v1)
    v2 = Vec3(-1.2, 0.4, 3.0)
    print(v1 - v2)