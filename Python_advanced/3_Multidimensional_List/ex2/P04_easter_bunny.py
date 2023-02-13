size = int(input())

pos_bunny = []
matrix = []
best_path = []

best_direction = None
max_collected_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        pos_bunny = [row, matrix[row].index("B")]


for direct,pos in directions.items():
    row, col = [
        pos_bunny[0] + pos[0],
        pos_bunny[1] + pos[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row,col])

        row += pos[0]
        col += pos[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = direct


print(best_direction)
print(*best_path,sep="\n")
print(max_collected_eggs)




