from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self,animal:Animal, price):
        if self.__budget >= price and self.__animal_capacity >= self.animals:
            self.animals.append(animal)
            return f"{self.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity >= self.animals and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker:Worker):
        if self.__workers_capacity <= self.workers:
            self.workers.append(worker)
            return f"{self.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for work"

    def fire_worker(self, worker_name):
        if worker_name in self.workers:
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget > 0:
            pass
