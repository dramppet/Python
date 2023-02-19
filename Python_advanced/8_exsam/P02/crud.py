SIZE = 6

matrix = []
coordinates = [0, 0]

for row in range(SIZE):
    line = list(input().split())
    matrix.append(line)

coordinates = input()

row  =int(coordinates[1])
col = int(coordinates[4])


while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    if command[1] == "up":
        row -= 1
    elif command[1] == "down":
        row +=1
    elif command[1] == "left":
        col -= 1
    elif command[1] == "right":
        col += 1

    if command[0] == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = command[2]
    elif command[0] == "Update":
        if matrix[row][col] != ".":
            matrix[row][col] = command[2]
    elif command[0] == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif command[0] == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])
[(print(*el))for el in matrix]
