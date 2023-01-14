n = int(input())

parking = set()

for _ in range(n):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        parking.add(car_number)
    else:
        parking.remove(car_number)

if parking:
    [print(car) for car in parking]
else:
    print('Parking Lot is Empty')