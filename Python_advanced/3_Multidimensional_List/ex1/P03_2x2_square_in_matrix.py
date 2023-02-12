rows, columns = list(map(int,input().split()))
matrix = [ input().split() for _ in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        symbols = matrix[row][col]

        if symbols == matrix[row][col + 1] and symbols == matrix[row + 1][col] and symbols == matrix[row + 1][col + 1]:
            equal_blocks += 1

print(equal_blocks)


