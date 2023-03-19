import math

number = int(input())

bol_list = [False] * (number + 1)

for el in range(1, number + 1):
    isPrime = True
    res = int(math.sqrt(el)) + 1
    for divisor in range(2, res):
        if el % divisor == 0:
            isPrime = False
            break
    bol_list[el] = isPrime

    if isPrime:
        for e in range(1, el + 1):
            if bol_list[e] == True:
                print('1',end='')
            else:
                print('0',end='')
        print()