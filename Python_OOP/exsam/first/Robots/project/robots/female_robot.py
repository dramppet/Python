from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    EATING_INCREASES  = 1

    def __init__(self, name: str, kind: str, price: float, weight = 7):
        super().__init__(name,kind,price, weight)

    def eating(self):
        self.weight += self.EATING_INCREASES
