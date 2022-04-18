number = int(input())

for num in range(2,1000):
    while number % num == 0:
        print(num)
        number /= num
