size = int(input())

cruisers = 3
bombs_hit = 0

matrix = []
submarine_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))

    if "S" in matrix[row]:
        submarine_pos = [row, matrix[row].index("S")]
        matrix[row][submarine_pos[1]] = "-"

while cruisers:
    direction = input()

    r = submarine_pos[0] + directions[direction][0]
    c = submarine_pos[1] + directions[direction][1]

    submarine_pos = [r, c]

    if matrix[r][c] == "C":
        cruisers -= 1
    elif matrix[r][c] == "*":
        bombs_hit += 1

        if bombs_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            break

    matrix[r][c] = "-"

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[submarine_pos[0]][submarine_pos[1]] = "S"
[print(*r,sep='') for r in matrix]
