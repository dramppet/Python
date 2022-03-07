class Beverage:
    def __init__(self, milliliters):
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

