divisor = int(input())
border = int(input())

count = 0

for i in range(1,border + 1):
    if (i % divisor == 0) and (i <= border) and i > 0:
        if i > count:
            count = i

print(count)