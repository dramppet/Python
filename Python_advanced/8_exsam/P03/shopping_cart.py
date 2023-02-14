def shopping_cart(*args):
    inventory = {'Soup': [], 'Pizza': [], 'Diessert': []}
    inventory_limit = {'Soup': 3, 'Pizza': 4, 'Diessert': 2}


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
