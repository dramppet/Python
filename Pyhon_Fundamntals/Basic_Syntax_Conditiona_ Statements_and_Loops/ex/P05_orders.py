count_order = int(int(input()))

total_price = 0

for _ in range(count_order):
    price_capsule = float(input())
    if price_capsule < 0.01 or price_capsule > 100.00:
        continue
    days = int(input())
    if days < 1 or days > 31:
        continue
    capsule_needed_for_day = int(input())
    if capsule_needed_for_day < 1 or capsule_needed_for_day > 2000:
        continue

    price = price_capsule * days * capsule_needed_for_day
    total_price += price

    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')