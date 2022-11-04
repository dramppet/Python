budget = float(input())
extras = int(input())
clothing_price = float(input())

decor = budget * 0.1
if extras > 150:
    clothing_price *= 0.9
total_expenses = decor + extras * clothing_price

if total_expenses <= budget:
    print('Action!')
    print(f'Wingard starts filming with {(budget - total_expenses):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(total_expenses - budget):.2f} leva more.')