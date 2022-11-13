count_day = int(input()) - 1
type_room = input()
ocenka = input()

price = 0

if type_room == 'room for one person':
    price = count_day * 18.00

elif type_room == 'apartment':
    price_a = 25.00
    if count_day < 10:
        price = (count_day * price_a) * 0.65
    elif count_day <= 15:
        price = (count_day * price_a) * 0.65
    elif count_day > 15:
        price = (count_day * price_a) * 0.5
elif type_room == 'president apartment':
    price_p = 35.00
    if count_day < 10:
        price = (count_day * price_p) * 0.9
    elif count_day <= 15:
        price = (count_day * price_p) * 0.85
    elif count_day > 15:
        price = (count_day * price_p) * 0.8


if ocenka == 'positive':
    price = price * 1.25
else:
    price = price * 0.9

print(f'{price:.2f}')