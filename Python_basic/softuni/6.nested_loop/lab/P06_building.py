floors = int(input())
rooms = int(input())

for flor in range(floors, 0, -1):
    for room in range(rooms):
        if flor == floors:
            print(f'L{flor}{room}', end=' ')
        elif flor % 2 != 0:
            print(f'A{flor}{room}', end=' ')
        else:
            print(f'O{flor}{room}', end=' ')
    print()