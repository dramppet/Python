def sum_numbers_func(file_name):
    data = open(file_name, 'r')

    sum_numbers = 0

    for number in data:
        sum_numbers += int(number)

    return sum_numbers

print(sum_numbers_func('numbers.txt'))