import math
from math import sqrt
n = int(input())
x = float(input())

sum_num = 0.0

for num in range(1,n + 1):
    print(f'{num} -> {sum_num}')
    sum_num += num / (math.pow(x,num -1))

print(f'{sum_num:.5f}')