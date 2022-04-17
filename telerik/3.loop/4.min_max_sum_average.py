import sys

numbers_count = int(input())

min_numbers = sys.maxsize
max_numbers = -sys.maxsize
sum_numbers = 0.0

for _ in range(numbers_count):
    num = float(input())

    sum_numbers += num

    if num > max_numbers:
        max_numbers = num

    if num < min_numbers:
        min_numbers = num

print(f'min={min_numbers:.2f}')
print(f'max={max_numbers:.2f}')
print(f'sum={sum_numbers:.2f}')
print(f'avg={(sum_numbers/numbers_count):.2f}')
