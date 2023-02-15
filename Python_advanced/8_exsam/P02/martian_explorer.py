def move_rover(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row,col + 1
    if direction == "up":
        return row - 1,col
    if direction =="down":
        return row + 1,col

SIZE = 6

rover_row, rover_col = 0, 0
area = []

for row in range(SIZE):
    row_elements = input().split()
    for col in range(SIZE):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col
    area.append(row_elements)

directions = input().split(", ")





for direction in directions:
    rover_row, rover_col = move_rover(direction, rover_row, rover_col)
