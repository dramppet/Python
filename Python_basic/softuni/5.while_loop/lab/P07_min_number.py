from sys import maxsize

command = input()

min_num = maxsize

while not command == 'Stop':
    num = int(command)

    if num < min_num:
        min_num = num

    command = input()

print(min_num)