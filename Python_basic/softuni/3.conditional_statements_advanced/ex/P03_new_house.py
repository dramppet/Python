ROSES = 5
DAHLIAS = 3.8
TULIPS = 2.8
NARCISSUS = 3
GLADIOLUS = 2.5

type_flowers = input()
count_flowers = int(input())
budget = int(input())

if type_flowers == 'Roses':
    price = count_flowers * ROSES
    if count_flowers > 80:
        price *= 0.9
elif type_flowers == 'Dahlias':
    price = count_flowers * DAHLIAS
    if count_flowers > 90:
        price *= 0.85
elif type_flowers == "Tulips":
    price = count_flowers * TULIPS
    if count_flowers > 80:
        price *= 0.85
elif type_flowers == "Narcissus":
    price = count_flowers * NARCISSUS
    if count_flowers < 120:
        price *= 1.15
elif type_flowers == 'Gladiolus':
    price = count_flowers * GLADIOLUS
    if count_flowers < 80:
        price *= 1.2

if budget >= price:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} '
          f'and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')