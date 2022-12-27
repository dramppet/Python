count_wagons = int(input())
train = [0] * count_wagons

while True:
    command = input()

    if command == 'End':
        break

    current_command = command.split(' ')

    if current_command[0] == 'add':
        train[-1] += int(current_command[1])
    elif current_command[0] == 'insert':
        idx = int(current_command[1])
        people = int(current_command[2])
        train[idx] += people
    elif current_command[0] == 'leave':
        idx = int(current_command[1])
        people = int(current_command[2])
        train[idx] -= people

print(train)