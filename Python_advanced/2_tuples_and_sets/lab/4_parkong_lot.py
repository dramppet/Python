count_parking = int(input())
parking_lot = {input() for _ in range(count_parking)}

COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

parking = set()

for name in parking_lot:
    command, numbers = name.split(', ')

    if command == 'IN':
        parking.add(numbers)
    elif command == 'OUT':
        parking.pop(numbers)
