from sys import maxsize

command = input()

max_num = -maxsize

while not command == 'Stop':
    num = int(command)
    if num > max_num:
        max_num = num
    command = input()

print(max_num)