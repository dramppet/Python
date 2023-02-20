def move_rover(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col


def out_side(row, col, SIZE):
    return row < 0 or col < 0 or row >= SIZE or col >= SIZE


def reposition_rover(row, col, SIZE):
    if row < 0:
        return SIZE - 1, col
    if row >= SIZE:
        return 0, col
    if col < 0:
        return row, SIZE - 1
    if col >= SIZE:
        return row, 0


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

water_found = False
metal_found = False
concrete_found = False

for direction in directions:
    rover_row, rover_col = move_rover(direction, rover_row, rover_col)

    if out_side(rover_row, rover_col, SIZE):
        rover_row, rover_col = reposition_rover(rover_row, rover_col, SIZE)

    cell_value = area[rover_row][rover_col]

    if cell_value == "W":
        water_found = True
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif cell_value == "C":
        concrete_found = True
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif cell_value == "M":
        metal_found = True
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif cell_value == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")

if water_found and metal_found and concrete_found:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')

