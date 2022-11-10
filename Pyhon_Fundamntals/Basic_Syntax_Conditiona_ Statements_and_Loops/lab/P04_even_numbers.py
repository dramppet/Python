num = int(int(input()))

for _ in range(num):
    number = int(input())

    if not number %2 == 0:
        print(f'{number} is odd')
        break
else:
    print('All number are even')