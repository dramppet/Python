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



