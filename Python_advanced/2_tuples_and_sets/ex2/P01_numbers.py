def add_set(command):
    if command[0] == 'First':
        for el in command[1:]:
            first_set.add(el)
    elif command[0] == 'Second':
        for el in command[1:]:
            second_set.add(el)
def remove_set(command):
    if command[0] == 'First':
        for el in command[1:]:
            if el in first_set:
                first_set.remove(el)
    elif command[0] == 'Second':
        for el in command[1:]:
            if el in second_set:
                second_set.remove(el)


first_set, second_set = {*input().split()}, {*input().split()}

COUNT_COMMANDS = int(input())

for _ in range(COUNT_COMMANDS):
    command_data = input().split()

    if command_data[0] == "Add":
        add_set(command_data[1:])
    elif command_data[0]=='Remove':
        remove_set(command_data[1:])
    elif command_data[0] == 'Check':
        print("True" if first_set.issubset(second_set) or second_set.issubset(first_set) else "False")

print(*sorted([int(x) for x in first_set]),sep=', ')
print(*sorted([int(x) for x in second_set]),sep=', ')