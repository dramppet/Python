from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self._radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__ength = length
        self._width = width

    def calculate_area(self):
        return self.__ength * self._width

    def calculate_perimeter(self):
        return  2 * (self.__ength + self._width)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())