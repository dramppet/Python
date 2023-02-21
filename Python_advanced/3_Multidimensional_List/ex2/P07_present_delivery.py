def eat_cookie(present_left, nice_kids):
    for cordinates in directions_command.values():
        r = santa_pos[0] + cordinates[0]
        c = santa_pos[1] + cordinates[1]

        if matrix[r][c].isalpha():
            if matrix[r][c] == "V":
                nice_kids += 1
            matrix[r][c] = "-"
            present_left -= 1

        if not present_left:
            break
    return present_left, nice_kids

count_present = int(input())
size_neighborhood = int(input())

matrix = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions_command = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size_neighborhood):
    matrix.append(input().split())

    if "S" in matrix[row]:
        santa_pos = [row, matrix[row].index("S")]
        matrix[row][santa_pos[1]] = "-"

    total_nice_kids += matrix[row].count("V")

command = input()

while command != "Christmas morning":

    santa_pos = [
        santa_pos[0] + directions_command[command][0],
        santa_pos[1] + directions_command[command][1]
    ]

    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        count_present -= 1
    elif house == "C":
        count_present, nice_kids_visited = eat_cookie(count_present, nice_kids_visited)

    matrix[santa_pos[0]][santa_pos[1]] = "-"

    if not count_present or total_nice_kids == nice_kids_visited:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = "S"

if not count_present and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")

