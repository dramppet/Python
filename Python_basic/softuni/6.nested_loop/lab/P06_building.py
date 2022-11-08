floor = int(input())
apartment = int(input())

for i in range(floor,0,-1):
    for j in range(apartment):
        if i == floor:
            print(f'L{i}{j}',end=' ')
        elif i % 2 != 0:
            print(f'A{i}{j}', end=' ')
        else:
            print(f'O{i}{j}', end=' ')
    print()