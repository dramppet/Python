import math

class Shape:
    def calculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, h, side):
        self.h = h
        self.side = side

    def calculate_area(self):
        return self.h * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * math.pi

class Squ(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


t = Triangle(2, 3)
c = Circle(5)
t1 = Triangle(8, 6)
s = Squ(5)

shapes = [t, c, t1, s]

for shape in shapes:
    print(shape.calculate_area())
