import math


class Shape:
    def claculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def claculate_area(self):
        return self.side * self.h


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def claculate_area(self):
        return math.pow(self.side, 2)


shapes = [Triangle(5, 8), Square(9)]

for shape in shapes:
    print(shape.claculate_area())


