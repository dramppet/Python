from project.animals.animal import Mammal
from project.food import Vegetable, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]