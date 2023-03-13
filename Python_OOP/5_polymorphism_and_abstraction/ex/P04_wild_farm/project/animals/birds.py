from project.animals.animal import Bird
from project.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]