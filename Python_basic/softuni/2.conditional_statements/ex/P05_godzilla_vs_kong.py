budget = float(input())
count_statist = int(input())
price_clothing_one_statist = float(input())

price_decor = budget  * 0.1
price_clothing = count_statist * price_clothing_one_statist
if count_statist >= 150:
    price_clothing = price_clothing - (price_clothing * 0.1)
all_sum = price_decor + price_clothing

if budget > all_sum:
    print('Action!')
    print(f'Wingard starts filming with {(budget - all_sum):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(all_sum - budget):.2f} leva more.')