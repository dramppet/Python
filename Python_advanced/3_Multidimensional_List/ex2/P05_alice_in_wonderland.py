size = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions_command = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"


while tea_bags < 10:
    directions = input()

    row = alice_pos[0] + directions_command[directions][0]
    col = alice_pos[1] + directions_command[directions][1]

    if not(0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"

    if position == "R":
        break

    if position == "." or position == "*":
        continue

    if position.isdigit():
        tea_bags += int(position)


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col],end = " ")
#     print()

[print(*row) for row in matrix]

