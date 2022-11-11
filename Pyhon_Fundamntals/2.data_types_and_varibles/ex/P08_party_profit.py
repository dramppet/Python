

count_group = int(input())
days_adventure = int(input())

price = 0

for day in range(1, days_adventure + 1):
    price += 50
    price -= count_group * 2

    if day % 10 ==  0:
        count_group -= 2
    if day % 15 == 0:
        count_group += 5
    if day % 3 == 0:
        price -= count_group * 3
    if day % 5 == 0:
        price += count_group * 20
        if day % 3 == 0:
            price -= 2 * count_group

print(f'{count_group} companions received {round(price / count_group)} coins each.')