class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients):
        self.name = name
        self.price = price
        self.ingredients = {}
        self.order = False

    def add_extra(self, ingredient:str, quantity:int, price_per_quantity:float):
        if ingredient in self.ingredients[ingredient]:



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
