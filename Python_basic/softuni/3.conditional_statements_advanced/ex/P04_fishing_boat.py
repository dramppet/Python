budget = int(input())
season = input()
count_fishmen = int(input())

price_ship = 0

if season == 'Spring':
    price_ship = 3000
elif season == 'Summer' or season == 'Autumn':
    price_ship = 4200
elif season == 'Winter':
    price_ship = 2600


if count_fishmen == 6:
    price_ship *= 0.9
if 7 < count_fishmen <= 11:
    price_ship *= 0.85
if count_fishmen > 12:
    price_ship *= 0.75

if not(season == 'Autumn') and count_fishmen % 2 == 0:
    price_ship *= 0.95

if budget > price_ship:
    print(f'Yes! You have {budget - price_ship:.2f} leva left.')
else:
    print(f'Not enough money! You need {price_ship - budget:.2f} leva.')