from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Triangle(Shape):
    def __init__(self, side, widht):
        self.side = side
        self.widht = widht

    def calc_area(self):
        return self.side * self.widht


s = [Triangle(2, 3)]

for se in s:
    print(se.calc_area())
