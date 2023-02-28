from food import Food


class Fruit(Food):
    def __init__(self, name:str, expiration_data:str):
        self.name = name
        super().__init__(expiration_data)