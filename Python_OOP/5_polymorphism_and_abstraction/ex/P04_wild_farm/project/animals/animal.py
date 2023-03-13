from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0


    @property
    @abstractmethod
    def food_that_eats(self):
        ...

    @staticmethod
    @abstractmethod
    def make_sound(self):
        pass


    def feed(self, food):
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {FoodType}!"

class Bird(ABC, Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(self, name, weight)
        self.wing_size = wing_size


class Mammal(ABC,Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(self, name, weight)
        self.living_region = living_region