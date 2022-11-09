size = int(input())
counter = 0

for row in range(1, size + 1):
    for col in range(1, row + 1):
        counter += 1

        print(f'{counter}',end = ' ' ) if row != col else print(f'{counter}')

        if counter == size:
            raise SystemExit
