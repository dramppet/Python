while True:
    command = input()

    if command == 'End':
        break
    if command == 'SoftUni':
        continue

    for i in range(len(command)):
        print(command[i]*2,end='')
    print()
