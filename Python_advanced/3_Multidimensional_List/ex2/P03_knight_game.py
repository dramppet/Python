size = int(input())

matrix = [list(input()) for _ in range(size)]

position = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

remove_knight = 0

while True:
    max_attacks = 0
    knight_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in position:
                    post_row = row + pos[0]
                    post_col = col + pos[1]

                    if  0 <= post_row < size and 0 <= post_col < size:
                        if matrix[post_row][post_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_position = [row, col]
                    max_attacks = attacks

    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = "0"
        remove_knight += 1
    else:
        break

print(remove_knight)




