import sys

count_number = int(input())

max_num = - sys.maxsize
sum_num = 0

for _ in range(count_number):
    num = int(input())
    sum_num += num

    if num > max_num:
        max_num = num

sum_num -= max_num

if sum_num == max_num:
    print('Yes')
    print(f'Sum = {sum_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - sum_num)}')