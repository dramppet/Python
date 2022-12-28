task = []

while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split('-')
    index = int(split_command[0])
    element = split_command[1]

    task.append((index, element))

sorted_task = [el[1] for el in sorted(task)]

print(sorted_task)


