from collections import deque

water_quantity = int(input())

people = deque()

while True:
    command = input()
    if command == 'Start':
        break

    people.appendleft(command)

while True:
    command = input()
    if command == "End":
        break
    if command.startswith('refill'):
       params = command.split()
       water_quantity += int(params[1])
    else:
        name = people.pop()
        water_wanted = int(command)
        if water_wanted <= water_quantity:
            print(f'{name} got water')
            water_quantity -= water_wanted
        else:
            print(f'{name} must wait')

print(f'{water_quantity} liters left')