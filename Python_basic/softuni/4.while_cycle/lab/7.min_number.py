import sys

number_input = input()
min_number = sys.maxsize

while not number_input == 'Stop':
    curr_num = int(number_input)

    if curr_num <= min_number:
        min_number = curr_num

    number_input = input()

print(min_number)