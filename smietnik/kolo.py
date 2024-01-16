@property
def r(self):
    return self.__r

@property
def area(self):
    return self.__area
@r.setter
def r(self,new_r):
    self.__r = new_r
    self.__area = 3.14159*new_r