from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_ADD = 3

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def train(self):
        self.speed = min(self.speed + self.SPEED_ADD, self.MAX_SPEED)
