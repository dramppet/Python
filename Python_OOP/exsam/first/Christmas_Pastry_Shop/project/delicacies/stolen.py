from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    @property
    def get_portion(self):
        return 250
    def __init__(self, name, price):
        super().__init__(name, self.portion, price)

    def details(self):
        return f"Stolen {self.name}: {self.get_portion}g - {self.price:.2f}lv."
