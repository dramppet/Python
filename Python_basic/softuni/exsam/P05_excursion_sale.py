count_sea = int(input())
count_mountain = int(input())

SEA = 680
MOUNTAIN = 499

price = 0

while True:
    command = input()

    if command == 'Stop':
        break

    if command == 'sea':
        if count_sea > 0:
            price += SEA
            count_sea -= 1
        else:
            continue
    elif command == 'mountain':
        if count_mountain > 0:
            price += MOUNTAIN
            count_mountain -= 1
        else:
            continue

    if count_sea == 0 and count_mountain == 0:
        print('Good job! Everything is sold.')
        break

print(f'Profit: {price} leva.')





