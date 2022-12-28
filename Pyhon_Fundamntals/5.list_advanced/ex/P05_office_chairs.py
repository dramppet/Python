number_of_rooms = int(input())

chairs_need = True
free_chairs = 0
for room in range(number_of_rooms):
    line = input().split()
    chairs = len(line[0])
    visitors = int(line[1])

    if chairs < visitors:
        print(f'{visitors - chairs} more chairs needed in room {room + 1}')
        chairs_need = False
    else:
        free_chairs += chairs - visitors

if chairs_need:
    print(f'Game On, {free_chairs} free chairs left')

