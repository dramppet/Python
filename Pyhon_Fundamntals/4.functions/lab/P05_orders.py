def calculate_total_price(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'water':
        return quantity * 1
    elif product == 'snacks':
        return  quantity * 2


product_input = input()
quantity_input = float(input())
print(f'{calculate_total_price(product_input,quantity_input):.2f}')