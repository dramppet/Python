import sys
n = int(input())

min_num = +sys.maxsize
max_num = -sys.maxsize
sum_num = 0

for _ in range(n):
    num = float(input())
    sum_num += num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f'min={min_num:.2f}')
print(f'max={max_num:.2f}')
print(f'sum={sum_num:.2f}')
print(f'avg={sum_num/n:.2f}')