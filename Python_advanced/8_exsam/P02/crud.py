SIZE = 6

matrix = []
coordinates = [0, 0]

for row in range(SIZE):
    line = list(input().split())
    matrix.append(line)

coordinates = input()

coordinate = [int(coordinates[1:2]), int(coordinates[4:5])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input().split(", ")
    row = coordinate[0]
    col = coordinate[1]

    if command[0] == "Stop":
        break

    if command[0] == "Create":
        pass

    elif command[0] == "Update":
        pass
    elif command[0] == "Delete":
        pass
    elif command[0] == "Read":
        pass
