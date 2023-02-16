SIZE = 6

matrix = []
coordinates = [0, 0]

for row in range(SIZE):
    line = list(input().split())
    matrix.append(line)

coordinates = *a

row = int(coordinates[0])
col = int(coordinates[1])

while True:
    command = input().split(", ")

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
