data = input()

products = {}

while True:
    if data == 'statistics':
        break

    product, quantity = data.split(': ')

    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)

    data = input()
total_quantity = 0
print('Products in stock:')
for key, value in products.items():
    total_quantity += value
    print(f'- {key}: {value}')

print(f'Total Products: {len(products)}')
print(f'Total Quantity: {total_quantity}')