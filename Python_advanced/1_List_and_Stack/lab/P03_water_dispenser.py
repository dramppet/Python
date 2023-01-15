from collections import deque

peoples = deque()
quantity_dispenser = int(input())

while True:
    person_name = input()

    if person_name == 'Start':
        break
    peoples.append(person_name)

while True:
    command = input()

    if command == 'End':
        break

    if command.startswith('refill'):
        single_command, water = command.split()
        quantity_dispenser += int(water)
    else:
        need_water = int(command)
        name = peoples.popleft()

        if quantity_dispenser >= need_water:
            print(f'{name} got water')
            quantity_dispenser -= need_water
        else:
            print(f'{name} must wait')

print(f'{quantity_dispenser} liters left')

