night = int(input()) - 1
place_type = input()
review = input()

price = 0

if place_type == 'room for one person':
    price = 18
elif place_type == 'apartment':
    price = 25

    if night < 10:
        price *= 0.7
    elif 10 <= night <= 15:
        price *= 0.65
    else:
        price *= 0.5
else:
    price = 35

    if night < 10:
        price *= 0.9
    elif 10 <= night <= 15:
        price *= 0.85
    else:
        price *= 0.8

if review == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f'{price * night:.2f}')
