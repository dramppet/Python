import sys

number = input()
max_number = -sys.maxsize

while not number == 'Stop':
    curr_num = int(number)

    if curr_num > max_number:
        max_number = curr_num


    number = input()

print(max_number)