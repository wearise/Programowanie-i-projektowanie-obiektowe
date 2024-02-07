class MyNumbers:
    def __iter__(self):
        self.a = [1,2,3,4,5]
        self.x = 0
        return self

    def __next__(self):
        if self.x < len(self.a):
            self.x += 1
            return self.a[self.x-1]
        else: raise "StopIteration"

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#   def __iter__(self):
#     self.a = [1, 2, 3, 4, 5]
#     self.x = 0
#     return self
#
#   def __next__(self):
#     self.x += 1
#     return self.a[self.x-1]
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))