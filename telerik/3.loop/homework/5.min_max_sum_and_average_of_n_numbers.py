import sys

count_number = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize
avg = 0.0
sum_number = 0

for _ in range(count_number):
    num = int(input())

    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num

    sum_number += num


print('min=',min_number)
print('max=',max_number)
print('sum=',sum_number)
print(f'avg={sum_number/count_number:.2f}')
