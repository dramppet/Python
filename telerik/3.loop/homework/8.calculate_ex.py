import math




n = int(input())
x = int(input())

calc_num = 0.0

def factNum(num):
    fact = 1

    for n in range(1,num):
        fact *= n

    return fact

for num in range(0,n):
    fact = factNum(num)
    div_num = math.pow(x,num)

    calc_num += fact / div_num

print(f'{calc_num:.5f}')