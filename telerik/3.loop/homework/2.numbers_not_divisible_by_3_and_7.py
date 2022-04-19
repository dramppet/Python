number = int(input())

for num in range(1, number + 1):
    if num % 3 == 0 or num % 7 == 0:
        continue
    print(num, end = ' ')