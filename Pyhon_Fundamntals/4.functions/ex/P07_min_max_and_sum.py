def min_number(numbers):
    return min(numbers)


def max_numbers(numbers):
    return max(numbers)


def sum_min_and_max(numbers):
    return sum(numbers)


list_numbers = list(map(lambda x: int(x), input().split(' ')))
print(f'The minimum number is {min_number(list_numbers)}')
print(f'The maximum number is {max_numbers(list_numbers)}')
print(f'The sum number is: {sum_min_and_max(list_numbers)}')